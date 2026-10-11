# Self-Service and Control Planes

[← Golden paths and interfaces](golden-paths-interfaces.md) · [Next: Delivery and supply chain →](delivery-supply-chain.md)

## Desired-state lifecycle

Safe self-service follows **request → authenticate → authorize → validate → plan →
approve if needed → reconcile → verify → observe → update → delete**. Provisioning
without update, drift, failure, and deletion handling creates future tickets.

Use explicit schemas and asynchronous operations for long-running work. Persist
desired state, current state, operation history, and ownership. Reconciliation must
be idempotent and converge after partial failure. Do not treat a CI job as a durable
control plane when the resource lifecycle outlives the job.

## Identity and authority

Separate developer identity, platform service identity, reconciliation identity,
and workload identity. Use short-lived credentials and resource-scoped roles.
Authorize each operation from verified attributes and policy; do not pass broad
cloud credentials through plugins, templates, or user-controlled pipelines.

## Provisioning models

- **IaC workflow:** reviewed plans and clear infrastructure state; feedback may be slower.
- **Cloud service catalog:** curated products and native governance; scope can be narrow.
- **Kubernetes-style API/control plane:** composable desired state; requires controller expertise.
- **Broker/API workflow:** flexible orchestration across systems; team owns durable state.

Terraform/OpenTofu, cloud-native services, and control-plane frameworks can coexist
when state ownership is explicit. Never let two reconcilers mutate the same field
without a contract.

## Day-two operations

Every capability needs discoverable status, audit, quotas, upgrade, rotation,
backup, recovery, transfer of ownership, and deletion. Provide bounded break-glass
and a manual recovery path. Test timeout-after-success, duplicate request, provider
throttling, policy change, orphan state, and consumer cancellation.
