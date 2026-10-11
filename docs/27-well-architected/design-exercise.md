# Enterprise Well-Architected Review Exercise

[← Module overview](index.md) · [Tools and metrics](tools-automation.md)

## Brief

A regulated payments workload runs primarily on AWS across three Availability
Zones. Azure provides workforce identity and Google Cloud hosts analytics. The
service grew through acquisitions and now includes EKS, Aurora PostgreSQL, Kafka,
S3, third-party payment networks, and a shared observability platform. It promises
99.99% availability, but SLO evidence is inconsistent. A recent deployment caused
a four-hour outage, DR has never been exercised, security exceptions have expired,
and cloud cost grew 48% while transaction volume grew 20%.

Lead a Well-Architected review that produces decisions and a credible improvement plan.

## Required discovery

Clarify workload boundary, customer journeys, owners, criticality, regulations,
data flows, SLO/RTO/RPO, architecture and dependencies, trust boundaries, delivery,
incidents, tests, capacity, operations, costs/unit economics, sustainability goals,
constraints, planned change, and risk authority.

## Produce these artifacts

1. **Review charter** — purpose, scope, exclusions, trigger, participants, framework/lenses, and schedule.
2. **Evidence map** — critical claim, current source, date, confidence, gap, and owner.
3. **Architecture narrative** — journeys, dependencies, failure/trust boundaries, and operational lifecycle.
4. **Cross-pillar findings** — observations, risks, controls, uncertainty, and options.
5. **Prioritized improvement plan** — containment, quick wins, foundations, strategic work, and accepted risk.
6. **Decision records** — major trade-offs, authority, residual risk, and revisit triggers.
7. **Assurance plan** — validation, review milestones, change triggers, metrics, and reporting.

## Constraints to address

- The AWS Well-Architected Tool contains answers from two years ago.
- Azure identity has different ownership and evidence access.
- The Google Cloud analytics team uses a separate risk-scoring method.
- The product leader fears review findings will delay a major launch.
- An AWS sales team proposes new services before discovery is complete.
- A low-frequency but high-impact payment-integrity risk lacks test evidence.
- The remediation budget can fund only three major initiatives this quarter.

## Strong answer outline

Define the payment journey as the workload and treat provider services as components.
Use AWS’s six pillars for depth, then apply Azure and Google Cloud guidance to their
dependencies. Establish evidence confidence; do not reuse stale answers as fact.
Express findings as business risks, consolidate duplicates, and surface uncertainty.

Prioritize integrity/security containment, recovery evidence, and safe delivery
foundations before broad optimization. Record the launch trade-off and authorized
risk decision. Put actions in product/platform roadmaps with owner, evidence, and
validation. Use milestones and change triggers, not a one-time compliance score.

## Self-scoring rubric

| Dimension | 0 | 2 | 4 |
| --- | --- | --- | --- |
| Context and scope | cloud account | rough boundary | business workload, lifecycle, owners, dependencies, exclusions |
| Evidence | claims accepted | documents collected | confidence, freshness, test/telemetry, uncertainty, access control |
| Framework application | pillar list | several questions | cross-pillar, cross-cloud, workload-specific reasoning |
| Risk and trade-offs | generic gaps | severity assigned | consequence, controls, options, authority, residual risk |
| Facilitation | interrogation | agenda and notes | safe challenge, conflicts handled, decisions and dissent captured |
| Improvement | recommendation list | owners/dates | sequenced roadmap, validation, governance, system-level learning |

Maximum: **24**. Aim for at least **19** before moving to the mock interview.

Return to the [module overview](index.md) when ready to continue.
