# Interaction Styles and Integration

[← API contracts](api-design-contracts.md) · [Next: Gateways →](gateway-management.md)

Choose the interaction from latency, coupling, network, scale, consumer diversity,
ordering, delivery, discoverability, and operational requirements.

| Style | Strong fit | Main cost or risk |
| --- | --- | --- |
| REST/HTTP | broad external compatibility and resource interactions | chattiness and weakly governed semantics |
| gRPC | typed low-latency internal calls and streaming | browser/proxy/tooling constraints |
| GraphQL | consumer-shaped reads across a governed graph | resolver cost, authorization, query abuse |
| Events/messages | temporal decoupling, fan-out, replay, burst absorption | duplicates, ordering, schema evolution |
| Webhook | outbound partner notification | delivery proof, replay, signing, endpoint quality |
| WebSocket | bidirectional near-real-time session | connection state, recovery, capacity |
| Batch/file | large scheduled exchange and legacy integration | freshness and reconciliation |

## Coupling rules

Avoid long synchronous chains across ownership or failure boundaries. Use deadlines,
bounded retries, idempotency, backpressure, and graceful degradation. Async delivery
does not remove contracts: define event identity, producer, schema, ordering scope,
retention, replay, privacy, and consumer compatibility.

## GraphQL and gRPC boundaries

For GraphQL, authorize resolved objects and fields, constrain depth/complexity,
prevent batching abuse, and observe resolver cost. For gRPC, manage deadlines,
status semantics, protobuf field evolution, reflection exposure, load balancing,
and browser translation deliberately.

## Webhook contract

Sign the raw request with timestamp and key identifier; verify before parsing,
reject stale replays, acknowledge quickly, queue processing, retry with backoff,
offer delivery history, and support secret/key rotation with overlap.

## Selection test

Explain why the chosen style improves the critical journey and how it fails. Using
multiple styles is valid when boundaries and operating ownership are explicit.
