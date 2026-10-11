# Ten-Minute Event Architecture Review

[← Advanced drills](scenario-drills.md) · [Next: Rapid-fire revision →](rapid-fire.md)

Use this structure to communicate semantics and business outcomes before products.

## 0:00–1:00 — Outcome and timing

State journeys, authorities, immediate versus eventual results, volume, burst,
freshness, consistency, loss/duplicate tolerance, and recovery objectives.

## 1:00–2:30 — Interaction model

Classify command, event, notification, and stream. Justify synchronous API, work queue,
pub/sub, event bus, retained log, workflow, or a combination.

## 2:30–4:00 — Guarantees and correctness

Trace producer commit, broker acknowledgment, delivery, consumer processing, effect,
and acknowledgment. Explain outbox, idempotency, ordering scope, version, and
reconciliation without an unqualified exactly-once claim.

## 4:00–5:15 — Scale and state

Show key, partition, consumer group, concurrency, skew, backpressure, capacity,
retention, offset/checkpoint, state store, late event, and recovery-drain model.

## 5:15–6:30 — Contracts and replay

Present envelope, schema ownership, compatibility, discovery, classification,
versioning, deprecation, replay isolation, and irreversible-effect protection.

## 6:30–8:00 — Reliability and operations

Cover retry taxonomy, DLQ repair, freshness SLO, telemetry, incident evidence,
regional recovery, bridge behavior, cost, and business convergence.

## 8:00–9:00 — Security and platform

Explain workload identity, authorization, encryption, tenant/privacy boundary,
connector trust, audit, AWS service selection, and multi-cloud non-equivalence.

## 9:00–10:00 — Decision and risk

Restate the design, migration sequence, measurable outcomes, top risks, residual
uncertainty, and evidence that would cause the decision to change.
