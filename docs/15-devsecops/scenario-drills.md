# Advanced Supply-Chain Incident Drills

[← Module overview](index.md) ·
[Scenario answer framework](../interview-playbook/scenario-answer-framework.md)

For each drill, state first containment, evidence, affected population, decision
owner, recovery, communication, and prevention.

## 1. Protected workflow file was maliciously changed

Revoke release identities, stop builds, preserve repository/audit evidence,
enumerate artifacts and deployments since the change, quarantine them, restore
reviewed workflow, rebuild on trusted runners, and strengthen workflow ownership.

## 2. Package registry serves a poisoned dependency

Freeze affected resolution, identify locked and cached versions, query SBOMs and
deployments, block the digest/version, rebuild from trusted sources, rotate
credentials if code executed, and improve namespace, mirror, and integrity policy.

## 3. Signing identity issued artifacts from an unknown repository

Stop admission for the identity/claim pattern, preserve transparency and IdP logs,
revoke trust where possible, identify consumers, and rebuild. Tighten issuer,
subject, audience, repository, workflow, and environment verification.

## 4. Registry tags were moved after approval

Resolve deployed digests, block the substituted digest, restore services with the
approved artifact, and investigate registry authority. Enforce immutable tags,
digest promotion, separate publication/admin rights, and admission by digest.

## 5. SBOM generator omitted copied binaries

Identify artifacts built by the faulty pipeline, scan/extract final images,
update exposure decisions, regenerate evidence, and notify owners. Add generator
validation, multiple evidence sources, and completeness tests.

## 6. Admission policy was changed to allow all

Restore reviewed policy, preserve audit logs, identify deployments admitted in
the window, verify/quarantine them, revoke policy authority, and separate policy
change, deployment, and emergency roles.

## 7. Zero-day affects the CI runner operating system

Stop sensitive jobs, isolate and patch/replace runners, revoke credentials,
enumerate produced artifacts, preserve forensic evidence, rebuild on clean images,
and validate ephemeral lifecycle and egress controls.

## 8. Scanner database falsely marks critical production images safe

Correct the intelligence source, query immutable artifacts with another validated
source, reprioritize deployed exposure, contain and rebuild affected workloads,
and add feed freshness, diversity, and failure alarms.

## 9. Break-glass exception token is leaked

Revoke it, stop or review all bypass activity, preserve identity/policy logs,
verify affected deployments, rotate related trust, and replace broad reusable
bypass with short-lived, scoped, approved, dual-observed emergency authorization.

## 10. Cloud organization guardrail blocks disaster recovery

Activate the approved DR authority, restore the minimum safe capability, record
changes, and validate services. Reconcile normal policy afterward and add DR
simulation, regional dependencies, and tested exception scope.

Return to the [module overview](index.md) when ready to continue.
