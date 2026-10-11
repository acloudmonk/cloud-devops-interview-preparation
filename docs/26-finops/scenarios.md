# Scenario Questions and Model Answers

[← Module overview](index.md) ·
[Scenario answer framework](../interview-playbook/scenario-answer-framework.md)

Answer each aloud before reading the model answer. State scope, cost basis, business
driver, accountable persona, decision, quality/risk guardrail, evidence, and trade-off.

## 1. The CFO mandates a 20% cloud-cost reduction

**Model answer:** Clarify financial timing, growth, product value, margin, accounting
basis, and risk appetite. Decompose price, quantity, mix, and one-time drivers.
Protect security and SLOs, prioritize reversible idle/schedule/right-size actions,
then architectural and commercial changes. Provide ranges, implementation cost,
owners, delivery dates, realized-savings validation, and explicit decisions where
the target requires product or risk trade-offs.

## 2. Forty percent of spend is unallocated

**Model answer:** Establish structural ownership through accounts/projects first,
govern metadata, create business mappings, and isolate genuinely shared/unknown
costs. Rank sources by materiality, assign remediation owners, and publish an
unallocated KPI. Allocate shared spend using measurable drivers or disclosed policy;
do not spread unknowns arbitrarily merely to claim 100% coverage.

## 3. A team disputes its chargeback invoice

**Model answer:** Freeze collection, not production. Reconcile invoice scope, cost
basis, time, credits, commitments, shared rules, resource ownership, and metadata
history. Correct errors transparently, version the rule, and provide an appeal path.
If trust is immature, return that element to showback until data and governance meet
an agreed threshold.

## 4. A production cost anomaly appears overnight

**Model answer:** Validate data freshness and materiality; identify service, account,
usage type, Region, resource, deployment, and owner. Compare traffic and planned
events, inspect security/abuse, pricing, loops, logging, and data transfer. Contain
safely using pre-authorized workload controls, communicate exposure, verify recovery,
and add preventive budgets, quotas, tests, or platform defaults.

## 5. A rightsizing recommendation removes HA headroom

**Model answer:** Reject utilization-only automation. Use workload demand, failure
capacity, scaling delay, quotas, maintenance, and SLO/error-budget evidence. Model
normal and failure modes, test under load and zone loss, then right-size the safe
baseline. Record resilience capacity separately so it is visible but not mislabeled waste.

## 6. Procurement wants maximum Savings Plan coverage

**Model answer:** Coverage alone is not the objective. Forecast the stable baseline
after migrations and optimizations, model utilization, discount, flexibility,
break-even, and downside scenarios, then purchase incrementally. Retain on-demand
flexibility and assign renewal/expiry ownership. Report realized effective savings
with both coverage and utilization.

## 7. Commitment utilization is high but savings are disappointing

**Model answer:** Check effective discount, on-demand comparator, benefit sharing,
term/payment, usage eligibility, overlapping discounts, fees, and whether the
commitment locked inefficient usage. High utilization means consumption, not good
economics. Compare realized savings with the counterfactual and upcoming architecture.

## 8. Kubernetes teams reduce requests to lower allocated cost

**Model answer:** The allocation rule has created an unsafe incentive. Show requests,
usage, limits, idle, and shared overhead separately; pair cost with SLOs, evictions,
throttling, and capacity risk. Use historical percentiles plus workload criticality,
and allocate platform headroom explicitly. Change the rule and stage rightsizing with rollback.

## 9. A shared observability platform cost doubles

**Model answer:** Decompose ingestion, cardinality, indexing, retention, queries,
replication, licenses, and egress by team or signal. Preserve security and SLO use
cases; apply sampling, filtering, tiered retention, metric governance, and owner
budgets. Allocate by measured drivers where useful and track cost per service or
signal alongside incident and detection outcomes.

## 10. Product usage and cloud spend both doubled

**Model answer:** Total spend alone cannot show efficiency. Calculate cost per valid
business unit with revenue, margin, quality, and mix. Separate fixed and variable
drivers and check whether unit cost improved. Efficient growth may be desirable;
focus optimization on declining unit economics or low-value features.

## 11. Finance and engineering dashboards disagree

**Model answer:** Compare billing scope, currency, time zone, data latency, taxes,
support, marketplace, credits, refunds, amortization, net/unblended basis, and
allocation version. Establish a reconciled source and semantic definitions while
retaining persona-specific views. Record expected differences rather than forcing
one dashboard to answer every question.

## 12. A multi-cloud migration promises lower compute prices

**Model answer:** Model total cost: egress and connectivity, duplicated platforms,
identity/security, support, skills, data movement, commitments, feature differences,
operational risk, and migration opportunity cost. Compare business value and exit
risk, not list prices. Pilot with measurable unit economics and quality guardrails.

## 13. Automated budget action stops a customer service

**Model answer:** Restore safely and treat the automation as a production incident.
Budgets should usually notify and escalate; any action must be workload-scoped,
pre-authorized, aware of criticality, tested, auditable, and reversible. Create
graduated controls for non-production, preserve service/SLO guardrails, and review
who approved the policy.

## 14. Leadership wants immediate chargeback

**Model answer:** Assess allocation coverage, reconciliation, shared-cost policy,
commitment/credit treatment, timeliness, owner mapping, and dispute readiness. Begin
with showback and decision cadences, measure behavior, then pilot chargeback with
stable products. Poor chargeback shifts disputes into accounting and encourages
local rather than enterprise optimization.

## 15. Carbon and cost recommendations conflict

**Model answer:** Quantify cost, emissions data quality, latency, resilience,
sovereignty, performance, and migration effort. Remove idle usage first where goals
align. For remaining choices, make business priorities and constraints explicit;
do not convert carbon to currency without an approved method or claim that cheaper
always means lower emissions.

Return to the [module overview](index.md) when ready to continue.
