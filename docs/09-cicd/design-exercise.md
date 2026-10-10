# Design Exercise: Governed Multi-Account Delivery

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

Use this no-code exercise to turn the module into an interview-ready design.
Complete it on paper or in a Markdown note; the deliverable is reasoning, not a
working pipeline.

## Brief

A company runs 40 services on Amazon ECS across development, staging, and
production AWS accounts. Source and pull requests are in GitHub. Ten teams deploy
about 60 times per day. Production is multi-region; checkout is revenue-critical.

Current problems:

- long-lived AWS keys are stored as repository secrets;
- every branch builds a new container and mutable tags are promoted;
- production approval happens in chat with no durable artifact identity;
- one persistent self-hosted runner pool serves forks and production;
- database migration runs during service startup;
- a failed regional deployment is often rerun without checking partial state;
- teams cannot explain which source, tests, and approvals produced a deployment.

Constraints: no regular outage, auditable separation of duties, ten-minute recovery
objective for a bad application release, and no mandate to replace GitHub Actions.

## Your deliverable

Draw and explain:

1. event, workflow, runner, identity, artifact, policy, deployment, and target
   boundaries;
2. how one reviewed commit produces one immutable digest that moves through all
   environments;
3. test and security evidence, including which gates block and which inform;
4. OIDC trust and least-privilege AWS roles for build and each environment;
5. isolation for forked code, trusted builds, and production deployment;
6. staged ECS rollout, verification signals, promotion thresholds, and abort path;
7. database expand–migrate–contract and feature-flag sequencing;
8. concurrency control, regional failure handling, and recovery ownership;
9. audit evidence and retention;
10. adoption plan and success measures.

## Required decisions

| Decision | State your choice and trade-off |
| --- | --- |
| Trigger and concurrency | Which events run which trust level? How are stale runs stopped? |
| Artifact identity | What is immutable, signed/attested, retained, and promoted? |
| Runner boundary | Which workloads use hosted or ephemeral self-hosted capacity? |
| AWS identity | Which claims may assume which account role? |
| Production strategy | Rolling, blue/green, canary, flags, or a combination—and why? |
| Data change | Where do migrations run and how is compatibility proved? |
| Promotion | Automated/manual decision, evidence, owner, and expiry |
| Recovery | Rollback, roll-forward, exposure removal, or regional stop |

## Evidence matrix

Create a matrix with rows for source review, unit/integration/contract tests,
vulnerability and policy results, SBOM/provenance, artifact digest, approval,
deployment events, canary comparison, and recovery. Columns should identify
producer, trusted identity, storage, consumer, retention, and failure behavior.

## Migration plan

Propose increments that reduce risk independently. A defensible order is inventory
and freeze new static keys; introduce OIDC roles; isolate runner trust; publish by
digest; promote one artifact; add environment evidence; move migrations out of
startup; pilot progressive delivery; then scale with reusable workflows.

For every increment name a pilot, owner, success metric, rollback of the process
change, and exception expiry. Avoid a big-bang platform migration.

## Review rubric

- **Trust:** untrusted code cannot reach privileged credentials or mutable release
  state.
- **Traceability:** source, workflow, evidence, digest, approval, and target are
  connected.
- **Compatibility:** old/new code, data, APIs, messages, and config can overlap.
- **Recovery:** triggers, authority, actions, and verification are executable.
- **Operations:** queue, failure, deployment, and business signals are owned.
- **Adoption:** the design improves developer flow without silent policy bypass.

Finish with a two-minute answer: context, top risks, design, rollout, recovery,
measures, and the first decision required from leadership.
