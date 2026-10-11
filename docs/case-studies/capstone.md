# Principal Architect Capstone

[← AI operations copilot](ai-operations-copilot.md) · [Next: References and module map →](references.md)

Estimated time: **90 minutes**. Use the [common scorecard](scorecard.md); target
80/100 before considering the case complete.

## Brief

Meridian Group acquired a European SaaS company while operating a North American
commerce business and 40 legacy applications in two data centers. AWS is the
primary cloud; the acquisition uses Azure, analytics uses Google Cloud, and factory
systems require local operation. Recent events include a six-hour checkout outage,
an identity breach, missed recovery objectives, and 55% annual cloud-cost growth.

The board requests within twelve months:

- regional launch of a shared customer platform;
- reduced outage and cyber-recovery risk;
- data residency and tenant-isolation evidence;
- faster, safer delivery across 70 product teams;
- 20% lower unit cost without a reliability regression;
- an AI operations assistant demonstration within one quarter;
- a credible data-center exit decision—not a predetermined exit.

## Evidence pack

- Peak commerce demand is 80,000 requests/second; normal is 1,500.
- The purchase SLO is undocumented; leadership says “five nines.”
- Order RPO is near zero; the tested regional recovery time is nine hours.
- Thirty percent of cloud cost is unallocated; commitments cover 45% of compute.
- Teams share long-lived CI credentials and eight manually managed clusters.
- The acquired SaaS uses a shared database and application tenant filters.
- Factory WAN outages average three hours each quarter.
- Only 40% of applications have verified owners and dependency maps.

## Discovery prompts

Identify the five questions that could most change sequencing or architecture.
Name decision owners, affected stakeholders, regulatory unknowns, critical business
capabilities, and claims that require evidence. Challenge conflicting targets.

## Candidate tasks

1. Define business outcomes, invariants, SLOs, RTO/RPO, unit metrics, and non-goals.
2. Segment the estate into target platforms and explicitly retained hybrid systems.
3. Propose options for customer identity, tenancy, data, integration, and regions.
4. Design landing-zone, network, Zero Trust, delivery, observability, and recovery controls.
5. Establish platform/team ownership, governance, funding, and exception processes.
6. Create a four-wave roadmap with dependencies, exit criteria, and reversible decisions.
7. Explain which cloud-native differences to retain and which contracts to standardize.
8. Present a ten-minute board recommendation and a deeper engineering defense.

## Failure injects

Reveal one every ten minutes after the initial design:

- A regulator says customer support staff outside the region cannot access raw records.
- The commerce team refuses a migration freeze before the largest annual event.
- Azure-to-AWS transfer estimates are four times the original business case.
- A recovery exercise finds corrupted replicas and an untested clean backup.
- The new platform control plane causes a deployment outage across three teams.
- The AI assistant retrieves a confidential incident from another business unit.
- Finance demands immediate commitment purchases to meet the annual target.
- A factory modernization pilot stops when its WAN path fails.

## Model direction

Do not propose one universal platform or a twelve-month big bang. Establish a
portfolio and business-capability map, owners, actual SLO/RTO/RPO, data obligations,
unit economics, and dependency confidence. Create secure cloud foundations and
federated identity, remove static pipeline credentials, define artifact trust, and
provide a small set of risk-tiered paved roads. Use cells/accounts/subscriptions to
bound blast radius while retaining provider-native services where they create value.

Protect commerce correctness and overload first; use measured error budgets and
progressive change. Build regional SaaS data planes with explicit tenant identity
and a minimal control plane. Treat cyber recovery as a separate clean trust path
with immutable backups, dependency-aware recovery waves, and exercises. Retain
factory-local control with store-and-forward integration until network and safety
evidence supports change. Repair allocation and unit metrics before commitments or
indiscriminate cuts.

The first-quarter AI demonstration should remain entitlement-aware and read-only,
measuring evidence-collection time and disclosure failures. Sequence the program as:
stabilize identity/recovery/observability; pilot platform and tenancy controls;
migrate bounded capabilities and prove regional recovery; then scale or retire based
on evidence. Give each wave business, security, reliability, cost, and adoption exit
criteria. Record risks the board consciously accepts.

## Strong close

Conclude with three funded decisions, three deferred decisions, the highest-risk
assumption, a 30-day evidence plan, and clear owners. Explain why architecture is a
sequence of reversible risk reductions rather than a final diagram.

## Capstone review questions

- Did the proposal prioritize and sequence, or simply include every desirable goal?
- Are cross-cloud choices linked to business constraints rather than neutrality slogans?
- Can teams deploy and recover safely while the transformation is incomplete?
- Do cost savings represent eliminated waste and improved unit economics?
- Can executives see decisions, risks, evidence, owners, and when to stop?
