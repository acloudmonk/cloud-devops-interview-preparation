# Enterprise FinOps Design Exercise

[← Module overview](index.md) · [Multi-cloud and sustainability](cloud-mapping.md)

## Brief

A digital-commerce company spends $3.2 million per month: 75% AWS, 15% Azure,
and 10% Google Cloud. AWS hosts customer products and EKS platforms, Azure hosts
workforce and data services, and Google Cloud hosts analytics and machine learning.
Spend grew 55% while revenue grew 22%. Only 61% is allocated, forecasts miss by
18%, commitments are purchased centrally without engineering plans, and teams
receive monthly spreadsheets too late to act. The CFO requests a 25% cut.

Design a FinOps operating model that improves business value and predictability
without arbitrary reliability, security, or product damage.

## Required discovery

Clarify products, margins, growth and demand drivers; billing contracts and
currencies; organization hierarchies; architecture and SLOs; unit metrics; shared
platforms; existing commitments and expiries; invoice/accounting requirements;
data quality; decision authority; engineering capacity; and material risks.

## Produce these artifacts

1. **Scope and outcomes** — business goals, spend boundary, personas, and success measures.
2. **Data architecture** — provider exports, FOCUS/provider fields, quality, access, and reconciliation.
3. **Allocation model** — structural ownership, metadata, shared-cost rules, and unallocated process.
4. **Unit economics** — product-specific numerators, denominators, quality guardrails, and owners.
5. **Planning system** — driver-based forecast, budgets, scenarios, anomalies, and variance workflow.
6. **Optimization portfolio** — usage, architecture, rate, Kubernetes, licensing, and sustainability actions.
7. **Operating model** — cadences, RACI, policy, showback/chargeback, exceptions, and enablement.
8. **Roadmap** — 30/60/90-day foundation, later maturity, dependencies, and residual risk.

## Constraints to address

- Revenue growth explains some spend growth; do not treat all increase as waste.
- Reliability and DR capacity has business-approved value but should be tiered.
- Shared EKS clusters need allocation without rewarding unsafe resource settings.
- Provider credits and commitments make invoice and workload cost views differ.
- Teams plan migrations that may invalidate new long-term commitments.
- Cost data contains sensitive commercial rates and customer allocation inputs.
- Finance needs accrual and invoice reconciliation; engineering needs timely drivers.

## Strong answer outline

Reframe the 25% request into value, efficiency, and risk outcomes. Establish a
governed cost data product with explicit bases and quality; raise allocation through
hierarchy, metadata, cost categories, and measured shared drivers; introduce product
unit economics; and build driver-based rolling forecasts with material anomaly response.

Prioritize reversible usage changes and architecture improvements, then commit only
a conservative stable baseline. Combine engineering, product, finance, procurement,
and platform ownership. Start with showback, publish assumptions, measure realized
outcomes, and use time-bound exceptions. Present savings ranges, implementation cost,
SLO/security guardrails, and decisions the CFO must approve.

## Self-scoring rubric

| Dimension | 0 | 2 | 4 |
| --- | --- | --- | --- |
| Business value | percentage cut only | goals acknowledged | value, growth, quality, and risk integrated |
| Data and allocation | dashboards | partial rules | reconciled data, bases, quality, owners, shared-cost model |
| Unit economics | total spend | generic unit | actionable product units with guardrails |
| Optimization | tool list | plausible actions | usage/rate separation, total cost, validation, prevention |
| Operating model | central team owns all | RACI exists | collaborative cadences, decision rights, policy, enablement |
| Evidence | estimated savings | tracked actions | realized value, forecast/anomaly metrics, and residual risk |

Maximum: **24**. Aim for at least **19** before moving to the mock interview.

Return to the [module overview](index.md) when ready to continue.
