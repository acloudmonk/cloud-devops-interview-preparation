# Ten-Minute Architecture Presentation

Last reviewed: **2026-10-07**

The goal is not to describe every box. Demonstrate that you can turn ambiguity
into a defensible, operable decision.

## Suggested timing

| Time | Content | Evidence of seniority |
| ---: | --- | --- |
| 0:00–1:00 | Outcome, users, critical journey | Business framing before technology |
| 1:00–2:00 | Assumptions and NFRs | Scale, latency, availability, RTO/RPO, residency |
| 2:00–4:00 | Architecture and data flow | Clear sync/async and state boundaries |
| 4:00–5:30 | Correctness and failure behavior | Invariants, idempotency, overload, recovery |
| 5:30–6:30 | Security and trust boundaries | Identity, secrets, encryption, abuse, audit |
| 6:30–7:30 | Operations | SLOs, telemetry, deployment, rollback, ownership |
| 7:30–8:30 | Options and trade-offs | Credible alternative and reason for selection |
| 8:30–9:30 | Cost and delivery | Cost drivers and incremental milestones |
| 9:30–10:00 | Risks and validation | What could invalidate the design and how to test |

## One-page speaking canvas

```text
Outcome:
Critical journey:
Top three assumptions:
Scale and growth:
Latency / availability / RTO / RPO:
Correctness invariant:

Recommended option:
Alternative:
Why selected:
Accepted trade-off:

Request and data flow:
Failure behavior:
Security boundary:
Operational evidence:
Cost drivers:
Delivery phases:
Top risks and tests:
```

## Diagram discipline

Use roughly seven to twelve primary boxes. Show:

- users and external dependencies;
- edge and trust boundaries;
- synchronous request path;
- asynchronous path;
- systems of record and caches;
- telemetry and operator control.

Add a second sequence or failure diagram when it explains behavior better than
adding more arrows to the main diagram.

## Challenge questions to rehearse

1. Which component fails first at twice the estimated peak?
2. Why is this not over-engineered for the initial deadline?
3. What is the simplest alternative?
4. What data can be lost, and how do you know?
5. What happens after payment succeeds but the response is lost?
6. How do you deploy a backward-incompatible data change?
7. What does an operator see during degradation?
8. What would you remove if the budget were cut by 30%?
9. Which cloud-specific choice is hardest to reverse?
10. What evidence would cause you to change your recommendation?

## Self-review rubric

| Level | Signal |
| --- | --- |
| Basic | Describes components and the happy path |
| Strong | Quantifies requirements and explains state, failure, and security |
| Senior | Compares options and covers operations, recovery, cost, and delivery |
| Principal | Connects decisions to business risk, ownership, governance, and evidence |

Record yourself once. Remove filler, service-name lists, and claims that lack a
metric, owner, failure boundary, or validation method.
