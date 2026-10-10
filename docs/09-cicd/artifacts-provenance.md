# Artifacts and Provenance

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

## Build once, promote many

Build the release unit once in a controlled environment, identify it by immutable
digest, attach evidence, and promote that exact digest through environments.
Rebuilding for production can change dependencies, timestamps, tools, base
images, or generated content and invalidates earlier evidence.

Environment-specific behavior belongs in separately controlled configuration,
secrets, and runtime flags—not a rebuild of application code.

## Artifact lifecycle

```mermaid
flowchart LR
    C[Source commit] --> B[Builder identity + inputs]
    B --> A[Artifact digest]
    A --> M[Metadata / SBOM / attestations]
    M --> Q[Policy decision]
    Q --> P[Promotion pointer]
    P --> D[Deployment record]
```

Record source revision, workflow revision, builder, dependency lock state,
timestamps, artifact digest, test/security evidence, approval, environment, and
deployment result. Prefer machine-verifiable links over mutable filenames.

## Artifact repository controls

- reject overwrite of released versions/tags;
- separate write, promote, read, delete, and retention permissions;
- scan and sign without allowing scanners to replace content;
- replicate/backup according to delivery recovery objectives;
- define quarantine and revocation behavior;
- protect metadata and tags from pointing to a different digest;
- retain evidence long enough for support, audit, and rollback policy.

## Provenance and attestations

Provenance describes how an artifact was produced. An attestation is a signed
statement about a subject such as an artifact digest. Trust depends on the
builder identity, isolation, input capture, signing-key lifecycle, verification
policy, and protection against a workflow approving itself.

An SBOM inventories components; it does not prove absence of vulnerabilities or
that the declared components produced the artifact.

## Reproducibility and hermeticity

Hermetic builds constrain undeclared network/tool/input dependencies.
Reproducible builds allow independent builds to produce the same result under
defined conditions. Both improve confidence but require deterministic tooling,
pinned inputs, time/locale handling, and verification ownership.

## Caches are not artifacts

Caches accelerate work and may be replaceable; artifacts are intended outputs
with identity, retention, and promotion semantics. Cache keys must include all
material inputs, and untrusted jobs must not poison privileged caches.

## Rollback retention

Retain deployable artifacts, compatible configuration/schema expectations, and
verification evidence for the rollback window. An old binary alone is not a
rollback if the database or external contract has moved incompatibly forward.
