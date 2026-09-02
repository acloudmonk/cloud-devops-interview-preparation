# Scenario Answer Framework

Senior architecture interviews test structured judgment under ambiguity. Do not
jump directly to a product name. Establish what success means, expose the
constraints, compare options, and explain how the system will be operated.

## The CLEAR-DOC framework

Use **CLEAR-DOC** to structure an answer without sounding scripted.

| Step | Purpose | Typical questions |
| --- | --- | --- |
| **C — Context** | Establish the business outcome and current state. | Who uses it? What problem are we solving? What exists today? |
| **L — Limits** | Surface constraints and non-functional requirements. | Scale, latency, availability, RTO/RPO, compliance, budget, skills? |
| **E — Evaluate** | Present two or three viable approaches. | What can be managed, built, bought, migrated, or deferred? |
| **A — Architecture** | Describe components, boundaries, and data flow. | Where does state live? What is synchronous? What is asynchronous? |
| **R — Rationale** | Recommend an option and make trade-offs explicit. | Why this option? What are we deliberately not optimizing? |
| **D — Defense** | Explain identity, security, privacy, and compliance. | Least privilege, encryption, segmentation, secrets, audit? |
| **O — Operations** | Cover delivery, observability, resilience, and recovery. | Deployment, SLOs, alerts, rollback, backup, failover, incidents? |
| **C — Cost and change** | Connect economics to an incremental delivery plan. | Cost drivers, unit cost, milestones, risks, validation, exit plan? |

## Minimum non-functional requirements

Clarify these before committing to a design:

- expected users, requests per second, data volume, and growth;
- response-time and throughput objectives;
- availability target and failure-domain requirements;
- recovery time objective (RTO) and recovery point objective (RPO);
- security classification, threat model, and compliance obligations;
- data residency and retention;
- budget, unit economics, and cost ceiling;
- team skills, delivery deadline, and operational ownership.

## Answer depth rubric

### Level 1 — Product awareness

Names plausible components but does not connect them into an operable design.

### Level 2 — Solution design

Provides a coherent data flow, scaling model, and basic security controls.

### Level 3 — Senior architect

Explains failure modes, observability, recovery, cost, migration, alternatives,
and trade-offs.

### Level 4 — Principal architect or consultant

Connects architecture to business value, governance, organizational capability,
delivery risk, stakeholder decisions, and measurable outcomes.

## Common interview mistakes

- Selecting a cloud service before requirements are known
- Claiming “zero downtime” without defining failure boundaries
- Treating multi-region as a checkbox rather than a consistency and operations decision
- Ignoring deployment, rollback, observability, and ownership
- Using retries without timeouts, backoff, jitter, or an idempotency strategy
- Confusing backups with a tested disaster-recovery capability
- Giving only one option and hiding its disadvantages
- Optimizing hypothetical scale while ignoring current business constraints
