# Scenario Questions and Model Answers

[← Design exercise](design-exercise.md) · [Next: Advanced drills →](scenario-drills.md)

Answer aloud: clarify outcome and constraints, state assumptions, propose the decision,
explain transition and failure behavior, name evidence, and close with trade-offs.

## 1. The CEO says, “Move all 600 applications in 12 months.” How do you begin?

**Model answer:** I clarify the forcing event, outcomes, immovable date, funding,
acceptable disruption, risk appetite, and definition of done. I establish accountable
business, platform, security, application, operations, and cutover owners. I time-box
inventory and dependency discovery, segment by criticality and confidence, validate
the landing zone, select a representative learning wave, and create disposition and
wave gates. I report business capabilities closed and legacy cost removed—not servers
copied—and expose confidence ranges and blockers early.

## 2. The CMDB is only 60 percent accurate. Must the program wait?

**Model answer:** No. I triangulate CMDB records with hypervisor/cloud exports, flows,
DNS, identity, monitoring, repositories, finance, contracts, and owner interviews.
Each fact receives source, date, confidence, and validator. High-criticality or
high-connectivity unknowns get deeper discovery; low-risk workloads can progress with
explicit assumptions. Rehearsals and early waves refine the graph. Incomplete evidence
changes risk and sequencing, but waiting for a perfect inventory creates false safety.

## 3. Leadership requires every application to be refactored during migration

**Model answer:** I connect modernization to measurable constraints and show schedule,
regression, skill, and coexistence risk. I separate changes required before movement
from safe landing, stabilization, and later modernization. Unsupported runtimes or
hard-coded identity may require early remediation; bounded replatforming may deliver
value without a rewrite. I propose evidence-based prioritization and re-evaluation
triggers. A uniform strategy ignores workload economics and threatens the exit date.

## 4. How would you choose the first wave?

**Model answer:** I choose a useful, recoverable dependency group that exercises the
real platform path: identity, network, deployment, data, monitoring, security, support,
cost, and decommissioning. It needs committed owners, testability, manageable data,
and a credible rollback. I avoid both the crown jewels and trivial static sites. Its
purpose is production value plus learning that changes automation, estimates, gates,
and later wave design.

## 5. A workload is technically compatible with rehosting but expensive in AWS

**Model answer:** I compare remain, rehost, replatform, repurchase, and retire using
full cash flow, deadline, capacity, licensing, support, resilience, people, dual run,
and decommissioning. I examine rightsizing and scheduling but do not assume future
savings. If rehost meets the deadline, I define post-move optimization with owner,
budget, metric, and trigger; if value remains negative, retain or repurchase may be
better. Compatibility alone does not establish business fit.

## 6. A critical application has many undocumented dependencies

**Model answer:** I combine flow observation across representative cycles, configuration
and code review, DNS/certificate/database/batch analysis, business-journey mapping,
and owner/vendor interviews. I classify dependencies by criticality, direction,
latency, protocol, data, and move-together constraint. I test synthetic paths and
rehearse. Until confidence improves, I keep the dependency group together or provide
temporary connectivity, with monitored assumptions and abort conditions.

## 7. Describe a near-zero-downtime database cutover

**Model answer:** I baseline-copy then continuously replicate/CDC, validate schema and
permissions, monitor lag and source impact, rehearse with production-like volume, and
reconcile business invariants. At cutover I freeze or fence writes, drain work, reach
the lag threshold, apply final changes, switch authoritative routing, invalidate
caches, run technical and business validation, and monitor. Rollback has a deadline
and accounts for post-cutover writes through reverse sync or an explicit fallback.

## 8. The cutover succeeds, but users report intermittent failures

**Model answer:** I use the command structure and correlation data to segment by
journey, cohort, location, dependency, and time. I check DNS/cache propagation,
identity, network paths, quotas, connection pools, certificates, jobs, and residual
legacy calls. I compare abort thresholds and data risk before rollback; when rollback
would split authority, controlled forward fix or cohort fallback may be safer. I keep
business communication and reconciliation active until stability criteria are met.

## 9. Security demands the legacy firewall rules be copied exactly

**Model answer:** I preserve control objectives, not accidental implementation. I map
flows, identities, trust boundaries, threats, data, and evidence, then replace broad
network trust with least-privilege identity and network controls where possible.
Required temporary parity gets an owner, compensating controls, logging, expiry, and
removal plan. Security validates that effectiveness is equal or better; migration is
not permission to reproduce years of unused access.

## 10. The landing zone exists. How do you prove it is ready?

**Model answer:** I take a representative workload through account vending, identity,
connectivity, DNS/certificates, deployment, secrets, logging, alerts, vulnerability
response, backup/restore, incident escalation, cost attribution, quota handling, and
access review. I verify ownership and service levels, not just resource existence.
Gaps become platform backlog or time-bound wave exceptions. A slide saying “landing
zone complete” is not readiness evidence.

## 11. A vendor product cannot run on the preferred managed service

**Model answer:** I confirm certified configurations, roadmap, license, support,
performance, data path, and contractual constraints with the vendor. I compare rehost,
relocate, repurchase, retain, or bounded replacement against deadline and business
value. I isolate its interfaces and operational risks, define a supportable target and
future review trigger, and avoid unsupported engineering merely to satisfy a cloud
standard. Exception does not mean ungoverned.

## 12. How do you prevent a migration factory becoming a ticket factory?

**Model answer:** I standardize high-risk repeated work as self-service paved paths,
with clear interfaces and service levels. Cross-functional wave teams retain outcome
ownership; platform and security specialists enable rather than receive serial
handoffs. I limit work in progress and measure wait time, rework, blocker age, and
defect escape. Recurring exceptions improve products or policy. Local workload
knowledge and business acceptance cannot be centralized away.

## 13. AWS is primary, but acquisitions use Azure and analytics uses Google Cloud

**Model answer:** I place workloads from business, data, regulatory, latency, ecosystem,
skill, and acquisition needs rather than forcing symmetry. I standardize identity
federation, control objectives, evidence, SLOs, tagging/allocation, incident ownership,
and architecture decisions while allowing provider-native implementation. I explicitly
design connectivity, DNS, data authority, egress, observability, recovery, and support.
Service-name mapping alone is not a multi-cloud architecture.

## 14. When is migration complete?

**Model answer:** I report separate states: technical cutover, business validation,
operational acceptance, security/control closure, hypercare exit, legacy data handling,
asset and license shutdown, CMDB/continuity updates, financial closure, and benefits
realization. Owners and evidence exist for each. This prevents “migrated” systems from
leaving unsupported services, broad temporary access, and years of dual cost.

## 15. How do you demonstrate modernization value?

**Model answer:** I baseline the constraint—lead time, incident rate, recovery,
scalability, support risk, unit cost, or user outcome—then assign an owner and target.
I measure after stabilization, normalize for volume and business change, include
delivery and operating cost, and compare with the counterfactual. If evidence does not
support value, I stop, simplify, or change direction. Container count is not an
outcome metric.

## 16. A migration wave misses its date. What do you do?

**Model answer:** I protect quality and inspect the system rather than demanding
overtime. I identify whether the constraint is discovery, dependency, platform queue,
test environment, vendor, data transfer, approval, or ownership. I quantify deadline
and downstream impact, reduce scope only along safe boundaries, resequence independent
work, and escalate decisions with options. Estimates and later waves are updated from
evidence; readiness gates are not silently waived to make the dashboard green.
