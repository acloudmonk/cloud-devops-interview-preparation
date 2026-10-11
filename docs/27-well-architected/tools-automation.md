# Review Tools, Automation, and Metrics

[← Module overview](index.md) · [Remediation governance](remediation-governance.md)

Tools can improve consistency, evidence freshness, traceability, and scale. They cannot
infer every business objective, user journey, threat, failure behavior, trade-off, or
organizational constraint.

## Tool roles

- AWS Well-Architected Tool records workloads, lenses, answers, improvement items, and milestones.
- Azure Well-Architected Review supplies pillar-aligned assessment questions and guidance.
- Google Cloud Well-Architected guidance and perspectives support structured review and provider-specific recommendations.
- Provider advisors, configuration services, security posture tools, cost tools, and observability systems supply evidence inputs.
- Architecture repositories, ADRs, risk systems, and delivery trackers preserve decisions and action ownership.

Confirm current product capabilities and access models; framework documentation changes
more quickly than static training material.

## Evidence automation

Automate facts that are deterministic and authorized: inventory, ownership metadata,
encryption settings, public exposure, backup policy, multi-zone placement, quotas,
logging, deployment metrics, cost allocation, and policy conformance. Store query time,
scope, environment, tool version, and raw evidence reference.

Avoid copying secrets, customer data, vulnerability detail, or unrestricted diagrams
into broad review reports. Grant least privilege and define retention and deletion.

## Human decision boundary

Automation can say that a setting differs from policy. A person must decide whether the
policy applies, which business risk exists, what trade-off is appropriate, and who accepts
residual risk. Auto-remediation requires production-grade authorization, testing, scope,
rollback, audit, and quality guardrails.

## Metrics that help

- percentage of critical workloads with current, evidence-backed reviews;
- review lead time and stakeholder participation;
- age and exposure of material findings and exceptions;
- remediation cycle time and validation completion;
- recurring finding themes removed through platform or policy improvements;
- incidents, SLOs, recovery, security, delivery, cost, and sustainability outcomes tied to changes.

## Metrics that mislead

Raw review count rewards shallow coverage. Questionnaire completion rewards certainty.
Pillar score comparison ignores context. Closed-ticket count ignores risk reduction.
Estimated savings ignores implementation and quality. Use such measures only with scope,
confidence, and outcome evidence.

## Version awareness

Record framework/lens/assessment version or review date. When official guidance changes,
triage whether it affects current risk rather than mechanically reopening every answer.

Return to the [module overview](index.md) when ready to continue.
