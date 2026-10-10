# Source-Control Governance Design Exercise

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**
Estimated time: **3–4 hours**
Expected cloud cost: **None**

## Brief

Design source-control governance for a 180-engineer organization operating 40
services, a platform, mobile clients, infrastructure code, and shared libraries.
Teams deploy from multiple times per day to quarterly. Two products are
regulated, external contributors work on one SDK, and the organization must
support two prior releases while moving from long-lived environment branches.

Do not create repositories or pipelines. Produce diagrams, tables, and decision
records.

## Requirements to clarify

- team topology, ownership, trust, data classification, and external access;
- deployment/release frequency, supported versions, and emergency-change needs;
- coupling and frequency of cross-component changes;
- CI duration, test confidence, artifact-promotion model, and delivery risks;
- regulatory separation, approval, signing, retention, and audit requirements;
- large binaries/generated files and repository performance constraints;
- platform availability, backup, recovery, and vendor-lock-in objectives.

## Required deliverables

1. **Repository-boundary map:** monorepo/multirepo decisions, owners, consumers,
   sensitive paths, shared code, and release units.
2. **Commit/branch lifecycle:** source of truth, branch lifetime, integration,
   release/backport, tag, and retirement rules.
3. **PR control matrix:** risk class, required owners/approvers/checks, merge
   method, stale-approval behavior, and merge queue.
4. **Identity and permission model:** humans, bots, CI, releases, external forks,
   administrators, break glass, and offboarding.
5. **Integrity/security plan:** signing, secret prevention/response, workflow
   protection, dependency pinning, audit, and retention.
6. **Migration plan:** environment-branch retirement, pilot, compatibility,
   freeze/synchronization, rollback, communication, and success metrics.
7. **Recovery runbooks:** bad merge, accidental force push, leaked secret,
   compromised signing key, unavailable provider, and large-history mistake.
8. **Operating metrics:** branch age, PR size/latency, queue time, bypasses,
   failed changes/reverts, ownership gaps, and CI reliability.

## Mandatory decision records

- trunk-based versus GitFlow/release-branch approach;
- merge commit versus squash/rebase policy;
- monorepo versus multirepo for the platform and services;
- protected-branch/ruleset and CODEOWNERS design;
- regulated-release signing and tag policy;
- external fork CI trust boundary;
- emergency change and post-incident reconciliation.

## Failure walkthroughs

Explain detection, containment, recovery, verification, and prevention for:

- a force push removes a day of shared default-branch history;
- a production credential is committed and cloned externally;
- a compromised automation identity creates a signed release tag;
- merge queue checks pass individually but combined changes fail;
- a critical fix reaches the release branch but not trunk;
- source hosting is unavailable during a production incident.

## Decision record template

| Field | Content |
| --- | --- |
| Decision | One precise repository/workflow/control choice |
| Context | Delivery, risk, team, and compliance constraints |
| Options | At least two viable alternatives |
| Choice and why | Evidence-based selection |
| Trade-offs | Flow, assurance, usability, cost, and recovery |
| Failure behavior | Blast radius and recovery path |
| Validation | Measurable acceptance criteria and rehearsal |
| Revisit trigger | Scale, incident, regulation, or platform change |

## Self-assessment

Score 0–4 for requirements, repository boundaries, workflow, governance,
security, release support, recovery, migration, metrics, and communication. A
strong result scores at least 30/40 with no category below 2.
