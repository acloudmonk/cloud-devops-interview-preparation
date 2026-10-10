# Docker & Container Engineering

[← Curriculum overview](../curriculum/index.md) ·
[Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**
Level: **Senior / Architect**

Senior container interviews test whether you understand images, runtime isolation,
network and storage boundaries, supply-chain trust, resource behavior, and failure
recovery—not whether you can memorize Docker commands.

!!! tip "Where to start"
    Start with **1. Container mental model** and follow the numbered path. Docker
    and OCI provide the technical anchor. AWS ECR, ECS, Fargate, and EKS provide
    the primary cloud context, with Azure and Google Cloud translations where the
    platform changes an architectural decision. No executable lab is required.

## Learning objectives

By the end of this module, you should be able to:

- distinguish an image, container, process, runtime, engine, registry, and orchestrator;
- explain OCI image and runtime responsibilities without treating containers as VMs;
- build deterministic, minimal, multi-platform images with intentional cache behavior;
- reason about namespaces, cgroups, capabilities, seccomp, rootless mode, and escape risk;
- design container DNS, port publication, service connectivity, and network policy;
- place mutable state correctly across layers, volumes, object stores, and databases;
- govern registries, tags, digests, provenance, signing, scanning, and retention;
- harden build and runtime identities, filesystems, secrets, and dependencies;
- diagnose startup, crash, resource, network, storage, and architecture failures;
- communicate portability, operability, security, performance, and cost trade-offs.

## Recommended module path

### Phase 1 — Learn the container system

| Step | Page | Outcome |
| ---: | --- | --- |
| 1 | [Container mental model](concepts.md) | Understand images, containers, processes, runtimes, and OCI boundaries |
| 2 | [Images and build engineering](images-builds.md) | Design deterministic layers, contexts, caches, and multi-stage builds |
| 3 | [Runtime isolation and resources](runtime-isolation.md) | Reason about namespaces, cgroups, signals, limits, and platform behavior |
| 4 | [Networking and service connectivity](networking.md) | Design container interfaces, DNS, ports, proxies, and policy |
| 5 | [Storage and state](storage.md) | Choose writable layers, mounts, volumes, external state, and backup boundaries |
| 6 | [Registries and supply-chain controls](registries-supply-chain.md) | Govern identity, promotion, scanning, signing, and lifecycle |
| 7 | [Security hardening](security-hardening.md) | Reduce build/runtime privilege, attack surface, and secret exposure |
| 8 | [Operations and troubleshooting](operations-troubleshooting.md) | Diagnose lifecycle, capacity, compatibility, and dependency failures |

### Phase 2 — Apply the reasoning

| Step | Page | Outcome |
| ---: | --- | --- |
| 9 | [Container-platform design exercise](design-exercise.md) | Design a governed AWS container platform without deploying it |
| 10 | [Scenario questions and model answers](scenarios.md) | Practise 15 core container scenarios |
| 11 | [Advanced incident drills](scenario-drills.md) | Handle 10 ambiguous container failures |
| 12 | [Ten-minute container review](presentation-template.md) | Present image, runtime, security, and operating decisions |

### Phase 3 — Revise and assess

| Step | Page | Outcome |
| ---: | --- | --- |
| 13 | [Rapid-fire revision](rapid-fire.md) | Test 50 concise verbal explanations |
| 14 | [Active-recall flashcards](flashcards.md) | Revisit weak concepts with spaced repetition |
| 15 | [Timed container mock interview](../mock-interviews/docker-container-engineering.md) | Complete a scored 50-minute assessment |
| 16 | [References and videos](references.md) | Deepen weak areas with primary sources |

## Scope boundary

This module covers container artifacts and execution. Pipeline promotion belongs
to [Module 09](../09-cicd/index.md), Kubernetes control-plane and workload
orchestration to [Module 11](../11-kubernetes/index.md), and full software
supply-chain threat modeling to [Module 15](../15-devsecops/index.md).

## Completion checklist

- [ ] I can trace source and base-image inputs to an immutable runtime image digest.
- [ ] I can explain which isolation comes from the kernel and which comes from policy.
- [ ] I can choose network, storage, identity, and resource controls from workload needs.
- [ ] I can diagnose a container without assuming its filesystem or process is a VM.
- [ ] I answered all 25 scenarios aloud and recorded weak areas.
- [ ] I completed the design exercise and the scored mock interview.
