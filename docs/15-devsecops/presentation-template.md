# Ten-Minute Secure-Delivery Architecture Review

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

## Minute 0–1 — Outcome and risk

State business service, assets, adversaries, exposure, regulations, delivery
constraints, recovery objectives, and assumptions.

## Minute 1–3 — Threat and trust model

Show source, contributor, dependency, runner, build, cache, registry, signing,
deployment, admission, and runtime boundaries. Name authoritative owners.

## Minute 3–5 — Protected delivery

Explain repository controls, workload identity, ephemeral runners, input pinning,
assurance tests, artifact digest, SBOM, provenance, signing, and promotion.

## Minute 5–6 — Release policy

Define decision inputs, enforcement points, warn/block behavior, exceptions,
availability, degraded mode, and break-glass.

## Minute 6–7 — Cloud and runtime

Cover AWS/ECR/EKS and organization controls, then translate identity, registry,
admission, posture, and evidence to Azure and Google Cloud.

## Minute 7–8 — Incident and recovery

Walk through compromised builder, dependency, signer, registry, or policy:
contain, preserve, enumerate artifacts, quarantine, restore trust, rebuild, verify.

## Minute 8–9 — Adoption

Describe risk tiers, paved workflows, pilot, advisory mode, enforcement waves,
legacy exceptions, security champions, and retirement criteria.

## Minute 9–10 — Measures and decision

Use exposure age, fix deployment time, recurrence, evidence coverage, false
positives, exception age, recovery, and delivery impact. Close with trade-off and
next validation.

Return to the [module overview](index.md) when ready to continue.
