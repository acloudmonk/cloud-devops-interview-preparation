# Advanced Event Architecture and Incident Drills

[← Scenario questions](scenarios.md) · [Next: Ten-minute architecture review →](presentation-template.md)

For each drill, state containment, evidence, guarantee boundary, durable correction,
validation, communication, and residual risk.

## Drill 1 — Retry storm overwhelms a recovered database

Pause or rate-limit consumers, disable unnecessary retries, preserve critical traffic,
and let the database recover below saturation. Correlate dependency errors, message
age, attempt count, concurrency, and deployment. Add end-to-end retry budgets, jitter,
backpressure, circuit breaking, bounded prefetch, and recovery ramp. Load-test both
failure and drain so queued work does not create a second outage.

## Drill 2 — Producer retry creates duplicate orders

Stop unsafe producers or consumers and identify event and business idempotency keys.
Compare accepted requests, domain records, outbox, broker, and external effects.
Repair with producer deduplication where supported, stable command identity, atomic
order creation, and consumer idempotency. Test lost acknowledgments and timeout-after-
commit rather than assuming the sender receives every success response.

## Drill 3 — Consumer group rebalances continuously

Stabilize membership and reduce rollout/concurrency churn. Inspect session and poll
timeouts, long handlers, network, resource pauses, partition assignment, and version
changes. Bound batch work, separate processing from polling where safe, use graceful
shutdown and cooperative assignment where supported, and verify duplicates, lag, and
state recovery during planned and unplanned membership change.

## Drill 4 — Schema registry is unavailable

Keep known compatible schemas and cached validation serving within a defined window;
pause publication of unknown versions rather than bypass governance blindly. Identify
whether serialization, validation, or only registration depends on the registry. Add
high availability, authenticated cache, version pinning, fail behavior, and recovery
reconciliation. Test that stale schemas cannot authorize an incompatible release.

## Drill 5 — Hot partition reaches days of lag

Protect correctness, expose affected entities, and isolate optional consumers. Measure
key distribution, payload, processing time, downstream calls, and retry amplification.
Reduce per-record work, allocate capacity, move heavy cohorts, or introduce a new
partitioning strategy with dual-run and state migration. Validate entity ordering,
consumer state, and live traffic while draining the backlog.

## Drill 6 — Replay sends millions of customer emails

Stop the consumer, revoke queued provider work if possible, preserve audit, and notify
incident owners. Determine replay range, consumer group, deduplication window, and
side-effect guard. Require replay plans, dry-run counts, isolated targets, approval,
rate limits, event-purpose controls, and durable business idempotency. Treat replay as
a production release, not an operator convenience.

## Drill 7 — Dead-letter re-drive loops immediately

Stop re-drive and preserve the failure cohort. Validate that the root cause, consumer
version, authorization, schema, and dependencies are actually fixed. Use a quarantine
state machine with diagnosis, transformation if governed, canary records, bounded
rate, attempt lineage, and abort threshold. Confirm the business outcome and remove
records only after successful convergence.

## Drill 8 — Broker reports healthy while checkout events vanish

Trace authoritative commit, outbox, relay, broker acknowledgment, route/filter,
subscription, consumer acknowledgment, and business state. Broker uptime cannot prove
end-to-end delivery. Restore the broken boundary, replay from durable evidence, and
add commit-to-effect SLOs, synthetic events, correlation, outbox-age alerts, and
reconciliation reports with clear producer and consumer ownership.

## Drill 9 — Cross-region replication reverses entity order

Fence concurrent writers or consumers for affected entities, identify source region,
sequence, replication lag, and conflict. Choose a home region, globally ordered key
strategy, or business conflict rule; multi-region transport alone cannot create total
order. Make consumers version-aware, reconcile divergence, and test failover while
records and effects are in flight.

## Drill 10 — Compromised connector exports an entire topic

Disable and isolate the connector, rotate credentials and keys, preserve audit, and
assess data exposure. Trace artifact, configuration, identity, topic permissions,
network egress, and payload classification. Scope connectors to destinations and
fields, isolate execution, pin/scan artifacts, control egress, use short-lived identity,
and alert on abnormal reads or offset resets.

## Drill 11 — Retention expires before a failed consumer recovers

Declare unrecoverable gap risk, freeze dependent decisions if correctness requires it,
and find authoritative sources, archives, outbox, or snapshots. Rebuild or reconcile
with explicit provenance. Set retention from worst-case detection and recovery time,
monitor lag against remaining retention, protect critical archives, and exercise a
consumer outage longer than the planned repair window.
