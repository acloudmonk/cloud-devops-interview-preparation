# Rate Optimization and Commitments

[← Module overview](index.md) · [Workload optimization](workload-optimization.md)

Rate optimization reduces the price paid for eligible usage through commitments,
reservations, negotiated agreements, licenses, credits, or market pricing. It does
not remove inefficient usage; buying a discount for waste can lock waste in.

## Decision model

1. Normalize demand after planned architecture and usage changes.
2. Identify the stable baseline by family, Region, operating system, term, and scope.
3. Model coverage, utilization, discount, break-even, expiry, and downside scenarios.
4. Preserve flexibility for migrations, growth uncertainty, acquisitions, and product exit.
5. Assign purchase authority, benefit-allocation rules, monitoring, and renewal dates.
6. Buy in increments, observe, and rebalance instead of committing the optimistic forecast.

## AWS constructs

- Savings Plans discount eligible compute usage in exchange for a spend commitment;
  Compute and EC2 Instance Savings Plans trade flexibility and discount differently.
- Reserved Instances or reserved capacity remain service-specific; payment options,
  scope, size flexibility, exchange, and capacity behavior vary.
- Spot Instances provide interruptible capacity and require fault-tolerant workloads.
- Enterprise agreements, private pricing, credits, and marketplace commitments add
  commercial constraints that must be reflected in effective cost and forecasts.

Always verify current eligibility and terms. A reservation discount and a capacity
reservation solve different problems unless a specific construct explicitly combines them.

## Metrics

- **Coverage**: eligible usage receiving commitment benefit.
- **Utilization**: purchased commitment actually consumed.
- **Effective savings rate**: realized savings divided by comparable on-demand cost.
- **Break-even**: usage or time needed for the commitment to outperform alternatives.
- **Commitment risk**: exposure to demand, architecture, price, term, currency, or contract change.

High utilization can coexist with low coverage; high coverage can coexist with poor
utilization. Report both with realized savings and expiry risk.

## Benefit allocation

Decide whether commitment benefits follow the purchasing account, consuming team,
or central portfolio. Publish how unused commitment and negotiated credits are
allocated. Poor rules can reward overconsumption or make team actions invisible.

## Interview trade-off

Separate workload optimization from rate optimization. First reduce and shape
demand; then cover a conservative stable baseline. State the flexibility purchased,
residual on-demand usage, ownership, and downside if demand changes.

Return to the [module overview](index.md) when ready to continue.
