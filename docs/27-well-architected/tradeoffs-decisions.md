# Trade-offs and Architecture Decisions

[← Module overview](index.md) · [Risk and prioritization](risk-prioritization.md)

Well-Architected does not mean maximizing every quality attribute. It means making
conscious, evidence-based choices that meet business objectives and remain operable.

## Trade-off method

1. State the business outcome and quality attributes with measurable priorities.
2. Identify constraints, threats, failure assumptions, demand, and lifecycle horizon.
3. Present viable options including “defer” and “change the requirement.”
4. Compare effects across operations, security, reliability, performance, cost, and sustainability.
5. Identify uncertainty, reversibility, migration cost, and organizational capability.
6. Select an option with the authorized owner and record residual risk.
7. Define signals, validation, expiry, and triggers to revisit the decision.

## Common cross-pillar tensions

| Decision | Potential benefit | Potential cost or risk |
| --- | --- | --- |
| Multi-Region active-active | lower interruption and geographic reach | consistency, attack surface, operations, spend, energy |
| Aggressive rightsizing | lower spend and waste | reduced burst/failure headroom |
| Stronger encryption/isolation | confidentiality and blast-radius control | latency, key dependency, operational complexity |
| High-cardinality telemetry | deeper diagnosis and product insight | ingestion cost, privacy, operational load |
| Rapid deployment | feedback and recovery through small change | unsafe change if tests, observability, or rollback lag |
| Managed service | reduced undifferentiated operation | lock-in, limits, price, control, dependency |

## Architecture decision record

Capture context, decision drivers, considered options, decision, status, consequences,
risks, evidence, owner, date, and revisit triggers. Link findings and remediation to
the ADR so future reviewers understand why a non-default design exists.

Avoid retrospective ADRs that rewrite history. If rationale is unknown, record the
current hypothesis and validate it with owners or operational evidence.

## Reversibility

Prefer experiments and reversible changes when uncertainty is high. For hard-to-reverse
choices—data model, identity boundary, Region, contract, multi-cloud topology—invest
more in discovery, prototypes, failure tests, migration/exit plans, and explicit approval.

## Decision quality

The chosen option need not match a framework default if constraints justify it.
Quality comes from accurate context, viable alternatives, transparent consequences,
proper authority, and evidence that the result meets its objectives.

Return to the [module overview](index.md) when ready to continue.
