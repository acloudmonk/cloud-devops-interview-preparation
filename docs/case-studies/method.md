# Case-Study Method

[← Case-study overview](index.md) · [Next: Common scorecard →](scorecard.md)

Use [CLEAR-DOC](../interview-playbook/scenario-answer-framework.md) as the answer
spine. The case method adds time management, artifacts, and failure injects.

## 1. Frame the decision

Restate the business outcome, decision deadline, decision owner, users, current
state, and definition of success. Separate facts, assumptions, constraints, and
unknowns. Ask which risk the organization is prepared to accept.

## 2. Quantify the limits

Establish demand, latency, availability, consistency, RTO/RPO, security and data
classification, residency, retention, budget, skills, dependencies, and delivery
deadline. Identify invariants such as “never bill twice” or “tenant data never
crosses a boundary.” Use ranges when exact data is unavailable.

## 3. Produce options

Offer two or three viable approaches, including “improve the current system” when
credible. Compare time-to-value, failure behavior, security, operations, cost,
lock-in, migration risk, and reversibility. Reject options explicitly.

## 4. Walk the architecture

Describe one request and one state change end to end: identity, edge, API, compute,
data, events, integrations, observability, and operator control. Label trust and
failure boundaries. Name cloud products only after the required capability is clear.

## 5. Defend and operate

Cover threat model, least privilege, secrets, encryption, audit, deployment,
compatibility, SLOs, alerts, runbooks, backup, failover, reconciliation, and on-call
ownership. Explain how the system behaves when dependencies are slow or unavailable.

## 6. Respond to an inject

For each failure: contain, preserve evidence, describe customer impact, identify
likely failure classes, restore safely, verify recovery, communicate, and prevent
recurrence. Do not redesign the whole system before stabilizing it.

## 7. Close the decision

Recommend one option, name assumptions and residual risks, and propose phased
delivery with measurable exit criteria. State the next reversible experiment and
what evidence could change the recommendation.

## Minimum artifacts

- assumptions and non-functional-requirement table;
- context/data-flow diagram with trust and failure boundaries;
- two-option decision record;
- SLI/SLO and recovery table;
- threat and failure-mode notes;
- cost drivers and unit metric;
- phased roadmap, owners, risks, and validation plan.
