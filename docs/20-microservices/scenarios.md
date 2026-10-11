# Scenario Questions and Model Answers

[← Enterprise design exercise](design-exercise.md) · [Next: Advanced drills →](scenario-drills.md)

## 1. Leadership mandates 100 microservices

**Model answer:** Service count is not an outcome. I would identify coordination,
scale, reliability, and ownership constraints, compare a modular monolith and
coarser services, and extract only boundaries with measurable independent value.
Each service adds delivery, data, security, observability, and on-call cost.

## 2. Two services always release together

**Model answer:** Inspect shared invariants, tables, libraries, call patterns, and
team ownership. Coordinated release may expose a misplaced boundary. Either evolve
contracts and ownership to restore independence or merge the services; keeping a
distributed boundary for its own sake is worse.

## 3. Order placement spans inventory and payment

**Model answer:** Keep each local invariant atomic, represent the order workflow as
explicit states, use idempotency and reliable message publication, and coordinate a
saga. Define reservations, expiry, compensation, timeout, reconciliation, and what
the customer sees; a global rollback is neither available nor truthful.

## 4. Database commit succeeds but event publication fails

**Model answer:** Store event intent in a transactional outbox with the domain
change, then relay and monitor it. Consumers handle duplicates and ordering. Alert
on outbox age, support replay, and reconcile business records; do not attempt an
unreliable “write then publish” sequence.

## 5. A request crosses eight synchronous services

**Model answer:** Measure hop latency, failure, and necessity. Collapse chatty
boundaries, aggregate at the owning service, move noncritical work async, or create
a purpose-built read model. Propagate deadlines and trace context; adding retries
at every hop will amplify failure.

## 6. Teams want to query another service's tables

**Model answer:** Clarify the query and freshness need. Use the owner's API for small
fresh reads or a versioned event-fed materialized view for scalable cross-domain
reads. Direct table access couples schema and authority; frequent transactional
joins may mean the boundary should be redrawn.

## 7. A payment call times out

**Model answer:** Timeout means outcome unknown. Use a business idempotency key,
persist the attempt, query or receive provider status, and reconcile before retrying.
Expose pending state to the user. Never convert ambiguous timeout directly into a
second charge or assume failure.

## 8. A team claims exactly-once event processing

**Model answer:** Ask for the precise boundary. Networks and consumers can repeat
delivery; broker guarantees do not make external side effects exactly once. Use
stable event IDs, idempotent state transitions, deduplication where useful, ordering
scope, and reconciliation. Describe the business effect, not a slogan.

## 9. One service is overloaded by a noisy tenant

**Model answer:** Apply tenant-aware quotas, admission control, bounded concurrency,
bulkheads, priority, and load shedding before unsafe saturation. Observe per-tenant
usage and business impact. Scale the real bottleneck and consider cells when
isolation value justifies duplicated capacity.

## 10. A shared library update breaks most services

**Model answer:** Stabilize and roll back affected consumers, then reduce domain
logic and release coupling in the library. Keep shared libraries small and stable,
version them compatibly, test consumers, and prefer network contracts or generated
types only where they do not force lockstep adoption.

## 11. Services use one organization-wide IAM role

**Model answer:** Treat this as excessive privilege and poor attribution. Inventory
access, create per-workload short-lived roles scoped to owned resources, stage the
migration, and monitor denials. Separate service, deployer, operator, and user-delegated
authority; network location is not authorization.

## 12. A schema change prevents rollback

**Model answer:** Use expand/migrate/contract so old and new service versions overlap
safely. Make producers/consumers tolerant, canary the change, verify migration, and
delay contraction until usage evidence proves compatibility. Application rollback
without data compatibility is false reassurance.

## 13. A region fails during a saga

**Model answer:** Recover authoritative state and workflow position to the agreed
RTO/RPO, prevent dual coordinators, and resume idempotently. Reconcile reservations
and external side effects before new progression. Multi-region compute alone does
not solve message, database, identity, or provider state.

## 14. Teams cannot diagnose a distributed incident

**Model answer:** Establish correlation across requests/messages, service and journey
SLIs, structured logs, traces, deployment markers, and business workflow metrics.
Maintain owned dependency maps and runbooks. Stabilize overload and changes first;
a trace suggests relationships but does not prove root cause.

## 15. A monolith modernization stalls after extracting utilities

**Model answer:** Utility extraction created dependencies without business autonomy.
Return to domain and change analysis, select one capability with clear owner and
value, create an anti-corruption layer, transfer data authority, route incrementally,
measure outcomes, and retire the old path. Merge low-value services if necessary.
