# Mock Interview: Kubernetes Ecosystem Strategy

[← Kubernetes Ecosystem module overview](../12-kubernetes-ecosystem/index.md) ·
[Master competency map](../master-competency-map.md)

Use this 50-minute interview after completing Module 12. Reveal follow-ups only
when their section begins.

## Candidate brief

A 350-engineer organization runs twelve EKS clusters. Teams adopted overlapping Helm,
Kustomize, Argo CD, Flux, ingress, mesh, CNI, autoscaling, policy, secret, certificate,
and operator stacks. Controllers overwrite one another, webhooks block deployments,
retries amplify outages, autoscalers create cost spikes, and upgrades reveal CRD/add-on
incompatibility. Design a supported platform ecosystem and migration.

## Schedule

| Time | Candidate task | Interviewer observes |
| --- | --- | --- |
| 0–5 min | Clarify users, outcomes, constraints, pain, risk, skills, and cost | Discovery before tool selection |
| 5–12 min | Inventory capabilities, controllers, identities, data planes, and ownership | Ecosystem mental model |
| 12–20 min | Design packaging/customization, GitOps, promotion, drift, and emergency change | Source and reconciliation |
| 20–29 min | Select CNI/eBPF, Gateway/ingress/mesh, traffic identity, and migration | Network architecture judgment |
| 29–36 min | Coordinate autoscaling, capacity, metrics, disruption, and safeguards | Control-loop reasoning |
| 36–43 min | Design policy, secrets, certificates, operators, CRDs, and trust recovery | Security and lifecycle |
| 43–50 min | Present consolidation, upgrades, support, SLOs, adoption, and recommendation | Platform leadership |

## Required follow-ups

1. Two GitOps controllers own the same resources. How do you restore authority safely?
2. A conversion webhook outage blocks access to critical custom resources. Recover.
3. Mesh retries amplify a database outage. What changes immediately and permanently?
4. A CNI upgrade leaves every new node NotReady. What evidence and rollback path matter?
5. An operator uninstall begins deleting cloud databases. How do you contain it?

## Decision follow-ups

| Candidate choice | Ask |
| --- | --- |
| Standardize on Helm | How do values, rendered review, hooks, CRDs, secrets, and rollback remain safe? |
| Standardize on one GitOps tool | How are tenancy, promotion, emergency change, continuity, and migration handled? |
| Deploy a service mesh everywhere | Which measurable requirement justifies universal data-plane cost/risk? |
| Adopt eBPF data plane | Which kernel/support/migration/debug assumptions are proven? |
| Use several autoscalers | Which controller owns replicas, requests, nodes, and Git-managed fields? |
| Enforce policy fail-closed | How do webhook outage, bootstrap, upgrades, and break-glass work? |

## Scorecard

Score each dimension from 0 to 4.

| Dimension | 0–1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- |
| Discovery | Lists favorite tools | Basic feature questions | Users, outcomes, risk, skill, cost | Finds constraints that remove components |
| Ownership model | Tool pipeline | Some controllers | Source/field/controller/data/identity map | Predicts reconciliation and dependency cycles |
| Packaging/GitOps | Generic Helm/Argo | Plausible workflow | Rendered evidence, tenancy, drift, emergency | Migration and continuity proven |
| Network/traffic | Product names | Basic CNI/mesh | Path, identity, policy, retries, migration | Data-plane failure and portability integrated |
| Scaling | “Use HPA/Karpenter” | Metrics and nodes | Interacting loops, lag, safeguards, downstream | Stability/cost evidence under failure |
| Trust/lifecycle | Policy/secrets named | Some HA/RBAC | Admission/secret/cert/CRD identity and recovery | Compromise, conversion, removal handled |
| Operations | Upgrade charts | Inventory/monitoring | Dependency order, skew, backup, SLO, support | Irreversible state and fleet continuity |
| Leadership | Vendor-logo slide | Understandable | Minimum stack, consolidation, adoption, measure | Concise trade-off with owner/evidence |

Maximum score: **32**. A score of 25 or more with no dimension below 2 is a
strong senior-level practice result.

## Reflection

Record one unjustified component, one conflicting owner, one hidden trust dependency,
one unsafe removal assumption, and one answer to shorten. Repeat within seven days.
