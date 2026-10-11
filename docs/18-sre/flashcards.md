# SRE Active-Recall Flashcards

[← Module overview](index.md) · [Rapid-fire revision](rapid-fire.md)

Use these cards without looking at the answer. Mark a card weak if you cannot add
one failure mode and one organizational or cost trade-off.

| Front | Back |
| --- | --- |
| SRE decision loop | Outcome → objective/risk → architecture/operations → change → incident/response → learning/investment. |
| Reliability target inputs | User tolerance, business/contract/safety impact, alternatives, dependencies, recovery, cost, and evidence. |
| Complete SLI definition | Population, valid/good event, measurement point, window, exclusions, delay, owner, and data quality. |
| SLO versus SLA | SLO guides engineering; SLA is an external/business commitment with specified consequences. |
| Error-budget policy purpose | Pre-agree how reliability evidence changes release risk, engineering priority, exceptions, and recovery criteria. |
| Serial availability caveat | Multiplication assumes required path and independence; real systems have correlation, fallback, and degradation. |
| Common-mode failure examples | Shared identity, control plane, network, data, configuration, deployment, quota, and operator. |
| Resilience versus recovery | Resilience maintains acceptable function through faults; recovery restores it after disruption exceeds resilience. |
| Incident role set | Commander, technical/operations leads, communications, scribe, and required specialists/liaisons. |
| Mitigation before root cause | Reduce user harm with reversible safe action; investigate cause in parallel or after stabilization. |
| Strong handover | Roles, impact/state, actions, hypotheses, risk, access, next decisions, and communication commitments. |
| Blameless accountability | Examine contextual decisions without punishment and assign accountable system improvements. |
| Corrective-action evidence | Demonstrated changed behavior: tested recovery, removed hazard, detected condition, or prevented recurrence class. |
| Toil test | Repetitive, manual, automatable, tactical, low enduring value, and scales with service demand. |
| Toil response ladder | Eliminate → simplify/standardize → safe self-service → automate → redesign. |
| Automation safety contract | Preconditions, scope, idempotency, permissions, bounds, evidence, abort, rollback/compensation, and owner. |
| Capacity model | Business demand → workload/resource demand → bottleneck/quotas → test evidence → scaling/headroom/recovery. |
| Failover capacity | Remaining capacity must carry critical load plus recovery effects under the same failure scenario. |
| Safe release contract | Progressive cohort, representative evidence, max exposure, compatibility, abort, rollback/forward, and owner. |
| Chaos experiment contract | Hypothesis, steady state, fault/scope, prerequisite, observer, abort, recovery, learning, follow-up. |
| Operational-readiness gate | Owner, SLO, alerts, runbooks, dependencies, capacity, deployment/recovery, access, contacts, known risks. |
| SRE organizational options | Embedded, central service, consulting/enabling, platform SRE, or product-owned with enablement. |
| On-call health signals | Actionable pages, after-hours load, repeats, escalation, response outcomes, staffing, fatigue, qualitative feedback. |
| AWS reliability anchors | Multi-AZ/Regional services, ELB/Route 53/Auto Scaling, queues, backups/restores, FIS, Resilience Hub, CloudWatch. |
| Strong SRE outcome | User reliability and safer recovery improve while operational load and engineering trade-offs remain sustainable. |

Return to the [module overview](index.md) when ready to continue.
