# Storage, Databases, and Analytics

[← Compute platforms](compute-platforms.md) · [Next: Integration →](integration.md)

| Capability | AWS | Azure | Google Cloud |
| --- | --- | --- | --- |
| Object storage | S3 | Blob Storage | Cloud Storage |
| Block storage | EBS | Managed Disks | Persistent Disk / Hyperdisk |
| Managed file | EFS/FSx | Azure Files/NetApp Files | Filestore |
| Managed relational | RDS/Aurora | Azure SQL, managed PostgreSQL/MySQL | Cloud SQL/AlloyDB |
| NoSQL families | DynamoDB, DocumentDB | Cosmos DB and specialist services | Firestore, Bigtable and specialist services |
| Warehouse | Redshift | Fabric/Synapse capabilities | BigQuery |
| Stream/batch analytics | Kinesis/Glue/EMR | Event Hubs/Data Factory/Databricks | Pub/Sub/Dataflow/Dataproc |

Never infer consistency, transactions, query language, indexing, partitioning, change
streams, backup, replication, or failover from the row position. “NoSQL” products may
serve fundamentally different models.

Data gravity often decides placement. Model authoritative ownership, residency,
replication mode, lag, conflict/fencing, schema, encryption/key dependency, deletion,
backup, restore, reconciliation, transfer bandwidth, egress, and exit time.

Avoid synchronous dual writes across clouds. Prefer an authoritative transaction plus
outbox/change stream, idempotent consumers, reconciliation, and explicit lag objectives.
Validate migration with business invariants, not only record counts.
