# Scenario Questions and Model Answers

[← Module overview](index.md) ·
[Scenario answer framework](../interview-playbook/scenario-answer-framework.md)

Answer each question aloud before reading the model answer. State assumptions,
business impact, failure boundary, decision, controls, trade-offs, validation,
ownership, and residual risk.

## 1. Every application owner requests Tier 0

**Model answer:** Run a BIA by business service and impact over time. Define minimum
acceptable service, MTPD, RTO, RPO, workload recovery time, dependencies, and
approval. Group services into a small number of costed tiers, sequence shared
foundations first, and require a risk owner to approve exceptions. “Critical”
without quantified consequence is not a recovery requirement.

## 2. A Multi-AZ application is described as disaster-ready

**Model answer:** Multi-AZ primarily addresses localized infrastructure failure
inside a Region. Test regional, identity, data-corruption, deployment, and account
failure separately. Add an objective-driven regional strategy, independent data
protection, replicated artifacts/configuration, emergency access, dependency
readiness, activation authority, and exercises. Preserve Multi-AZ because DR does
not replace routine availability.

## 3. The business demands zero RPO across two Regions

**Model answer:** Clarify whether any lost acknowledged transaction is unacceptable
and whether temporary unavailability is preferable. Synchronous distance adds
latency and correlated availability risk; asynchronous replication creates loss
exposure. Consider a globally consistent database only if workload semantics,
latency, Region support, and cost fit. Otherwise use a single writer, measured lag,
idempotent intake, durable queues, reconciliation, and explicit residual-risk approval.

## 4. Route 53 health checks can automate regional failover

**Model answer:** Endpoint health is insufficient for a stateful irreversible
promotion. Combine end-to-end service health, outage scope, replication lag,
recovery capacity, security state, and primary fencing. Automate safe traffic
actions but gate database promotion where ambiguity remains. Test client DNS
caching, TTL, resolver behavior, false positives, and rollback/failback.

## 5. Backups are green, so recovery is compliant

**Model answer:** Job success proves copy creation, not recoverability. Verify
catalog and key access, isolated restore, application consistency, dependency
order, data integrity, performance, business validation, actual RPO/RTO, and
reconciliation. Test representative and largest data sets, retain evidence, and
track failed restores as risk.

## 6. Ransomware affects production and replicated data

**Model answer:** Do not perform ordinary failover into a possibly compromised
environment. Contain access, preserve evidence, identify a trusted point, establish
clean identity/network controls, restore immutable isolated copies in a clean room,
scan and validate, rotate credentials, reconcile transactions, and reopen in waves.
Coordinate security incident response, DR, crisis leadership, legal, and communications.

## 7. Warm standby cannot handle production load

**Model answer:** That can be valid only if scale-up completes within measured RTO.
Pre-establish quotas, IP capacity, images, configuration, dependencies, and load
tests. Define minimum service during scale-up, prioritize traffic, and use admission
control. If scale-up evidence misses the objective, fund more baseline capacity or
renegotiate the target.

## 8. Failover succeeds but customers cannot sign in

**Model answer:** Treat identity as a critical dependency in the service graph.
Check federation endpoints, redirect URIs, certificates, secrets, conditional
access, network paths, DNS, emergency administration, and tenant/provider impact.
Pre-register recovery endpoints and test real sign-in flows. Provide only approved
degraded access; never bypass authentication to meet RTO.

## 9. Two Regions accepted conflicting writes

**Model answer:** Stop further divergence, choose or establish an authoritative
writer, preserve logs, quantify affected entities, and use domain-aware conflict
resolution rather than timestamp-only last-write-wins. Reconcile money and inventory
with business owners, communicate impact, and redesign fencing, ownership, IDs,
idempotency, or partitioning before re-enabling multi-writer behavior.

## 10. The primary Region recovers during DR activation

**Model answer:** Avoid oscillation. The recovery commander should compare progress,
data state, confidence, and remaining RTO. Once stateful promotion crosses a defined
point of no return, complete recovery unless the plan specifies safe abort. Fence
the old primary, stabilize service, and plan controlled failback after reconciliation.

## 11. A supplier has no usable recovery evidence

**Model answer:** Assess business impact, contractual commitments, concentration,
data portability, and exit time. Add monitoring, timeouts, queuing, degraded mode,
manual or alternate supplier paths, cached/reference data where safe, and tested
contacts. Record accepted residual risk; a contract is not a technical control.

## 12. A quarterly DR test meets RTO but loses more data than RPO

**Model answer:** Record the test as an objective failure. Determine whether lag,
backup interval, promotion point, or measurement caused it. Protect affected
transactions, improve replication/backup and lag alarms, retest, and require the
risk owner to accept any temporary gap. Do not average the failed result away.

## 13. Leadership proposes multi-cloud for every critical service

**Model answer:** Identify the provider-level risk the requirement addresses and
compare it with single-provider multi-Region capability. Include data consistency,
identity, networking, skills, security, feature parity, observability, testing,
and duplicated delivery cost. Use multi-cloud only where reduced concentration
risk outweighs operational complexity and both paths can be exercised continuously.

## 14. The recovery runbook contains console screenshots and credentials

**Model answer:** Remove secrets immediately and rotate any exposed value. Replace
fragile screenshots with version-controlled intent, verified commands or automation,
expected evidence, safe checkpoints, role-based emergency access, and provider-doc
references. Assign an owner, review trigger, test date, and offline or out-of-band
availability appropriate to the threat model.

## 15. Technology is restored but the business remains unavailable

**Model answer:** RTO must stop at an agreed business service level, not server
startup. Include work recovery time, staffing, supplier readiness, validation,
manual backlog, reconciliation, fraud/privacy controls, communications, and return
to normal. Update the BIA and dependency map, then exercise business users with
the technical recovery team.

Return to the [module overview](index.md) when ready to continue.
