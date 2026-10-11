# Advanced SaaS Architecture and Incident Drills

[← Scenario questions](scenarios.md) · [Next: Ten-minute architecture review →](presentation-template.md)

For each drill, state containment, evidence, tenant impact, durable correction,
validation, customer communication, and residual risk.

## Drill 1 — Cross-tenant cache leak

Disable or bypass the affected cache, revoke exposed sessions if needed, preserve
evidence, and activate security/privacy response. Trace key construction, tenant
context, object authorization, replication, and logs to determine exposure. Fix keys
and server-side checks, purge all copies, add negative isolation tests and static
guardrails, then validate every cache tier and similar lookup path.

## Drill 2 — Tenant catalog routes traffic to the wrong cell

Stop catalog mutations and unsafe routing, fail closed where identity or residency is
uncertain, and restore the last verified mapping. Compare catalog version, cache age,
DNS/gateway state, workflow history, and cell ownership. Add monotonic configuration
versions, authenticated snapshots, atomic placement changes, reconciliation, and a
canary that verifies tenant-to-cell routing before accepting traffic.

## Drill 3 — Bulk tenant starves shared database connections

Protect critical journeys by reducing bulk concurrency, applying tenant limits, and
reserving capacity. Identify query, pool, lock, and tier behavior rather than merely
scaling compute. Implement fair scheduling, workload pools, bounded pagination,
backpressure, and product quotas. Validate mixed-size load, recovery, and that small
tenants receive predictable service during the large tenant's peak.

## Drill 4 — Federation certificate expires for one customer

Limit impact to the tenant, confirm emergency administrative access, and coordinate
certificate replacement through an authenticated channel. Inspect expiry monitoring,
metadata refresh, clock, and rollover overlap. Add proactive notification, support for
multiple valid keys, self-service validation, synthetic tenant sign-in, and a tested
break-glass path that does not bypass application authorization.

## Drill 5 — Metering replay doubles an invoice

Pause invoice finalization, preserve raw events and rating versions, and reconcile
source, ledger, aggregate, and invoice totals. Correct with traceable adjustment
records. Add deterministic idempotency, immutable event lineage, replay boundaries,
late-arrival policy, and pre-invoice controls. Test duplicates and partial batch
failure without using observability counters as financial truth.

## Drill 6 — Regional failover violates residency policy

Stop new writes into the disallowed location if safe, preserve availability according
to the explicit policy, and engage compliance and customer communication. Determine
which data, telemetry, backups, keys, and support paths moved. Redesign regional
recovery groups by policy, encode placement constraints, and exercise failover with
residency assertions rather than relying on a generic global DR runbook.

## Drill 7 — Deletion workflow remains incomplete for months

Identify affected tenants and data classes, honor legal holds, restrict stale copies,
and prioritize overdue deletion. Compare the manifest against databases, objects,
indexes, analytics, telemetry, third parties, and backups. Add ownership, deadlines,
durable workflow state, retries, dead-letter repair, tombstones, reconciliation, and
customer evidence. Test deletion after restore and event replay.

## Drill 8 — Feature flag outage disables premium access

Restore a last-known-good signed or authenticated entitlement snapshot and choose
fail behavior based on safety, not revenue intuition. Separate release flag, product
entitlement, authorization, and billing state. Add cache expiry rules, versioning,
local evaluation, audit, circuit breaking, reconciliation, and exercises for stale or
contradictory decisions without putting the provider in every request path.

## Drill 9 — Cell deployment breaks only legacy-schema tenants

Halt the ring, route or roll back affected tenants, and preserve database evidence.
Inventory software, schema, configuration, and migration status per tenant. Restore
expand/contract compatibility, make migrations resumable and observable, and enforce
maximum skew. Canary representative tenant shapes—not merely infrastructure—and
block rollout when tenant-level journey signals regress.

## Drill 10 — Support export exposes another tenant's audit rows

Remove access, preserve chain of custody, determine recipients and exposure, and
follow incident obligations. Trace support identity, query scope, export job, object
policy, link expiry, and audit evidence. Replace ad hoc queries with tenant-scoped
export APIs, dual authorization, short-lived delivery, content validation, watermark
or manifest, and automated cross-tenant negative tests.

## Drill 11 — A cell approaches hard service quotas

Freeze risky placements, shed optional work, reserve headroom, and prepare controlled
tenant moves. Measure the constraining quota and dependencies rather than average
utilization. Define cell capacity envelopes, forecast heavy hitters, automate placement
and evacuation, request quota increases early, and test migration with correctness,
metering continuity, rollback, and source cleanup.
