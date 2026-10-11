# Schema, Indexing, and Query Design

[← Transactions and consistency](transactions-consistency.md) · [Next: Replication, availability, and global data →](replication-availability.md)

## Model for invariants and access

Normalize to reduce update anomalies and enforce relational integrity; denormalize to
serve bounded access paths without costly joins. Documents should group data read and
changed together within size and contention limits. Every duplication needs an owner,
freshness target, update path, and reconciliation strategy.

## Indexes are maintained data structures

Indexes accelerate selected predicates, joins, sorting, uniqueness, or search by
trading write amplification, storage, memory, build time, and maintenance. Choose
columns/fields and order from actual query predicates and selectivity. Composite,
covering, partial, sparse, inverted, spatial, vector, or range-friendly indexes solve
different problems; one index does not optimize every condition.

## Query plan reasoning

Use execution plans and runtime evidence to examine access method, estimated versus
actual rows, join order, sort/spill, partitions scanned, index-only coverage, network,
and lock time. A slow query can reflect stale statistics, parameter skew, data growth,
missing or unused indexes, N+1 application behavior, contention, or insufficient I/O.
Do not add an index before identifying the limiting work.

## Pagination and bounded reads

Prefer keyset/seek pagination for large changing datasets when a stable unique order
exists. Offset pagination may scan and discard increasing rows and can duplicate or
skip results during concurrent change. Bound result size, time, memory, and query
complexity; protect the database from unrestricted reporting paths.

## Safe schema change

Use expand/migrate/contract: add compatible structures, deploy code that supports old
and new, backfill in bounded resumable batches, verify, switch reads/writes, observe,
then remove old structures after evidence. Separate metadata-only change from table
rewrite or index build behavior. Test locks, log growth, replicas, backup, and rollback.

## Statistics and maintenance

Query optimizers depend on current statistics and healthy data structures. Monitor
bloat/fragmentation, vacuum or garbage collection, compaction, checkpoints, index
usage, and plan regressions according to engine. Maintenance consumes I/O and can
interfere with production, so schedule and throttle using measurable headroom.
