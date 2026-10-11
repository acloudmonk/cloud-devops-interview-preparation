# Site Reliability Engineering

[← Curriculum overview](../curriculum/index.md) ·
[Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-11**
Level: **Senior / Architect**

Site Reliability Engineering applies software-engineering methods to operations
so services can meet explicit reliability objectives at sustainable cost. SRE is
not a renamed operations team, a universal 99.99% target, or an expectation that
humans compensate indefinitely for unsafe architecture and change.

!!! tip "Where to start"
    Start with **1. SRE decision model** and follow the numbered path. AWS is the
    primary cloud context; Azure and Google Cloud are translated where controls
    differ. No executable lab or cloud deployment is required.

## Learning objectives

By the end of this module, you should be able to:

- connect user outcomes, reliability risk, SLOs, engineering work, and learning;
- define meaningful SLIs/SLOs and operate a credible error-budget policy;
- reason about availability mathematics, dependencies, redundancy, and recovery;
- establish incident command, technical response, communication, and handover;
- run blameless postmortems with owned, prioritized corrective work;
- distinguish toil from valuable operations and automate safely;
- forecast capacity and engineer performance before saturation;
- reduce change risk through progressive delivery and tested rollback;
- design fault injection, game days, and chaos experiments with safeguards;
- build sustainable on-call and choose an appropriate SRE engagement model.

## Recommended module path

### Phase 1 — Learn the reliability operating system

| Step | Page | Outcome |
| ---: | --- | --- |
| 1 | [SRE decision model](concepts.md) | Connect service outcomes, objectives, operations, engineering, and learning |
| 2 | [SLIs, SLOs, and error-budget governance](slos-error-budgets.md) | Turn user expectations into owned reliability policy |
| 3 | [Reliability architecture and risk](reliability-architecture.md) | Reason about dependencies, failure domains, recovery, and cloud controls |
| 4 | [Incident response and communication](incidents-response.md) | Establish command, stabilize service, and communicate under uncertainty |
| 5 | [Postmortems and organizational learning](postmortems-learning.md) | Convert incidents into prioritized system improvement |
| 6 | [Toil, automation, and operational engineering](toil-automation.md) | Reduce repetitive work without automating unsafe ambiguity |
| 7 | [Capacity and performance engineering](capacity-performance.md) | Forecast demand, model bottlenecks, and protect headroom |
| 8 | [Safe change and resilience testing](safe-change-resilience.md) | Control release risk and validate recovery with experiments |
| 9 | [On-call and SRE organization](organization-oncall.md) | Design sustainable ownership, readiness, and engagement models |

### Phase 2 — Apply the reasoning

| Step | Page | Outcome |
| ---: | --- | --- |
| 10 | [Enterprise SRE design exercise](design-exercise.md) | Build a reliability operating model for an AWS-first platform |
| 11 | [Scenario questions and model answers](scenarios.md) | Practise 15 senior SRE scenarios |
| 12 | [Advanced incident drills](scenario-drills.md) | Handle 10 ambiguous production and organizational failures |
| 13 | [Ten-minute reliability review](presentation-template.md) | Present objectives, risks, architecture, operations, and investment |

### Phase 3 — Revise and assess

| Step | Page | Outcome |
| ---: | --- | --- |
| 14 | [Rapid-fire revision](rapid-fire.md) | Test 50 concise verbal explanations |
| 15 | [Active-recall flashcards](flashcards.md) | Revisit weak concepts with spaced repetition |
| 16 | [Timed SRE mock interview](../mock-interviews/site-reliability-engineering.md) | Complete a scored 50-minute assessment |
| 17 | [References and videos](references.md) | Deepen weak areas with primary sources |

## Relationship to adjacent modules

[Module 17](../17-observability/index.md) covers telemetry, Prometheus, Grafana,
OpenTelemetry, and alert design. This module uses that evidence to govern service
reliability and human response. Detailed high availability, disaster recovery,
and business continuity remain planned for [Module 25](../25-ha-dr-bcp/index.md);
this module covers the operating practices that make those designs trustworthy.

## Completion checklist

- [ ] I can negotiate reliability rather than choosing an arbitrary percentage.
- [ ] I can explain error-budget policy without using it as punishment.
- [ ] I can lead incident response and communicate uncertainty clearly.
- [ ] I can write a systems-focused postmortem with effective actions.
- [ ] I can identify toil and automate with rollback and ownership.
- [ ] I can design capacity, change, and resilience-testing controls.
- [ ] I answered all 25 scenarios aloud and completed the scored mock interview.
