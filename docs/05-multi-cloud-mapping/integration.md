# APIs, Messaging, Events, and Workflows

[← Data platforms](data-platforms.md) · [Next: Delivery and IaC →](delivery-iac.md)

| Capability | AWS | Azure | Google Cloud |
| --- | --- | --- | --- |
| API management | API Gateway | API Management | Apigee / API Gateway |
| Queue | SQS | Service Bus queues | Cloud Tasks (targeted) / Pub/Sub patterns |
| Pub/sub and events | SNS, EventBridge | Service Bus topics, Event Grid | Pub/Sub, Eventarc |
| Streaming | Kinesis | Event Hubs | Pub/Sub with Dataflow patterns |
| Workflow | Step Functions | Logic Apps / Durable Functions | Workflows |

This table is deliberately many-to-many. Preserve producer/consumer ownership, schema,
protocol, fan-out, partition/ordering, delivery, deduplication, retry/backoff, dead
letters, retention, replay, flow control, transaction integration, and observability.

An “exactly once” label is scoped; end-to-end side effects still require idempotency
and reconciliation. Cross-cloud brokers add latency, egress, identity, certificate,
DNS, route, and outage coupling. Prefer local ingestion plus asynchronous replication
when it meets the business objective.

Use portable schemas and contract tests where they create value. Do not conceal native
semantics behind a generic wrapper that makes failure impossible to diagnose.
