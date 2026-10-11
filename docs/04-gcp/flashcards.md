# Active-Recall Flashcards

[← Rapid fire](rapid-fire.md) · [Next: Mock interview →](../mock-interviews/gcp-architecture.md)

Hide the answer, speak first, then mark **again**, **hard**, or **good**.

| # | Front | Back |
| ---: | --- | --- |
| 1 | GCP hierarchy | Organization → folders → projects → resources. |
| 2 | Project boundary | IAM, API, quota, lifecycle, billing, blast radius. |
| 3 | Organization Policy | Constraint on resource configuration/behavior. |
| 4 | IAM deny | Prevents specified permissions despite applicable allow. |
| 5 | Global VPC | Network global; subnets regional. |
| 6 | Shared VPC roles | Host owns shared network; service projects run workloads. |
| 7 | Cloud NAT | Outbound translation, not inbound access. |
| 8 | Private Google Access | Private-address resources reach supported Google APIs. |
| 9 | Private Service Connect | Private endpoint between service consumer and producer. |
| 10 | Cloud Router | Exchanges dynamic routes with BGP peers. |
| 11 | Workload Identity Federation | Short-lived access from external workloads without SA keys. |
| 12 | WIF for GKE | Maps Kubernetes workload identity to Google Cloud access. |
| 13 | VPC Service Controls | Defense against exfiltration for supported managed services. |
| 14 | CMEK obligation | Key policy, availability, rotation, location, and recovery. |
| 15 | MIG | Health-managed, scalable VM fleet. |
| 16 | Cloud Run guardrail | Bound concurrency/instances to protect dependencies. |
| 17 | Spanner decision | Relational consistency plus horizontal scale must justify it. |
| 18 | Bigtable key risk | Poor row-key distribution creates hotspots. |
| 19 | Pub/Sub default | At-least-once delivery; consumers need idempotency. |
| 20 | Cloud Tasks | Controlled deferred delivery rather than event broadcast. |
| 21 | Oldest message age | Better backlog urgency signal than count alone. |
| 22 | HA versus backup | Continuity versus recovery of prior state. |
| 23 | RTO | Maximum target recovery time. |
| 24 | RPO | Maximum target data-loss interval. |
| 25 | Error budget | Permitted unreliability over the SLO window. |
| 26 | Failure headroom | Capacity available while components are unavailable. |
| 27 | Budget caveat | Usually notification, not a hard spending ceiling. |
| 28 | Unit economics | Cost tied to a business-value denominator. |
| 29 | Six pillars | Operations, security, reliability, cost, performance, sustainability. |
| 30 | Answer loop | Clarify → decide → justify → fail → operate → verify. |
