# Remediation and Continuous Governance

[← Module overview](index.md) · [Facilitation](facilitation.md)

A review creates value only when material findings lead to a decision and verified
outcome. Closing a ticket or changing a questionnaire answer is not evidence that risk fell.

## Improvement plan

Group findings into:

- immediate containment for active or intolerable exposure;
- quick improvements with high value and low coupling;
- foundational enablers that unlock several remediations;
- strategic architecture changes requiring roadmap and funding;
- investigation where evidence is insufficient;
- explicitly accepted, transferred, avoided, or deferred risk.

For each item record outcome, owner, sponsor, target, dependencies, effort range,
quality guardrails, evidence of completion, and validation date. Avoid creating a
separate review backlog that product and engineering planning never sees.

## Validation

Validate the control and the workload outcome. Evidence may include configuration,
automated policy, threat or failure tests, load tests, SLO trends, restore exercises,
incident reduction, unit cost, deployment results, or operator rehearsal. Confirm no
cross-pillar regression and update architecture diagrams, ADRs, runbooks, and inventory.

## Continuous review triggers

- new workload or production readiness;
- major architecture, Region, provider, data, identity, or supplier change;
- critical incident, near miss, threat change, or audit finding;
- material demand, SLO, regulatory, cost, or business-model change;
- platform/framework/service evolution that changes an earlier assumption;
- risk-exception expiry or scheduled milestone.

Use lightweight change-path reviews for bounded decisions and deeper periodic reviews
for the whole workload. Reusing evidence and automating configuration checks reduces fatigue.

## Portfolio governance

Maintain workload inventory, owner, criticality, last review, review depth, top risk,
overdue actions, exception expiry, and next trigger. Aggregate themes to improve landing
zones, paved roads, policies, training, and funding. Do not rank teams publicly by raw
framework score; scope and maturity differences make the comparison misleading.

## Closure criteria

A finding closes when agreed evidence demonstrates the risk is reduced to the target,
an authorized owner accepts residual risk, the workload records are updated, and any
new consequence is understood. Reopen it when the evidence expires or assumptions change.

## Feedback loop

Review recurring findings for system causes: unclear ownership, weak platform defaults,
missing skills, conflicting incentives, funding gaps, or standards that do not fit.
Improve the environment rather than repeatedly asking each team to solve the same problem.

Return to the [module overview](index.md) when ready to continue.
