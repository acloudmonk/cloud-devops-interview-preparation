# Active-Recall Flashcards

[← Rapid-fire revision](rapid-fire.md) · [Next: References and videos →](references.md)

Cover the answer column and recall the design consequence as well as the term.

| # | Prompt | Recall answer |
| ---: | --- | --- |
| 1 | Source of truth | Authoritative write owner for a fact; derived stores reconcile from it. |
| 2 | Access pattern | Key/predicate, order, result, frequency, latency, consistency, and transaction scope. |
| 3 | Polyglot persistence | Multiple justified models with explicit authority and synchronization. |
| 4 | Relational fit | Cross-record invariants, joins, constraints, transactions, flexible queries. |
| 5 | Key-value fit | Known-key operations with predictable horizontal scale. |
| 6 | Document fit | Aggregate-shaped data read and changed together. |
| 7 | Serializable | Outcome equivalent to a serial order; conflicts may abort and retry. |
| 8 | MVCC | Snapshot reads over versions; long transactions and cleanup still matter. |
| 9 | Optimistic concurrency | Version/compare-and-set detects conflict and retries. |
| 10 | Read-your-writes | A caller sees its committed update despite replica routing. |
| 11 | Replica lag | Time/log distance from authoritative commit to replica apply. |
| 12 | Index trade-off | Faster selected reads for write, storage, memory, and maintenance cost. |
| 13 | Composite index | Field order determines supported prefix predicates and sort. |
| 14 | Query plan | Evidence of scans, estimates, joins, sorts, spills, pruning, and runtime. |
| 15 | Expand/migrate/contract | Compatible overlap, bounded backfill, verified switch, delayed removal. |
| 16 | Partition key | Determines placement, routing, locality, skew, and transaction scope. |
| 17 | Scatter/gather | Query contacts many shards, increasing latency and failure surface. |
| 18 | Resharding | Copy/change capture, validation, fencing, routing cutover, rollback, cleanup. |
| 19 | Cache-aside | Load cache on miss while database remains authority. |
| 20 | Cache stampede | Simultaneous misses overload the authority. |
| 21 | Connection budget | Sum of all pools and operators must remain below database capacity. |
| 22 | Unknown commit | Timeout does not prove rollback; check business state before retry. |
| 23 | Replication versus backup | Replicas serve availability; backups preserve historical recovery points. |
| 24 | PITR | Backup plus transaction history restores a selected prior time. |
| 25 | Restore test | Timed isolated recovery plus integrity, isolation, and application verification. |
| 26 | CDC migration | Baseline copy plus ongoing committed changes before cutover. |
| 27 | RPO | Maximum acceptable data loss. |
| 28 | RTO | Maximum acceptable capability restoration time. |
| 29 | Row-level security | Database-enforced row policy using trusted context. |
| 30 | Global multiwriter | Local writes add conflict and coordination complexity; define invariant ownership. |
