# Design Exercise: Governed Multi-Account EKS Platform

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

Use this no-code exercise to convert Kubernetes mechanics into an architect-level
design. Complete it on paper or in a Markdown note.

## Brief

A company is moving 45 services from separate ECS clusters to Kubernetes. Ten teams
need development and production environments across two AWS regions. Workloads include
public APIs, workers, scheduled jobs, a three-member database, node-level security
agents, and a sandbox that executes partner-supplied code.

Current proposals contain these risks:

- one shared production cluster and one broad administrator role;
- every Pod inherits node IAM permissions and unrestricted egress;
- no resource requests, limits, quotas, topology spread, or disruption budgets;
- liveness probes call shared databases and restart all replicas during outages;
- stateful workloads use EBS without zone, backup, quorum, or restore planning;
- public Services are created independently with mutable image tags;
- add-ons and Kubernetes versions have no ownership or upgrade policy;
- teams expect namespaces to isolate hostile partner code.

Constraints: EKS is the approved AWS platform, regulated workloads need separation,
bad-release recovery objective is ten minutes, one availability zone may fail, and
the platform team has eight engineers.

## Your deliverable

Draw and explain:

1. AWS account, VPC, region, cluster, namespace, node, Pod, data, and identity boundaries;
2. control-plane access, human authentication, RBAC, workload identity, admission,
   audit, and emergency authority;
3. workload primitive and lifecycle standards for APIs, workers, jobs, agents, data,
   and partner code;
4. node pools/Fargate or stronger sandbox choices, placement, topology, capacity,
   upgrades, and autoscaling;
5. ingress, Service/DNS, endpoint, egress, network-policy, TLS, and load-balancer paths;
6. StorageClass, EBS/EFS/external data, zone, attachment, backup, restore, and quorum;
7. requests/limits, quotas, health probes, rollout, PDB, termination, and observability;
8. version/add-on ownership, compatibility testing, maintenance, and continuity;
9. one-zone, API, DNS, registry, IAM, webhook, CNI/CSI, and regional failure response;
10. adoption stages, developer experience, exceptions, evidence, and success measures.

## Required decisions

| Decision | State your choice and trade-off |
| --- | --- |
| Cluster/account topology | Shared, dedicated, or risk-tiered; blast radius versus cost/operations |
| Node/runtime boundary | Managed nodes, Fargate, dedicated pools, sandbox; feature versus isolation |
| Human/workload identity | AWS authentication, RBAC, Pod AWS role, rotation, audit, break-glass |
| Placement/capacity | Requests, topology, taints, priority, autoscaling, failure headroom |
| Traffic | Public/private entry, targets, DNS, policy, egress, source identity |
| State | Managed service versus in-cluster, class/topology, backup/restore/quorum |
| Lifecycle | Health, rollout, compatibility, disruption, shutdown, rollback/forward |
| Upgrades | Versions, add-ons, compatibility, order, surge, observation, recovery |

## Evidence matrix

For source/image digest, API change, admission, identity/RBAC, scheduling, deployment,
load balancing, storage operation, scaling, disruption, and recovery, record producer,
trusted identity, storage, consumer, retention, and failure behavior.

## Adoption plan

A defensible sequence is inventory and workload classification; create a platform
contract; establish identity/RBAC/admission/audit; pilot stateless internal services;
add capacity and network standards; prove one-zone disruption and upgrades; onboard
stateful workloads only after restore tests; then isolate regulated/hostile workloads.

For each increment name a pilot, owner, measurable outcome, exception expiry, rollback
of the process change, and support model. Do not build a giant platform API before
learning from representative workloads.

## Review rubric

- **Reconciliation:** object owners and desired-state sources are unambiguous.
- **Isolation:** API, cloud identity, runtime, network, node, cluster/account, and data
  boundaries match risk.
- **Availability:** topology, capacity, probes, disruption, data, and traffic agree.
- **Operations:** upgrades, evidence, debugging, continuity, and recovery are executable.
- **Portability:** upstream contracts are separated from EKS-specific integrations.
- **Adoption:** the paved path is usable, measured, owned, and not bypass-driven.

Finish with a two-minute recommendation: context, top risks, platform boundaries,
migration, recovery, measures, and the first decision required from leadership.
