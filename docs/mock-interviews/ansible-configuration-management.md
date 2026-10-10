# Ansible and Configuration-Management Mock Interview

[← Mock interview overview](index.md) ·
[Module 14 overview](../14-ansible/index.md) ·
[Scenario answer framework](../interview-playbook/scenario-answer-framework.md)

Duration: **50 minutes**

Level: **Senior / Architect**
Primary context: **AWS with Ansible; Azure and GCP follow-ups**

## Candidate brief

A regulated enterprise manages 8,000 Linux and Windows VMs across 60 AWS
accounts, plus Azure and GCP. Teams use static inventory, shared SSH keys,
unpinned laptop runtimes, shell-heavy playbooks, and overlapping Terraform and
Ansible ownership. Design a safe self-service automation platform and migration.

## Interview structure

### 0–5 minutes — Discovery

Ask about service owners, fleet lifecycle, operating systems, connectivity,
criticality, maintenance windows, identity, secrets, current failures,
compliance evidence, managed-service constraints, and recovery objectives.

### 5–15 minutes — Architecture

Choose appropriate automation mechanisms, assign ownership, design dynamic
inventory and tag governance, define role/collection contracts, execution
environments, controller topology, and AWS/Azure/GCP boundaries.

### 15–25 minutes — Trust and delivery

Design SSO/RBAC, short-lived job identity, target connection and escalation,
secret retrieval, source/dependency trust, lint/test/convergence gates, approval,
canary, bounded rolling batches, stop conditions, and outcome evidence.

### 25–35 minutes — Incident branches

The interviewer selects two:

1. An inventory change expands a production patch from 40 to 4,000 hosts.
2. The controller fails while runners continue a rolling service restart.
3. A compromised collection ran with a privileged AWS and target identity.
4. An SSM job leaves sensitive transfer data in S3 after failure.
5. Terraform replaces instances during a long Ansible configuration run.

For each, contain first, preserve evidence, classify completed changes, recover
service, reconcile desired state, and improve controls.

### 35–42 minutes — Evolution and trade-offs

Explain CLI versus AWX/Automation Controller, SSH versus Systems Manager,
mutable configuration versus immutable images, Vault versus external secrets,
static versus dynamic inventory, and centralized versus delegated content.

### 42–47 minutes — Executive communication

Summarize the target model, largest risks, migration waves, investment, trade-off,
and success measures in two minutes, then answer one challenge from a security or
application executive.

### 47–50 minutes — Candidate questions

Ask about failure history, team incentives, platform ownership, audit needs,
support requirements, or which business outcome should improve first.

## Scoring rubric

Score 0–4 in each dimension:

| Dimension | Evidence expected |
| --- | --- |
| Discovery | constraints, owners, failure modes, and assumptions surfaced |
| Tool and lifecycle ownership | one authoritative owner for each mutable field |
| Inventory and data | governed discovery, limits, precedence, and freshness |
| Trust and security | bounded identity, transport, escalation, secrets, and supply chain |
| Content and runtime | contracts, versions, execution environments, and controller design |
| Delivery and recovery | tests, convergence, canary, batches, stops, evidence, and recovery |
| Cloud translation | AWS depth with accurate Azure and GCP adaptation |
| Communication | structured recommendation, trade-offs, adoption, and measures |

Maximum score: **32**

- **27–32:** strong senior/architect signal
- **21–26:** credible, with specific gaps to revisit
- **15–20:** implementation familiarity without enough operating-model depth
- **0–14:** rebuild fundamentals and repeat the module scenarios

## Improvement loop

1. Record the answer and score each row with evidence.
2. Select the two weakest dimensions.
3. Revisit the matching Module 14 pages and official references.
4. Rewrite the decision as context, options, choice, trade-off, failure, recovery,
   and measure.
5. Repeat with a different incident pair within one week.
