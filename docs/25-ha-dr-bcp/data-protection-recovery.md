# Data Protection and Recoverability

[← Module overview](index.md) · [DR strategies](dr-strategies.md)

Data recovery must address infrastructure loss, logical corruption, accidental
deletion, malicious destruction, ransomware, and application-level inconsistency.
Each requires a different recovery point and isolation boundary.

## Protection model

For every data set, record owner, classification, source of truth, RPO, retention,
legal hold, consistency boundary, encryption/key dependency, copy locations,
immutability, restore order, validation method, and deletion process.

A robust design commonly applies the 3-2-1 idea: multiple copies, different
failure media or services, and at least one off-site or separately isolated copy.
For cyber recovery, strengthen this with immutable or logically air-gapped copies,
separate administration, multifactor controls, and monitored restore access.

## AWS-first controls

- Centralize policies and reporting with AWS Backup where supported.
- Use cross-account backup vaults and cross-Region copies for stronger isolation.
- Evaluate AWS Backup Vault Lock and S3 Object Lock for retention enforcement.
- Enable versioning and appropriate replication for object recovery requirements.
- Use point-in-time recovery, snapshots, transaction logs, and native database tools deliberately.
- Protect KMS keys, IAM recovery roles, service control policies, and break-glass access.
- Store infrastructure definitions, application artifacts, configuration, and dependency manifests independently.

Feature support and immutability behavior vary by service and mode; confirm current
provider documentation rather than assuming one policy protects every resource.

## Replication versus backup

Synchronous replication can reduce data loss but may couple availability to
latency or remote failure. Asynchronous replication protects availability but
creates measurable lag and potential loss. Both can reproduce corruption.
Point-in-time, immutable backups preserve an earlier state, but restore takes time.
A mature service often needs replication for availability and backups for recovery.

## Restore is the product

Measure successful recovery, not backup-job completion. Test catalog discovery,
permissions, key access, clean-room restore, data integrity, application startup,
transaction reconciliation, performance at recovery scale, and business acceptance.
Capture actual RPO, restore time, recovery time, failure reason, and corrective owner.

## Cyber-recovery sequence

Contain destructive access, preserve evidence, identify a trusted recovery point,
establish a clean identity and network boundary, restore foundational services,
scan and validate, reconcile data, rotate credentials, reopen in controlled waves,
and monitor for reinfection. Ordinary failover may copy the compromise.

Return to the [module overview](index.md) when ready to continue.
