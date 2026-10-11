# Platform Architecture

[← Product and operating model](product-operating-model.md) · [Next: Golden paths and interfaces →](golden-paths-interfaces.md)

## Logical layers

1. **Experience:** portal, CLI, API, IDE, documentation, notifications.
2. **Product/catalog:** ownership, templates, scorecards, dependencies, lifecycle.
3. **Orchestration:** workflows, approvals, state machines, reconciliation.
4. **Control:** identity, policy, quotas, tenancy, secrets, audit, cost boundaries.
5. **Resources:** cloud accounts/projects, clusters, runtimes, data, networks.
6. **Evidence:** delivery, inventory, posture, telemetry, SLO, usage, feedback.

Keep interfaces replaceable. The portal should call versioned platform APIs rather
than directly owning privileged infrastructure logic. Long-running operations need
durable state, idempotency, cancellation, status, retry, and reconciliation.

## AWS-first reference boundary

An AWS platform commonly uses federated workforce identity, a multi-account landing
zone, workload identity, IaC, governed artifact registries, delivery services,
ECS/EKS/Lambda or other runtimes, observability, service catalog metadata, and a
portal such as Backstage. The product contract matters more than one implementation.

Translate capabilities to Azure subscriptions/management groups, Entra identity,
Azure Policy and delivery/runtime services; or Google organizations/folders/projects,
Cloud IAM, Organization Policy and delivery/runtime services. Native controls,
quotas, tenancy, and managed-service behavior are not identical.

## Build, buy, compose

Buy commodity capabilities when integration and operation cost exceed differentiation.
Build the glue and contracts unique to the organization. Evaluate total lifecycle,
extension, data, identity, portability, vendor viability, and exit—not feature count.
Avoid a fragile “platform of plugins” with no ownership or compatibility strategy.

## Platform topology

Use shared services for discovery and policy where centralization helps, but bound
runtime and reconciliation blast radius with accounts, subscriptions/projects,
regions, clusters, or cells. A central control plane must not hold unnecessary
organization-wide mutation authority.
