# High Availability, Disaster Recovery & Business Continuity

[← Curriculum overview](../curriculum/index.md) ·
[Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-11**
Level: **Senior / Architect**

High availability (HA), disaster recovery (DR), and business continuity (BC)
solve related but different problems. HA keeps an acceptable service running
through expected component failures. DR restores an acceptable service after a
declared disruption. Business continuity keeps critical business outcomes,
people, suppliers, facilities, communications, and technology operating while
normal conditions are unavailable.

!!! tip "Where to start"
    Start with **1. Continuity decision model** and follow the numbered path.
    AWS is the primary design context; Azure and Google Cloud equivalents are
    compared explicitly. Exercises are architecture and interview practice—no
    executable lab or cloud deployment is required.

## Learning objectives

By the end of this module, you should be able to:

- translate business impact into recovery tiers, RTO, RPO, MTPD, and service levels;
- distinguish resilience, HA, backup, DR, crisis management, and continuity;
- design for component, Availability Zone, Region, identity, and control-plane failure;
- select backup/restore, pilot light, warm standby, or multi-site deliberately;
- protect data against infrastructure loss, corruption, deletion, and ransomware;
- explain consistency, replication lag, failover, failback, and split-brain risks;
- create executable recovery runbooks with authority and communication paths;
- test technical recovery and business continuity without creating uncontrolled risk;
- compare AWS designs with Azure and Google Cloud capabilities and terminology.

## Recommended module path

### Phase 1 — Learn the continuity decision system

| Step | Page | Outcome |
| ---: | --- | --- |
| 1 | [Continuity decision model](concepts.md) | Separate HA, DR, backup, and business continuity decisions |
| 2 | [Business impact and recovery objectives](objectives-bia.md) | Convert business consequences into recovery tiers and measurable objectives |
| 3 | [HA and failure-domain architecture](ha-failure-domains.md) | Contain routine failures across compute, network, data, and dependencies |
| 4 | [Disaster-recovery strategies](dr-strategies.md) | Choose a recovery pattern that matches objectives and economics |
| 5 | [Data protection and recoverability](data-protection-recovery.md) | Design immutable, isolated, restorable, and validated data protection |
| 6 | [Multi-Region traffic, failover, and failback](multi-region-failover.md) | Coordinate routing, state, dependencies, and return to normal service |
| 7 | [Business continuity and crisis management](business-continuity.md) | Sustain priority business services beyond the technology recovery plan |
| 8 | [Runbooks, exercises, and governance](testing-governance.md) | Prove recovery capability and govern exceptions with evidence |
| 9 | [AWS-first multi-cloud capability map](cloud-mapping.md) | Translate architecture intent across AWS, Azure, and Google Cloud |

### Phase 2 — Apply the reasoning

| Step | Page | Outcome |
| ---: | --- | --- |
| 10 | [Enterprise continuity design exercise](design-exercise.md) | Design tiered HA/DR/BC for an AWS-first regulated platform |
| 11 | [Scenario questions and model answers](scenarios.md) | Practise 15 senior architecture scenarios |
| 12 | [Advanced recovery drills](scenario-drills.md) | Work through 10 ambiguous failure and continuity events |
| 13 | [Ten-minute continuity review](presentation-template.md) | Present objectives, architecture, activation, evidence, and residual risk |

### Phase 3 — Revise and assess

| Step | Page | Outcome |
| ---: | --- | --- |
| 14 | [Rapid-fire revision](rapid-fire.md) | Test 50 concise verbal explanations |
| 15 | [Active-recall flashcards](flashcards.md) | Revisit weak concepts with spaced repetition |
| 16 | [Timed HA/DR/BC mock interview](../mock-interviews/high-availability-disaster-recovery.md) | Complete a scored 50-minute assessment |
| 17 | [References and videos](references.md) | Deepen weak areas with primary and authoritative sources |

## Relationship to adjacent modules

[Module 18](../18-sre/index.md) defines reliability objectives, incident
response, and the operating discipline that makes recovery credible. This module
goes deeper into continuity requirements, recovery architecture, activation,
failback, and organizational survival. [Module 17](../17-observability/index.md)
provides the evidence used to detect failure and verify recovery; future cloud
provider modules will add service-level implementation depth.

## Completion checklist

- [ ] I can distinguish HA, DR, backup, and BC using business outcomes.
- [ ] I can derive defensible RTO/RPO targets from a business impact analysis.
- [ ] I can choose a DR strategy and explain cost, complexity, and residual risk.
- [ ] I can design data recovery for corruption and cyberattack, not only outages.
- [ ] I can explain failover and failback as controlled business decisions.
- [ ] I can propose exercises that prove people, process, and technology recovery.
- [ ] I answered all 25 scenarios aloud and completed the scored mock interview.
