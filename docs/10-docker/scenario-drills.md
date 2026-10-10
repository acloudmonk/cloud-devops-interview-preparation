# Advanced Container Incident Drills

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

Use the [scenario-answer framework](../interview-playbook/scenario-answer-framework.md).
Spend six minutes per drill: clarify, contain, preserve evidence, investigate,
recover, verify, prevent, and identify the trade-off. Model answers are omitted.

## 1. Compromised base image

An approved base digest used by 160 images is found to contain a backdoor. Some
derived images are running in three accounts and two regions. Lead containment,
impact analysis, rebuild order, evidence, and customer-risk decisions.

## 2. Valid signature from a stolen workload identity

The image signature verifies, but the CI workload identity was compromised for six
hours. Determine what remains trustworthy, what must be revoked/blocked/rebuilt, and
how future policy should constrain signing and builder identity.

## 3. Registry regional replication lag

A disaster-recovery exercise shifts workloads before required manifests and
attestations have replicated. Some layers exist and some do not. Decide whether to
wait, copy, use an alternate source, or stop, while preserving artifact identity.

## 4. Shared kernel zero-day

A remotely exploitable kernel vulnerability affects container hosts. No patch is
available for 48 hours. Workloads range from internal APIs to untrusted customer
code. Define risk-tiered isolation, scheduling, network, capacity, and recovery.

## 5. Writable-layer exhaustion on one host

Several tasks fail only on one EC2 container host. Application dashboards look
normal, but image pulls and log writes fail. Diagnose bytes, inodes, snapshots,
logs, deleted-open files, and garbage collection without destroying evidence.

## 6. Multi-architecture manifest points to mismatched code

The AMD64 and ARM64 child images under one release index were produced from
different source revisions. Only ARM users see a payment bug. Lead rollback,
traceability, customer impact, and prevention across the build matrix.

## 7. Backup is crash-consistent but application is not

A volume snapshot exists for a stateful container, but the service uses a write-ahead
log and external queue. Explain restoration, consistency validation, message replay,
data-loss decisions, and the future backup contract.

## 8. Debug container becomes an attack path

An engineer attaches a privileged diagnostic container with host mounts during an
incident. Credentials may have been exposed and no session transcript exists.
Contain and redesign emergency debugging while preserving useful diagnostics.

## 9. Rootless migration breaks networking

A security program moves build and runtime workloads to rootless containers. Low
ports, overlay networking, and cgroup limits behave differently. Plan diagnosis,
compatibility decisions, exceptions, and safe adoption without abandoning the goal.

## 10. Runtime and orchestration state disagree

The orchestrator reports a task stopped, but a workload process and network listener
remain on the host. Explain evidence preservation, containment, runtime/shim/kernel
investigation, reconciliation, and fleet-wide detection.
