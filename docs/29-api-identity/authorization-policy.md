# Authorization and Policy

[← Identity protocols](identity-protocols.md) · [Next: Workload identity →](workload-federation.md)

Authorization evaluates **principal, action, resource, context, and policy**. A valid
token establishes inputs; it does not prove permission to every object.

## Models

- **RBAC:** roles group permissions; simple until role explosion and exceptions grow.
- **ABAC:** attributes support contextual rules; depends on trustworthy, current data.
- **ReBAC:** relationships such as owner or member support sharing graphs; graph
  consistency and traversal cost matter.
- **Policy as code/service:** central language and evidence; adds availability,
  latency, schema, rollout, and emergency-dependency concerns.

Combine models deliberately. Coarse scopes can admit a request to an API while
resource-level policy checks tenant, ownership, state, purpose, device, or risk.

## Decision contract

Define policy version, input schema, missing/unknown behavior, deny precedence,
decision reason, evidence retention, cache key and lifetime, revocation expectation,
and owner. Default deny is insufficient if identifiers are confused or resource
context is incomplete.

## Multi-tenant safeguards

Derive tenant context from trusted identity and resource data—not a caller-controlled
header alone. Scope every query and cache, test cross-tenant identifiers, protect
support impersonation, and audit delegated administration. Separate platform role,
tenant role, object relationship, and commercial entitlement.

## AWS anchor and translation

AWS IAM evaluates AWS resource authorization; Amazon Verified Permissions uses Cedar
for application permissions. Azure role-based access control and Microsoft Entra
app roles/scopes, plus Google Cloud IAM and conditional bindings, solve related but
not identical layers. Preserve common policy intent while retaining native semantics.

## Change safety

Test allow and deny cases, shadow-evaluate policy, canary by tenant, record decision
deltas, support rollback, and require expiring exceptions. Measure denied legitimate
work, unintended access, decision latency, coverage, and stale data.
