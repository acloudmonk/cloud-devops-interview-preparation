# Platform Engineering and Internal Developer Platforms

[← Curriculum overview](../curriculum/index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-11**
Level: **Senior / Architect**

Platform engineering applies product thinking to reusable capabilities that help
teams deliver and operate software safely with less cognitive load. An internal
developer platform is not merely a portal, Kubernetes cluster, or central ticket
queue; it is a supported product of interfaces, workflows, controls, and services.

!!! tip "Where to start"
    Start with **1. Platform engineering decision model** and follow the numbered
    path. AWS is the architecture anchor with Azure and Google Cloud translations.
    No executable lab or cloud deployment is required.

## Learning objectives

- decide when a platform product is justified and which problems it should not own;
- discover developer journeys, cognitive load, constraints, and measurable outcomes;
- design platform layers, APIs, control planes, portals, catalogs, and golden paths;
- provide self-service without centralizing excessive privilege or hiding ownership;
- embed delivery, supply-chain, policy, tenancy, cost, and operational controls;
- operate the platform as a reliable dependency with SLOs and lifecycle contracts;
- drive voluntary adoption, migration, feedback, funding, and deprecation;
- measure value using flow, quality, reliability, satisfaction, and economics;
- translate AWS-first capabilities to Azure and Google Cloud without false parity.

## Recommended module path

### Phase 1 — Learn the platform product

| Step | Page | Outcome |
| ---: | --- | --- |
| 1 | [Platform engineering decision model](concepts.md) | Connect users, friction, capabilities, controls, and outcomes |
| 2 | [Product and operating model](product-operating-model.md) | Establish customers, ownership, roadmap, funding, and team boundaries |
| 3 | [Platform architecture](platform-architecture.md) | Separate experience, orchestration, control, resource, and evidence layers |
| 4 | [Golden paths and interfaces](golden-paths-interfaces.md) | Design discoverable, composable, versioned workflows and contracts |
| 5 | [Self-service and control planes](self-service-control-planes.md) | Reconcile desired state with safe identity and lifecycle boundaries |
| 6 | [Delivery and software supply chain](delivery-supply-chain.md) | Build safe source-to-production paths and artifact trust |
| 7 | [Security, tenancy, and governance](security-tenancy-governance.md) | Apply guardrails, isolation, policy, exceptions, and evidence |
| 8 | [Reliability and platform operations](reliability-operations.md) | Define SLOs, support, upgrades, incidents, recovery, and dependencies |
| 9 | [Adoption, metrics, and economics](adoption-metrics-economics.md) | Measure value, migration, satisfaction, capacity, and unit cost |

### Phase 2 — Apply the reasoning

| Step | Page | Outcome |
| ---: | --- | --- |
| 10 | [Enterprise platform design exercise](design-exercise.md) | Design an AWS-first thin viable platform for 200 developers |
| 11 | [Scenario questions and model answers](scenarios.md) | Practise at least 15 senior platform scenarios |
| 12 | [Advanced platform drills](scenario-drills.md) | Resolve at least 10 ambiguous technical and organizational failures |
| 13 | [Ten-minute platform review](presentation-template.md) | Present customers, contracts, controls, operation, adoption, and value |

### Phase 3 — Revise and assess

| Step | Page | Outcome |
| ---: | --- | --- |
| 14 | [Rapid-fire revision](rapid-fire.md) | Test at least 50 concise explanations |
| 15 | [Active-recall flashcards](flashcards.md) | Revisit at least 25 weak concepts |
| 16 | [Timed platform engineering mock interview](../mock-interviews/platform-engineering.md) | Complete a scored 50-minute assessment |
| 17 | [References and videos](references.md) | Deepen weak areas with primary sources |

## Relationship to adjacent modules

[CI/CD](../09-cicd/index.md), [Kubernetes](../11-kubernetes/index.md),
[Terraform/OpenTofu](../13-terraform/index.md), [DevSecOps](../15-devsecops/index.md),
[Observability](../17-observability/index.md), and [SRE](../18-sre/index.md) supply
specialist practices. The platform packages their common capabilities without
removing product-team responsibility for application and service outcomes.

## Completion checklist

- [ ] I can define the customer problem before proposing a portal or toolchain.
- [ ] I can distinguish platform, portal, control plane, and golden path.
- [ ] I can design secure self-service with explicit ownership and escape hatches.
- [ ] I can explain contracts, upgrades, SLOs, incidents, and recovery.
- [ ] I can measure adoption and outcomes without rewarding vanity activity.
- [ ] I answered all 25 scenarios aloud and completed the scored mock interview.
