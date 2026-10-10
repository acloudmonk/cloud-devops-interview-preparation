# SBOMs, Provenance, Attestations, and Signing

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Artifact assurance requires precise questions. A digest identifies bytes; a
signature binds a signer or identity to a statement; provenance describes how an
artifact was built; an SBOM inventories components; policy decides whether the
evidence is acceptable.

## Evidence model

- **Digest:** immutable content identity, not trust.
- **Signature:** integrity and asserted signer identity, not code safety.
- **SBOM:** component inventory for analysis and response, not vulnerability proof.
- **Provenance:** builder, source, inputs, parameters, and output relationship.
- **Attestation:** signed statement about an artifact, test, scan, or process.
- **Verification policy:** expected issuer, subject, repository, workflow, builder,
  predicate, freshness, and artifact digest.

Store evidence alongside immutable artifacts through supported OCI or attestation
mechanisms. Preserve association by digest and define retention, access, and
availability for incident response.

## SLSA reasoning

SLSA provides progressive build and source integrity expectations. Treat a level
as evidence about defined requirements, not a universal security grade. Map the
exact threat and requirement being satisfied, verify provenance rather than only
generating it, and record unsupported gaps.

## Keyless and key-managed signing

Keyless signing exchanges a trusted workload identity for a short-lived signing
certificate and transparency evidence. It reduces long-lived key custody but
depends on the identity provider, trust root, claim policy, timestamp/log
availability, and verification implementation. Key-managed signing depends on
secure generation, hardware or KMS custody, rotation, authorization, and revocation.

## Verification failure

Decide behavior for unavailable transparency service, expired certificate,
revoked trust root, missing provenance, mismatched digest, or unknown predicate.
Cache trustworthy verification material where appropriate and maintain an
audited, scoped, expiring emergency path. Do not silently change deny to allow.

## Artifact promotion

Promote the same digest between environments rather than rebuilding. Attach or
reference evidence from the protected build, record approvals and environment
decisions separately, and verify again at deployment/admission.

Return to the [module overview](index.md) when ready to continue.
