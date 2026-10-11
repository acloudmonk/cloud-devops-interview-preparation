# Advanced Database Architecture and Incident Drills

[← Scenario questions](scenarios.md) · [Next: Ten-minute database review →](presentation-template.md)

For each drill, state containment, evidence, correctness risk, durable correction,
recovery validation, communication, and residual risk.

## Drill 1 — Connection storm during regional failover

Throttle application restarts and retries, reserve connections for recovery, reset
stale pools, and protect the promoted writer. Inspect DNS/endpoint refresh, pool sizes,
timeouts, proxy behavior, unknown transactions, and authentication. Add global
connection budgets, jittered startup, bounded retry, health-based admission, and a
failover test with maximum application instances and realistic transactions.

## Drill 2 — Replica lag causes overselling

Route reservation and correctness reads to the authoritative transaction boundary,
pause unsafe order acceptance if required, and reconcile inventory and orders. Measure
commit/apply lag, long transactions, I/O, and read routing. Make the reservation
atomic, expose pending state, classify replica-safe reads, and alert on business
staleness rather than relying on an average lag metric.

## Drill 3 — Autovacuum or compaction falls behind

Control write volume and long transactions, protect disk headroom, and schedule safe
maintenance. Inspect dead versions/tombstones, transaction age, I/O, checkpoints,
index bloat, and workload changes. Tune based on measured churn, split oversized work,
remove blockers, and validate query latency, storage recovery, replicas, and backup
while maintenance catches up.

## Drill 4 — Hot partition throttles an otherwise idle table

Identify key and access skew, affected journeys, item size, secondary indexes, and
retry amplification. Apply admission or isolate the heavy cohort. Redesign the key,
write-shard with a controlled aggregation path, or create dedicated placement while
preserving required order and transactions. Migrate with dual evidence and validate
per-partition rate rather than total capacity.

## Drill 5 — Online schema change fills the transaction log

Pause or throttle the migration before storage or replica failure, preserve rollback,
and monitor recovery capacity. Inspect batch size, transaction duration, index work,
log retention, replication slots, and lag. Make backfill resumable with checkpoints,
small commits, adaptive rate, abort thresholds, and cleanup; test at production scale
including failover and point-in-time recovery.

## Drill 6 — Cache contains cross-tenant data

Bypass and purge affected keys, restrict access, preserve evidence, and activate
security/privacy response. Trace key construction, tenant context, authorization,
serialization, invalidation, and replicas. Use immutable verified tenant context,
namespaced/versioned keys, server-side authorization, safe TTL, and negative isolation
tests across every cache and derived store.

## Drill 7 — Point-in-time restore misses encryption keys

Preserve backups and halt key destruction, recover through approved escrow or versioned
key copies if available, and report actual recovery risk. Map key lifecycle to backup
retention, region/account isolation, access, and restore procedures. Exercise clean-
room recovery with primary-account compromise and verify data, roles, certificates,
extensions, and application startup—not only snapshot availability.

## Drill 8 — Query plan changes after statistics update

Capture old/new plans, parameters, estimates, runtime, locks, I/O, and data skew.
Stabilize with rollback, plan control, query rewrite, or index change according to
engine support. Improve statistics and representative tests, monitor plan hashes and
latency distributions, and avoid permanently pinning a plan without a review trigger
as data shape evolves.

## Drill 9 — CDC migration falls hours behind before cutover

Postpone cutover, protect source log retention, and identify throughput, large
transactions, schema incompatibility, target indexes, or network constraints. Scale
or tune safely, prebuild selectively, and measure catch-up rate. Rehearse drain,
validate counts/checksums/invariants and query behavior, then cut over only with
rollback capacity and reconciled errors.

## Drill 10 — Accidental delete replicates globally

Stop further destructive activity, revoke compromised access, preserve logs, and
select a recovery point. Replicas are not backups; restore an isolated copy, identify
valid changes after deletion, and merge or apply corrections with audit. Add least
privilege, just-in-time administration, deletion guardrails, immutable backup, PITR,
and exercises for partial logical recovery.

## Drill 11 — Shard rebalance saturates production I/O

Throttle or pause movement, reserve capacity for critical queries, and identify donor,
recipient, network, compaction, and log pressure. Rebalance smaller ranges during
headroom, prioritize hot shards, and enforce SLO abort conditions. Improve forecast
and placement so migration begins early; validate routing, counts, invariants, replica
health, backup, and old-range cleanup after each move.
