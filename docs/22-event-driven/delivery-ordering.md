# Delivery, Acknowledgment, and Ordering

[← Patterns and platforms](patterns-platforms.md) · [Next: Partitioning and consumer scaling →](partitioning-scaling.md)

## Follow the message boundary by boundary

Separate producer creation, network send, broker acknowledgment, broker durability,
delivery to a consumer, processing, external side effect, and consumer acknowledgment
or offset commit. A platform guarantee at one boundary does not automatically cover
the entire business effect.

## Delivery semantics

- **At-most-once:** loss is possible, but the platform does not deliberately redeliver.
- **At-least-once:** accepted messages are retried, so consumers must expect duplicates.
- **Exactly-once within a defined system:** transactions or deduplication can atomically
  couple selected broker reads and writes; external APIs and databases remain outside
  unless they participate in that exact boundary.

State the scope rather than claiming “exactly once.” For a payment, use a stable
business idempotency key, persist outcome, query ambiguous provider state, and
reconcile; no broker slogan prevents a duplicated external charge.

## Acknowledgment timing

Acknowledging before durable business work risks loss. Acknowledging after the effect
permits redelivery if the consumer crashes in between. Make the effect idempotent or
commit processing evidence atomically with local state. Tune visibility or lease time
for work duration and extend it carefully; an expired lease can create concurrent work.

## Ordering

Global ordering limits parallelism and is rarely required. Define the entity whose
transitions must be serialized—order, account, device, or tenant—and use that key for
an ordered group or partition. Events for different keys can progress concurrently.

Even when the broker delivers in order, retries, multiple producers, consumer
parallelism, failover, and external writes can produce stale effects. Include entity
version or sequence and make consumers reject, buffer, or reconcile gaps and late
records according to business rules.

## Producer correctness

Use stable event IDs, business keys, schema/type/version, occurrence and publication
times, correlation and causation, producer identity, and trace context. Retries need
bounded exponential backoff with jitter. A successful database commit followed by a
failed publish is a dual-write problem; solve it with an outbox or change capture,
not an unbounded retry inside the request.
