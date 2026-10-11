# Storage, Databases, and Analytics

[← Compute platforms](compute-platforms.md) · [Next: Integration services →](integration-services.md)

## Start with authority and access paths

Identify authoritative facts, invariants, transactions, data shape, queries, volume,
growth, throughput, latency, consistency, availability, durability, recovery, retention,
residency, privacy, analytics, skills, and cost. Derived caches, indexes, lakes, and
warehouses require freshness, rebuild, authorization, deletion, and ownership.

## Storage choices

Storage accounts provide Blob, Files, Queue, and Table capabilities with different
semantics. Select locally, zone, geo, or geo-zone redundant options based on failure
and recovery needs; read-access variants affect secondary reads. Managed Disks provide
VM block storage; Azure Files provides managed file shares; Data Lake Storage adds
hierarchical namespace capabilities to Blob. Verify protocol, performance, consistency,
failover, backup, private access, and transaction costs.

## Database choices

Azure SQL Database and Managed Instance serve different SQL Server compatibility and
management needs; Azure Database for PostgreSQL addresses managed PostgreSQL; Cosmos DB
offers globally distributed NoSQL APIs and explicit consistency choices; Azure Managed
Redis supports cache/in-memory patterns; Azure AI Search handles search/vector needs.
Select from invariants and access patterns, not product category alone.

## Analytics and data governance

Fabric, Databricks, Synapse capabilities, Data Factory, Event Hubs, Stream Analytics,
and Data Lake patterns can support analytical workloads. Define data products/zones,
catalog and lineage, schema, quality, authority, access, privacy, residency, retention,
workload isolation, replay, and cost. Verify current product boundaries and licensing;
analytics branding evolves faster than data-governance responsibilities.

## Protect and recover data

Combine service-native PITR/backups, Azure Backup where applicable, soft delete,
versioning, immutable vault/storage controls, and cross-subscription/Region strategy
when justified. Replication is not backup because it can copy corruption or deletion.
Restore into isolation and validate identity, keys, networking, configuration,
performance, application consistency, and business invariants within RTO/RPO.
