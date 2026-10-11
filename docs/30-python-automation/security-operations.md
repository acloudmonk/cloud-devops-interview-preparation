# Security, Observability, and Governance

[← Packaging](packaging-delivery.md) · [Next: Design exercise →](design-exercise.md)

Automation is privileged production software. Govern its identity, changes, evidence,
and emergency behavior according to blast radius.

## Security

Use short-lived workload identity, least privilege, permission boundaries, isolated
environments, protected dependencies, and secret-manager retrieval. Validate every
target and untrusted input. Avoid `eval`, unsafe deserialization, shell string
construction, permissive temporary files, and logging credentials or sensitive data.
Separate plan, approval, execution, and audit roles for high-risk work.

## Observability contract

Emit structured events with run ID, tool/version, actor, environment, target, action,
attempt, duration, outcome, reason, and provider request ID. Metrics include selected,
changed, unchanged, skipped, failed, uncertain, retry/throttle, age/backlog, duration,
and cost. Trace meaningful API/workflow boundaries; do not create expensive noise.

## Governance

Inventory owners, repositories, artifacts, schedules/triggers, runtime identities,
permissions, targets, data classification, dependencies, SLOs, change history, and
retirement. Classify automation by impact and require stronger approval, isolation,
testing, and rollout as blast radius grows.

## Incident model

Provide a kill switch that prevents new work without corrupting active state. Revoke
identity, preserve code/config/checkpoint/provider evidence, enumerate affected targets,
stabilize, reconcile against authoritative state, restore through reviewed artifacts,
and communicate residual uncertainty.

## Economics

Count API calls, logs, compute, storage, network, licenses, operator/review time,
incident risk, and maintenance. Measure lead time, failure/recovery rate, toil removed,
policy coverage, correctness, and adoption—not lines of Python or jobs executed.
