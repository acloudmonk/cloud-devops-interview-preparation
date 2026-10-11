# Case 2: Regulated Multi-Tenant SaaS

[← Global commerce surge](global-commerce.md) · [Next: Platform transformation →](platform-transformation.md)

## Brief

A B2B analytics company has 60 tenants and expects 500 within two years. Large
regulated customers require regional data residency, customer-managed keys,
federated identity, export and deletion, and evidence of isolation. The existing
shared database uses application-level tenant filters and manual onboarding.

## Discovery prompts

- What data and performance isolation do contract tiers require?
- Which control-plane metadata may be global and which data must remain regional?
- How are tenant identity, domains, roles, support access, and offboarding managed?
- What noisy-neighbor, recovery, encryption, audit, and customization obligations exist?
- What are onboarding time, per-tenant unit cost, and operational staffing targets?

## Candidate tasks

1. Compare pooled, siloed, and bridge tenancy models by risk and economics.
2. Separate global control plane from regional tenant data planes.
3. Design federation, authorization, tenant context, keys, audit, and support access.
4. Define provisioning, schema change, backup/restore, export, deletion, and migration.
5. Establish tenant SLOs, quotas, cost allocation, incident response, and roadmap.

## Failure injects

- A missing predicate exposes one tenant's record to another.
- A premium tenant saturates a shared analytics worker pool.
- A customer revokes its key during an active export.
- A regional database restore recovers some tenants to an inconsistent point.
- Sales promises tenant-specific code branches to close a strategic deal.

## Model direction

Make tenant identity a verified request invariant propagated through policy,
storage, events, caches, logs, and cost records. Defense in depth may combine
gateway validation, workload policy, database row-level controls or separate
resources, tenant-aware cache keys, and automated cross-tenant tests. Use pooled
resources for standard tenants, selective silos for justified regulatory or scale
needs, and a common provisioning contract to avoid two unrelated platforms.

Keep the control plane minimal and metadata-only where possible; deploy data planes
into approved regions. Automate tenant lifecycle, federation, key policy, quotas,
backup scope, restore verification, deletion evidence, and break-glass support.
Use cell-based partitioning to bound blast radius and enable migration. Meter cost
and SLOs by tenant/tier, and price dedicated isolation explicitly. Reject unmanaged
customer forks; meet variation through configuration and versioned extension points.

## Strong close

Recommend a default tenancy tier plus documented promotion triggers. Name how
isolation is continuously proven and how a tenant is moved, restored, exported,
and deleted without relying on a manual checklist.
