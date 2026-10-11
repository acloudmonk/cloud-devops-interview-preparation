# Ten-Minute Reliability Review

[← Module overview](index.md) · [Design exercise](design-exercise.md)

Use this structure to present an SRE recommendation. Lead with the user promise
and reliability risk, not team structure or tooling.

## 0:00–1:00 — Outcome and reliability gap

State the critical journey, users, business harm, current SLO/incident evidence,
dominant uncertainty, constraints, and desired decision.

## 1:00–2:00 — Objectives and governance

Define SLI population/good event/measurement, SLO target/window, recovery needs,
error-budget state, policy, owner, and contractual boundary.

## 2:00–4:00 — Architecture and risk

Trace dependencies and failure domains; explain capacity, quotas, redundancy,
containment, degradation, data, recovery, AWS controls, and assumptions about
correlation and multi-cloud services.

## 4:00–5:30 — Incident and learning system

Cover declaration, command/technical/communications roles, mitigation authority,
handover, customer updates, postmortem triggers, corrective actions, and verification.

## 5:30–6:30 — Change and resilience

Show progressive delivery, compatibility, rollback/roll-forward, readiness gates,
load/recovery tests, game days, and a bounded fault experiment.

## 6:30–7:30 — Capacity and automation

Explain demand/peak/failure forecasts, headroom, scaling, bottlenecks, quotas, toil
priorities, safe self-service/automation, and manual recovery competence.

## 7:30–9:00 — Organization and migration

Name product/platform/SRE/risk owners, engagement model, on-call staffing and
health, first journey, rollout waves, exceptions, investment, and exit criteria.

## 9:00–10:00 — Measures and recommendation

Report SLO/user impact, detection/mitigation/recovery, recurrence, change risk,
capacity, toil/pages, verified actions, and team health. Close with the first
decision, trade-off, and validation experiment.

Return to the [module overview](index.md) when ready to continue.
