# DevSecOps Rapid-Fire Revision

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Answer each in 20–40 seconds with one limitation or failure mode.

## Operating model and threats

1. **DevSecOps?** Shared secure-delivery ownership with automated evidence, decisions, response, and feedback.
2. **Shift-left limitation?** Early feedback is useful but bypassable and lacks deployment/runtime context.
3. **Threat model output?** Owned threats, requirements, mitigations, tests, assumptions, and accepted risk.
4. **Trust boundary?** Point where identity, authority, data, or assurance assumptions change.
5. **Prevent versus detect?** Stop the event versus discover it; both need response and recovery.
6. **Scanner versus decision?** Evidence with uncertainty versus context-aware allow, block, warn, or exception.
7. **Risk owner?** Person authorized to accept residual business risk, not the scanner operator.
8. **Security champion?** Product-aligned facilitator, not a replacement for security or engineering ownership.
9. **Control placement rule?** Earliest reliable feedback plus later independent verification.
10. **Useful metric?** Reduced critical deployed exposure and recurrence, not alerts created.

## Code and build

1. **SAST?** Static source analysis; limited by rules, language, flow, and runtime context.
2. **SCA?** Component and known-vulnerability analysis; presence is not proof of exploitability.
3. **DAST?** External testing of a running interface; limited by reachable behavior and coverage.
4. **Secret detection response?** Revoke, investigate, rotate, remove, redesign delivery, verify.
5. **Dependency confusion defense?** Govern namespaces/registries, lock and verify integrity, constrain resolution.
6. **Protected branch value?** Review and change policy; administrators and stolen identities remain threats.
7. **Ephemeral runner?** Clean short-lived execution destroyed after the job to reduce persistence.
8. **OIDC workload identity?** Short-lived credential bound to verified pipeline claims.
9. **Cache threat?** Untrusted or cross-tenant data can alter builds or exfiltrate secrets.
10. **Hermetic build?** Build constrained to declared inputs; it does not prove inputs are safe.

## Artifact evidence

1. **Digest?** Immutable content identifier, not a trust statement.
2. **Signature?** Integrity plus signer assertion under a verification policy, not safety proof.
3. **SBOM?** Component inventory bound to an artifact; not a vulnerability verdict.
4. **Provenance?** Verifiable statement of source, builder, inputs, process, and output relationship.
5. **Attestation?** Signed statement about an artifact or process property.
6. **SLSA?** Progressive supply-chain integrity requirements, not a universal security grade.
7. **Keyless signing?** Short-lived certificate binds ephemeral key to federated identity and transparency evidence.
8. **Verification policy?** Expected issuer, subject, claims, builder, predicate, digest, and freshness.
9. **Promotion rule?** Promote the same verified digest; do not rebuild per environment.
10. **Evidence outage?** Use designed cache/degraded/emergency behavior, never silent allow.

## Cloud and policy

1. **Image scan timing?** Scan final image on build/push and rescan on new intelligence.
2. **Mutable-tag risk?** Approved name can later resolve to different bytes.
3. **Admission value?** Independent final preventive check with environment context.
4. **Admission risk?** Availability, bootstrap, bypass, policy compromise, and recovery.
5. **IaC static scan limitation?** Computed values and actual plan/runtime state may be unknown.
6. **Posture remediation rule?** Change authoritative source; use emergency mutation only to contain active risk.
7. **SCP purpose?** Coarse AWS organization guardrail, not complete workload authorization.
8. **Exception contract?** Scope, owner, reason, risk, compensation, evidence, expiry, remediation.
9. **Fail-open versus closed?** Business availability trade-off against threat impact; decide and rehearse explicitly.
10. **Multi-cloud standardization?** Common outcomes/evidence with cloud-native implementation mappings.

## Response and leadership

1. **CVSS limitation?** Technical severity omits deployment, exposure, reachability, controls, and business impact.
2. **KEV use?** Known exploitation signal that raises priority; still map affected deployed assets.
3. **Fix completion?** Corrected artifact is verified as deployed and exposed old versions are removed.
4. **Build compromise first step?** Stop releases, isolate builder, revoke authority, preserve evidence.
5. **Blast-radius query?** Which artifacts were built, where deployed, which identities/data they reached.
6. **Trust recovery?** Restore identities, builders, inputs, policy, and verification before rebuilding.
7. **Disclosure program?** Intake, triage, safe communication, ownership, timeline, advisory, monitoring.
8. **False-positive cost?** Bypass pressure, delay, wasted work, and loss of trust in real findings.
9. **Principal-level measure set?** Exposure, fix time, recurrence, coverage, exception age, recovery, delivery impact.
10. **Executive close?** Threats, bounded trust, evidence, decision, recovery, adoption, measures, next investment.

Return to the [module overview](index.md) when ready to continue.
