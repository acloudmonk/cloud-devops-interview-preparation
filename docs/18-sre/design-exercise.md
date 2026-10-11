# Enterprise SRE Design Exercise

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

This is a paper exercise. Reliability objectives, risk, ownership, response,
learning, and sustainable operations matter more than product names.

## Scenario

A financial-services company runs 180 services, primarily on AWS across EKS,
ECS, Lambda, RDS, DynamoDB, and SQS, with customer identity on Azure and analytics
on Google Cloud. Teams promise 99.99% availability without common SLI definitions.
Releases cause repeated incidents, pages average 45 per engineer per week, capacity
is reviewed only after saturation, postmortem actions remain open, and a recent
regional dependency failure required six hours to recover.

## Deliverables

1. **Discovery:** critical journeys, users, business impact, contracts, architecture,
   dependencies, incidents, SLOs, alerts, changes, capacity, teams, and constraints.
2. **Objective model:** valid/good events, measurement points, targets/windows,
   recovery needs, internal/external boundaries, and error-budget policy.
3. **Risk model:** failure modes, common-mode dependencies, quotas, capacity,
   change paths, data, detection, containment, recovery, owner, and validation.
4. **Incident system:** severity, declaration, roles/authority, channels, technical
   response, customer/executive communication, handover, vendor, and closure.
5. **Learning:** postmortem triggers/template/facilitation, corrective-action
   priority, risk acceptance, verification, theme analysis, and roadmap feedback.
6. **Toil/automation:** inventory, prioritization, elimination/self-service,
   automation safety, support ownership, skills, and outcome measurement.
7. **Capacity/performance:** demand model, peak/failure headroom, bottlenecks,
   quotas, tests, autoscaling, forecasts, and architectural thresholds.
8. **Change/resilience:** progressive delivery, data compatibility, rollback,
   readiness gates, recovery tests, game days, and fault experiments.
9. **Organization:** product/platform/SRE boundaries, engagement model, on-call
   staffing/training/health, service onboarding, and executive risk owners.
10. **Migration/measures:** first journey, waves, exceptions, investment, incident
    and SLO outcomes, page/toil reduction, capacity accuracy, and action completion.

## Decision worksheets

| Journey | SLI and target | Dominant risk | Budget action | Owner |
| --- | --- | --- | --- | --- |
| Example: card authorization | correct response within 800 ms for 99.95% over 28 days | dependency timeout/retry amplification | restrict high-risk change at fast burn | payments owner |

| Failure experiment | Steady state | Fault/scope | Abort | Evidence/owner |
| --- | --- | --- | --- | --- |
| Example: one-zone worker loss | queue age and completion SLO | terminate 25% in one AZ | error-budget burn threshold | platform plus payments |

## Review rubric

Score 0–4 for discovery, objectives/governance, architecture/risk, incident response,
learning, toil/automation, capacity/change/testing, organization/on-call,
cloud/migration depth, and executive communication. A strong answer negotiates
reliability and shows how controls are tested, not merely documented.

Return to the [module overview](index.md) when ready to continue.
