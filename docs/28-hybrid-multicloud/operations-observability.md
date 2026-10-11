# Operations and Observability

[← Module overview](index.md) · [Platforms and delivery](platform-portability.md)

A distributed estate needs one service operating model even when provider tools
remain different. Organize around business services, not separate cloud dashboards.

## Operational foundation

- authoritative inventory of workloads, environments, owners, criticality, data, and dependencies;
- shared SLI/SLO and incident severity language with provider-specific runbooks;
- consistent change, maintenance, vulnerability, backup, capacity, and lifecycle responsibilities;
- central service view plus drill-down to raw native telemetry and audit evidence;
- support contracts, escalation paths, time zones, and handovers tested before incidents.

## Telemetry architecture

Use OpenTelemetry and common semantic conventions where they add interoperability.
Preserve provider-native logs, metrics, traces, events, billing, and security context.
Control cardinality, volume, retention, privacy, egress, time synchronization, and
failure buffering. A central platform should not be a single point that blinds every environment.

## Incident command

Declare one incident with a clear commander, provider/environment leads, security,
communications, business owner, and vendor liaison. Maintain a shared timeline and
facts while assigning environment-specific investigation. Track provider tickets,
contractual notifications, data consistency, and recovery decisions centrally.

## Configuration and drift

Separate global intent from environment realization. Continuously inventory and
compare policy, versions, identity, routes, DNS, certificates, artifacts, data schemas,
and recovery readiness. Resolve intentional differences through ADRs and exceptions,
not forced uniformity.

## Operating-capability test

Can on-call engineers locate the owner, trace a user journey across boundaries,
diagnose link versus application failure, obtain emergency access, contact providers,
degrade safely, reconcile data, and restore visibility without one central tool?

Return to the [module overview](index.md) when ready to continue.
