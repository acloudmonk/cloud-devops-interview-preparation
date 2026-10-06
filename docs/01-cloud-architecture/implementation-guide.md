# AWS Implementation Guide

Last reviewed: **2026-10-04**

Estimated time: **12–20 hours for the core path**

This guide turns the [architecture lab](lab.md) into a staged implementation.
The companion workspace is `labs/aws/01-cloud-architecture-ticketing` in the
repository root.

!!! warning "Cost and access"
    Use a dedicated AWS sandbox, short-lived credentials, a budget alert, and
    project tags. Never assume free-tier eligibility. NAT gateways, load
    balancers, CloudFront, retained logs, and backups may continue to cost money.

## Phase 0: establish measurable requirements

Complete the assumptions, SLO, threat-model, and Architecture Decision Record
templates before provisioning. Calculate:

```text
arrival rate = concurrent users / admission window in seconds
request rate = arrival rate × requests per journey
required capacity = peak request rate × headroom factor
concurrency = request rate × average service time in seconds
```

Define percentile-based latency, availability, backlog age, reservation
correctness, RTO, and RPO. Identify the three assumptions most likely to change
the design.

**Exit evidence:** another reviewer can reproduce the estimates and challenge
the assumptions.

## Phase 1: prove correctness locally

Implement these contracts:

- `GET /events/{eventId}`
- `POST /reservations` with an `Idempotency-Key` header
- `GET /orders/{orderId}`
- worker handling order messages
- payment stub supporting success, decline, timeout, and unknown outcome

Use an atomic conditional transition for seat reservation. Store the
idempotency key, request fingerprint, status, and original response. Do not use
a read-then-write sequence for correctness.

```bash
cd labs/aws/01-cloud-architecture-ticketing
cp .env.example .env
docker compose up --build
curl http://localhost:8080/health
```

Run `python -m unittest discover -s tests -v` first. The completed local slice
contains the API, worker, payment stub, DynamoDB Local, LocalStack SQS/DLQ,
idempotency and concurrency tests, and a cross-platform smoke script. Its
README includes dispatch-outage and ambiguous-payment exercises.

Required tests:

1. Two concurrent callers compete for one seat; exactly one succeeds.
2. A request replay returns the original result without another message.
3. A payment timeout after acceptance enters reconciliation rather than charging again.
4. Work queued during a worker outage is processed after restart.

## Phase 2: provision the AWS core

Keep Terraform state bootstrap separate from workload resources. The workload
should create a two-AZ VPC, private ECS tasks, ECR, an ALB, DynamoDB, SQS with a
DLQ, task roles, security groups, logs, dashboards, and alarms.

```bash
cd labs/aws/01-cloud-architecture-ticketing/infra/terraform/workload
terraform init
terraform fmt -check -recursive
terraform validate
terraform plan -out=tfplan
terraform show tfplan
terraform apply tfplan
```

Do not commit `tfplan`, state, account-specific variable files, or credentials.

**Exit evidence:** tasks are healthy in two Availability Zones, have no public
IP, and the public endpoint can create then retrieve a synthetic order.

## Phase 3: protect the edge and control admission

1. Put CloudFront and AWS WAF before the origin.
2. Host a static waiting-room page in a private S3 origin.
3. Use a CloudFront Function to validate a short-lived signed admission token.
4. Route admitted traffic to the application and other traffic to the waiting room.
5. Add managed and rate-based WAF rules with logging that excludes tokens and PII.
6. Define the metric and operator procedure that opens or closes admission.

The old **Virtual Waiting Room on AWS** solution is discontinued. Use the
current [CloudFront visitor-prioritization guidance](https://aws.amazon.com/blogs/networking-and-content-delivery/visitor-prioritization-on-e-commerce-websites-with-cloudfront-and-cloudfront-functions/)
as the starting pattern.

**Exit evidence:** missing, expired, and modified tokens fail closed; valid
tokens reach the API; excessive request rates are constrained.

## Phase 4: implement durable order processing

Use SQS standard queues for load leveling and make consumers idempotent for
at-least-once delivery. Use Step Functions Standard for the visible saga:

1. validate order and idempotency;
2. conditionally reserve inventory;
3. authorize payment;
4. confirm on known success;
5. release inventory on known failure;
6. reconcile ambiguous payment results;
7. move exhausted failures to the DLQ.

Set visibility timeout beyond expected processing time. Scale workers using
backlog-per-task and message age, not only CPU.

**Exit evidence:** duplicates have no duplicate business effect, poison work
reaches the DLQ, and a worker outage drains within the recovery objective.

## Phase 5: secure and deliver

- Separate API and worker task roles and restrict them to named resources.
- Retrieve runtime secrets from Secrets Manager or Parameter Store.
- Encrypt data stores, queues, logs, and secrets where required.
- Redact tokens, identity, and payment information from logs.
- Use GitHub Actions OIDC to assume a narrowly scoped deployment role.
- Build immutable images tagged with the commit SHA and scan code, IaC, and images.
- Deploy to a test environment, run invariant tests, require approval, and retain rollback.

**Exit evidence:** secret scanning passes, no static AWS key exists, the threat
model is reviewed, and the previous task definition can be restored.

## Phase 6: observe customer outcomes

Emit structured logs with correlation and order IDs. Build a dashboard for
CloudFront, WAF, ALB, ECS, DynamoDB, SQS/DLQ, and purchase-journey metrics.
Page for fast user-impacting SLO burn or inability to process orders; use
ticket-level alerts for slow capacity and cost trends.

**Exit evidence:** trace one order across edge, API, queue, worker, workflow,
and final business state without exposing sensitive data.

## Phase 7: load and failure testing

Run smoke, baseline, ramp, spike, soak, and controlled breakpoint profiles.
Start locally with the included k6 script. Use
[Distributed Load Testing on AWS](https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/solution-overview.html)
only when workstation capacity is insufficient and after reviewing cost.

For each fault experiment define hypothesis, steady-state signal, blast radius,
stop condition, rollback, and observer. Begin with task termination, paused
workers, payment latency, and poison messages. AWS Fault Injection Service is
an advanced path after alarms and stop conditions work.

**Exit evidence:** admission prevents uncontrolled overload, invariants hold,
and recovery time is measured rather than estimated.

## Phase 8: recovery and regional extension

Recreate the stack from source, restore protected data, reconcile outstanding
work, and measure RTO/RPO. Only then evaluate multi-region serving with Route
53 or Global Accelerator, DynamoDB Global Tables, regional workflows, and
explicit write ownership.

Prove failover, failback, conflict behavior, residency, dependency isolation,
and reconciliation. Two deployed regional stacks alone are not active-active.

## Teardown

```bash
terraform plan -destroy
terraform destroy
```

Verify by project tag that no NAT gateway, Elastic IP, load balancer, CloudFront
distribution, ECS task, ECR image, DynamoDB table/backup/replica, queue, DLQ,
workflow, bucket/version, log group, dashboard, alarm, secret, KMS key, snapshot,
or state bootstrap resource remains. Record the final cost check and teardown
time without account identifiers.
