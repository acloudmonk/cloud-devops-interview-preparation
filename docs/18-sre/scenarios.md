# SRE Scenario Questions and Model Answers

[← Module overview](index.md) ·
[Scenario answer framework](../interview-playbook/scenario-answer-framework.md)

Answer each aloud before reading the model. Lead with user/business outcome,
state assumptions, then cover objective, risk, response, ownership, and validation.

## 1. The CEO requests 100% availability

**Model answer:** Clarify critical journeys, harm, timing, alternatives, contracts,
and risk tolerance. Explain that distributed systems and planned change make an
absolute guarantee infeasible and can create disproportionate cost/complexity.
Use historical/user evidence to propose journey-specific SLO and recovery targets,
identify investment needed for higher levels, state residual risk, and let the
business owner choose with transparent trade-offs.

## 2. Define an SLO for checkout

**Model answer:** Identify valid checkout attempts and count good events only when
the user receives a correct terminal result within the chosen latency. Measure at
the user-facing boundary, segment material regions/payment methods, state window,
target, exclusions, data delay, owner, and dependency blind spots. Pair it with
multi-window burn alerts and a pre-agreed error-budget policy.

## 3. The team exhausted its error budget

**Model answer:** Confirm SLI quality and causes, current risk, and customer impact.
Apply the agreed policy: restrict high-risk change, prioritize the dominant
reliability work, allow security/mandatory/low-risk remediation with appropriate
review, and require risk-owner approval for exceptions. Do not freeze all change
or punish the team; some changes reduce risk. Define recovery and exit criteria.

## 4. Availability numbers imply the SLO cannot be met

**Model answer:** Map the actual critical path and whether dependencies are serial,
parallel, cached, optional, or degradable. Validate correlated failure and provider
SLA assumptions. Negotiate stronger dependency objectives, add containment/fallback,
redesign the flow, or adjust the product objective. Multiplying marketing figures
without topology and user semantics is not a reliability analysis.

## 5. Lead a severe production incident

**Model answer:** Declare severity and impact, assign commander, technical,
communications, and scribe roles, freeze unsafe change, establish channels and
update cadence, and pursue reversible stabilization before root cause. Keep a
fact/hypothesis/action timeline, control risky commands, verify recovery from the
user perspective, monitor recurrence, hand over residual work, then trigger review.

## 6. A rollback did not restore service

**Model answer:** Stop repeated blind rollback, reassess whether data, configuration,
dependency, cache, feature flag, or control plane is incompatible. Protect data and
blast radius, choose roll-forward, restore, failover, or degradation using evidence,
and communicate uncertainty. Later add compatibility contracts, migration sequencing,
rollback verification, and exercises that include state—not only binaries.

## 7. Design a blameless postmortem

**Model answer:** Document user impact and evidence-based timeline, then examine
technical and organizational conditions, detection, decisions, defenses, response,
and what worked. Ask why actions were reasonable with information available.
Create prioritized systemic actions with owners, due dates, risk, and verification;
track completion and share transferable learning without removing accountability.

## 8. On-call receives 50 pages per engineer each week

**Model answer:** Treat responder overload as reliability risk. Protect current
capacity with grouping/inhibition and escalation support, then analyze pages by
impact, rule, service, cause, action, time, and repeat frequency. Remove ownerless/
non-actionable pages, shift tickets, implement SLO symptom alerts, fix top causes,
staff fairly, and measure both load and missed detection.

## 9. Reduce toil by 50%

**Model answer:** Establish a task inventory and define toil consistently. Rank by
frequency, interruption, risk, growth, and engineering cost. Eliminate demand first,
simplify and self-serve next, automate deterministic work with safety controls,
and redesign systemic causes. Measure demand, time, errors, queue age, and capacity
returned—not scripts written or a forced percentage.

## 10. Plan capacity for a tenfold product event

**Model answer:** Model event shape, user mix, requests, state, background work,
cache coldness, retries, and failure conditions. Identify bottlenecks/quotas, test
representative load and data, pre-scale components with long lead time, protect
dependencies with shedding/backpressure, reserve failover headroom, define abort/
degrade plans, and monitor real demand against forecasts during the event.

## 11. Introduce chaos engineering

**Model answer:** Start from a known reliability risk and recovery hypothesis, not
a tool. Establish steady-state user/SLO measure, smallest fault scope, prerequisites,
observers, abort, rollback, authority, and communication. Begin outside production
or on a narrow cohort, prove detection/recovery, capture learning/actions, and
expand only as operational maturity and business value justify.

## 12. Choose an SRE organizational model

**Model answer:** Assess service criticality, product ownership, current maturity,
shared platform needs, staffing, incident load, and desired outcome. Embedded SRE
fits sustained deep partnership; consulting enables many teams; platform SRE builds
common capabilities; direct service SRE needs strict onboarding. Define engagement
entry/exit, responsibility, roadmap, and prevent SRE becoming a ticket queue.

## 13. A cloud provider region is degraded

**Model answer:** Measure critical journey impact and provider/dependency state,
stabilize load and protect data, then choose stay, degrade, traffic shift, or
failover using tested capacity and consistency criteria. Declare command and
provider escalation, communicate uncertainty, verify secondary dependencies and
recovery, and avoid a failover that creates a larger outage. Reconcile data later.

## 14. Release velocity conflicts with reliability

**Model answer:** Use SLO and error-budget evidence to make risk explicit. Improve
small changes, progressive exposure, automated verification, feature separation,
compatibility, and rollback/roll-forward so speed and safety reinforce each other.
When burn is high, temporarily restrict the riskiest changes and prioritize causes;
do not frame all feature work as the enemy of reliability.

## 15. Measure whether SRE is successful

**Model answer:** Use user SLO attainment and impact, detection/mitigation/recovery,
recurrence, change failure/blast radius, capacity forecast/headroom, toil and page
load, corrective-action verification, readiness adoption, and team health. Pair
numbers with business value and qualitative review; ticket closure or uptime alone
can hide brittle systems and exhausted people.

Return to the [module overview](index.md) when ready to continue.
