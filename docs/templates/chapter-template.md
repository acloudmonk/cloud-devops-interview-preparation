# Module Title

Last reviewed: **YYYY-MM-DD**
Level: **Foundation / Advanced / Architect**

## Why this matters

State the business and architectural relevance.

## Learning objectives

- Objective one
- Objective two
- Objective three

## Mental model

Give the smallest useful model before introducing products or implementation.

## Core concepts

Explain terminology, boundaries, invariants, and failure behavior.

## Architecture decisions

| Decision | Option A | Option B | Selection factors |
| --- | --- | --- | --- |
| Example | Description | Description | Constraints and trade-offs |

Document important choices as Architecture Decision Records. Include the
context, decision, alternatives, consequences, validation evidence, owner, and
review trigger.

## Security, reliability, operations, and cost

Cover all four dimensions or explicitly explain why one is not applicable.

## Cross-cloud relevance

| Capability | AWS | Azure | GCP | Vendor-neutral option |
| --- | --- | --- | --- | --- |
| Example | Service | Service | Service | Technology |

Explain semantic differences such as delivery guarantees, ordering,
consistency, transaction boundaries, scaling, identity, networking, recovery,
quotas, and pricing. A list of similar service names is not sufficient.

## AWS implementation reasoning

Unless the subject is specific to another platform, use AWS for the concrete
architecture walkthrough. Include service-selection rationale, identity,
networking, telemetry, validation, cost, and recovery reasoning. Application
code and cloud deployment are optional future material. Keep the concept
explanation vendor neutral.

## Capacity, SLOs, and recovery

Show reproducible demand assumptions, SLI/SLO definitions, error-budget or
burn-rate thinking, service quotas, RTO/RPO, and measured restore evidence.

## Threat model and trust boundaries

Identify actors, entry points, data classes, trust boundaries, abuse cases,
least-privilege controls, encryption, audit, residency, and remaining risks.

## Troubleshooting

Start from symptoms and evidence. Avoid product-specific guesses.

Add a runbook or decision tree for the most likely operational failures.

## Common mistakes

- Mistake and consequence
- Mistake and consequence

## Hands-on exercise

Link to a lightweight design exercise with requirements, assumptions, capacity,
diagrams, decisions, failure analysis, SLOs, cost, and presentation evidence.
Do not require code or cloud deployment unless a later milestone explicitly
adds an optional implementation lab.

## Knowledge checks

Include short questions, one design exercise, common follow-up questions, and
scoring anchors for weak, acceptable, and strong answers.

## Interview practice

Link to scenarios, rapid-fire questions, and a scoring rubric.

## References

Use the reference template and include a last-verified date, lifecycle status,
and replacement link for deprecated material.
