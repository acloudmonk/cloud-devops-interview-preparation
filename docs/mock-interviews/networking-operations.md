# Mock Interview: Cloud Networking Operations

[← Networking module overview](../07-networking/index.md) ·
[Master competency map](../master-competency-map.md)

Use this 50-minute interview after completing Module 07. Reveal follow-ups only
when their section begins.

## Candidate brief

A public API runs across three AWS Availability Zones and connects privately to
one data center. After a DNS cutover, some clients reach the old endpoint; peak
traffic produces outbound timeouts; and a recent firewall change affects only
one zone. Design the network and lead diagnosis without deploying resources.

## Schedule

| Time | Candidate task | Interviewer observes |
| --- | --- | --- |
| 0–5 min | Clarify flows, users, objectives, constraints, and changes | Discovery before products |
| 5–14 min | Draw DNS-to-dependency forward and return paths | Layer and ownership model |
| 14–24 min | Diagnose inconsistent DNS and zonal failure | Hypotheses and discriminating evidence |
| 24–33 min | Diagnose peak outbound timeouts | NAT/state/capacity reasoning |
| 33–41 min | Design ingress, egress, hybrid, and failover | Security/reliability/cost trade-offs |
| 41–46 min | Translate key decisions to Azure and GCP | Semantic multi-cloud knowledge |
| 46–50 min | Give an executive incident/design summary | Concision and ownership |

## Required follow-ups

1. Authoritative DNS is correct. Why can clients still see the old endpoint?
2. Aggregate egress bandwidth is moderate. What finite state can be exhausted?
3. A route exists from the failing subnet. What does that fail to prove?
4. Small requests work through the VPN but large uploads stall. Explain.
5. The backup circuit has routes but cannot carry full demand. What is recovery?

## Branching follow-ups

| Candidate choice | Ask |
| --- | --- |
| Lower DNS TTL now | Which caches already hold the previous TTL? |
| Open the firewall | What exact flow, duration, approval, rollback, and evidence? |
| Add NAT capacity | What distinguishes port/state exhaustion from bandwidth? |
| Fail over Region | Are data, DNS, certificates, dependencies, and capacity ready? |
| Capture packets | At which boundary, with what filter and data controls? |
| Add retries | Which layer owns retry and is the operation idempotent? |

## Scorecard

Score each dimension from 0 to 4.

| Dimension | 0–1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- |
| Discovery | Starts with tools | Basic topology questions | Customer, flow, scope, time, change | Finds ambiguity that changes architecture |
| Flow model | Lists components | Plausible forward path | DNS through return path and state | Names every trust/ownership boundary |
| Diagnosis | Random checks | Useful checks | Falsifiable hypotheses and comparison | Minimal decisive evidence with privacy controls |
| DNS/TLS | Record/cert trivia | Basic mechanisms | Cache/delegation/identity reasoning | Safe convergence and trust lifecycle |
| Routing/security | Route means success | Mentions policies | Directional routes, state, least privilege | Handles asymmetric/transit failure safely |
| Resilience | Adds redundancy | Multiple paths | Independent failure domains and capacity | Convergence, sessions, failback, testing |
| Multi-cloud | Product-name map | Rough equivalents | Explains semantic differences | Adjusts design because of those differences |
| Communication | Tool dump | Understandable | Structured, concise, decision-oriented | Controls time and executive risk discussion |

Maximum score: **32**. A score of 25 or more with no dimension below 2 is a
strong senior-level practice result.

## Reflection

Record one missed requirement, one incorrect layer assumption, one unsafe
change, one missing verification signal, and one answer to shorten. Repeat the
same prompt within seven days.
