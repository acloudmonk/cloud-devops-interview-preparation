# Rapid-Fire Revision

[← Ten-minute database review](presentation-template.md) · [Next: Active-recall flashcards →](flashcards.md)

Answer each aloud in one or two sentences, then add a trade-off or failure mode.

1. **What starts database selection?** Business invariants, data shape, and access patterns.
2. **What is a source of truth?** The authoritative system allowed to accept changes for a fact.
3. **What is polyglot persistence?** Purposeful use of multiple data models with explicit authority and synchronization.
4. **What is relational strength?** Transactions, constraints, joins, and flexible declarative queries.
5. **What is key-value strength?** Predictable low-latency access through known keys at scale.
6. **What is document-model strength?** Storing and atomically changing aggregate-shaped hierarchical data.
7. **What is a graph database for?** Relationship-centric traversal where edges are first-class.
8. **What is a search index?** A derived structure optimized for text, relevance, filtering, and facets.
9. **What is OLTP?** High-concurrency operational transactions over current business state.
10. **What is OLAP?** Historical analytical scans and aggregations, often columnar.
11. **What does atomicity mean?** Transaction effects commit together or not at all.
12. **What does isolation mean?** Concurrent transactions behave according to a defined visibility model.
13. **What does durability mean?** An acknowledged commit survives failures within the promised boundary.
14. **What is a dirty read?** Reading another transaction's uncommitted change.
15. **What is a lost update?** One concurrent write unknowingly overwrites another.
16. **What is write skew?** Snapshot transactions update different rows while violating a shared invariant.
17. **What is serializable isolation?** Concurrent outcome is equivalent to some serial transaction order.
18. **What is optimistic concurrency?** Detect conflict using version/compare-and-set and retry.
19. **What is pessimistic locking?** Prevent conflict by acquiring locks before change.
20. **What is MVCC?** Multiple row versions provide transaction snapshots and reduce reader/writer blocking.
21. **What is read-your-writes?** A session sees its own committed update on later reads.
22. **What is bounded staleness?** Reads may lag but only within an explicit time or version limit.
23. **Why can replicas be stale?** Asynchronous apply trails the authoritative writer.
24. **What is replication lag?** Difference in time or log position between source commit and replica apply.
25. **Is replication a backup?** No; it propagates accidental deletion and corruption too.
26. **What is an index?** Maintained auxiliary structure that trades write/storage cost for faster access.
27. **What is a composite index?** An ordered index over multiple fields whose order affects usability.
28. **What is a covering index?** An index containing everything a query needs without base-row lookup.
29. **Why inspect a query plan?** To see actual access, estimates, joins, sort/spill, pruning, and cost.
30. **What is selectivity?** How narrowly a predicate filters the dataset.
31. **What is an N+1 query?** One parent query triggers repeated per-row child queries.
32. **Why prefer keyset pagination?** It avoids growing offset scans and is steadier under change.
33. **What is expand/migrate/contract?** Compatible schema addition, data/code transition, then delayed removal.
34. **What is partitioning?** Dividing data by key/range for pruning, lifecycle, locality, or scale.
35. **What is sharding?** Distributing partitions across independently scaled nodes or clusters.
36. **What makes a good shard key?** Routing utility, distribution, locality, cardinality, and manageable growth.
37. **What is a hot shard?** One shard receives disproportionate bytes, operations, or expensive queries.
38. **What is scatter/gather?** A query fans out to many shards and merges results.
39. **What is resharding?** Moving data and routing to a new distribution scheme while preserving correctness.
40. **What is cache-aside?** Application loads the cache from authority after a miss.
41. **What is cache stampede?** Many clients regenerate the same expired or missing value simultaneously.
42. **What protects against stampede?** Coalescing, jittered TTL, soft expiry, warming, and bounded concurrency.
43. **What is a connection budget?** Maximum pooled application and operator connections below server capacity.
44. **Why can a proxy fail to multiplex?** Session or transaction state may pin a backend connection.
45. **What does a database timeout mean?** The client stopped waiting; commit outcome may be unknown.
46. **What is point-in-time recovery?** Restoring state to a selected time using backup plus transaction logs.
47. **What proves a backup?** An isolated timed restore with data and application correctness validation.
48. **What is RPO?** Maximum acceptable data-loss interval.
49. **What is RTO?** Maximum acceptable time to restore the business capability.
50. **What is CDC?** Capturing committed changes for replication, integration, or migration.
51. **What validates a migration?** Counts, checksums, invariants, query semantics, performance, and reconciliation.
52. **What is row-level security?** Database policy restricting rows based on trusted execution context.
53. **Why mask nonproduction data?** Test environments should not inherit unrestricted production sensitivity.
54. **What is a global-write trade-off?** Local write latency versus conflict/coordination and partition availability.
55. **What is a strong database answer?** It connects invariants and access paths to guarantees, operation, recovery, and cost.
