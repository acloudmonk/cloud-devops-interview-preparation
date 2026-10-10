# Terraform and Infrastructure-as-Code Mock Interview

[← Mock interview overview](index.md) ·
[Module 13 overview](../13-terraform/index.md) ·
[Scenario answer framework](../interview-playbook/scenario-answer-framework.md)

Duration: **50 minutes**

Level: **Senior / Architect**
Primary context: **AWS with Terraform; OpenTofu and multi-cloud follow-ups**

## Candidate brief

A regulated enterprise has 70 AWS accounts, copied Terraform roots, inconsistent state,
static CI credentials, manual console drift, and unversioned modules. It must reduce
provisioning time without increasing blast radius. Some teams propose OpenTofu; Azure and
GCP adoption is growing.

Design the target IaC operating model and explain how you would migrate safely.

## Interview structure

### 0–5 minutes — Discovery

Ask about ownership, account/environment topology, change frequency, state backends,
critical resources, compliance, current incidents, support, recovery targets, team skills,
and managed-platform constraints.

### 5–15 minutes — Architecture

Define root/state/repository boundaries, module product model, dependency contracts,
Terraform/OpenTofu policy, AWS organization integration, and Azure/GCP translation.

### 15–25 minutes — Trust and delivery

Design workload identity, plan/apply permissions, runner isolation, dependency controls,
tests, target-specific saved plans, policy, approvals, same-plan apply, and verification.

### 25–35 minutes — Incident branches

The interviewer selects two:

1. A stale approved plan replaces a production database dependency.
2. A failed apply leaves state locked and cloud resources partially created.
3. A provider update proposes changes across every account.
4. A plan artifact exposes a credential.
5. An emergency console fix is removed by drift automation.

For each, protect customers, preserve evidence, diagnose configuration/state/remote truth,
choose recovery, and improve the system.

### 35–42 minutes — Terraform/OpenTofu decision

Compare governance/licensing, support, managed execution, registries, tool-specific
features, compatibility, state encryption, migration order, and exit cost. Avoid claiming
that present compatibility guarantees future bidirectional migration.

### 42–47 minutes — Adoption and measures

Propose foundation bootstrap, legacy inventory, pilot roots, module rollout, migration
waves, exception handling, training, and retirement. Define lead time, failure, drift,
recovery, version adoption, and satisfaction measures.

### 47–50 minutes — Executive summary

Give a concise recommendation with outcome, minimum platform contract, top risks,
investment, owner, evidence, and next decision.

## Scorecard

Score each dimension from 0–4 for a total of 32:

| Dimension | 0 | 2 | 4 |
| --- | --- | --- | --- |
| Discovery | guesses | basic requirements | exposes ownership, risk, scale, recovery, and constraints |
| State architecture | unsafe/one state | backend mentioned | bounded states, locking, confidentiality, contracts, tested recovery |
| Module/environment design | copied code | reusable modules | product contracts, versions, promotion, deprecation, measured adoption |
| Identity/security | static admin keys | some IAM | federation, scoped roles, runner/supply-chain/secret controls and audit |
| Delivery assurance | apply pipeline | plan and approval | same-plan apply, layered tests/policy, target/outcome verification |
| Operations/recovery | rerun/rollback | basic troubleshooting | evidence-led drift, partial apply, import, refactor, upgrade recovery |
| Tool/multi-cloud judgment | brand choice | feature list | Terraform/OpenTofu and cloud trade-offs with migration/exit evidence |
| Communication/adoption | tool dump | structured design | prioritized recommendation, transition, measures, owners, decision |

Interpretation:

- **27–32:** principal-level architecture and operating judgment
- **21–26:** strong senior performance with bounded gaps
- **15–20:** useful implementation knowledge but weak lifecycle/governance depth
- **0–14:** unsafe or tool-command-centered answer

## Improvement loop

Record missed assumptions, destructive-change reasoning, state/recovery gaps, unclear tool
comparisons, and weak metrics. Revisit the corresponding module page, repeat only the weak
segment after 48 hours, then repeat the full interview within one week.
