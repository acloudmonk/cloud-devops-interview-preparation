# Case 1: Global Commerce Surge

[← Common scorecard](scorecard.md) · [Next: Regulated SaaS →](regulated-saas.md)

## Brief

A retailer sells limited products in weekly global releases. Normal traffic is
2,000 requests/second; release traffic may reach 150,000. Inventory must not
oversell, payment providers time out unpredictably, and buyers expect confirmation
within three seconds. The current single-region application caused duplicate
charges and a 90-minute outage. Launch is in sixteen weeks.

## Discovery prompts

- Which journeys need 99.95% availability and which may degrade or queue?
- Is inventory global, regional, or allocated before release?
- What are reservation expiry, payment, refund, fraud, and reconciliation rules?
- What RTO/RPO and residency constraints apply to orders and customer identity?
- What is the demand distribution, bot threat, budget ceiling, and team capability?

## Candidate tasks

1. Define correctness invariants, SLIs/SLOs, RTO/RPO, and capacity assumptions.
2. Compare single-region active/passive with a multi-region serving approach.
3. Design edge admission, browse caching, reservation, payment, events, and records.
4. Explain idempotency, concurrency control, backpressure, and reconciliation.
5. Provide security, observability, release, game-day, and cost-per-order plans.

## Failure injects

- The cache fails cold five minutes before release.
- Payment accepts a charge but the client times out.
- Event consumers are unavailable for forty minutes.
- A region fails after reservations exist but before order confirmation.
- A botnet rotates identities faster than the edge rule update cycle.

## Model direction

Use an edge waiting room and admission budget so downstream correctness systems
never absorb uncontrolled demand. Separate cacheable catalogue reads from scarce
inventory writes. Create a reservation with atomic conditional state and expiry;
use business idempotency keys across checkout and payment. Persist the order intent
before asynchronous side effects, publish through an outbox or equivalent durable
pattern, and reconcile provider records rather than treating timeout as failure.

A single write home with multi-zone availability and cross-region recovery is a
credible sixteen-week starting point. A globally distributed write design is valid
only with an explicit conflict and inventory-allocation model. Use AWS capabilities
such as CloudFront/WAF, managed queueing, serverless or container compute, and a
database selected for transaction semantics after defining requirements. Canary by
journey, rehearse peak load and regional recovery, and measure cost per confirmed
order. Preserve browsing and queue status when purchasing must pause.

## Strong close

Recommend the simplest design that protects inventory and payment correctness at
peak. State the assumption most likely to change the regional strategy and the load,
failure, and reconciliation evidence required before launch.
