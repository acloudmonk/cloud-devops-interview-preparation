# Ansible and Configuration Management

[← Curriculum overview](../curriculum/index.md) ·
[Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**
Level: **Senior / Architect**

Senior interviews test whether you can design a safe automation service, not
whether you can memorize YAML syntax. This module treats Ansible as an
agentless configuration, orchestration, and operational-automation platform.
AWS is the primary context, with Azure and Google Cloud translations.

!!! tip "Where to start"
    Start with **1. Configuration-management decision model** and follow the
    numbered path. The exercises are documentation-only: reason, design, and
    answer aloud without creating cloud resources.

## Learning objectives

By the end of this module, you should be able to:

- choose configuration management, image baking, cloud-init, IaC, or a managed service;
- model trustworthy inventory, variables, facts, groups, and precedence;
- design idempotent playbooks, handlers, failure controls, and rolling changes;
- create stable roles and collections with explicit contracts and versions;
- operate execution environments, AWX/Automation Controller, and delegated automation;
- protect credentials, secrets, privilege escalation, logs, and target access;
- layer linting, syntax, check mode, integration, convergence, and outcome tests;
- automate AWS fleets through dynamic inventory and Systems Manager;
- translate identity, inventory, and connectivity decisions to Azure and GCP;
- define clear ownership boundaries between Terraform/OpenTofu and Ansible.

## Recommended module path

### Phase 1 — Learn the automation operating system

| Step | Page | Outcome |
| ---: | --- | --- |
| 1 | [Configuration-management decision model](concepts.md) | Select the right control mechanism and ownership model |
| 2 | [Inventory, variables, and facts](inventory-variables.md) | Build explainable target and data models |
| 3 | [Playbooks, idempotency, and failure control](playbooks-idempotency.md) | Design convergent, bounded, recoverable runs |
| 4 | [Roles, collections, and content contracts](roles-collections.md) | Package reusable automation as governed products |
| 5 | [Execution platforms and operations](execution-platform.md) | Operate runners, controllers, workflows, schedules, and evidence |
| 6 | [Security, secrets, and trust](security-secrets.md) | Bound credentials, escalation, content, and output exposure |
| 7 | [Testing and quality gates](testing-quality.md) | Prove syntax, behavior, convergence, compatibility, and outcomes |
| 8 | [AWS and multi-cloud integration](cloud-integration.md) | Design dynamic inventory, connectivity, identity, and translations |
| 9 | [Terraform and Ansible boundaries](terraform-ansible-boundary.md) | Prevent overlapping ownership and fragile hand-offs |

### Phase 2 — Apply the reasoning

| Step | Page | Outcome |
| ---: | --- | --- |
| 10 | [Enterprise automation design exercise](design-exercise.md) | Design a governed AWS-first automation service |
| 11 | [Scenario questions and model answers](scenarios.md) | Practise 15 senior Ansible scenarios |
| 12 | [Advanced incident drills](scenario-drills.md) | Handle 10 ambiguous automation incidents |
| 13 | [Ten-minute automation review](presentation-template.md) | Present boundaries, trust, rollout, recovery, and value |

### Phase 3 — Revise and assess

| Step | Page | Outcome |
| ---: | --- | --- |
| 14 | [Rapid-fire revision](rapid-fire.md) | Test 50 concise verbal explanations |
| 15 | [Active-recall flashcards](flashcards.md) | Revisit weak concepts with spaced repetition |
| 16 | [Timed Ansible mock interview](../mock-interviews/ansible-configuration-management.md) | Complete a scored 50-minute assessment |
| 17 | [References and videos](references.md) | Deepen weak areas with primary sources |

## Scope boundary

Terraform/OpenTofu state and infrastructure lifecycle belong to
[Module 13](../13-terraform/index.md). Pipeline architecture belongs to
[Module 09](../09-cicd/index.md). This module focuses on target selection,
configuration convergence, orchestration, content reuse, execution control,
and operational automation.

## Completion checklist

- [ ] I can choose Ansible only when it is the appropriate lifecycle owner.
- [ ] I can explain inventory resolution and variable precedence without guessing.
- [ ] I can design an idempotent, observable, bounded rolling change.
- [ ] I can secure controller, runner, credential, secret, and privilege boundaries.
- [ ] I can diagnose unreachable, failed, changed, skipped, and inconsistent hosts.
- [ ] I can separate Terraform and Ansible ownership with explicit hand-offs.
- [ ] I answered all 25 scenarios aloud and completed the scored mock interview.
