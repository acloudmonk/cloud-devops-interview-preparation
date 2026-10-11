# Azure Architecture

[← Curriculum overview](../curriculum/index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-11**
Level: **Senior / Architect**

Azure architecture starts with workload outcomes, required qualities, and operating
responsibilities, then selects tenants, management groups, subscriptions, Regions,
services, boundaries, and controls. Strong designs explain Azure Resource Manager
scope, service semantics, quotas, dependencies, failure, recovery, evidence, and cost.

!!! tip "Where to start"
    Start with **1. Azure architecture decision model** and follow the numbered path.
    Module 01 supplies provider-neutral foundations; this module applies them to Azure.
    It is documentation and interview practice, so no deployment lab is required.

## Learning objectives

- translate outcomes and nonfunctional requirements into Azure decisions;
- reason about geographies, Regions, Availability Zones, and service scopes;
- design management-group, subscription, landing-zone, and governance boundaries;
- combine Microsoft Entra, Azure RBAC, Policy, keys, posture, detection, and response;
- select network, edge, hybrid, compute, container, serverless, and app platforms;
- choose storage, database, analytics, API, messaging, event, and workflow services;
- engineer resilience, observability, operations, backup, and disaster recovery;
- manage quotas, capacity, allocation, unit economics, and sustainability;
- apply Cloud Adoption Framework and Azure Well-Architected at the correct scopes;
- present Azure decisions with alternatives, evidence, trade-offs, and exit triggers.

## Recommended module path

### Phase 1 — Learn Azure architecture

| Step | Page | Outcome |
| ---: | --- | --- |
| 1 | [Azure architecture decision model](concepts.md) | Derive a design from outcomes, workload, and evidence |
| 2 | [Global infrastructure and service scope](global-infrastructure.md) | Place workloads across geographies, Regions, zones, and edge |
| 3 | [Management groups, landing zones, and governance](governance-landing-zones.md) | Design hierarchy, subscription, policy, and ownership boundaries |
| 4 | [Enterprise platform and shared services](enterprise-platform.md) | Deliver governed subscriptions, automation, and shared capabilities |
| 5 | [Identity, security, and data protection](identity-security.md) | Build layered preventive, detective, and responsive controls |
| 6 | [Networking, hybrid connectivity, and edge](networking-edge.md) | Design routing, DNS, ingress, egress, and private connectivity |
| 7 | [Compute, containers, serverless, and app platforms](compute-platforms.md) | Select runtime patterns from workload and operating constraints |
| 8 | [Storage, databases, and analytics](data-platforms.md) | Select authoritative and derived data services deliberately |
| 9 | [APIs, messaging, events, and workflows](integration-services.md) | Control coupling, delivery, ordering, and failure handling |
| 10 | [Azure service-selection matrices](service-selection.md) | Compare capabilities without reducing decisions to product lists |
| 11 | [Reliability, observability, and operations](reliability-operations.md) | Operate and recover Azure workloads with measurable evidence |
| 12 | [Cost, capacity, quotas, and sustainability](cost-capacity.md) | Govern economics and finite platform capacity |
| 13 | [Azure Well-Architected review](well-architected.md) | Review five pillars and convert findings into owned improvement |

### Phase 2 — Apply the reasoning

| Step | Page | Outcome |
| ---: | --- | --- |
| 14 | [Enterprise Azure design exercise](design-exercise.md) | Design a regulated global digital platform on Azure |
| 15 | [Scenario questions and model answers](scenarios.md) | Practise at least 15 senior Azure architecture scenarios |
| 16 | [Advanced architecture and incident drills](scenario-drills.md) | Resolve at least 10 ambiguous Azure failures |
| 17 | [Ten-minute Azure architecture review](presentation-template.md) | Present workload, foundation, design, evidence, and trade-offs |

### Phase 3 — Revise and assess

| Step | Page | Outcome |
| ---: | --- | --- |
| 18 | [Rapid-fire revision](rapid-fire.md) | Test at least 50 concise explanations |
| 19 | [Active-recall flashcards](flashcards.md) | Revisit at least 25 weak concepts |
| 20 | [Timed Azure architecture mock interview](../mock-interviews/azure-architecture.md) | Complete a scored 50-minute assessment |
| 21 | [References and videos](references.md) | Deepen weak areas with authoritative sources |

## Scope boundary and specialist handoffs

This module owns Azure-specific platform composition, service selection, governance,
dependencies, quotas, and operational trade-offs. Continue into deeper modules for:

| Azure architecture area | Continue with |
| --- | --- |
| VNets, DNS, hybrid, TLS, and load balancing | [Cloud Networking & DNS](../07-networking/index.md) |
| Azure DevOps/GitHub delivery and release strategies | [CI/CD & Progressive Delivery](../09-cicd/index.md) |
| AKS and its ecosystem | [Kubernetes](../11-kubernetes/index.md) and [Kubernetes Ecosystem](../12-kubernetes-ecosystem/index.md) |
| Bicep alternatives and infrastructure delivery | [Terraform/OpenTofu & IaC](../13-terraform/index.md) |
| Supply chain and Zero Trust | [DevSecOps](../15-devsecops/index.md) and [Zero Trust](../16-zero-trust/index.md) |
| Azure Monitor and reliability management | [Observability](../17-observability/index.md) and [SRE](../18-sre/index.md) |
| Application and tenant architecture | [Microservices](../20-microservices/index.md) and [SaaS](../21-saas/index.md) |
| Events and database internals | [Event-Driven Architecture](../22-event-driven/index.md) and [Database Architecture](../23-databases/index.md) |
| Migration and enterprise recovery | [Migration & Modernization](../24-migration-modernization/index.md) and [HA/DR](../25-ha-dr-bcp/index.md) |
| Economics and formal cross-cloud review | [FinOps](../26-finops/index.md) and [Well-Architected Reviews](../27-well-architected/index.md) |
| Hybrid/multi-cloud and enterprise APIs | [Hybrid & Multi-Cloud](../28-hybrid-multicloud/index.md) and [APIs & Identity](../29-api-identity/index.md) |

## Completion checklist

- [ ] I can justify tenant, management-group, subscription, Region, and network boundaries.
- [ ] I can distinguish Azure resource scope, control plane, data plane, and dependencies.
- [ ] I can explain Entra roles, Azure RBAC, Policy, managed identities, and PIM.
- [ ] I can select Azure compute, data, integration, and edge services from requirements.
- [ ] I can design degradation, recovery, observability, and incident access.
- [ ] I can model quotas, cost allocation, demand, commitments, and unit economics.
- [ ] I can apply landing-zone and workload-review guidance at the correct scope.
- [ ] I answered every scenario aloud and completed the scored mock interview.
