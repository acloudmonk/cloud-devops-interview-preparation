# Azure Well-Architected Review

[← Cost and capacity](cost-capacity.md) · [Next: Design exercise →](design-exercise.md)

## Apply the framework at workload scope

Azure Well-Architected evaluates a workload across five pillars: reliability, security,
cost optimization, operational excellence, and performance efficiency. Cloud Adoption
Framework and Azure Landing Zones address broader adoption and platform governance.
Use both at their intended scope; a compliant landing zone does not prove workload quality.

## Review all five pillars

| Pillar | Architecture questions |
| --- | --- |
| Reliability | Does the workload tolerate failure, preserve data, and recover within proven objectives? |
| Security | Are identities, data, applications, infrastructure, detection, and response protected appropriately? |
| Cost Optimization | Is cost modeled, visible, accountable, demand-aligned, and continuously optimized for value? |
| Operational Excellence | Are ownership, observability, safe change, incident response, automation, and learning effective? |
| Performance Efficiency | Do architecture, SKUs, scale, data paths, and evolution meet demand efficiently? |

Balance pillars from business requirements. More redundancy may improve reliability but
increase cost and operational complexity; aggressive caching may improve performance
while creating consistency, privacy, and invalidation risks. Record accepted trade-offs.

## Establish scope and evidence

Define workload, owners, lifecycle, environments, journeys, dependencies, objectives,
regulations, and review date. Include application, data, platform, security, operations,
finance, and business roles. Examine diagrams, configuration, Policy/RBAC, metrics,
SLOs, incidents, changes, cost data, tests, and restore/failover evidence rather than
accepting aspirational questionnaire answers.

## Use assessments and workload guidance

Microsoft’s Well-Architected assessment and Azure Advisor can provide recommendations,
but validate relevance, freshness, and business context. Use workload guides for
technology-specific depth after the base scope is clear. Recommendations do not own
risk, understand every dependency, or authorize production change.

## Convert findings into improvement

For each risk capture affected journey, evidence, likelihood, impact, current control,
recommendation, alternatives, effort, dependency, risk owner, and completion measure.
Prioritize material risks and low-regret actions; explicitly accept residual risk at the
right authority. Repeat after significant architecture, demand, incident, regulation,
migration, or platform change and track evidence freshness and action aging.
