# Enterprise Automation Design Exercise

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

This is a paper design exercise. Do not deploy resources. Produce decisions,
boundaries, workflows, recovery, and measurable outcomes.

## Scenario

A regulated company operates 8,000 Linux and Windows VMs across 60 AWS accounts,
with smaller Azure and GCP estates. Teams run unpinned playbooks from laptops,
share SSH keys, maintain static inventories, use shell commands heavily, and
frequently restart entire services. Terraform provisions most cloud resources,
but some Ansible playbooks also modify them. There is no reliable job evidence,
second-run test, or recovery practice.

The company wants a self-service automation platform that reduces change time
without creating fleet-wide failure or a central root credential.

## Constraints

- production has no direct inbound internet or administrator SSH;
- identities must be short-lived and attributable;
- business services span accounts, regions, and mixed operating systems;
- a regional controller or cloud API can fail during a run;
- application teams need autonomy within owned services;
- existing automation must migrate incrementally.

## Deliverables

### 1. Discovery questions

Ask about service ownership, fleet and image lifecycle, connectivity, existing
roles, criticality, maintenance windows, current incidents, secrets, compliance,
controller requirements, Windows/Linux mix, and recovery objectives.

### 2. Responsibility map

Classify cloud infrastructure, base image, bootstrap, host configuration,
application release, patching, secrets, compliance, and break-glass actions.
Assign one authoritative system and owner to each.

### 3. Inventory architecture

Define account/region sources, filters, constructed groups, tag governance,
refresh policy, snapshot evidence, count anomaly detection, and explicit limits.

### 4. Trust architecture

Show human SSO, controller RBAC, runner identity, discovery role, mutation role,
target connection, privilege escalation, secret retrieval, and audit boundaries.

### 5. Content model

Define repositories, roles, collections, owners, versioning, deprecation,
dependency pinning, execution environments, and promotion.

### 6. Safe change workflow

Design review, lint, tests, inventory sync, preflight, approval, canary, rolling
batches, stop conditions, verification, notifications, and evidence retention.

### 7. Failure and recovery

Cover unreachable hosts, partial configuration, handler failure, expired
credential, stale inventory, package outage, controller loss, and bad collection.

### 8. Migration plan

Inventory existing content, rank risk, freeze unsafe patterns, onboard one
service, convert credentials, establish tests, migrate in waves, and retire
legacy laptop execution using measured exit criteria.

### 9. Multi-cloud translation

Explain what remains common and what changes for Azure and GCP inventory,
identity, connectivity, logging, and managed-service alternatives.

### 10. Measures

Propose change success rate, convergence rate, unreachable rate, recovery time,
credential age, inventory anomalies, self-service adoption, manual effort, and
service-impact metrics.

## Decision worksheets

### Automation ownership

| Capability | Authoritative owner | Interface | Credential | Recovery owner |
| --- | --- | --- | --- | --- |
| Example: EC2 lifecycle | Terraform | governed tags/readiness event | account provisioning role | cloud platform |

### Run control

| Risk                     | Prevent | Detect | Stop/contain | Recover | Evidence |
| ------------------------ | ------- | ------ | ------------ | ------- | -------- |
| Wrong production targets |         |        |              |         |          |
| Secret exposure          |         |        |              |         |          |
| Non-convergent role      |         |        |              |         |          |
| Partial rolling change   |         |        |              |         |          |

## Review rubric

Score each dimension from 0–4:

- requirements and explicit assumptions;
- lifecycle ownership and inventory safety;
- identity, secrets, transport, and supply-chain controls;
- idempotency, testing, rollout, and recovery;
- AWS depth and accurate Azure/GCP translation;
- migration realism and measurable outcomes;
- concise architect-level communication.

A strong answer connects every control to a failure mode and operational owner.

Return to the [module overview](index.md) when ready to continue.
