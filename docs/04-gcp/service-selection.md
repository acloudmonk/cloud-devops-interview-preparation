# GCP Service-Selection Matrices

[← Integration](integration-services.md) · [Next: Reliability and operations →](reliability-operations.md)

Matrices create a shortlist; current documentation, prototypes, quotas, and failure
tests validate the decision.

## Compute

| Criterion | Compute Engine/MIG | GKE | Cloud Run | Functions |
| --- | --- | --- | --- | --- |
| Control | High | Kubernetes | Managed container | Managed function |
| Best fit | legacy/specialized | K8s portfolios | stateless services/jobs | bounded handlers |
| Watch | patching/capacity | complexity/upgrades | limits/concurrency | limits/retries |

## Data

| Service | Model | Primary question |
| --- | --- | --- |
| Cloud SQL | managed relational | Does engine, scale, and HA fit? |
| AlloyDB | PostgreSQL-compatible | Does its compatibility/performance fit? |
| Spanner | distributed relational | Is horizontal scale/consistency justified? |
| Firestore | document | Do queries and indexes fit? |
| Bigtable | wide-column | Does key design match access? |

## Connectivity

| Requirement | Evaluate |
| --- | --- |
| Encrypted internet hybrid | HA VPN |
| Private high-throughput hybrid | Dedicated/Partner Interconnect |
| Private published service | Private Service Connect |
| Google APIs without external IP | Private Google Access |
| Global external HTTP(S) | Global external Application Load Balancer |

Record context, candidates, decision, rejected alternatives, security, failure,
operational owner, cost, evidence, assumptions, and review/exit triggers.
