# Landing-Zone and Platform Readiness

[← Strategies and target state](strategies-target-state.md) · [Next: Waves and migration factory →](waves-factory.md)

## A landing zone is an operating capability

It includes organization and account/subscription/project structure, identity,
network, DNS, security, logging, key management, policy, tagging, budgets, service
catalog, automation, observability, backup, incident response, quotas, support, and
ownership. A collection of accounts and networks is not sufficient.

## AWS-first readiness baseline

Establish AWS Organizations and account vending, IAM Identity Center/federation,
least-privilege roles, SCP guardrails, VPC/IP/DNS/egress patterns, connectivity,
CloudTrail and configuration evidence, Security Hub/GuardDuty integration, KMS and
secrets patterns, backup, Systems Manager, deployment pipelines, monitoring, cost
allocation, quotas, and support escalation. Validate Region/service availability and
data residency for each wave.

## Prove the path, not only the components

Run a representative workload through account request, connectivity, deployment,
certificate/DNS, secrets, logging, alerting, backup/restore, vulnerability handling,
incident escalation, cost attribution, and access review. Include on-premises and
partner paths. Record service-level objectives for platform capabilities.

## Readiness gate

Before a wave commits, confirm target capacity and quotas, production connectivity,
identity, controls, observability, backup/recovery, automation, support ownership,
change approvals, and tested exception handling. Temporary exceptions require scope,
risk owner, compensating control, expiry, and remediation plan.

## Avoid the two landing-zone traps

An underbuilt foundation pushes every team into unsafe custom work. An overcentralized
foundation becomes a queue that blocks delivery. Standardize high-risk, repeated
capabilities; provide paved paths and self-service; allow governed extension based on
clear boundaries and feedback.
