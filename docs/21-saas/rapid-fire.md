# Rapid-Fire Revision

[← Ten-minute architecture review](presentation-template.md) · [Next: Active-recall flashcards →](flashcards.md)

Answer each aloud in one or two sentences, then add a trade-off or failure mode.

1. **What is SaaS?** A provider-operated product and business model delivered through a unified lifecycle.
2. **Is every SaaS product multitenant?** No; dedicated resources can still use a unified SaaS operating model.
3. **Is every multitenant system SaaS?** No; internal platforms can share resources without a SaaS business model.
4. **What is a tenant?** The customer or organizational boundary for identity, policy, data, service, and billing.
5. **What is pooling?** Multiple tenants share a resource while logical isolation protects their workloads.
6. **What is siloing?** A resource or stack is dedicated to one tenant.
7. **What is a bridge model?** Pool and silo choices are combined across components or tiers.
8. **What is a cell?** A bounded data-plane copy serving a subset of tenants.
9. **Why use cells?** To bound capacity and blast radius and support geographic placement.
10. **What does a tenant catalog hold?** Stable identity, placement, lifecycle, tier, policy, identity, and billing metadata.
11. **What is the control plane?** The authority for tenant lifecycle, placement, configuration, and fleet orchestration.
12. **What is the data plane?** The components that serve tenant business workloads and data.
13. **Why decouple the planes?** Existing tenant traffic should survive bounded control-plane unavailability.
14. **What is tenant isolation?** Explicit prevention of one tenant accessing another tenant's resources.
15. **Why is authentication insufficient?** A valid user can still request or query the wrong tenant's resource.
16. **What is trusted tenant context?** Server-constructed context derived from verified identity and routing evidence.
17. **Why avoid a tenant header as authority?** A caller can manipulate it and create confused-deputy access.
18. **What should an isolation test do?** Attempt horizontal access across tenant boundaries and expect denial.
19. **Can encryption replace isolation?** No; authorization and partitioning still control data access.
20. **Why can a user have several tenant roles?** Membership and authorization belong to the user-tenant relationship.
21. **What is federation?** Trusting an external identity provider through a protocol such as OIDC or SAML.
22. **What is delegated administration?** A tenant administrator manages bounded users and settings for that tenant.
23. **What is provider support access?** Time-bound, approved, tenant-scoped privileged access with audit.
24. **What is an entitlement?** A versioned decision about product capabilities a tenant may consume.
25. **How does entitlement differ from authorization?** Entitlement grants product capability; authorization grants an actor's action.
26. **How does quota differ from billing?** Quota controls consumption in time; billing determines financial charge.
27. **Why use a lifecycle state machine?** To make partial, asynchronous tenant operations explicit and repairable.
28. **Why must onboarding be idempotent?** Retries should converge without duplicate resources or accounts.
29. **What does offboarding include?** Export, revocation, retention, deletion, billing close, evidence, and tombstone.
30. **What is data residency?** A policy governing where applicable data and copies are stored or processed.
31. **Why is primary-database region insufficient?** Backups, logs, analytics, DR, exports, and vendors also carry data.
32. **What is a tenant partition key?** The stable key used to scope tenant-owned records and access paths.
33. **What is a noisy neighbor?** A tenant whose consumption degrades service for other tenants.
34. **How do you contain noisy neighbors?** Fair scheduling, quotas, concurrency, backpressure, isolation, and cells.
35. **Why is global availability misleading?** It can hide complete failure for a small tenant or cell.
36. **What is a tenant-aware SLO?** A reliability objective measured through tenant or tier experience.
37. **What is fair scheduling?** Allocating shared capacity so one workload cannot starve others.
38. **Why reserve cell headroom?** Placement, failover, and bursts require capacity before a hard limit.
39. **What is a deployment ring?** A controlled cohort receiving a change before broader rollout.
40. **Why track versions per tenant?** Support and rollout need software, schema, flag, and configuration evidence.
41. **What is tenant-aware observability?** Health and usage can be analyzed by tenant, tier, cell, and journey.
42. **What is the cardinality risk?** Unbounded tenant labels can overload or greatly increase metric cost.
43. **What is a usage ledger?** Immutable deduplicated records supporting rating, billing, and reconciliation.
44. **Why not bill from metrics?** Sampling, aggregation, mutation, and retention can destroy financial evidence.
45. **What is rating?** Applying price and plan rules to normalized usage.
46. **How are billing corrections represented?** As traceable adjusting records rather than erased history.
47. **What is cost to serve?** Direct and allocated provider cost attributable to a tenant, tier, or feature.
48. **Why can tags be insufficient?** Shared application resources require usage-based allocation beyond ownership tags.
49. **What is a feature flag?** A controlled exposure mechanism, not a permanent custom-product fork.
50. **Why is one artifact important?** It reduces version fragmentation while configuration controls supported variance.
51. **How should a tenant move cells?** Copy/stream, validate, fence, switch routing atomically, observe, then retire source.
52. **What makes dedicated hosting SaaS-like?** Unified onboarding, version, release, operations, and governance.
53. **What should survive a regional recovery?** Catalog, identity, placement, keys, data, queues, usage, and deletion evidence.
54. **What is the main SaaS economic test?** Growth should not require proportional operational effort or destroy margin.
55. **What is a strong SaaS architecture answer?** It links product promises to tenant isolation, lifecycle, operations, and economics.
