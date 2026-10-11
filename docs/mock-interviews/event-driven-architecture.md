# Messaging and Event-Driven Architecture Mock Interview

[← Mock interview overview](index.md) · [Module 22 overview](../22-event-driven/index.md)

Duration: **50 minutes**
Level: **Senior / Architect**
Primary context: **AWS-first global commerce with Kafka and multi-cloud consumers**

## Candidate brief

A global retailer synchronously connects order, payment, inventory, fulfilment,
loyalty, notification, fraud, and analytics. Campaigns create 60-times traffic, a
payment timeout caused duplicate charges, inventory events arrive out of order, and
analytics is six hours behind. Teams publish ungoverned JSON. Design an asynchronous
target architecture and safe migration; leadership currently asks for Kafka everywhere.

## Interview structure

### 0–7 minutes — Discovery and interaction model

Clarify business journeys, authorities, immediate versus eventual results, message
meaning, consumers, volume, burst, freshness, ordering, retention, replay, recovery,
privacy, regions, cost, and team capability. Challenge a product-first mandate.

### 7–18 minutes — Semantics, partitioning, and contracts

Choose API, queue, pub/sub, bus, log, and workflow boundaries. Explain producer
commit, broker acknowledgment, delivery, consumer effect, acknowledgment, outbox,
idempotency, entity version, partition key, groups, schemas, and compatibility.

### 18–28 minutes — Processing and operations

Cover projections, event time, late data, retry taxonomy, DLQ repair, backpressure,
skew, autoscaling, retention, replay, observability, freshness SLOs, reconciliation,
security, connectors, privacy, and cost.

### 28–38 minutes — Failure branches

Choose three:

- consumer crashes after charging but before acknowledgment;
- a poison record blocks a FIFO group;
- one key accumulates days of lag;
- schema registry is unavailable during deployment;
- re-drive immediately returns every record to the DLQ;
- replay sends millions of duplicate emails;
- cross-region replication reverses entity order;
- a connector identity is used to export an entire topic.

### 38–45 minutes — Platform and migration

Map requirements to EventBridge, SNS, SQS, Kinesis, MSK, and Step Functions; compare
Azure and Google Cloud dependencies, bridge guarantees, regional recovery, rollout,
dual-run evidence, consumer onboarding, old-flow retirement, and economic ownership.

### 45–50 minutes — Executive close

State the recommended interaction model, first migration slice, measurable freshness
and correctness outcomes, principal risks, residual uncertainty, and evidence that
could change the design.

## Scoring rubric

| Dimension | Points |
| --- | ---: |
| Discovery, meaning, and interaction selection | 7 |
| Delivery, ordering, idempotency, and consistency | 10 |
| Partitioning, consumer scaling, and backpressure | 7 |
| Contracts, schemas, processing state, and replay | 8 |
| Resilience, observability, recovery, and reconciliation | 8 |
| Security, platform fit, migration, and cost | 7 |
| Trade-offs and executive communication | 3 |
| **Total** | **50** |

Interpretation: **43–50** architect-ready; **35–42** strong with targeted gaps;
**25–34** incomplete guarantee or operating reasoning; **below 25** rebuild from
message meaning and boundary-by-boundary delivery. An unqualified “exactly once” or
“Kafka for everything” answer cannot exceed 34.

## Improvement loop

Record the three weakest decisions, revisit the corresponding module pages and
primary sources, redraw the message lifecycle and failure boundaries, then repeat
within seven days with different failure branches.
