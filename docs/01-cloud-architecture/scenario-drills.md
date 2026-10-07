# Advanced Scenario Drills

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-07**

The core scenario page contains 15 model answers. These 12 drills bring the
pilot total to 27 scenarios. Answer each aloud with CLEAR-DOC before opening the
answer outline. The outline is a reasoning spine, not a script.

## 16. Hot partition during ticket release

**Prompt:** Overall database capacity is below 40%, but one popular event is
throttled and reservation latency rises sharply.

**What is tested:** Partition-key design, skew, evidence, and safe mitigation.

**Strong answer spine:** Confirm whether throttling is concentrated on one key
or partition and correlate it with the event identifier. Protect correctness
while reducing admitted write rate. Separate reads from reservation writes,
review key cardinality and item size, and evaluate write sharding only with a
deterministic aggregation/reconciliation model. Pre-warm or provision capacity
only if the service's scaling behavior and event forecast justify it. Rehearse
the hot-event distribution rather than testing uniform keys.

**Follow-ups:** How would you read sharded inventory? What happens when one seat
is much hotter than the event? Which metric distinguishes total saturation from skew?

## 17. Cache reports seats that no longer exist

**Prompt:** Customers see available seats in search, but reservation frequently
returns a conflict.

**What is tested:** Cache semantics and business correctness.

**Strong answer spine:** Treat search availability as a hint and the inventory
system of record as authoritative. Use short, evidence-based TTLs and explicit
staleness messaging. Never use cache state to confirm a seat. Measure stale-hit
and reservation-conflict rates, prevent cache stampedes, and invalidate or
refresh after state changes without assuming invalidation is perfectly reliable.

**Follow-ups:** Is a conflict an availability failure? When would you remove the
cache? What customer experience reduces repeated contention?

## 18. One Availability Zone becomes impaired

**Prompt:** An application remains reachable, but latency rises after one zone
loses network connectivity.

**Strong answer spine:** Verify target and dependency health by zone. Ensure
remaining zones have failure capacity, stop routing to unhealthy targets, and
check whether zonal dependencies, NAT paths, or uneven connection pools retain
traffic. Scale only within tested downstream limits. Explain recovery of
stateless services separately from stateful quorum, replication, and queue behavior.

**Follow-ups:** Do you reserve capacity for zone loss? Could cross-zone balancing
hide a bad dependency? When is zonal evacuation unsafe?

## 19. Primary Region is unavailable during payment

**Prompt:** The business asks for automatic regional failover with no duplicate charges.

**Strong answer spine:** Define outage scope, decision authority, RTO, and RPO.
Fence or establish write ownership before admitting payments in the recovery
Region. Carry provider idempotency keys across failover, reconcile unknown
outcomes, and restore queue/workflow state. Separate browsing failover from the
more constrained purchase path. Automate routing only when health signals cannot
create a split-brain write path; test failback as seriously as failover.

**Follow-ups:** Who declares failover? Which dependencies remain global? How are
DNS caches and in-flight requests handled?

## 20. Events arrive out of order

**Prompt:** A `TicketConfirmed` event sometimes arrives before `TicketHeld` in a
downstream analytics and notification service.

**Strong answer spine:** Clarify whether ordering is required globally or only
per ticket/order. Include entity version and event identifier, make consumers
idempotent, and reject, buffer, or reconcile stale versions. Prefer per-entity
ordering to global ordering. Maintain an authoritative state lookup for repair
and define how long consumers wait for a gap before escalating.

**Follow-ups:** Does FIFO guarantee business correctness? How are poison events
handled? Can the consumer rebuild its state?

## 21. A schema change breaks older consumers

**Prompt:** A producer removes a field after its own deployment succeeds, and
two consumers fail hours later.

**Strong answer spine:** Restore compatibility or roll back the producer first.
Use additive changes, tolerant readers, versioned contracts, and consumer-driven
contract tests. Separate deploy from activation with a compatibility window.
Track consumer ownership and lag, and define deprecation evidence before removal.

**Follow-ups:** How do database expand/contract changes work? Who owns event
schemas? What if one consumer cannot upgrade for six months?

## 22. Data residency conflicts with global active-active

**Prompt:** Leadership wants global writes, while identity data must remain in
the customer's legal region.

**Strong answer spine:** Classify identity, order, operational, and derived data.
Keep regulated identity in a regional system and exchange opaque identifiers or
minimum necessary claims. Evaluate regional cells, single-writer ownership, and
global non-sensitive catalogue data. Document cross-border support access,
backups, logs, encryption keys, and deletion—not only the primary database.

**Follow-ups:** Are observability records regulated? Where does encryption help
and where does it not? How does customer migration between regions work?

## 23. Bots consume the entire release

**Prompt:** Infrastructure remains healthy, but automated clients obtain most
tickets before legitimate customers.

**Strong answer spine:** Frame this as fairness and abuse, not only capacity.
Combine identity/account controls, waiting-room admission, rate and behavioral
signals, purchase limits, risk-based challenges, and post-purchase detection.
Protect origin access and resist bypass. Measure false positives and provide an
appeal/support path. Avoid claiming one CAPTCHA or WAF rule solves adversarial behavior.

**Follow-ups:** How do privacy requirements limit detection? What fails open or
closed? How do you prevent privileged customers from bypassing fairness?

## 24. Dashboard is green while customers fail

**Prompt:** CPU, memory, and host health are normal, but purchase completion drops 20%.

**Strong answer spine:** Infrastructure health is not the customer SLI. Add
journey success, latency, payment outcome, queue age, and dependency metrics.
Correlate by version, region, zone, client, and outcome without high-cardinality
explosion. Use synthetic and real-user signals, structured logs, and traces to
identify the broken step. Alert on SLO burn rather than every component threshold.

**Follow-ups:** Which signal pages a human? How do you avoid PII in telemetry?
What if synthetic traffic succeeds but real traffic fails?

## 25. Rollback cannot undo the database migration

**Prompt:** A canary release changes a shared schema; application rollback now fails.

**Strong answer spine:** Stop rollout and stabilize with a compatible application
version. Use expand/migrate/contract: add compatible schema, deploy readers and
writers, backfill observably, switch behavior, then remove only after evidence.
Avoid destructive changes in the same step as application activation. Define
forward-fix versus rollback criteria and test restore without using backup as the
first response to every migration issue.

**Follow-ups:** How do you backfill without overload? What if old and new writers
coexist? When is feature-flag rollback insufficient?

## 26. Reliability target exceeds the budget

**Prompt:** A stakeholder asks for 99.999% availability but will fund only one Region.

**Strong answer spine:** Translate the percentage into allowed interruption and
critical journeys. Show which failure classes a single Region cannot meet and
quantify incremental cost and operational capability. Offer tiered options:
multi-AZ with tested recovery, warm standby, or multi-region serving. Ask which
business loss justifies each tier, and document the accepted risk if funding
does not match the target.

**Follow-ups:** Does multi-region automatically deliver five nines? Which global
dependencies remain? What organizational changes are required?

## 27. Cloud bill doubles after resilience work

**Prompt:** Costs double after queues, replicas, observability, and recovery
capacity are added; leadership asks to remove them.

**Strong answer spine:** Attribute spend to business capability and unit cost.
Remove waste first: idle environments, excessive retention, unbounded telemetry,
cross-zone/region transfer, and over-provisioned recovery. Preserve controls
whose removal violates agreed RTO/RPO or overload safety. Compare recovery tiers
and test lower-cost options. Make the reliability-versus-cost decision explicit
rather than silently eroding the objective.

**Follow-ups:** Which resilience capacity can be scaled down? How do you price a
confirmed order? What evidence proves a cost optimization is safe?

## Drill scoring

Score each answer from zero to two in each dimension:

| Dimension | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Clarification | Assumes | Some constraints | Business outcome and measurable limits |
| Architecture | Product list | Coherent happy path | State, boundaries, alternatives, rationale |
| Failure | Ignored | Names failure | Detection, degradation, recovery, evidence |
| Security | Generic | Basic controls | Threat/trust/data-specific decisions |
| Operations | CPU dashboard | Metrics and alerts | SLO, ownership, rollout, rollback, runbook |
| Cost/change | Ignored | Mentions cost | Unit economics and phased delivery |

Ten or more out of twelve is a strong senior-level answer. A high score still
requires concise delivery; depth that cannot be communicated is difficult to use.
