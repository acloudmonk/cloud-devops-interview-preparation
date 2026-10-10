# Control Plane and Node Architecture

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

The Kubernetes control plane stores intent and coordinates reconciliation. Nodes run
workloads and report status. Managed Kubernetes changes who operates components; it
does not erase their behavior or customer responsibility.

## API request path

1. Client resolves and connects securely to the API endpoint.
2. Authentication establishes an identity and groups.
3. Authorization decides whether that identity may perform the verb on the resource.
4. Mutating admission may default or modify the object.
5. Schema and validating admission accept or reject it.
6. The API server persists the object in etcd and returns its resource representation.
7. Watches notify controllers, schedulers, and clients; later status updates show progress.

Audit policy records selected request metadata/bodies and stages. Balance forensic
value, sensitive-data exposure, volume, retention, and independent protection.

## Core responsibilities

| Component | Responsibility | Typical failure symptom |
| --- | --- | --- |
| API server | API validation, authn/authz/admission, storage front end, watches | Requests fail/slow; controllers lose updates |
| etcd | Strongly consistent durable control-plane state | API unavailable or stale if quorum/latency fails |
| Scheduler | Bind unscheduled Pods to feasible/preferred nodes | Pods remain Pending with scheduling events |
| Controller manager | Reconcile built-in resources and lifecycle | Desired and observed state stop converging |
| Cloud controller | Integrate nodes, routes, load balancers, volumes as applicable | Cloud resources fail to create/update/delete |
| Kubelet | Reconcile assigned Pods and report node/workload status | Containers/probes/mounts fail on a node |
| Container runtime | Pull, unpack, execute, and supervise containers via CRI | Image/runtime creation and lifecycle errors |
| Network/storage plugins | Implement CNI/CSI contracts | Pod networking or volume operations fail |

## etcd and control-plane continuity

etcd needs quorum, low-latency durable storage, encryption and access control, tested
snapshots/restores, and version-compatible operations. A backup is not complete until
restore and reconciliation consequences are tested. Restoring old cluster state can
conflict with cloud resources, certificates, external databases, and workloads that
continued changing.

In EKS, AWS operates the Kubernetes control plane and etcd availability/backups as a
service responsibility; customers operate API access, identity mappings/access
entries, RBAC, admission choices, add-ons, nodes, workloads, and disaster strategy.
AKS and GKE divide responsibility differently by feature/tier—verify the current
shared-responsibility documentation.

## Node lifecycle

A node object represents kubelet-reported capacity/conditions and scheduling state.
Cloud instance health and Kubernetes node readiness are related but different.
Node pressure, runtime failure, CNI/CSI issues, certificate problems, or API
partitions can make a running machine unsuitable.

For planned maintenance: cordon, drain with disruption constraints and workload
semantics, replace/upgrade, verify system and application health, then return
capacity. DaemonSets, local storage, unmanaged Pods, finalizers, long termination,
and PodDisruptionBudgets can change drain behavior.

## High-availability reasoning

Separate control-plane availability, node/zone capacity, workload replicas, traffic
distribution, data quorum/topology, DNS, identity, and cloud dependencies. Three Pod
replicas on one node or zone are not highly available. A healthy managed control
plane does not keep an under-capacity or misconfigured workload serving customers.

## Evidence map

Preserve API/audit events, object specs/status/managed fields, controller and scheduler
logs/metrics, node conditions, kubelet/runtime/plugin logs, cloud API/audit events,
and customer signals. Events are useful but ephemeral, rate-limited observations—not
a durable audit or complete chronology.
