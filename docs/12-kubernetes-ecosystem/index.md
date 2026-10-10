# Kubernetes Ecosystem

[← Curriculum overview](../curriculum/index.md) ·
[Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**
Level: **Senior / Architect**

Senior platform interviews test whether you can choose, integrate, govern, upgrade,
and remove ecosystem components without creating conflicting controllers or an
unmaintainable platform—not whether you recognize every project logo.

!!! tip "Where to start"
    Start with **1. Ecosystem decision model** and follow the numbered path. Upstream
    Kubernetes contracts remain the foundation. Amazon EKS is the primary cloud
    context, with AKS and GKE translations where managed add-ons change ownership.
    No cluster installation or executable lab is required.

## Learning objectives

By the end of this module, you should be able to:

- evaluate ecosystem tools by capability, ownership, compatibility, and exit cost;
- choose Helm, Kustomize, or a combination without creating multiple sources of truth;
- design GitOps reconciliation, promotion, secrets, tenancy, drift, and emergency change;
- distinguish Kubernetes network contracts from CNI and eBPF implementations;
- decide when Gateway API, ingress, or a service mesh is justified;
- coordinate workload, event, and node autoscaling without unstable control loops;
- design admission policy, external secret delivery, certificates, and exception lifecycle;
- govern CRDs, operators, webhooks, add-ons, upgrades, backups, and deletion safety;
- troubleshoot reconciliation, webhook, network, scaling, policy, and controller conflicts;
- communicate platform product, portability, reliability, security, and cost trade-offs.

## Recommended module path

### Phase 1 — Learn the ecosystem decision system

| Step | Page | Outcome |
| ---: | --- | --- |
| 1 | [Ecosystem decision model](concepts.md) | Evaluate need, ownership, maturity, coupling, evidence, and exit strategy |
| 2 | [Packaging and customization](packaging-customization.md) | Choose Helm, Kustomize, composition, validation, and promotion boundaries |
| 3 | [GitOps and reconciliation](gitops.md) | Design Argo CD/Flux ownership, drift, promotion, tenancy, and recovery |
| 4 | [CNI, eBPF, and network platforms](networking-ebpf.md) | Separate Kubernetes contracts from implementation and migration trade-offs |
| 5 | [Gateway API and service mesh](gateway-service-mesh.md) | Choose north-south/east-west traffic, identity, policy, and telemetry layers |
| 6 | [Autoscaling and capacity](autoscaling-capacity.md) | Coordinate HPA, VPA, event, node, and cloud-capacity control loops |
| 7 | [Policy, secrets, and certificates](policy-secrets.md) | Design admission, secret delivery, PKI, exceptions, and failure behavior |
| 8 | [Operators and ecosystem operations](operators-operations.md) | Govern CRDs/controllers, add-ons, upgrades, continuity, and troubleshooting |

### Phase 2 — Apply the reasoning

| Step | Page | Outcome |
| ---: | --- | --- |
| 9 | [Platform ecosystem design exercise](design-exercise.md) | Design a governed EKS platform toolchain without deploying it |
| 10 | [Scenario questions and model answers](scenarios.md) | Practise 15 core ecosystem scenarios |
| 11 | [Advanced incident drills](scenario-drills.md) | Handle 10 ambiguous controller and platform incidents |
| 12 | [Ten-minute ecosystem review](presentation-template.md) | Present selection, ownership, integration, risk, and adoption |

### Phase 3 — Revise and assess

| Step | Page | Outcome |
| ---: | --- | --- |
| 13 | [Rapid-fire revision](rapid-fire.md) | Test 50 concise verbal explanations |
| 14 | [Active-recall flashcards](flashcards.md) | Revisit weak concepts with spaced repetition |
| 15 | [Timed ecosystem mock interview](../mock-interviews/kubernetes-ecosystem.md) | Complete a scored 50-minute assessment |
| 16 | [References and videos](references.md) | Deepen weak areas with primary sources |

## Scope boundary

Kubernetes API, workload, scheduling, Service, storage, RBAC, probe, and upgrade
fundamentals belong to [Module 11](../11-kubernetes/index.md). CI/CD artifact and
promotion principles belong to [Module 09](../09-cicd/index.md). This module focuses
on optional/extended controllers and their operational integration.

## Completion checklist

- [ ] I can justify every platform component with a requirement and exit strategy.
- [ ] I can name the source of truth and field/controller owner for each outcome.
- [ ] I can plan version compatibility, failure behavior, upgrade, backup, and removal.
- [ ] I can distinguish portable APIs from implementation-specific dependencies.
- [ ] I answered all 25 scenarios aloud and recorded weak areas.
- [ ] I completed the design exercise and the scored mock interview.
