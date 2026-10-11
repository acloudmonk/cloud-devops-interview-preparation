# Governance and the FinOps Practice

[← Module overview](index.md) · [Platform and Kubernetes cost](platform-kubernetes-cost.md)

FinOps governance defines decision rights, guardrails, evidence, and accountability
without turning every engineering action into central approval. The practice should
make good economic decisions easier at the speed teams work.

## Responsibility model

- Leadership sets business outcomes, risk appetite, and escalation authority.
- Product owns value, demand assumptions, service levels, and prioritization.
- Engineering owns architecture, usage, technical remediation, and quality impact.
- Finance owns planning, accounting alignment, accrual, and financial controls.
- Procurement manages commercial terms, renewals, negotiation, and supplier risk.
- FinOps practitioners enable data, standards, analysis, facilitation, and maturity.
- Platform teams embed defaults, allocation, telemetry, and self-service guardrails.

## Operating cadences

- Daily or event-driven anomaly triage for material unexpected changes.
- Weekly workload review for actionable drivers and completed optimizations.
- Monthly product/finance forecast, variance, unit economics, and commitment review.
- Quarterly architecture, portfolio, contract, maturity, and policy review.
- Annual strategy and planning aligned with product and technology roadmaps.

Cadence should reflect materiality and data latency; avoid meetings without a
decision, action, owner, due date, and outcome measure.

## Policy examples

Require ownership metadata, approved Regions/services, budget recipients, lifecycle
and retention standards, non-production schedules, commitment authority, marketplace
approval, architecture review thresholds, and exception expiry. Enforce hard controls
only where risk demands them; use visibility and nudges for context-dependent decisions.

## Showback and chargeback

Showback gives teams visibility without transferring ledger cost. Chargeback assigns
financial responsibility and changes incentives. Introduce chargeback only after
allocation, adjustments, disputes, shared costs, and accountability are trusted.
Provide a dispute path and prevent local optimization that harms enterprise value.

## Maturity and measurement

Assess each capability independently using an incremental crawl/walk/run mindset.
Useful measures include allocation coverage, forecast accuracy, anomaly response,
recommendation cycle time, realized savings, commitment utilization/coverage, unit
economics, policy exceptions, and stakeholder adoption. Avoid a maturity score that
rewards more process rather than better decisions.

## Automation principles

Automate data quality, enrichment, alerts, safe schedules, and approved remediation.
For destructive or customer-impacting action, require scoped authorization, dry run,
change controls, rollback, audit, and SLO guardrails. Cost automation is production
automation and deserves the same engineering discipline.

Return to the [module overview](index.md) when ready to continue.
