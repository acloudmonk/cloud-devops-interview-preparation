# Reliability, Observability, and Operations

[← Integration services](integration-services.md) · [Next: Cost and capacity →](cost-capacity.md)

## Derive resilience from objectives

Map user journeys to SLOs, RTO/RPO, dependency budgets, degradation, and data-loss
tolerance. Design across AZs where required, eliminate hidden single points, bound
retries and timeouts, isolate overload, and preserve a simpler recovery path. Multi-
Region is justified by business continuity needs, not architectural prestige.

## Observe the service, platform, and change

Use CloudWatch metrics, logs, alarms, dashboards, synthetics, and tracing/X-Ray or
OpenTelemetry; CloudTrail for API activity; Config for resource history/compliance;
Health and service events for provider impact. Correlate telemetry with deployment,
identity, Region/AZ, account, tenant, and business journey. Define retention, access,
cost, and data protection.

## Operate through automation with escape paths

Use Systems Manager and automation for inventory, patching, commands, sessions, and
runbooks where applicable. Prefer auditable, short-lived operator access. Automate
safe diagnosis and remediation with scope, concurrency, circuit breakers, approvals,
rollback, and evidence; preserve manual break-glass procedures for automation failure.

## Engineer recovery

Backups, replicas, Multi-AZ, and multi-Region solve different failures. Test restore,
failover, failback, DNS/routing, identity, keys, quotas, dependencies, data integrity,
and operator readiness. AWS Resilience Hub and Fault Injection Service can help assess
and exercise architectures, but owners must define hypotheses and safe boundaries.

## Run incidents and changes

Define on-call, severity, command, communications, vendor escalation, access,
containment, recovery, and learning. Deploy gradually with health metrics and abort
conditions. Track toil, recurring failure, operational readiness, and action closure;
runbooks without exercised people and permissions are not recovery capability.
