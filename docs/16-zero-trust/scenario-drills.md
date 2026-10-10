# Advanced Zero Trust Incident Drills

[← Module overview](index.md) ·
[Scenario answer framework](../interview-playbook/scenario-answer-framework.md)

For each drill, state first containment, evidence to preserve, affected identities
and resources, decision owner, recovery, communication, and prevention.

## 1. IdP signing key is suspected compromised

Constrain federation and high-risk access, preserve IdP and relying-party evidence,
identify accepted issuers/keys and active sessions, rotate signing trust through a
controlled overlap, revoke suspect sessions, validate every relying party, and
investigate administrator and key-management paths. Use independent emergency
access for critical operations.

## 2. A valid session bypassed phishing-resistant MFA

Revoke the session family, isolate the device/account, preserve browser, proxy,
endpoint, and application evidence, and enumerate actions. Investigate token theft
or adversary-in-the-browser behavior rather than blaming MFA. Reduce session
exposure, bind or constrain tokens where supported, and improve continuous signals.

## 3. An ABAC attribute granted cross-tenant access

Block the affected rule or resource path, preserve decision inputs and policy
versions, identify every decision made with the bad attribute, notify data owners,
and repair source plus consumers. Add authoritative ownership, schema validation,
missing-value behavior, negative tenant tests, and staged policy deployment.

## 4. EKS pods used the node role to read unrelated data

Remove the unintended permission/path, isolate affected nodes and pods, preserve
tokens and CloudTrail/runtime evidence, identify accessed data, and rotate exposed
credentials. Adopt pod-specific roles, restrict metadata, narrow resource policy,
add network controls, and test that node credentials are unreachable.

## 5. The identity-aware proxy fails across a region

Protect control-plane changes, invoke the documented resource-specific degraded
mode, route to a healthy region where safe, and provide monitored emergency access
for essential work. Do not expose origins broadly. Reconcile cached decisions and
sessions after recovery, then test regional dependency and capacity assumptions.

## 6. A policy rollout denies all production responders

Rollback to the last verified policy using separated authority, activate tightly
scoped break-glass if needed, preserve deployment and decision logs, and restore
incident access. Add simulation, canary enforcement, independent recovery roles,
policy health checks, and a rule preventing one change from disabling all recovery.

## 7. Private CA issued unauthorized workload certificates

Stop suspect issuance, isolate the registration authority, preserve CA and
workload evidence, enumerate certificates and accepted trust domains, revoke or
replace trust, reissue legitimate identities, and verify every enforcement point.
Repair issuance authorization and protect CA administration and keys.

## 8. A contractor remained active after departure

Disable identities and sessions, identify every linked account, role, device,
token, key, and action since the end date, preserve evidence, and engage resource
owners. Correct authoritative lifecycle and sponsor expiry, reconcile downstream
systems, and measure deprovisioning completion rather than IdP disablement alone.

## 9. Teams created direct paths around the access proxy

Restrict bypass routes without blocking recovery, identify who used them and why,
and preserve network/application logs. Fix DNS, security-group, load-balancer, and
origin authentication controls; improve proxy usability and availability; create
a monitored, expiring exception workflow; and continuously test alternate paths.

## 10. Risk engine labels executives as low risk despite anomalies

Do not let the score create privilege. Constrain affected sessions, inspect model
inputs, identity links, policy, and actions, and apply deterministic controls for
high-value transactions. Correct data and bias issues, validate explainability,
monitor false outcomes, and keep risk signals able to restrict—not independently
grant—access.

Return to the [module overview](index.md) when ready to continue.
