# Scenario Questions and Model Answers

[← Enterprise design exercise](design-exercise.md) · [Next: Advanced drills →](scenario-drills.md)

## 1. Leadership mandates Kafka for every integration

**Model answer:** I would classify each interaction by timing, ownership, fan-out,
ordering, replay, throughput, and operational skill. Kafka fits retained partitioned
streams, but a queue, event router, workflow, or synchronous API may better express
other needs. Standardize decision criteria, not one technology.

## 2. A database commit succeeds but event publication fails

**Model answer:** This is a dual-write gap. Persist publication intent in an outbox
with the domain transaction, relay at least once, monitor outbox age, and reconcile.
Consumers remain idempotent because the relay can duplicate. Change data capture is
another option when its ordering, schema, and ownership semantics are acceptable.

## 3. A team promises exactly-once payment processing

**Model answer:** Ask for the exact boundary. Broker transactions can couple selected
reads, offsets, and writes but not an external payment API. Use a stable payment
idempotency key, persist attempts, resolve timeout-after-success with provider status,
and reconcile ledger and order state before retrying.

## 4. Events for an order are processed out of sequence

**Model answer:** Verify producers, partition or message-group key, parallel handling,
retry path, and entity sequence. Route an order to one ordering scope, include version,
and make the consumer reject, buffer, or reconcile gaps. Do not demand global order
when only per-order transitions need serialization.

## 5. Adding consumers no longer reduces lag

**Model answer:** Compare usable partitions with group members, then inspect hot
partitions, processing time, downstream saturation, prefetch, batch, and rebalance.
Extra consumers beyond partitions are idle. Fix the limiting resource or partition
model and validate drain rate under representative skew.

## 6. One customer creates a hot partition

**Model answer:** Preserve only the ordering scope that business requires. Consider a
finer entity key, dedicated tenant stream, controlled subpartition plus aggregation,
or reduced work. Random salting may spread load but complicates order and state.
Apply tenant quota and observe skew before migration.

## 7. A poison message blocks a FIFO group

**Model answer:** Quarantine after bounded classified attempts, preserve group and
failure evidence, and decide whether later messages may safely proceed. Repair the
producer or consumer, then controlled re-drive in order. A DLQ is not success; verify
the business entity converges and alert on DLQ age.

## 8. A producer removes an event field

**Model answer:** Stop the incompatible release or restore the field. Inventory actual
consumers, maintain overlap, publish a new type only if meaning changes, and use schema
compatibility plus consumer contract tests. Historical events retain old semantics,
so replay/upcasting must be designed rather than rewritten.

## 9. Operations wants to replay six months of events

**Model answer:** Define source range, target groups, rate, schema interpretation,
deduplication, side-effect suppression, and abort criteria. Validate in an isolated
consumer or destination first. Protect live capacity and never replay blindly into
payments, emails, or partner calls.

## 10. Queue depth is stable but users report stale results

**Model answer:** Depth hides age, partition skew, poison groups, and processing
latency. Measure oldest age and commit-to-visible freshness by journey, then inspect
partitions, retries, outbox, consumer effect, and projection position. Alert on SLO
burn rather than only resource health.

## 11. A consumer crashes after charging but before acknowledgment

**Model answer:** Redelivery is expected. Use the same business idempotency key,
persist the attempt and known provider result, query ambiguous state, and reconcile.
Only acknowledge after the local durable decision. Deduplicating event IDs alone may
not protect the external provider effect.

## 12. Personal data was placed in a long-retention topic

**Model answer:** Stop further publication, restrict access, determine exposure and
copies, and follow privacy response. Prefer minimal or tokenized events or claim check,
align retention and keys, and propagate correction/deletion to projections and
archives. Immutable does not remove legal obligations.

## 13. A DLQ contains 20 million records

**Model answer:** Protect capacity and evidence, classify failure cohorts, and identify
the first cause rather than mass re-drive. Fix schema, dependency, authorization, or
code by cohort; replay at bounded rate with idempotency and progress checkpoints.
Add DLQ arrival/age ownership, retention, and automated repair tests.

## 14. A cross-cloud bridge is duplicating events

**Model answer:** Treat at-least-once delivery as normal across the bridge. Preserve
stable IDs and business versions, make destinations idempotent, and inspect source
acknowledgment, bridge checkpoints, retry, failover, and transformation. Document
ordering and RPO as the weakest combined path, then reconcile both sides.

## 15. A consumer silently skipped unknown event types

**Model answer:** Unknown types should be observable and governed. Quarantine or
ignore only according to explicit subscription policy, alert on unexpected producer/
schema, and preserve the record for repair. Fix routing/catalog ownership and add
contract tests; silently acknowledging unknown required work causes loss.

## 16. A region fails with consumers behind

**Model answer:** Determine committed producer records, replicated log position,
consumer offsets, in-flight effects, and RPO. Fence duplicate active consumers,
restore destinations, schemas, keys, and checkpoints, then resume idempotently.
Reconcile business state; broker recovery alone does not prove complete processing.
