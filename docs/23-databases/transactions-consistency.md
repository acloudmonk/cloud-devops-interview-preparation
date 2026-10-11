# Transactions, Consistency, and Concurrency

[← Data models and platform selection](data-model-selection.md) · [Next: Schema, indexing, and query design →](schema-index-query.md)

## ACID and business correctness

Atomicity, consistency, isolation, and durability describe transaction behavior, but
the database cannot infer every business invariant. Constraints, transaction design,
and application logic express correctness. Keep transactions short, bounded, and free
of slow external calls. A committed transaction may still require asynchronous work.

## Isolation and anomalies

Know dirty reads, non-repeatable reads, phantoms, lost updates, write skew, and stale
replica reads. Isolation names vary by engine; validate actual behavior. Serializable
isolation provides a strong reasoning model but can abort transactions, so clients
need bounded retry and idempotency. Snapshot isolation can still permit write skew
when an invariant spans multiple records.

## Concurrency control

Pessimistic locking prevents conflicts by blocking, which can create waits and
deadlocks. Optimistic concurrency uses version/compare-and-set and retries conflicts,
which works well when contention is low. MVCC lets readers see snapshots while writers
create versions; vacuum/garbage collection, long transactions, and storage growth
remain operational concerns.

## Consistency choices

Define read-your-writes, monotonic reads, bounded staleness, causal consistency, or
linearizability according to the workflow. “Eventual” must include maximum tolerated
staleness and user behavior. Read replicas improve capacity and locality but can show
old data; route correctness-critical reads to an authority or use a session/version
token where supported.

## Distributed transactions and sagas

A database transaction across shards or systems adds coordination, latency, and
failure coupling. Use it when the invariant truly requires atomic commit and the
platform supports the needed availability. Otherwise model explicit intermediate
states, reservations, compensation, timeouts, idempotency, and reconciliation. A saga
does not restore history; compensation is a new business action.

## Durable acknowledgment

Understand write concern, quorum, log/WAL acknowledgment, replica policy, and failover
rollback. An application success response should match the promised durability. More
replicas do not help if acknowledgment occurs before data reaches the required fault
domains, and synchronous quorum can reduce availability during partition.
