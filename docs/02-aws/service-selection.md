# AWS Service-Selection Matrices

[← Integration services](integration-services.md) · [Next: Reliability and operations →](reliability-operations.md)

These matrices are interview prompts, not automatic selectors. Start with workload
semantics, verify current service behavior and quotas, and record alternatives.

## Compute and application runtime

| Option | Strong fit | Principal trade-off to test |
| --- | --- | --- |
| EC2 with Auto Scaling | Host/OS control, legacy compatibility, special hardware | Patching, image lifecycle, capacity, scaling, and recovery remain yours |
| ECS on EC2 | AWS-native containers with density or host control | Cluster capacity and host operations |
| ECS on Fargate | Containers without worker-node administration | Supported task shapes, startup, networking, limits, and price |
| EKS on EC2 | Kubernetes ecosystem plus node-level flexibility | Control-plane, node, add-on, upgrade, policy, and skill complexity |
| EKS on Fargate | Kubernetes pods without worker-node administration | Feature compatibility, pod shape, daemon needs, and economics |
| Lambda | Event-driven, bounded, bursty execution | Duration, concurrency, cold start, payload, state, and downstream pressure |
| App Runner | Managed web/API container runtime | Platform limits, networking, observability, and customization |

## Storage and database

| Requirement | Typical AWS options | Decision evidence |
| --- | --- | --- |
| Object and archival data | S3 storage classes, Glacier classes | Access frequency, retrieval time/cost, immutability, lifecycle |
| VM block storage | EBS; instance store for ephemeral data | AZ scope, durability, IOPS/throughput, snapshot, attachment |
| Shared file access | EFS or an appropriate FSx family | Protocol, semantics, latency, throughput, clients, backup |
| Relational transactions | RDS engines or Aurora | Compatibility, transactions, extensions, connections, HA, cost |
| Key-value/document access | DynamoDB | Keys, access paths, partitions, consistency, transactions, cost |
| Cache/in-memory data | ElastiCache or MemoryDB | Authority, durability, consistency, eviction, failover |
| Search and log analytics | OpenSearch Service | Query, indexing, shard lifecycle, security, operational cost |
| Warehouse and lake query | Redshift, Athena, EMR, Glue and S3 patterns | Workload isolation, latency, scale, governance, skills, economics |

## Integration and workflow

| Need | Typical choice | Critical question |
| --- | --- | --- |
| Buffer work for consumers | SQS | What are retry, visibility, ordering, age, and DLQ semantics? |
| Push fan-out | SNS, commonly with SQS subscriptions | How are subscribers isolated and deliveries filtered? |
| Route business/system events | EventBridge | Who owns schemas, rules, archives, replay, and cross-account trust? |
| Retained partitioned stream | Kinesis Data Streams | What partition key, shard capacity, ordering, and replay are required? |
| Orchestrate stateful workflow | Step Functions | Standard/Express semantics, idempotency, compensation, history, cost? |
| Expose managed API | API Gateway or load-balancer/service patterns | Protocol, auth, quotas, transformation, latency, streaming, cost? |

## Connectivity and edge

| Need | Typical choice | Principal distinction |
| --- | --- | --- |
| Connect a few VPCs | VPC peering | Direct, non-transitive routing with growing pairwise management |
| Hub connectivity | Transit Gateway | Central routing, segmentation, scale, attachment and transfer cost |
| Private service exposure | PrivateLink | Endpoint-based consumer access without broad routed connectivity |
| Managed global WAN | Cloud WAN | Policy-based core-network management across sites and Regions |
| Encrypted internet hybrid path | Site-to-Site VPN | Internet variability, tunnel/device/location redundancy |
| Dedicated hybrid connectivity | Direct Connect | Private capacity but encryption and physical diversity need design |
| HTTP content delivery | CloudFront | Caching, origins, invalidation, WAF, TLS, and edge behavior |
| Static global network ingress | Global Accelerator | Supported protocols, endpoints, health, static anycast addresses |

## Final selection test

For any option state authority, scope, consistency, scaling unit, quotas, failure and
degradation, security boundary, observability, backup/recovery, deployment, ownership,
pricing dimensions, skills, portability, and evidence that would change the decision.
