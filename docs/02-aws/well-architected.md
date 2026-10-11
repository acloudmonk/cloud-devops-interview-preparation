# AWS Well-Architected Review

[← Cost and capacity](cost-capacity.md) · [Next: Design exercise →](design-exercise.md)

## Use the framework as a conversation

AWS Well-Architected organizes guidance into six pillars: operational excellence,
security, reliability, performance efficiency, cost optimization, and sustainability.
The review helps owners examine decisions and risk; it is not a certification, audit,
architecture score, or substitute for workload-specific requirements.

## Review all six pillars

| Pillar | Architecture questions |
| --- | --- |
| Operational excellence | Are ownership, observability, safe change, incident response, learning, and automation effective? |
| Security | Are identities, traceability, data, infrastructure, detection, and response protected through shared responsibility? |
| Reliability | Does the workload handle demand and failure, preserve data, and recover within proven objectives? |
| Performance efficiency | Do selected resource types, architectures, and evolution processes meet demand efficiently? |
| Cost optimization | Is spend visible, accountable, demand-aligned, and continuously optimized for value? |
| Sustainability | Is useful work delivered with efficient resources, data, software, and demand management? |

Do not optimize pillars independently. For example, removing redundancy may lower cost
but violate reliability, and retaining all telemetry forever may improve investigation
while harming cost, privacy, and sustainability. Record the business trade-off.

## Establish scope and evidence

Define the workload, owners, lifecycle stage, environments, critical journeys,
dependencies, objectives, regulations, and review date. Include product, application,
platform, operations, security, finance, and business voices. Use architecture diagrams,
configuration, metrics, SLOs, incidents, changes, cost data, tests, restore/failover
evidence, and interviews rather than accepting aspirational answers.

## Apply lenses selectively

Use relevant AWS lenses for technology or industry concerns only after the base
workload scope is clear. A serverless, SaaS, financial-services, or other lens adds
questions; it does not replace the six pillars or organizational control requirements.
Verify current lens availability and version in the Well-Architected Tool.

## Convert findings into decisions

Describe each risk with affected journey, evidence, likelihood, impact, existing
control, recommendation, alternatives, effort, dependency, and risk owner. Prioritize
high-risk and low-regret actions, identify accepted residual risk, and create measurable
completion criteria. Do not produce a long unowned checklist.

## Review continuously

Record milestones in the Well-Architected Tool or an equivalent governed system and
repeat after material architecture, demand, regulation, incident, migration, or
organizational change. Track action aging, risk reduction, recurring findings, and
evidence freshness. Independent facilitation can improve challenge, but workload
owners remain responsible for decisions and outcomes.
