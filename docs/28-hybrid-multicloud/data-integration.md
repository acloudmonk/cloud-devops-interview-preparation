# Data Placement and Integration

[← Module overview](index.md) · [Identity and trust](identity-security.md)

Data is usually less portable than compute. Placement decisions must include source
of truth, residency, gravity, consistency, latency, volume, movement, privacy,
retention, recovery, analytics, and exit requirements.

## Data decision record

For each domain, record owner, classification, authoritative store, allowed locations,
replicas, consistency and conflict policy, RPO/RTO, encryption/key boundary, interfaces,
lineage, retention/deletion, transfer cost, and recovery/exit test.

## Integration patterns

- synchronous API for low-latency interactions that can tolerate link dependency;
- asynchronous events/queues for decoupling, buffering, replay, and independent recovery;
- batch/file transfer for large or time-insensitive movement with integrity manifests;
- CDC/replication for controlled copies with lag, ordering, schema, and failure handling;
- federated query only when performance, availability, privacy, and cost are acceptable.

Use idempotency, versioned contracts, schema governance, backpressure, dead-letter
handling, reconciliation, and end-to-end traceability. Avoid distributed transactions
across unreliable long-distance boundaries when domain redesign can localize state.

## Sovereignty and privacy

Data residency alone may not satisfy sovereignty: administration, support, encryption
keys, metadata, backups, logs, and legal access can matter. Map regulation with legal
and privacy owners; apply minimization, purpose limitation, access, retention, deletion,
and transfer controls across every copy.

## Exit and recovery

Measure export time, format usability, transfer bandwidth/cost, target ingestion,
schema/application dependencies, integrity verification, dual-run/reconciliation,
and contract deletion. A backup stored in a proprietary format is not a complete exit plan.

Return to the [module overview](index.md) when ready to continue.
