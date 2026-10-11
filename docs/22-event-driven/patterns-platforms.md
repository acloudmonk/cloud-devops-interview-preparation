# Patterns and Platform Selection

[← Decision model](concepts.md) · [Next: Delivery, acknowledgment, and ordering →](delivery-ordering.md)

## Select the interaction model

| Model | Primary purpose | Important trade-off |
| --- | --- | --- |
| Work queue | One worker handles each task | Load leveling, retries, and task ownership |
| Publish/subscribe | Each subscription receives a fact | Independent fan-out and subscription durability |
| Event bus/router | Rules route discrete events | Flexible integration but hidden routing dependencies |
| Retained log/stream | Groups read ordered partitions and replay | High throughput and history with partition/state complexity |
| Workflow/orchestrator | Coordinates explicit multi-step state | Visibility and timeouts at the cost of central workflow ownership |
| Synchronous API | Immediate response from authority | Direct latency and availability coupling |

Competing consumers share work within one logical subscription. Separate consumer
groups or subscriptions represent independent processing interests. Creating a new
queue for every consumer can be valid, but destination sprawl needs ownership,
provisioning, retention, access, and cost governance.

## Event choreography versus orchestration

Choreography lets capabilities react to facts without a central coordinator. It works
well for optional reactions and simple flows but can hide the business journey across
many subscriptions. Orchestration makes workflow state, timeout, compensation, and
operator visibility explicit. It can become overly centralized if it owns domain
decisions that belong to services. Hybrid designs are normal.

## Broker selection criteria

Compare protocol and client support, push/pull model, queue and stream semantics,
ordering scope, retention, replay, filtering, transactions, partitioning, throughput,
message size, delay/scheduling, DLQ behavior, regional durability, replication,
security, observability, operational ownership, ecosystem, and cost. A checklist of
features is insufficient; rank the requirements for each message class.

## Payload and claim check

Keep messages bounded. Large payloads increase latency, retry cost, broker storage,
and privacy exposure. A claim-check pattern stores the payload in protected object
storage and sends an expiring reference plus integrity metadata. Consumers still need
authorization, lifecycle alignment, and handling for missing or expired objects.

## Avoid accidental request-response

Reply queues and correlation IDs can implement asynchronous request-response, but
they often recreate a distributed synchronous chain with harder timeouts and cleanup.
Use them when the conversation truly benefits from messaging; otherwise expose a job
resource or workflow state that callers can query or receive by callback.

## Bridge carefully

A bridge can connect clouds, protocols, or legacy brokers, but its guarantee is no
stronger than the weakest side. Define deduplication, ordering, transformation,
backpressure, security, observability, replay, and cutover. Avoid invisible cyclic
routes and never assume broker-specific transactions cross the bridge.
