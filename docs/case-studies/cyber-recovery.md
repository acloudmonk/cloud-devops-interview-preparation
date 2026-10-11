# Case 5: Cyber-Recovery Crisis

[← Hybrid modernization](hybrid-modernization.md) · [Next: Reliability and FinOps →](reliability-finops.md)

## Brief

A ransomware event compromises workforce identity and encrypts parts of an AWS and
on-premises estate. Production is stopped as a precaution. Backups exist, but the
last full recovery exercise was fourteen months ago. Customer ordering, warehouse
dispatch, payroll, and regulatory reporting compete for restoration priority.

## Discovery prompts

- Which identities, keys, control planes, endpoints, logs, and backup paths are trusted?
- Who declares crisis, sets business priorities, and authorizes reconnection?
- What are service dependencies, maximum tolerable outage, RTO/RPO, and manual workarounds?
- Are backups immutable, isolated, scanned, restorable, and protected by separate credentials?
- What legal, insurance, law-enforcement, customer, and regulator duties apply?

## Candidate tasks

1. Define immediate command, containment, evidence-preservation, and communication.
2. Establish a clean-room trust anchor, identity path, tooling, and recovery environment.
3. Prioritize business capabilities through dependency-aware recovery waves.
4. Validate backup integrity, malware status, data correctness, and service readiness.
5. Plan reconnection, heightened monitoring, failback, lessons, and long-term controls.

## Failure injects

- The latest backup contains dormant malicious persistence.
- The backup administrator account is part of the compromised identity domain.
- A restored database is clean but six hours behind a downstream ledger.
- Executives demand immediate internet reconnection before forensic validation.
- A critical SaaS provider suspends federation because signing keys may be exposed.

## Model direction

Invoke incident and crisis command, preserve evidence, isolate affected paths, and
avoid destructive “cleanup” before scope is understood. Establish trusted out-of-
band communications and clean identities. Recovery begins in an isolated clean room
from immutable, independently controlled backups and known-good IaC, images,
dependencies, keys, and configuration. Scan and validate before reconnecting.

Use the business impact analysis to restore end-to-end capabilities, not individual
servers. Reconcile ledgers and asynchronous work against authoritative external
records. Apply explicit readiness gates: security confidence, functional and data
checks, capacity, observability, owner approval, and rollback. Communicate uncertainty
and workarounds. After stabilization, rotate trust, close persistence paths, test
recovery more frequently, measure restore evidence, and separate backup authority
from the primary identity and production planes.

## Strong close

State who owns the go/no-go decision and what evidence is non-negotiable before
reconnection. Balance recovery speed with the risk of restoring compromise; neither
the newest backup nor the fastest server restore is automatically correct.
