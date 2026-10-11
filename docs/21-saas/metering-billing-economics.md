# Metering, Billing, and Economics

[← Reliability, performance, and scale](reliability-performance.md) · [Next: Delivery, observability, and operations →](delivery-operations.md)

## Separate the flow

**Telemetry** explains system behavior. **Metering** creates auditable usage facts.
**Rating** applies price and plan rules. **Billing** produces financial obligations.
**Entitlement** grants product capability. These systems may share events but must
not be treated as one mutable counter.

## Usage ledger

A usage record should include stable tenant and account IDs, meter, quantity, unit,
event time, ingestion time, source, idempotency key, schema version, and correction
relationship. Preserve immutable facts, deduplicate deterministically, define late
arrival and time-zone rules, and reconcile source totals through invoice. Do not bill
directly from sampled observability metrics.

## Pricing and entitlement

Support subscription, per-seat, consumption, tiered, commitment, overage, and hybrid
models deliberately. Plan changes need effective time, proration, grace, and rollback
rules. Product access must not depend synchronously on a payment provider being
available; consume a locally available entitlement state within a declared staleness
window and reconcile commercial changes.

## Quotas and limits

Quotas protect safety and communicate product tiers. Define hard versus soft limits,
measurement window, burst allowance, warning, override, and reset behavior. A billing
meter is not automatically suitable for real-time enforcement because its consistency
and latency requirements differ.

## Tenant economics

Measure revenue, cloud and third-party consumption, support effort, and shared-cost
allocation by tenant, tier, feature, and cohort. Useful measures include cost to
serve, gross margin, contribution margin, utilization, acquisition, retention, and
feature value. Tags cannot allocate shared application work; application-level usage
and defensible allocation drivers are required.

## Disputes and corrections

Preserve lineage from invoice line to rated aggregate to raw usage. Corrections are
new adjusting records, not edits that erase history. Provide replay, backfill,
reconciliation, approval, and customer-visible explanation. Restrict billing access
and avoid placing sensitive workload data into usage records.

## Architecture outcome

Economics should influence placement and tier design without allowing sales to create
unbounded custom infrastructure. Premium isolation, regions, retention, or support
must have a productized delivery and cost model that maintains one operational plane.
