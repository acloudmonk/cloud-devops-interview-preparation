# CI/CD & Progressive Delivery

[← Curriculum overview](../curriculum/index.md) ·
[Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**
Level: **Senior / Architect**

Senior CI/CD interviews test whether you can move a reviewed source change into
production as the same trusted artifact, with fast evidence, controlled risk,
clear ownership, and recoverable failure—not whether you can recall one YAML syntax.

!!! tip "Where to start"
    Start with **1. Delivery-system mental model** and follow the numbered path.
    GitHub Actions is the workflow anchor and AWS is the deployment anchor, with
    Jenkins, GitLab CI/CD, Azure Pipelines, and other cloud targets translated
    where semantics affect design. No pipeline or cloud deployment is required.

## Learning objectives

By the end of this module, you should be able to:

- separate continuous integration, delivery, deployment, release, and exposure;
- design event, orchestration, worker, artifact, policy, and deployment boundaries;
- build once and promote an immutable artifact with traceable evidence;
- place fast, reliable tests and risk-based policy gates in the feedback path;
- secure runners, tokens, secrets, third-party actions, caches, and environments;
- choose rolling, blue/green, canary, feature-flag, and GitOps-style delivery patterns;
- coordinate backward-compatible database, API, configuration, and flag changes;
- design approvals and emergency change without turning governance into ceremony;
- diagnose flaky, slow, compromised, stuck, or partially successful pipelines;
- communicate reliability, security, developer-experience, and cost trade-offs.

## Recommended module path

### Phase 1 — Learn the delivery system

| Step | Page | Outcome |
| ---: | --- | --- |
| 1 | [Delivery-system mental model](concepts.md) | Understand CI, delivery, deployment, release, and evidence flow |
| 2 | [Pipeline architecture](pipeline-architecture.md) | Design triggers, orchestration, workers, concurrency, and reusable workflows |
| 3 | [Testing and quality gates](testing-quality-gates.md) | Balance feedback speed, confidence, flakiness, and policy |
| 4 | [Artifacts and provenance](artifacts-provenance.md) | Build once, promote immutably, and trace source to deployment |
| 5 | [Identity, secrets, and runners](security-runners.md) | Secure workflow code, credentials, dependencies, and execution environments |
| 6 | [Deployment and release strategies](deployment-strategies.md) | Choose rollout, verification, rollback, and release mechanisms |
| 7 | [Database, configuration, and flags](database-config-flags.md) | Coordinate backward-compatible state and behavior changes |
| 8 | [Operations and troubleshooting](operations-troubleshooting.md) | Make pipelines observable, reliable, recoverable, and cost-aware |

### Phase 2 — Apply the reasoning

| Step | Page | Outcome |
| ---: | --- | --- |
| 9 | [Delivery-platform design exercise](design-exercise.md) | Design an enterprise delivery system without deployment |
| 10 | [Scenario questions and model answers](scenarios.md) | Practise 15 core CI/CD scenarios |
| 11 | [Advanced incident drills](scenario-drills.md) | Handle 10 ambiguous delivery failures |
| 12 | [Ten-minute delivery review](presentation-template.md) | Present flow, controls, risks, and decisions clearly |

### Phase 3 — Revise and assess

| Step | Page | Outcome |
| ---: | --- | --- |
| 13 | [Rapid-fire revision](rapid-fire.md) | Test 50 concise verbal explanations |
| 14 | [Active-recall flashcards](flashcards.md) | Revisit weak concepts with spaced repetition |
| 15 | [Timed CI/CD mock interview](../mock-interviews/cicd-progressive-delivery.md) | Complete a scored 50-minute assessment |
| 16 | [References and videos](references.md) | Deepen weak areas with primary sources |

## Scope boundary

This module covers delivery-system architecture and operations. Source-control
branch/PR governance belongs to [Module 08](../08-git/index.md). Container image
construction belongs to [Module 10](../10-docker/index.md), Kubernetes rollout
mechanics to [Module 11](../11-kubernetes/index.md), and full supply-chain threat
modeling to [Module 15](../15-devsecops/index.md).

## Completion checklist

- [ ] I can trace one source revision to its artifact, evidence, deployment, and release.
- [ ] I can explain why rebuilding per environment breaks promotion integrity.
- [ ] I can choose rollout and recovery from workload/state constraints.
- [ ] I can secure untrusted code, runners, credentials, and privileged publication.
- [ ] I answered all 25 scenarios aloud and recorded weak areas.
- [ ] I completed the design exercise before reading scenario answers.
- [ ] I completed the mock interview and recorded evidence for each score.
