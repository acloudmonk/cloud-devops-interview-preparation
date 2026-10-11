# Case 6: Reliability and FinOps Turnaround

[← Cyber-recovery crisis](cyber-recovery.md) · [Next: AI operations copilot →](ai-operations-copilot.md)

## Brief

A cloud-native media platform grew cost 70% year over year while revenue grew 18%.
It also suffered six major incidents from saturation and risky changes. Finance
wants an immediate 30% cut; engineering proposes broad Savings Plans and smaller
clusters. Teams cannot allocate 35% of spend and have no user-journey SLOs.

## Discovery prompts

- Which customer journeys and revenue units drive demand and availability needs?
- What spend is unallocated, shared, idle, anomalous, or tied to reliability headroom?
- What are utilization distributions, seasonality, growth, and architectural constraints?
- Which incidents came from capacity, change, dependency, data, or observability failure?
- Who owns unit cost and reliability decisions, and what commitments already exist?

## Candidate tasks

1. Define service-level SLIs/SLOs, error budgets, and unit-economic measures.
2. Repair allocation using account/project, tag/label, workload, and shared-cost rules.
3. Separate waste, rate, architecture, demand, and reliability-headroom decisions.
4. Prioritize changes by verified savings, reliability risk, effort, and reversibility.
5. Create forecasting, anomaly, commitment, and governance feedback loops.

## Failure injects

- A right-sizing change causes throttling during a live event.
- A one-year commitment is proposed from only four weeks of stable usage.
- Kubernetes allocation penalizes a team for platform-system overhead.
- A cache optimization cuts compute but doubles data-transfer cost.
- Teams game the SLO by excluding a failing customer path from the indicator.

## Model direction

Reject an indiscriminate percentage cut. First establish trustworthy allocation and
customer-centric reliability measures. Attribute direct costs, allocate shared cost
with transparent drivers, label unknown spend, and track cost per active subscriber,
stream hour, or successful transaction. Correlate cost changes with latency, errors,
saturation, and business outcomes.

Remove clearly idle resources and anomalies first; tune workload requests, storage,
data transfer, retention, and scaling with measured demand. Preserve explicit
reliability headroom. Purchase commitments only after usage is optimized, forecast,
owned, and covered by risk-adjusted break-even analysis. Use SLO/error-budget
governance so risky optimization receives progressive rollout and rollback. Create
a recurring engineering-finance review that tracks realized—not estimated—savings
and prevents cost shifting across services.

## Strong close

Recommend a 90-day sequence with safe quick wins, measurement repairs, architectural
experiments, and commitment gates. Explain which 30% target is feasible, by when,
and what reliability or growth trade-off leadership would need to accept.
