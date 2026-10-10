# GitOps and Reconciliation

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

GitOps uses versioned declarative desired state and automated reconciliation for
delivery and operations. Git hosting alone is not GitOps; the critical properties are
pull-based or controlled reconciliation, traceable change, drift handling, health,
security boundaries, and recovery.

## Argo CD and Flux mental model

Both ecosystems reconcile sources into cluster state, with different APIs,
compositional patterns, tenancy controls, extension models, and operating choices.
Evaluate the current supported features rather than reduce the comparison to UI versus
CLI. The portable invariant is source → verified artifact/config → reconciler identity
→ target → observed health/status.

## Source-of-truth design

Decide repository boundaries, application/platform ownership, environment/region
representation, promotion model, dependency/version pinning, secrets, and generated
content. Avoid environment branches that silently diverge. Promotion should change a
reviewed immutable reference or configuration delta, not rebuild the artifact.

The repository is desired-state evidence, not the complete operational truth. Runtime
status, cloud resources, data, controller versions, credentials, and external systems
also determine reality.

## Reconciliation ownership

- Define which paths/namespaces/clusters each reconciler may read and mutate.
- Separate platform and tenant credentials/projects/tenancies.
- Constrain destination, source, resource kinds, impersonation, and cluster registration.
- Avoid two reconcilers or a pipeline and reconciler owning the same field/outcome.
- Set prune, orphan, replacement, retry, dependency ordering, and deletion deliberately.

Auto-sync reduces drift time but can amplify a bad commit across many targets. Use
progressive cohorts, health evidence, bounded concurrency, and promotion gates at the
appropriate source boundary. Controller “Healthy/Synced” is not customer health.

## Drift and emergency change

Classify drift as unauthorized mutation, emergency action, controller/defaulting
effect, ignored runtime field, or legitimate external ownership. Choose detect-only,
auto-correct, or human review by risk. Ignore only fields with a named owner and reason.

For emergency change: declare authority and time limit, pause or redirect reconciliation
as designed, make the bounded change, preserve evidence, verify customers, commit the
intended state, resume, and confirm convergence. An undocumented `kubectl edit` that
the controller immediately reverses is not a break-glass process.

## Secrets and source security

Never store plaintext secrets in Git. Encryption-in-Git, references to external secret
stores, and runtime delivery have different key, rotation, availability, audit, and
recovery models. Protect repository/workflow/reconciler identities, commit/release
integrity, dependency sources, and controller supply chain.

## Failure and continuity

Plan for source-host outage, controller loss, invalid desired state, compromised repo
or reconciler, expired credentials/certificates, target API outage, webhook failure,
dependency cycle, and mass deletion. Existing workloads may keep running while change
and recovery capability degrades. Retain known-good revisions/artifacts, independent
access and evidence, controller state/config backup, and a tested reconciliation path.

## Measures

Track reconciliation latency/error/backlog, drift age, failed health, promotion lead
time, rollback/roll-forward time, manual/bypass changes, controller/API load, stale
applications, and customer outcome. Do not reward raw sync frequency or treat “no
drift” as proof the desired state is correct.
