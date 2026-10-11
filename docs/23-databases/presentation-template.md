# Ten-Minute Database Architecture Review

[← Advanced drills](scenario-drills.md) · [Next: Rapid-fire revision →](rapid-fire.md)

Use this structure to present database reasoning before cloud product names.

## 0:00–1:00 — Authority and workload

State business facts, invariants, source of truth, access paths, volume/growth, skew,
latency, concurrency, geography, RPO/RTO, privacy, and team constraints.

## 1:00–2:15 — Data model and platform

Justify relational, key-value, document, graph, time-series, search, vector, object,
analytical, or combined models. Mark authoritative and derived stores.

## 2:15–3:30 — Transactions and consistency

Explain transaction boundary, isolation, concurrency, stale reads, idempotency,
cross-system workflow, acknowledgment durability, and reconciliation.

## 3:30–4:45 — Schema and access paths

Show schema/aggregate choices, indexes, top query plans, pagination, statistics,
maintenance, and expand/migrate/contract evolution.

## 4:45–6:00 — Scale and topology

Cover partitions/shards, key and skew, routing, replicas, write ownership, read policy,
conflict, headroom, resharding, and global latency.

## 6:00–7:00 — Cache and connections

State truth, TTL/invalidation, stampede behavior, cold-cache survival, pool budget,
proxy semantics, timeouts, failover reset, and retry boundary.

## 7:00–8:15 — Security and recovery

Explain workload/admin identity, tenant boundary, encryption, audit, residency,
retention/deletion, backup/PITR, isolated restore, validation, and clean-room access.

## 8:15–9:15 — Migration, operations, and cost

Present observability, capacity, maintenance, licensing, copy/CDC, validation, cutover,
rollback, retirement, and AWS-to-multi-cloud translation.

## 9:15–10:00 — Decision and risk

Restate the design, first milestone, measurable outcomes, top failure modes, residual
risk, and evidence that would cause the database decision to change.
