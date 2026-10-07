# Active-Recall Flashcards

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Use these prompts without looking at the answer. Speak for 30–60 seconds, then
compare your response with the cue. The cue is a minimum, not a script.

## Architecture foundations

| Prompt | Answer cue |
| --- | --- |
| What is the difference between availability and reliability? | Availability is readiness for use at a point in time; reliability is sustained correct service over an interval. A system can be reachable yet return incorrect results. |
| How do scalability and elasticity differ? | Scalability is the ability to handle growth; elasticity is timely adjustment of capacity as demand changes. |
| Why is “multi-AZ” not a complete reliability answer? | It does not define failure detection, dependency behavior, state recovery, degraded modes, testing, or whether the application actually survives an AZ loss. |
| What does a good architecture assumption contain? | A value or range, its source or rationale, its design impact, and a plan to validate it. |
| When should a modular monolith be preferred? | When team size, domain maturity, delivery speed, and operational capability make distributed ownership costlier than the scaling or autonomy benefit. |
| What is a blast radius? | The users, data, tenants, regions, or capabilities affected by one failure or change. Good designs deliberately bound it. |

## Distributed-systems reasoning

| Prompt | Answer cue |
| --- | --- |
| What does CAP actually force during a network partition? | A choice about whether a particular operation preserves consistency or availability; the whole system need not make one universal choice. |
| Why are retries dangerous? | They multiply load during failure, can repeat side effects, and synchronize clients. Bound attempts, use deadlines, backoff and jitter, and require idempotency. |
| What is idempotency? | Repeating the same logical request has the same intended effect as processing it once. Persist the idempotency decision at the side-effect boundary. |
| At-least-once delivery implies what application responsibility? | Consumers must handle duplicates and partial processing; delivery guarantees do not create exactly-once business effects. |
| When is a queue useful? | To absorb bursts, decouple availability and pace, and enable retries—but only when delay and eventual consistency are acceptable. |
| What is backpressure? | A mechanism by which downstream capacity limits upstream production instead of allowing unbounded work and collapse. |
| Why are timeouts part of capacity design? | Long waits hold threads, connections, memory, and concurrency, turning a slow dependency into resource exhaustion. |
| What is load shedding? | Rejecting or degrading lower-priority work deliberately so the system protects critical work and recovers. |

## Data and correctness

| Prompt | Answer cue |
| --- | --- |
| How would you prevent two customers reserving one seat? | Establish one authoritative ownership boundary and use an atomic conditional update or transaction with a version/state precondition. |
| Why can a cache not be the source of truth for seat ownership? | Eviction, replication lag, failover, and invalidation races can expose stale state; correctness must live in an authoritative durable store. |
| What is the payment “unknown outcome” problem? | A timeout does not reveal whether the provider committed. Reconcile by stable operation ID and provider status; do not blindly retry a new charge. |
| When is eventual consistency appropriate? | When temporary divergence is acceptable, convergence is defined, and the user/business behavior during lag is explicit. |
| What creates a hot partition? | A skewed access key or monotonically concentrated workload directs disproportionate traffic to one partition despite low aggregate utilization. |
| What is schema evolution safety? | Producers and consumers tolerate compatible versions during rollout, with validation, observability, and a plan for old events. |

## Reliability and operations

| Prompt | Answer cue |
| --- | --- |
| Define SLI, SLO, and SLA. | SLI is the measured behavior; SLO is the internal target; SLA is the external commitment and consequence. |
| What does an error budget enable? | A quantitative balance between reliability and change: allowed unreliability can guide release pace and risk decisions. |
| How do RTO and RPO differ? | RTO is acceptable recovery time; RPO is acceptable data-loss window. Both must be tied to a business process. |
| What is the first step in incident diagnosis? | Confirm customer impact and time window, then compare healthy and unhealthy dimensions before forming and testing hypotheses. |
| Why can dashboards be green while customers fail? | Aggregate infrastructure metrics may miss one journey, tenant, region, status code, dependency, or correctness failure. Measure end-to-end outcomes. |
| How do you reason about queue backlog? | Inspect arrival and processing rates, oldest-message age, failure/redrive rate, consumer saturation, dependency health, and time to drain. |
| What belongs in a degraded mode? | The protected critical journey, disabled features, activation signal, customer experience, operational owner, exit criteria, and testing evidence. |

## AWS and multi-cloud judgment

| Prompt | Answer cue |
| --- | --- |
| When is Lambda a strong compute choice? | Event-driven, bursty, bounded-duration work where per-request economics and low infrastructure ownership outweigh concurrency, cold-start, and runtime constraints. |
| When is ECS often simpler than EKS? | When container scheduling is needed but Kubernetes portability/ecosystem benefits do not justify control-plane concepts and operating complexity. |
| DynamoDB or Aurora for reservations? | Decide from access patterns, transaction/relational needs, contention model, scale shape, team skill, operational model, and migration constraints—not a universal ranking. |
| SQS or Kinesis? | SQS distributes discrete work; Kinesis preserves ordered records within shards for streaming consumers and replay. Confirm ordering, throughput, retention, and consumer model. |
| What makes a cross-cloud comparison credible? | Compare behavioral guarantees, limits, failure domains, identity, networking, observability, and operating model—not product names alone. |
| When is multi-region active-active justified? | When business objectives require it and ownership, conflict behavior, dependency topology, operations, testing, and cost are explicitly solved. |

## Practice rule

Mark a card **known** only when you can provide a definition, one practical
example, one failure or trade-off, and one question that would change your
choice. Revisit missed cards after one day, three days, and seven days.
