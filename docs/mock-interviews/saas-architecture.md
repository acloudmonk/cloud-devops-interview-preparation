# SaaS Architecture Mock Interview

[← Mock interview overview](index.md) · [Module 21 overview](../21-saas/index.md)

Duration: **50 minutes**
Level: **Senior / Architect**
Primary context: **AWS-first regulated B2B SaaS with multi-cloud dependencies**

## Candidate brief

A compliance-workflow vendor operates 180 customer-specific installations. It wants
one SaaS product for 10,000 organizations across North America, Europe, and India.
Tenant sizes range from five to 80,000 users. Enterprises require federation, audit,
residency, exports, and optional dedicated data; small customers expect instant trials.
Design the target architecture and an evidence-led migration.

## Interview structure

### 0–7 minutes — Discovery and SaaS contract

Clarify tenant definition, plans, pricing units, scale distribution, journeys, SLO,
RTO/RPO, identity, isolation, residency, audit, lifecycle, migration, and economic
objectives. Distinguish SaaS from infrastructure sharing.

### 7–18 minutes — Tenancy, control plane, and trust

Choose pool/silo/bridge boundaries for compute, data, keys, identity, and telemetry.
Describe cells, placement, catalog, onboarding, entitlements, federation, tenant
context, authorization, workload identity, support access, and isolation evidence.

### 18–28 minutes — Data, reliability, and operations

Cover partitioning, residency, encryption, retention, export, deletion, tenant/tier
SLOs, noisy-neighbor controls, capacity, recovery, progressive delivery, telemetry,
fleet governance, and control-plane failure.

### 28–38 minutes — Failure branches

Choose three:

- a cache returns one tenant's object to another;
- a bulk export exhausts shared database connections;
- tenant routing points to the wrong regional cell;
- federation expires for one enterprise;
- regional recovery violates data residency;
- a metering replay doubles customer invoices;
- restore reintroduces deleted tenant data;
- a release fails only for legacy-schema tenants.

### 38–45 minutes — Economics and migration

Explain usage ledger, rating, billing, quota, entitlement, disputes, cost allocation,
tier margin, cohort migration, compatibility, rollback, customer communication, and
retirement of customer-specific installations.

### 45–50 minutes — Executive close

State the recommended tenancy and cell model, first milestone, product and operating
outcomes, principal risks, residual uncertainty, and evidence that could change the
design.

## Scoring rubric

| Dimension | Points |
| --- | ---: |
| Product model, discovery, and tenant definition | 6 |
| Tenancy, placement, cells, and isolation | 10 |
| Control plane, lifecycle, identity, and authorization | 9 |
| Data, compliance, residency, and deletion | 7 |
| Reliability, performance, delivery, and operations | 8 |
| Metering, billing, economics, and migration | 7 |
| Trade-offs and executive communication | 3 |
| **Total** | **50** |

Interpretation: **43–50** architect-ready; **35–42** strong with targeted gaps;
**25–34** incomplete tenant, lifecycle, or economic reasoning; **below 25** rebuild
from the SaaS contract and trusted tenant context. A service-list answer cannot
exceed 34.

## Improvement loop

Record the three weakest decisions, return to the matching module pages and primary
sources, redraw tenant trust and lifecycle state, then repeat within seven days with
different failure branches.
