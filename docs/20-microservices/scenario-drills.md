# Advanced Microservices Architecture and Incident Drills

[← Scenario questions](scenarios.md) · [Next: Ten-minute architecture review →](presentation-template.md)

For each drill, state containment, evidence, failure classes, durable correction,
validation, communication, and residual risk.

## Drill 1 — Retry storm during dependency brownout

Protect the dependency with admission control, reduced concurrency, circuit breaking,
load shedding, and disabled nonessential retries. Trace where retries multiply and
preserve customer correctness. Add propagated deadlines, one deliberate retry layer,
budgets, jitter, idempotency, per-dependency bulkheads, and a load test that includes
brownout and recovery without synchronized retry waves.

## Drill 2 — Duplicate payment after consumer restart

Pause unsafe consumption, identify business/event IDs, compare provider and internal
records, refund or resolve through business policy, and notify owners. Fix consumer
state transition and idempotency atomically, retain deduplication evidence, and
replay a controlled range. Test crash before/after side effect and acknowledgment;
broker delivery guarantees alone cannot protect the external charge.

## Drill 3 — Outbox backlog silently grows

Preserve domain writes while declaring delayed downstream impact. Inspect relay
health, database contention, broker quota, poison records, and release changes.
Restore bounded publishing, monitor oldest-record age and throughput, isolate poison
messages, scale carefully, and verify consumers plus business convergence. Add SLOs,
alerts, replay controls, retention, and reconciliation.

## Drill 4 — Service discovery sends traffic to terminating instances

Drain traffic, reduce rollout pace, and restore healthy capacity. Correlate readiness,
deregistration delay, connection reuse, DNS/proxy cache, shutdown grace, and client
timeouts. Align lifecycle signals, stop accepting work before termination, complete
or requeue in-flight work, and test rolling updates under long connections and
dependency latency.

## Drill 5 — Event version breaks an old consumer

Stop or quarantine the incompatible producer/consumer path and preserve the event
log. Restore an additive compatible schema or translate at the boundary. Inventory
consumers and version use, add schema compatibility plus contract tests, support
overlap, and define replay/upcasting. Never mutate historical meaning or assume all
consumers deploy with the producer.

## Drill 6 — Distributed trace contains customer secrets

Restrict telemetry access, stop capture, preserve audit evidence, rotate exposed
credentials, and follow privacy response. Trace propagation should carry identifiers,
not payload secrets. Add field allowlists, redaction, sampling, retention, tenant-
aware access, and tests across gateways, SDKs, queues, logs, and vendors.

## Drill 7 — One database restore creates impossible business state

Pause workflows that could worsen divergence. Identify authoritative services,
restore points, events, and external records. Rebuild derived views and reconcile
orders, inventory, payments, and messages with idempotent repair. Define dependency-
aware RPO, coordinated recovery runbooks, replay boundaries, verification invariants,
and exercises; independent backups do not guarantee business consistency.

## Drill 8 — Service mesh rollout increases tail latency

Canary rollback or bypass affected traffic, compare proxy and application telemetry,
and inspect retries, mTLS, connection pools, resource limits, routing, and telemetry
export. Fix capacity/configuration and validate representative payloads and failure.
Keep business resilience in the application contract; mesh defaults must not add
hidden retries or make every request depend on an overloaded control plane.

## Drill 9 — Shared read model serves stale authorization data

Disable sensitive actions or query the authority directly, identify freshness and
revocation lag, and assess exposure. Authorization-critical state needs explicit
staleness bounds and fail behavior. Use event version/sequence, lag alerts, expiry,
revocation channel, and reconciliation; never treat an eventually consistent
projection as current authority without a documented risk decision.

## Drill 10 — Coordinated release train returns

Map why coordination is required: incompatible contracts, shared data, environment,
tests, ownership, or governance. Stabilize releases, then remove coupling through
additive contracts, private state, consumer tests, artifact independence, and team
authority—or merge services where cohesion demands it. Measure independent lead
time and failure isolation rather than repository or deployment count.
