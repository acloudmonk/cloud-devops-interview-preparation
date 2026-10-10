# Enterprise DevSecOps Design Exercise

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

This is a paper exercise. Design decisions, trust, evidence, recovery, adoption,
and measurable outcomes matter more than product names.

## Scenario

A regulated company has 500 repositories, shared persistent runners, long-lived
AWS keys, inconsistent scanners, mutable image tags, no reliable SBOM/provenance,
and manual production approvals. Critical findings create thousands of tickets,
but teams cannot identify deployed exposure. EKS is primary; AKS and GKE adoption
is growing. A compromised dependency recently reached staging.

## Deliverables

1. **Discovery:** assets, data, threats, delivery paths, identities, builders,
   artifact stores, deployments, regulations, incidents, owners, and recovery.
2. **Threat model:** source, dependency, runner, cache, build, registry, signing,
   deployment, admission, and runtime trust boundaries.
3. **Responsibility map:** product, platform, security, risk owner, and incident roles.
4. **Protected build:** review, ephemeral runner, egress, federation, reproducible
   inputs, evidence, signing, publication, and isolation.
5. **Assurance strategy:** SAST, SCA, secrets, DAST, IaC, image, API, and manual
   review placed by risk and feedback speed.
6. **Artifact contract:** digest, SBOM, provenance, attestations, signature,
   retention, promotion, and consumer verification.
7. **Release policy:** risk inputs, warn/block, admission, exceptions, degraded
   mode, break-glass, and recovery.
8. **Vulnerability response:** deployed inventory, prioritization, containment,
   rebuild, rollout, verification, disclosure, and root-cause feedback.
9. **Migration:** pilot, legacy evidence, paved workflow, enforcement waves,
   exceptions, training, and retirement criteria.
10. **Measures:** exposure age, fix deployment time, recurrence, coverage,
    false positives, exception age, recovery, and delivery impact.

## Decision worksheets

| Trust boundary | Threat | Prevent | Detect | Contain/recover | Evidence owner |
| --- | --- | --- | --- | --- | --- |
| Example: release builder | persistent compromise | ephemeral isolated runner | integrity/runtime alert | stop releases and rebuild | platform security |

| Policy decision | Inputs | Enforce where | Failure mode | Exception owner |
| --- | --- | --- | --- | --- |
| Production image admission | digest, provenance, signer, scan | deployment and cluster | deny with tested emergency path | service risk owner |

## Review rubric

Score 0–4 for discovery, threat-to-control traceability, build trust, artifact
evidence, release policy, incident recovery, AWS/multi-cloud depth, adoption,
measures, and executive communication. A strong answer explains limitations and
does not treat tool installation as risk reduction.

Return to the [module overview](index.md) when ready to continue.
