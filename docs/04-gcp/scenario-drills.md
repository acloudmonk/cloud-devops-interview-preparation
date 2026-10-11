# Advanced Architecture and Incident Drills

[← Scenarios](scenarios.md) · [Next: Presentation →](presentation-template.md)

For each drill state first evidence, stabilization, hypotheses, recovery, validation,
prevention, owner, and trade-off.

## 1. A new organization constraint blocks production recovery

Compare Policy Intelligence/effective policy and audit logs across working and failing
projects. Stabilize through the approved recovery route; use only a logged, expiring
exception. Then add pre-deployment policy tests and recovery-path conformance checks.

## 2. A zonal GKE capacity shortage blocks rescheduling

Inspect events, node pools, reservations, quotas, disruption constraints, and workload
requests. Protect critical workloads, shed optional demand, use approved alternate
zones/classes, then validate placement diversity and failure headroom.

## 3. Cloud NAT ports are exhausted

Correlate NAT metrics/logs with source endpoints and connection behavior. Reduce abusive
concurrency/retries, add approved address/port capacity, fix connection reuse, and alarm
on allocation pressure rather than only total traffic.

## 4. Private Service Connect name resolution differs by site

Query authoritative and recursive paths from each location. Verify zones, forwarding,
response policy, endpoint IP, routes, firewall, and return. Centralize ownership and add
synthetic resolution/connectivity tests from every network boundary.

## 5. CMEK access fails during a regional event

Identify key location, version state, IAM/deny, service agent, quota, and dependency.
Preserve data safety; recover through a pretested compatible path. Review whether the
key topology and emergency permissions meet the workload RTO.

## 6. Pub/Sub oldest-unacked age grows while CPU is low

Inspect delivery errors, flow control, poison messages, ordering keys, downstream
latency, quotas, and retry storms. Quarantine poison work, protect downstream systems,
scale the real bottleneck, and validate business completion after replay.

## 7. Cloud SQL fails over but the application remains unavailable

Check instance state, DNS/address use, connectors, pools, stale sessions, retry bounds,
and credentials. Drain/rebuild unhealthy pools, limit reconnect storms, validate writes,
then test failover routinely with realistic clients.

## 8. Shared VPC firewall change breaks many service projects

Use audit logs and connectivity tests to locate the effective hierarchical/VPC rule.
Roll back safely, protect critical flows, then add ownership, staged rollout, policy
tests, canaries, and blast-radius limits.

## 9. Multi-region application accepts conflicting writes

Stop unsafe writes, establish the authoritative record, reconcile with business rules,
and communicate impact. Redesign ownership, consistency, fencing/idempotency, and
failover so partitions cannot create silent corruption.

## 10. Daily cost doubles with stable demand

Use billing export to isolate project, SKU, location, and labels; correlate deployments,
logs, egress, retention, and idle capacity. Stop only confirmed waste, preserve SLOs,
and add anomaly ownership and unit-cost regression gates.

## 11. Workforce identity provider is unavailable

Test cached sessions and critical operations, activate controlled break-glass access,
increase monitoring, and postpone risky change. Afterward validate account custody,
alerts, rotation, minimal permissions, communications, and recurring exercises.
