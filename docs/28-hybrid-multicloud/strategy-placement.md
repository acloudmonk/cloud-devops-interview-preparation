# Strategy and Workload Placement

[← Module overview](index.md) · [Decision model](concepts.md)

Start from portfolio constraints and workload characteristics, then select a
pattern. Do not make every application cross-provider merely because the enterprise
has multiple providers.

## Placement criteria

Assess user/device latency, data residency and sovereignty, hardware proximity,
managed capability, existing estate, licensing, dependency gravity, reliability,
security, skills, delivery maturity, support, cost, egress, contract, and exit time.
Record who owns the decision and when it expires.

## Common patterns

| Pattern | Appropriate driver | Main caution |
| --- | --- | --- |
| Cloud-first portfolio | new workloads favor public cloud | legacy integration and governance |
| Tiered hybrid | front end and back end in different environments | latency and synchronous coupling |
| Environment hybrid | lifecycle stages in different locations | parity, test fidelity, data exposure |
| Partitioned multi-cloud | workloads/users assigned by capability or jurisdiction | fragmented operations and data |
| Analytics hybrid | operational data processed elsewhere | movement, privacy, freshness, egress |
| Edge hybrid | local latency/offline physical process | fleet lifecycle and disconnected security |
| Redundant multi-cloud | same outcome in multiple providers | state, feature parity, cost, correlated control |
| Cloud bursting | temporary capacity outside primary | data movement, licensing, readiness, economics |

Prefer portfolio-level multi-cloud—different workloads placed well—over splitting
one tightly coupled transaction path across clouds. Use asynchronous interfaces
and bounded failure where components must cross environments.

## Decision record

Document driver, pattern, duration (migration transition or steady state), workload
and data placement, rejected options, quality objectives, dependencies, commercial
assumptions, portability target, operational capability, risks, and exit trigger.

## Simplification test

Ask whether a single provider plus multiple Regions, a managed SaaS capability, or
a migration sequence meets the requirement with less risk. Multi-cloud is justified
only when its added outcome remains valuable after full lifecycle cost and failure
complexity are included.

Return to the [module overview](index.md) when ready to continue.
