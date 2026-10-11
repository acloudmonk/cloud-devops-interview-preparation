# Control Plane and Tenant Lifecycle

[← Tenancy and isolation](tenancy-isolation.md) · [Next: Identity and authorization →](identity-authorization.md)

## Tenant catalog as authority

The catalog records stable tenant ID, display metadata, lifecycle state, placement,
tier, entitlements, identity connections, residency, encryption references, billing
account, and configuration version. Separate stable identity from mutable names and
domains. Protect catalog writes, audit every change, and expose only required fields
to data-plane services.

## Lifecycle state machine

A useful lifecycle is `requested → validating → provisioning → active → suspended →
closing → deleting → deleted`, with explicit failed and repair states. Each transition
has an owner, authorization rule, idempotency key, timeout, compensating action, and
observable evidence. Avoid a single synchronous request that partially creates
identity, infrastructure, billing, and product state.

## Onboarding workflow

1. Validate commercial order, uniqueness, region, tier, and compliance inputs.
2. Allocate immutable tenant ID and placement through policy.
3. Provision or register data-plane resources with declarative automation.
4. Configure federation, administrators, keys, quotas, and entitlements.
5. Run isolation and readiness checks before routing production traffic.
6. Activate billing and support visibility, then notify the customer.

Retries must converge. Persist workflow state and make each activity safe to repeat.
At scale, protect dependencies with bounded concurrency and admission control.

## Entitlements and configuration

Pricing plan, entitlement, feature flag, quota, and authorization are related but
not interchangeable. The billing plan describes a commercial package; entitlement
states what a tenant may use; quota limits consumption; authorization decides whether
this principal can perform this action. Centralize evaluation, version decisions,
cache with safe expiry, and audit changes. Avoid per-tenant code branches.

## Suspension and offboarding

Define reasons and effects separately: payment delinquency, security containment,
customer request, or contract end may require different access. Preserve provider
operations, export, appeal, and evidence as policy requires. Offboarding covers data
export, federation removal, secret revocation, retention hold, deletion propagation,
backup expiry, billing close, catalog tombstone, and customer proof. “Delete row” is
not a lifecycle design.

## Control-plane resilience

Prioritize lifecycle integrity over instant completion. Use durable workflows,
deduplicated commands, reconciliation, immutable audit events, and privileged break-
glass procedures. Data planes should consume signed or authenticated configuration
snapshots and keep serving within a declared staleness window when safe.
