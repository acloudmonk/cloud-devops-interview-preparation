# Communication and Contracts

[← Domain and service boundaries](domain-boundaries.md) · [Next: Data ownership and consistency →](data-consistency.md)

## Choose interaction from business timing

Use synchronous request/response when the caller needs an immediate decision and
can tolerate dependency availability and latency. Use asynchronous messaging when
work can complete later, bursts need buffering, or producers and consumers should
be temporally decoupled. Async does not remove semantic coupling.

Avoid long synchronous chains. Each hop consumes latency budget and multiplies
failure probability. Aggregate at a boundary, move noncritical work async, cache
only with explicit staleness, or reconsider service granularity.

## Contract content

Define identity, intent, schema, validation, errors, idempotency, deadlines,
pagination, rate limits, ordering scope, delivery expectations, privacy, ownership,
version, deprecation, and examples. Events should name completed domain facts, not
vague notifications that make consumers query the producer immediately.

## Evolution

Prefer additive changes and tolerant readers. Never reuse a field with new meaning.
Test provider and consumer expectations, observe version usage, support overlap,
publish deadlines, and remove only after evidence. Event history and replay make
schema mistakes durable; upcasting or translation needs ownership.

## Gateway and discovery

Use an edge/API gateway for external authentication, routing, throttling, and stable
consumer boundaries. Internal discovery maps logical identity to healthy instances;
it does not solve authorization or resilience. Service mesh may standardize transport
security and telemetry but cannot decide business retries or idempotency.

## AWS-first mapping

Capabilities may use API Gateway/ALB, ECS/EKS/Lambda, Cloud Map, EventBridge, SNS,
SQS, or streaming services after requirements are known. Translate to Azure and
Google by interaction and operational semantics, not product-name equivalence.
