# Rapid-Fire Revision

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-07**

Answer each in 30–60 seconds. The cue is the minimum idea a strong answer should
contain, not a full response.

## Distributed-systems fundamentals

1. **Scalability versus elasticity?** Scalability is ability to handle growth;
   elasticity is timely capacity adjustment with demand.
2. **Availability versus reliability?** Availability is usable time; reliability
   is correct operation over time under stated conditions.
3. **Resilience versus fault tolerance?** Resilience includes degradation and
   recovery; fault tolerance aims to continue through selected faults.
4. **Why is a timeout necessary?** It bounds resource retention and the caller's
   uncertainty; it must fit an end-to-end deadline.
5. **When is a retry unsafe?** Non-idempotent operation, unknown prior outcome,
   permanent error, exhausted deadline, or overloaded dependency.
6. **Why add jitter?** It prevents synchronized retries and periodic work from
   recreating a traffic spike.
7. **What does a circuit breaker do?** Stops repeated calls to a failing boundary
   temporarily; it needs a truthful fallback and careful recovery.
8. **What is backpressure?** A slower consumer signals or constrains a faster
   producer so work does not grow without bound.
9. **Load shedding versus throttling?** Throttling enforces a rate; shedding
   rejects/degrades work to protect critical capacity.
10. **Why can autoscaling fail?** Delayed signals, quotas, cold starts, stateful
    bottlenecks, dependency limits, or scaling on the wrong metric.
11. **What is an invariant?** A business property that must remain true across
    concurrency and failure, such as one seat per confirmed order.
12. **What does idempotency require?** Stable key, request fingerprint, stored
    outcome, retention policy, and atomic business effect.
13. **Does exactly-once delivery solve duplicates?** Business effects still need
    idempotency across retries, side effects, and failure boundaries.
14. **CAP in one sentence?** During a network partition, a distributed system
    must choose how a given operation trades consistency and availability.
15. **What does PACELC add?** Even without partition, systems trade latency and consistency.

## Architecture and data

1. **Stateless service?** Request processing does not depend on irreplaceable
    local instance state; durable state lives behind an explicit boundary.
2. **When use a queue?** To decouple timing, absorb bursts, retry durable work,
    and allow independent scaling when asynchronous completion is acceptable.
3. **When not use a queue?** The caller requires an immediate authoritative
    result or added state/latency/operations outweigh the benefit.
4. **Event versus command?** Event states what happened; command requests a
    specific owner to perform an action.
5. **Saga limitation?** Compensation is business logic, not a universal rollback,
    and intermediate states remain visible.
6. **Cache-aside risk?** Staleness, stampede, invalidation races, and origin overload.
7. **Why is global ordering expensive?** It centralizes coordination and limits
    parallelism; prefer ordering only within the entity boundary that needs it.
8. **How detect a hot partition?** Segment throttling/latency by key distribution
    rather than relying on aggregate capacity.
9. **RDBMS versus key-value store?** Decide from invariants, transactions, access
    patterns, query flexibility, scale, and operating model.
10. **CQRS benefit and cost?** Models reads/writes independently but adds eventual
    consistency, synchronization, and operational complexity.

## Reliability and operations

1. **SLI, SLO, SLA?** Indicator is measurement, objective is internal target,
    agreement is an external commitment with consequences.
2. **Error budget?** Allowed unreliability implied by the SLO, used to balance
    delivery velocity and reliability work.
3. **RTO versus RPO?** Maximum acceptable restoration time versus acceptable
    data loss measured in time.
4. **Backup versus DR?** Backup is a copy; DR is tested people, process, systems,
    dependencies, and measured recovery.
5. **What should page an operator?** Actionable, urgent customer impact or rapid
    SLO burn—not every infrastructure threshold.
6. **Golden signals?** Latency, traffic, errors, and saturation, supplemented by
    business and correctness signals.
7. **Why can health checks lie?** They may test only process liveness, share the
    failed dependency, or miss the customer path.
8. **Canary limitation?** Low traffic may not expose scale, tenant, data, cache,
    dependency, or regional differences.
9. **Safe database change?** Expand, deploy compatible code, migrate/verify,
    switch, then contract.
10. **Why test failback?** Recovery Region state and routing may make returning
    harder and riskier than initial failover.

## AWS and multi-cloud reasoning

1. **Why CloudFront before origin?** Edge caching, TLS, abuse controls, and
    admission reduce latency and protect constrained origin capacity.
2. **ALB versus API Gateway?** Compare routing/runtime integration with API
    lifecycle, authentication, throttling, protocols, scale, and cost.
3. **ECS versus EKS?** Choose based on Kubernetes ecosystem/operating capability,
    not because both run containers.
4. **DynamoDB conditional write use?** Atomically enforce a state transition or
    uniqueness rule under concurrency.
5. **SQS standard queue assumption?** At-least-once delivery with possible
    duplicates and best-effort ordering; consumer must be idempotent.
6. **EventBridge versus SQS?** Event routing to subscribers versus buffered work
    ownership and consumer backpressure.
7. **Multi-AZ versus multi-region?** Different failure scope, data model, cost,
    latency, routing, and operational complexity.
8. **Global Tables risk?** Multi-writer conflict semantics, residency, dependency
    isolation, and reconciliation still require design.
9. **Cross-cloud service mapping mistake?** Similar names do not guarantee equal
    transactions, delivery, networking, scaling, recovery, or pricing.
10. **Portable architecture?** Portable principles and contracts matter more than
    forcing identical service implementations.

## Senior/consulting judgment

1. **First architecture question?** What business outcome and critical journey
    are we protecting or improving?
2. **How present an unknown?** State the assumption, sensitivity, owner, and
    evidence needed to resolve it.
3. **Why offer alternatives?** Architecture is a constrained decision; the
    alternative exposes what the recommendation optimizes and sacrifices.
4. **How reduce delivery risk?** Thin vertical slices, reversible changes,
    compatibility, observability, progressive exposure, and explicit exit gates.
5. **Principal-level closing statement?** Recommendation, accepted trade-off,
    top risk, accountable owner, validation evidence, and next decision.
