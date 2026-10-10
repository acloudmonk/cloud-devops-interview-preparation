# Advanced CI/CD Scenario Drills

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

Use the [scenario-answer framework](../interview-playbook/scenario-answer-framework.md).
Spend six minutes per drill: clarify, contain, investigate, recover, verify, prevent,
and identify the trade-off. These deliberately omit model answers.

## 1. Compromised third-party action

A SHA-pinned action used by 70 repositories is reported compromised at that SHA.
Some runs published artifacts and three deployed to production. Lead the response
without assuming pinning made the action safe.

## 2. Mutable release tag

The `v4.2` image tag now resolves to a different digest than yesterday. Production
clusters differ, release records mention only the tag, and the registry audit log
retains seven days. Establish truth and design the permanent control.

## 3. Poisoned base image

Builds are reproducible from application source, but the trusted base-image tag was
silently replaced. Explain containment, impact analysis, rebuild criteria, evidence,
and how future provenance should represent all material inputs.

## 4. Destructive schema migration completed

The new release corrupts invoices after dropping a legacy column. Restoring the
old binary will not work. Customers are active and the latest backup is four hours
old. Choose recovery and explain which pre-release controls would have changed it.

## 5. Merge queue and deployment concurrency conflict

Every queued merge is valid, but rapid main-branch runs cancel one another during
production promotion. Some environments show skipped versions. Redesign concurrency
without turning the entire pipeline into one slow global lock.

## 6. Cloud API times out after partial success

A deployment call times out. The CI step reports failure, but half the ECS services
may have updated. The rerun button is available. Describe the state-read, recovery,
idempotency, and operator evidence required before anyone uses it.

## 7. Valid provenance from a compromised builder

The signature and attestation validate, yet forensic evidence shows the authorized
builder image was compromised. Explain what provenance proves, what it does not,
and how to scope, revoke, rebuild, and strengthen the builder trust root.

## 8. GitOps controller fights an emergency change

An operator changes production to stop an incident, but the reconciler restores
the harmful desired state. Decide how to pause/reconcile safely while preserving a
single source of truth and an auditable emergency path.

## 9. Feature-flag service is unavailable

Checkout depends on several server-side flags. The flag service times out during a
release and instances disagree because of cached values. Define safe defaults,
consistency needs, operational control, and testing for this dependency failure.

## 10. Primary CI provider is unavailable

A critical vulnerability requires deployment while the source/CI provider is down.
Design a continuity procedure that retains review, immutable source/artifact
identity, independent verification, least privilege, and later reconciliation.
