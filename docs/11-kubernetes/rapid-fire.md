# Kubernetes Rapid-Fire Revision

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

Answer each in 30–60 seconds with a definition, failure mode, and condition that
changes the design.

## API and reconciliation

1. **Declarative desired state?** Submit intended object state; controllers repeatedly reconcile observed state toward it.
2. **Spec versus status?** User/controller intent versus system-reported observation; successful write does not imply convergence.
3. **Controller?** Idempotent loop that watches resources, compares state, acts, and records status/events.
4. **Resource version?** Optimistic-concurrency/watch token for object state, not an application release version.
5. **Generation?** Increment for desired-state changes; compare with observed generation to detect stale status.
6. **Owner reference?** Identity relationship enabling dependent lifecycle and garbage collection.
7. **Finalizer?** Deletion barrier for required cleanup; stuck finalizer means cleanup/controller is incomplete.
8. **Label versus annotation?** Selectable identity/group metadata versus non-identifying tool/context metadata.
9. **Admission?** Mutating/defaulting and validating policy after authn/authz before persistence.
10. **Event limit?** Ephemeral rate-limited observation, not complete audit or durable incident history.

## Workloads and scheduling

1. **Pod?** Smallest scheduling unit sharing network and selected namespaces/volumes; normally controller-owned.
2. **Deployment?** Manages ReplicaSets for replaceable replicas and declarative rolling updates.
3. **StatefulSet?** Stable ordinal/network/storage identity; application still owns replication/quorum/consistency.
4. **DaemonSet?** Ensures a Pod on each eligible node for node-local functions.
5. **Job retry risk?** Duplicate/uncertain execution; make external work idempotent and bounded.
6. **Request versus limit?** Scheduling/reservation signal versus runtime upper bound; CPU throttles, memory may OOM.
7. **Taint/toleration?** Node repels Pods unless tolerated; toleration permits but does not attract placement.
8. **Affinity?** Required/preferred placement relative to node or Pod labels; strict rules can block recovery.
9. **Topology spread?** Balance matching Pods across domains, constrained by eligible capacity and skew policy.
10. **Priority/preemption?** Higher-priority Pod may displace lower-priority work; capacity recovery still needs safeguards.

## Network and storage

1. **Service?** Stable virtual endpoint selecting ready backends represented through EndpointSlices.
2. **Headless Service?** DNS discovery without cluster virtual IP; does not implement membership or safety.
3. **Ingress/Gateway?** Traffic API requiring a controller/implementation; object alone moves no packets.
4. **NetworkPolicy model?** Additive allowed traffic for selected Pods/directions, enforced only by supporting plugin.
5. **CoreDNS failure check?** Query/name/search/`ndots`, resolver, CoreDNS/cache/upstream, path, policy, and application cache.
6. **PVC?** Workload claim for storage characteristics bound to a persistent volume.
7. **StorageClass?** Dynamic provisioning/driver/parameters/reclaim/binding/expansion/topology policy.
8. **WaitForFirstConsumer?** Delay volume provisioning/binding so Pod scheduling topology influences placement.
9. **ReadWriteOnce?** Typically one-node attachment, not necessarily single-Pod access.
10. **Snapshot limit?** Storage point-in-time copy; application consistency, external state, keys, and restore remain separate.

## Security and reliability

1. **RBAC Role versus ClusterRole?** Namespaced permission object versus cluster-scoped/reusable permission definition.
2. **Service account?** Namespaced workload/API identity; not equivalent to external cloud role without federation.
3. **Kubernetes Secret?** API object whose base64 is encoding; protect access, storage, backup, delivery, and rotation.
4. **Pod Security Admission?** Built-in namespace-level enforce/audit/warn of versioned Pod Security Standards.
5. **Namespace isolation limit?** Administrative scope, not a hard runtime/control-plane tenant boundary.
6. **PDB?** Limits voluntary disruption of healthy replicas; does not prevent crashes or zone failure.
7. **Startup versus readiness?** Initialization gate versus eligibility to receive intended traffic.
8. **Liveness?** Local failure where restart is likely to recover—not deep shared-dependency health.
9. **Deployment rollback limit?** Restores recorded Pod template, not schema, external effects, or all configuration.
10. **EKS managed boundary?** AWS operates control plane; customer owns access, workloads, nodes/add-ons, data, and design.

## Operations and judgment

1. **Pending first step?** Read scheduler events and test exact constraints before adding capacity.
2. **CrashLoopBackOff?** Retry pacing; inspect prior exit/logs, OOM, command/config/probes/dependencies for cause.
3. **ImagePullBackOff?** Check reference/digest/platform/auth/network/registry/node disk; backoff is not cause.
4. **Cordon versus drain?** Stop new normal scheduling versus evict/delete existing Pods under policy/flags.
5. **Node Ready limit?** Kubelet/node signal; application, network, storage, and customer health can still fail.
6. **HPA dependency?** Valid timely metric, readiness behavior, stabilization, resources, downstream and node capacity.
7. **Upgrade prerequisite?** API/add-on/controller/workload compatibility inventory plus supported skew and recovery.
8. **Managed control-plane rollback?** Often unavailable; test compatibility and plan roll-forward before upgrade.
9. **Regional failover requirement?** Consistent artifacts/config/identity/policy plus data/RTO routing and tested reconciliation.
10. **Principal-level close?** Constraints, boundaries, desired-state design, failure/recovery, adoption, measures, owner, decision.
