# Data Ownership and Consistency

[← Communication and contracts](communication-contracts.md) · [Next: Resilience and performance →](resilience-performance.md)

## Private data ownership

A service owns its schema and business invariants. Other services use its API,
events, or purpose-built read models rather than direct table access. Separate
logical schemas or credentials can establish ownership before separate database
servers. Polyglot persistence is optional, not a goal.

## Consistency by invariant

Keep rules requiring atomic correctness inside one boundary where possible. For
cross-service workflows, define intermediate states, time limits, idempotency,
compensation, reconciliation, and user-visible status. “Eventual consistency” is
incomplete without a convergence bound and failure behavior.

## Reliable state and message change

A transactional outbox stores the domain update and event intent atomically, then
a relay publishes. Consumers must still handle duplicates and ordering. Change data
capture is an implementation option; it needs schema, privacy, and operational
ownership.

## Sagas

A saga is a sequence of local transactions with compensating business actions.
Choreography reduces central coordination initially but can hide flow; orchestration
makes state explicit but creates workflow infrastructure. Compensation is not a
rollback: a refund cannot erase that a charge and notification occurred.

## Cross-service reads

Choose API composition for small, fresh queries with bounded fan-out; materialized
views/CQRS for scalable or resilient reads with accepted staleness; or move the
boundary if constant joins reveal misplaced ownership. Record source, version,
freshness, rebuild, and deletion behavior for derived data.

## Reconciliation

Compare authoritative records and repair discrepancies after partial failure.
Design operational queries and immutable business identifiers from the start.
Backups per service are insufficient if restore points create an impossible global
business state; recovery requires dependency-aware reconciliation.
