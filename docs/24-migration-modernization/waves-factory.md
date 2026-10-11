# Waves and the Migration Factory

[← Landing-zone readiness](landing-zone-readiness.md) · [Next: Data movement and cutover →](data-cutover.md)

## Form waves around dependencies and outcomes

Sequence business capabilities and strongly connected dependencies, not arbitrary
server batches. Consider critical calendars, data gravity, shared services, latency,
vendor availability, environments, compliance, change freezes, team capacity, and
rollback feasibility. Keep waves small enough to learn and large enough to deliver a
meaningful outcome.

## Start with representative learning

A first wave should be valuable but recoverable and should exercise identity,
connectivity, delivery, data, monitoring, security, support, cost, and shutdown paths.
Avoid choosing only trivial workloads; they create false confidence. Feed lessons into
standards, estimates, automation, and later wave composition.

## Operate a migration factory

Use repeatable intake, assessment, design, remediation, build, test, cutover,
hypercare, handover, and decommissioning. Standard artifacts and automation improve
flow, but workload owners remain accountable for behavior and acceptance. Track queues,
blocked time, rework, defect escape, and constraint capacity—not only completions.

## Wave gates

- **Entry:** ownership, scope, dependency confidence, disposition, target, funding.
- **Build-ready:** landing zone, connectivity, access, automation, quotas, licenses.
- **Cutover-ready:** rehearsed runbook, validation, monitoring, support, rollback.
- **Operational acceptance:** SLOs, alerts, recovery, security evidence, knowledge.
- **Closure:** data retention, legacy shutdown, contracts, CMDB, benefits, lessons.

## Govern without hiding bad news

Maintain an integrated dependency plan, decision/risk/assumption/issue log, wave
dashboard, change control, architecture/security review, and accountable escalation.
Use confidence ranges and expose blocked work. Red status is useful information; a
green dashboard with unresolved dependencies is not control.
