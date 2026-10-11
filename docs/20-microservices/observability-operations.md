# Observability and Operations

[← Delivery and testing](delivery-testing.md) · [Next: Organization and migration →](organization-migration.md)

## Observe customer journeys and boundaries

Use metrics, structured logs, traces, profiles, events, deployment markers, and
business state. Propagate correlation and trace context across requests and messages,
while protecting sensitive data. Trace sampling must retain errors and rare critical
paths without making telemetry cost unbounded.

Define SLOs for customer journeys and owned services. Page on actionable symptoms;
use service metrics for diagnosis. Track dependency latency/errors, saturation,
retry volume, queue age, duplicate/reconciliation rate, saga age, and contract
version usage.

## Ownership and incident response

Maintain a current service catalog with team, repository, API/events, dependencies,
data classification, dashboards, SLO, runbook, on-call, cost, and lifecycle. Catalog
freshness is an operational control, not documentation decoration.

During incidents establish command, protect users/data, bound retries, shed load,
pause unsafe consumers or releases, and preserve evidence. A distributed trace is
useful but not a causal proof; correlate deploys, infrastructure, state, and business
events.

## Recovery

Back up and restore service data with dependency-aware RTO/RPO. Rebuild derived
views, replay safely, reconcile external side effects, and verify business invariants.
Test loss of region, broker, identity, discovery, control plane, and observability;
avoid making diagnostic tools a runtime dependency.

## Cost and lifecycle

Allocate compute, storage, data transfer, telemetry, messaging, and platform cost by
service/team/journey where useful. Retire unused services, endpoints, event versions,
flags, and data. A small service still has fixed ownership and operational cost.
