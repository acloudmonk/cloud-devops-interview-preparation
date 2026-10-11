# Allocation and Unit Economics

[← Module overview](index.md) · [FinOps decision model](concepts.md)

Allocation connects technology spend to accountable business constructs. Unit
economics divides an appropriate cost by a meaningful demand or value unit so
teams can distinguish efficient growth from growing inefficiency.

## Allocation hierarchy

Prefer durable structural signals first, then enrich them:

1. billing organization and payer or contract boundary;
2. account, subscription, project, folder, or management hierarchy;
3. product, service, environment, team, cost center, and owner metadata;
4. provider cost categories or allocation rules;
5. workload telemetry, platform metering, and business attribution;
6. documented rules for shared, support, tax, credit, and commitment costs.

Tags or labels are useful but incomplete. Some charges are untaggable, metadata
can change after usage, and shared services need consumption or policy-based
allocation. Define naming, allowed values, inheritance, validation, ownership,
and treatment of unallocated spend.

## Shared-cost methods

| Method | Appropriate when | Risk |
| --- | --- | --- |
| Equal split | Consumption is genuinely similar | Hides heavy users |
| Proportional to direct spend | Shared usage broadly follows workload scale | Reinforces inefficient spend |
| Measured consumption | Reliable usage driver exists | Metering effort and disputes |
| Business driver | Value unit explains consumption | Requires trusted product data |
| Central overhead | Allocation cost exceeds decision value | Weak local accountability |

Use showback before chargeback when data and trust are immature. Publish rules,
version changes, and reconciliation. Do not pretend an arbitrary allocation is
precise; label estimated and unallocated amounts.

## Unit-economics design

Examples include cost per order, successful payment, active customer, build,
environment-hour, model inference, gigabyte processed, or support case. A useful
unit is understood by product and engineering, correlates with demand, and can be
acted on without encouraging harmful behavior.

Define numerator, denominator, scope, time window, cost basis, adjustments,
quality guardrails, and owner. Pair unit cost with outcome measures such as
conversion, latency, reliability, carbon, or gross margin. Falling cost per
transaction is not success if failure or fraud rises.

## AWS-first implementation

Use AWS Organizations and accounts for strong boundaries; activate governed
cost-allocation tags; use Cost Categories for business groupings; use billing
data and workload metrics for shared-service allocation. Maintain an unallocated
cost KPI and a remediation path rather than silently spreading unknown spend.

Return to the [module overview](index.md) when ready to continue.
