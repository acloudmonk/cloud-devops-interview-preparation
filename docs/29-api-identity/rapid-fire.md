# Rapid-Fire Revision

[← Module overview](index.md) · [Flashcards](flashcards.md)

Answer each aloud in under 30 seconds, then add one trade-off or failure mode.

1. **API contract?** Semantics, schema, errors, auth, limits, compatibility, and lifecycle promise.
2. **Authentication?** Evidence establishing who or what controls an identity.
3. **Authorization?** Decision whether a principal may perform an action on a resource in context.
4. **Delegation?** A client receives bounded authority to act for a user or workload.
5. **Federation?** One trust domain accepts and maps assertions from another.
6. **REST strength?** Broad HTTP interoperability and resource-oriented semantics.
7. **gRPC strength?** Typed efficient service calls and streaming with generated clients.
8. **GraphQL strength?** Consumer-shaped queries across a governed graph.
9. **Async API value?** Temporal decoupling, buffering, fan-out, and replay.
10. **Webhook invariant?** Authentic, replay-resistant delivery processed idempotently.
11. **Idempotency key?** Stable retry identity bound to principal, request, outcome, and retention.
12. **Cursor pagination?** Opaque continuation tied to deterministic ordering and filters.
13. **Breaking change?** Any change that violates a consumer’s supported semantic contract.
14. **Deprecation proof?** Owners contacted, migration supported, and observed use reaches zero.
15. **Gateway role?** Central entry routing, coarse policy, traffic protection, and evidence.
16. **Gateway anti-pattern?** Embedding all business logic and object authorization centrally.
17. **Rate limit versus quota?** Short-window traffic control versus allowed consumption over time.
18. **OAuth purpose?** Delegated authorization to protected resources.
19. **OIDC purpose?** Authentication and identity claims layered on OAuth flows.
20. **SAML purpose?** XML assertion-based enterprise browser federation.
21. **SCIM purpose?** Standardized user/group provisioning and lifecycle.
22. **JWT property?** Signed compact claims; not automatic confidentiality or authorization.
23. **ID token consumer?** The OIDC client for the stated audience.
24. **Access token consumer?** The target resource server for its audience and scopes.
25. **Refresh token risk?** Long-lived authority capable of obtaining new access tokens.
26. **PKCE value?** Binds authorization code redemption to the initiating client instance.
27. **State value?** Correlates authorization response and helps prevent request forgery.
28. **Nonce value?** Binds OIDC authentication response and helps prevent replay/substitution.
29. **Issuer check?** Prevents trusting a token from the wrong authority or tenant.
30. **Audience check?** Prevents a token issued for one resource/client being reused elsewhere.
31. **JWKS?** Published public verification keys identified by key ID.
32. **Key-rotation requirement?** Planned overlap, bounded caching, monitoring, rollback, and rehearsal.
33. **RBAC limit?** Role explosion and poor representation of resource relationships/context.
34. **ABAC risk?** Incorrect, stale, or attacker-controlled attributes drive decisions.
35. **ReBAC?** Authorization derived from relationships such as owner, member, or parent.
36. **Policy decision point?** Component evaluating inputs and policy to return a decision.
37. **Policy enforcement point?** Component that obtains and enforces the decision.
38. **Tenant invariant?** Trusted actor tenant and authoritative resource tenant must align by policy.
39. **Workload federation?** Exchange trusted runtime assertion for short-lived target authority.
40. **Static-key alternative?** Platform role, managed identity, certificate, or federated assertion.
41. **mTLS proves?** Peer possession of an accepted private key, not business permission.
42. **Token revocation limit?** Self-contained tokens may remain valid until expiry.
43. **Fail closed?** Deny when a required trustworthy authorization decision cannot be made.
44. **Safe authorization cache?** Key includes all decision inputs and staleness is risk-approved.
45. **Broken object authorization?** Valid actor accesses a resource without resource-level permission.
46. **Support impersonation safeguard?** Approved, scoped, visible, short-lived, prohibited, and audited delegation.
47. **Useful identity SLO?** Successful critical journey, not merely token endpoint uptime.
48. **API cost driver?** Requests, payload/egress, transformation, logs, policy calls, and support.
49. **Strong audit event?** Actor, client, tenant, action, resource, policy/version, result, reason, request ID.
50. **Architect closing test?** Contract, trust, policy, failure, evidence, owner, cost, and residual risk.
