# Advanced Kubernetes Incident Drills

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

Use the [scenario-answer framework](../interview-playbook/scenario-answer-framework.md).
Spend six minutes per drill: clarify, contain, preserve evidence, investigate,
recover, verify, prevent, and identify the trade-off. Model answers are omitted.

## 1. API server is available but controllers stop converging

Creates and reads succeed, yet Deployments, Jobs, and node lifecycle no longer update.
Lead scope, controller/leader-election/watch investigation, workload protection,
recovery, and evidence preservation in a managed control plane.

## 2. Accidental namespace deletion

A production namespace is terminating with workloads, Secrets, claims, and cloud load
balancers. Some finalizers are stuck. Decide what to freeze, restore, recreate, or
allow to delete without stripping finalizers blindly.

## 3. etcd restore creates external-state conflict

A self-managed cluster restores a snapshot from two hours ago while load balancers,
volumes, DNS records, and databases reflect newer operations. Plan isolation,
reconciliation, identity/certificate checks, data decisions, and safe return.

## 4. One-zone failure and impossible PDBs

Half the replicas and nodes disappear; strict topology and PDBs block maintenance
while remaining nodes lack capacity. Balance customer recovery, quorum, voluntary
disruption rules, temporary exceptions, and future capacity/topology design.

## 5. Compromised privileged DaemonSet

A node agent with host mounts, host PID/network, and a broad cloud role is compromised.
Scope every node/account exposure, isolate without erasing evidence, rotate identities,
replace nodes, verify workloads/data, and redesign the boundary.

## 6. CoreDNS saturation causes partial outage

Only some applications fail, DNS latency spikes, and application search-path behavior
creates high query volume. Diagnose cache, `ndots`, upstream dependencies, node-local
behavior, autoscaling, policy, and safe mitigation without masking the demand source.

## 7. CSI operation times out after partial success

Kubernetes reports attach failure, but the cloud disk may already be attached to a
failed node. A force-detach button is available. Establish actual state, fencing,
data safety, idempotency, retry, and ownership before acting.

## 8. Stolen service-account token

A bounded projected token appears in an external artifact. Explain audience, expiry,
RBAC, Pod/workload identity, cloud-role session, audit, revocation limitations,
containment, and the permanent credential-handling control.

## 9. API deprecation discovered after control-plane upgrade

Stored objects remain, but an old controller cannot update them and no control-plane
downgrade is supported. Lead compatibility recovery, controller replacement, data/
CRD safety, remaining upgrade decisions, and preventive API inventory.

## 10. Regional failover has configuration and data drift

The standby EKS cluster has different RBAC, admission, Secrets, image digests, and
database replication lag. Traffic can be switched in five minutes. Decide whether and
how to fail over, what evidence is required, and how to eliminate untested drift.
