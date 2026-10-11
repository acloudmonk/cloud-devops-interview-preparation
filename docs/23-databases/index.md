# Database Architecture

[← Curriculum overview](../curriculum/index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-11**
Level: **Senior / Architect**

Database architecture begins with business invariants, data shape, and access paths—not
with a vendor product. The design must explain transaction and consistency boundaries,
query performance, growth, failure, recovery, security, lifecycle, and operating cost.

!!! tip "Where to start"
    Start with **1. Database architecture decision model** and follow the numbered
    path. AWS is the primary cloud context, with PostgreSQL, Azure, Google Cloud,
    and portable-engine translations. This module requires no deployment lab.

## Learning objectives

- translate business invariants and access patterns into data-platform requirements;
- choose relational, key-value, document, wide-column, graph, time-series, search,
  vector, object, analytical, or combined models deliberately;
- explain ACID, isolation, MVCC, optimistic/pessimistic concurrency, and anomalies;
- design schemas, indexes, queries, statistics, and safe data evolution;
- distinguish replicas, quorum, failover, consistency, durability, backup, and DR;
- select partition and shard keys while reasoning about skew and resharding;
- use caches and connection pools without corrupting truth or causing overload;
- protect identities, data, keys, audit, privacy, retention, and administrative paths;
- prove backup, point-in-time recovery, tenant restore, migration, and reconciliation;
- compare AWS-first database capabilities with Azure, Google Cloud, and open systems.

## Recommended module path

### Phase 1 — Learn the data system

| Step | Page | Outcome |
| ---: | --- | --- |
| 1 | [Database architecture decision model](concepts.md) | Define authority, invariants, workload, and nonfunctional constraints |
| 2 | [Data models and platform selection](data-model-selection.md) | Select storage models from data shape and access patterns |
| 3 | [Transactions, consistency, and concurrency](transactions-consistency.md) | Protect invariants under concurrent and distributed change |
| 4 | [Schema, indexing, and query design](schema-index-query.md) | Design explainable access paths and evolvable schemas |
| 5 | [Replication, availability, and global data](replication-availability.md) | Choose topology, failover, read routing, and conflict behavior |
| 6 | [Partitioning, sharding, and scale](partitioning-sharding.md) | Distribute data with explicit key, skew, and migration decisions |
| 7 | [Caching and connection management](caching-connections.md) | Protect truth and databases from stale cache or connection storms |
| 8 | [Security, privacy, and governance](security-governance.md) | Secure access, data, keys, audit, lifecycle, and tenancy |
| 9 | [Backup, recovery, and migration](backup-recovery-migration.md) | Prove recoverability and move data without silent corruption |
| 10 | [AWS-first multi-cloud capability map](cloud-mapping.md) | Translate requirements across database services and engines |

### Phase 2 — Apply the reasoning

| Step | Page | Outcome |
| ---: | --- | --- |
| 11 | [Enterprise database design exercise](design-exercise.md) | Design an AWS-first global commerce data platform |
| 12 | [Scenario questions and model answers](scenarios.md) | Practise at least 15 senior database scenarios |
| 13 | [Advanced architecture and incident drills](scenario-drills.md) | Resolve at least 10 ambiguous data-system failures |
| 14 | [Ten-minute database architecture review](presentation-template.md) | Present authority, guarantees, performance, recovery, and cost |

### Phase 3 — Revise and assess

| Step | Page | Outcome |
| ---: | --- | --- |
| 15 | [Rapid-fire revision](rapid-fire.md) | Test at least 50 concise explanations |
| 16 | [Active-recall flashcards](flashcards.md) | Revisit at least 25 weak concepts |
| 17 | [Timed database architecture mock interview](../mock-interviews/database-architecture.md) | Complete a scored 50-minute assessment |
| 18 | [References and videos](references.md) | Deepen weak areas with authoritative sources |

## Scope boundary

[Microservices](../20-microservices/index.md) covers service data ownership,
[Event-Driven Architecture](../22-event-driven/index.md) covers outbox, streams, and
replay, and [HA/DR](../25-ha-dr-bcp/index.md) covers enterprise continuity. This module
focuses on database semantics, physical access, scaling, operation, and recovery.

## Completion checklist

- [ ] I can derive a database choice from invariants and access patterns.
- [ ] I can identify transaction isolation and stale-read anomalies.
- [ ] I can explain an index plan and its write/storage trade-offs.
- [ ] I can distinguish replicas, backups, and tested recovery.
- [ ] I can design a shard key and a safe resharding path.
- [ ] I can diagnose locks, connections, skew, lag, and cache inconsistency.
- [ ] I answered every scenario aloud and completed the scored mock interview.
