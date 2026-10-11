# Hybrid and Multi-Cloud Architecture

[← Curriculum overview](../curriculum/index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-11**
Level: **Senior / Architect**

Hybrid architecture connects public cloud with private data centers, edge sites,
or hosted environments. Multi-cloud deliberately uses services from more than one
public cloud provider. Neither is automatically more resilient, portable, secure,
or cost-effective; each must solve a named business constraint worth its complexity.

!!! tip "Where to start"
    Start with **1. Distributed-estate decision model** and follow the numbered
    path. AWS is the anchor, with Azure, Google Cloud, on-premises, edge, and SaaS
    dependencies treated explicitly. No executable lab is required.

## Learning objectives

- distinguish hybrid, multi-cloud, distributed cloud, edge, and ordinary SaaS use;
- derive workload placement from business, data, latency, sovereignty, and operating constraints;
- design resilient routing, connectivity, DNS, IP addressing, and traffic inspection;
- federate workforce and workload identity without creating a universal blast radius;
- select data placement, replication, integration, and consistency deliberately;
- evaluate portability versus useful provider specialization;
- operate security, observability, delivery, inventory, and incidents across environments;
- design continuity without assuming provider diversity equals independence;
- govern skills, contracts, cost, egress, ownership, and exit risk.

## Recommended module path

### Phase 1 — Learn the distributed-estate system

| Step | Page | Outcome |
| ---: | --- | --- |
| 1 | [Distributed-estate decision model](concepts.md) | Connect business drivers to placement, boundaries, and operating evidence |
| 2 | [Strategy and workload placement](strategy-placement.md) | Choose environments and patterns without defaulting to multi-cloud |
| 3 | [Connectivity, routing, and DNS](connectivity-dns.md) | Build redundant, observable, non-overlapping communication paths |
| 4 | [Identity, security, and trust](identity-security.md) | Federate access while containing compromise and preserving recovery |
| 5 | [Data placement and integration](data-integration.md) | Manage gravity, sovereignty, replication, consistency, and movement |
| 6 | [Platforms, portability, and delivery](platform-portability.md) | Balance common platforms with provider-native value |
| 7 | [Operations and observability](operations-observability.md) | Establish inventory, telemetry, service ownership, and incident command |
| 8 | [Resilience and continuity](resilience-continuity.md) | Test correlated failure, degraded modes, recovery, and exit paths |
| 9 | [Governance, cost, and capability](governance-cost.md) | Control complexity, commercial exposure, skills, and lifecycle |

### Phase 2 — Apply the reasoning

| Step | Page | Outcome |
| ---: | --- | --- |
| 10 | [Enterprise hybrid/multi-cloud design exercise](design-exercise.md) | Design a regulated AWS-first distributed enterprise platform |
| 11 | [Scenario questions and model answers](scenarios.md) | Practise 15 senior architecture scenarios |
| 12 | [Advanced distributed-estate drills](scenario-drills.md) | Work through 10 ambiguous cross-environment failures |
| 13 | [Ten-minute strategy review](presentation-template.md) | Present drivers, placement, architecture, operations, and residual risk |

### Phase 3 — Revise and assess

| Step | Page | Outcome |
| ---: | --- | --- |
| 14 | [Rapid-fire revision](rapid-fire.md) | Test 50 concise explanations |
| 15 | [Active-recall flashcards](flashcards.md) | Revisit weak concepts with spaced repetition |
| 16 | [Timed hybrid/multi-cloud mock interview](../mock-interviews/hybrid-multicloud.md) | Complete a scored 50-minute assessment |
| 17 | [References and videos](references.md) | Deepen weak areas with primary sources |

## Relationship to adjacent modules

[Networking](../07-networking/index.md), [Zero Trust](../16-zero-trust/index.md),
[Observability](../17-observability/index.md), [HA/DR](../25-ha-dr-bcp/index.md),
[FinOps](../26-finops/index.md), and [Well-Architected reviews](../27-well-architected/index.md)
provide specialist depth used here. This module joins them into one distributed
operating model rather than repeating their full content.

## Completion checklist

- [ ] I can justify each environment with a durable business driver.
- [ ] I can describe end-to-end identity, network, DNS, data, and failure boundaries.
- [ ] I can separate portability goals from platform standardization.
- [ ] I can quantify egress, duplicated capability, operational, and exit costs.
- [ ] I can design and test correlated-failure and provider-loss scenarios.
- [ ] I answered all 25 scenarios aloud and completed the scored mock interview.
