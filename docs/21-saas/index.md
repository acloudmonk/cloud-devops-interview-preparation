# SaaS Architecture

[← Curriculum overview](../curriculum/index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-11**
Level: **Senior / Architect**

Software as a service is a business and operating model, not merely a shared
database or subscription screen. Strong SaaS architecture connects tenant context,
isolation, lifecycle automation, reliability, security, cost, and product tiers so
growth does not create proportional operational effort.

!!! tip "Where to start"
    Start with **1. SaaS decision model** and follow the numbered path. AWS is the
    architecture anchor, with Azure and Google Cloud translations. This module is
    theoretical and scenario-driven; no deployment lab is required.

## Learning objectives

- distinguish SaaS, multitenancy, managed hosting, and customer-operated software;
- select pool, silo, bridge, cell, and deployment-stamp models by explicit trade-off;
- propagate trustworthy tenant context and enforce isolation at every resource layer;
- separate a global control plane from tenant-serving data planes;
- automate onboarding, configuration, entitlements, suspension, export, and deletion;
- federate enterprise identity and implement tenant-aware authorization safely;
- design data partitioning, encryption, residency, retention, and portability;
- contain noisy neighbors and reason about tenant, tier, cell, and global SLOs;
- produce auditable usage records, bills, quotas, and tenant unit economics;
- operate and evolve one product across many tenant configurations without forks.

## Recommended module path

### Phase 1 — Learn the SaaS system

| Step | Page | Outcome |
| ---: | --- | --- |
| 1 | [SaaS decision model](concepts.md) | Connect the business model to architecture and operations |
| 2 | [Tenancy, isolation, and placement](tenancy-isolation.md) | Select pool, silo, bridge, cell, and stamp boundaries |
| 3 | [Control plane and tenant lifecycle](control-plane-lifecycle.md) | Automate catalog, provisioning, entitlement, and offboarding workflows |
| 4 | [Identity and authorization](identity-authorization.md) | Bind users and workloads to verified tenant context |
| 5 | [Data, residency, and compliance](data-residency-compliance.md) | Partition, encrypt, retain, export, and delete tenant data |
| 6 | [Reliability, performance, and scale](reliability-performance.md) | Control noisy neighbors, blast radius, capacity, and recovery |
| 7 | [Metering, billing, and economics](metering-billing-economics.md) | Design auditable usage, pricing, quota, and unit-cost flows |
| 8 | [Delivery, observability, and operations](delivery-operations.md) | Release and troubleshoot through tenant-aware operational views |

### Phase 2 — Apply the reasoning

| Step | Page | Outcome |
| ---: | --- | --- |
| 9 | [Enterprise SaaS design exercise](design-exercise.md) | Design an AWS-first regulated B2B SaaS platform |
| 10 | [Scenario questions and model answers](scenarios.md) | Practise at least 15 senior SaaS scenarios |
| 11 | [Advanced architecture and incident drills](scenario-drills.md) | Resolve at least 10 ambiguous tenant failures |
| 12 | [Ten-minute SaaS architecture review](presentation-template.md) | Present business, tenancy, trust, operations, and economics |

### Phase 3 — Revise and assess

| Step | Page | Outcome |
| ---: | --- | --- |
| 13 | [Rapid-fire revision](rapid-fire.md) | Test at least 50 concise explanations |
| 14 | [Active-recall flashcards](flashcards.md) | Revisit at least 25 weak concepts |
| 15 | [Timed SaaS architecture mock interview](../mock-interviews/saas-architecture.md) | Complete a scored 50-minute assessment |
| 16 | [References and videos](references.md) | Deepen weak areas with authoritative sources |

## Scope boundary

[Microservices Architecture](../20-microservices/index.md) provides service-boundary
and distributed-data depth. [API and Identity](../29-api-identity/index.md) covers
protocol and federation mechanics. [FinOps](../26-finops/index.md) covers enterprise
cloud economics. This module applies those capabilities specifically to a provider
operating one product for many tenants. Module 22 covers brokers and streams deeply.

## Completion checklist

- [ ] I can explain why SaaS is more than shared infrastructure.
- [ ] I can justify tenancy separately for compute, data, identity, and telemetry.
- [ ] I can trace tenant context from sign-in through authorization and data access.
- [ ] I can design lifecycle workflows that are idempotent, observable, and reversible.
- [ ] I can explain one tenant's experience during overload, release, and recovery.
- [ ] I can reconcile metered usage with billing and unit economics.
- [ ] I answered all 25 scenarios aloud and completed the scored mock interview.
