# Cross-Cloud Well-Architected Review Mock Interview

[← Mock interview overview](index.md) ·
[Module 27 overview](../27-well-architected/index.md) ·
[Scenario answer framework](../interview-playbook/scenario-answer-framework.md)

Duration: **50 minutes**

Level: **Senior / Architect**

Primary context: **AWS-first regulated payments workload with multi-cloud dependencies**

## Candidate brief

A payments workload runs on AWS across three Availability Zones, uses Azure for
workforce identity, and Google Cloud for analytics. A deployment caused a four-hour
outage, DR is untested, security exceptions expired, and cost grew faster than
transaction volume. The AWS Well-Architected Tool contains two-year-old answers.
Leadership wants an architecture “certification” before a product launch. Lead the
review and recommend an improvement operating model.

## Interview structure

### 0–6 minutes — Charter and discovery

Define workload and outcome, owners, lifecycle/launch trigger, critical journeys,
quality objectives, providers/dependencies, constraints, exclusions, frameworks/lenses,
participants, evidence, sensitive-data handling, and outputs.

### 6–17 minutes — Architecture and evidence

Walk request/data/deployment/operations paths across AWS’s six pillars. Apply Azure
and Google Cloud guidance to their dependencies. Distinguish current state, intent,
claim, observation, test, uncertainty, and stale evidence.

### 17–27 minutes — Findings and trade-offs

Develop three findings with condition, evidence, failure/threat scenario, consequence,
controls, confidence, severity, options, and cross-pillar effects. Decide what needs
containment, investigation, remediation, or authorized acceptance.

### 27–37 minutes — Review-room branches

Choose two:

1. The owner asserts all controls exist but cannot show evidence.
2. Cost optimization proposes removing untested DR capacity.
3. A serious credential exposure appears in an uploaded artifact.
4. AWS and Azure assessment scores contradict each other.
5. The launch date arrives before remediation can complete.

Protect people and sensitive data, handle uncertainty, preserve decision authority,
and define a safe next action and validation.

### 37–44 minutes — Improvement and governance

Sequence containment, quick improvements, foundations, strategic change, and risk
acceptance. Integrate actions into roadmaps; define evidence, milestones, change
triggers, portfolio themes, automation boundaries, and outcome metrics.

### 44–47 minutes — Executive recommendation

Summarize scope and confidence, top risks, three decisions, investment/dependencies,
launch trade-off, residual exposure, and next review milestone.

### 47–50 minutes — Candidate questions

Ask about risk authority, product/launch value, incident history, regulatory duties,
quality targets, evidence access, funding, platform roadmap, or provider incentives.

## Scoring rubric

| Dimension | Expected evidence |
| --- | --- |
| Scope and discovery | workload outcome, lifecycle, owners, dependencies, constraints, exclusions |
| Evidence discipline | source, date, scope, confidence, intent versus reality, sensitivity |
| Framework application | AWS depth, accurate Azure/Google mapping, relevant lens/perspective |
| Risk quality | condition, scenario, consequence, controls, uncertainty, calibrated priority |
| Trade-offs and decisions | cross-pillar options, authority, ADR, residual risk |
| Facilitation | safe challenge, conflict handling, escalation, clear communication |
| Remediation | sequencing, owners, dependencies, roadmap integration, validation |
| Continuous governance | milestones, triggers, automation boundary, portfolio learning |
| Executive signal | concise recommendation, investment, confidence, decisions needed |

Score each 0–4. Maximum: **36**. Scores of 31–36 show strong architect signal;
24–30 are credible with gaps; 17–23 need deeper evidence and risk reasoning;
below 17 should revisit the concepts and scenarios.

Return to the [module overview](../27-well-architected/index.md) after scoring.
