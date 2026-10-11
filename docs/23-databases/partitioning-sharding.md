# Partitioning, Sharding, and Scale

[← Replication and availability](replication-availability.md) · [Next: Caching and connection management →](caching-connections.md)

## Partition for a measurable reason

Partitioning divides data and work by key or range. It can improve pruning, retention,
maintenance, write throughput, or geographic placement. Sharding distributes partitions
across independent nodes or clusters, adding routing, rebalancing, cross-shard query,
transaction, and recovery complexity. Scale vertically and fix access paths before
introducing distribution that the workload does not require.

## Key properties

A good key supports dominant queries, distributes bytes and operations, preserves
needed locality, has adequate cardinality, avoids monotonic hot spots when harmful,
and supports placement/residency. Natural tenant keys may produce extreme skew. Hash
keys distribute point access; range keys support scans and locality; compound or
hierarchical keys can balance both with added design complexity.

## Hot partitions and scatter/gather

Observe per-partition rate, latency, storage, throttling, and key cohorts. A large
tenant, celebrity item, current timestamp, or low-cardinality status can dominate.
Queries without a routing key may contact every shard, increasing latency, cost, and
failure probability. Derived indexes or aggregate stores can serve global queries.

## Cross-shard operations

Joins, uniqueness, secondary indexes, counters, and transactions become coordination
problems. Scope invariants to one shard where possible. Globally unique identifiers
can be generated without a central database, but business uniqueness may still need
an authority. Distributed transactions are sometimes necessary; measure their
availability, latency, and recovery cost.

## Resharding

Plan before limits: destination schema, copy/change capture, checkpoints, validation,
dual-read/write or fencing, routing cutover, rollback, and source retirement. Rebalancing
consumes network, storage, I/O, and log retention. Throttle and monitor it against live
SLOs. Never discover the migration path only after one shard is full.

## Capacity model

Forecast records, bytes, indexes, versions/tombstones, backup, replicas, working set,
reads/writes, query fan-out, connections, and growth. Preserve headroom for failover,
rebuild, compaction, schema change, and rebalancing. Average utilization is unsafe when
one partition or fault domain has no remaining capacity.
