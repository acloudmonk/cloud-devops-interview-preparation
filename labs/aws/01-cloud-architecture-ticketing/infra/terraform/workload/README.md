# Workload Terraform

Implement the workload in reviewable modules rather than one large root module.

Suggested module order:

1. `network` — two or more AZs, routing, endpoints, and controlled egress
2. `data` — DynamoDB inventory, idempotency, and order state
3. `messaging` — SQS, DLQ, redrive, alarms, and policies
4. `compute` — ECR, ECS cluster, task definitions, services, and task roles
5. `edge` — ALB, CloudFront, WAF, S3 waiting room, and origin protection
6. `workflow` — Step Functions and payment-stub integration
7. `observability` — logs, metrics, dashboards, alarms, and notifications

Minimum quality gates:

```bash
terraform fmt -check -recursive
terraform init -backend=false
terraform validate
```

Also run a security scanner selected by the project and review an actual plan
before apply. Pin provider/module versions deliberately and commit the generated
`.terraform.lock.hcl`; only its backup is ignored.
