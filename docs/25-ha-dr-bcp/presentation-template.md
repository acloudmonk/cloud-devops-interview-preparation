# Ten-Minute Continuity Review

[← Module overview](index.md) · [Design exercise](design-exercise.md)

Use this structure when an interviewer asks for an executive architecture review.
Keep service names subordinate to outcomes, assumptions, and evidence.

## Minute 0–1 — Outcome and scope

Name the critical business service, users, minimum acceptable operation, operating
period, regulatory context, and disruptions included and excluded.

## Minute 1–2 — Impact and objectives

State impact over time, recovery tier, availability target, RTO, RPO, MTPD, work
recovery time, measurement boundaries, and accountable approver.

## Minute 2–4 — Failure model and architecture

Walk through component, zone, Region, data, cyber, identity, control-plane, supplier,
and people failures. Show regional HA, selected DR strategy, data ownership,
isolation, degraded modes, and recovery dependency order.

## Minute 4–5 — Data and cyber recovery

Explain replication and lag, backups, immutability, account/key isolation, clean-room
recovery, integrity checks, transaction reconciliation, retention, and evidence.

## Minute 5–6 — Activation and traffic

Describe signals, declaration authority, command roles, fencing, capacity, routing,
promotion, communication, validation gates, and point of no return.

## Minute 6–7 — Business continuity

Cover workforce, facilities, suppliers, alternate channels, manual process capacity,
security/privacy controls, customer/regulator communication, and backlog recovery.

## Minute 7–8 — Failback and return to normal

Define the source of truth, resynchronization, reconciliation, readiness, phased
traffic movement, restored protection, emergency-access closure, and closure criteria.

## Minute 8–9 — Evidence and governance

Present restore and failover results, actual RTO/RPO, scenario coverage, unresolved
findings, owners, retest dates, change triggers, exceptions, and risk acceptance.

## Minute 9–10 — Recommendation

Summarize the largest risk, target state, immediate controls, phased investment,
cost/complexity trade-off, residual risk, decision required, and success measure.

## Closing sentence pattern

“For **[business service]**, I recommend **[strategy]** against **[failure set]**
to meet **[service/RTO/RPO]**. We will prove it through **[exercise/evidence]**;
the business must decide **[investment or residual risk]**.”

Return to the [module overview](index.md) when ready to continue.
