# Findings, Risk, and Prioritization

[← Module overview](index.md) · [Cross-cloud mapping](cloud-framework-mapping.md)

A useful finding connects evidence to a credible business consequence and an owned
decision. A generic recommendation such as “enable multi-factor authentication” is
not enough when scope, threat, affected identities, current control, and urgency are unknown.

## Finding structure

Record:

- workload, environment, component, pillar/concern, and observation date;
- factual condition and evidence source;
- uncertainty or assumption requiring validation;
- threat or failure scenario and plausible cause;
- customer, safety, security, compliance, financial, or operational consequence;
- existing preventive, detective, and recovery controls;
- likelihood/exposure, impact, urgency, and confidence;
- recommended outcome and options, not only a preferred product;
- owner, decision authority, target date, dependencies, and validation evidence.

Keep **observation**, **risk**, **recommendation**, and **decision** separate. This
prevents a framework preference from being presented as proven business risk.

## Prioritization

Use an agreed model rather than multiplying arbitrary numbers. Consider consequence,
exposure, exploitability or failure likelihood, detection/recovery capability,
regulatory deadline, customer commitments, change window, remediation effort,
dependencies, reversibility, and confidence. Highlight low-confidence/high-impact
items for rapid investigation.

Sequence foundational controls—ownership, identity, observability, backup, delivery,
and quotas—when they unlock multiple findings. Separate immediate containment,
near-term remediation, strategic redesign, and accepted residual risk.

## Severity discipline

Provider labels such as high-risk issue are useful inputs, not universal enterprise
severity. Calibrate against the workload’s criticality and threat/failure model.
Avoid downgrading a risk solely because remediation is difficult, and avoid inflating
severity to force priority.

## Exceptions and acceptance

A valid exception names the unmet expectation, business reason, scope, compensating
controls, residual risk, accountable acceptor, expiry/review date, and trigger for
reassessment. Reviewers advise; the authorized business or risk owner accepts.

## Quality check

A person outside the review should understand what is true, why it matters, which
evidence supports it, what remains uncertain, what choice is recommended, who decides,
and how closure will be proven. If not, rewrite the finding before publishing it.

Return to the [module overview](index.md) when ready to continue.
