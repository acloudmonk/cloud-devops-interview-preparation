# Kubernetes, Platforms, and Shared Costs

[← Module overview](index.md) · [Rate optimization](rate-optimization.md)

Shared platforms create leverage but weaken the direct relationship between a
cloud invoice and the product that consumed capacity. FinOps for platforms needs
provider billing, cluster telemetry, scheduling context, and transparent policy.

## Kubernetes cost layers

1. Cloud infrastructure: nodes, disks, load balancers, NAT, egress, registries, and support.
2. Cluster control and platform services: ingress, observability, policy, security, service mesh, and operators.
3. Namespace/workload consumption: CPU, memory, accelerators, storage, and network.
4. Idle and stranded capacity: requested but unused resources and unscheduled headroom.
5. Business attribution: product, team, environment, tenant, customer, or transaction.

Requests influence scheduling and capacity more directly than instantaneous usage;
limits affect risk and contention. Show both requested, used, and allocated capacity.
Do not reward teams for removing safe limits or punish required failover headroom.

## Allocation choices

- attribute dedicated resources directly;
- allocate shared cluster cost by requests, usage, or a blended rule;
- expose idle cost separately before assigning it;
- assign common platform cost as product overhead, consumption-based charge, or central investment;
- disclose assumptions for Spot, commitments, credits, shared storage, and network.

## Optimization controls

Right-size requests from representative history and peak behavior; use autoscaling
at workload, node, and provisioning layers; improve bin packing; isolate special
hardware; schedule ephemeral environments; control log and metric cardinality;
review cross-zone and egress paths; and use interruptible capacity only for tolerant
workloads. Validate disruption budgets, startup time, quotas, and availability.

## Platform product economics

Measure cost alongside adoption, developer lead time, reliability, security control
coverage, support demand, and duplicated capability removed. A platform that raises
shared spend may still improve enterprise unit economics by reducing team toil and
time to market. Show marginal and fully loaded cost rather than claiming one is truth.

## SaaS and multi-tenancy

Map shared cost to tenant and feature using stable identifiers and sampled or direct
metering. Protect customer privacy, avoid extreme telemetry cardinality, and reconcile
usage meters with billing. Pair cost per tenant with revenue, tier, service level,
support, and gross margin; never optimize a high-value customer from cost alone.

Return to the [module overview](index.md) when ready to continue.
