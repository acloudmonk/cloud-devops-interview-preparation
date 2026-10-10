# Ten-Minute IaC Architecture Review

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Use this structure to present an infrastructure delivery platform to technical and
executive interviewers.

## 0:00–1:00 — Outcome and constraints

State the business outcome, regulatory needs, scale, team model, change frequency,
recovery objective, and current failure evidence. Declare assumptions.

## 1:00–2:30 — Ownership and boundaries

Show root/state boundaries by account, region, environment, capability, and owner. Name
the source of truth, dependency contracts, and what IaC deliberately does not own.

## 2:30–4:00 — State and identity

Explain backend durability, locking, encryption, recovery, short-lived workload identity,
plan/apply separation, runner trust, and break glass.

## 4:00–5:30 — Module and repository model

Describe platform module contracts, safe defaults, versioning, upgrade/deprecation,
repository choice, and promotion without copied environments.

## 5:30–7:00 — Delivery controls

Walk through tests, target-specific saved plan, policy and cost/security evidence,
approval, same-plan apply, post-apply verification, and drift detection.

## 7:00–8:00 — Terraform and OpenTofu

Explain Terraform-first standardization, permitted OpenTofu use, managed-platform needs,
tool-specific features, version pinning, migration evidence, and support ownership.

## 8:00–9:00 — Failure and recovery

Cover partial apply, stale/destructive plan, state recovery, provider compromise, manual
emergency change, and stop/rollback/roll-forward criteria.

## 9:00–10:00 — Adoption and decision

Propose a bounded pilot, legacy-root inventory, migration waves, measures, named owners,
risks, and the next decision required from leadership.

## Closing sentence

“The recommendation is a small, supported IaC platform contract with bounded state and
identity, evidence-based applies, recoverable lifecycle, and deliberate Terraform/OpenTofu
governance—not one tool, state file, or administrator credential for everything.”
