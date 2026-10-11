# AWS Architecture

[← Curriculum overview](../curriculum/index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-11**
Level: **Senior / Architect**

AWS architecture starts with workload outcomes and required qualities, then selects
accounts, Regions, services, boundaries, controls, and operating responsibilities.
Strong designs explain service semantics, quotas, dependencies, failure behavior,
recovery, security evidence, delivery, and cost—not merely product names.

!!! tip "Where to start"
    Start with **1. AWS architecture decision model** and follow the numbered path.
    Module 01 supplies provider-neutral foundations; this module applies them to AWS.
    It is documentation and interview practice, so no deployment lab is required.

## Learning objectives

- translate outcomes and nonfunctional requirements into AWS design decisions;
- reason about Regions, Availability Zones, edge locations, and service scopes;
- design an AWS multi-account environment and governed landing zone;
- combine IAM, Organizations policies, encryption, detection, and response;
- select network, edge, hybrid, compute, container, and serverless patterns;
- choose storage, database, analytics, API, messaging, and workflow capabilities;
- engineer resilience, observability, operability, backup, and disaster recovery;
- manage quotas, capacity, cost allocation, unit economics, and sustainability;
- identify shared-responsibility boundaries and hidden service dependencies;
- present AWS decisions with alternatives, trade-offs, evidence, and exit triggers.

## Recommended module path

### Phase 1 — Learn AWS architecture

| Step | Page | Outcome |
| ---: | --- | --- |
| 1 | [AWS architecture decision model](concepts.md) | Derive a design from outcomes, workload, and evidence |
| 2 | [Global infrastructure and service scope](global-infrastructure.md) | Place workloads across Regions, AZs, and edge locations |
| 3 | [Organizations, landing zones, and governance](multi-account-governance.md) | Design account boundaries, guardrails, and platform ownership |
| 4 | [Identity, security, and data protection](identity-security.md) | Build layered preventive, detective, and responsive controls |
| 5 | [Networking, hybrid connectivity, and edge](networking-edge.md) | Design routing, DNS, ingress, egress, and private connectivity |
| 6 | [Compute, containers, and serverless](compute-platforms.md) | Select runtime patterns from workload and operating constraints |
| 7 | [Storage, databases, and analytics](data-platforms.md) | Select authoritative and derived data services deliberately |
| 8 | [APIs, messaging, events, and workflows](integration-services.md) | Control coupling, delivery, ordering, and failure handling |
| 9 | [Reliability, observability, and operations](reliability-operations.md) | Operate and recover AWS workloads with measurable evidence |
| 10 | [Cost, capacity, quotas, and sustainability](cost-capacity.md) | Govern economics and finite service capacity |

### Phase 2 — Apply the reasoning

| Step | Page | Outcome |
| ---: | --- | --- |
| 11 | [Enterprise AWS design exercise](design-exercise.md) | Design a regulated global digital platform on AWS |
| 12 | [Scenario questions and model answers](scenarios.md) | Practise at least 15 senior AWS architecture scenarios |
| 13 | [Advanced architecture and incident drills](scenario-drills.md) | Resolve at least 10 ambiguous AWS failures |
| 14 | [Ten-minute AWS architecture review](presentation-template.md) | Present workload, foundation, design, evidence, and trade-offs |

### Phase 3 — Revise and assess

| Step | Page | Outcome |
| ---: | --- | --- |
| 15 | [Rapid-fire revision](rapid-fire.md) | Test at least 50 concise explanations |
| 16 | [Active-recall flashcards](flashcards.md) | Revisit at least 25 weak concepts |
| 17 | [Timed AWS architecture mock interview](../mock-interviews/aws-architecture.md) | Complete a scored 50-minute assessment |
| 18 | [References and videos](references.md) | Deepen weak areas with authoritative sources |

## Scope boundary

[Module 01](../01-cloud-architecture/index.md) owns provider-neutral architecture;
Networking, Kubernetes, Databases, Security, SRE, HA/DR, FinOps, and Migration provide
deeper specialist coverage. This module owns AWS-specific platform composition,
service selection, governance, dependencies, quotas, and operational trade-offs.

## Completion checklist

- [ ] I can justify Region, account, network, identity, and runtime boundaries.
- [ ] I can distinguish AWS service scope, control plane, data plane, and dependencies.
- [ ] I can explain SCPs, IAM policies, resource policies, and permission boundaries.
- [ ] I can select AWS compute, data, and integration services from requirements.
- [ ] I can design degradation, backup, recovery, observability, and incident access.
- [ ] I can model quotas, cost allocation, demand, commitments, and unit economics.
- [ ] I can identify evidence that would change my AWS architecture decision.
- [ ] I answered every scenario aloud and completed the scored mock interview.
