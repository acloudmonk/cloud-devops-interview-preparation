# Safe Change and Resilience Testing

[← Module overview](index.md) · [Module 09: CI/CD](../09-cicd/index.md)

Change is a major source of production risk, while avoiding change leaves defects,
security exposure, and operational drift. SRE reduces the blast radius and time
to detect, decide, and recover.

## Change-safety model

- small, attributable, reviewed, automated changes;
- representative pre-production and production verification;
- backward/forward compatibility for APIs, data, events, and configuration;
- progressive exposure by instance, zone, region, tenant, or traffic cohort;
- automated health/SLO analysis with human authority for ambiguous risk;
- fast rollback or roll-forward, plus tested data recovery where reversal is unsafe;
- change freeze criteria based on risk, not calendar superstition.

Separate deployment from release using feature controls, but operate flag ownership,
expiry, state, audit, dependency, and emergency behavior. Rollback is not safe when
database or message changes are incompatible; use expand/migrate/contract patterns.

## Release reliability

Use canary, rolling, blue/green, or traffic-shadow patterns according to state,
capacity, observability, and risk. Define evaluation window, comparable baseline,
minimum sample, success/failure signals, max exposure, abort, and decision owner.
Avoid a canary that shares the same dependency/configuration fault or receives only
low-risk traffic.

## Resilience testing ladder

1. Unit/property tests for retries, timeouts, idempotency, and state transitions.
2. Integration tests for dependency and partial-failure semantics.
3. Load/stress/soak tests for capacity and performance limits.
4. Recovery tests for restore, failover, rollback, credential, and access paths.
5. Game days for people, process, communication, and multi-system response.
6. Controlled fault injection/chaos experiments in production-like or production scope.

## Chaos experiment contract

State hypothesis, steady-state/user measure, fault, scope/blast radius, prerequisites,
owner, observers, abort threshold, rollback, expected learning, and follow-up. Begin
with a known recovery mechanism and smallest useful scope. Do not experiment during
unknown instability or use chaos to prove bravery.

AWS Fault Injection Service can inject supported AWS faults; Resilience Hub can
assess and organize resilience posture. Azure Chaos Studio and provider/platform-
specific Google Cloud or open-source tools provide related capabilities. The tool
does not define the hypothesis, business safety, or recovery ownership.

## Readiness gate

Before production ownership, require service/owner inventory, SLOs, dashboards,
alerts, runbooks, dependency and capacity review, deployment/rollback, backup/
restore evidence, security access, incident contacts, known risks, and on-call
training. Exceptions need a risk owner, compensating control, and expiry.

Return to the [module overview](index.md) when ready to continue.
