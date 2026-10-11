# Enterprise Microservices Design Exercise

[← Organization and migration](organization-migration.md) · [Next: Scenario questions →](scenarios.md)

## Brief

A retailer's modular monolith handles catalogue, cart, inventory, orders, payment,
shipping, and notification. Weekly releases require 14 teams to coordinate. Peak
events reach 50 times normal demand; payment timeouts caused duplicate charges and
the last database release blocked checkout for 40 minutes. Leadership demands
“microservices on AWS” in nine months.

## Constraints

- inventory cannot oversell and confirmed orders require near-zero RPO;
- payment and shipping providers are external and sometimes slow;
- browsing may degrade, but order state must remain explainable and reconcilable;
- teams have strong CI but limited distributed tracing and event operations;
- migration cannot pause feature delivery;
- Azure hosts customer identity and Google Cloud receives analytics events.

## Candidate direction

Challenge full decomposition. Map domains and extract one capability whose change
or scale pain justifies independence. Keep inventory reservation and its atomic
invariants together. The order service owns workflow state; payment owns provider
interaction and business idempotency; shipping reacts after an approved order.
Use an edge API boundary and avoid exposing internal services to clients.

Persist order transitions and outbox intent atomically, publish versioned domain
events, and make consumers idempotent. Use an explicit saga where business progress
and compensation must be visible. Define pending states and reconciliation against
payment/provider records. Build materialized reads for cross-domain order status
when staleness is acceptable.

On AWS, select API, compute, database, queue/event, identity, and observability
services only after these semantics. Use workload roles, private data credentials,
deadlines, retry budgets, admission control, immutable artifacts, contract tests,
progressive delivery, traces, and journey SLOs. Translate identity and analytics
contracts across clouds without creating synchronous cross-cloud checkout calls.

## Scored deliverable (50 points)

| Area | Points | Strong evidence |
| --- | ---: | --- |
| Decision and domain boundaries | 8 | justified extraction, invariants, ownership, granularity |
| Communication and contracts | 7 | timing, APIs/events, compatibility, idempotency |
| Data and consistency | 9 | authority, saga/outbox, reads, reconciliation, recovery |
| Resilience and performance | 7 | budgets, overload, dependencies, degradation, capacity |
| Security and identity | 6 | user/workload/tenant/data boundaries, least privilege |
| Delivery and operations | 8 | testing, rollout, SLOs, observability, incidents, recovery |
| Migration, organization, cost | 5 | strangler wave, owners, evidence, retirement, economics |

Score 40+ only when the design explains business state under partial failure.
