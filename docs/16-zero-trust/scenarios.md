# Zero Trust Scenario Questions and Model Answers

[← Module overview](index.md) ·
[Scenario answer framework](../interview-playbook/scenario-answer-framework.md)

Answer each question aloud before reading the model. Lead with discovery,
identify the implicit trust being removed, then cover decision, enforcement,
failure, recovery, adoption, and measurable outcome.

## 1. Replace a broad remote-access VPN

**Question:** The CIO wants to remove the VPN in 90 days. What do you design?

**Model answer:** I would not begin with the deadline or a ZTNA product. I would
inventory user-to-resource flows, application protocols, device populations,
privileged paths, dependencies, and recovery needs. Pilot identity-aware access
for browser applications using federated identity, device posture, resource-level
policy, short sessions, and logs. Broker administrative and legacy access rather
than exposing subnets. Run coexistence, measure successful tasks and denied paths,
then retire VPN routes by cohort while preserving a tested emergency path.

## 2. MFA is enabled, but accounts remain overprivileged

**Question:** Is the organization now Zero Trust?

**Model answer:** No. MFA raises authentication assurance but does not correct
standing privilege, broad roles, weak resource policy, stolen sessions, or
unmonitored use. I would inventory effective access, introduce resource ownership,
separate administrator identities, move privilege to just-in-time elevation,
shorten sessions, review unused grants, and enforce action-level authorization.

## 3. Design contractor access from unmanaged devices

**Model answer:** Classify required applications, data, actions, residency, and
sponsor lifecycle. Use federated contractor identity, strong authentication,
automatic expiry, browser-only or isolated access, restricted download/copy, and
short sessions for appropriate resources. Require managed devices for higher-risk
actions. Log decisions, review sponsor ownership, and avoid unnecessary personal
device telemetry.

## 4. Protect AWS production administration

**Model answer:** Federate through IAM Identity Center, separate daily and admin
personas, use phishing-resistant authentication, and make production permission
sets narrowly scoped, approved, short-lived, and attributable. Prefer Systems
Manager or another broker over inbound SSH. Apply SCP guardrails and resource
policies, centralize CloudTrail, alert on elevation and sensitive actions, and test
independent break-glass access. SCPs bound permissions; they do not grant them.

## 5. A legacy application cannot use federation

**Model answer:** Put it behind an identity-aware gateway if protocol and trust
allow, map authenticated identity to the smallest application role, protect the
remaining service credential in a broker or vault, and log original plus mapped
identity. Segment the application and database. Time-box this compensating design,
measure usage, and fund native modernization rather than presenting the gateway
as complete application authorization.

## 6. Choose RBAC or ABAC for a global data platform

**Model answer:** I would combine them. RBAC provides understandable baseline job
functions; ABAC narrows decisions using authoritative data classification,
country, tenant, environment, and purpose attributes. I would define attribute
owners and freshness, keep policies explainable, test missing/conflicting values,
log policy versions, and require application-level tenant enforcement.

## 7. Secure EKS workloads calling AWS services

**Model answer:** Give each workload a dedicated Kubernetes service account and
map it to a narrowly scoped IAM role using EKS Pod Identity or IRSA. Constrain
trust to expected cluster/namespace/service-account context, avoid node-role
fallback, set token audience and lifetime correctly, restrict metadata access,
apply network policy and destination authorization, and trace CloudTrail actions
back to the pod identity. Rehearse issuer and role revocation.

## 8. Is service-mesh mTLS sufficient?

**Model answer:** No. It protects transport and authenticates participating
certificate identities. It does not prove image integrity, safe runtime state,
tenant ownership, business authorization, or permitted data use. Add workload
issuance controls, destination policy, application authorization, egress policy,
telemetry, certificate recovery, and supply-chain assurance.

## 9. The device posture provider is unavailable

**Model answer:** Use resource-specific failure policy. Deny privileged changes;
possibly permit read-only access using recently verified posture for a bounded
period; and provide monitored emergency access for essential operations. Detect
stale versus negative posture, communicate degradation, protect policy changes,
and test recovery. A universal fail-open or fail-closed answer ignores business risk.

## 10. Design a multi-cloud workforce model

**Model answer:** Establish one governed workforce lifecycle and primary IdP,
federate into provider-native short-lived roles, and map common job outcomes to
cloud-specific entitlements. Apply organization guardrails in each cloud,
centralize normalized evidence without losing native semantics, and govern
privileged elevation consistently. Validate differences rather than forcing
identical policy syntax or claiming service parity.

## 11. A team wants 24-hour workload tokens for reliability

**Model answer:** I would find why renewal fails, improve issuer availability and
client refresh behavior, and use bounded caching or overlapping credentials.
Longer bearer lifetime increases theft and revocation exposure. Tokens should be
audience-bound, automatically renewed, protected in memory/filesystem, and denied
outside required context. Test issuer outage and clock skew explicitly.

## 12. Build an AWS data perimeter

**Model answer:** Classify sensitive resources and expected access, then use
organization and resource policies to restrict untrusted identities, resources,
and networks using appropriate condition keys. Add fine-grained IAM, VPC endpoints,
encryption, and data-service controls. Test managed-service calls, delegated
administration, cross-account access, and confused-deputy conditions before
enforcement; monitor denied and exceptional paths.

## 13. Measure Zero Trust success

**Model answer:** Tie measures to reduced exposure and business usability: standing
privilege, long-lived credentials, unused grants, protected transactions, session
lifetime, revoke time, lateral paths, exception age, false denies, bypass use,
incident containment, policy availability, and successful user tasks. License
count, agent deployment, or MFA enrollment alone are activity metrics.

## 14. The board asks whether Zero Trust prevents breaches

**Model answer:** No architecture prevents every breach. Zero Trust reduces
implicit trust, unnecessary access, credential value, and lateral movement while
improving decision evidence and containment. I would state residual risks such as
endpoint compromise, authorized misuse, policy errors, supply-chain compromise,
and control-plane failure, then explain layered prevention, detection, response,
and recovery.

## 15. Prioritize a two-year migration

**Model answer:** Start with inventory, identity lifecycle, phishing-resistant
privileged access, logging, and credential hygiene. Select one high-value bounded
transaction for a measurable pilot. Build reusable workforce/workload identity,
policy, proxy, and evidence capabilities; migrate by risk and feasibility through
observe, warn, and enforce; time-box exceptions; exercise failures; and retire
legacy pathways only when task success and emergency recovery are proven.

Return to the [module overview](index.md) when ready to continue.
