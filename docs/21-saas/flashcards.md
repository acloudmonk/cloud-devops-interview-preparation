# Active-Recall Flashcards

[← Rapid-fire revision](rapid-fire.md) · [Next: References and videos →](references.md)

Cover the answer column and recall the decision, not only the definition.

| # | Prompt | Recall answer |
| ---: | --- | --- |
| 1 | SaaS versus multitenancy | SaaS is a provider product/operating model; multitenancy is resource sharing. |
| 2 | SaaS versus managed hosting | SaaS keeps a unified lifecycle; managed hosting often accumulates bespoke instances. |
| 3 | Pool model | Shared resource with explicit logical isolation and fairness controls. |
| 4 | Silo model | Tenant-dedicated resource; stronger boundary but higher fleet and capacity cost. |
| 5 | Bridge model | Different tenancy boundaries by component, obligation, or product tier. |
| 6 | Cell | Bounded data plane for a subset of tenants, limiting scale and blast radius. |
| 7 | Placement authority | Catalog mapping tenant to region, cell, partition, tier, and policy. |
| 8 | Tenant isolation | Explicitly blocks cross-tenant resource access beyond ordinary authentication. |
| 9 | Trusted tenant context | Immutable service context derived from validated identity and routing. |
| 10 | Control plane | Tenant catalog, lifecycle, placement, configuration, entitlement, and fleet authority. |
| 11 | Data plane | Serves tenant business requests, jobs, and data. |
| 12 | Lifecycle workflow | Durable idempotent state machine with compensation and reconciliation. |
| 13 | Entitlement | Versioned product capability granted to a tenant. |
| 14 | Authorization | Decision that a principal may perform an action on a resource in tenant context. |
| 15 | Federation | Per-tenant trust with an external identity provider using OIDC or SAML. |
| 16 | Support access | Just-in-time, purpose-bound, tenant-scoped privileged access with evidence. |
| 17 | Residency scope | Primary data, replicas, backups, telemetry, analytics, exports, DR, and vendors. |
| 18 | Deletion manifest | Evidence and progress for deleting every applicable copy and derived representation. |
| 19 | Noisy-neighbor control | Fair scheduling, quota, concurrency, backpressure, isolation, and load shedding. |
| 20 | Tenant-aware SLO | Reliability measured by tenant/tier journey, not only a global average. |
| 21 | Deployment ring | Ordered cohort used to limit change exposure and collect evidence. |
| 22 | Usage ledger | Immutable, deduplicated, versioned usage facts with lineage. |
| 23 | Rating | Application of price and plan rules to usage. |
| 24 | Billing correction | New adjustment linked to original records, preserving history. |
| 25 | Quota versus meter | Quota enforces safe consumption; meter records auditable billable use. |
| 26 | Cost to serve | Direct and defensibly allocated provider cost by tenant/tier/feature. |
| 27 | Feature flag debt | Long-lived flags create hidden versions and must have owner and expiry. |
| 28 | Tenant move | Copy/stream, validate, fence, atomic route switch, observe, retire. |
| 29 | Control-plane outage behavior | Continue safe data-plane service from bounded snapshots; pause unsafe mutations. |
| 30 | SaaS scale test | Tenant growth should not require proportional manual operations. |
