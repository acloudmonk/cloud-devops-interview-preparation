# Kubernetes Operations and Troubleshooting

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

Troubleshoot Kubernetes by following ownership and reconciliation from desired state
to observed state. Do not begin with random restarts or a broad command dump.

## Evidence-led workflow

1. State customer impact, scope, start time, and recent change.
2. Identify the object, namespace, UID, generation, owners, selectors, and intended state.
3. Read status conditions and events in chronological context.
4. Find the responsible controller, scheduler, kubelet, plugin, or cloud integration.
5. Compare healthy and failing digest, node, zone, architecture, tenant, and cohort.
6. Contain safely, preserve evidence, and test the smallest hypothesis.
7. Recover, verify customer outcomes and convergence, then prevent recurrence.

## Symptom map

| Symptom | First boundaries to inspect |
| --- | --- |
| Pending | scheduler events, requests/capacity, placement, taints, quota, PVC/topology |
| ImagePullBackOff | reference/digest, platform, auth, DNS/network, registry, node disk |
| CreateContainerConfigError | ConfigMap/Secret/service account/volume/runtime configuration |
| CrashLoopBackOff | exit code/signal, logs, command, config, OOM, probes, dependency |
| Running but not Ready | readiness/startup, listener, endpoint, dependency, sidecar |
| Evicted | node pressure, ephemeral storage, memory, PID, QoS, kubelet thresholds |
| Terminating | finalizer, preStop/grace, volume detach, API/controller reachability |
| Service unavailable | selector, EndpointSlice/readiness, ports, policy, DNS, LB path |

Backoff describes retry pacing, not root cause. A Pod restart may erase filesystem,
logs, and timing evidence; collect what matters first.

## Observability layers

Monitor API availability/latency/errors, etcd health where owned, scheduler/controller
queues, admission latency, node conditions/capacity, kubelet/runtime/CNI/CSI, workload
golden signals, DNS, load balancers, cloud quotas/APIs, and business outcomes. Events
are transient; export important audit, metrics, logs, traces, and change/deployment data.

Avoid high-cardinality labels and unrestricted audit bodies. Define retention,
sampling, cost, privacy, access, and correlation identifiers. Tool-specific stacks
belong in Module 17; here the focus is evidence coverage.

## Upgrades and add-ons

Inventory API removals, admission/webhooks, CRDs, controllers, CNI/CSI/DNS/proxy,
node OS/runtime, clients, and workload compatibility. Follow supported version skew
and managed-service sequencing. Test in representative environments, upgrade control
plane then nodes/add-ons as documented, use surge capacity and disruption budgets,
observe, and retain an explicit rollback/roll-forward plan.

A managed control-plane upgrade may be irreversible. Node rollback does not reverse
API/storage changes. Backups, manifests, and compatibility evidence matter more than
a generic “rollback” promise.

## Node maintenance

Cordon stops new normal scheduling; drain evicts/deletes Pods according to flags and
policies; neither proves application traffic drained or data is safe. Inspect PDBs,
local storage, DaemonSets, unmanaged Pods, termination duration, topology capacity,
and stateful quorum. Replace rather than hand-repair immutable nodes where practical.

## EKS operating boundaries

Track supported Kubernetes versions and deprecation dates, control-plane/API access,
managed node group/AMI and Fargate behavior, add-on compatibility, IAM/OIDC, subnet/
IP capacity, security groups, load balancer and CSI controllers, service quotas, and
CloudTrail/control-plane logs. Managed service health does not cover every workload or
customer configuration.

## Continuity

Define failure behavior for API/control-plane impairment, one-zone node loss, registry,
DNS, cloud IAM/API, admission webhook, CNI/CSI, and region outage. Maintain bounded
emergency authority, known-good artifacts/configuration, independent evidence, and a
tested reconciliation process. Multi-cluster/region adds routing, data, identity,
configuration, and release-consistency problems; it is not free availability.
