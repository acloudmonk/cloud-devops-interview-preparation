# AWS Well-Architected Pillars and Lenses

[← Module overview](index.md) · [Scope and evidence](scope-evidence.md)

The AWS Well-Architected Framework organizes review questions across six pillars.
Use them to understand design and operational choices in context, not to prescribe
AWS services before requirements are known.

## Six-pillar review map

| Pillar | Review focus | Representative evidence |
| --- | --- | --- |
| Operational Excellence | organization, preparation, operation, learning | ownership, runbooks, delivery metrics, incidents, improvement loop |
| Security | identity, detection, protection, data, incident response | trust model, policies, logs, threat model, tests, response evidence |
| Reliability | foundations, architecture, change, failure management | quotas, SLOs, dependencies, capacity, recovery tests, failure evidence |
| Performance Efficiency | selection, scaling, monitoring, evolution | workload profiles, load tests, latency, utilization, technology decisions |
| Cost Optimization | financial management, awareness, efficiency, demand | allocation, unit cost, forecasts, usage/rate actions, realized value |
| Sustainability | demand alignment and resource efficiency | utilization, architecture choices, data lifecycle, measurement assumptions |

AWS pillars are not independent workstreams. For example, moving to an active-active
regional design changes reliability, cost, operations, security, performance, and
sustainability. Record the combined decision and residual risks.

## AWS Well-Architected Tool

The AWS Well-Architected Tool can record workloads, apply the core framework and
relevant lenses, capture answers and improvement items, and track milestones.
Define access carefully because review records can contain sensitive architecture
and risk information. Exported scores and reports do not replace supporting evidence.

## Lenses

Use an official or custom lens when technology, industry, or organization-specific
risks require additional questions. Select lenses before review and avoid stacking
irrelevant lenses that create fatigue. A lens supplements rather than cancels the
core framework, legal obligations, or specialist assessments.

## Review method

1. Establish workload context and business priorities.
2. Walk critical journeys and dependencies across pillars.
3. Use framework questions to expose decisions, evidence, and uncertainty.
4. Record applicable answers and improvement items without forcing false certainty.
5. Agree risk ownership and a small prioritized improvement plan.
6. Create a milestone after material change and validate remediation outcomes.

## Common misuse

- treating “not applicable” as a way to hide an unresolved decision;
- equating a managed service with a fully implemented control;
- selecting best-practice answers based on design intent rather than production evidence;
- reporting only high-risk issue counts without business context;
- repeating the questionnaire without closing or reassessing findings;
- allowing the reviewer to own workload risk or remediation.

Return to the [module overview](index.md) when ready to continue.
