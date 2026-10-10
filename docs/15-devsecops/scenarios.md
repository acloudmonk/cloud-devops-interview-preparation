# Scenario Questions and Model Answers

[← Module overview](index.md) ·
[Scenario answer framework](../interview-playbook/scenario-answer-framework.md)

Answer aloud before reading. State assumptions, trust boundary, containment,
recovery, evidence, owner, and measurable improvement.

## 1. Critical CVE appears in thousands of images

**Model answer:** Validate affected versions, query SBOM/artifact and deployment
inventory, then prioritize known exploitation, reachability, exposure, privilege,
and service impact. Contain exposed critical workloads, rebuild from fixed inputs,
promote one verified digest, and confirm deployed replacement. Track exposure age
and root cause rather than opening identical unowned tickets.

## 2. A secret is committed to a public repository

**Model answer:** Revoke first, preserve audit evidence, determine permissions,
use, forks, logs, artifacts, and exposure window, then rotate dependents. Remove
from history where useful, but assume copied. Replace static secret delivery with
short-lived workload identity/runtime retrieval and add format-specific detection.

## 3. Security wants every scanner to block every pull request

**Model answer:** Map scanners to threats, confidence, context, and feedback stage.
Block high-confidence preventable risk; enrich and deduplicate other evidence.
Use advisory rollout, service risk tiers, tested exceptions, and later independent
verification. Measure escaped exposure and false positives, not alerts generated.

## 4. An image is signed, so leadership calls it secure

**Model answer:** A signature proves integrity and an asserted signer under a
trust policy; it does not prove safe source, dependencies, build, or behavior.
Require expected identity/claims, protected provenance, SBOM and relevant tests,
then verify the exact digest at release/admission. Protect the signing authority.

## 5. A shared runner may be compromised

**Model answer:** Stop protected releases, isolate the runner, revoke job and
signing credentials, preserve disk/image/log/cache evidence, and enumerate
artifacts produced during the exposure. Quarantine or block them, rebuild on a
trusted ephemeral platform, verify consumers, and redesign tenant/egress/cache isolation.

## 6. Admission verification service is unavailable

**Model answer:** Apply the documented threat-specific degraded mode: trusted
cached bundles or a narrow audited emergency path, never an improvised global
allow. Protect critical platform recovery workloads, restore verification, review
everything admitted during degradation, and test availability regularly.

## 7. SCA reports a critical package that is unreachable

**Model answer:** Validate version and reachability evidence, but also consider
exposure, exploit maturity, future code paths, and evidence confidence. A scoped,
expiring exception with monitoring may be reasonable; upgrade when feasible.
Record why severity alone did not determine the decision.

## 8. Terraform policy blocks an emergency containment change

**Model answer:** Use a bounded break-glass path authorized by the incident owner,
contain the active exposure, record exact mutations and expiry, then update the
authoritative IaC and reconcile state. Review whether policy needs a tested
emergency mode without weakening routine enforcement.

## 9. Developers request production secrets in pull-request jobs

**Model answer:** Refuse because untrusted code can exfiltrate them. Split
untrusted validation from protected post-merge/release workflows, use ephemeral
runners and short-lived claim-bound identity, and provide synthetic or isolated
test data. Test fork and workflow-change attacks.

## 10. Teams generate SBOMs but cannot answer exposure questions

**Model answer:** Bind each SBOM to an artifact digest, store it durably, normalize
formats/components, and connect artifact to deployment inventory and owner.
Measure coverage and query time. Generation without distribution, correlation,
freshness, and response workflow is incomplete.

## 11. A base image is removed from its registry

**Model answer:** Pause builds, identify source and previously built digests,
verify whether removal signals compromise, preserve trusted copies/evidence, and
assess dependent artifacts. Move to approved mirrored/pinned bases with ownership,
retention, update policy, and tested replacement.

## 12. A policy rollout blocks system workloads

**Model answer:** Halt expansion, use the approved recovery exemption, restore
critical services, preserve admission decisions, and classify coverage/test gaps.
Introduce namespace/workload risk tiers, dry-run evidence, representative system
tests, versioned policy, and an expiring exemption contract.

## 13. A dependency update fixes a CVE but breaks compatibility

**Model answer:** Compare exploit risk and service failure risk. Test the upgrade,
seek alternate fixed versions or backport, add temporary compensating controls,
monitor exploitation, and obtain time-bound risk acceptance. Fix deployment—not
ticket closure—is the completion condition.

## 14. Multi-cloud teams demand identical security products

**Model answer:** Standardize outcomes and evidence contracts—identity, protected
build, artifact digest, provenance, admission, findings, exceptions, and response.
Map AWS, Azure, and GCP native controls where semantics differ. Forced product
uniformity can reduce native integration and create unsupported gaps.

## 15. A legacy service cannot meet provenance policy

**Model answer:** Classify criticality and exposure, document the missing trust
guarantee, constrain publication/deployment, add compensating review and signing,
and create an owned migration deadline. Enforce provenance for new artifacts while
tracking legacy exceptions and preventing expansion.

Return to the [module overview](index.md) when ready to continue.
