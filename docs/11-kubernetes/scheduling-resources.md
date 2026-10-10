# Scheduling, Resources, and Scaling

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

The scheduler selects a node for each unscheduled Pod by filtering infeasible nodes
and scoring feasible ones. Kubelet/runtime enforcement happens later. “Pending” is
an outcome of constraints and capacity, not a root cause.

## Scheduling inputs

- resource requests and allocatable node capacity;
- node selectors and required/preferred node affinity;
- Pod affinity/anti-affinity and topology-spread constraints;
- taints and tolerations;
- volumes and storage topology;
- ports, devices, runtime classes, and plugin-specific resources;
- priority, preemption, and scheduler profiles.

Toleration permits scheduling onto a tainted node; it does not require it. Affinity
expresses placement intent; required rules can make workloads unschedulable. Labels
used for security or compliance placement need protected provenance.

## Requests, limits, and quality of service

Requests guide scheduling and commonly inform CPU shares; limits bound resource use.
CPU excess is throttled, while memory pressure can lead to OOM termination/eviction.
Kubernetes QoS classes derive from request/limit patterns and influence eviction,
but do not guarantee application priority or availability.

Measure working set, heap/native memory, page cache, CPU throttle, latency, concurrency,
and node pressure. Arbitrary low limits create instability; no requests create unsafe
packing and misleading autoscaling. Leave capacity for system daemons, rollouts,
failures, and node drains.

## Namespace governance

ResourceQuota limits aggregate namespace consumption/object counts. LimitRange can
set/default/min/max per-object resources. Neither replaces capacity planning or
workload-specific measurement. Quotas, priority classes, and admission policy should
prevent one tenant from exhausting cluster/API resources without blocking recovery.

## Autoscaling layers

| Layer | Decision | Main lag/risk |
| --- | --- | --- |
| HPA | Change workload replicas from metrics | Metric validity, readiness, stabilization, downstream capacity |
| VPA | Recommend/change Pod requests | Restart behavior, HPA interaction, history quality |
| Node autoscaler | Add/remove nodes for unschedulable/underused capacity | Provision time, quotas, topology, disruption |

Scaling one layer can move the bottleneck. More Pods may overload a database; node
scale-up may be too slow for traffic; scale-down may conflict with PDBs/local data;
custom metrics may lag. Define minimum recovery capacity and test cold-start behavior.

## EKS anchor

EKS can use managed node groups, self-managed nodes, Fargate profiles, and current
node-provisioning/autoscaling options. Choose by workload isolation, instance/device
needs, operational control, startup speed, pricing, availability, and add-on support.
Protect AWS account/region quotas and multiple availability-zone capacity as explicit
dependencies.

AKS and GKE have analogous managed node pools and autoscaling/serverless modes, but
identity, networking, upgrade, and feature constraints differ. Keep workload resource
contracts portable while documenting platform-specific capacity behavior.

## Pending-Pod diagnostic order

Read scheduler events, then test requests versus allocatable, required labels/affinity,
taints/tolerations, topology constraints, PVC binding/topology, host ports/devices,
quotas/admission, and cloud capacity/quota. Adding nodes cannot solve contradictory
rules or a missing storage topology.
