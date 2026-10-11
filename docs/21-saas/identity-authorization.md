# Identity and Authorization

[← Control plane and lifecycle](control-plane-lifecycle.md) · [Next: Data, residency, and compliance →](data-residency-compliance.md)

## Separate identity dimensions

A principal may be a user, tenant administrator, support operator, service workload,
automation client, or external partner. A user can belong to multiple tenants with
different roles. Model provider workforce identity separately from customer identity,
and workload identity separately from both.

## Enterprise federation

Support OIDC or SAML federation through per-tenant connection metadata. Resolve the
tenant before or during authentication using a verified domain, invitation, tenant-
specific URL, or explicit organization selection. Prevent domain-claim takeover,
support key and certificate rotation, and preserve emergency access. SCIM-style
provisioning may automate users and groups, but authorization still needs application
policy and revocation behavior.

## Trusted tenant context

Tokens should carry stable subject, issuer, audience, tenant membership, and bounded
claims. The service validates signature, issuer, audience, time, and policy before
constructing immutable tenant context. Do not trust an HTTP header or request field
that can contradict the token and route. For cross-service calls, propagate the
original subject where required and use the workload's own identity for service
authorization.

## Authorization and isolation

Use role-based access for understandable job functions and attribute or relationship
policy where resource context matters. Decisions should include tenant, subject,
action, resource, tier, and environment. Enforce server-side and close to the data;
UI hiding is not authorization. Cache only with bounded lifetime and a revocation
strategy. Record decision evidence without leaking sensitive claims.

## Provider support access

Support access is a separate privileged product: just-in-time approval, tenant scope,
purpose, time limit, session evidence, sensitive-field masking, and customer-visible
audit where appropriate. Do not create a universal support bypass. Break-glass use
must be rare, alerted, reviewed, and tested.

## AWS-first capability choices

Amazon Cognito or an external identity provider can broker customer identity; IAM
roles provide workload credentials; Verified Permissions can externalize fine-grained
policy. Azure commonly uses Microsoft Entra External ID and managed identities;
Google Cloud offers Identity Platform multitenancy and workload identity. Service
names do not solve tenant binding or policy design—validate the complete trust path.
