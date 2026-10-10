# Kubernetes Scenarios

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

Answer aloud before reading the model answer. Identify desired/observed state, object
ownership, responsible controller, failure boundary, customer impact, recovery, and
verification.

## 1. Pods stay Pending after node scale-up

**Model answer:** Read scheduler events rather than add more nodes blindly. Check
requests versus allocatable, required affinity/selectors, taints/tolerations, topology,
PVC zone/binding, ports/devices, quota/admission, and cloud instance availability.
Fix the actual contradictory constraint or capacity class and verify placement plus
failure-domain distribution.

## 2. Deployment is available but customers receive errors

**Model answer:** Protect traffic and compare business signals with Pod readiness,
EndpointSlices, Service ports, load balancer targets, TLS/routing, dependencies, and
new/old cohorts. `Available` reflects configured readiness/minimum availability, not
business correctness. Restore/disable exposure and improve representative health and
post-deploy verification.

## 3. Liveness probes cause a restart storm

**Model answer:** Stop correlated restarts, preserve logs/events, and separate local
process liveness from shared dependency health. Use startup/readiness for initialization
and traffic eligibility; make liveness bounded and locally recoverable. Add dependency
resilience and test outage behavior before restoring enforcement.

## 4. Node drain never completes

**Model answer:** Inspect remaining Pods, PDBs, DaemonSets, unmanaged Pods, local data,
finalizers, preStop/grace, eviction errors, and replacement capacity/topology. Do not
force-delete stateful/quorum work blindly. Restore capacity or safely adjust the exact
constraint, complete application draining, and correct maintenance/PDB design.

## 5. Pod is OOM-killed despite low average memory

**Model answer:** Confirm cgroup/container OOM evidence and inspect peaks, working set,
heap, native memory, page cache, concurrency, request/limit, and node pressure. Averages
hide bursts. Protect traffic, fix leak/concurrency or right-size with headroom, align
runtime memory awareness, and alert on limit proximity/events.

## 6. Service name resolves but connection fails

**Model answer:** Test from the failing Pod. Inspect listener/bind, Service selector and
ports, ready EndpointSlices, Pod/node routes, network policy, security groups, proxy,
TLS/SNI, and return path. DNS proves only name resolution. Correct the narrow boundary
and verify application protocol plus another node/zone.

## 7. EBS-backed Pod cannot move after zone failure

**Model answer:** Establish volume/PV/node affinity, attachment and zone state, data
quorum, recovery point, and customer impact. A zonal disk cannot simply attach in
another zone. Fail over through application replication or restore/copy a validated
snapshot according to RPO/RTO; redesign topology and test zone recovery.

## 8. Workload cannot call AWS after identity migration

**Model answer:** Do not restore node-wide credentials. Trace service account, token
audience/claims, EKS workload-identity association or IAM trust, role policy, SDK token
path, DNS/network to STS/service, and CloudTrail denial. Correct the least-privilege
binding and test only from the intended namespace/service account.

## 9. Admission webhook blocks every deployment

**Model answer:** Protect existing workloads, establish webhook availability/TLS,
scope, timeout, failure policy, namespace/object selectors, and recent change. Use the
predefined break-glass procedure only if risk warrants; restore service or narrowly
bypass with audit/expiry. Design HA, bounded timeouts, monitoring, and failure behavior.

## 10. Secret was printed in a Pod log

**Model answer:** Revoke/rotate immediately, restrict log access/retention, and scope
which Pods, identities, collectors, exports, and users saw it. Preserve evidence without
copying the value. Fix application/config delivery and redaction; review RBAC and
secret-consumption paths. Deleting the Pod or log line is not remediation.

## 11. Rollout rollback does not restore service

**Model answer:** Verify image/template revision plus ConfigMap/Secret, database/schema,
messages, traffic, and external effects. Deployment rollback covers only recorded Pod
template state. Stop exposure, choose roll-forward or compatible prior version based
on data state, then adopt immutable config/artifact evidence and compatible change.

## 12. NetworkPolicy exists but traffic is still allowed

**Model answer:** Verify the installed CNI enforces policy and supports the used fields;
check namespace/Pod selectors, direction isolation, additive policy union, ipBlock,
host/node traffic, and actual source/destination labels. Correct and test from an
unauthorized Pod, then add continuous policy verification/flow visibility.

## 13. Cluster autoscaler adds no nodes

**Model answer:** Inspect unschedulable reasons, node-group template labels/taints/
resources, scaling bounds, AWS IAM/API/quota/capacity, backoff, and whether any node
type could satisfy topology/PVC/device constraints. Autoscaling cannot solve impossible
placement. Fix the template/constraint or offer a viable capacity class.

## 14. Namespace tenant gains cluster-wide access

**Model answer:** Revoke/contain the binding and preserve audit evidence. Trace Role/
ClusterRole aggregation, wildcard verbs/resources, group/service account subjects,
impersonation, token exposure, and indirect workload-creation privilege. Scope impact,
rotate credentials, repair least privilege, and add review/detection for privilege paths.

## 15. EKS upgrade breaks a critical workload

**Model answer:** Pause further node/add-on rollout and compare API removals, admission,
CRDs/controllers, CNI/CSI/DNS/proxy, node/runtime, and application behavior. Shift to
compatible nodes/version where supported or roll forward the dependency; control-plane
downgrade may be unavailable. Improve preflight inventory, representative tests,
version-skew sequencing, surge, and observable gates.
