# Scenario Questions and Model Answers

Last reviewed: **2026-09-02**

Answer each prompt aloud before reading the model answer. Use the
[CLEAR-DOC framework](../interview-playbook/scenario-answer-framework.md)
and challenge any unstated assumptions.

## 1. Ten-times traffic spike

**Prompt:** Design a customer-facing service for ten million registered users.
Traffic increases tenfold for two hours during a scheduled event.

**Clarify:** Active users, request mix, regional distribution, latency target,
write volume, event predictability, consistency needs, and cost ceiling.

**Architect-level answer:** Establish a measured baseline and load-test the peak
journeys. Cache static and safe read-heavy content at the edge; use stateless,
horizontally scalable request handling across failure zones; protect dependencies
with admission control and bounded concurrency. Buffer deferrable work in durable
queues and scale consumers on message age plus processing rate. Partition hot
data deliberately, pre-scale slow resources for the scheduled event, and use
autoscaling for residual variation. Define graceful degradation, per-tenant
limits, dashboards, synthetic tests, and rollback criteria. Run a rehearsal at
or above projected peak and compare unit cost with the business value.

**Trade-off:** Pre-provisioning costs more but reduces the cold-start and quota
risk of purely reactive scaling.

## 2. Intermittent 502 and 504 responses

**Prompt:** An application works internally, but external users intermittently
receive 502 and 504 responses through the load balancer.

**Architect-level answer:** Separate the two symptoms and trace a failing request
from DNS and edge through the load balancer, network path, proxy, application,
and dependencies. Correlate load-balancer access logs, backend latency,
connection resets, health-check state, saturation, deployments, and traces.
Compare timeout budgets at every hop and look for a shorter upstream timeout
than downstream processing time. Check keep-alive behavior, connection-pool
exhaustion, uneven target distribution, zone health, DNS changes, and security
rules. Mitigate with rollback or traffic reduction before tuning blindly, then
reproduce under controlled load and add an SLO-based alert.

**Follow-up:** How would you distinguish an overloaded backend from a network
path or proxy timeout?

## 3. Retry storm after dependency degradation

**Prompt:** A payment dependency slows down. Application instances retry three
times, traffic quadruples, and the dependency fails completely.

**Architect-level answer:** Stop amplification with an end-to-end deadline,
bounded concurrency, retry budget, exponential backoff and jitter, and one clear
retry owner. Retry only transient failures and only idempotent operations. Use a
circuit breaker as a protection mechanism, not as a substitute for a business
fallback. Queue permissible work, shed noncritical traffic, and expose a truthful
degraded state. Add dependency latency and retry-rate SLOs, then load-test the
failure mode rather than only the healthy path.

## 4. Multi-region active/active request

**Prompt:** A stakeholder asks for active/active in two regions to guarantee zero
downtime.

**Architect-level answer:** Replace “zero downtime” with a measurable availability
target, maximum outage, data-loss tolerance, and failure scope. Identify global
dependencies and decide whether writes can occur in both regions. Compare
active/passive, active/active reads with a single writer, and multi-writer
designs. Multi-writer improves some availability paths but introduces conflict,
ordering, latency, and reconciliation complexity. Design traffic management,
capacity after failure, data replication, fencing, failback, observability, and
regular exercises. Recommend the least complex topology that meets the verified
RTO/RPO and business value.

## 5. Strong consistency versus availability

**Prompt:** A product manager says every service must remain available during a
partition and all users must immediately see the latest data.

**Architect-level answer:** Explain that guarantees must be chosen per operation
and invariant. For safety-critical writes, reject or delay operations when
quorum cannot be established. For catalog, search, or analytical reads, bounded
staleness may be acceptable. Separate commands from projections where useful,
surface pending state to users, and design reconciliation. Document what each
API guarantees rather than labeling the entire platform CP or AP.

## 6. Duplicate orders after timeout

**Prompt:** Customers sometimes submit an order twice because the first response
times out even though payment succeeded.

**Architect-level answer:** Introduce a client-generated idempotency key scoped
to the business operation. Atomically persist the key with order state before
performing or confirming irreversible effects. Return the stored result for
duplicates and propagate an operation identity to downstream payment and
fulfilment services. Use an outbox or equivalent atomic publication strategy,
reconciliation for ambiguous outcomes, and a retention period aligned with the
business retry window. The user experience should show “processing” rather than
encourage blind resubmission.

## 7. Queue backlog grows for six hours

**Prompt:** Consumer processing stops for six hours while producers continue.

**Architect-level answer:** Protect retention first and determine the oldest
message age, arrival rate, processing rate, partition distribution, poison
messages, and downstream health. Restore consumption without overwhelming
dependencies. Increase concurrency only when partitions and downstream capacity
permit it; isolate or dead-letter poison messages; maintain idempotent processing
for replay. Estimate drain time from net processing rate, prioritize time-sensitive
messages if semantics allow, and communicate breached backlog SLOs. Prevent
recurrence with lag and message-age alerts, capacity tests, and runbooks.

## 8. Database CPU reaches 90 percent

**Prompt:** Production database CPU is 90%. Should the team resize immediately?

**Architect-level answer:** Resize as a reversible mitigation if customer impact
is imminent, but diagnose before declaring it the solution. Correlate the change
with traffic, releases, query plans, indexes, lock waits, connection counts,
cache hit rate, storage latency, replicas, maintenance, and hot tenants. Reduce
wasteful query work, cap unsafe concurrency, cache appropriate reads, and move
read traffic only when consistency allows. Partition or change the data model
only when evidence shows a structural limit. Validate the fix against latency,
throughput, and cost—not CPU alone.

## 9. Cache outage takes down the application

**Prompt:** A cache cluster fails and the database is immediately overwhelmed.

**Architect-level answer:** Treat the origin-protection failure as part of the
cache design. Use bounded fallback concurrency, request coalescing, staggered
TTLs, jitter, stale-if-safe behavior, and prioritized load shedding. Restore the
cache gradually so repopulation does not create another spike. Decide explicitly
whether the cache is optional acceleration or required state; if required,
design and test it as critical infrastructure. Exercise cold-cache recovery and
monitor hit rate, eviction, hot keys, and origin load.

## 10. Payment succeeds but inventory fails

**Prompt:** An order spans payment, inventory, shipping, and notification.
Payment succeeds, but inventory reservation fails.

**Architect-level answer:** Define a saga with explicit business states and
compensations. Decide whether inventory should be reserved before charging or
whether a failed reservation triggers a refund/void. Use durable commands or
events, idempotent handlers, an outbox, timeouts, and reconciliation. An
orchestrator makes the workflow and recovery visible; choreography may reduce
central control but can obscure ownership. Preserve an audit trail and provide
the customer with a truthful pending or compensated status.

## 11. Monolith modernization

**Prompt:** A large monolith blocks independent delivery. Leadership asks for a
complete microservices rewrite in twelve months.

**Architect-level answer:** Establish measurable bottlenecks before equating
microservices with modernization. Map domain boundaries, change coupling,
runtime dependencies, data ownership, and team ownership. Improve build,
testing, observability, and modularity first. Use a Strangler Fig approach for a
high-value, well-bounded capability, protected by an anti-corruption layer.
Measure delivery lead time, failure rate, reliability, and operating cost.
Continue only where the evidence justifies the distribution overhead.

## 12. Noisy tenant in a shared SaaS platform

**Prompt:** One tenant consumes most CPU and database connections, degrading all
other tenants.

**Architect-level answer:** Add tenant identity to telemetry and enforce quotas
at ingress, workload, and data layers. Isolate connection pools and queues,
prioritize critical operations, and use fair scheduling or cells for stronger
blast-radius control. Autoscaling alone may reward the abusive pattern and raise
cost. Define per-tenant SLOs and unit economics, then offer explicit service
tiers or dedicated isolation where the business case supports it.

## 13. Canary passes but production fails

**Prompt:** A canary deployment looks healthy, yet after full rollout 15% of API
requests fail.

**Architect-level answer:** Check whether canary traffic represented the affected
tenants, routes, regions, payloads, and dependencies. Use outcome-oriented
metrics rather than CPU and process health alone. Compare old and new versions
by status class, latency percentile, business conversion, and trace attributes.
Automate rollback on meaningful error-budget burn, preserve schema compatibility,
and increase exposure in controlled stages. Improve the canary selection model
and test low-volume critical journeys synthetically.

## 14. Global third-party outage

**Prompt:** A critical third-party API is unavailable globally for four hours.

**Architect-level answer:** Classify which journeys can fail closed, fail open,
queue, use cached data, or degrade. Enforce timeouts and isolation so the outage
does not exhaust local resources. Store permissible work durably with clear
expiry and customer status, then reconcile when the provider returns. Avoid
claiming a second provider is instant resilience: it requires compatible
semantics, data, contracts, testing, and operational readiness. Review vendor
SLAs, exit options, and business continuity with stakeholders.

## 15. Reduce cost by 30 percent

**Prompt:** Leadership mandates a 30% cloud-cost reduction without reducing
availability.

**Architect-level answer:** Baseline cost by product, environment, tenant, and
unit of business value. Remove idle and orphaned capacity, correct storage
lifecycle and logging retention, and right-size using utilization plus SLO data.
Then evaluate commitments, scheduling, autoscaling, managed-service choices,
data transfer, and architectural inefficiencies. Protect reliability capacity
and verify changes through load and recovery tests. Convert the target into
unit-cost and value metrics so savings remain durable rather than becoming a
one-time deletion exercise.

## Self-assessment

For each answer, score one point for each item you covered:

- business outcome and clarifying questions;
- measurable non-functional requirements;
- at least two options or an explicit alternative;
- coherent components and data flow;
- security and trust boundaries;
- failure modes and recovery;
- observability and operational ownership;
- cost and delivery plan;
- explicit trade-offs;
- validation evidence.

Scores below seven indicate that the answer likely needs more architect-level
depth.
