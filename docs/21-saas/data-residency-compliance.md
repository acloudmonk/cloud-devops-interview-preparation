# Data, Residency, and Compliance

[← Identity and authorization](identity-authorization.md) · [Next: Reliability, performance, and scale →](reliability-performance.md)

## Data model and partitioning

Classify provider, tenant, user, configuration, transactional, telemetry, audit,
usage, billing, and derived data. Every tenant-owned record needs an authoritative
tenant partition key. Shared-table, schema-per-tenant, database-per-tenant, and
account/project-per-tenant models trade efficiency, isolation, limits, backup,
migration, and operations differently.

Queries, uniqueness constraints, caches, object paths, search indexes, events, and
exports must preserve tenant scope. Global indexes are especially dangerous if the
application assumes filtering will always be added later.

## Encryption and keys

Use encryption in transit and at rest, with explicit key ownership and rotation.
A provider-managed shared key, provider-managed tenant key, and customer-managed key
offer different cost, availability, revocation, and support characteristics. A key
per tenant improves cryptographic separation but can introduce quota and fleet
operations. Key deletion is not a substitute for complete lifecycle deletion.

## Residency and sovereignty

Residency policy covers more than the primary database: backups, replicas, object
copies, indexes, logs, traces, support exports, analytics, disaster recovery, and
third parties matter. Store placement policy in the tenant catalog and enforce it in
provisioning and routing. Document whether administrators and support staff can
access data cross-border and how failover affects the promise.

## Retention, export, and deletion

Map data classes to legal basis, retention, hold, export format, deletion deadline,
and backup expiry. Keep a deletion manifest and reconcile across systems. Tombstones
can prevent deleted records from reappearing during replay or restore. Verify restore
procedures do not silently violate deletion obligations.

## Audit and evidence

Audit records need actor, tenant, action, target, decision, time, source, and outcome.
Protect integrity, access, retention, and clock quality. Separate customer-facing
audit from provider security evidence while maintaining traceability. Never place
secrets or unrestricted personal data into immutable audit streams.

## Analytics boundary

Aggregate or de-identify product analytics according to purpose and contract. Tenant
administrators should see only their scope; provider analysts receive the minimum
necessary access. Define re-identification risk, small-cohort suppression, export,
lineage, and deletion propagation before centralizing data.
