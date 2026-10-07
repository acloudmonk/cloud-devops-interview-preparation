# AWS Design Walkthrough

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-07**

This is an interview walkthrough, not a deployment tutorial. Use it to explain
how a vendor-neutral requirement becomes an AWS-oriented design while preserving
alternatives and trade-offs.

## 1. Establish the critical journey

```text
discover event → enter waiting room → browse → hold seat → pay → confirm
```

Classify each step:

| Step | Can degrade? | Correctness need | Likely mode |
| --- | --- | --- | --- |
| Browse | Yes; stale catalogue may be acceptable | Never invent an event | Cached/read-heavy |
| Admission | Yes; waiting is acceptable | Token cannot be forged/replayed freely | Edge control |
| Hold seat | Limited | One active owner | Synchronous atomic write |
| Payment | Limited | Never double charge | Idempotent external command |
| Notifications | Yes | Eventual delivery | Asynchronous |

## 2. Protect capacity at the edge

Start with the capability: global delivery, abuse protection, and controlled
admission. An AWS answer may use Route 53, CloudFront, and AWS WAF, with edge
logic and a waiting-room origin. The important point is that admission is tied
to tested downstream capacity and can be tightened before stateful systems saturate.

Explain origin-bypass protection, token lifetime, false positives, operator
control, and the customer experience when admission is closed.

## 3. Keep request handling replaceable

Use stateless request handlers across multiple Availability Zones. ECS on
Fargate is a reasonable starting choice for a container-oriented team; Lambda
or EKS may fit different workload and operating constraints. The answer should
cover health routing, failure capacity, connection/concurrency limits, deployment,
and rollback—not only automatic scaling.

## 4. Put correctness in the state transition

The reservation boundary owns the invariant:

```text
AVAILABLE → HELD → CONFIRMED
              ↘ EXPIRED/RELEASED → AVAILABLE
```

An AWS implementation could use a DynamoDB conditional write or a relational
transaction. The decision depends on access patterns and broader transaction
needs. Never rely on a cache or read-then-write sequence to prevent double selling.

An idempotency key must be bound to the request fingerprint and stored outcome.
Replaying the same request returns the original result; using the key for a
different request is rejected.

## 5. Decouple deferrable work

After the authoritative hold, queue permitted background work such as payment
workflow coordination, notifications, and reconciliation. With SQS, assume
at-least-once delivery and make the consumer's business effect idempotent. Define
visibility timeout, retry ownership, maximum age, DLQ behavior, and replay controls.

Do not claim that adding a queue makes a system reliable. Explain what happens
when publishing fails after the database write, when consumers stop, and when a
poison message repeatedly fails.

## 6. Treat payment timeout as unknown

A timeout does not prove failure. The payment provider may have accepted the
charge and lost the response. Carry a stable provider idempotency key, record an
unknown state, query/reconcile the provider, and keep customer/order state truthful.
Do not release inventory and charge again blindly.

## 7. Observe the business state

Correlate technical and customer evidence:

- admission rate and waiting time;
- browse and purchase success/latency;
- reservation conflicts and invariant violations;
- queue age and DLQ depth;
- unknown payment count and reconciliation age;
- deployment version, Region, and Availability Zone.

Explain which conditions page immediately, which create tickets, and which are
capacity or cost trends.

## 8. Recover in stages

Start with single-Region multi-AZ and tested reconstruction/restore. If the RTO,
RPO, and business loss justify multi-region, add an explicit write-ownership,
replication, routing, dependency, failover, reconciliation, and failback model.

Browsing may fail over more easily than reservation/payment. Different critical
journeys may have different recovery designs.

## 9. Present two options

| Option | Strength | Cost/risk | Appropriate when |
| --- | --- | --- | --- |
| Multi-AZ with cross-region recovery | Lower complexity and cost | Regional RTO is non-zero | Verified recovery meets business tolerance |
| Multi-region serving with constrained writes | Faster selected regional recovery | Replication, routing, operations, and reconciliation | Outage loss justifies continuous regional readiness |

## 10. Close with evidence

A strong interview recommendation ends with validation:

- release-shaped load and cache-hit assumptions;
- concurrent reservation and idempotency tests;
- worker outage and backlog-drain measurement;
- payment ambiguity and reconciliation exercise;
- zonal failure and deployment rollback;
- restore/failover measured against RTO/RPO;
- unit cost per admitted and confirmed order.

Use the [worked capacity example](capacity-slo-worked-example.md),
[decision matrix](decision-matrix.md), and
[presentation template](presentation-template.md) to rehearse this walkthrough.
