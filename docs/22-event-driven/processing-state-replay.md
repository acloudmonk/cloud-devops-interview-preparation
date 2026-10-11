# Processing State, Replay, and Consistency

[← Event contracts and schemas](contracts-schemas.md) · [Next: Resilience and operations →](resilience-operations.md)

## Idempotent consumer

Define the business effect that must not repeat. Use event ID for delivery duplicate
detection and business key/version for semantic duplicate protection. Store processed
evidence with the local state change when possible. Keep deduplication retention at
least as long as redelivery and replay risk; otherwise an old event becomes “new.”

## Outbox and inbox

A transactional outbox commits domain state and publication intent together, then a
relay publishes at least once. Monitor oldest outbox age, relay failures, poison rows,
and broker acknowledgment. An inbox can atomically record consumption with local
state. Both reduce dual-write gaps but still require cleanup, replay, and reconciliation.

## Projections and CQRS

Consumers can build purpose-specific read models from events. Store source position,
schema/version handling, and projection generation. A projection is derived and may
be rebuilt, but its staleness and authorization still affect users. Validate business
invariants after rebuild rather than trusting a completed offset alone.

## Replay as a production change

Specify source range, target consumers, rate, ordering, schema interpretation, side-
effect suppression, deduplication, and abort conditions. Replaying into email, payment,
or partner consumers can repeat irreversible effects. Prefer a new consumer group or
isolated destination for validation before controlled promotion.

## Event time and processing time

Event time reflects when a fact occurred; processing time reflects when a processor
saw it. Streaming windows need watermark and lateness policy. Late data may update,
correct, or be rejected from a result. Clock quality and producer timestamp trust must
be explicit, especially for devices and cross-organization sources.

## Event sourcing boundary

Event sourcing stores domain state as an ordered event history and reconstructs an
aggregate by replay. It requires invariant ownership, snapshots, version/upcasting,
privacy strategy, tooling, and operational skill. A broker log is not automatically a
domain event store, and event sourcing is not required for ordinary integration events.

## Reconciliation

Correct systems assume gaps and drift are possible. Compare authoritative state,
outbox, broker, consumer position, projection, and external side effects. Build safe
repair commands, auditable correction events, and business reports. Reconciliation
is the final correctness layer when transactional boundaries end.
