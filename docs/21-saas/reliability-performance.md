# Reliability, Performance, and Scale

[← Data, residency, and compliance](data-residency-compliance.md) · [Next: Metering, billing, and economics →](metering-billing-economics.md)

## Reliability has multiple lenses

Measure global availability, tenant availability, tier commitments, cell health, and
critical journeys. A global average can hide one tenant being completely unavailable.
Define SLOs for sign-in, core transactions, asynchronous completion, provisioning,
exports, and billing correctness. Use error budgets to govern product changes.

## Noisy-neighbor controls

Apply tenant- and tier-aware quotas, request limits, concurrency bounds, queue
fairness, database resource controls, cache limits, payload limits, and load shedding.
Protect provider control traffic and critical workflows from bulk exports or reports.
Rate limits without fair scheduling can still let a large tenant monopolize workers.

## Capacity and placement

Model tenant count and size distribution, not only average requests per second.
Track heavy hitters, burst, storage, background work, connection count, and growth.
Place tenants by headroom, data locality, compliance, affinity, and risk. Use cells
when bounded blast radius and predictable scale justify the fleet complexity.

## Failure containment

Use timeouts, idempotency, retry budgets, circuit breakers, bulkheads, backpressure,
and degraded modes. Decide whether a dependency failure affects one tenant, cell,
tier, region, or the entire product. Avoid a synchronous control-plane dependency on
every data-plane request. Test corrupted tenant configuration and entitlement-cache
failure, not only infrastructure loss.

## Recovery

Define RTO and RPO by workflow and tier. Backups are useful only after restore and
tenant-isolation validation. Shared databases make single-tenant recovery difficult;
design point-in-time extraction, replay, or corrective transactions in advance.
Regional recovery must restore tenant placement, identity configuration, keys,
queues, catalog, and billing continuity—not just compute.

## Performance and fairness evidence

Observe latency and errors by tenant, tier, cell, operation, and dependency while
controlling metric cardinality. Maintain per-tenant drill-down through logs or traces
with access controls. Load tests need mixed tenant sizes, bursts, long jobs, retries,
and failure recovery. A system that reaches peak throughput by starving small tenants
has failed the SaaS requirement.
