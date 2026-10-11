# Storage, Databases, and Analytics

[← Compute platforms](compute-platforms.md) · [Next: Integration services →](integration-services.md)

## Start with authority and access patterns

Identify authoritative facts, invariants, transactions, data shape, access paths,
volume, growth, throughput, latency, consistency, availability, durability, recovery,
retention, residency, privacy, analytics, skills, and cost. Derived caches, indexes,
lakes, and warehouses require freshness, rebuild, deletion, and authorization plans.

## Storage choices

S3 provides regional object storage with storage classes, versioning, replication,
lifecycle, Object Lock, and event integration. EBS is zonal block storage for EC2; EFS
is managed regional file storage; FSx families address specific file-system workloads.
Compare protocol, sharing, latency, throughput, durability, backup, encryption, access,
failure scope, and data-transfer cost.

## Database choices

RDS and Aurora serve relational workloads; DynamoDB provides managed key-value/document
access at scale; ElastiCache accelerates access; OpenSearch supports search/analytics;
DocumentDB, Neptune, Keyspaces, Timestream, MemoryDB, and others address distinct
models. Product labels never replace transaction, query, consistency, partition,
connection, backup, and migration analysis.

## Analytics architecture

Use S3-based lakes, Glue catalog/integration, Athena query, EMR processing, Redshift
warehousing, Kinesis streaming, and governed analytics capabilities as requirements
justify. Define zones, schemas, lineage, quality, ownership, privacy, access, retention,
cost, replay, and workload isolation. A data lake without governance becomes an opaque
collection of copies.

## Protect and recover data

Combine service-native backups/PITR, AWS Backup where applicable, versioning, immutable
or isolated copies, cross-account/Region strategies when justified, and tested restore.
Replication improves availability but can replicate deletion or corruption. Prove
application-consistent recovery and business invariants within RTO/RPO.
