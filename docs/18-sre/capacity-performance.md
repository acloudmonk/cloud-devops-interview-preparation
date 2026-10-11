# Capacity and Performance Engineering

[← Module overview](index.md) · [Module 17: Observability](../17-observability/index.md)

Capacity engineering ensures critical flows have sufficient resources, quotas,
and dependency capability under normal, peak, failure, maintenance, and recovery
conditions. Autoscaling reacts within boundaries; it does not replace forecasting.

## Demand model

Forecast business drivers such as active users, transactions, objects, messages,
data size, tenant mix, feature adoption, seasonality, campaigns, retries, and
backfills. Translate them into arrival rate, concurrency, read/write mix, CPU,
memory, I/O, network, connections, partitions, and external-service demand.

Document baseline, peak shape/duration, growth bands, uncertainty, lead time,
failure scenario, and safety margin. Reconcile forecast with actuals and revise
model assumptions rather than treating a spreadsheet as truth.

## Performance relationships

- Utilization near saturation can cause nonlinear queueing and tail latency.
- Little's Law (`concurrency = throughput × time in system`) helps relate demand,
  latency, and in-flight work when assumptions approximately hold.
- Averages hide tail behavior and cohort imbalance; examine distributions.
- Horizontal scaling fails when state, locks, partitions, quotas, or dependencies
  remain bottlenecks.
- Failover capacity must account for remaining-zone/region capacity and recovery traffic.

## Testing strategy

Use load tests for expected demand, stress tests to find limits, spike tests for
sudden demand, soak tests for leaks/compaction/queues, and scalability tests across
resource levels. Test representative data volume, cache state, dependency behavior,
network conditions, and background work. Protect production with explicit scope,
abort conditions, isolation, and business approval.

## Autoscaling design

Choose a leading signal tied to demand or saturation, target, min/max, cooldown,
startup/readiness time, scale-in safety, and dependency limits. Queue depth alone
needs arrival/service rate and oldest-message age. CPU may be irrelevant for I/O-
bound work. Pre-scale when boot time exceeds acceptable demand response.

## Quotas and headroom

Inventory cloud-service quotas, IPs, load-balancer targets, database connections,
partitions, API limits, certificates, storage, and third-party contracts. Alert on
forecasted exhaustion with lead time. Reserve headroom for zone loss, deployments,
replay/backfill, incident debugging, and delayed scaling.

## Capacity decision

State the service objective, bottleneck, forecast range, test evidence, scaling
mechanism, headroom, cost, failure behavior, dependency constraint, and trigger for
architectural change. Overprovisioning may be appropriate when the cost of scarcity
dominates resource cost; justify it rather than calling all idle capacity waste.

Return to the [module overview](index.md) when ready to continue.
