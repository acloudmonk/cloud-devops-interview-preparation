# Ten-Minute AWS Architecture Review

[← Advanced drills](scenario-drills.md) · [Next: Rapid-fire revision →](rapid-fire.md)

Use one minute per section. Lead with workload decisions and evidence, not a service
catalog.

## 1. Outcomes and workload

State users, critical journeys, demand, data, SLOs, RTO/RPO, compliance, residency,
delivery, skill, and economic constraints.

## 2. Global placement

Explain Region, AZ, edge or hybrid placement, service scope, latency, residency,
capacity, and why multi-Region is or is not justified.

## 3. Organization and governance

Show Organizations, OUs, accounts, landing-zone capabilities, delegated ownership,
guardrails, evidence, exceptions, and lifecycle.

## 4. Identity and security

Cover workforce/workload identity, authorization layers, keys, data classification,
detection, incident access, shared responsibility, and control evidence.

## 5. Network and edge

Present address, routing, DNS, ingress, egress, VPC endpoints, inspection, hybrid paths,
traffic policy, failure domains, telemetry, and data-transfer trade-offs.

## 6. Compute and delivery

Justify EC2, containers, serverless, or managed runtime; explain scaling, state,
deployment, supply chain, rollback, quotas, and team responsibility.

## 7. Data and integration

Name sources of truth, storage/database choices, transactions, consistency, caching,
analytics, APIs, queues/events/workflows, idempotency, replay, and recovery.

## 8. Reliability and operations

Show dependency budgets, degradation, observability, alerting, incident ownership,
backup/restore, failover/failback, automation, and exercised evidence.

## 9. Capacity and economics

Explain quota and capacity model, top pricing dimensions, allocation, unit economics,
optimization sequence, commitments, and sustainability decisions.

## 10. Recommendation

Restate the architecture, top trade-offs and risks, first delivery slice, evidence
needed, accountable owners, and conditions that would change the decision.
