# Terraform, OpenTofu, and Infrastructure as Code

[← Curriculum overview](../curriculum/index.md) ·
[Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**
Level: **Senior / Architect**

Senior interviews test whether you can design a safe infrastructure delivery system,
not whether you can recall every HCL function. This module uses Terraform as the
primary interview vocabulary and treats OpenTofu as a compatible but independently
evolving alternative.

!!! tip "Where to start"
    Start with **1. Infrastructure-as-Code decision model** and follow the numbered
    path. AWS is the primary platform context; Azure and GCP translations expose
    provider, identity, state, and organizational differences. No cloud deployment
    or executable lab is required.

## Learning objectives

By the end of this module, you should be able to:

- explain declarative planning, dependency graphs, state, refresh, and lifecycle;
- protect state integrity, concurrency, confidentiality, backup, and recovery;
- design module interfaces, versions, composition, ownership, and deprecation;
- choose repository, root-module, account, region, and environment boundaries;
- design short-lived provider authentication and least-privilege execution roles;
- build plan, policy, testing, approval, apply, evidence, and rollback workflows;
- handle drift, import, moved resources, refactoring, provider upgrades, and incidents;
- distinguish Terraform CLI, HCP Terraform/Enterprise, and Terraform Stacks;
- compare Terraform and OpenTofu using compatibility, governance, features, and exit cost;
- communicate AWS-first decisions and their Azure/GCP translations.

## Recommended module path

### Phase 1 — Learn the IaC operating system

| Step | Page | Outcome |
| ---: | --- | --- |
| 1 | [Infrastructure-as-Code decision model](concepts.md) | Reason about desired state, ownership, blast radius, and lifecycle |
| 2 | [Configuration, graph, and workflow](configuration-workflow.md) | Explain HCL, evaluation, plan, apply, replacement, and uncertainty |
| 3 | [State, backends, locking, and recovery](state-backends.md) | Protect the source of resource identity and recover safely |
| 4 | [Module contracts and composition](modules-contracts.md) | Design stable, testable, versioned platform interfaces |
| 5 | [Environment and repository architecture](environments-architecture.md) | Partition accounts, regions, environments, roots, and pipelines |
| 6 | [Providers, identity, and multi-cloud](providers-identity.md) | Design authentication, aliases, permissions, and cloud translations |
| 7 | [Testing, policy, and security](testing-policy-security.md) | Layer validation, tests, policy, supply-chain, and secret controls |
| 8 | [Automation, drift, and lifecycle operations](automation-operations.md) | Operate plans, applies, imports, refactors, upgrades, and recovery |
| 9 | [Terraform and OpenTofu decision guide](terraform-opentofu.md) | Compare shared foundations and deliberate divergence |

### Phase 2 — Apply the reasoning

| Step | Page | Outcome |
| ---: | --- | --- |
| 10 | [Enterprise IaC design exercise](design-exercise.md) | Design a governed AWS-first operating model without deploying it |
| 11 | [Scenario questions and model answers](scenarios.md) | Practise 15 core Terraform/OpenTofu scenarios |
| 12 | [Advanced incident drills](scenario-drills.md) | Handle 10 ambiguous state, identity, drift, and migration incidents |
| 13 | [Ten-minute IaC architecture review](presentation-template.md) | Present boundaries, controls, recovery, adoption, and trade-offs |

### Phase 3 — Revise and assess

| Step | Page | Outcome |
| ---: | --- | --- |
| 14 | [Rapid-fire revision](rapid-fire.md) | Test 50 concise verbal explanations |
| 15 | [Active-recall flashcards](flashcards.md) | Revisit weak concepts with spaced repetition |
| 16 | [Timed IaC mock interview](../mock-interviews/terraform-iac.md) | Complete a scored 50-minute assessment |
| 17 | [References and videos](references.md) | Deepen weak areas with primary sources |

## Scope boundary

Git branching and pull-request governance belong to [Module 08](../08-git/index.md).
General pipeline and supply-chain architecture belongs to [Module 09](../09-cicd/index.md).
Cloud service design belongs to Modules 01–05. This module focuses on the lifecycle,
trust, architecture, and operations of declarative infrastructure management.

## Completion checklist

- [ ] I can explain how configuration, state, provider reads, and the plan interact.
- [ ] I can design state and execution boundaries that contain failure and access.
- [ ] I can evolve modules and resource addresses without destructive recreation.
- [ ] I can diagnose stale plans, drift, locks, imports, partial applies, and upgrades.
- [ ] I can justify Terraform or OpenTofu without treating them as permanently identical.
- [ ] I answered all 25 scenarios aloud and completed the scored mock interview.
