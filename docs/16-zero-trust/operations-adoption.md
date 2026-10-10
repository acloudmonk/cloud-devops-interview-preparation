# Telemetry, Response, and Adoption

[← Module overview](index.md) · [Scenario answer framework](../interview-playbook/scenario-answer-framework.md)

Zero Trust is operational only when teams can explain decisions, detect misuse,
revoke access, recover dependencies, and improve policy. A design diagram without
these feedback loops is an access modernization project, not a durable capability.

## Minimum decision evidence

Record subject and workload identity, authentication assurance, device/posture
summary, resource and action, policy and version, decision, enforcement result,
session or request correlation, exception, and time. Minimize sensitive signal
detail and set retention from investigation, privacy, and regulatory needs.

Correlate IdP, endpoint, proxy, cloud control-plane, workload, network, data, and
application events. Normalize identities carefully; the same person or workload
may have several identifiers, sessions, roles, and delegated chains.

## Response patterns

| Event | Immediate response | Recovery question |
| --- | --- | --- |
| Stolen user session | revoke sessions, constrain access, preserve evidence | how was the session captured and replayed? |
| Workload token leak | disable trust/grant, isolate workload, trace calls | which issuer, audience, and consumers are affected? |
| Policy permits excess access | rollback or add boundary, enumerate use | why did review, testing, or ownership fail? |
| Device signal outage | invoke resource-specific degraded mode | was stale or missing posture distinguishable? |
| Certificate authority compromise | stop issuance, establish new trust, reissue | can every verifier and workload migrate safely? |

## Exceptions and emergency access

An exception needs scope, risk owner, compensating controls, evidence, expiry, and
removal criteria. Break-glass must be independent enough to survive the failed
control, tightly scoped, strongly authenticated, monitored in real time, reviewed
after use, and tested without normalizing bypass.

## Phased adoption

1. **Discover:** identify high-value resources, flows, identities, implicit trust,
   owners, incidents, and control dependencies.
2. **Stabilize:** improve identity lifecycle, phishing resistance, inventory,
   logging, ownership, and credential hygiene.
3. **Pilot:** protect one valuable, bounded transaction with measurable outcomes.
4. **Expand:** offer reusable identity, policy, proxy, workload, and evidence paths.
5. **Enforce:** move from observe to warn to deny with tested recovery.
6. **Optimize:** remove obsolete pathways, tune signals, reduce exceptions, and
   exercise incidents continuously.

## Outcome measures

Measure privileged standing access, long-lived credential count, unused grants,
protect-surface coverage, session/token lifetime, time to revoke, lateral paths,
expired exceptions, policy decision errors, false-deny rate, bypass use, identity
incident containment time, and user task success. Product deployment or MFA
coverage alone does not demonstrate reduced risk.

## Ownership

Identity teams own identity assurance and lifecycle; endpoint teams own posture;
platform teams own paved enforcement and workload identity; resource owners own
fine-grained authorization; security owns standards, threat intelligence, and
assurance; risk owners accept residual exposure. Shared accountability must not
mean ownerless policy.

Return to the [module overview](index.md) when ready to continue.
