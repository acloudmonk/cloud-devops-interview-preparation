# Resource Hierarchy and Governance

[← Global infrastructure](global-infrastructure.md) · [Next: Enterprise platform →](enterprise-platform.md)

The hierarchy is **organization → folders → projects → resources**. Policies normally
inherit downward. Projects are fundamental trust, API, quota, lifecycle, and cost
boundaries—not merely folders for resources.

Use folders for durable policy and delegation groupings. Use separate projects when
ownership, lifecycle, environment, data, quota, blast radius, or chargeback warrants
isolation. Keep the hierarchy shallow enough to explain effective policy.

## Controls are different

- **IAM allow policies** grant principals roles over resources.
- **IAM deny policies** prevent specified permissions even when an allow exists.
- **Organization Policy** constrains resource configurations and permitted behaviors.
- **Tags** provide governed metadata that some policies can target.
- **Billing accounts, budgets, and exports** support financial governance; budgets do
  not automatically cap spend.

Define project creation, API enablement, metadata, ownership, logging, network
attachment, security monitoring, exceptions, suspension, and deletion. Roll restrictive
policies through inventory, testing, staged enforcement, monitoring, and a time-bound
exception process.

Giving Owner does not solve an Organization Policy constraint, deny policy, service
perimeter, quota, or network failure. Trace each decision engine independently.
