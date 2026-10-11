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
| 4 | [Enterprise platform and shared services](enterprise-platform.md) | Deliver governed accounts, products, automation, and shared capabilities |
| 5 | [Identity, security, and data protection](identity-security.md) | Build layered preventive, detective, and responsive controls |
| 6 | [Networking, hybrid connectivity, and edge](networking-edge.md) | Design routing, DNS, ingress, egress, and private connectivity |
| 7 | [Compute, containers, and serverless](compute-platforms.md) | Select runtime patterns from workload and operating constraints |
| 8 | [Storage, databases, and analytics](data-platforms.md) | Select authoritative and derived data services deliberately |
| 9 | [APIs, messaging, events, and workflows](integration-services.md) | Control coupling, delivery, ordering, and failure handling |
| 10 | [AWS service-selection matrices](service-selection.md) | Compare capabilities without reducing decisions to product lists |
| 11 | [Reliability, observability, and operations](reliability-operations.md) | Operate and recover AWS workloads with measurable evidence |
| 12 | [Cost, capacity, quotas, and sustainability](cost-capacity.md) | Govern economics and finite service capacity |
| 13 | [AWS Well-Architected review](well-architected.md) | Review all six pillars and convert findings into owned improvement |

### Phase 2 — Apply the reasoning

| Step | Page | Outcome |
| ---: | --- | --- |
| 14 | [Enterprise AWS design exercise](design-exercise.md) | Design a regulated global digital platform on AWS |
| 15 | [Scenario questions and model answers](scenarios.md) | Practise at least 15 senior AWS architecture scenarios |
| 16 | [Advanced architecture and incident drills](scenario-drills.md) | Resolve at least 10 ambiguous AWS failures |
| 17 | [Ten-minute AWS architecture review](presentation-template.md) | Present workload, foundation, design, evidence, and trade-offs |

### Phase 3 — Revise and assess

| Step | Page | Outcome |
| ---: | --- | --- |
| 18 | [Rapid-fire revision](rapid-fire.md) | Test at least 50 concise explanations |
| 19 | [Active-recall flashcards](flashcards.md) | Revisit at least 25 weak concepts |
| 20 | [Timed AWS architecture mock interview](../mock-interviews/aws-architecture.md) | Complete a scored 50-minute assessment |
| 21 | [References and videos](references.md) | Deepen weak areas with authoritative sources |

## Scope boundary

[Module 01](../01-cloud-architecture/index.md) owns provider-neutral architecture;
This module owns AWS-specific platform composition, service selection, governance,
dependencies, quotas, and operational trade-offs. Continue into the specialist module
when a decision requires implementation or domain depth:

| AWS architecture area | Continue with |
| --- | --- |
| VPC, DNS, hybrid, TLS, load balancing | [Cloud Networking & DNS](../07-networking/index.md) |
| Delivery pipelines and release strategies | [CI/CD & Progressive Delivery](../09-cicd/index.md) |
| EKS and its ecosystem | [Kubernetes](../11-kubernetes/index.md) and [Kubernetes Ecosystem](../12-kubernetes-ecosystem/index.md) |
| CloudFormation alternatives and infrastructure delivery | [Terraform/OpenTofu & IaC](../13-terraform/index.md) |
| Supply chain and Zero Trust | [DevSecOps](../15-devsecops/index.md) and [Zero Trust](../16-zero-trust/index.md) |
| Telemetry and reliability management | [Observability](../17-observability/index.md) and [SRE](../18-sre/index.md) |
| Application and tenant architecture | [Microservices](../20-microservices/index.md) and [SaaS](../21-saas/index.md) |
| Events and database internals | [Event-Driven Architecture](../22-event-driven/index.md) and [Database Architecture](../23-databases/index.md) |
| Migration and enterprise recovery | [Migration & Modernization](../24-migration-modernization/index.md) and [HA/DR](../25-ha-dr-bcp/index.md) |
| Economics and formal architecture review | [FinOps](../26-finops/index.md) and [Well-Architected Reviews](../27-well-architected/index.md) |
| Hybrid/multi-cloud and enterprise APIs | [Hybrid & Multi-Cloud](../28-hybrid-multicloud/index.md) and [APIs & Identity](../29-api-identity/index.md) |

## Completion checklist

- [ ] I can justify Region, account, network, identity, and runtime boundaries.
- [ ] I can distinguish AWS service scope, control plane, data plane, and dependencies.
- [ ] I can explain SCPs, IAM policies, resource policies, and permission boundaries.
- [ ] I can select AWS compute, data, and integration services from requirements.
- [ ] I can design degradation, backup, recovery, observability, and incident access.
- [ ] I can model quotas, cost allocation, demand, commitments, and unit economics.
- [ ] I can identify evidence that would change my AWS architecture decision.
- [ ] I answered every scenario aloud and completed the scored mock interview.
