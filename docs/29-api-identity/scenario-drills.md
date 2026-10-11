# Advanced Trust-Boundary Drills

[← Module overview](index.md) · [Scenario questions](scenarios.md)

Use five minutes per drill. State impact, facts, containment, trust decision, evidence,
recovery, communication, reconciliation, and prevention.

## 1. An authorization policy deploy denies every customer

Stop rollout, restore the last reviewed policy, and preserve policy/version/decision
evidence. Separate bad policy from missing attributes or decision-service failure,
validate critical journeys, then add shadow evaluation, canary tenants, deny-delta
alarms, rollback ownership, and safe emergency authorization.

## 2. A token issuer signs with an unexpected algorithm

Reject outside the explicit algorithm and issuer policy; do not accept whatever the
token declares. Preserve header and metadata safely, inspect discovery/key compromise
or configuration drift, contain affected clients, rotate trust if needed, and add
algorithm allowlists plus change alerts.

## 3. A partner redirect URI was changed maliciously

Disable the client or redirect, revoke affected grants/sessions, and preserve client
registration and administrator evidence. Identify codes or tokens exposed, notify
owners, restore exact approved redirect matching, strengthen privileged change control,
and alert on redirect or credential modifications.

## 4. The authorization service exceeds its latency budget

Protect the critical API with bounded deadlines and explicitly approved cached
decisions only where stale access is safe. Segment dependency, datastore, policy,
tenant, and rule cost; shed noncritical work, scale or simplify hot paths, and verify
that performance changes preserve deny semantics.

## 5. A wildcard workload trust policy is exploited

Revoke or narrow the trust, isolate the workload, disable downstream sessions where
possible, and enumerate actions from exchange and resource logs. Replace wildcard
issuer/subject matching with exact repository, environment, service account, audience,
and permission boundaries; test replay from untrusted contexts.

## 6. A GraphQL introspection endpoint reveals sensitive structure

Assess whether schema exposure enabled exploit or sensitive field discovery; do not
assume disabling introspection fixes authorization. Restrict production introspection
where justified, remove unsafe fields, enforce field/object policy and query limits,
rotate exposed secrets, and test unauthorized graph traversal.

## 7. Webhook retries create repeated refunds

Pause the affected consumer action, identify delivery IDs and business effects, and
reconcile the authoritative ledger. Store event identity and processing outcome
atomically, make the refund transition idempotent, preserve signed replay evidence,
and test timeout-after-success plus out-of-order delivery.

## 8. SCIM group mapping grants administrators unexpectedly

Disable the mapping and privileged sessions, preserve source attributes and mapping
changes, then enumerate access granted. Restore reviewed role assignment, separate
identity attribute from privileged authorization, add approval and negative tests,
and reconcile every tenant before resuming provisioning.

## 9. A JWKS endpoint is unavailable during rotation

Use still-valid cached keys within documented bounds and fail closed for unknown keys;
never disable verification. Restore discovery through the independent path, inspect
rotation timing and cache headers, validate recovery, then rehearse overlap, stale
cache, unknown-key, and clock-skew cases.

## 10. Break-glass access leaves no audit trail

End the session, preserve infrastructure and provider evidence, and determine every
action taken. Reconcile changes to source and normal policy, rotate emergency material,
and replace opaque access with short-lived named identity, approval, narrow scope,
independent logging, notification, and scheduled exercise.

## Self-review

- Did I distinguish credential validity from permission and business correctness?
- Did I identify authoritative identity, tenant, resource, and policy data?
- Did I protect recovery paths without silently failing open?
- Did I preserve evidence without storing reusable credentials?
- Did I convert the incident into a tested platform or governance improvement?
