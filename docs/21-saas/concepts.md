# SaaS Decision Model

[← Module overview](index.md) · [Next: Tenancy, isolation, and placement →](tenancy-isolation.md)

## SaaS, multitenancy, and hosting

SaaS means the provider operates a continuously evolving product through a unified
experience. Multitenancy means at least some resources serve multiple tenants. A
SaaS product may use dedicated infrastructure while retaining common onboarding,
release, operations, and product governance. Conversely, a shared internal platform
can be multitenant without being a commercial SaaS product.

Managed hosting becomes SaaS only when bespoke installs stop behaving as separate
products. One-off versions, manual tenant changes, and customer-specific runbooks
destroy economies of scale even if the provider hosts every instance.

## Start with the business contract

Before selecting cloud services, discover:

- who a tenant is and whether organizations contain subtenants or workspaces;
- pricing units, plans, entitlements, trials, and service commitments;
- expected tenant count, size distribution, growth, churn, and geographic markets;
- identity federation, delegated administration, audit, export, and support needs;
- isolation, residency, encryption, retention, and regulatory obligations;
- availability, latency, recovery, maintenance, and version expectations;
- provider objectives for gross margin, release frequency, and support effort.

The architecture should make the commercial promise enforceable and measurable.

## Core planes

The **control plane** owns tenant catalog, provisioning, placement, identity
configuration, entitlements, billing relationships, lifecycle state, and fleet
orchestration. The **data plane** serves tenant workloads and business data. The
**analytics plane** can derive product, operational, and economic insight while
preserving privacy and access boundaries.

A control-plane outage should not automatically stop already provisioned tenant
traffic. Cache or replicate bounded configuration, define fail-closed versus
fail-open behavior per decision, and reconcile when control returns. Privileged
control-plane actions require stronger assurance than ordinary product traffic.

## SaaS principles

1. Carry verified tenant context through every request, job, event, record, and log.
2. Enforce isolation independently of ordinary authentication.
3. Automate lifecycle operations and make workflows idempotent and observable.
4. Keep one product and avoid tenant-specific code forks.
5. Treat tiers as policy and entitlement, not scattered conditionals.
6. Measure health, usage, cost, and value by tenant and tier.
7. Limit blast radius through cells or stamps as scale and risk justify.
8. Design deletion, export, recovery, and suspension before production.

## Architecture decision record

For every major component, record tenant sharing boundary, isolation enforcement,
placement key, scaling unit, quota, encryption boundary, failure domain, deployment
unit, telemetry dimension, cost attribution, migration mechanism, and exit path.
Different components can use different models; consistency of reasoning matters more
than a single tenancy slogan.
