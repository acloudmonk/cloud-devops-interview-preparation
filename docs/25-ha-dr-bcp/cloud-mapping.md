# AWS-First Multi-Cloud Capability Map

[← Module overview](index.md) · [Runbooks and governance](testing-governance.md)

Translate intent, guarantees, and operating behavior—not product names alone.
Availability-zone design, regional relationships, replication, failover, and
service-level responsibilities differ by provider and service.

## Capability mapping

| Intent | AWS examples | Azure examples | Google Cloud examples |
| --- | --- | --- | --- |
| Zonal distribution | Availability Zones, ELB, Auto Scaling | Availability Zones, Load Balancer, VM Scale Sets | Zones, Cloud Load Balancing, Managed Instance Groups |
| Global traffic | Route 53, Global Accelerator, CloudFront | Front Door, Traffic Manager | Cloud Load Balancing, Cloud DNS |
| Central backup | AWS Backup, service-native backups | Azure Backup | Backup and DR Service, service-native backups |
| VM/workload recovery | Elastic Disaster Recovery | Azure Site Recovery | Backup and DR Service or workload-specific patterns |
| Object replication | S3 replication and versioning | Blob redundancy/replication options | Cloud Storage dual/multi-region and replication behavior |
| Relational regional DR | Aurora Global Database, RDS replicas | Azure SQL failover groups and service-specific replicas | Cloud SQL cross-region replicas, AlloyDB/Spanner patterns |
| Global NoSQL | DynamoDB global tables | Cosmos DB multi-region writes | Spanner multi-region, Firestore locations |
| Resilience assessment | AWS Resilience Hub | Azure reliability guidance and resiliency capabilities | Google Cloud Well-Architected reliability guidance |

This is an orientation map, not a claim of feature equivalence. Confirm service,
tier, Region, consistency, encryption, failover, and SLA details in current docs.

## Provider questions

- Is a resource zonal, zone-redundant, regional, multi-region, or global?
- Are paired-region or location constraints relevant?
- Is replication synchronous or asynchronous, and how is lag exposed?
- Is failover automatic, provider-managed, customer-triggered, or application-led?
- Does promotion change endpoints, identities, keys, or connection semantics?
- Are backups isolated from workload administrators and destructive control planes?
- Can the recovery Region provide capacity and all required service features?
- How are organization/account/subscription/project policies reproduced safely?

## Multi-cloud as a recovery strategy

Using another provider can reduce some provider-level concentration risks, but it
adds identity, data, network, tooling, skills, security, observability, and testing
complexity. It is justified only when the business requirement exceeds what a
single-provider multi-Region design can deliver and the organization can operate
both paths continuously. A portable application with non-portable data or identity
does not provide a complete recovery capability.

## Interview guidance

Lead with objectives and failure boundaries. Describe the AWS design in depth,
then explain which guarantees must be revalidated when translating to Azure or
Google Cloud. Avoid presenting a service-name table as an architecture.

Return to the [module overview](index.md) when ready to continue.
