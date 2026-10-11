# Active-Recall Flashcards

[← Rapid-fire revision](rapid-fire.md) · [Next: References and videos →](references.md)

| # | Prompt | Answer |
| ---: | --- | --- |
| 1 | Microservices decision loop | Business change, domain, team, lifecycle, distributed cost, evidence |
| 2 | Modular monolith default | Explicit modules preserve simple transactions while boundaries mature |
| 3 | Boundary signals | Cohesion, invariants, ownership, change, scale, security, lifecycle |
| 4 | Distributed-monolith symptom | Services coordinate releases, share data, call synchronously, and fail together |
| 5 | Sync selection | Immediate decision needed and dependency budget is acceptable |
| 6 | Async selection | Delayed completion, buffering, fan-out, or temporal decoupling is valuable |
| 7 | Contract evolution | Additive changes, tolerant readers, tests, overlap, usage evidence, retirement |
| 8 | Private data rule | Only owning service accesses schema; others use API, event, or read model |
| 9 | Consistency statement | Invariant, authority, intermediate state, convergence bound, failure, repair |
| 10 | Transactional outbox | Commit domain change and event intent together, then publish |
| 11 | Consumer safety | Stable event ID, idempotent state transition, ordering scope, reconciliation |
| 12 | Saga | Local transactions plus explicit progress and business compensation |
| 13 | Materialized view | Derived read model with source, freshness, rebuild, and deletion behavior |
| 14 | Timeout-after-success | Caller times out after remote effect; query by idempotency key before retry |
| 15 | Resilience set | Deadline, bounded retry, jitter, circuit, bulkhead, admission, shedding |
| 16 | Overload objective | Preserve correctness and recovery capacity before maximizing accepted work |
| 17 | Workload identity | Short-lived scoped role per service/runtime, not shared static keys |
| 18 | Service authorization | Owning service validates actor, action, resource, tenant, and current policy |
| 19 | Test portfolio | Unit, component, contract, integration, selected end-to-end, production canary |
| 20 | Safe schema change | Expand, migrate, verify overlap, then contract |
| 21 | Journey observability | Correlated metrics, logs, traces, events, deploys, and business state |
| 22 | Recovery proof | Restore authorities, rebuild views, replay safely, reconcile side effects |
| 23 | Service ownership | Code, contract, data, SLO, on-call, cost, lifecycle, retirement |
| 24 | Strangler flow | Observe, isolate, translate, route a slice, transfer authority, retire old path |
| 25 | Success evidence | Less coordination and safer independent change with acceptable system cost |
