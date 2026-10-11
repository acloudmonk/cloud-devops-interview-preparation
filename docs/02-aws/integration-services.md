# APIs, Messaging, Events, and Workflows

[← Data platforms](data-platforms.md) · [Next: Service-selection matrices →](service-selection.md)

## Select the interaction model first

Choose synchronous request/response, queue, publish/subscribe, event stream, event bus,
or workflow from coupling, latency, throughput, ordering, replay, fan-out, transaction,
failure, and audit needs. Asynchrony moves failure; it does not remove it.

## AWS capability boundaries

- API Gateway exposes managed REST, HTTP, and WebSocket APIs with defined limits.
- SQS buffers work; standard queues favor scale and at-least-once delivery, while FIFO
  adds ordering/deduplication within explicit constraints.
- SNS pushes messages to multiple subscribers and can combine with SQS for isolation.
- EventBridge routes events among producers, consumers, SaaS, and scheduled sources.
- Kinesis retains ordered records within shards for streaming and replay.
- Step Functions coordinates workflows with explicit state and service integrations.

## Engineer delivery semantics

Assume duplicates where delivery is at least once. Use stable idempotency keys,
conditional writes, deduplication windows, transaction/outbox patterns, and
reconciliation. Ordering is scoped—often to a queue group, partition, or shard—and
retries can change observed order. Define schema compatibility and event ownership.

## Control failure and backpressure

Set visibility timeouts, acknowledgement behavior, retry limits, exponential backoff
with jitter, dead-letter handling, redrive, poison-message quarantine, consumer
concurrency, and downstream budgets. Monitor age and end-to-end business delay, not
only queue depth. Replays require authorization, capacity controls, and side-effect
safety.

## Secure integrations

Apply producer/consumer identity, resource policies, encryption, private connectivity
where justified, schema and payload validation, sensitive-data minimization, tenant
isolation, logging, and cross-account trust. Avoid embedding credentials in messages
or treating an event bus as an unrestricted enterprise network.
