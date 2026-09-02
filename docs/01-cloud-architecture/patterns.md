# Resilience and Integration Patterns

Last reviewed: **2026-09-02**

Patterns are reusable responses to forces and failure modes. They are not
mandatory components. Every pattern adds behavior that must be tested and
operated.

## Timeout, retry, backoff, and jitter

Every remote call needs a deadline aligned with the end-to-end latency budget.
Retries should be used only for failures likely to be transient and only when
the operation is safe to repeat.

A safe retry policy considers:

- connection and request timeouts;
- maximum attempts and total deadline;
- exponential backoff plus random jitter;
- idempotency or deduplication;
- retry budgets to prevent amplification;
- `Retry-After` or explicit server signals;
- whether retries belong at one layer rather than every layer.

## Circuit breaker

A circuit breaker stops calls to a dependency after failures cross a threshold,
then probes for recovery. It can reduce wasted work and cascading failure, but
poor thresholds can cause synchronized outages or slow recovery.

Use it with timeouts, bounded concurrency, telemetry, and a defined fallback.
Do not use it to conceal a dependency that the business journey cannot operate
without.

## Bulkhead

Bulkheads isolate resources so one workload, tenant, dependency, or request
class cannot exhaust all capacity. Isolation may be applied to thread pools,
connection pools, queues, compute groups, accounts, subscriptions, projects,
clusters, or cells.

The trade-off is reduced pooling efficiency and greater operational overhead.

## Rate limiting and load shedding

Rate limits enforce a consumption policy; load shedding protects the system
when it approaches unsafe operating conditions. Good designs prioritize work,
return explicit errors, provide retry guidance, and protect recovery traffic.

Common algorithms include token bucket, leaky bucket, fixed window, and sliding
window. Scope matters: user, tenant, API key, route, region, or global.

## Caching

Caching can improve latency, availability, and cost, but introduces staleness
and invalidation complexity.

Decide:

- cache location: client, edge, gateway, service, or database;
- read strategy: cache-aside, read-through, refresh-ahead;
- write strategy: write-through, write-behind, invalidation;
- TTL, eviction, consistency, and stampede protection;
- behavior when the cache or origin is unavailable;
- data sensitivity and tenant isolation.

## Queue-based load leveling

A durable queue separates intake rate from processing rate. It is appropriate
when work can be asynchronous and a temporary backlog is acceptable.

Define backlog SLOs, retention, dead-letter handling, poison-message policy,
ordering needs, deduplication, replay, and downstream capacity. Autoscaling on
queue depth alone is incomplete; consider message age and processing duration.

## CQRS and event sourcing

**Command Query Responsibility Segregation (CQRS)** separates write and read
models when their consistency, scale, or representation needs differ.

**Event sourcing** stores domain changes as an append-only event history from
which state can be derived. It supports audit and temporal reconstruction but
adds event-versioning, replay, privacy, and operational complexity.

They can be used independently. Avoid them when a conventional transactional
model satisfies the requirements.

## Saga

A saga coordinates a business process across independently committed steps.
Failure invokes compensating actions rather than a global distributed rollback.

- **Choreography:** services react to events; simple initially but flows can
  become implicit and difficult to observe.
- **Orchestration:** a coordinator directs steps; flow is explicit but the
  orchestrator becomes critical workflow infrastructure.

Compensation is a business action, not a database rollback. Refunding a payment
does not erase the fact that the charge occurred.

## Strangler Fig and anti-corruption layer

The Strangler Fig pattern incrementally routes capabilities from a legacy system
to a new implementation. An anti-corruption layer translates between legacy and
new domain models so the new design does not inherit accidental semantics.

Success requires an ownership map, traffic-routing strategy, data transition
plan, observability across both paths, and criteria for retiring old behavior.

## Sidecar and ambassador

A sidecar runs supporting functionality next to an application instance. An
ambassador is a specialized sidecar or proxy that handles outbound or inbound
communication concerns.

They can standardize telemetry, security, and network behavior but consume
resources, add failure modes, and may hide important network behavior from
application teams.

## Deployment patterns

| Pattern | Strength | Principal risk |
| --- | --- | --- |
| Rolling | Efficient gradual replacement | Old and new versions overlap |
| Blue/green | Fast traffic switch and rollback | Duplicate environment cost; data compatibility |
| Canary | Validates with limited real traffic | Requires representative routing and strong metrics |
| Feature flag | Separates deployment from release | Flag debt and behavioral combinations |
| Immutable infrastructure | Reduces configuration drift | Image pipeline and state separation are required |

Database and event-schema compatibility often determine whether an application
rollback is truly safe.

## Pattern interaction checklist

Before combining patterns, test the interactions:

- Can retries defeat rate limits or overload recovery?
- Can a circuit breaker turn a partial failure into a complete outage?
- Can caches serve unsafe stale data after a failover?
- Can queue replay duplicate irreversible side effects?
- Can canary metrics detect tenant-specific or low-volume failures?
- Can a deployment roll back after a schema or event change?
