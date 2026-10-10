# Zero Trust Rapid-Fire Revision

[← Module overview](index.md) · [Active-recall flashcards](flashcards.md)

Answer each in one or two sentences, then add assumptions or trade-offs when asked.

1. **What is Zero Trust?** An architecture and operating model that removes
   implicit trust and makes explicit, least-privilege, resource-focused decisions.
2. **Does it mean trust nothing?** No; it means confidence must come from relevant
   evidence and remain bounded, revocable, and observable.
3. **What is a protect surface?** A bounded set of important data, applications,
   assets, services, or transactions receiving focused controls.
4. **What is implicit trust?** Access accepted because of location, prior entry,
   group membership, or another fact not sufficient for the current action.
5. **What are the three common principles?** Verify explicitly, use least
   privilege, and assume breach.
6. **Policy decision point?** The component that evaluates request context against policy.
7. **Policy enforcement point?** The component that allows, constrains, or denies the request.
8. **Policy information point?** A source of identity, posture, resource, or risk signals.
9. **Authentication versus authorization?** Authentication establishes subject
   evidence; authorization decides whether an action on a resource is allowed.
10. **Why is MFA insufficient?** It does not remove excess privilege, authorize
    each action, prevent stolen sessions, or limit lateral movement.
11. **Why prefer phishing-resistant MFA?** It resists credential replay and fake
    verifier attacks better than passwords, SMS, or one-time codes.
12. **What does federation improve?** Central lifecycle and short-lived access,
    while creating a critical IdP and signing-trust dependency.
13. **What is JIT access?** Privilege granted for a bounded need and time rather
    than standing permanently.
14. **What is JEA?** Just-enough access limits actions and resources, complementing JIT duration.
15. **RBAC strength?** It is understandable and maps well to stable job functions.
16. **RBAC weakness?** Role explosion and permission accumulation obscure effective access.
17. **ABAC strength?** It scales contextual decisions using subject and resource attributes.
18. **ABAC weakness?** Bad ownership, stale attributes, or complex rules make decisions unsafe.
19. **What is ReBAC?** Authorization based on relationships such as owner, member,
    tenant, parent, or delegated user.
20. **How should risk scoring be used?** Primarily to challenge or restrict within
    declarative boundaries, not invent new access.
21. **Is a managed device trusted?** No; management supplies useful posture signals
    but does not prove absence of compromise.
22. **What is continuous evaluation?** Reconsidering a session when meaningful
    identity, device, behavior, or resource context changes.
23. **What is a safe posture outage response?** A resource-specific deny, reduced
    capability, bounded stale state, or monitored emergency path.
24. **Why protect sessions?** A stolen valid session can bypass initial authentication.
25. **Why use short-lived tokens?** They reduce replay windows and standing
    credential value, provided renewal and revocation are reliable.
26. **What should a token verifier check?** Signature, issuer, audience, subject,
    time, intended use, and protocol-specific replay controls.
27. **What is workload identity?** A verifiable identity bound to running software
    and platform context, used for authorization.
28. **Why avoid shared service accounts?** They destroy attribution, expand blast
    radius, and make rotation and least privilege difficult.
29. **What does mTLS prove?** Possession of a certificate from accepted trust and
    transport protection—not application intent or image safety.
30. **What does a service mesh add?** Standardized service identity, encryption,
    coarse policy, and telemetry at the traffic layer.
31. **Why is mesh not enough?** Business, tenant, and data authorization still
    require destination-aware policy.
32. **What is microsegmentation?** Dividing and controlling reachable paths to
    reduce unnecessary communication and lateral movement.
33. **Is private connectivity authorization?** No; it reduces exposure but does
    not establish who may perform which action.
34. **Why replace subnet VPN access?** Application-specific access narrows the
    reachable surface and improves per-resource policy and evidence.
35. **What is a data perimeter?** Broad guardrails restricting sensitive resources
    to expected identities, resources, networks, and service paths.
36. **What is the confused deputy problem?** A privileged service is tricked into
    using its authority for an unintended caller or resource.
37. **Secret manager versus workload identity?** A manager secures secret lifecycle;
    workload identity can avoid distributing reusable secrets.
38. **Why are short-lived certificates useful?** They reduce stale identity and
    revocation dependence, but make issuance availability critical.
39. **What must credential rotation prove?** New issuance and adoption, old
    disablement, observed failures, and controlled rollback.
40. **What is break-glass?** Strongly controlled, monitored emergency authority
    independent enough to recover from normal-control failure.
41. **Should every error fail closed?** Not universally; decide by resource risk,
    safety, recoverability, and available reduced capability.
42. **What makes policy observable?** Logged inputs, policy version, decision,
    enforcement result, identity, resource, action, and correlation.
43. **How should policy change ship?** Versioned review, automated positive and
    negative tests, simulation, canary, rollback, and separated recovery authority.
44. **What should an exception contain?** Scope, owner, risk, compensating control,
    evidence, expiry, and removal criteria.
45. **Where should adoption start?** With valuable bounded transactions, identity
    and asset hygiene, owners, current flows, and measurable risk.
46. **Why observe before enforce?** To learn legitimate dependencies and policy
    defects without normalizing permanent non-enforcement.
47. **How is success measured?** Reduced access exposure and containment time with
    acceptable business task success and control reliability.
48. **Is product deployment a maturity measure?** No; capability coverage,
    decision quality, recovery, and outcomes matter.
49. **How do clouds differ?** They expose different identity hierarchies, policy
    languages, enforcement boundaries, limits, and evidence semantics.
50. **Best interview closing question?** Which implicit trust are we removing,
    which evidence replaces it, and how do we recover when that evidence fails?

Return to the [module overview](index.md) when ready to continue.
