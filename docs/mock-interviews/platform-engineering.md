# Platform Engineering Mock Interview

[← Mock interview overview](index.md) · [Module 19 overview](../19-platform-engineering/index.md)

Duration: **50 minutes**
Level: **Senior / Architect**
Primary context: **AWS-first enterprise with Azure and Google Cloud teams**

## Candidate brief

Two hundred developers across 35 teams operate 80 services using EKS, ECS, Lambda,
and managed data services. Environments take ten days, pipelines are copied, static
keys remain, change failure is 22%, ownership is incomplete, and audit evidence is
manual. Design a six-month platform engineering strategy and thin viable platform.

## Interview structure

### 0–7 minutes — Discovery and product decision

Clarify personas, journeys, baselines, business outcomes, workload archetypes,
responsibility, regulation, skills, existing tooling, constraints, and non-goals.

### 7–18 minutes — Product and architecture

Define the first golden path, product/team model, experience and API contracts,
catalog, workflow, control plane, state ownership, cloud foundations, and day-two
lifecycle. Explain portal versus platform and build/buy/compose choices.

### 18–28 minutes — Delivery, security, and operations

Cover workload identity, build isolation, artifact provenance/promotion, policy,
tenancy, secrets, evidence, platform SLOs, dependencies, support, upgrades,
incidents, backup, recovery, and degraded operation.

### 28–38 minutes — Failure branches

Choose three:

- client timeout leaves a partially provisioned environment;
- a GitOps controller deletes healthy workloads across accounts;
- a platform update breaks 30 services;
- a policy rollout blocks an emergency correction;
- the portal fails during a production incident;
- a build runner leaks another team's credential;
- cloud quota exhaustion creates a provisioning backlog;
- developers fork and bypass the golden path.

### 38–45 minutes — Adoption and economics

Describe pilot, migration, enablement, escape hatches, deprecation, feedback, flow,
quality, reliability, experience, adoption, platform capacity, and unit economics.
Translate the control model to Azure and Google Cloud.

### 45–50 minutes — Executive close

State the customer problem, first path, six-month sequence, funded team, expected
outcomes, largest residual risks, and evidence required for expansion.

## Scoring rubric

| Dimension | Points |
| --- | ---: |
| Discovery and product thinking | 7 |
| Architecture, interfaces, and lifecycle | 9 |
| Self-service, state, and control plane | 7 |
| Delivery, security, tenancy, and governance | 8 |
| Reliability, support, upgrades, and recovery | 7 |
| Adoption, organization, economics, and multi-cloud | 7 |
| Failure reasoning and communication | 5 |
| **Total** | **50** |

Interpretation: **43–50** architect-ready; **35–42** strong with targeted gaps;
**25–34** incomplete product or operational reasoning; **below 25** rebuild from
customer journeys and platform contracts. An answer that equates portal installation
with a complete platform cannot score above 34.

## Improvement loop

Record the three weakest decisions, revisit the matching module pages and primary
sources, redraw the lifecycle and responsibility boundaries, then repeat within
seven days using different failure branches.
