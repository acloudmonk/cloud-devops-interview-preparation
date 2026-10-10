# Design Exercise: Governed Kubernetes Platform Ecosystem

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

Use this no-code exercise to turn ecosystem choices into a supportable platform
product. Complete it on paper or in a Markdown note.

## Brief

A company operates twelve EKS clusters across development, staging, production, and
two regions. Teams independently adopted Helm, Kustomize, Argo CD, Flux, two ingress
controllers, two service meshes, multiple CNI modes, three autoscalers, two policy
engines, and four secret-delivery patterns.

Current problems:

- pipelines and GitOps controllers overwrite the same resources;
- charts expose hundreds of values and hooks perform database changes;
- emergency edits are reverted before incidents recover;
- admission webhooks occasionally block the API path;
- mesh retries amplify application retries and overload databases;
- autoscalers fight over replicas, requests, and nodes;
- CRDs and operators have no owners, backups, or upgrade order;
- EKS upgrades reveal add-on incompatibility late;
- teams cannot identify which add-on is mandatory, optional, or deprecated.

Constraints: AWS/EKS is primary, AKS/GKE portability matters for selected workloads,
regulated services require strong policy and identity evidence, and the platform team
has ten engineers.

## Your deliverable

Draw and explain:

1. requirement-to-capability map and criteria to retain, replace, consolidate, or remove;
2. source, package/customization, GitOps, API/admission, domain-controller, data-plane,
   cloud, and workload ownership boundaries;
3. supported Helm/Kustomize interface, rendered evidence, versioning, promotion, and rollback;
4. GitOps repository/tenancy/promotion/drift/emergency-change and continuity design;
5. CNI/eBPF and Gateway/mesh selection, identity, traffic, telemetry, and migration;
6. workload/event/node autoscaling ownership, metrics, stabilization, limits, and cost;
7. policy, secret, and certificate architecture including failure and compromise;
8. CRD/operator/add-on catalog, compatibility, backup, upgrade, and safe removal;
9. platform SLOs, troubleshooting evidence, support, documentation, and exception lifecycle;
10. staged adoption and decommission roadmap with measurable outcomes.

## Decision matrix

| Decision | State your choice and trade-off |
| --- | --- |
| Packaging | Helm, Kustomize, combination, interface, rendering, release ownership |
| Reconciliation | Argo CD/Flux/pipeline ownership, tenancy, drift, prune, emergency change |
| Network data plane | AWS VPC CNI/alternative/eBPF, policy, IP/MTU, support, migration |
| Traffic layer | LB/Ingress/Gateway/mesh/API gateway, identity, retry, telemetry, cost |
| Scaling | Metric/event/workload/node owner, interaction, stabilization, safeguards |
| Trust services | Admission, secrets, certificates, identity, HA, failure policy, audit |
| Operators | Approved use, CRD lifecycle, privilege, backup, version matrix, deletion |
| Fleet | Cluster/add-on versions, rollout cohorts, continuity, support, retirement |

## Ownership table

For replicas, resources, images, labels, routes, policies, Secrets, certificates,
nodes, and external resources, name the source of truth, only authoritative writer,
status producer, emergency process, drift policy, and recovery evidence.

## Adoption plan

A defensible sequence is inventory/controllers and privileges; freeze new add-ons;
define decision/ownership standards; consolidate configuration/GitOps; stabilize
admission and secret/certificate trust services; rationalize network/traffic/scaling;
build compatibility/upgrade evidence; then remove redundant components safely.

For each increment define a pilot, owner, support/SLO, user migration, success metric,
exception expiry, and rollback or forward-only boundary. Do not replace every tool in
one platform rewrite.

## Review rubric

- **Need:** every component maps to a measurable user or risk outcome.
- **Ownership:** no hidden or competing writer controls the same field/outcome.
- **Trust:** controller privilege, identity, supply chain, and failure policy are explicit.
- **Lifecycle:** compatibility, backup, upgrade, restore, removal, and external state are tested.
- **Portability:** upstream APIs and product/provider extensions are distinguishable.
- **Product:** supported interfaces, SLOs, documentation, costs, and adoption are owned.

Finish with a two-minute recommendation: consolidation priorities, top risks, target
platform contract, migration, measures, and the first decision required from leadership.
