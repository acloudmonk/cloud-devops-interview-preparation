# Caching and Connection Management

[← Partitioning and sharding](partitioning-sharding.md) · [Next: Security, privacy, and governance →](security-governance.md)

## Cache patterns

Cache-aside loads on miss; read-through delegates loading; write-through updates cache
with the write; write-behind accepts cache writes before durable persistence and needs
strong loss/recovery controls. Choose the source of truth, consistency expectation,
miss behavior, invalidation, and degraded mode. A cache should not silently become
authority because the database is slow.

## Invalidation and stampede

Use bounded TTL plus event/version-based invalidation where justified. Include tenant,
authorization, locale, and schema dimensions in keys. Prevent stampede with request
coalescing, jittered TTL, soft expiry, background refresh, admission, and stale-if-safe
behavior. Negative caching needs short bounds because absence can change.

## Correctness

Never cache authorization-sensitive or transaction-critical state without explicit
staleness policy and revocation. Version values so an old invalidation cannot remove
new state or a late fill overwrite a newer write. Treat cache loss as expected and
load-test database survival during cold start or regional cache failure.

## Connection pools

Connections consume server memory and process resources. Total possible connections
equal application instances multiplied by per-instance pool size plus jobs, operators,
and failover overlap. Bound pools below database capacity, use acquisition and query
timeouts, release promptly, and expose wait time. Unlimited pools move overload into
the database.

## Proxies and multiplexing

A database proxy or pooler can absorb connection churn and multiplex compatible
sessions, but transaction pinning, prepared statements, session variables, temporary
tables, or driver behavior can reduce reuse. The proxy adds capacity, security, and
failure considerations. Test actual application semantics through it.

## Failover and retry

Drain or reset stale connections after endpoint change. Retry only transient,
idempotent operations with a bounded budget and full-transaction scope where required.
A timeout leaves commit outcome unknown; query transaction/business status before
repeating a non-idempotent write.
