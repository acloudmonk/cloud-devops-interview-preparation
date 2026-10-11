# Enterprise Database Design Exercise

[← AWS-first multi-cloud map](cloud-mapping.md) · [Next: Scenario questions →](scenarios.md)

## Brief

A global marketplace stores catalog, inventory, orders, payments, carts, search,
sessions, audit, and analytics in one self-managed PostgreSQL cluster. Peak campaigns
cause lock waits and connection exhaustion. Search queries compete with checkout,
replica lag exposes stale inventory, backups have never been restored, and a schema
change blocked writes for 35 minutes. Leadership requests “move everything to NoSQL.”

## Constraints

- order and payment ledgers require explainable atomic state and near-zero RPO;
- inventory oversell must remain within explicit reservation policy;
- catalog reads are 100 times writes with flexible attributes and full-text search;
- traffic reaches 200,000 requests per second and is uneven by seller and product;
- customers require regional residency, tenant export, and provable deletion;
- analytics can lag minutes but cannot affect checkout capacity;
- RTO is 30 minutes, with quarterly recovery evidence;
- Azure receives fulfilment changes and Google Cloud hosts a recommendation workload.

## Candidate direction

Reject technology-first migration. Map invariants and access patterns. Retain a
relational authority for orders, payments, and tightly coupled inventory transactions
unless evidence justifies another model. Separate service ownership and bounded
schemas/databases. Create derived search and analytics stores through an outbox/CDC
path, and use a key-value or document model only for access patterns that benefit.

Design indexes and queries from top journeys, isolate reporting, bound connections
through pools/proxy, and make cache loss survivable. Partition or shard only after
measuring capacity and skew; choose keys with a resharding path. Route correctness-
critical reads according to lag and preserve user-visible pending state.

On AWS, evaluate Aurora/RDS, DynamoDB, ElastiCache, OpenSearch, and analytical services
by workload. Define workload identity, tenant policy, encryption, audit, residency,
retention, and safe administration. Use Multi-AZ/replicas for availability plus
separate backup/PITR and isolated restore tests for recovery.

Migrate in cohorts with schema compatibility, baseline copy, CDC, validation, shadow
reads, performance comparison, cutover fencing, rollback, reconciliation, and old-
authority retirement. Translate cross-cloud integrations asynchronously.

## Scored deliverable (50 points)

| Area | Points | Strong evidence |
| --- | ---: | --- |
| Workload, authority, and model choice | 9 | invariants, access paths, justified stores, minimal polyglot scope |
| Transactions and consistency | 8 | isolation, concurrency, stale reads, workflow, reconciliation |
| Schema, query, and performance | 7 | indexes, plans, evolution, connections, cache behavior |
| Scale, partitioning, and global topology | 8 | key/skew, routing, replicas, conflicts, headroom, migration |
| Security, privacy, and governance | 6 | identity, tenant, encryption, audit, residency, lifecycle |
| Availability, backup, and recovery | 7 | topology, RPO/RTO, PITR, isolation, restore verification |
| Migration, operations, and cost | 5 | CDC, validation, rollback, observability, skills, economics |

Score 40+ only when correctness and recovery are demonstrated under concurrency,
replica lag, failover, bad schema change, accidental deletion, and migration.
