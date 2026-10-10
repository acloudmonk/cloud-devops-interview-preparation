# Delivery-System Mental Model

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

## Separate the terms

| Capability | Meaning |
| --- | --- |
| Continuous integration | Frequently combine small changes and produce fast evidence about the integrated state |
| Continuous delivery | Keep a verified release candidate deployable through an automated path; production may require a decision |
| Continuous deployment | Automatically deploy every qualifying change to production |
| Deployment | Install/activate a version in an environment |
| Release | Make behavior available to intended users or consumers |
| Exposure | Gradually change which users/traffic experience released behavior |

A deployment can occur without release through feature flags. A release can
change exposure without deploying new code. This separation makes recovery
faster and reduces high-risk coupled events.

## Trace one immutable release unit

```mermaid
flowchart LR
    S[Reviewed source revision] --> B[Hermetic build]
    B --> A[Immutable artifact]
    A --> E[Evidence + provenance]
    E --> P[Promotion decision]
    P --> D[Deployment]
    D --> V[Verification]
    V --> R[Release / exposure]
    R --> O[Operational feedback]
```

At every arrow, identify identity, input, immutable output, authorization,
evidence, retention, retry/idempotency, and failure recovery.

## Control plane and execution plane

The control plane stores workflow definitions, triggers, policy, credentials,
approvals, desired versions, and history. The execution plane runs untrusted or
trusted jobs and deployments. Separate their permissions and failure domains.

A green control-plane run does not prove the correct artifact is serving real
traffic. Verify the artifact identity and customer outcome in the target.

## Delivery invariants

Strong systems preserve these properties:

- the promoted artifact is exactly the tested artifact;
- evidence refers to the exact source, workflow, dependencies, builder, and artifact;
- no single untrusted change can both alter and approve its trust controls;
- credentials are short-lived, scoped, and unavailable to untrusted execution;
- deployments are repeatable, observable, idempotent where possible, and recoverable;
- concurrent changes cannot silently overwrite a newer desired state;
- manual decisions record identity, evidence, scope, time, and reason.

## Feedback versus assurance

Move cheap deterministic checks early and expensive environment/system evidence
later. Parallelize independent work, avoid duplicating the same evidence, and
use risk to decide what blocks. A pipeline optimized only for speed creates
failures; one optimized only for gates drives bypass and batch size.

## Failure classifications

Classify failures as source/test defect, workflow/configuration defect, worker or
dependency outage, artifact/evidence problem, policy/approval issue, deployment
or target failure, verification failure, or release/exposure failure. This
determines ownership and safe retry.

## Strong interview answer

Start with deployment/release outcomes and constraints. Draw source-to-customer
flow, name trust and state boundaries, define evidence and authorization, choose
progressive risk controls, explain failure recovery, and give measurable success
criteria such as lead time, deployment frequency, failed-change rate, and recovery time.
