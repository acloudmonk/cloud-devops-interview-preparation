# Backup, Recovery, and Migration

[← Security and governance](security-governance.md) · [Next: AWS-first multi-cloud map →](cloud-mapping.md)

## Recovery begins with objectives

Map business processes to RPO, RTO, integrity, retention, and dependency order. Define
recovery for accidental row change, tenant deletion, schema release, corruption,
instance loss, regional loss, and credential compromise. One backup policy cannot
serve every failure mode.

## Backup design

Combine automated snapshots, transaction-log or point-in-time recovery, and exports
or isolated copies where appropriate. Define frequency, retention, immutability,
cross-account/project protection, region, encryption keys, catalog, monitoring, and
expiry. Include schemas, roles, extensions, parameters, procedures, and external
objects needed to reconstruct the service.

## Restore proves recoverability

Regularly restore into isolated infrastructure, measure time, verify checksums/counts,
constraints, critical queries, application compatibility, tenant isolation, and
business invariants. Reconnect dependent services only after acceptance. A completed
restore API call is not proof that the product is correct or available.

## Point-in-time and partial recovery

Choose a recovery point before the harmful transaction, then account for valid changes
after it. Whole-database restore may be unsafe for a single tenant or table. Design
logical extraction, temporal/history tables, audit/change streams, replay, or corrective
transactions. Preserve evidence and prevent restored deleted data from escaping.

## Migration patterns

Assess engine features, types, collation, constraints, procedures, extensions, query
behavior, volume, change rate, downtime, and rollback. Options include offline copy,
backup restore, logical export/import, continuous replication/CDC, dual read, and
carefully controlled dual write. Compatible wire protocol does not prove semantic
compatibility.

## Online migration sequence

1. Establish schema and baseline copy with reproducible tooling.
2. Capture ongoing changes and monitor lag plus errors.
3. Validate counts, checksums, aggregates, invariants, query plans, and performance.
4. Rehearse cutover, fence or quiesce writes, drain changes, and switch routing.
5. Observe correctness and retain a time-bounded rollback path.
6. Reconcile, archive evidence, and retire the old authority deliberately.

## Recovery security

Backups are high-value data. Restrict list/read/restore/delete, separate backup
administration, protect keys, alert on policy changes, and test recovery when primary
identity or account is compromised. A clean-room restore needs trusted artifacts,
network isolation, malware/corruption checks, and controlled promotion.
