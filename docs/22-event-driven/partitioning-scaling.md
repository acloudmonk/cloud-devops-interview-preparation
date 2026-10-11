# Partitioning and Consumer Scaling

[← Delivery and ordering](delivery-ordering.md) · [Next: Event contracts and schemas →](contracts-schemas.md)

## Partition key is a business decision

The key controls ordering, state locality, load distribution, and consumer parallelism.
Choose the smallest business entity requiring order while preserving an even-enough
distribution. A tenant key protects tenant ordering but can create a hot partition;
an order key scales better but cannot serialize all tenant activity.

## Capacity model

Estimate records per second, bytes per second, peak/burst factor, retention bytes,
replication, partition throughput, consumer processing time, target freshness, and
recovery drain rate. Required consumer concurrency is roughly arrival rate multiplied
by mean processing time, adjusted for variance and headroom. Scaling on CPU alone
misses queue age and partition lag.

## Consumer groups

Members of one group divide partitions or compete for messages, so adding consumers
beyond usable partitions may add no throughput. Separate groups provide independent
views and positions. Rebalancing can pause work or cause duplicate processing; use
cooperative assignment where supported, bounded processing, graceful shutdown, and
idempotency.

## Hot keys and skew

Observe throughput and lag by partition, key cohort, tenant, and handler. Remedies
include better semantic keys, isolating heavy tenants, splitting a key with an
aggregation stage, reducing work, or dedicating a stream. Random salting increases
distribution but sacrifices straightforward per-entity ordering and state locality.

## Backpressure

Queues buffer a burst; they do not erase a sustained capacity deficit. Bound producer
admission, consumer concurrency, in-memory prefetch, batch size, downstream calls,
and retries. Prioritize critical classes and shed optional work before every consumer
overloads the database. Track oldest-message age as well as depth or offset lag.

## Changing partition count

Increasing partitions can change key-to-partition mapping, disturb ordering assumptions,
move state, and create consumer rebalances. Treat repartitioning as a migration with
compatibility, state movement, observation, and rollback. Retention and replication
cost grow with topic and partition count, so “more partitions” is not free capacity.
