# Resilience and Continuity

[← Module overview](index.md) · [Operations and observability](operations-observability.md)

Provider diversity reduces only the failure modes that are truly independent.
Shared identity, DNS, code, CI/CD, third parties, carriers, data, and operations can
create larger correlated failures than a single-cloud design.

## Failure model

Test loss or degradation of a site, link, carrier, resolver, identity provider,
certificate/key service, cloud Region, provider control plane, shared SaaS, delivery
system, observability platform, and operations team. Include latency and partial
brownouts, not only clean outages.

## Continuity patterns

- isolate workloads by provider/region and fail business traffic between complete stacks;
- partition customers, geography, or capabilities so failure has bounded impact;
- use store-and-forward or local autonomous operation during disconnection;
- offer safe degraded functions rather than synchronous cross-cloud dependence;
- maintain independent backups, recovery access, artifacts, and minimum control planes.

Multi-cloud active-active is difficult when writes require global consistency. Define
single-writer, sharding, conflict resolution, fencing, RPO, reconciliation, and failback.
Do not route traffic before data and downstream capacity are safe.

## Exercises

Progress from tabletop to link failover, identity loss, DNS failure, data-lag, provider
loss, clean-room restore, and business continuity. Measure customer SLO, detection,
decision, RTO/RPO, manual work, cost, capacity, communication, and reconciliation.

## Exit versus DR

DR restores service after disruption; provider exit changes the strategic platform
over a longer horizon. Both need data and application movement, but exit also includes
contract, skills, feature replacement, delivery/operations, customer migration, and
verified deletion. Fund and test according to the real trigger and required time.

Return to the [module overview](index.md) when ready to continue.
