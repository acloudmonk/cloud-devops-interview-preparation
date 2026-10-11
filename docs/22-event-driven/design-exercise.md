# Enterprise Event-Platform Design Exercise

[← AWS-first multi-cloud map](cloud-mapping.md) · [Next: Scenario questions →](scenarios.md)

## Brief

A global retailer handles checkout synchronously across order, payment, inventory,
fulfilment, loyalty, notification, fraud, and analytics. Peak campaigns create 60
times normal load. A payment timeout recently caused duplicate charges, inventory
events arrive out of order, analytics is six hours behind, and teams publish JSON
without owners or schemas. Leadership asks for “Kafka everywhere on AWS.”

## Constraints

- checkout must acknowledge accepted orders within 800 milliseconds;
- payment and inventory facts require explainable, reconcilable state;
- notifications may be delayed but not silently lost;
- analytics needs replayable history and event-time windows;
- peak input is 250,000 events per second with highly skewed product demand;
- PCI and personal data must be minimized, regionally governed, and auditable;
- Azure hosts loyalty integration and Google Cloud hosts an analytics consumer;
- regional recovery targets 30 minutes RTO and less than one minute RPO.

## Candidate direction

Challenge the product-first mandate. Use durable commands or workflow state for
required actions, domain-owned integration events for facts, queues for independent
work, and a retained partitioned stream where replay and ordered computation justify
it. Keep synchronous authorization only where checkout requires an immediate answer.

Persist order state and outbox intent atomically. Give every event a stable ID,
business key/version, schema, occurrence/publication time, correlation, causation,
classification, and trace context. Partition by the smallest entity requiring order;
isolate known hot cohorts or aggregate where product-key skew is unavoidable.

Consumers commit local state and processing evidence together, use provider/business
idempotency for payments, and reconcile broker facts against authoritative systems.
Apply bounded retries, per-consumer DLQs, backpressure, fair scheduling, and controlled
re-drive. Separate irreversible effects from general replay paths.

On AWS, evaluate EventBridge, SNS, SQS, Kinesis, MSK, and Step Functions against each
message class. Bridge Azure and Google Cloud asynchronously with explicit weakest-link
semantics. Define tenant/region security, schema governance, freshness SLOs, capacity,
cost, multi-region recovery, and migration from synchronous flows.

## Scored deliverable (50 points)

| Area | Points | Strong evidence |
| --- | ---: | --- |
| Discovery and interaction choices | 7 | business timing, message meaning, justified sync/async patterns |
| Delivery, ordering, and correctness | 9 | precise guarantees, idempotency, outbox, versions, reconciliation |
| Partitioning, scaling, and backpressure | 8 | keys, skew, groups, capacity, lag, recovery drain |
| Contracts, schemas, and replay | 7 | ownership, compatibility, retention, safe replay, event time |
| Resilience and operations | 8 | retry taxonomy, DLQ workflow, SLOs, evidence, regional recovery |
| Security and governance | 6 | identity, isolation, classification, privacy, audit, lifecycle |
| Platform, migration, and cost | 5 | AWS-first fit, cross-cloud boundary, sequence, economics |

Score 40+ only when business correctness remains explainable after duplicates,
reordering, partial processing, replay, and regional failure.
