# Advanced Program and Cutover Drills

[← Scenario questions](scenarios.md) · [Next: Presentation template →](presentation-template.md)

For each drill, state immediate control, investigation, decision authority, recovery,
communications, evidence, and prevention. Practise a three-minute response.

## Drill 1 — Hidden dependency before cutover

Telemetry reveals that a supposedly isolated workload calls an undocumented license
server three days before cutover. Do not ignore or blindly open access. Establish
business impact and frequency, validate ownership and license/network constraints,
test a controlled target path, update the dependency graph and runbook, and reassess
go/no-go. If evidence cannot be produced, defer the workload or keep its dependency
group together. Record why the discovery process missed it and improve later gates.

## Drill 2 — Replication lag consumes the rollback window

Pause progression and protect the authoritative source. Measure change rate, backlog,
throughput, source pressure, network, large transactions, and target apply behavior.
Reduce avoidable load or increase safe capacity, then recalculate the cutover and
rollback timelines from evidence. Do not cut over with unknown divergence. If the
window cannot be met, reschedule, change synchronization strategy, or obtain explicit
business acceptance for a different downtime model.

## Drill 3 — Landing-zone control blocks production traffic

Treat the guardrail as a control until proven incorrect. Identify the intended flow,
control objective, denied event, and least-privilege change. Test in a representative
environment and preserve audit. If a temporary exception is unavoidable, bound its
scope, owner, compensating monitoring, expiry, and removal. Feed repeated legitimate
denials into the platform product rather than creating permanent workload-specific
bypasses.

## Drill 4 — DNS cutover is only partially visible

Segment resolution by resolver, geography, client, TTL, cache, split-horizon zone,
and record family. Confirm health checks and routing independently of DNS. Keep the old
endpoint safe and monitored while authority remains clear; use cohort routing where
available. Decide rollback before writes or state diverge. Future rehearsals must
measure actual cache behavior and include internal, partner, mobile, and batch clients.

## Drill 5 — Performance passes, month-end batch fails

Separate interactive averages from the full business workload. Capture the batch
critical path, data volume, concurrency, locks, storage/network throughput, quotas,
and dependent deadlines. Compare with the current baseline and target acceptance.
Tune or redesign only with bottleneck evidence; consider schedule, partitioning, and
bounded scale. The workload remains unaccepted until representative peak-cycle
evidence or an explicitly approved contingency exists.

## Drill 6 — Rollback would lose new cloud writes

Stop treating rollback as a routing flip. Identify the authoritative log, writes since
cutover, idempotency, reverse replication, conflicts, and business invariants. Freeze
or fence further writes if safe, preserve evidence, and choose reconciliation plus
reverse sync, cohort fallback, or forward fix. Business and data owners approve the
loss/availability trade-off. Redesign the next cutover with an explicit last safe
rollback point and post-cutover-write treatment.

## Drill 7 — Cost doubles after successful migration

Separate expected dual-run cost from waste and structural target cost. Validate tags,
allocation, demand, sizing, schedules, storage lifecycle, data transfer, licenses,
support, shared costs, and idle legacy assets. Right-size after performance evidence,
remove temporary resources, and accelerate safe decommissioning. Avoid long-term
commitments until demand stabilizes. Report unit economics and benefit variance with
owners, rather than claiming success from technical cutover alone.

## Drill 8 — A vendor administrator needs broad temporary access

Define the exact task, systems, time, location, identity, and data exposure. Prefer a
named federated identity, just-in-time elevation, constrained session, approval,
recording/logging, supervised break-glass path, and immediate revocation. Verify vendor
contract and data-handling terms. If residual risk exceeds authority, escalate or
delay; never hide a shared account in the runbook. Review evidence and remove access
afterward.

## Drill 9 — The executive dashboard is green but waves keep slipping

Audit metric definitions and source data. Replace activity counts with dependency
confidence, ready inventory, gate pass rate, blocker age, queue time, rework, defect
escape, cutover stability, legacy closure, and benefit measures. Reforecast with
confidence ranges and show the constraint explicitly. Create accountable decisions,
not cosmetic status. Psychological safety and independent review matter because a
program that punishes red status loses its early-warning system.

## Drill 10 — A rewrite program is halfway complete and value is doubtful

Reassess the original constraint, delivered increments, remaining cost, schedule,
risk, demand, skills, and credible alternatives without privileging sunk cost. Preserve
useful assets and establish a thin end-to-end slice or strangler boundary. Options may
be narrow the scope, replatform, repurchase, retain, or stop. Leadership decides from
forward-looking value and exit implications; teams receive a clear operating and data
migration path.

## Drill 11 — Decommissioning threatens records retention

Do not power off until legal, records, security, data, and business owners agree on
what must remain, format, immutability, access, search, retention, legal hold, deletion,
recovery, and evidence. Validate the archive and retrieval process with representative
requests. Remove production access and licenses in controlled stages, sanitize assets,
update inventories and continuity plans, and retain signed closure evidence. Archiving
unreadable data is not compliant decommissioning.
