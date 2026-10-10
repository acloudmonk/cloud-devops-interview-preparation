# Advanced Kubernetes Ecosystem Incident Drills

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

Use the [scenario-answer framework](../interview-playbook/scenario-answer-framework.md).
Spend six minutes per drill: clarify, contain, preserve evidence, investigate,
recover, verify, prevent, and identify the trade-off. Model answers are omitted.

## 1. Compromised GitOps controller

The reconciler's cloud and cluster identities may have been used to mutate eight
clusters. Desired Git history looks clean. Lead isolation, credential revocation,
artifact/object comparison, customer/data scope, trusted restoration, and redesign.

## 2. Two reconcilers own the same production resources

Argo CD and Flux alternately replace labels, replica ownership, and generated Secrets.
Applications flap and both tools report drift. Establish authority, freeze safely,
reconcile state, migrate consumers, and prevent dual ownership.

## 3. Conversion webhook unavailable during upgrade

The API server cannot read or update a critical CRD version because its conversion
webhook has no healthy endpoints. Explain API impact, recovery ordering, certificate/
version evidence, stored-version safety, and future bootstrap design.

## 4. eBPF data-plane map exhaustion

Only high-density nodes lose new connections. Restarting the agent temporarily helps.
Investigate map/resource limits, workload/cardinality, kernel/plugin versions, policy/
service state, safe cleanup, capacity, and durable monitoring/remediation.

## 5. Mesh certificate authority compromise

The mesh CA signing identity may have issued unauthorized workload certificates across
two regions. Plan trust-root rotation, identity/session scope, workload disruption,
federation, evidence, authorization review, and customer communication.

## 6. Autoscaling feedback creates a cost spiral

Latency raises replicas, new Pods increase telemetry and dependency contention, node
provisioning accelerates, and latency worsens. Stabilize the system and redesign metrics,
budgets, backpressure, downstream capacity, and controller interactions.

## 7. Secret provider outage during mass restart

Running Pods have cached credentials, but new Pods cannot mount secrets after a zone
failure. Decide availability versus credential-risk behavior, capacity preservation,
provider recovery, bounded cache, and continuity testing.

## 8. Gateway controller creates conflicting load balancers

Two GatewayClasses accept related routes and provision public AWS resources with
different security groups and certificates. Contain exposure, establish attachment/
class ownership, reconcile cloud state, and design admission plus cost controls.

## 9. Operator restores a deleted external database

An emergency manual deletion was intentional, but the operator recreates an empty
database and redirects applications. Address reconciliation ownership, data protection,
finalizers/deletion policy, emergency suspension, recovery, and audit.

## 10. Kubernetes upgrade exposes ecosystem dependency cycle

Admission requires policy engine, policy engine requires secrets, secret controller
requires CNI, and CNI update requires new nodes admitted by policy. Build a safe
bootstrap/upgrade sequence and redesign the cycle for continuity.
