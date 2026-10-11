# Database Architecture Mock Interview

[← Mock interview overview](index.md) · [Module 23 overview](../23-databases/index.md)

Duration: **50 minutes**
Level: **Senior / Architect**
Primary context: **AWS-first global marketplace with multi-cloud consumers**

## Candidate brief

A marketplace stores catalog, inventory, orders, payments, carts, search, sessions,
audit, and analytics in one self-managed PostgreSQL cluster. Campaigns cause locks and
connection exhaustion, replicas expose stale inventory, search competes with checkout,
backups have never been restored, and schema changes block writes. Leadership asks to
move everything to NoSQL. Design the target data architecture and migration.

## Interview structure

### 0–7 minutes — Discovery and authority

Clarify business invariants, sources of truth, access patterns, size/growth, skew,
latency, throughput, concurrency, consistency, RPO/RTO, geography, residency, privacy,
retention, migration window, skills, and economics.

### 7–18 minutes — Models, transactions, and access paths

Select relational, key-value, document, search, cache, and analytical boundaries.
Explain transaction/isolation, concurrency, stale reads, schema, indexes, query plans,
pagination, connections, and derived-store synchronization.

### 18–28 minutes — Scale, topology, and recovery

Cover partition/shard key, skew, routing, replicas, read/write ownership, conflicts,
failover, caching, headroom, backup/PITR, isolated restore, tenant recovery, security,
encryption, audit, residency, lifecycle, and observability.

### 28–38 minutes — Failure branches

Choose three:

- checkout times out during database commit;
- replica lag causes inventory oversell;
- autoscaling exhausts database connections;
- an online schema change fills the transaction log;
- one tenant creates a hot shard;
- cache loss overloads the primary;
- accidental deletion replicates globally;
- failover completes but applications remain unavailable.

### 38–45 minutes — Platform and migration

Map requirements to Aurora/RDS, DynamoDB, ElastiCache, OpenSearch, and analytics;
compare Azure/Google dependencies and portable engines. Explain baseline copy, CDC,
validation, performance evidence, fencing, cutover, rollback, reconciliation, and
retirement.

### 45–50 minutes — Executive close

State recommended authoritative and derived stores, first migration slice, measurable
correctness/performance/recovery outcomes, major risks, cost/skill implications, and
evidence that could change the decision.

## Scoring rubric

| Dimension | Points |
| --- | ---: |
| Discovery, authority, invariants, and model choice | 9 |
| Transactions, consistency, and concurrency | 8 |
| Schema, query, indexes, cache, and connections | 8 |
| Partitioning, replication, global scale, and failure | 8 |
| Security, governance, backup, and recovery | 8 |
| Platform selection, migration, operations, and cost | 6 |
| Trade-offs and executive communication | 3 |
| **Total** | **50** |

Interpretation: **43–50** architect-ready; **35–42** strong with targeted gaps;
**25–34** incomplete correctness or recovery reasoning; **below 25** rebuild from
invariants and access paths. A product-first “all NoSQL” answer cannot exceed 34.

## Improvement loop

Record the three weakest decisions, revisit the matching pages and primary sources,
redraw authority and transaction/recovery boundaries, then repeat within seven days
using different failure branches.
