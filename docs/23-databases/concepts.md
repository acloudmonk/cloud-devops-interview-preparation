# Database Architecture Decision Model

[← Module overview](index.md) · [Next: Data models and platform selection →](data-model-selection.md)

## Begin with authority and invariants

Identify the authoritative owner of each fact and the rules that must never be broken:
no duplicate ledger posting, inventory cannot fall below policy, an email is unique
within a tenant, or an order total equals approved lines. Put strongly related
invariants inside one transactional boundary where possible. Cross-system rules need
workflow state, idempotency, and reconciliation rather than imagined global rollback.

## Describe the workload

Record data shape, entity and relationship cardinality, item/row size, total volume,
growth, retention, read/write ratio, access paths, query predicates, range and
aggregation needs, latency percentiles, throughput, burst, concurrency, geographic
distribution, and online versus analytical behavior. Include data skew and the largest
tenant/entity—not only averages.

## Nonfunctional constraints

- transaction scope, consistency, ordering, and acceptable staleness;
- availability, durability, RTO, RPO, and degraded behavior;
- privacy, residency, encryption, audit, retention, and deletion;
- change rate, schema evolution, portability, and team skill;
- maintenance, patching, observability, support, licensing, and total cost;
- migration window, rollback, verification, and legacy dependencies.

## Source of truth and derived stores

Name authoritative writes. Caches, search indexes, analytics stores, projections, and
read replicas are derived unless explicitly designed otherwise. Every derived store
needs freshness, rebuild, authorization, deletion, and fallback behavior. Polyglot
persistence is valuable only when ownership and synchronization remain explainable.

## Managed-service decision

Managed databases reduce infrastructure work but do not own schema, query, capacity,
connection, failover, data-quality, privacy, or recovery decisions. Compare control,
compatibility, extensions, maintenance, scaling, observability, lock-in, skills, and
cost. “Serverless” changes capacity and billing behavior; it does not remove limits.

## Database decision record

Capture model and engine, authoritative datasets, transactions, consistency, access
patterns, schema, indexes, partition key, replicas, read routing, caching, connections,
backup/PITR, restore evidence, encryption, identity, residency, observability, capacity,
cost, migration, exit strategy, risks, and conditions that trigger re-evaluation.
