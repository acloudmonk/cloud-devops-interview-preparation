# Enterprise IaC Design Exercise

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

This is a documentation-only architecture exercise. Produce decisions, diagrams, tables,
and runbooks; do not provision cloud resources.

## Scenario

A regulated company has 70 AWS accounts across development, test, and production in two
regions. Fifteen product teams use copied Terraform roots, long-lived access keys, local
or inconsistently configured S3 state, and modules pinned to branches. Network and
security teams also make console changes. Two teams want OpenTofu for licensing and state
encryption; leadership wants one auditable operating model. Azure adoption begins next
year, and a GCP analytics environment already exists.

Recent events include:

- a stale plan replaced a production database subnet group;
- concurrent applies left state and infrastructure partially updated;
- a module default change opened an ingress rule;
- a leaked plan artifact exposed a secret;
- a provider upgrade proposed widespread replacement;
- an emergency console change was later reverted by automation.

## Deliverables

### 1. Outcomes and constraints

Define measurable goals for lead time, change failure, audit evidence, recovery,
credential lifetime, state durability, module adoption, drift age, and exceptions.

### 2. Ownership map

Assign owners for platform standards, root configuration, modules, state service,
runners, cloud roles, providers, policy, incident response, and business outcomes.

### 3. State and root topology

Draw account, region, environment, and capability boundaries. Explain why each root is
combined or separated and how consumers obtain outputs without broad remote-state access.

### 4. Repository architecture

Choose monorepo, domain repositories, or a hybrid. Define CODEOWNERS, versioning,
promotion, dependency updates, release notes, and deprecation.

### 5. Identity and trust

Design CI federation into AWS roles, read/plan versus apply permissions, production
approval, backend administration, break glass, runner isolation, and audit correlation.

### 6. Delivery workflow

Show validation, tests, target-specific saved plan, policy/cost/security evidence,
approval, same-plan apply, outcome verification, and drift monitoring.

### 7. Module product model

Define the first three paved-path modules, their interfaces, invariants, test strategy,
version policy, support SLO, consumer migration, and measures.

### 8. Terraform/OpenTofu policy

Decide whether both tools are permitted, where each is supported, how a root records its
tool/version, which features constrain migration, and what evidence is required for a
transition. Include HCP Terraform/Enterprise evaluation if proposed.

### 9. Recovery and lifecycle runbooks

Cover stuck lock, backend outage, lost/corrupt state, wrong import, partial apply, stale
plan, provider regression, destructive change, manual emergency change, and tool migration.

### 10. Multi-cloud translation

Map AWS account/role/backend/policy decisions to Azure subscription/federated identity
and GCP project/service-account impersonation. Identify deliberately cloud-specific modules.

## Required decision tables

### Root boundary

| Capability | Owner | Account/region | State | Apply identity | Change cadence | Failure radius |
| --- | --- | --- | --- | --- | --- | --- |
| Example: network foundation | network platform | production/shared, one region | dedicated | network apply role | monthly | regional shared connectivity |

### Tool selection

| Requirement              | Terraform evidence | OpenTofu evidence | Decision/exception | Exit cost |
| ------------------------ | ------------------ | ----------------- | ------------------ | --------- |
| Managed remote execution |                    |                   |                    |           |
| Open-source licensing    |                    |                   |                    |           |
| State/plan encryption    |                    |                   |                    |           |
| Enterprise support       |                    |                   |                    |           |

### Control model

| Risk                       | Prevent | Detect | Respond/recover | Evidence |
| -------------------------- | ------- | ------ | --------------- | -------- |
| Stale/destructive plan     |         |        |                 |          |
| State compromise           |         |        |                 |          |
| Provider/module compromise |         |        |                 |          |
| Unauthorized drift         |         |        |                 |          |

## Review rubric

Score each dimension from 0–4:

- requirements and explicit assumptions;
- ownership and bounded state/execution architecture;
- identity, secrets, supply-chain, and policy controls;
- module and environment lifecycle;
- Terraform/OpenTofu decision quality;
- failure, recovery, and migration realism;
- AWS depth and Azure/GCP translation;
- adoption plan, measures, and executive communication.

A strong answer proposes a small supported platform contract, not a universal repository
and administrator credential. It explains trade-offs, transition order, evidence, and
how unsafe legacy roots are retired.
