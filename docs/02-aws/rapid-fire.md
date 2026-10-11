# Rapid-Fire Revision

[← Presentation template](presentation-template.md) · [Next: Flashcards →](flashcards.md)

Answer each in one or two sentences before adding an example.

1. **What is an AWS Region?** A separate geographic area containing multiple isolated Availability Zones.
2. **What is an Availability Zone?** One or more data centers with independent facilities and redundant low-latency connectivity to other AZs in a Region.
3. **Is every AWS service Regional?** No; resources and APIs may be global, Regional, zonal, or edge-scoped.
4. **Why document service scope?** Placement determines failure, residency, authorization, recovery, quota, and dependency behavior.
5. **What is static stability?** Continuing essential operation through impairment without requiring immediate control-plane changes.
6. **When is multi-Region justified?** When business impact, RTO/RPO, residency, or global service needs outweigh replication and operating complexity.
7. **What is an AWS account boundary?** A strong resource, administration, quota, billing, and blast-radius boundary.
8. **What belongs in the Organizations management account?** Organization management only; business workloads should normally live in member accounts.
9. **What is an OU for?** Grouping accounts with common policy and operational needs.
10. **Does an SCP grant permission?** No; it limits the maximum permissions available to affected principals.
11. **What does AWS Control Tower provide?** Managed setup and governance capabilities for a multi-account landing zone built on other AWS services.
12. **What is a landing zone?** An operable, governed cloud foundation including identity, network, security, logging, delivery, cost, and lifecycle.
13. **Why use delegated administrators?** To keep service administration out of the management account and assign accountable specialist ownership.
14. **What identity should a workload use?** A scoped IAM role with short-lived credentials.
15. **What controls effective AWS authorization?** Identity/resource policies, trust, SCPs/RCPs, boundaries, sessions, endpoint/key policies, conditions, and explicit denies.
16. **Why is a KMS key a dependency?** Unavailable, denied, disabled, or deleted keys can make durable encrypted data unusable.
17. **What is CloudTrail primarily for?** Recording supported AWS API and account activity for audit and investigation.
18. **What is AWS Config primarily for?** Resource configuration history, relationships, and compliance evaluation.
19. **What is GuardDuty?** A managed threat-detection service using AWS data sources and threat intelligence.
20. **Is a VPC Regional?** Yes; its subnets are placed in individual Availability Zones.
21. **Are security groups stateful?** Yes; return traffic for allowed flows is automatically permitted.
22. **Are network ACLs stateful?** No; inbound and outbound rules must account for both directions.
23. **What is VPC peering’s routing limitation?** It is non-transitive.
24. **What does Transit Gateway provide?** Managed hub-style connectivity among VPCs and hybrid networks.
25. **What does PrivateLink provide?** Private service exposure through interface endpoints without broad network routing.
26. **Does Direct Connect encrypt traffic by default?** No; add appropriate encryption when required.
27. **What does a NAT gateway enable?** Outbound IPv4 translation for private resources; it is not inbound publishing.
28. **Why deploy NAT gateways per AZ?** To avoid cross-AZ dependency and transfer for workloads requiring resilient egress.
29. **Route 53 versus CloudFront?** Route 53 provides DNS/routing; CloudFront caches and delivers content through edge locations.
30. **CloudFront versus Global Accelerator?** CloudFront is an HTTP/content CDN; Global Accelerator routes supported network traffic using static anycast addresses and the AWS backbone.
31. **When is EC2 appropriate?** When the workload needs host/OS/runtime control or compatibility unavailable at a higher abstraction.
32. **ECS versus EKS?** ECS is AWS-native orchestration; EKS provides managed Kubernetes control planes and ecosystem compatibility.
33. **What does Fargate remove?** Customer management of worker servers for supported ECS/EKS workloads, not application or configuration responsibility.
34. **What protects a downstream from Lambda bursts?** Concurrency limits, buffering/backpressure, connection budgets, and idempotent bounded retries.
35. **What is EBS?** Zonal block storage commonly attached to EC2.
36. **What is EFS?** Managed regional shared file storage using NFS semantics.
37. **Why use S3 versioning?** To preserve recoverable object versions against overwrite/deletion, subject to lifecycle and access controls.
38. **RDS Multi-AZ versus read replica?** Multi-AZ targets availability; read replicas primarily scale reads and have separate lag/failover semantics.
39. **What is DynamoDB partition-key risk?** Skew can create hot partitions and uneven capacity despite high total service scale.
40. **What is a derived store?** A cache, search index, projection, or analytical copy rebuilt from an authoritative source.
41. **What does SQS provide?** Managed message queues that buffer and decouple producers from consumers.
42. **What does SNS provide?** Push-based publish/subscribe fan-out to supported endpoints.
43. **What does EventBridge provide?** Rule-based event routing among AWS, custom, and SaaS sources/targets.
44. **What does Kinesis provide?** Retained partitioned streams with ordered records within a shard.
45. **Why must consumers be idempotent?** At-least-once delivery and retries can produce duplicate processing.
46. **What is a dead-letter queue?** An isolation destination for messages that exceed configured processing attempts.
47. **What should backlog monitoring include?** Oldest age, arrival/completion rate, in-flight work, failures, and business delay.
48. **Why is a replica not a backup?** It can quickly copy accidental deletion, corruption, or malicious change.
49. **What proves RTO/RPO?** Timed recovery and integrity evidence under representative failure, not design claims.
50. **What is a service quota?** An adjustable or fixed limit scoped to a service, account, Region, or resource dimension.
51. **Why model failure capacity?** Remaining resources must handle demand after an AZ, dependency, or deployment loss.
52. **What is CUR/Data Exports used for?** Detailed AWS billing and usage analysis and allocation.
53. **Why use unit economics?** Cost per business outcome distinguishes efficiency from demand growth.
54. **When should Savings Plans be purchased?** After stable eligible usage is understood and flexibility/risk are evaluated.
55. **What makes an AWS design architect-level?** Traceable outcomes, deliberate boundaries, service semantics, failure behavior, evidence, operations, and economic trade-offs.
