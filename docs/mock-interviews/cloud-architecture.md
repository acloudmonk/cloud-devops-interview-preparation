# Mock Interview: Cloud Architecture and Distributed Systems

[← Module overview](../01-cloud-architecture/index.md) ·
[Master competency map](../master-competency-map.md)

Use this 50-minute interview after completing the pilot module. A study partner
can act as interviewer, or you can record yourself and reveal each follow-up
only when its time begins.

## Candidate brief

A ticketing company expects one million visitors during a 15-minute on-sale
window. Customers browse events, reserve seats for five minutes, and pay through
an external provider. The existing single-region application slows down under
load and has occasionally sold the same seat twice.

Design an AWS-based architecture. The business wants a credible path to higher
availability but has a small platform team and must control cost.

## Interview schedule

| Time | Candidate task | Interviewer observes |
| --- | --- | --- |
| 0–5 min | Clarify outcomes, constraints, and assumptions | Discovery discipline; avoidance of premature service selection |
| 5–12 min | Estimate demand and define SLOs, RTO, and RPO | Quantitative reasoning and handling of uncertainty |
| 12–25 min | Present the logical design and main data flows | Boundaries, state ownership, consistency, and AWS mapping |
| 25–35 min | Respond to failure and scale follow-ups | Degradation, observability, diagnosis, recovery, and blast radius |
| 35–42 min | Address security, cost, and delivery | Practical judgment beyond the happy path |
| 42–47 min | Compare an alternative and phase the change | Trade-offs and migration safety |
| 47–50 min | Give an executive summary | Clear recommendation, risks, and next decision |

Do not try to mention every AWS service. Explain why each major component is
needed and what behavior it provides.

## Core follow-ups

Ask these after the candidate presents the initial design.

1. The database shows low average CPU, but reservation latency is rising. What
   do you inspect first, and why?
2. The payment provider times out after accepting some charges. How do you avoid
   charging twice while eventually resolving the order?
3. A sudden bot surge consumes most admission capacity. How do you preserve
   fairness and legitimate-user access?
4. One Availability Zone is impaired. Describe detection, traffic behavior,
   state implications, and recovery.
5. The product owner asks for active-active regional writes next month. What
   questions must be answered before accepting that solution?

## Branching follow-ups

Choose two based on the candidate's design.

| If the candidate chooses… | Ask… |
| --- | --- |
| DynamoDB for reservations | How will the key design avoid hot partitions, and where are conditional writes required? |
| Aurora for reservations | What is the contention strategy, and how will connection pressure and failover be handled? |
| Synchronous calls throughout | Which dependency should be decoupled first, and what consistency change follows? |
| SQS for order processing | What are the duplicate, ordering, poison-message, and backlog-drain behaviors? |
| Multi-region active-active | Who owns a seat during a partition, and how are conflicting writes prevented or resolved? |
| A cache in the write path | What happens on stale data, cache loss, or partial invalidation? |
| Lambda for burst handling | Which concurrency, downstream-capacity, timeout, and retry limits protect the system? |
| EKS or ECS | Why does the team's operating model justify that compute choice? |

## Evidence expected in a strong answer

- explicit load assumptions and a small amount of defensible arithmetic;
- a consistency boundary that prevents duplicate seat ownership;
- admission control, backpressure, bounded retries, and idempotency;
- separate treatment of browse, reserve, payment, and notification paths;
- customer-facing SLIs plus dependency and saturation signals;
- defined degraded modes and manual operational decisions;
- security and abuse controls at each trust boundary;
- an incremental rollout with validation and rollback gates;
- one credible alternative and the conditions under which it becomes preferable.

## Scorecard

Score each dimension from 0 to 4. Record evidence, not impressions.

| Dimension | 0–1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- |
| Discovery | Jumps to a solution | Covers common requirements | Prioritizes measurable constraints | Exposes business ambiguity that could change the design |
| Quantitative reasoning | No scale model | Rough numbers without consequences | Links estimates to capacity and SLOs | Tests sensitivity and explains validation |
| Architecture | Service list or unclear flow | Plausible happy path | Clear boundaries and state ownership | Evolvable design with bounded blast radius |
| Distributed systems | Ignores duplicates/partitions | Names patterns | Applies consistency, idempotency, and backpressure correctly | Explains edge cases and impossibility/trade-offs precisely |
| Reliability | Says “multi-AZ” only | Names failure controls | Defines degradation, detection, and recovery | Connects SLOs, error budget, RTO/RPO, and testing |
| Operations | Little diagnostic detail | Basic logs/metrics | Customer SLIs, saturation, tracing, runbooks | Hypothesis-led diagnosis and safe operational controls |
| Security and abuse | Missing | Generic security list | Trust boundaries and layered controls | Risk-based controls integrated with availability and fairness |
| Economics and delivery | Missing | Mentions cost or phases | Identifies drivers and staged rollout | Quantifies decision triggers and reversible migration gates |
| Trade-offs | One “best” solution | Superficial alternative | Compares credible options | States when the recommendation should change |
| Communication | Unstructured | Understandable | Concise, signposted, audience-aware | Controls time and turns complexity into clear decisions |

Maximum score: **40**.

- **32–40:** strong architect-level signal; refine weak dimensions.
- **24–31:** sound foundation; repeat after targeted study.
- **16–23:** reasoning is incomplete or too service-led; revisit the module.
- **0–15:** rebuild fundamentals before adding more platform detail.

The thresholds guide practice; they are not hiring standards.

## Reflection and repeat loop

After the interview, write down:

1. the first moment your answer became unclear;
2. one missed clarifying question;
3. one unsupported assumption or calculation;
4. one failure mode you handled weakly;
5. one answer that should be shortened;
6. the single skill to practise before repeating the interview.

Repeat the same prompt within seven days. Keep the requirements constant so
that improvement in reasoning and communication is visible.
