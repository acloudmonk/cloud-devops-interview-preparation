# AWS Architecture Decision Matrix

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-07**

Use this matrix to explain selection criteria. Do not recite it as a fixed
reference architecture: capability, constraints, and operating model come first.

## Compute and entry point

| Decision | Starting option | Prefer when | Reconsider when |
| --- | --- | --- | --- |
| ECS on Fargate | Containerized API and workers | Team wants containers without managing nodes | Kubernetes APIs or event-only functions are a real requirement |
| AWS Lambda | Short event/request handlers | Burstiness, low idle usage, and bounded execution fit | Long processing, specialized runtime, or steady high utilization dominates |
| Amazon EKS | Kubernetes platform | Existing platform team, policies, and ecosystem justify it | The team would operate Kubernetes only for one application |
| ALB | HTTP load balancing to services | Host/path routing and long-lived service processes fit | API product controls, usage plans, or WebSocket/API lifecycle dominate |
| API Gateway | Managed API front door | Authentication, throttling, API lifecycle, and serverless integration matter | High sustained throughput economics or ALB-native routing is preferable |

## Data and messaging

| Decision | Starting option | Prefer when | Reconsider when |
| --- | --- | --- | --- |
| DynamoDB | Inventory/idempotency key access | Known key access, conditional writes, and horizontal scale fit | Relational joins, constraints, and flexible transactions dominate |
| Aurora PostgreSQL | Orders and relational workflows | SQL, relational integrity, and reporting access are important | Write partitioning or unpredictable key-value scale dominates |
| ElastiCache | Derived hot reads and rate state | Recomputable data and latency reduction justify operational cost | Correctness would depend on cache durability |
| SQS standard | Background commands/work | At-least-once delivery and independent consumers fit | Strict ordering across all messages is a hard requirement |
| SQS FIFO | Ordered message groups | Per-entity ordering and deduplication window fit | Throughput model or global ordering expectations conflict |
| EventBridge | Business event routing | Multiple loosely coupled subscribers and filtering matter | It is being used as a work queue with consumer backpressure needs |
| Kinesis | Ordered partitioned stream | Replay, high-rate streams, and ordered shards matter | Simple task distribution is the actual requirement |
| Step Functions Standard | Visible durable workflow | Long-running saga state, retries, and compensation need auditability | A simple idempotent worker is sufficient |

## Edge and resilience

| Capability | AWS option | Interview decision signal |
| --- | --- | --- |
| Global caching | CloudFront | Cache only data whose staleness is understood |
| Abuse control | AWS WAF | Rate and managed rules complement, not replace, application authorization |
| Admission control | CloudFront logic plus controlled origin access | Protect downstream capacity before saturation |
| DNS recovery | Route 53 | Health signal, TTL, client caching, and failback must be explained |
| DDoS baseline | Shield Standard | Included protection does not eliminate workload-specific capacity planning |
| Fault experiments | AWS FIS | Use only after steady state, stop conditions, and rollback are defined |

## The five-sentence decision method

For any service choice, answer:

1. **Capability:** What problem must the component solve?
2. **Constraint:** Which scale, correctness, latency, security, or team constraint matters?
3. **Choice:** Which service is the current recommendation?
4. **Trade-off:** What disadvantage or lock-in is accepted?
5. **Evidence:** What measurement or failure test would prove the choice?

Example:

> We need an atomic seat-state transition under bursty key-based access. I would
> start with DynamoDB conditional writes because the access pattern is known and
> the workload needs managed horizontal scale. I accept a less flexible query
> model and must design partition keys carefully. Aurora is the alternative if
> relational constraints and ad hoc transactional queries dominate. I would
> validate hot-key distribution, conditional conflicts, latency, throttling,
> and recovery using release-shaped traffic.

## Multi-cloud translation prompts

When translating a decision, compare behavior rather than labels:

- transaction and consistency boundaries;
- delivery, ordering, and redrive semantics;
- scaling unit and quota model;
- identity and private-network integration;
- regional and global failure behavior;
- telemetry and operational ownership;
- pricing unit and data-transfer effects;
- migration and exit cost.

See the [multi-cloud translation guide](multi-cloud.md) for the capability map.
