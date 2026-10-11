# Messaging and Event-Driven Architecture References and Videos

[← Active-recall flashcards](flashcards.md) · [Module overview](index.md)

Verify current guarantees, quotas, ordering, retention, regional behavior, pricing,
and support in official documentation before production decisions. Delivery claims
must always name their boundary.

## Suggested reading order

1. [AWS decision guide: Amazon SQS, SNS, or EventBridge](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/sns-or-sqs-or-eventbridge.html)
2. [Azure asynchronous messaging options](https://learn.microsoft.com/azure/architecture/guide/technology-choices/messaging)
3. [Google Cloud event-driven architecture with Pub/Sub](https://docs.cloud.google.com/solutions/event-driven-architecture-pubsub)
4. [Apache Kafka introduction](https://kafka.apache.org/documentation/)
5. [AWS transactional outbox pattern](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html)

## AWS architecture anchor

- [Amazon SQS Developer Guide](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html)
- [Amazon SNS Developer Guide](https://docs.aws.amazon.com/sns/latest/dg/welcome.html)
- [Amazon EventBridge User Guide](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html)
- [Amazon Kinesis Data Streams introduction](https://docs.aws.amazon.com/streams/latest/dev/introduction.html)
- [Amazon Managed Streaming for Apache Kafka](https://docs.aws.amazon.com/msk/latest/developerguide/what-is-msk.html)
- [AWS Step Functions Developer Guide](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html)
- [AWS Prescriptive Guidance: publish-subscribe pattern](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/publish-subscribe.html)
- [AWS Builders' Library](https://aws.amazon.com/builders-library/)

## Patterns, contracts, and streaming

- [Azure publisher-subscriber pattern](https://learn.microsoft.com/azure/architecture/patterns/publisher-subscriber)
- [Azure competing consumers pattern](https://learn.microsoft.com/azure/architecture/patterns/competing-consumers)
- [Azure messaging bridge pattern](https://learn.microsoft.com/azure/architecture/patterns/messaging-bridge)
- [Apache Kafka design and delivery semantics](https://kafka.apache.org/40/design/design/)
- [CloudEvents specification and resources](https://cloudevents.io/)
- [AsyncAPI specification](https://www.asyncapi.com/docs/reference/specification/latest)
- [OpenTelemetry messaging semantic conventions](https://opentelemetry.io/docs/specs/semconv/messaging/messaging-spans/)

## Reliability, security, and operations

- [Google Cloud Pub/Sub reliability guidance](https://docs.cloud.google.com/pubsub/docs/reliability-intro)
- [Google Cloud Pub/Sub exactly-once delivery](https://docs.cloud.google.com/pubsub/docs/exactly-once-delivery)
- [Azure queue-based load leveling pattern](https://learn.microsoft.com/azure/architecture/patterns/queue-based-load-leveling)
- [OWASP API Security Top 10](https://owasp.org/API-Security/)
- [Google SRE books](https://sre.google/books/)

## Video sources

- [AWS Events](https://www.youtube.com/@AWSEventsChannel)
- [AWS Developers](https://www.youtube.com/@awsdevelopers)
- [Microsoft Azure](https://www.youtube.com/@MicrosoftAzure)
- [Google Cloud Tech](https://www.youtube.com/@googlecloudtech)
- [CNCF](https://www.youtube.com/@cncf)

Search the official channels for current sessions on event-driven architecture,
Amazon EventBridge/SQS/Kinesis/MSK, Azure Service Bus/Event Hubs, Google Cloud Pub/Sub,
Kafka delivery semantics, schema evolution, and OpenTelemetry messaging.

## Books for deeper study

- *Designing Data-Intensive Applications* by Martin Kleppmann
- *Enterprise Integration Patterns* by Gregor Hohpe and Bobby Woolf
- *Designing Event-Driven Systems* by Ben Stopford
- *Kafka: The Definitive Guide* by Gwen Shapira and others
- *Building Event-Driven Microservices* by Adam Bellemare
- *Release It!* by Michael T. Nygard

## Suggested review loop

1. Choose one business journey and classify each command, event, stream, and query.
2. Trace commit through broker acknowledgment, delivery, effect, and consumer commit.
3. Define entity order, key, partitions, consumer groups, retention, and capacity.
4. Inject duplicate, gap, late event, poison record, skew, and regional failure.
5. Plan an isolated replay and reconcile every authoritative and derived state.
6. Translate the design across AWS, Kafka, Azure, and Google Cloud without false parity.
7. Re-answer scenarios aloud and state what evidence would change each choice.
