# Cross-Cloud Capability Matrices

[← Portability and placement](portability-placement.md) · [Next: Design exercise →](design-exercise.md)

Use this page to create a shortlist, then validate current documentation and prototype
critical semantics.

| Capability | AWS | Azure | Google Cloud | Validate |
| --- | --- | --- | --- | --- |
| Workload boundary | Account | Subscription | Project | policy, quota, network, billing |
| VM | EC2 | Virtual Machines | Compute Engine | images, scale, disks, placement |
| Kubernetes | EKS | AKS | GKE | identity, upgrade, network, storage |
| Serverless container | ECS/Fargate/App Runner | Container Apps | Cloud Run | protocols, scale, limits |
| Function | Lambda | Functions | Cloud Run functions | triggers, duration, retries |
| Object | S3 | Blob Storage | Cloud Storage | consistency, location, lifecycle |
| Relational | RDS/Aurora | Azure SQL/managed engines | Cloud SQL/AlloyDB | compatibility, HA, recovery |
| Document/key-value | DynamoDB families | Cosmos DB families | Firestore/Bigtable families | model, query, consistency |
| Warehouse | Redshift | Fabric/Synapse | BigQuery | workload, isolation, pricing |
| Kubernetes registry | ECR | ACR | Artifact Registry | trust, replication, scanning |
| Monitoring | CloudWatch | Azure Monitor | Cloud Monitoring | SLI, cardinality, retention |
| Key service | KMS | Key Vault | Cloud KMS | hierarchy, availability, rotation |

## Validation record

For each candidate capture scope, location, API/protocol, limits, consistency/delivery,
identity, network, encryption, backup/recovery, observability, SLA, quota, pricing,
compliance, operational owner, proof, gaps, and exit trigger.

Do not publish a mapping as timeless truth. Add review dates and prefer durable
capability descriptions; link current provider sources for volatile detail.
