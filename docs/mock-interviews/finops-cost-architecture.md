# FinOps and Cost Architecture Mock Interview

[← Mock interview overview](index.md) ·
[Module 26 overview](../26-finops/index.md) ·
[Scenario answer framework](../interview-playbook/scenario-answer-framework.md)

Duration: **50 minutes**

Level: **Senior / Architect**

Primary context: **AWS-first digital business with Azure and Google Cloud services**

## Candidate brief

A digital-commerce company spends $3.2 million monthly: 75% AWS, 15% Azure, and
10% Google Cloud. Spend grew 55% while revenue grew 22%. Allocation is 61%,
forecasts miss by 18%, shared EKS platforms are disputed, central commitments do
not reflect engineering migrations, and teams receive late spreadsheets. The CFO
asks for a 25% reduction. Design the FinOps strategy and operating model.

## Interview structure

### 0–6 minutes — Discovery

Ask about business outcomes, products, revenue/margin, demand, architecture and
SLOs, billing contracts, cost basis, currencies, organization hierarchy, data
quality, unit metrics, commitments, shared platforms, authority, and constraints.

### 6–15 minutes — Data, allocation, and economics

Design provider ingestion and reconciliation, access, allocation hierarchy,
metadata governance, shared-cost rules, unallocated handling, showback/chargeback,
and product unit economics with quality guardrails.

### 15–25 minutes — Planning and optimization

Establish driver-based scenarios, forecast and budget cadences, variance and
anomaly response. Build a portfolio across idle/schedule/right-size, architecture,
network/data, Kubernetes, licensing, commitments, and sustainability. Separate
estimated from implemented and realized value.

### 25–35 minutes — Event branches

Choose two:

1. A network-topology release creates a sixfold data-transfer spike.
2. Rightsizing removes the headroom required for a zone failure.
3. Kubernetes allocation encourages teams to understate requests.
4. A commitment expires while a major migration remains uncertain.
5. A budget action stops a revenue-generating production service.

Contain safely, identify cost and customer impact, state authority, preserve
security/reliability, make a durable decision, and verify realized outcome.

### 35–42 minutes — Practice and governance

Define personas, RACI, daily/weekly/monthly/quarterly cadences, policy, platform
guardrails, education, disputes, exceptions, maturity, and automation boundaries.
Explain cross-cloud normalization and provider-specific detail.

### 42–47 minutes — Executive recommendation

Summarize business value, largest drivers, confidence, first actions, architecture
and commercial decisions, implementation capacity, quality guardrails, expected
range, residual risk, and approvals required.

### 47–50 minutes — Candidate questions

Ask about product strategy, risk appetite, margin, forecast/accounting needs,
contracts, migration plans, engineering capacity, incentives, or decision authority.

## Scoring rubric

| Dimension | Expected evidence |
| --- | --- |
| Discovery and value | products, demand, outcome, quality, constraints, personas |
| Cost data | scope, basis, latency, quality, security, reconciliation |
| Allocation and unit economics | ownership, shared rules, useful units, guardrails |
| Planning and anomalies | drivers, scenarios, variance, materiality, response |
| Workload optimization | architecture depth, total cost, safe change, realized value |
| Rate optimization | stable baseline, coverage/utilization, flexibility, expiry risk |
| Platforms and Kubernetes | requests/usage/idle, shared value, incentive awareness |
| Governance | RACI, cadence, policy, exceptions, enablement, automation safety |
| Cloud and communication | AWS depth, multi-cloud semantics, clear recommendation |

Score each 0–4. Maximum: **36**. Scores of 31–36 show strong architect signal;
24–30 are credible with gaps; 17–23 need deeper value and accountability reasoning;
below 17 should revisit the concepts and scenarios.

Return to the [module overview](../26-finops/index.md) after scoring.
