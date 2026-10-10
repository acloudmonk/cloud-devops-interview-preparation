# Git & Source-Control Strategy

[← Curriculum overview](../curriculum/index.md) ·
[Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**
Level: **Senior / Architect**

Senior Git interviews test whether you can preserve history, recover safely,
design collaboration rules, and connect source control to delivery and audit.
Command recall matters less than understanding the commit graph and the
organizational consequences of changing it.

!!! tip "Where to start"
    Start with **1. Git mental model** and follow the numbered path. GitHub is
    the collaboration anchor, with GitLab and Azure DevOps concepts translated
    where workflow semantics differ. No hosted repository or coding lab is required.

## Learning objectives

By the end of this module, you should be able to:

- explain blobs, trees, commits, tags, references, HEAD, index, and working tree;
- distinguish content history from branch names and remote-tracking references;
- choose merge, rebase, squash, revert, reset, restore, and cherry-pick safely;
- compare trunk-based development, short-lived branches, release branches, and GitFlow;
- design pull-request, CODEOWNERS, branch/ruleset, and exception governance;
- choose monorepo, multirepo, submodule, subtree, and large-file approaches;
- protect credentials, commits, tags, dependencies, and automation identities;
- diagnose conflicts, lost commits, regressions, accidental history rewrites, and large repositories;
- connect source-control controls to CI/CD without treating a green check as sufficient assurance.

## Recommended module path

### Phase 1 — Learn the system

| Step | Page | Outcome |
| ---: | --- | --- |
| 1 | [Git mental model](concepts.md) | Understand objects, references, HEAD, index, and distributed history |
| 2 | [Daily change workflow](daily-workflow.md) | Build reviewable commits and inspect staged/unstaged state |
| 3 | [Branching and integration](branching-integration.md) | Choose merge, rebase, squash, cherry-pick, and release operations |
| 4 | [Collaboration strategies](collaboration-strategies.md) | Match branching policy to delivery, risk, and team constraints |
| 5 | [Pull-request governance](pull-request-governance.md) | Design reviews, ownership, rulesets, exceptions, and merge queues |
| 6 | [Repository architecture](repository-architecture.md) | Evaluate monorepo, multirepo, shared code, and large-file trade-offs |
| 7 | [Security and integrity](security-integrity.md) | Protect identity, credentials, history, tags, and automation |
| 8 | [Recovery and troubleshooting](recovery-troubleshooting.md) | Recover safely and find regressions with evidence |

### Phase 2 — Apply the reasoning

| Step | Page | Outcome |
| ---: | --- | --- |
| 9 | [Source-control design exercise](design-exercise.md) | Design governance for a growing platform organization |
| 10 | [Scenario questions and model answers](scenarios.md) | Practise 15 core Git and governance scenarios |
| 11 | [Advanced incident drills](scenario-drills.md) | Handle 10 ambiguous recovery and collaboration failures |
| 12 | [Ten-minute source-control review](presentation-template.md) | Present workflow, controls, risks, and decisions clearly |

### Phase 3 — Revise and assess

| Step | Page | Outcome |
| ---: | --- | --- |
| 13 | [Rapid-fire revision](rapid-fire.md) | Test 50 concise verbal explanations |
| 14 | [Active-recall flashcards](flashcards.md) | Revisit weak concepts with spaced repetition |
| 15 | [Timed Git strategy mock interview](../mock-interviews/git-source-control.md) | Complete a scored 50-minute assessment |
| 16 | [References and videos](references.md) | Deepen weak areas with primary sources |

## Scope boundary

This module covers source control and collaboration governance. Pipeline design,
artifact promotion, deployment approvals, and progressive delivery belong to
[Module 09 — CI/CD](../09-cicd/index.md). Detailed software supply-chain
security belongs to [Module 15 — DevSecOps](../15-devsecops/index.md).

## Completion checklist

- [ ] I can draw a commit graph and predict merge, rebase, reset, and revert outcomes.
- [ ] I can recover an apparently lost commit without guessing or deleting evidence.
- [ ] I can choose a branching model from delivery and regulatory constraints.
- [ ] I can design least-privilege review and emergency-change governance.
- [ ] I answered all 25 scenarios aloud and recorded weak areas.
- [ ] I completed the design exercise before reading scenario answers.
- [ ] I completed the mock interview and recorded evidence for each score.
