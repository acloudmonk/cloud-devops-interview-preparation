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
