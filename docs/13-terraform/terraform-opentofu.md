# Terraform and OpenTofu Decision Guide

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Terraform is the primary vocabulary in this module because it remains the most broadly
recognized interview and enterprise reference point. OpenTofu shares the historical HCL,
provider, module, workflow, and state foundations but is an independently governed tool.
Treat compatibility as something to verify, not a permanent guarantee.

## Shared foundation

Both tools center on declarative configuration, providers, dependency graphs, modules,
plan/apply, state, backends, imports, and lifecycle operations. Most architecture lessons
in this module apply to both. Use the selected tool consistently within a root and pin its
version in automation.

## Decision matrix

| Dimension | Terraform | OpenTofu | Question to ask |
| --- | --- | --- | --- |
| Governance/license | HashiCorp product and licensing model | Linux Foundation project and open-source model | What are legal/procurement requirements? |
| Managed platform | HCP Terraform and Terraform Enterprise integration | third-party/self-managed automation ecosystem | Which execution/governance service is required? |
| Registry/ecosystem | Terraform Registry and vendor ecosystem | OpenTofu Registry with broad provider/module compatibility | Which dependencies are certified and supported? |
| Product features | Terraform CLI plus HCP-specific capabilities such as Stacks | independently developed CLI capabilities, including state/plan encryption | Which feature is materially required? |
| Support | HashiCorp and partners | community and commercial vendors | Who owns production escalation? |
| Compatibility | source of current Terraform formats/behavior | aims for practical configuration/provider compatibility | What exact versions and features were tested? |

Do not choose solely from ideology or name recognition. Evaluate operating service,
support, compliance, ecosystem dependencies, feature needs, team skills, upgrade path,
and exit cost.

## Terraform-specific coverage

- HCP Terraform/Enterprise remote execution, state, projects, teams, policy, agents,
  private registry, audit, and run tasks.
- Terraform Stacks as a distinct HCP-oriented component/deployment model.
- HashiCorp-specific support, licensing, release, and registry assumptions.

Do not call HCP Terraform workspaces or Stacks portable OpenTofu abstractions.

## OpenTofu-specific coverage

- Linux Foundation governance and OpenTofu release/support ecosystem.
- OpenTofu Registry behavior and dependency resolution.
- Client-side state and plan encryption and its key/provider lifecycle.
- Features that diverge from Terraform language or evaluation behavior.

Encryption adds key-management and recovery dependencies. Losing encryption metadata or
keys can make state unusable; it does not remove the need for backend access controls.

## Migration principles

1. Inventory tool versions, providers, modules, backends, automation, policy, and features.
2. Back up configuration and every relevant state version.
3. Read the exact migration and state-compatibility guidance for both versions.
4. Test initialization and a no-change plan in an isolated, representative workflow.
5. Avoid enabling tool-specific features until rollback requirements are satisfied.
6. Migrate interdependent roots in a documented dependency order.
7. Update runner binaries, caches, commands, policy, documentation, and support ownership.
8. Canary, verify, and record an exit decision.

Never alternate binaries casually against production state. A tool may read another's
state while writing fields or using features the reverse path cannot safely consume.

## Interview answer

“I use Terraform as the default interview vocabulary, but I evaluate Terraform and
OpenTofu independently. The shared model makes skills portable; managed-platform needs,
governance, support, specific features, and tested state compatibility decide the tool.
I pin one tool per root and require a rehearsed migration before claiming portability.”
