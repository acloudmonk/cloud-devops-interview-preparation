# Scenario Questions and Model Answers

[← Module overview](index.md) · [Scenario answer framework](../interview-playbook/scenario-answer-framework.md)

Answer with outcome, actor, contract, trust, policy, failure, owner, evidence, and
residual risk. Product names support the decision; they are not the answer.

## 1. A mobile client retries and creates duplicate orders

**Model answer:** Confirm timeout and prior-outcome ambiguity. Add a client-generated,
principal-scoped idempotency key, request fingerprint, atomic stored outcome, retention,
and conflict rule. Return the original result, test concurrent retries, and measure
duplicate prevention without hiding downstream non-idempotent effects.

## 2. Leadership requests one API for every consumer

**Model answer:** Start from journeys and compatibility, not uniformity. Keep one
capability model where semantics align, but use consumer-specific façade or query
patterns when latency, aggregation, trust, or lifecycle differs. Avoid duplicating
business invariants and assign contract owners.

## 3. A partner wants password grant because it is simple

**Model answer:** Do not collect user passwords in the client. Determine whether the
actor is a user or workload, then use authorization code with PKCE, client credentials,
or federation as appropriate. Provide migration support and disable the legacy grant
with observed-use evidence.

## 4. A valid JWT accesses another tenant’s invoice

**Model answer:** Treat it as broken object-level authorization. Contain the route,
preserve token metadata and decision logs without leaking tokens, enumerate affected
objects, and notify owners. Bind issuer, subject, trusted tenant, action, and resource
on every access; test cross-tenant IDs and caches.

## 5. Signing keys rotate and half the services reject tokens

**Model answer:** Stabilize with approved overlap or rollback, not signature bypass.
Inspect issuer metadata, key IDs, caches, algorithms, clocks, and refresh failures.
Use published discovery/JWKS, bounded caching, overlap, alerting, staged rotation,
and a rehearsal that includes stale and isolated consumers.

## 6. The identity provider is unavailable but API servers are healthy

**Model answer:** Separate new authentication, token refresh, existing access-token
validation, session, and authorization dependencies. Continue only operations whose
cached trust and staleness risk are acceptable; fail closed for sensitive changes.
Communicate degraded capability and test recovery/reconciliation.

## 7. Teams put all authorization in the gateway

**Model answer:** Keep coarse authentication, audience, route, and scope checks at the
gateway, but enforce object, tenant, state, and business permission near authoritative
data or a policy decision point. Prevent internal bypass and correlate both decisions.

## 8. GraphQL reduces calls but the database saturates

**Model answer:** Attribute cost by operation, field, resolver, tenant, and consumer.
Add persisted/allowlisted operations where suitable, depth/complexity and timeout
limits, batching/data loaders, quotas, caching, and resolver SLOs. Protect expensive
authorization and preserve partial-error semantics.

## 9. A webhook secret is exposed

**Model answer:** Rotate with a short overlap, block or investigate abused deliveries,
and preserve send/receive evidence. Sign raw body plus timestamp/key ID, reject stale
replay, queue processing after quick acknowledgement, support delivery history, and
scope secrets per endpoint or tenant.

## 10. SCIM disables users hours after termination

**Model answer:** Establish the authoritative termination event and required latency.
Revoke active sessions/refresh paths for high risk, reconcile directory and application
state, and inspect mapping failures. Add provisioning SLOs, event/health monitoring,
immutable identifiers, retries, dead-letter handling, and periodic reconciliation.

## 11. CI in another cloud needs AWS access

**Model answer:** Federate the external workload assertion into a narrowly scoped AWS
role; bind issuer, subject, audience, repository/workflow/environment, and session.
Avoid stored access keys, separate deployment stages, log exchanges and actions, and
test that assertion replay from another context fails.

## 12. Business asks for immediate token revocation

**Model answer:** Explain that self-contained access tokens remain valid until expiry
unless every resource uses introspection or a deny mechanism. Balance short lifetime,
refresh rotation, session revocation, high-risk deny lists, latency, availability, and
privacy. Define the actual containment objective and measure it.

## 13. A breaking API version still has one consumer

**Model answer:** Verify real traffic, business owner, criticality, and migration
blocker. Provide compatible adaptation or supported migration, communicate deadline,
and grant only owned time-bound exception. Retire after observed zero use, preserving
rollback and audit rather than silently running forever.

## 14. Support engineers need customer impersonation

**Model answer:** Prefer delegated support action over credential impersonation.
Require case, approval or just-in-time privilege, tenant/user scope, visible banner,
prohibited operations, short session, reason, and immutable evidence. Notify where
appropriate and review anomalous or repeated access.

## 15. Multi-cloud teams demand identical identity products

**Model answer:** Standardize actor taxonomy, assurance, token/claim contract, policy
intent, evidence, recovery, and exception handling. Map AWS, Azure, and Google native
identity mechanisms where semantics differ. Forced product symmetry can add secrets,
availability dependencies, and weaker authorization.
