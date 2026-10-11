# Rapid-Fire Revision

[← Presentation](presentation-template.md) · [Next: Flashcards →](flashcards.md)

Answer each in 20–40 seconds.

| # | Question | Strong answer cue |
| ---: | --- | --- |
| 1 | Resource hierarchy? | Organization, folders, projects, resources; inheritance downward. |
| 2 | Why projects? | Trust, API, quota, lifecycle, cost, and blast-radius boundary. |
| 3 | IAM versus Organization Policy? | Access authorization versus configuration constraint. |
| 4 | IAM deny? | Overrides applicable allows for specified permissions/principals. |
| 5 | Folder purpose? | Durable policy/delegation grouping, not workload runtime. |
| 6 | Budget behavior? | Alerts/automation signal; not guaranteed hard cap. |
| 7 | Global VPC? | Network global; subnets and many resources regional. |
| 8 | Zone? | Failure domain within a region. |
| 9 | Multi-region means DR? | No; inspect every dependency and write/recovery behavior. |
| 10 | Shared VPC? | Host project shares network resources with service projects. |
| 11 | VPC peering caveat? | Non-transitive; plan DNS/routes/firewalls/scale. |
| 12 | Cloud Router? | Dynamic route exchange, not packet forwarding appliance. |
| 13 | Cloud NAT? | Managed outbound NAT; no inbound connectivity. |
| 14 | Private Google Access? | Google APIs from eligible resources without external IP. |
| 15 | Private Service Connect? | Private service consumption/publication endpoints. |
| 16 | HA VPN versus Interconnect? | Internet encrypted agility versus private capacity/latency. |
| 17 | Global versus regional LB? | Client/backend scope, sovereignty, failover, protocol. |
| 18 | Cloud Armor? | Edge security policy; not secure application design replacement. |
| 19 | Service account? | Workload identity, not a person or secret container. |
| 20 | Avoid SA keys how? | Attached identity and workload identity federation. |
| 21 | VPC Service Controls? | Exfiltration boundary for supported services; complements IAM. |
| 22 | CMEK trade-off? | More control plus key availability and operations dependency. |
| 23 | Secret Manager? | Versioned secret storage/access; rotation still designed. |
| 24 | Audit log use? | Attribution and evidence; configure routing, retention, access. |
| 25 | MIG fit? | Managed VM fleet with health, autoscale, rollout, distribution. |
| 26 | GKE fit? | Kubernetes requirements justify its operational surface. |
| 27 | Cloud Run fit? | Stateless containers/jobs with managed scaling. |
| 28 | Cloud Run risk? | Burst/concurrency can exhaust downstream systems. |
| 29 | Functions fit? | Bounded event handlers with idempotent retry behavior. |
| 30 | App Engine fit? | Opinionated managed application runtime. |
| 31 | Cloud Storage location? | Choose from latency, durability, residency, cost, recovery. |
| 32 | Cloud SQL fit? | Managed familiar relational engine within scale/HA limits. |
| 33 | AlloyDB fit? | PostgreSQL-compatible workload needing its performance architecture. |
| 34 | Spanner fit? | Horizontally scalable relational consistency when justified. |
| 35 | Firestore fit? | Document access patterns within query/index constraints. |
| 36 | Bigtable fit? | Low-latency wide-column access with deliberate row keys. |
| 37 | BigQuery fit? | Analytical warehouse, not an OLTP default. |
| 38 | HA versus backup? | Availability preserves service; backup recovers past state. |
| 39 | Pub/Sub default delivery? | At least once; design idempotency and duplicates. |
| 40 | Ordering key trade-off? | Required order can constrain throughput and recovery. |
| 41 | Cloud Tasks fit? | Rate-controlled deferred delivery to a target. |
| 42 | Eventarc fit? | Routing supported events to destinations. |
| 43 | Workflows fit? | Managed step orchestration and compensation logic. |
| 44 | Replay safety? | Authorized, bounded, idempotent, observable, reconciled. |
| 45 | SLI? | Measured indicator of user-relevant service behavior. |
| 46 | SLO? | Target for an SLI over a window. |
| 47 | Error budget? | Allowed unreliability guiding risk and change decisions. |
| 48 | Useful queue alert? | Oldest age and business delay, not only depth. |
| 49 | Restore proof? | Isolated restore plus technical and business validation. |
| 50 | Regional failover capacity? | Compute, data, IP, quota, keys, network, operators. |
| 51 | Quota role? | Finite reliability boundary; forecast and alarm. |
| 52 | Committed use discount? | Discount for predictable commitment; not rightsizing. |
| 53 | Spot VM fit? | Interruption-tolerant, checkpointed/retryable work. |
| 54 | Unit cost? | Spend divided by value measure such as order/tenant. |
| 55 | Six WAF pillars? | Operations, security, reliability, cost, performance, sustainability. |
| 56 | Strong risk statement? | Condition, failure, impact, and evidence. |
| 57 | Strong decision record? | Context, options, choice, trade-offs, evidence, triggers. |
| 58 | Landing zone? | Evolving governed foundation, not a one-time network. |
| 59 | Break glass? | Minimal, protected, monitored, tested emergency access. |
| 60 | Best interview structure? | Clarify, decide, justify, fail, operate, verify. |

## Spoken question set

Use the compact table above as the answer key.

1. **What is the Google Cloud resource hierarchy?**
2. **Why use separate projects?**
3. **How do IAM and Organization Policy differ?**
4. **What does an IAM deny policy do?**
5. **Why use folders?**
6. **Does a Cloud Billing budget cap spend?**
7. **What is global about a VPC network?**
8. **What is a zone?**
9. **Does multi-region automatically provide disaster recovery?**
10. **What is Shared VPC?**
11. **What important limitation does VPC Network Peering have?**
12. **What does Cloud Router do?**
13. **What does Cloud NAT do?**
14. **What is Private Google Access?**
15. **What is Private Service Connect?**
16. **When would you compare HA VPN with Cloud Interconnect?**
17. **How do global and regional load-balancing choices differ?**
18. **What does Cloud Armor provide?**
19. **What is a service account?**
20. **How can a workload avoid service-account keys?**
21. **What do VPC Service Controls provide?**
22. **What trade-off does CMEK introduce?**
23. **What does Secret Manager provide?**
24. **Why retain Cloud Audit Logs?**
25. **When does a managed instance group fit?**
26. **When does GKE fit?**
27. **When does Cloud Run fit?**
28. **What downstream risk can Cloud Run scaling create?**
29. **When do Cloud Run functions fit?**
30. **When does App Engine fit?**
31. **How should you choose a Cloud Storage location?**
32. **When does Cloud SQL fit?**
33. **When does AlloyDB fit?**
34. **When does Spanner fit?**
35. **When does Firestore fit?**
36. **When does Bigtable fit?**
37. **When does BigQuery fit?**
38. **How do high availability and backup differ?**
39. **What is Pub/Sub's default delivery behavior?**
40. **What trade-off does an ordering key create?**
41. **When does Cloud Tasks fit?**
42. **When does Eventarc fit?**
43. **When do Workflows fit?**
44. **What makes replay safe?**
45. **What is an SLI?**
46. **What is an SLO?**
47. **What is an error budget?**
48. **What is a useful queue-backlog alert?**
49. **What proves a restore succeeded?**
50. **What must regional failover capacity include?**
51. **Why are quotas architecture concerns?**
52. **What is a committed use discount?**
53. **When do Spot VMs fit?**
54. **What is unit cost?**
55. **What are the six Well-Architected pillars?**
56. **What makes a strong risk statement?**
57. **What makes a strong architecture decision record?**
58. **What is a landing zone?**
59. **What is break-glass access?**
60. **What is the recommended interview-answer loop?**
