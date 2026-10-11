# Enterprise SaaS Design Exercise

[← Delivery and operations](delivery-operations.md) · [Next: Scenario questions →](scenarios.md)

## Brief

A compliance-workflow vendor runs 180 customer-specific installations on virtual
machines. Releases take six weeks, identity settings differ, support cannot identify
the installed version, and gross margin falls as customers grow. The company wants a
single B2B SaaS product on AWS for 10,000 organizations across North America, Europe,
and India. Regulated enterprises demand federation, audit, residency, exports, and
optional dedicated data; small customers require low cost and instant trials.

## Constraints

- tenant sizes range from five users to 80,000 users with unpredictable batch work;
- core workflow availability target is 99.95%, with near-zero RPO for approved records;
- a tenant must never view another tenant's cases, audit data, or usage;
- enterprise plans support SAML/OIDC, delegated administration, and customer keys;
- usage combines active seats, workflow runs, and retained storage;
- regional data must include backups, telemetry, analytics, and support exports;
- Azure-based customers send identities; Google Cloud receives approved analytics;
- migration cannot stop current releases or force every customer to move at once.

## Candidate direction

Define immutable tenant identity and a global control plane for catalog, placement,
lifecycle, federation configuration, entitlements, and billing relationships. Keep
tenant-serving traffic in regional cells selected through the catalog. Use pooled
compute and partitioned data for smaller tiers, with dedicated databases or cells for
productized premium isolation. Preserve one artifact and operational plane.

Resolve tenant from a verified organization selection or tenant URL, validate the
token, and construct immutable context. Enforce policy at API and data boundaries,
use scoped workload roles, partition caches/objects/events, and continuously test
cross-tenant denial. Design just-in-time support access with audit.

Model onboarding, migration, plan change, suspension, export, and deletion as durable
idempotent workflows. Keep the data plane serving through bounded control-plane
unavailability. Introduce per-tenant/tier fairness, cell capacity limits, progressive
release rings, tenant-aware SLOs, and recovery exercises.

Build an immutable usage ledger with late-event and correction rules; separate it
from real-time quota and entitlements. Attribute shared cost using product usage and
report margin by tier. Migrate cohorts with anti-corruption adapters, reconciliation,
dual-run evidence, and retirement criteria.

## Scored deliverable (50 points)

| Area | Points | Strong evidence |
| --- | ---: | --- |
| Business model and discovery | 6 | tenant, plans, value, scale, commitments, constraints |
| Tenancy, placement, and isolation | 10 | component-level pool/silo choices and enforced trust path |
| Control plane and lifecycle | 7 | authoritative catalog and convergent automated workflows |
| Identity, data, and compliance | 8 | federation, policy, residency, keys, audit, deletion |
| Reliability and operations | 8 | cells, fairness, SLOs, recovery, tenant-aware evidence |
| Metering and economics | 6 | auditable usage, rating boundary, quota, allocation, margin |
| Delivery and migration | 5 | one product, rings, compatibility, cohorts, retirement |

Score 40+ only when tenant isolation and lifecycle correctness are demonstrable,
not assumed from cloud service selection.
