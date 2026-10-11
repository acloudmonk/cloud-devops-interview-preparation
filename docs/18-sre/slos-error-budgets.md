# SLIs, SLOs, and Error-Budget Governance

[← Module overview](index.md) · [Module 17: Observability](../17-observability/slos-alerting.md)

An SLI measures service behavior, an SLO sets an internal reliability objective,
and an error budget expresses tolerable unreliability. An SLA is a business/legal
commitment with defined scope and consequences; it is not automatically the right
engineering target.

## Build an SLO from a journey

1. Identify the user and critical action.
2. Define valid events and what counts as good.
3. Choose the measurement point closest to actual experience.
4. Select a rolling or calendar window and target from evidence and risk.
5. State exclusions narrowly; maintenance is still user impact unless the promise says otherwise.
6. Name service and business owners, dependencies, review cadence, and data quality.
7. Pair the objective with alerts and an error-budget policy.

Prefer ratio SLIs such as successful valid requests / valid requests. Define
correctness and latency where a technically successful but unusable response is
not good. Use separate objectives for materially different journeys instead of
averaging critical and low-value traffic.

## Error-budget interpretation

For a percentage target, allowed bad fraction is `1 - target`. A 99.9% request
success SLO allows 0.1% valid requests to be bad during the window. Translate the
budget into events or time only when the SLI semantics support that translation.
Budget is a risk signal, not spare outage time that must be consumed.

## Error-budget policy

Define actions before budget is exhausted: normal delivery while healthy; increased
review/testing at elevated burn; reliability work and restricted high-risk change
when threatened; executive/risk-owner decision for exceptions; and exit criteria
after recovery. Exemptions require scope, owner, reason, expiry, and compensating control.

The policy must consider incidents caused outside the service team, dependency
failures, planned changes, data-quality gaps, and low traffic. Do not punish teams
for honest reporting or encourage hiding failures to protect feature velocity.

## Cascading objectives

User-journey objectives should drive supporting service indicators. Internal SLOs
may be tighter than an external promise to leave budget for dependencies and
unknown failure. Avoid multiplying independent availability figures without
checking topology, correlation, retries, failover, and whether all components are
actually required for the user action.

## Governance and review

Review SLOs when user behavior, architecture, traffic, dependency, contract, or
cost changes—not simply each quarter. Track budget burn, decision outcomes,
measurement gaps, exclusions, exceptions, and whether alerts led to action.
Retire objectives that have no user, owner, decision, or trustworthy measurement.

Return to the [module overview](index.md) when ready to continue.
