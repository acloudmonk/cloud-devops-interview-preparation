# Site Reliability Engineering Mock Interview

[← Mock interview overview](index.md) ·
[Module 18 overview](../18-sre/index.md) ·
[Scenario answer framework](../interview-playbook/scenario-answer-framework.md)

Duration: **50 minutes**

Level: **Senior / Architect**

Primary context: **AWS-first financial-services platform with multi-cloud dependencies**

## Candidate brief

A financial-services company runs 180 services, mostly on AWS, with customer
identity on Azure and analytics on Google Cloud. Teams promise 99.99% availability
without common SLI definitions. Releases cause repeated incidents, on-call is
overloaded, capacity is reactive, postmortem actions age, and recovery from a
regional dependency failure took six hours. Design the SRE operating model.

## Interview structure

### 0–5 minutes — Discovery

Ask about critical journeys, users, business/contract/safety impact, architecture,
dependencies, incidents, SLOs, changes, capacity, on-call, ownership, and constraints.

### 5–15 minutes — Objectives and risk

Define one journey SLI/SLO, measurement and error-budget policy. Analyze failure
domains, serial/common-mode dependencies, capacity/quotas, containment, degradation,
recovery, AWS/multi-cloud assumptions, and risk ownership.

### 15–25 minutes — Operating system

Design incident declaration/roles/authority/communication/handover, postmortem and
verified corrective actions, toil prioritization and automation safety, capacity
forecasting, progressive change, readiness, and resilience tests.

### 25–35 minutes — Incident branches

Choose two:

1. Retry amplification turns an identity-provider brownout into global impact.
2. A database failover completes, but applications do not recover.
3. Autoscaling exhausts a cloud quota during a peak event.
4. Rollback fails because the previous release cannot read migrated data.
5. Automation removes healthy capacity across multiple regions.

Establish roles, stabilize users and data, manage uncertainty, verify recovery,
communicate, preserve evidence, and identify durable controls.

### 35–42 minutes — Organization and trade-offs

Discuss reliability versus cost/velocity, embedded versus enabling/platform SRE,
product responsibility, on-call sustainability, managed service assumptions,
multi-region complexity, and error-budget exceptions.

### 42–47 minutes — Executive recommendation

Summarize user promise, largest risk, first journey, target operating model,
investment, migration waves, residual risk, and measures in two minutes.

### 47–50 minutes — Candidate questions

Ask about business risk tolerance, incident history, authority, staffing, service
ownership, contracts, platform roadmap, or the first reliability outcome to improve.

## Scoring rubric

| Dimension | Expected evidence |
| --- | --- |
| Discovery and business alignment | journeys, impact, constraints, dependencies, owners |
| SLO and budget governance | valid SLI, target, measurement, policy, exception, decision |
| Architecture and risk | failure domains, correlation, capacity, containment, recovery |
| Incident response | roles, stabilization, communication, handover, verification |
| Learning and automation | systemic postmortem, actions, toil, safe engineering |
| Capacity and change | forecast, quotas, testing, progressive delivery, rollback |
| Resilience validation | readiness, recovery tests, game days, bounded experiments |
| Organization and on-call | responsibility, engagement, staffing, health, incentives |
| Cloud and communication | AWS depth, multi-cloud reality, structure, trade-offs |

Score each 0–4. Maximum: **36**. Scores of 31–36 show strong architect signal;
24–30 are credible with gaps; 17–23 need deeper reliability operating-model
reasoning; below 17 should revisit the concepts and scenarios.

Return to the [module overview](../18-sre/index.md) after scoring.
