# Scenario Questions and Model Answers

[← Module overview](index.md) ·
[Scenario answer framework](../interview-playbook/scenario-answer-framework.md)

Answer each aloud before reading the model answer. State context, evidence,
uncertainty, risk, trade-off, decision authority, action, and validation.

## 1. Leadership wants a Well-Architected certification

**Model answer:** Explain that the review is not a certification or guarantee. Define
the desired business outcome—risk visibility, production readiness, or improvement—
and the workload scope. Produce an evidence-backed risk and action record with dated
framework context. If external assurance is required, identify the appropriate audit,
attestation, or certification process separately.

## 2. The AWS Tool shows no high-risk issues

**Model answer:** Check answer age, scope, evidence, lenses, environment, and who
completed it. Walk current journeys, incidents, tests, SLOs, and configuration.
“No issue” based on intent or stale answers is not assurance. Create a milestone,
correct unsupported answers, and retain evidence references and uncertainty.

## 3. The workload owner says every control is implemented

**Model answer:** Avoid accusation. Ask for representative operational evidence:
failure tests, restore results, incident records, access review, load tests, and cost
allocation. Sample critical claims by risk. Record gaps as unverified rather than
absent, assign evidence follow-up, and escalate only active material exposure.

## 4. A review finds 80 recommendations

**Model answer:** Consolidate duplicates by business risk and system cause. Separate
containment, investigation, foundation, quick improvement, strategic redesign, and
accepted risk. Prioritize consequence, exposure, confidence, dependencies, and effort.
Commit a small funded set with owners and validation; retain the rest transparently.

## 5. A best practice conflicts with a regulatory requirement

**Model answer:** The obligation and business context take precedence over a generic
recommendation. Confirm applicability with compliance/legal expertise, document the
constraint, compare compliant alternatives across pillars, record the decision and
residual risk, and consider a custom lens or organization standard for future reviews.

## 6. Cost optimization proposes removing DR capacity

**Model answer:** Bring the approved BIA, RTO/RPO, recovery tests, and actual capacity
into the review. Model tiered or scaled standby options, but do not label required
resilience as waste. Record the cost/reliability trade-off and require the business
risk owner to change the objective before reducing capability.

## 7. Security and delivery leaders disagree on release gates

**Model answer:** Restate shared outcomes and threat/change evidence. Compare preventive
gates with automated tests, signed artifacts, progressive delivery, detection, and
rollback. Measure lead time and escaped risk. Create a proportionate control by risk,
record dissent and decision authority, then validate both security and delivery outcomes.

## 8. A managed service is assumed to solve reliability

**Model answer:** Clarify shared responsibility and service-specific behavior. Examine
configuration, quotas, client retries/timeouts, zonal/regional design, backup, maintenance,
dependencies, observability, and recovery tests. Managed operation reduces some work;
it does not automatically meet the workload SLO or recovery objective.

## 9. Azure and AWS assessments produce different scores

**Model answer:** Do not compare raw scores. Align workload scope, quality objectives,
review date, evidence, pillar semantics, and risk model. Consolidate common business
risks while retaining provider-specific controls. Report decisions and exposure, not
a synthetic cross-cloud average.

## 10. An executive wants the review completed in one hour

**Model answer:** Offer a scoped triage, not a comprehensive review. Focus on context,
critical journey, top known risks, recent incidents, and evidence gaps. Label confidence
and exclusions, identify any urgent escalation, and propose focused follow-ups with
owners. Never imply full coverage from a time-boxed conversation.

## 11. A serious exposure appears during the session

**Model answer:** Stop normal review flow and follow the security or incident process.
Limit sensitive discussion, preserve evidence, notify authorized responders, and avoid
uncontrolled remediation. Record only appropriately classified review metadata and
resume the review when containment and disclosure rules permit.

## 12. The product launch precedes remediation

**Model answer:** Quantify the launch value and risk consequence, existing controls,
confidence, and time. Identify minimum containment, monitoring, rollback, support, and
post-launch actions. The authorized owner decides delay, scope reduction, guarded launch,
or acceptance; capture expiry and triggers. The reviewer does not silently approve.

## 13. Teams game the framework score

**Model answer:** Stop using raw scores for performance comparison. Audit a sample of
answers against evidence, reframe success around risk reduction and workload outcomes,
protect teams from punitive ranking, and track finding age, validated remediation,
incidents, SLOs, security, delivery, and unit value instead.

## 14. A vendor reviewer recommends only its own services

**Model answer:** Disclose the conflict, return to requirements and options, ask for
evidence and trade-offs, and include platform-independent or alternative designs.
Separate framework alignment from purchase decisions. Escalate procurement or ethics
concerns if incentives compromise review independence.

## 15. Remediation tickets close but incidents continue

**Model answer:** Reopen outcome validation. Check whether tickets changed the real
failure path, whether evidence and environment matched, and whether common causes such
as ownership, platform defaults, or incentives remain. Update ADRs/tests, validate under
representative conditions, and track incident/SLO outcomes rather than closure count.

Return to the [module overview](index.md) when ready to continue.
