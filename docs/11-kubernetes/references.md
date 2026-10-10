# Kubernetes References and Videos

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last verified: **2026-10-10**

Prefer upstream specifications and official managed-service documentation for behavior
that changes. Verify version, feature state, platform support, quotas, and deprecations
before using guidance in production.

## Architecture and API machinery

- [Kubernetes concepts](https://kubernetes.io/docs/concepts/)
  — authoritative entry point for architecture, workloads, services, storage, config,
  security, policy, scheduling, and administration.
- [Kubernetes components](https://kubernetes.io/docs/concepts/overview/components/)
  — control-plane and node-component responsibilities.
- [Controllers](https://kubernetes.io/docs/concepts/architecture/controller/)
  — control loops, desired/current state, API-mediated action, and controller design.
- [Kubernetes API concepts](https://kubernetes.io/docs/reference/using-api/api-concepts/)
  — resource versions, watches, consistency, pagination, concurrency, and streaming.
- [Server-side apply](https://kubernetes.io/docs/reference/using-api/server-side-apply/)
  — declarative field management, managers, conflicts, and merge behavior.
- [Owners and dependents](https://kubernetes.io/docs/concepts/overview/working-with-objects/owners-dependents/)
  and [finalizers](https://kubernetes.io/docs/concepts/overview/working-with-objects/finalizers/)
  — garbage-collection relationships and deletion cleanup.
- [etcd documentation](https://etcd.io/docs/)
  — consensus, operations, recovery, performance, security, and version behavior.

## Workloads, placement, and scaling

- [Workload management](https://kubernetes.io/docs/concepts/workloads/controllers/)
  — Deployments, StatefulSets, DaemonSets, Jobs, CronJobs, and workload selection.
- [Pod lifecycle](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/)
  — phases, container states, conditions, probes, restart, and termination.
- [Configure probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)
  — startup, readiness, liveness, handlers, timing, and failure behavior.
- [Disruptions](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/)
  — voluntary/involuntary disruption and PodDisruptionBudget semantics.
- [Scheduling, preemption, and eviction](https://kubernetes.io/docs/concepts/scheduling-eviction/)
  — placement, topology, taints, priority, preemption, and node pressure.
- [Resource management](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)
  — requests, limits, CPU/memory behavior, Pod resources, and extended resources.
- [Horizontal Pod Autoscaling](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/)
  — metrics, algorithm, readiness, behavior, stabilization, and limitations.

## Networking and storage

- [Services, load balancing, and networking](https://kubernetes.io/docs/concepts/services-networking/)
  — Pod network model, Services, EndpointSlices, ingress/Gateway, and NetworkPolicy.
- [DNS for Services and Pods](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/)
  — records, namespaces, search domains, Pod hostnames, and headless Services.
- [Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
  — selection, isolation, additive allow rules, and implementation prerequisites.
- [Persistent volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)
  — PV/PVC lifecycle, access modes, reclaim, binding, expansion, and protection.
- [Storage classes](https://kubernetes.io/docs/concepts/storage/storage-classes/)
  — dynamic provisioning, reclaim policy, binding mode, topology, and parameters.
- [CSI documentation](https://kubernetes-csi.github.io/docs/)
  — Kubernetes CSI deployment, features, sidecars, snapshots, and driver contracts.

## Security and operations

- [Kubernetes security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/)
  — API, workload, network, authentication, authorization, logging, and supply-chain checks.
- [RBAC good practices](https://kubernetes.io/docs/concepts/security/rbac-good-practices/)
  — least privilege and indirect escalation through workloads, tokens, binding, and webhooks.
- [Service accounts](https://kubernetes.io/docs/concepts/security/service-accounts/)
  — workload identities, projected tokens, RBAC, and external use.
- [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/)
  and [Pod Security Admission](https://kubernetes.io/docs/concepts/security/pod-security-admission/)
  — privileged/baseline/restricted profiles and namespace enforcement modes.
- [Secrets good practices](https://kubernetes.io/docs/concepts/security/secrets-good-practices/)
  — access, storage, encryption, lifecycle, and workload-consumption guidance.
- [Auditing](https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/)
  — policy, stages, backends, metadata, and sensitive-data considerations.
- [Troubleshooting applications](https://kubernetes.io/docs/tasks/debug/debug-application/)
  and [clusters](https://kubernetes.io/docs/tasks/debug/debug-cluster/)
  — official diagnostic entry points.
- [Version skew policy](https://kubernetes.io/releases/version-skew-policy/)
  and [API deprecation policy](https://kubernetes.io/docs/reference/using-api/deprecation-policy/)
  — supported component relationships and API lifecycle guarantees.

## Amazon EKS anchor

- [Amazon EKS Best Practices Guide](https://docs.aws.amazon.com/eks/latest/best-practices/introduction.html)
  — security, reliability, networking, scaling, autoscaling, and upgrades.
- [EKS reliability guidance](https://docs.aws.amazon.com/eks/latest/best-practices/reliability.html)
  — control-plane, data-plane, application, and shared-responsibility practices.
- [EKS networking guidance](https://docs.aws.amazon.com/eks/latest/best-practices/networking.html)
  — VPC CNI, address capacity, modes, and operational recommendations.
- [EKS security guidance](https://docs.aws.amazon.com/eks/latest/best-practices/security.html)
  — identity, data, Pod/node/runtime, network, detection, and infrastructure controls.
- [EKS workload AWS access](https://docs.aws.amazon.com/eks/latest/userguide/service-accounts.html)
  — Kubernetes service accounts, IAM roles for service accounts, and EKS Pod Identity.
- [EKS access entries](https://docs.aws.amazon.com/eks/latest/userguide/access-entries.html)
  — current cluster-access identity and authorization management.
- [EKS cluster-upgrade guidance](https://docs.aws.amazon.com/eks/latest/best-practices/cluster-upgrades.html)
  — API deprecations, add-ons, control/data-plane order, and in-place/blue-green choices.
- [EKS add-ons](https://docs.aws.amazon.com/eks/latest/userguide/eks-add-ons.html)
  — supported operational software, versions, configuration, and ownership.
- [EBS CSI](https://docs.aws.amazon.com/eks/latest/userguide/ebs-csi.html)
  and [EFS CSI](https://docs.aws.amazon.com/eks/latest/userguide/efs-csi.html)
  — AWS block/shared storage integration and identity prerequisites.

## AKS and GKE translation

- [AKS Well-Architected guidance](https://learn.microsoft.com/azure/well-architected/service-guides/azure-kubernetes-service)
  — reliability, security, cost, operations, and performance decisions.
- [Secure an AKS deployment](https://learn.microsoft.com/azure/aks/secure-aks)
  — control-plane, identity, network, node, data, monitoring, backup, and governance.
- [AKS storage and backup practices](https://learn.microsoft.com/azure/aks/operator-best-practices-storage)
  — Azure Disk/File choices, provisioning, protection, and restore validation.
- [GKE best practices](https://cloud.google.com/kubernetes-engine/docs/best-practices)
  — cluster, workload, networking, security, scaling, and operations guidance.
- [GKE enterprise multi-tenancy](https://cloud.google.com/kubernetes-engine/docs/best-practices/enterprise-multitenancy)
  — project/cluster/namespace topology, identity, networking, resources, and fleet concerns.
- [Harden GKE cluster security](https://cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster)
  — control-plane, nodes, workloads, identity, network, data, and audit controls.

## Videos

- [AWS re:Invent 2024 — Building production-grade resilient architectures with Amazon EKS](https://www.youtube.com/watch?v=g9USwIPr7Xs)
  — official AWS session on resilience, fleet operations, upgrades, and observability.
- [AWS re:Invent 2024 — How to build scalable platforms with Amazon EKS](https://www.youtube.com/watch?v=WkPrmHKZsq4)
  — official AWS platform-architecture session. Keep ecosystem-specific details for
  Module 12 and verify current features in the EKS documentation.

Official channels for newer material:

- [Kubernetes](https://www.youtube.com/@KubernetesCommunity)
- [Cloud Native Computing Foundation](https://www.youtube.com/@cncf)
- [AWS Events](https://www.youtube.com/@AWSEventsChannel)
- [Microsoft Developer](https://www.youtube.com/@MicrosoftDeveloper)
- [Google Cloud Tech](https://www.youtube.com/@googlecloudtech)

## Books

- Brendan Burns, Joe Beda, Kelsey Hightower, and Lachlan Evenson, *Kubernetes: Up & Running*
- Brendan Burns and Craig Tracey, *Managing Kubernetes*
- Liz Rice and Michael Hausenblas, *Container Security*
- Michael Hausenblas and Stefan Schimanski, *Programming Kubernetes*

Check edition, Kubernetes version, and managed-platform assumptions before purchasing
or following commands.

## Suggested reading order

1. Components, controllers, API concepts, workloads, and Pod lifecycle
2. Scheduling/resources, services/DNS/policy, storage, and security
3. EKS reliability, networking, security, identity, storage, and upgrade guidance
4. AKS/GKE architecture translations and Kubernetes lifecycle policies
5. Official talks and selected book chapters for platform-design depth
