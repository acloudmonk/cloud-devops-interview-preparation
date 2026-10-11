# Scope, Discovery, and Evidence

[← Module overview](index.md) · [Architecture-review model](concepts.md)

The workload—not the cloud account—is the primary review boundary. A workload is a
set of technology and operational components that together deliver a business
outcome. Shared platforms and external services appear as dependencies or separate
review scopes with explicit contracts.

## Scope statement

Record business outcome, users, owner, lifecycle stage, critical journeys, data
classification, Regions/providers, environments included, shared dependencies,
third parties, review trigger, time horizon, known constraints, and exclusions.
State whether the review covers design intent, production reality, or both.

Avoid reviewing an entire enterprise in one session. Split by business service or
independently operated workload, then review portfolio-wide controls separately.

## People to involve

- business and product owner for value, criticality, and risk acceptance;
- architect and senior engineers for decisions and dependencies;
- operations/SRE for incidents, SLOs, capacity, recovery, and toil;
- security/privacy/compliance for threats, data, and obligations;
- finance/FinOps for cost and value evidence;
- platform/network/data specialists and critical supplier owners;
- facilitator who can separate discovery from judgment.

## Pre-review evidence

Request the minimum useful pack: current context and dependency diagrams; critical
journeys and quality targets; data flows and classification; identity/trust model;
deployment and change process; observability and incidents; capacity/performance
tests; backup/DR exercises; cost/unit economics; risks/exceptions; and major ADRs.

Do not delay all discovery until documents are perfect. Missing or stale artifacts
are themselves observations, and the session can establish what evidence matters.

## Question pattern

Ask: “What outcome does this support?”, “How does it fail?”, “What tells you that?”,
“When was that tested?”, “Who decides and responds?”, and “What trade-off was
accepted?” Follow the critical request path and dependency graph rather than moving
mechanically through provider questions.

## Evidence hygiene

Capture source, owner, environment, date, scope, and confidence. Protect diagrams,
commercial data, incident records, vulnerabilities, and customer information with
least privilege and retention. Do not paste secrets or sensitive configurations
into review tools. Distinguish current observation from future design intent.

## Readiness and stop conditions

Reschedule or narrow the review if no accountable workload owner participates, the
scope cannot be defined, or disclosure restrictions prevent meaningful evidence.
Proceed with explicit uncertainty when that is itself useful, but do not present
the result as comprehensive.

Return to the [module overview](index.md) when ready to continue.
