# APIs and Enterprise Identity Flashcards

[← Module overview](index.md) · [Rapid-fire revision](rapid-fire.md)

1. **Decision chain?** Capability → consumer → interaction → contract → actor → trust → policy → operation → evidence.
2. **Contract beyond schema?** Semantics, errors, retries, auth, limits, compatibility, support, retirement.
3. **Retry-safe write?** Scoped key, request fingerprint, atomic outcome, conflict rule, retention.
4. **API-style choice?** Latency, coupling, network, scale, delivery, ordering, consumers, operation.
5. **GraphQL guardrails?** Field/object auth, depth/cost limits, batching control, resolver evidence.
6. **Webhook pattern?** Sign raw body/time/key, reject replay, acknowledge, queue, retry, reconcile.
7. **Gateway boundary?** Coarse identity/traffic policy centrally; business/resource policy near authority.
8. **OAuth/OIDC?** Delegated API authorization / authentication layer and identity claims.
9. **SAML/SCIM?** Browser federation / user and group provisioning lifecycle.
10. **Token validation?** Issuer, audience, signature, algorithm, type, time, required claims, tenant.
11. **ID/access token?** Client authentication result / resource-server authority.
12. **Refresh token?** Protected long-lived grant with rotation, reuse detection, revocation.
13. **Modern browser flow?** Authorization code with PKCE, exact redirect, state/nonce as applicable.
14. **RBAC/ABAC/ReBAC?** Roles / attributes / relationships, often combined.
15. **Authorization tuple?** Principal, action, resource, context, policy.
16. **Tenant context?** Trusted identity plus authoritative resource data, not caller header alone.
17. **Policy contract?** Inputs, version, unknown/deny behavior, reason, cache, evidence, owner.
18. **Workload identity chain?** Runtime attestation → short-lived assertion → exact trust → scoped authority.
19. **Federation trust?** Exact issuer, subject, audience, context, mapping, lifecycle, recovery.
20. **Rotation proof?** Overlap, cache refresh, isolated consumer, rollback, telemetry, rehearsal.
21. **Revocation reality?** Stop future issue and sessions; existing self-contained tokens may persist.
22. **Identity outage design?** Separate login, refresh, validation, session, policy, and safe degradation.
23. **API incident evidence?** Contract/version, request, actor, tenant, decision, dependency, outcome.
24. **Retirement proof?** Usage inventory, owner contact, migration, deadline, exception, zero traffic.
25. **Strong answer?** Journey/invariant → contract → trust/policy → failure/operation → proof/trade-off.

Review missed cards after one day, three days, and seven days.
