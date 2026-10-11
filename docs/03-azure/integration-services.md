# APIs, Messaging, Events, and Workflows

[← Data platforms](data-platforms.md) · [Next: Service-selection matrices →](service-selection.md)

## Select interaction semantics first

Choose synchronous request/response, queue, publish/subscribe, event stream, grid, or
workflow from coupling, latency, throughput, ordering, replay, fan-out, transaction,
failure, and audit needs. Asynchrony introduces state and delayed failure; design it.

## Azure capability boundaries

- API Management publishes and governs APIs; gateway tiers and deployment models have
  distinct networking, scale, latency, feature, and availability characteristics.
- Service Bus supplies queues/topics with enterprise messaging capabilities such as
  sessions, transactions, scheduled delivery, and dead lettering by tier/feature.
- Event Grid routes discrete events to handlers with filtering and delivery behavior.
- Event Hubs ingests retained partitioned event streams for multiple consumers.
- Logic Apps orchestrates integration workflows; Durable Functions coordinates
  stateful code workflows with replay-aware programming constraints.

## Engineer delivery and ordering

Assume duplicate delivery where guarantees permit it. Use stable idempotency keys,
conditional writes, deduplication where available, outbox/inbox patterns, and
reconciliation. Ordering is scoped to an entity/session/partition and retries can alter
observed order. Define schemas, compatibility, ownership, correlation, and privacy.

## Control failure and backpressure

Set lock/visibility duration, acknowledgements, delivery counts, retry with jitter,
dead-letter handling, TTL, poison isolation, consumer concurrency, partitioning, and
downstream budgets. Monitor oldest event/message and business completion delay, not only
queue depth. Replay/redrive needs authorization, capacity control, idempotency, and
side-effect safety.

## Secure integration

Use managed identities where supported, scoped RBAC/data-plane permissions, private
endpoints or network controls where justified, encryption, schema/payload validation,
sensitive-data minimization, tenant isolation, diagnostics, and cross-subscription trust.
Do not embed secrets in messages or make the integration platform an unrestricted bus.
