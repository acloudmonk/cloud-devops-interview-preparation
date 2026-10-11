# Ten-Minute Microservices Architecture Review

[← Advanced drills](scenario-drills.md) · [Next: Rapid-fire revision →](rapid-fire.md)

## Minute 0–1 — Outcome and decision

State business change, current constraint, alternatives, and why service boundaries
are or are not justified.

## Minute 1–3 — Domain and ownership

Show bounded contexts, language, invariants, service granularity, teams, authority,
and what remains in a modular monolith.

## Minute 3–5 — Interaction and data

Walk one sync request and one async workflow: contracts, deadlines, events, private
data, saga/outbox, read models, idempotency, and reconciliation.

## Minute 5–7 — Security and failure

Explain user/workload identity, authorization, tenant/data controls, overload,
dependency failure, degradation, recovery, and regional assumptions.

## Minute 7–9 — Delivery and operations

Cover compatibility, tests, progressive release, observability, SLOs, ownership,
incident response, backup/restore, and cost.

## Minute 9–10 — Migration and trade-offs

Recommend the next strangler slice, evidence, rollback/retirement, residual risk,
multi-cloud boundary, and condition that would favor merging rather than splitting.
