# Kubernetes

[← Curriculum overview](../curriculum/index.md) ·
[Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**
Level: **Senior / Architect**

Senior Kubernetes interviews test whether you can reason about desired state,
reconciliation, scheduling, failure domains, workload identity, networking, storage,
and safe operations—not whether you can recall `kubectl` commands.

!!! tip "Where to start"
    Start with **1. Kubernetes mental model** and follow the numbered path. Upstream
    Kubernetes concepts are the foundation; Amazon EKS is the primary cloud anchor,
    with AKS and GKE translations where managed-service responsibility differs. Helm,
    GitOps, service mesh, and other ecosystem tools belong to Module 12. No cluster
    deployment or executable lab is required.

## Learning objectives

By the end of this module, you should be able to:

- explain declarative desired state, reconciliation, ownership, and eventual convergence;
- trace an API request through authentication, authorization, admission, storage, and controllers;
- choose Pods, Deployments, StatefulSets, DaemonSets, Jobs, and disruption controls;
- design requests, limits, quotas, placement, topology, priority, and autoscaling;
- reason about Services, DNS, ingress/Gateway, CNI, network policy, and traffic paths;
- select storage classes, access modes, topology, reclaim, backup, and recovery behavior;
- secure RBAC, service accounts, workload identity, secrets, admission, nodes, and tenants;
- distinguish startup, readiness, liveness, rollout, autoscaling, and customer health;
- plan upgrades, node maintenance, observability, continuity, and systematic troubleshooting;
- communicate reliability, portability, security, developer-experience, and cost trade-offs.

## Recommended module path

### Phase 1 — Learn the Kubernetes system

| Step | Page | Outcome |
| ---: | --- | --- |
| 1 | [Kubernetes mental model](concepts.md) | Understand API objects, desired state, controllers, ownership, and convergence |
| 2 | [Control plane and node architecture](control-plane.md) | Trace API, etcd, scheduler, controllers, kubelet, and runtime responsibilities |
| 3 | [Workloads and controllers](workloads-controllers.md) | Choose workload primitives, rollouts, health, disruption, and lifecycle |
| 4 | [Scheduling, resources, and scaling](scheduling-resources.md) | Design placement, capacity, limits, priority, and autoscaling |
| 5 | [Networking and traffic](networking.md) | Trace pod, Service, DNS, ingress, policy, and external traffic paths |
| 6 | [Storage and stateful workloads](storage.md) | Design volumes, classes, topology, identity, backup, and recovery |
| 7 | [Security and multi-tenancy](security.md) | Secure identities, RBAC, admission, secrets, nodes, and tenant boundaries |
| 8 | [Operations and troubleshooting](operations-troubleshooting.md) | Operate upgrades, nodes, controllers, observability, and incident diagnosis |

### Phase 2 — Apply the reasoning

| Step | Page | Outcome |
| ---: | --- | --- |
| 9 | [Kubernetes platform design exercise](design-exercise.md) | Design a governed EKS platform without deploying it |
| 10 | [Scenario questions and model answers](scenarios.md) | Practise 15 core Kubernetes scenarios |
| 11 | [Advanced incident drills](scenario-drills.md) | Handle 10 ambiguous cluster incidents |
| 12 | [Ten-minute Kubernetes review](presentation-template.md) | Present platform, workload, security, and operating decisions |

### Phase 3 — Revise and assess

| Step | Page | Outcome |
| ---: | --- | --- |
| 13 | [Rapid-fire revision](rapid-fire.md) | Test 50 concise verbal explanations |
| 14 | [Active-recall flashcards](flashcards.md) | Revisit weak concepts with spaced repetition |
| 15 | [Timed Kubernetes mock interview](../mock-interviews/kubernetes-platform.md) | Complete a scored 50-minute assessment |
| 16 | [References and videos](references.md) | Deepen weak areas with primary sources |

## Scope boundary

Container image and runtime engineering belong to [Module 10](../10-docker/index.md).
Helm, Kustomize, Argo CD, Flux, service mesh, eBPF products, external policy/secrets,
operators, and ecosystem selection belong to
[Module 12](../12-kubernetes-ecosystem/index.md). This module uses only the ecosystem
detail required to explain the upstream Kubernetes contract.

## Completion checklist

- [ ] I can trace one desired-state change through API storage and reconciliation.
- [ ] I can choose workload, placement, traffic, storage, identity, and health controls.
- [ ] I can separate application, Kubernetes, node, cloud, and dependency failures.
- [ ] I can plan a safe rollout, disruption, upgrade, recovery, and evidence path.
- [ ] I answered all 25 scenarios aloud and recorded weak areas.
- [ ] I completed the design exercise and the scored mock interview.
