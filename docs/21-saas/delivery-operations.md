# Delivery, Observability, and Operations

[← Metering, billing, and economics](metering-billing-economics.md) · [Next: Enterprise design exercise →](design-exercise.md)

## One product, controlled exposure

Use immutable artifacts, automated database compatibility, deployment rings, cells,
and tenant-aware feature flags. Release order should include internal test tenants,
canary cells, early adopters, then broader cohorts. Track which software, schema,
configuration, and entitlement versions each tenant receives. Feature flags need
owners, expiry, safe defaults, audit, and removal; they must not become permanent
customer-specific forks.

## Tenant-aware telemetry

Correlate request, job, event, deployment, cell, tier, and pseudonymous tenant ID.
Offer global, cell, tier, and individual-tenant views. High-cardinality tenant labels
can overwhelm metric systems, so combine bounded aggregates with logs, traces, and
controlled drill-down. Apply access, redaction, retention, and residency to telemetry.

## Operational signals

Track customer journeys, saturation and fairness, queue age, isolation denials,
catalog/configuration staleness, onboarding duration, entitlement failures, metering
lag, invoice reconciliation, tenant moves, deletion backlog, and per-tenant cost.
Infrastructure health without tenant experience is insufficient.

## Support and incident response

Support tooling should show tenant placement, recent changes, feature state, service
health, limits, and safe diagnostic actions without exposing other tenants. Incidents
need impact by tenant and tier, containment by cell or workload, communication,
correctness checks, and later reconciliation. Do not publish another tenant's identity
or behavior in status communications.

## Fleet governance

Inventory every stamp and cell, version, policy, key state, capacity, and compliance
attribute. Detect drift, roll out changes progressively, and enforce maximum supported
version skew. Automate repairs but guard high-blast-radius control-plane actions with
preview, concurrency bounds, approval, and abort conditions.

## Multi-cloud translation

AWS CloudWatch and OpenTelemetry, Azure Monitor, and Google Cloud Observability can
all participate in tenant-aware operations. The architecture requirement is portable:
propagate safe context, preserve isolation, control cardinality, connect technical and
business signals, and make fleet state queryable. Product names do not create that
operating model automatically.
