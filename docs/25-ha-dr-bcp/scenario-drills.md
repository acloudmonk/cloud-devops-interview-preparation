# Advanced Recovery Drills

[← Module overview](index.md) · [Scenario questions](scenarios.md)

Use five minutes per drill. Do not jump directly to a cloud service. Establish
impact, facts, command, safe containment, recovery choice, validation,
communication, failback, and durable improvement.

## Drill 1 — Regional symptoms with uncertain cause

Customers see intermittent failures, provider status is green, and replication
lag is increasing. Decide when to declare, what evidence is sufficient, whether
to degrade or fail over, and which action becomes irreversible.

## Drill 2 — Corrupt release replicated everywhere

The latest application and schema change reached both Regions. Backups are intact,
but older application versions cannot read the schema. Protect new transactions,
choose a compatible recovery point, and propose safer change controls.

## Drill 3 — Recovery Region quota exhaustion

Warm standby starts scaling but compute and public-address quotas block capacity.
Provide an immediate minimum-service response, escalation path, customer policy,
and preventive quota/capacity evidence.

## Drill 4 — Backup administrator compromised

An attacker has production and backup-console access. Explain isolation boundaries,
credential containment, immutable copies, clean-room recovery, forensic needs,
and who authorizes restoration.

## Drill 5 — DNS failover is only partially effective

Some clients move while corporate resolvers and mobile applications remain pinned
to primary. Address caching, alternate entry, client behavior, communication,
monitoring, and how the next design reduces dependence on emergency DNS changes.

## Drill 6 — Primary returns after secondary accepts writes

The old primary contains transactions absent from secondary; secondary contains
new post-failover transactions. Fence both sides safely, choose authority, reconcile
by business semantics, and plan controlled failback.

## Drill 7 — Identity provider and emergency channel fail

Normal workforce identity and the primary chat system are unavailable. Explain
pre-provisioned emergency roles, strong authentication, logging, alternate contact
trees, least privilege, expiry, and later access review.

## Drill 8 — Payment supplier outage during peak demand

Cloud systems are healthy, but authorization is unavailable. Choose queue, retry,
alternate supplier, degraded checkout, or refusal based on duplicate-charge and
customer harm. Include backlog control and reconciliation.

## Drill 9 — Pandemic or facility loss reduces staff

Both cloud Regions are available, but half the recovery team and a call center are
unavailable. Apply succession, minimum staffing, cross-training, remote access,
work prioritization, supplier support, and business workarounds.

## Drill 10 — Exercise itself causes production impact

A failover test routes production traffic to an undersized standby. Stop safely,
restore service, communicate, preserve evidence, and improve experiment bounds,
prechecks, abort criteria, approvals, and capacity validation without abandoning tests.

## Self-review prompts

- Did I name the customer and business consequence?
- Did I separate containment, continuity, recovery, and return to normal?
- Did I protect integrity and security while pursuing RTO?
- Did I identify authority, communication cadence, and decision records?
- Did I verify recovery with business transactions and actual data state?
- Did I leave an owned, testable improvement rather than “be more careful”?

Return to the [module overview](index.md) when ready to continue.
