# Registries and Container Supply-Chain Controls

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

A registry is a release-system boundary. It stores content-addressed manifests,
indexes, configurations, and layers; controls who may publish or consume them; and
retains metadata needed to prove which artifact reached a runtime.

## Names, tags, and digests

`registry/namespace/repository:tag` is a human-friendly reference. A tag can move.
A digest identifies manifest content and is the correct deployment identity. Record
both when useful: the tag communicates release meaning, while the digest proves
exact bytes.

A multi-platform tag may resolve to an OCI image index; each platform manifest has
its own digest. Verification should understand whether policy applies to the index,
each image, or both.

## Build once, promote by identity

Build and verify one image, then promote the same digest through environments.
Copying between registries or accounts must preserve content identity and associated
signatures/attestations. Rebuilding per environment introduces new inputs and makes
earlier test evidence inapplicable.

On AWS, use Amazon ECR repositories with narrow push/pull policies, immutable tags
where appropriate, encryption, audit logs, lifecycle policies, scanning, and
cross-account/region architecture based on recovery needs. ECS task definitions and
EKS workloads should resolve the intended digest even if a release tag is retained
for humans.

Azure Container Registry and Google Artifact Registry provide comparable identity,
replication, scanning, access, and retention capabilities. Translate policy rather
than assuming identical defaults.

## Evidence portfolio

Connect the image digest to:

- reviewed source revision and build definition;
- base-image and dependency digests/locks;
- builder identity and provenance attestation;
- SBOM and license/vulnerability findings;
- signature or keyless workload identity;
- test and policy results;
- environment approval and deployment record.

An SBOM is an inventory, scanning is a time-bound finding set, a signature binds an
identity to content, and provenance makes claims about creation. None alone proves
the image is secure or correct.

## Vulnerability decisions

Separate presence, exploitability, reachability, fix availability, business impact,
and compensating controls. Define severity/age policies, documented exceptions with
owners and expiry, rescanning when intelligence changes, and base-image rebuild
cadence. A scan at build time does not cover vulnerabilities disclosed tomorrow.

Do not “fix” a library in a running container. Rebuild from controlled inputs,
produce a new digest/evidence set, and redeploy.

## Registry resilience and lifecycle

Design authentication/token flow, pull-through cache trust, replication lag,
rate limits, deletion protection, garbage collection, and regional outage behavior.
Retain every digest required for running workloads, rollback windows, audit, and
incident investigation. Test restore or replication, not just configuration.

Lifecycle policy must understand tags and untagged manifests, multi-platform indexes,
signatures/attestations, and active runtime references. Deleting an “untagged” child
manifest can break a retained index or recovery path if the registry permits it.

## Admission and runtime verification

Policy can require approved registry/repository, digest pinning, trusted signer or
provenance identity, acceptable vulnerability/exception state, and platform match.
Fail-open versus fail-closed behavior must follow workload risk and control-plane
availability. Preserve an audited, constrained continuity procedure for emergencies.
