# Advanced Distributed-Estate Drills

[← Module overview](index.md) · [Scenario questions](scenarios.md)

Use five minutes per drill. Cover impact, facts, command, containment, data/trust,
recovery, communication, reconciliation, and prevention.

## 1. An on-premises route leak reaches two clouds

Stop propagation at the nearest trusted boundaries, preserve BGP and change
evidence, and identify affected prefixes before changing advertisements. Restore
explicit approved routes, validate asymmetric paths and inspection, then add
prefix filters, maximum-prefix limits, route ownership, staged changes, and a
rehearsed rollback.

## 2. A DNS forwarding loop causes intermittent failures

Trace one failing name through client caches, conditional forwarders, private
zones, resolvers, and authoritative servers. Break the loop without creating a
split-brain answer, lower stale-cache risk, and publish ownership. Prevent repeat
failure with an acyclic resolution design, query telemetry, synthetic tests, and
controlled zone changes.

## 3. A cross-cloud gateway certificate expires at peak demand

Confirm the affected trust path and whether traffic can fail over safely. Issue
and deploy a validated replacement through the approved emergency process; do
not disable authentication. Verify both peers, revoke superseded material, and
add inventory, ownership, expiry alerting, automated rotation, and a tested
overlap period.

## 4. Link loss creates a dangerous replication backlog

Protect the authoritative system and storage headroom first. Classify traffic by
business criticality, apply producer backpressure or controlled shedding, and
preserve ordering and idempotency metadata. Restore capacity gradually, monitor
age rather than count alone, reconcile duplicates and gaps, and revise offline
capacity and recovery forecasts.

## 5. A compromised pipeline makes signed artifacts suspect

Pause promotion across every environment, revoke build and signing authority,
and preserve repository, runner, identity, transparency, and deployment evidence.
Enumerate artifacts and consumers from the compromise window, quarantine or
roll back by risk, rebuild on trusted infrastructure, re-attest, and separate
future source, build, signing, and deployment trust.

## 6. Offline factories produce conflicting event times

Do not order business events solely by wall-clock timestamp. Preserve local
sequence, device identity, source offset, ingestion time, and domain version;
apply the documented conflict rule when sites reconnect. Repair time
synchronization, quantify affected decisions, replay idempotently, and test long
disconnection plus clock-jump scenarios.

## 7. Two “diverse” carrier links share one physical metro

Declare the common-mode dependency and move critical traffic to an independent
path or safe local mode. Prioritize essential journeys and communicate reduced
capacity. Validate carrier maps and demarcations, redesign physical and provider
diversity, add out-of-band access, and test loss of the shared facility rather
than only logical circuit failover.

## 8. A provider control-plane API is unavailable

Keep stable workloads serving through the data plane and freeze nonessential
changes. Use pre-provisioned capacity, cached configuration, bounded queues, and
documented local authority; avoid frantic cross-cloud migration. Monitor resource
headroom and expiring dependencies, then reconcile desired state after recovery
and test how long the platform can operate without control-plane mutation.

## 9. An acquisition creates an identity collision

Stop or scope the affected federation before another incorrect authorization.
Use immutable issuer-plus-subject identifiers rather than email or display name,
review sessions and grants, and notify affected owners. Build an explicit account
linking and exception process, separate authentication from authorization, and
test duplicate, renamed, disabled, and re-hired identities.

## 10. A provider-exit rehearsal misses its objective

Treat the rehearsal as evidence, not a paperwork failure. Measure missing data,
format incompatibility, transfer time, target capacity, feature gaps, operating
skills, and contract constraints. Fix the highest-risk bottlenecks, retest a
representative workload, update cost and elapsed-time assumptions, and escalate
any residual gap to the owner who accepts exit risk.

## Self-review

- Did I protect customer/safety outcome before restoring architecture symmetry?
- Did I identify common-mode identity, DNS, carrier, CI/CD, and operator dependencies?
- Did I state authoritative data and reconciliation behavior?
- Did I preserve native evidence while using one incident command?
- Did I turn a recurring gap into a platform, contract, or governance improvement?

Return to the [module overview](index.md) when ready to continue.
