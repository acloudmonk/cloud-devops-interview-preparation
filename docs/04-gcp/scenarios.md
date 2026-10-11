# Scenario Questions and Model Answers

[← Design exercise](design-exercise.md) · [Next: Advanced drills →](scenario-drills.md)

Answer aloud before reading. Clarify, decide, explain failure and operations, name
evidence, and close with trade-offs.

## 1. Design a foundation for 100 product teams

**Model answer:** I clarify regulation, identity, isolation, network, cost, and delivery
needs. I create a shallow folder model, platform and workload projects, automated
project vending, groups and federated identities, Organization Policy, Shared VPC where
justified, centralized evidence, and explicit platform/workload responsibilities.

## 2. One project or many

**Model answer:** Projects are trust, API, quota, lifecycle, and billing boundaries. I
separate environments or workloads when ownership, data, quota, policy, or blast radius
differs, while designing cross-project DNS, identity, network, keys, logs, and cost.

## 3. IAM, deny, or Organization Policy

**Model answer:** IAM allow grants actions; deny prevents permissions even with allows;
Organization Policy restricts configurations. I identify the failing decision engine,
inheritance, condition, principal, resource, and audit evidence instead of adding Owner.

## 4. Choose Compute Engine, GKE, Cloud Run, functions, or App Engine

**Model answer:** I compare OS control, protocol, state, duration, latency, scaling,
isolation, portability, limits, skills, and cost. I select the least operationally
complex platform that meets requirements and test quotas and downstream protection.

## 5. Survive a zone failure

**Model answer:** I classify every dependency by scope, distribute capacity and state
appropriately, retain remaining-zone capacity, remove zonal network/key dependencies,
and exercise loss while measuring SLO, data integrity, autoscaling, and operations.

## 6. Private managed service works in GCP but not on-premises

**Model answer:** I verify which private-access pattern the product uses, then trace DNS,
endpoint IP, advertised routes, VPN/Interconnect, firewall, return path, authorization,
and service perimeter from the failing client. I compare a working GCP path.

## 7. A service account has a role but access is denied

**Model answer:** I confirm the actual token principal, impersonation chain, permission,
scope, IAM conditions, deny, Organization Policy, VPC Service Controls, network path,
and audit logs. I grant only the required permission and avoid exported keys.

## 8. Cloud Run overwhelms Cloud SQL

**Model answer:** I cap instances/concurrency and buffer or throttle demand. I inspect
connection reuse, pool size, transaction/query latency, retries, and burst shape, then
load-test a connection budget and alert on saturation plus business delay.

## 9. Select Pub/Sub, Eventarc, Cloud Tasks, or Workflows

**Model answer:** Pub/Sub distributes events, Eventarc routes supported events, Tasks
controls deferred target delivery, and Workflows orchestrates steps. I decide from
fan-out, ordering, scheduling, rate, state, compensation, replay, and ownership.

## 10. Design global web ingress

**Model answer:** I select a global external Application Load Balancer where appropriate,
multi-region backends, health checks, CDN, Armor, DNS, certificates, capacity, and a
data strategy. I test backend/regional loss and distinguish edge availability from
application and state availability.

## 11. Restore after destructive data change

**Model answer:** I stop propagation, preserve evidence, identify a clean point, restore
into isolation, validate checksums and business invariants, reconcile later writes,
then cut over under change control. I record achieved RTO/RPO and fix the control gap.

## 12. Organization Policy blocks emergency recovery

**Model answer:** I identify the exact constraint and inheritance, compare the recovery
design with approved locations/services, and use a pre-authorized, time-bound exception
with logging and approval only if risk owners accept it. I redesign so emergency paths
are tested under normal guardrails.

## 13. Failover hits regional quota

**Model answer:** I inventory relevant quotas and actual capacity in advance, reserve or
request headroom, reduce optional demand, and test degraded capacity. During incident I
stabilize within safe limits and pursue escalation, not assume quota approval is instant.

## 14. Secure cross-project CI/CD

**Model answer:** I separate build, deploy, and runtime identities; use federation and
short-lived impersonation; scope roles to target resources; sign and scan artifacts;
promote immutable digests; gate policy; log approvals; and retain rollback evidence.

## 15. A required service is absent in the preferred region

**Model answer:** I verify current feature/SKU availability, data residency, latency,
egress, dependencies, and recovery. I compare another region, an alternative service,
or an isolated exception, document risk, prototype the critical path, and define an
exit trigger.

## 16. Lead a Well-Architected review

**Model answer:** I scope journeys and evidence, bring workload and platform owners,
review all six pillars, state risks as condition/failure/impact/evidence, rank them,
assign owners and acceptance criteria, track exceptions, and schedule re-review.
