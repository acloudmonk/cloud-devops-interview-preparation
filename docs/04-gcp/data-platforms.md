# Storage, Databases, and Analytics

[← Compute platforms](compute-platforms.md) · [Next: Integration →](integration-services.md)

Start with access pattern, consistency, transaction scope, model, latency, throughput,
size, residency, RPO/RTO, analytics, skills, and cost.

| Need | Candidates | Key distinction |
| --- | --- | --- |
| Object/archive | Cloud Storage | location, class, lifecycle, retention |
| Block/file | Persistent Disk/Hyperdisk, Filestore | performance, scope, protocol |
| Managed relational | Cloud SQL, AlloyDB | compatibility, scale, HA, operations |
| Scalable relational | Spanner | consistency, schema, instance configuration |
| Document/mobile | Firestore | query model, indexes, limits |
| Wide-column | Bigtable | key design, access pattern, replication |
| Cache | Memorystore | eviction, persistence, failover |
| Analytics | BigQuery, Dataflow, Dataproc | warehouse vs stream/batch vs Spark/Hadoop |

Keep an explicit authoritative system. High availability is not backup: plan deletion,
corruption, disaster, retention, isolated restore, and business validation. Replication
does not automatically provide zero data loss or conflict resolution.

Model connections, hot keys/partitions, indexes, quotas, egress, and failure capacity.
For migration, profile workloads, select CDC or offline paths, rehearse rollback, and
reconcile business invariants—not only byte counts.
