# Database Architecture References and Videos

[← Active-recall flashcards](flashcards.md) · [Module overview](index.md)

Verify current engine versions, extensions, transaction and consistency semantics,
topologies, quotas, Regions, backup behavior, pricing, and support before production
decisions. Compatibility labels require workload-specific testing.

## Suggested reading order

1. [AWS decision guide: Choosing an AWS database service](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/databases-on-aws-how-to-choose.html)
2. [Azure: Understand data models](https://learn.microsoft.com/azure/architecture/data-guide/technology-choices/understand-data-store-models)
3. [Azure: Prepare to choose a data store](https://learn.microsoft.com/azure/architecture/guide/technology-choices/data-store-considerations)
4. [AWS Well-Architected: Use a purpose-built data store](https://docs.aws.amazon.com/wellarchitected/latest/framework/perf_data_use_purpose_built_data_store.html)
5. [PostgreSQL transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html)

## Relational design and operation

- [PostgreSQL index types](https://www.postgresql.org/docs/current/indexes-types.html)
- [PostgreSQL query planning](https://www.postgresql.org/docs/current/using-explain.html)
- [PostgreSQL concurrency control](https://www.postgresql.org/docs/current/mvcc.html)
- [PostgreSQL backup and restore](https://www.postgresql.org/docs/current/backup.html)
- [PostgreSQL high availability and replication](https://www.postgresql.org/docs/current/high-availability.html)
- [Amazon RDS best practices](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_BestPractices.html)
- [Amazon RDS Multi-AZ failover](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.Failover.html)
- [Amazon Aurora User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html)

## NoSQL, partitioning, and caching

- [DynamoDB partition-key design](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-design.html)
- [DynamoDB read consistency](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html)
- [DynamoDB transactions](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/transactions.html)
- [MongoDB sharding](https://www.mongodb.com/docs/manual/sharding/)
- [MongoDB transactions](https://www.mongodb.com/docs/manual/core/transactions/)
- [Redis caching patterns](https://redis.io/docs/latest/develop/clients/patterns/)

## Multi-cloud selection and reliability

- [Azure data-store technology choices](https://learn.microsoft.com/azure/architecture/guide/technology-choices/data-stores-getting-started)
- [Azure mission-critical data-platform considerations](https://learn.microsoft.com/azure/well-architected/mission-critical/mission-critical-data-platform)
- [Google Cloud database services](https://cloud.google.com/products/databases)
- [Google Cloud database reliability guidance](https://cloud.google.com/architecture/framework/reliability/reliability-of-databases)
- [Google SRE books](https://sre.google/books/)

## Video sources

- [AWS Events](https://www.youtube.com/@AWSEventsChannel)
- [AWS Developers](https://www.youtube.com/@awsdevelopers)
- [Microsoft Azure](https://www.youtube.com/@MicrosoftAzure)
- [Google Cloud Tech](https://www.youtube.com/@googlecloudtech)
- [PostgreSQL](https://www.youtube.com/@postgresql)

Search the official channels for current sessions on database selection, Aurora/RDS,
DynamoDB data modeling, PostgreSQL query plans and MVCC, distributed databases,
online migration, failover, and recovery testing.

## Books for deeper study

- *Designing Data-Intensive Applications* by Martin Kleppmann
- *Database Internals* by Alex Petrov
- *SQL Performance Explained* by Markus Winand
- *High Performance MySQL* by Silvia Botros and Jeremy Tinley
- *PostgreSQL: Up and Running* by Regina Obe and Leo Hsu
- *NoSQL Distilled* by Pramod Sadalage and Martin Fowler

## Suggested review loop

1. Choose one workload and write authority, invariants, and its ten highest-value access paths.
2. Compare two models against transaction, consistency, query, growth, and skill needs.
3. Inspect example plans, indexes, connection budgets, cache failure, and partition skew.
4. Inject replica lag, deadlock, hot shard, schema lock, cache loss, and region failover.
5. Restore an isolated point conceptually and define data/application acceptance tests.
6. Design baseline-copy/CDC migration with validation, rollback, and reconciliation.
7. Translate requirements across AWS, Azure, Google Cloud, and portable engines.
