# Ten-Minute Azure Architecture Review

[← Advanced drills](scenario-drills.md) · [Next: Rapid-fire revision →](rapid-fire.md)

Use one minute per section. Lead with decisions and evidence, not a product catalog.

## 1. Outcomes and workload

State users, journeys, demand, data, SLOs, RTO/RPO, compliance, residency, delivery,
skills, support, and economic constraints.

## 2. Global placement

Explain geography, Region, zone, edge/hybrid placement, service scope, latency,
capacity, and why multi-Region is or is not justified.

## 3. Hierarchy and landing zones

Show tenant, management groups, subscriptions, resource groups, platform/workload
landing zones, Policy, exceptions, lifecycle, and responsibility boundaries.

## 4. Identity and security

Cover Entra, RBAC, managed identities, PIM, Conditional Access, keys, data protection,
Defender/Sentinel, emergency access, shared responsibility, and evidence.

## 5. Network and edge

Present address, routing, DNS, ingress, egress, private endpoints, hub/vWAN, Firewall,
hybrid paths, health, failure domains, telemetry, and transfer trade-offs.

## 6. Compute and delivery

Justify VMs, AKS, Container Apps, App Service, or Functions; explain scaling, state,
deployment, artifacts, rollback, capacity, quotas, and ownership.

## 7. Data and integration

Name sources of truth, storage/database choices, consistency, caching, analytics, API
Management, Service Bus/Event Grid/Event Hubs, workflows, idempotency, and recovery.

## 8. Reliability and operations

Show dependencies, degradation, Azure Monitor, alerts, incidents, support, backup,
restore, failover/failback, automation, and exercised evidence.

## 9. Capacity, economics, and review

Explain quotas, top meters, allocation, unit economics, optimization, commitments,
sustainability, and five-pillar Well-Architected risks.

## 10. Recommendation

Restate architecture, top trade-offs and risks, first delivery slice, evidence needed,
accountable owners, and conditions that would change the decision.
