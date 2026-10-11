# AWS-First Multi-Cloud Capability Map

[← Security and governance](security-governance.md) · [Next: Enterprise design exercise →](design-exercise.md)

Choose by semantics and operating model, not by service-name similarity. Verify
current quotas, delivery boundaries, ordering, retention, regional behavior, and
pricing in official documentation.

| Need | AWS anchor | Azure examples | Google Cloud examples | Portable option |
| --- | --- | --- | --- | --- |
| Durable work queue | Amazon SQS | Service Bus Queue, Queue Storage | Pub/Sub subscription, Cloud Tasks | RabbitMQ, NATS JetStream |
| Discrete pub/sub | Amazon SNS | Event Grid, Service Bus Topic | Pub/Sub | NATS, RabbitMQ |
| Content-routed event bus | Amazon EventBridge | Event Grid | Eventarc | Broker/router implementations |
| Retained event stream | Amazon MSK, Kinesis Data Streams | Event Hubs | Managed Service for Apache Kafka, Pub/Sub | Apache Kafka, Apache Pulsar |
| Workflow state | AWS Step Functions | Durable Functions, Logic Apps | Workflows | Temporal, Camunda |
| Schema/catalog | EventBridge Schemas, Glue Schema Registry | Schema Registry | Pub/Sub schemas | Apicurio, Karapace |
| Change data capture | Database-specific streams, DMS | Database/partner capabilities | Datastream | Debezium, Kafka Connect |

## AWS selection shortcut

Use SQS for load-leveled work and consumer-owned retries; SNS for simple push fan-out;
EventBridge for routed discrete events and service/SaaS integration; Kinesis for
AWS-native partitioned streams; MSK when Kafka protocol, ecosystem, retention, and
consumer-group semantics are required; Step Functions for explicit workflow state.
Combinations are normal—for example EventBridge routing to an SQS subscription.

## Important non-equivalences

Push versus pull, queue versus retained log, ordering key, acknowledgment, replay,
filtering, transactions, message size, DLQ, and regional replication differ. Google
Cloud Pub/Sub combines concepts differently from Kafka; Azure Event Grid is not Event
Hubs; SNS and EventBridge are not interchangeable. Translate the requirement, then
test failure and recovery behavior.

## Portability strategy

Standardize domain schemas, CloudEvents-style envelope where useful, identity intent,
observability, and business idempotency. Encapsulate provider clients behind small
adapters without erasing unique semantics. A lowest-common-denominator abstraction can
hide critical guarantees. Bridges need their own SLO, backpressure, duplicate,
ordering, security, replay, and reconciliation design.
