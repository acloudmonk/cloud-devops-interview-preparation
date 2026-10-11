# FinOps and Cost Architecture

[← Curriculum overview](../curriculum/index.md) ·
[Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-11**
Level: **Senior / Architect**

FinOps is an operational framework and cultural practice for maximizing the
business value of technology. It connects engineering, finance, product,
procurement, and leadership through timely data, shared accountability, and
continuous decisions about value—not a one-time cost-cutting project.

!!! tip "Where to start"
    Start with **1. FinOps decision model** and follow the numbered path. AWS is
    the primary cloud context; Azure and Google Cloud are mapped where their
    commercial or technical controls differ. No executable lab or live billing
    account is required.

## Learning objectives

By the end of this module, you should be able to:

- establish FinOps scope, personas, outcomes, lifecycle, and maturity;
- build accurate cost allocation while treating tags as only one input;
- distinguish invoice, amortized, net, unblended, effective, and unit cost views;
- design AWS cost data, reporting, budget, forecast, and anomaly workflows;
- optimize architecture and usage without transferring risk to reliability or teams;
- select commitments using stable demand, coverage, utilization, and risk appetite;
- allocate shared platforms and Kubernetes costs with transparent assumptions;
- operate showback, chargeback, governance, and exception processes;
- translate FinOps capabilities across AWS, Azure, and Google Cloud.

## Recommended module path

### Phase 1 — Learn the FinOps operating system

| Step | Page | Outcome |
| ---: | --- | --- |
| 1 | [FinOps decision model](concepts.md) | Connect technology usage, business value, accountability, and iteration |
| 2 | [Allocation and unit economics](allocation-unit-economics.md) | Map spend to owners and meaningful business-value measures |
| 3 | [Cost data, visibility, and reporting](cost-data-reporting.md) | Build governed billing data and decision-oriented views |
| 4 | [Planning, budgeting, forecasting, and anomalies](planning-anomalies.md) | Set expectations and respond to material variance quickly |
| 5 | [Workload and architecture optimization](workload-optimization.md) | Remove waste and improve efficiency without unsafe trade-offs |
| 6 | [Rate optimization and commitments](rate-optimization.md) | Choose discounts and commercial constructs using risk-adjusted demand |
| 7 | [Kubernetes, platforms, and shared costs](platform-kubernetes-cost.md) | Make shared infrastructure costs understandable and actionable |
| 8 | [Governance and FinOps practice](governance-operating-model.md) | Define decision rights, cadences, policies, incentives, and maturity |
| 9 | [AWS-first multi-cloud and sustainability](cloud-mapping.md) | Translate FinOps capabilities and avoid false provider equivalence |

### Phase 2 — Apply the reasoning

| Step | Page | Outcome |
| ---: | --- | --- |
| 10 | [Enterprise FinOps design exercise](design-exercise.md) | Design a value and accountability model for an AWS-first enterprise |
| 11 | [Scenario questions and model answers](scenarios.md) | Practise 15 senior FinOps and cost-architecture scenarios |
| 12 | [Advanced cost incident drills](scenario-drills.md) | Work through 10 ambiguous financial and engineering events |
| 13 | [Ten-minute FinOps review](presentation-template.md) | Present value, drivers, decisions, risks, and evidence to executives |

### Phase 3 — Revise and assess

| Step | Page | Outcome |
| ---: | --- | --- |
| 14 | [Rapid-fire revision](rapid-fire.md) | Test 50 concise verbal explanations |
| 15 | [Active-recall flashcards](flashcards.md) | Revisit weak concepts with spaced repetition |
| 16 | [Timed FinOps mock interview](../mock-interviews/finops-cost-architecture.md) | Complete a scored 50-minute assessment |
| 17 | [References and videos](references.md) | Deepen weak areas with primary and authoritative sources |

## Relationship to adjacent modules

[Module 25](../25-ha-dr-bcp/index.md) explains the recovery capability whose
cost must be matched to business impact. [Module 18](../18-sre/index.md) provides
reliability objectives and operational risk; FinOps makes the value and economic
trade-offs visible. [Module 13](../13-terraform/index.md) provides IaC controls
that help enforce ownership and lifecycle policy. Future provider and
Well-Architected modules add service-specific and review depth.

## Completion checklist

- [ ] I can define a FinOps outcome without reducing it to “spend less.”
- [ ] I can choose a cost basis and explain how adjustments affect the answer.
- [ ] I can design allocation and unit economics that teams can act on.
- [ ] I can evaluate usage and rate optimization separately.
- [ ] I can explain commitment risk, shared costs, and Kubernetes attribution.
- [ ] I can propose governance that preserves engineering ownership and speed.
- [ ] I answered all 25 scenarios aloud and completed the scored mock interview.
