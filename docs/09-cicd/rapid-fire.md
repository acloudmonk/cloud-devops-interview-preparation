# CI/CD Rapid-Fire Revision

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

Answer each in 30–60 seconds with a definition, risk, and condition that changes
the design.

## Delivery foundations

1. **Continuous integration?** Frequently integrate small changes and verify the shared code state with fast, trustworthy feedback.
2. **Continuous delivery?** Keep a releasable artifact ready through automation; production release may remain a decision.
3. **Continuous deployment?** Every qualifying change proceeds automatically to production.
4. **Deployment versus release?** Deployment installs capability; release/exposure makes it available to users.
5. **Pipeline control plane?** Events, workflow definitions, policy, identity, approvals, and orchestration deciding what may run.
6. **Pipeline execution plane?** Runners, tools, networks, caches, and target APIs doing the work.
7. **Pipeline as code?** Versioned, reviewed delivery logic; it remains privileged executable code.
8. **Build once?** Produce one immutable artifact and promote its digest rather than rebuilding per environment.
9. **Gate?** Explicit evidence-based decision that blocks, warns, or permits progression.
10. **Green pipeline proves?** Only that configured work reported success in that execution context—not correctness or trust.

## Testing, artifacts, and evidence

1. **Test portfolio?** Complementary unit, integration, contract, end-to-end, performance, security, and resilience evidence.
2. **Test pyramid value?** More fast focused tests with fewer expensive broad tests; topology depends on system risk.
3. **Flaky-test harm?** Destroys signal, delays flow, and trains people to ignore or rerun failures.
4. **Hermetic build?** Declared, controlled inputs isolated from undeclared environment/network variation.
5. **Reproducible build?** Same inputs and process can yield bit-for-bit equivalent output.
6. **Artifact digest?** Content-derived immutable identity; unlike a tag, it changes when content changes.
7. **SBOM?** Inventory of components and relationships, not proof they are safe or untampered.
8. **Provenance?** Attested information about source, builder, inputs, and process producing an artifact.
9. **Attestation limit?** Trust is bounded by signer identity, builder integrity, policy, and completeness of claims.
10. **Cache versus artifact?** Cache accelerates recomputation and may be disposable; artifact is a governed release output.

## Security and runners

1. **OIDC federation benefit?** Short-lived claim-bound cloud credentials instead of stored long-lived keys.
2. **AWS trust-policy focus?** Issuer, audience, repository/organization, ref or protected environment, and least privilege.
3. **Workflow-token default?** Read-only, with minimal permissions granted per job.
4. **Fork workflow risk?** Attacker-controlled code may target tokens, secrets, networks, caches, or privileged outputs.
5. **`pull_request_target` concern?** Privileged base context becomes dangerous if it executes fork-controlled content.
6. **SHA pinning?** Prevents silent tag movement but does not prove the pinned code is benign.
7. **Hosted runner strength?** Ephemeral clean environment with low operational burden for most workloads.
8. **Persistent runner risk?** Cross-job state, credential theft, poisoned tools/cache, and network persistence.
9. **Environment protection?** Target-scoped approvals, branches, waits, secrets, and policy before privileged deployment.
10. **Secret in log response?** Revoke/rotate, restrict evidence, scope impact, then fix the exposure path.

## Deployment and compatibility

1. **Rolling deployment?** Replace instances gradually; old/new versions coexist and must remain compatible.
2. **Blue/green?** Prepare a parallel environment and switch traffic; costs capacity but enables fast fallback.
3. **Canary?** Expose a representative bounded cohort, compare explicit signals, then promote or abort.
4. **Feature flag?** Runtime exposure control with owner, default, telemetry, security model, and expiry.
5. **GitOps?** Reconciliation of actual state toward versioned desired state; not itself a traffic strategy.
6. **Expand–migrate–contract?** Add compatible structure, move data/consumers, then remove obsolete structure later.
7. **Rollback limit?** New data/schema/external effects may make the previous binary unsafe.
8. **Roll-forward?** Correct current state with a new compatible change when reversal is slower or impossible.
9. **Canary signal set?** Technical SLOs plus correctness and business outcomes against a relevant baseline.
10. **Post-deploy verification?** Confirm exact digest/config, target health, customer outcomes, and stable steady state.

## Operations and leadership

1. **Lead time?** Time from change commitment to successfully running for customers; define start/end consistently.
2. **Deployment frequency?** Rate of successful production changes, interpreted with value, size, and reliability.
3. **Change failure rate?** Proportion of changes causing degradation or remediation under a stable definition.
4. **Recovery time?** Time to restore customer service, not merely to close the pipeline incident.
5. **Safe retry?** Re-read state and repeat only idempotent or uniquely keyed operations with bounded backoff.
6. **Concurrency group?** Scope that serializes/cancels competing runs for a shared mutable target.
7. **Partial deploy response?** Establish actual target state before completing, restoring, or routing around it.
8. **Manual approval value?** Contextual risk judgment using artifact, evidence, target, and health—not ritual waiting.
9. **Break-glass?** Time-bound least privilege, explicit authority, audit, verification, and prompt reconciliation.
10. **Principal-level close?** Decision, trade-off, evidence, risk, owner, measurable next step, and review date.
