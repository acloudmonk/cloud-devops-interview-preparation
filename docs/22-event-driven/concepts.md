# Asynchronous Architecture Decision Model

[← Module overview](index.md) · [Next: Patterns and platform selection →](patterns-platforms.md)

## Why introduce messaging?

Messaging can decouple availability, time, scale, and deployment. Producers can
record intent or facts while consumers operate independently and absorb bursts.
That benefit introduces new state: broker acceptance, delivery attempts, consumer
position, processing outcome, retries, duplicates, and business convergence.

Do not choose event-driven architecture merely because it is fashionable. Prefer a
direct synchronous call when the caller needs an immediate authoritative answer and
the dependency can meet the shared latency and availability contract. Prefer a
durable asynchronous boundary when work can complete later, burst buffering matters,
or independent subscribers need the same fact.

## Message meanings

- A **command** asks a named capability to perform an action and can be accepted or rejected.
- A **domain event** records a fact meaningful inside a bounded context.
- An **integration event** exposes a stable fact for external consumers.
- A **notification** signals that something changed, possibly requiring a follow-up read.
- A **document message** carries the state required by a consumer.
- A **stream event** is a record in an ordered, retained sequence used for ongoing computation.

Name facts in past tense and avoid disguised commands such as `OrderCreated` whose
only purpose is forcing a particular consumer action. Events are immutable statements;
correction is represented by a new event with lineage.

## Coupling does not disappear

Messaging reduces temporal and endpoint coupling but retains semantic, contract,
ordering, volume, privacy, and operational coupling. A producer owns event meaning;
the platform team owns broker capability; consumers own safe processing. Critical
business journeys require an explicit end-to-end owner even when no service calls
another directly.

## Discovery questions

Ask for business outcome, producer authority, expected consumers, volume and burst,
message size, latency and freshness, ordering scope, delivery tolerance, retention,
replay need, recovery objectives, privacy, residency, failure handling, and cost.
Define what the user sees while processing is pending or failed.

## Architecture decision record

Record message meaning, owner, destination, routing, partition key, schema, size,
durability, acknowledgment, retry, retention, replay, idempotency, authorization,
encryption, observability, capacity, recovery, cost, and deprecation. If any of these
are “broker default,” the business contract is probably underspecified.
