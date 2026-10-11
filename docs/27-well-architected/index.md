# Cross-Cloud Well-Architected Reviews

[← Curriculum overview](../curriculum/index.md) ·
[Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-11**
Level: **Senior / Architect**

A Well-Architected review is a structured conversation about workload outcomes,
design choices, operating evidence, risks, and improvements. It is not an audit,
a certification, a product recommendation exercise, or a competition for the
highest framework score.

!!! tip "Where to start"
    Start with **1. Architecture-review decision model** and follow the numbered
    path. AWS is the primary review context; Azure and Google Cloud are mapped by
    intent and current pillar structure. No executable lab or cloud deployment is
    required.

## Learning objectives

By the end of this module, you should be able to:

- define a workload, review scope, lifecycle trigger, stakeholders, and success outcome;
- prepare discovery and evidence without turning the review into a document request;
- apply AWS Well-Architected pillars, lenses, and the AWS Well-Architected Tool;
- translate review intent across Azure and Google Cloud frameworks;
- distinguish observed fact, assumption, recommendation, risk, and accepted exception;
- prioritize findings by business impact, likelihood, urgency, effort, and dependency;
- facilitate constructive reviews and challenge unsupported claims safely;
- document cross-pillar trade-offs and architecture decisions;
- turn findings into owned remediation, validation, and continuous review.

## Recommended module path

### Phase 1 — Learn the review operating system

| Step | Page | Outcome |
| ---: | --- | --- |
| 1 | [Architecture-review decision model](concepts.md) | Connect business outcomes, architecture, evidence, risk, and improvement |
| 2 | [Scope, discovery, and evidence](scope-evidence.md) | Prepare a workload review with the right people and trustworthy inputs |
| 3 | [AWS Well-Architected pillars and lenses](aws-framework.md) | Apply the six pillars without reducing them to service checklists |
| 4 | [Azure and Google Cloud framework mapping](cloud-framework-mapping.md) | Translate intent while preserving provider-specific differences |
| 5 | [Findings, risk, and prioritization](risk-prioritization.md) | Produce defensible, actionable findings and a sequenced risk view |
| 6 | [Trade-offs and architecture decisions](tradeoffs-decisions.md) | Make cross-pillar choices explicit and reversible where possible |
| 7 | [Facilitation and stakeholder communication](facilitation.md) | Run psychologically safe, decision-oriented review sessions |
| 8 | [Remediation and continuous governance](remediation-governance.md) | Convert review output into validated change and recurring assurance |
| 9 | [Review tools, automation, and metrics](tools-automation.md) | Use provider tools and evidence automation without score gaming |

### Phase 2 — Apply the reasoning

| Step | Page | Outcome |
| ---: | --- | --- |
| 10 | [Enterprise review design exercise](design-exercise.md) | Review an AWS-first regulated workload with multi-cloud dependencies |
| 11 | [Scenario questions and model answers](scenarios.md) | Practise 15 senior architecture-review scenarios |
| 12 | [Advanced review-room drills](scenario-drills.md) | Handle 10 ambiguous evidence, risk, and stakeholder situations |
| 13 | [Ten-minute executive review](presentation-template.md) | Present context, top risks, trade-offs, roadmap, and decisions |

### Phase 3 — Revise and assess

| Step | Page | Outcome |
| ---: | --- | --- |
| 14 | [Rapid-fire revision](rapid-fire.md) | Test 50 concise verbal explanations |
| 15 | [Active-recall flashcards](flashcards.md) | Revisit weak concepts with spaced repetition |
| 16 | [Timed Well-Architected mock interview](../mock-interviews/well-architected-review.md) | Complete a scored 50-minute assessment |
| 17 | [References and videos](references.md) | Deepen weak areas with primary and authoritative sources |

## Relationship to adjacent modules

This module integrates decisions from [Cloud Architecture](../01-cloud-architecture/index.md),
[Zero Trust](../16-zero-trust/index.md), [Observability](../17-observability/index.md),
[SRE](../18-sre/index.md), [HA/DR/BC](../25-ha-dr-bcp/index.md), and
[FinOps](../26-finops/index.md). It teaches how to review those capabilities as
one workload system. Future provider modules add deeper service implementation;
the review method remains outcome- and evidence-driven.

## Completion checklist

- [ ] I can define a reviewable workload and exclude irrelevant scope.
- [ ] I can ask evidence-seeking questions without making the session adversarial.
- [ ] I can compare AWS, Azure, and Google Cloud frameworks accurately.
- [ ] I can express risk and trade-offs without hiding behind a score.
- [ ] I can produce an owned, sequenced, and measurable improvement plan.
- [ ] I can explain when a recommendation should be deferred or accepted as risk.
- [ ] I answered all 25 scenarios aloud and completed the scored mock interview.
