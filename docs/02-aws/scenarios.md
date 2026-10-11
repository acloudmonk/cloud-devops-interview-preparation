# Scenario Questions and Model Answers

[← Design exercise](design-exercise.md) · [Next: Advanced drills →](scenario-drills.md)

Answer aloud before reading the model answer. Clarify, decide, explain failure and
operations, name evidence, and close with trade-offs.

## 1. Design the AWS foundation for 100 product teams

**Model answer:** I begin with regulation, isolation, ownership, delivery, network,
logging, and billing needs. I use a protected Organizations management account,
security and infrastructure OUs/accounts, separate production/nonproduction workload
accounts, sandbox and policy-staging areas, delegated administrators, federated access,
central immutable audit, account vending, and paved paths. SCPs restrict dangerous
possibility but do not grant access. The platform has service levels, versions,
exceptions, lifecycle, and adoption/flow metrics.

## 2. One large account or many small accounts

**Model answer:** Accounts are strong isolation, administration, quota, and billing
boundaries. I separate environments and workloads where blast radius, ownership,
policy, data classification, lifecycle, or billing justify it, while avoiding an
account per tiny component. I design cross-account identity, DNS, network, keys,
logging, deployment, support, and cost allocation. The decision follows policy and
operating boundaries, not an arbitrary account-count target.

## 3. Choose between EC2, ECS, EKS, Fargate, and Lambda

**Model answer:** I compare runtime/OS control, state, duration, latency, concurrency,
scaling, isolation, deployment, ecosystem, portability, networking/storage, skill,
limits, observability, and cost. Lambda fits bounded event-driven execution; Fargate
removes node operation; ECS gives AWS-native orchestration; EKS is justified by
Kubernetes needs and skill; EC2 maximizes host control. I model downstream capacity,
quotas, failure, and the operating team before standardizing.

## 4. The application must survive an Availability Zone failure

**Model answer:** I map every request and state dependency by AZ, distribute independent
compute and load balancing, verify database/storage topology, and remove single-AZ NAT,
endpoint, appliance, or node dependencies. I keep headroom for remaining AZs and test
zonal evacuation, scaling, connections, retry behavior, and data integrity. I include
cross-AZ transfer and latency in the trade-off. Merely selecting three subnets does not
prove availability.

## 5. Leadership requests active-active multi-Region for every workload

**Model answer:** I derive need from business impact, RTO/RPO, residency, and credible
Regional risk. I compare backup/restore, pilot light, warm standby, active/passive, and
active/active per journey. Active-active requires data authority/conflict semantics,
global routing, identity, keys, deployments, observability, quota, failback, and regular
testing. If those costs exceed value, I recommend a simpler tested recovery pattern
and document the residual risk.

## 6. Private subnets cannot reach an external API intermittently

**Model answer:** I trace DNS, route table, NAT gateway by AZ, security groups, NACLs,
firewall/proxy, return path, ephemeral ports, connection tracking, MTU, endpoint health,
and external limits. Flow Logs and NAT metrics distinguish route, reject, port, and
capacity hypotheses. I avoid cross-AZ NAT dependencies, add resilient egress paths as
required, and consider PrivateLink or provider endpoints when supported and justified.

## 7. An engineer receives AccessDenied despite an allow policy

**Model answer:** I identify principal/session, action, resource ARN, Region/account,
and request context, then evaluate trust policy, identity and resource policies,
permissions boundary, session policy, SCP/RCP, endpoint policy, KMS key policy, and
explicit denies. I use CloudTrail and policy simulation/access analysis where useful.
I fix the narrow cause and preserve least privilege; attaching administrator access
hides the authorization model and creates risk.

## 8. Lambda traffic exhausts database connections

**Model answer:** I protect the database first by limiting reserved concurrency or
event-source concurrency and applying backpressure. I inspect connection creation,
pool reuse, timeouts, transaction length, retries, and burst shape. RDS Proxy may help
compatible workloads, but I still budget connections across services and failure
conditions. I load-test scaling and degraded behavior and alarm on saturation and
business latency—not only invocation errors.

## 9. Select SQS, SNS, EventBridge, or Kinesis

**Model answer:** I choose from delivery pattern, consumers, ordering scope, retention,
replay, throughput, routing, source integration, and operations. SQS buffers work; SNS
pushes fan-out; EventBridge routes events by rules among integrated producers and
consumers; Kinesis provides retained partitioned streams. Combinations are common. I
define idempotency, schema, DLQ/redrive, backpressure, quotas, encryption, ownership,
and end-to-end delay.

## 10. An S3 bucket contains sensitive records used by analytics

**Model answer:** I classify and minimize data, use Block Public Access, tight bucket
and identity policies, organization/account conditions, encryption and deliberate KMS
administration, access logging/audit, VPC endpoint controls when justified, lifecycle,
retention/Object Lock if required, and Macie or equivalent discovery. Analytics roles
receive scoped column/object access and masked data where possible. I test deletion,
legal hold, restore, and key availability.

## 11. Backups are green, but no restore has been tested

**Model answer:** I treat recoverability as unproven. I map data dependencies and
application consistency, restore into an isolated account/environment, validate keys,
identity, network, DNS, quotas, configuration, integrity, performance, and business
journeys, and measure RTO/RPO. I distinguish replication from backup and protect
copies from the same compromise. Evidence and defects update runbooks, architecture,
and continuity decisions.

## 12. CloudWatch cost increases sharply

**Model answer:** I allocate by account, log group, metric, trace, source, and team;
identify ingestion, custom high-cardinality metrics, retention, verbose logs, queries,
and duplicate pipelines. I preserve security and SLO evidence while filtering at
source, sampling appropriately, setting retention/tiering, aggregating metrics, and
removing unused telemetry. Budgets and per-service telemetry cost ownership prevent
recurrence. Turning off visibility globally is not optimization.

## 13. A critical workload reaches an AWS service quota

**Model answer:** I stop unsafe scaling and protect service with throttling, admission
control, queues, or degradation. I confirm the exact quota scope—account, Region, AZ,
resource, API—and current utilization, scaling rate, and increase lead time. I request
adjustment if possible, redistribute only when semantics permit, and redesign hard
limits. Capacity and quota checks enter delivery gates, forecasts, alarms, and game
days.

## 14. How would you secure cross-account deployment

**Model answer:** The pipeline assumes a narrowly trusted deployment role using
short-lived credentials, explicit source and conditions, permissions boundaries where
useful, signed/versioned artifacts, protected approvals, and immutable audit. Build and
runtime roles are separate; production accounts do not trust arbitrary repositories or
users. Changes are policy-tested and staged, secrets are not copied into pipelines,
and break-glass/recovery works if the delivery system is impaired.

## 15. The cheapest Region lacks a required service feature

**Model answer:** I rank compliance, residency, user latency, availability, service
capability, dependencies, quotas, support, connectivity, skills, recovery, and total
cost. I compare another Region, alternative service, self-managed option, hybrid
placement, or delayed feature—with operational and exit consequences. Price alone does
not override required qualities. I document the decision and a trigger to reassess as
AWS capability or demand changes.

## 16. How do you conduct an AWS architecture review

**Model answer:** I define scope, business journeys, evidence, stakeholders, and risk
owners; map the architecture and dependencies; assess operational excellence,
security, reliability, performance, cost, and sustainability plus relevant lenses; and
validate claims with metrics, tests, configuration, incidents, and restore evidence. I
prioritize risks by business impact and likelihood, assign actions and due dates, and
record accepted trade-offs. A review is a learning and decision process, not a score.
