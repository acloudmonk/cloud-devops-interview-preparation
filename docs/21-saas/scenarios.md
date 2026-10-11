# Scenario Questions and Model Answers

[← Enterprise design exercise](design-exercise.md) · [Next: Advanced drills →](scenario-drills.md)

## 1. Leadership says SaaS requires one shared database

**Model answer:** SaaS is a unified product and operating model; multitenancy is an
architecture choice. I would discover scale, compliance, economics, and lifecycle
goals, then select pool, silo, or bridge per component. Dedicated resources can still
be SaaS when onboarding, releases, operations, and governance remain unified.

## 2. A request includes a tenant ID header

**Model answer:** I would not trust caller-controlled tenant context. Resolve tenant
from a verified route or organization selection, validate token membership, construct
immutable context, and compare all identifiers. Enforce tenant policy at API and data
boundaries and test horizontal cross-tenant access.

## 3. A regulated customer demands dedicated infrastructure

**Model answer:** Clarify dedicated compute, data, account, network, keys, telemetry,
and operations rather than accept a vague requirement. Productize the justified
boundary as a tier, automate it through the same control plane, keep one artifact,
price its cost, and document residual shared dependencies.

## 4. One tenant's export slows everyone

**Model answer:** Protect interactive paths immediately with tenant-aware concurrency,
fair queues, quotas, priority, and load shedding. Measure the actual bottleneck, then
separate bulk workers or cells where needed. Add per-tenant usage, queue-age, and
throttling evidence plus a safe export contract.

## 5. Onboarding fails after creating identity but before storage

**Model answer:** Persist a lifecycle state machine and idempotency key. Retry safe
steps, compensate resources that cannot be retained, expose a repair state, and do
not route traffic until readiness checks pass. Reconciliation should detect orphaned
identity, billing, keys, placement, and storage.

## 6. The control plane is unavailable

**Model answer:** Existing tenants should continue within declared configuration and
entitlement staleness windows. Pause unsafe lifecycle mutations, retain durable
commands, and use authenticated snapshots. Define which decisions fail closed, then
reconcile state and audit ordering when the control plane recovers.

## 7. A user belongs to two tenants

**Model answer:** Keep subject identity separate from tenant membership and role.
Require an explicit, verified active organization, issue bounded tenant context, and
make tenant switching a new authorization decision. Never infer the tenant only from
email domain or reuse cached permissions across organizations.

## 8. A customer requires European residency

**Model answer:** Map the promise across databases, replicas, backups, objects, logs,
traces, analytics, support exports, keys, third parties, and DR. Enforce placement
from catalog policy, restrict support access, test failover, and document any lawful
cross-border processing instead of equating residency with one database region.

## 9. Product wants hundreds of tenant-specific features

**Model answer:** Separate productized entitlements and temporary release flags from
custom code. Centralize and version decisions, use safe defaults and expiry, audit
changes, and measure adoption. Reject permanent forks; promote recurring customer
needs into supported capabilities with an operational and pricing model.

## 10. Finance wants invoices from monitoring metrics

**Model answer:** Sampled, mutable telemetry is unsuitable as financial evidence.
Create immutable deduplicated usage records with event time, source, unit, lineage,
and correction semantics. Rate and invoice downstream, reconcile totals, and keep
quota and entitlement behavior separate from billing aggregation.

## 11. A tenant disputes a consumption charge

**Model answer:** Trace the invoice line through rating and aggregation to immutable
usage facts. Verify identity, time windows, duplicates, late records, and plan version.
Issue an adjusting record rather than rewrite history, explain the outcome, and add
reconciliation or product evidence that prevents recurrence.

## 12. A database restore reintroduces deleted tenant data

**Model answer:** Contain access and follow privacy/security response. Compare the
deletion manifest and legal holds, reapply tombstones or deletion, and verify all
derived stores. Recovery procedures must replay post-backup deletion evidence and
test that exports, indexes, analytics, and replicas converge.

## 13. Global dashboards are green but one tenant is down

**Model answer:** Global averages masked concentrated impact. Use journey SLOs and
tenant/tier/cell views, then correlate placement, configuration, identity, quota,
dependency, and recent change. Control metric cardinality with aggregates plus secure
log/trace drill-down and alert on full tenant outages.

## 14. Sales promises a unique regional version

**Model answer:** Clarify the underlying regulatory or product need and meet it with
configuration, entitlement, placement, or deployment rings where possible. A code
fork creates security, support, and release debt. Any regional variant needs explicit
ownership, compatibility, retirement, and economics within one product lifecycle.

## 15. A large tenant must move to a dedicated cell

**Model answer:** Treat placement as a controlled migration: provision destination,
copy or stream changes, validate counts and invariants, quiesce or fence writes,
atomically change routing, observe, and retain a bounded rollback path. Reconcile
old data and metering, then prove source retirement.

## 16. A support engineer needs production access

**Model answer:** Use just-in-time approval scoped to tenant, purpose, actions, and
time, with strong workforce identity, masking, session audit, and customer evidence
where required. Prefer safe diagnostic tools and impersonation-resistant workflows;
never grant a permanent cross-tenant support role.
