# Reliability, Observability, and Operations

[← Service-selection matrices](service-selection.md) · [Next: Cost and capacity →](cost-capacity.md)

## Derive resilience from requirements

Map journeys to SLOs, RTO/RPO, dependency budgets, degradation, and loss tolerance.
Choose zonal, zone-redundant, or Regional service topologies from verified semantics;
remove hidden single-zone dependencies; bound timeouts/retries; isolate overload; and
preserve a simpler recovery path. Multi-Region requires data and operating justification.

## Build actionable observability

Azure Monitor encompasses platform metrics, logs, alerts, workbooks, managed Prometheus,
and Application Insights capabilities; Log Analytics workspaces store/query supported
logs; Activity Log captures subscription control-plane events. Add Resource Health,
Service Health, Change Analysis, Network Watcher, and workload telemetry as needed.
Correlate by deployment, tenant, subscription, Region/zone, and business journey.

## Create an operations baseline

Define ownership, inventory, configuration, update/patch, vulnerability, backup,
monitoring, alerting, automation, incident, change, capacity, cost, and support. Azure
Arc can extend management to supported hybrid/multicloud resources; Azure Automation,
Update Manager, Policy, and Monitor can standardize controls. Preserve auditable
emergency access and manual paths when central automation is unavailable.

## Engineer recovery

Azure Backup, Site Recovery, native replicas, availability features, and multi-Region
patterns solve different failures. Test restore, failover, failback, routing/DNS,
identity, keys, quotas, dependencies, data integrity, and operator readiness. Recovery
plans need business validation and current permissions—not only successful platform jobs.

## Operate incidents and changes

Define on-call, severity, command, communications, Microsoft/support escalation,
diagnostic access, containment, recovery, and learning. Deploy through slots, canaries,
revisions, or controlled rollouts with health and abort conditions. Track toil,
recurring failure, operational readiness, and action closure; validate runbooks in games.
