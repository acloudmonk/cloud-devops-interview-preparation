# Ten-Minute SaaS Architecture Review

[← Advanced drills](scenario-drills.md) · [Next: Rapid-fire revision →](rapid-fire.md)

Use this structure to communicate a SaaS design without collapsing into a cloud
service inventory.

## 0:00–1:00 — Product and tenant

State business model, tenant definition, plans, scale distribution, customer journeys,
regulatory markets, service commitments, and provider economic goals.

## 1:00–2:30 — Tenancy and placement

Show pool, silo, and bridge choices for compute, data, identity, keys, telemetry, and
analytics. Explain regional cells, placement authority, blast radius, and migration.

## 2:30–4:00 — Trust and data

Trace tenant resolution, federation, authorization, workload identity, partitioning,
encryption, residency, support access, audit, export, retention, and deletion.

## 4:00–5:30 — Control plane and lifecycle

Present catalog authority, onboarding state machine, configuration, entitlement,
quota, suspension, offboarding, idempotency, reconciliation, and control-plane outage.

## 5:30–7:00 — Reliability and operations

Explain tenant/tier SLOs, fairness, overload, cell capacity, telemetry, progressive
delivery, recovery, fleet management, incident impact, and customer communication.

## 7:00–8:00 — Metering and economics

Separate usage ledger, rating, billing, entitlement, and enforcement. Show lineage,
corrections, cost allocation, tier margin, and how economics affects placement.

## 8:00–9:00 — Migration and multi-cloud

Sequence customer cohorts, data verification, federation, compatibility, rollback,
and legacy retirement. Translate capabilities across AWS, Azure, and Google Cloud
without promising false parity or synchronous cross-cloud critical paths.

## 9:00–10:00 — Decision and risk

Restate recommended model, first milestone, measurable outcomes, top risks, controls,
residual uncertainty, and evidence that would cause the design to change.
