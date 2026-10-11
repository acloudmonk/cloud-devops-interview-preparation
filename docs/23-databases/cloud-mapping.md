# AWS-First Multi-Cloud Capability Map

[← Backup, recovery, and migration](backup-recovery-migration.md) · [Next: Enterprise design exercise →](design-exercise.md)

Map requirements and engine semantics before products. Verify current Regions,
versions, extensions, consistency, topology, quotas, backup, pricing, and support.

| Need | AWS anchor | Azure examples | Google Cloud examples | Portable engines |
| --- | --- | --- | --- | --- |
| Managed relational | Amazon RDS, Aurora | Azure SQL, Azure Database for PostgreSQL/MySQL | Cloud SQL, AlloyDB | PostgreSQL, MySQL, SQL Server |
| Distributed relational | Aurora DSQL, Aurora PostgreSQL Limitless | Azure Cosmos DB for PostgreSQL options | Spanner | CockroachDB, YugabyteDB |
| Key-value/document | DynamoDB, DocumentDB | Cosmos DB, Azure Managed Redis | Firestore, Bigtable | MongoDB, Cassandra, Redis |
| Graph | Neptune | Cosmos DB graph options | Partner/portable services | Neo4j, JanusGraph |
| Time series | Timestream, purpose-built stores | Azure Data Explorer | Bigtable, BigQuery patterns | TimescaleDB, InfluxDB |
| Cache/in-memory | ElastiCache, MemoryDB | Azure Managed Redis | Memorystore | Redis/Valkey |
| Search/vector | OpenSearch Service, engine extensions | Azure AI Search, database extensions | Vertex AI Search, database extensions | OpenSearch, pgvector |
| Warehouse/analytics | Redshift, Athena/S3 | Fabric/Synapse ecosystem | BigQuery | Trino, ClickHouse |
| Migration/CDC | AWS DMS, engine replication | Azure Database Migration Service | Database Migration Service, Datastream | Debezium, native logical replication |

## AWS-first selection

Use RDS/Aurora when relational constraints, transactions, joins, and SQL ecosystem fit;
DynamoDB for access-pattern-driven key-value/document workloads at scale; DocumentDB
only after validating required MongoDB compatibility; Neptune for graph traversal;
ElastiCache or MemoryDB for explicit in-memory needs; OpenSearch for search-derived
views; Redshift/Athena for analytical access. Purpose-built does not mean maximally
polyglot—each new engine adds ownership and synchronization cost.

## Non-equivalence warnings

“PostgreSQL compatible,” “MongoDB compatible,” global tables, multiprimary, serverless,
and point-in-time recovery vary in extension, transaction, consistency, conflict,
scaling, failover, and operational behavior. Benchmark representative schema and
queries, test failures, restore data, and validate drivers before committing.

## Portability strategy

Use open protocols and engines where they meet requirements, keep domain logic outside
proprietary features when portability has business value, automate schema and data
tests, and maintain logical export. Do not sacrifice correctness or operability for an
untested future migration. An exit plan is evidence and tooling, not a claim of being
cloud agnostic.
