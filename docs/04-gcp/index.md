# GCP Architecture

[← Curriculum overview](../curriculum/index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-11**

Level: **Senior / Architect**

Google Cloud architecture starts with outcomes and operating constraints, then chooses
resource, identity, network, regional, service, and data boundaries. Strong answers
explain service scope, dependencies, quotas, failure, recovery, evidence, and cost—not
only product names.

!!! tip "Where to start"
    Start with **1. GCP architecture decision model** and follow the numbered path.
    Module 01 supplies provider-neutral foundations. No deployment lab is required.

## Learning objectives

- translate requirements into defensible Google Cloud decisions;
- design organization, folder, project, billing, policy, and ownership boundaries;
- reason about global, regional, zonal, and multi-regional resources;
- select identity, network, compute, data, integration, and edge services;
- engineer reliability, observability, recovery, capacity, cost, and sustainability;
- apply the Google Cloud Well-Architected Framework and present trade-offs.

## Recommended module path

### Phase 1 — Learn GCP architecture

| Step | Page | Outcome |
| ---: | --- | --- |
| 1 | [GCP architecture decision model](concepts.md) | Derive designs from outcomes and evidence |
| 2 | [Global infrastructure and service scope](global-infrastructure.md) | Place resources deliberately |
| 3 | [Resource hierarchy and governance](resource-hierarchy-governance.md) | Design organizations, folders, projects, and guardrails |
| 4 | [Enterprise platform and shared services](enterprise-platform.md) | Build a governed cloud foundation |
| 5 | [Identity, security, and data protection](identity-security.md) | Layer preventive, detective, and responsive controls |
| 6 | [Networking, hybrid connectivity, and edge](networking-edge.md) | Design routing, DNS, ingress, egress, and private access |
| 7 | [Compute, containers, serverless, and app platforms](compute-platforms.md) | Select a runtime deliberately |
| 8 | [Storage, databases, and analytics](data-platforms.md) | Match data semantics to services |
| 9 | [APIs, messaging, events, and workflows](integration-services.md) | Control coupling and delivery failure |
| 10 | [GCP service-selection matrices](service-selection.md) | Compare capabilities and constraints |
| 11 | [Reliability, observability, and operations](reliability-operations.md) | Operate and recover with evidence |
| 12 | [Cost, capacity, quotas, and sustainability](cost-capacity.md) | Govern economics and finite capacity |
| 13 | [Google Cloud Well-Architected review](well-architected.md) | Review six pillars and perspectives |

### Phase 2 — Apply the reasoning

| Step | Page | Outcome |
| ---: | --- | --- |
| 14 | [Enterprise GCP design exercise](design-exercise.md) | Design a regulated global platform |
| 15 | [Scenario questions and model answers](scenarios.md) | Practise at least 15 senior scenarios |
| 16 | [Advanced architecture and incident drills](scenario-drills.md) | Resolve at least 10 ambiguous failures |
| 17 | [Ten-minute GCP architecture review](presentation-template.md) | Present decisions and trade-offs |

### Phase 3 — Revise and assess

| Step | Page | Outcome |
| ---: | --- | --- |
| 18 | [Rapid-fire revision](rapid-fire.md) | Test at least 50 explanations |
| 19 | [Active-recall flashcards](flashcards.md) | Revisit at least 25 concepts |
| 20 | [Timed GCP architecture mock interview](../mock-interviews/gcp-architecture.md) | Complete a scored 50-minute assessment |
| 21 | [References and videos](references.md) | Deepen weak areas with primary sources |

## Specialist handoffs

Continue with [Networking](../07-networking/index.md), [Kubernetes](../11-kubernetes/index.md),
[Terraform/OpenTofu](../13-terraform/index.md), [Observability](../17-observability/index.md),
[SRE](../18-sre/index.md), [FinOps](../26-finops/index.md), or
[Well-Architected Reviews](../27-well-architected/index.md) for deeper treatment.

## Completion checklist

- [ ] I can justify organization, folder, project, Region, and network boundaries.
- [ ] I distinguish IAM, deny policies, and Organization Policy.
- [ ] I can select GCP compute, data, integration, and edge services from requirements.
- [ ] I can design degradation, recovery, observability, and emergency access.
- [ ] I can model quotas, cost allocation, commitments, and unit economics.
- [ ] I answered every scenario aloud and completed the scored mock.
