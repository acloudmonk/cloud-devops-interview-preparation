# Environment and Repository Architecture

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Repository and state topology should follow ownership and failure domains. There is no
universally correct monorepo, multi-repo, directory, workspace, or stack pattern.

## Start with boundaries

For every root configuration identify:

- business capability and accountable owner;
- cloud organization/account/subscription/project and region;
- environment and data classification;
- credentials and maximum permitted actions;
- state/backend and execution queue;
- upstream/downstream contracts;
- change cadence, SLO, maintenance window, and recovery objective.

## Repository choices

| Model | Strength | Main risk | Best fit |
| --- | --- | --- | --- |
| Monorepo | atomic review, shared standards, discoverability | broad CI impact and permissions | related roots with common governance |
| Repository per platform/domain | clear ownership and access | cross-repo coordination | independently operated capabilities |
| Repository per environment | strong isolation | duplicated code and promotion drift | exceptional regulatory separation |

Repositories do not provide the state boundary by themselves. A single repository can
contain many independently locked roots; separate repositories can still share a
dangerously broad execution identity.

## Environment strategies

Prefer the same versioned module contract promoted with environment-specific inputs.
Avoid copying entire configurations between development and production. Separate roots
and state are usually appropriate when environments have separate accounts, credentials,
approvals, or blast radius.

CLI workspaces provide multiple state instances for one configuration. They are useful
when instances are structurally similar and governance is simple; they are not a general
security boundary. HCP Terraform workspaces are execution/state/governance objects and
should not be confused with CLI workspaces.

## AWS-first topology

A common enterprise hierarchy is:

```text
organization foundations
├── identity and security accounts
├── network/shared-services accounts
└── workload accounts
    ├── non-production regions
    └── production regions
```

Do not automatically put the whole hierarchy in one root. Organization policy, network
foundations, clusters, data services, and application infrastructure often have different
owners and change rates. Exchange small explicit contracts rather than whole-state read
access.

## Azure and GCP translation

- Azure boundaries include tenant, management group, subscription, resource group, and
  region; provider aliases and subscription-scoped identity require deliberate design.
- GCP boundaries include organization, folder, project, and region/zone; service-account
  impersonation and project APIs are part of the dependency model.
- Across clouds, use separate provider configurations and platform-specific modules.
  Share policy intent, naming rules, and workflow controls where semantics truly match.

## Promotion

Promote an immutable module/provider selection and reviewed configuration revision.
Generate a new plan against each target's current state. Never promote a plan file across
accounts, regions, environments, or time windows.

## Dependency orchestration

Use a DAG of independently owned roots only when contracts and failure behavior are
clear. Avoid a master pipeline that can apply every environment with one credential.
For enterprise fan-out, limit concurrency, expose per-root status, stop on risk signals,
and support partial rollout and pause.

## Decision test

If two resources must share credentials, approval, maintenance window, rollback decision,
and change together, the same root may be reasonable. If those differ materially, split
the state and establish an explicit interface.
