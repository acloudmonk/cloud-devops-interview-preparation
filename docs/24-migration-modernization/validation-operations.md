# Validation and Operational Acceptance

[← Data movement and cutover](data-cutover.md) · [Next: Security, compliance, and governance →](security-compliance.md)

## Build a traceable acceptance model

Map business journeys and nonfunctional requirements to tests, owners, environments,
evidence, thresholds, and defects. Cover functional behavior, integrations, data,
performance, scale, resilience, recovery, security, compliance, accessibility,
observability, deployment, operability, and cost. Baseline the current service where
that baseline is healthy; otherwise use agreed target outcomes.

## Test failure and recovery

Exercise dependency loss, network impairment, quota exhaustion, identity failure,
regional or zonal events where relevant, bad deployment, corrupted data, backup
restore, failover/failback, alert routing, and operator access. Confirm RTO/RPO through
timed evidence rather than architecture claims.

## Make operations ready before cutover

Name the service owner, on-call team, escalation path, dashboards, SLOs, alerts,
runbooks, access, configuration/asset records, maintenance, capacity process, backup,
security response, vendor support, cost owner, and known risks. Train using scenarios
and shadow support; a document handoff alone does not create capability.

## Hypercare with exit criteria

Use enhanced monitoring and staffed triage for a defined period. Track errors,
latency, saturation, data reconciliation, security findings, user impact, spend,
incidents, and workarounds. Exit when explicit stability and ownership criteria are
met—not merely when the calendar expires.

## Separate completion states

Technical cutover, business acceptance, operational acceptance, security closure,
legacy decommissioning, financial closure, and benefits realization are different
states. Report each so migrated-but-not-closed workloads do not accumulate risk and
double cost.
