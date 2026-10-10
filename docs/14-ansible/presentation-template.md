# Ten-Minute Automation Architecture Review

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Use this structure to present an Ansible platform or change design without
turning the discussion into a list of modules and keywords.

## Minute 0–1 — Outcome and constraints

State the service outcome, fleet, criticality, operating systems, compliance,
connectivity, change window, and recovery objective. Name assumptions.

## Minute 1–2 — Tool and ownership decisions

Explain why Ansible is appropriate, what image pipelines, Terraform/OpenTofu,
deployment platforms, and managed services own, and how overlaps are prevented.

## Minute 2–4 — Targets and trust

Describe inventory source, filters, tag governance, snapshot/limit controls,
human and workload identity, target connection, privilege escalation, secrets,
and execution-zone isolation.

## Minute 4–6 — Content and delivery

Show role/collection contracts, pinned execution environment, review, lint,
integration/convergence tests, approval, canary, bounded batches, handlers, and
outcome verification.

## Minute 6–7 — Failure and recovery

Walk through wrong targets, unreachable hosts, partial mutation, handler failure,
controller loss, and compromised content. State stop conditions and owners.

## Minute 7–8 — AWS and multi-cloud

Explain AWS dynamic inventory and SSH versus Systems Manager. Translate account,
identity, inventory, connectivity, and audit choices to Azure and GCP.

## Minute 8–9 — Adoption and operations

Describe brownfield discovery, paved workflows, delegated ownership, exception
expiry, controller capacity, evidence retention, and legacy retirement.

## Minute 9–10 — Measures and recommendation

Use change success, unreachable and convergence rates, recovery time, inventory
anomalies, credential age, adoption, and service impact. Close with the decision,
largest trade-off, and next validation.

## Reviewer prompts

- Is every mutable field owned by one system?
- Can the exact target set and authority be explained before execution?
- Does the design remain safe when a dependency fails midway?
- Is a second run expected to be unchanged?
- Does evidence prove application outcome, not only task completion?
- Is the migration path credible for current teams?

Return to the [module overview](index.md) when ready to continue.
