# Scenario Questions and Model Answers

[← Enterprise design exercise](design-exercise.md) · [Next: Advanced drills →](scenario-drills.md)

## 1. Leadership says all scale problems require NoSQL

**Model answer:** I would profile access paths, invariants, query plans, contention,
connections, working set, growth, and skew first. Fix modeling and operations, then
select a different model only when its transaction, query, and scale properties fit.
NoSQL moves constraints into design and application code; it does not erase them.

## 2. A read replica returns stale order status

**Model answer:** Classify the query's staleness tolerance and measure lag. Route
read-your-writes or correctness-critical status to the writer, wait on a version/token
where supported, or show pending state. Scale apply capacity and fix long transactions;
do not pretend every replica is an authoritative current view.

## 3. Checkout times out during database commit

**Model answer:** The outcome is unknown, not necessarily failed. Use a stable business
idempotency key and query authoritative transaction/order state before retry. Bound
timeouts and retry the complete transaction only when safe. Reconcile payment,
inventory, and order rather than issuing a second uncontrolled write.

## 4. A new index slows all writes

**Model answer:** Stop or roll back the change if safe, inspect build mode, locks, log,
I/O, cache, replica lag, and write amplification. Verify the query benefit against
real plans. Rebuild online or progressively if supported, schedule with headroom, and
remove redundant indexes after usage evidence.

## 5. Application autoscaling exhausts database connections

**Model answer:** Bound total pools across maximum instances below database capacity,
apply acquisition/query timeouts, and use a compatible proxy/pooler. Scale based on
queue and database headroom, not only application CPU. Find leaked or long-held
connections and validate failover behavior through the pool.

## 6. A tenant key creates one enormous shard

**Model answer:** Analyze tenant size and operation skew, required tenant-local
transactions, and query routing. Isolate the tenant, use a finer compound key, or add
a controlled subpartition and aggregation layer. Plan copy/change capture, validation,
cutover, rollback, and source retirement before the shard reaches a hard limit.

## 7. A deadlock appears after a release

**Model answer:** Capture the wait-for graph, transaction statements, lock order,
duration, indexes, and plan changes. Roll back or contain the release, enforce a
consistent access order, shorten transactions, add appropriate indexes, and implement
bounded whole-transaction retry. Raising timeouts does not remove the cycle.

## 8. A cache outage overloads the primary database

**Model answer:** Rate-limit and shed optional work, coalesce misses, preserve critical
queries, and restore cache progressively. Fix stampede with jittered TTL, soft expiry,
bounded concurrency, warming, and database capacity headroom. Validate that cache
loss is a planned degraded mode, not a database disaster.

## 9. Multi-region writes conflict on account balance

**Model answer:** Last-write-wins is unsafe for money. Choose a single authority or
partition account ownership, route writes accordingly, and use ledger entries with
idempotency and reconciliation. If synchronous global serialization is required,
accept and test its latency/partition availability trade-off.

## 10. Backup jobs are green but no restore has been tested

**Model answer:** Recoverability is unproven. Restore an isolated point, measure time,
validate data, schema, roles, keys, extensions, critical queries, tenant boundaries,
and application startup. Exercise destructive and regional scenarios, record evidence,
and remediate if actual RPO/RTO differ from policy.

## 11. One tenant requests point-in-time restore

**Model answer:** A whole shared-database rollback would erase other tenants' valid
changes. Restore the database to an isolated environment, extract and validate the
tenant scope, reconcile later legitimate changes, and apply corrective operations.
Design tenant history/export and deletion evidence for future partial recovery.

## 12. An ORM generates an N+1 query storm

**Model answer:** Stabilize with rate/concurrency bounds and revert the change. Use
query tracing and plans to confirm repeated round trips, then batch, join, prefetch,
or create a bounded read model. Add representative performance tests and query-count
budgets; increasing database size hides the application access-path defect.

## 13. A schema migration blocks a large table

**Model answer:** Cancel or complete according to engine safety and preserve evidence.
Use expand/migrate/contract, online build/change mechanisms, resumable bounded backfill,
lock timeouts, lag/log monitoring, and abort thresholds. Validate rollback and old/new
application overlap before contraction.

## 14. A MongoDB-compatible service is proposed as drop-in

**Model answer:** Inventory commands, transactions, consistency, indexes, aggregation,
drivers, change streams, limits, backup, and operational behavior. Run compatibility
and performance tests with production shapes and failures. API similarity is not
semantic equivalence; plan code change and rollback explicitly.

## 15. Analytics queries saturate the transaction database

**Model answer:** Protect checkout using workload limits and cancel unsafe queries.
Move analytical access to replicas only if lag/load is acceptable or feed a warehouse
through CDC/outbox. Define freshness, data quality, deletion, and reconciliation.
Do not let unrestricted reporting share critical transaction capacity.

## 16. Failover completes but applications remain unavailable

**Model answer:** Database promotion is one step. Check endpoint/DNS caching, stale
pools, TLS, credentials, transaction retry, driver topology, schema jobs, and dependent
services. Reset connections safely, resolve unknown writes idempotently, and measure
application journey recovery in future failover exercises.
