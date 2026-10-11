# Security, Privacy, and Governance

[← Caching and connections](caching-connections.md) · [Next: Backup, recovery, and migration →](backup-recovery-migration.md)

## Identity and authorization

Use short-lived workload identity or rotated scoped credentials, separate application,
migration, backup, monitoring, and administrator roles, and deny public access by
default. Database permissions should match schemas, tables, procedures, operations,
and environments. Network isolation complements but does not replace authorization.

## Application access

Use parameterized queries, validate dynamic identifiers, restrict ORM-generated
queries, bound result size/time, and prevent mass assignment. Row-level security can
reinforce tenant boundaries but depends on trustworthy session context and complete
policy coverage. Test horizontal and vertical privilege escalation against real paths.

## Encryption and keys

Encrypt transport and storage, validate server identity, rotate certificates and keys,
and restrict key administration separately from data administration. Customer-managed
or tenant-specific keys change availability, quota, recovery, and support. Field-level
encryption can reduce operator exposure but complicates query and indexing.

## Audit and monitoring

Record privileged login, policy/role change, schema change, export, backup/restore,
replication, key action, and sensitive data access according to risk. Protect audit
integrity, retention, access, and clock quality. Avoid logging query parameters or
rows containing secrets and personal data.

## Data lifecycle

Classify data and define collection purpose, residency, retention, archive, legal hold,
export, correction, and deletion. Propagate lifecycle to replicas, caches, indexes,
change streams, analytics, backups, and test copies. Mask or synthesize nonproduction
data; production snapshots should not become uncontrolled developer datasets.

## Administrative safety

Require strong workforce identity, just-in-time privileged access, approval for high-
impact changes, safe query consoles, session evidence, and break-glass review. Protect
drop, truncate, mass update, restore, replication reconfiguration, and parameter change
with preview, backup, scope check, and rollback. Separate duties where required.

## Multi-tenant boundaries

Choose shared table, schema, database, instance, account/project, or hybrid isolation
from risk and economics. Ensure keys, uniqueness, queries, backups, telemetry, support,
and tenant restore preserve the boundary. Encryption alone does not stop a valid
application identity from selecting the wrong tenant's rows.
