# Reliability, Observability, and Operations

[← Service selection](service-selection.md) · [Next: Cost and capacity →](cost-capacity.md)

Reliability belongs to a user journey. Define SLI, SLO, error budget, dependency budget,
failure domains, degradation, RTO/RPO, and recovery evidence.

Use Cloud Monitoring metrics/SLOs, Cloud Logging structured logs, trace context, Cloud
Trace, Error Reporting, audit logs, uptime checks, and business probes as appropriate.
Standardize labels, correlation, retention, access, routing, redaction, and cost.

- distribute stateless capacity and verify health-check semantics;
- bound timeouts, retries, concurrency, queues, and connection pools;
- shed optional work before cascading failure;
- plan zone/region capacity, quotas, DNS, keys, identity, and operator access;
- protect backups independently and restore into an isolated environment;
- validate records and business invariants before declaring recovery.

Operate through detect → assess impact → stabilize → diagnose → recover → verify →
learn. Runbooks include access, decision points, rollback, evidence, communications,
and escalation. Test them in game days. Track SLO burn, alert quality, toil, change
failure, restore duration, repeat incidents, and action completion.
