# Kubernetes Security and Multi-Tenancy

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

Kubernetes security composes API identity, RBAC, admission, workload identity,
runtime isolation, network/storage controls, node trust, supply-chain evidence, and
operational audit. A namespace is an administrative scope, not a hard tenant sandbox.

## API identity and authorization

Authenticate humans through an external identity provider and short-lived access;
authenticate workloads with bounded service-account tokens. RBAC grants verbs on
resources and subresources. Start with namespaced least privilege, avoid wildcard and
`cluster-admin`, separate read from secret/exec/port-forward/impersonate/escalation
abilities, and regularly review effective/bound permissions.

The ability to create/update a workload can become code execution under its service
account and may expose mounted secrets, nodes, networks, or privileged features.
Evaluate indirect privilege paths, not only direct Secret reads.

## EKS identities

Separate AWS authentication to the cluster from Kubernetes authorization inside it.
Use current EKS access mechanisms and RBAC deliberately; avoid permanent broad
bootstrap mappings. For Pods, use EKS workload identity mechanisms such as IAM roles
for service accounts or the current supported approach so each workload receives a
narrow AWS role rather than inheriting the node role.

Protect OIDC trust conditions, service-account namespace/name, token audience,
session/audit attribution, and metadata access. Task/node/Pod identity boundaries in
AWS are not interchangeable.

## Admission and Pod security

Admission should enforce organizational invariants after authentication/authorization:
approved registries/digests, Pod Security Standards, non-root, no privilege escalation,
capability drop, seccomp, read-only root where feasible, resource requirements,
trusted identities, topology, and labels.

Use the built-in Pod Security Admission modes (`enforce`, `audit`, `warn`) with the
appropriate profile and version. Roll out using audit evidence, namespace ownership,
exceptions with expiry, and a recovery path. External policy engines are Module 12.

## Secrets

Kubernetes Secrets are API objects; base64 is encoding, not encryption. Enable and
manage encryption at rest, restrict API/etcd/backups, avoid broad list/watch, use
short-lived external identity where possible, prevent log/env/config leaks, and
design rotation/reload behavior. Anyone who can run a Pod under a service account may
be able to consume its accessible secrets.

## Node and runtime boundary

Nodes run many Pods and hold kubelet/runtime credentials, images, logs, volumes, and
network position. Patch and replace them, restrict management access, protect metadata,
use minimal supported images, detect drift, and separate high-risk workloads into
dedicated nodes, accounts, clusters, or stronger sandbox/microVM boundaries.

Privileged Pods, hostPath, host PID/network, dangerous capabilities, runtime sockets,
devices, and unrestricted daemon workloads can collapse node isolation. Apply default
deny network policy where enforced, egress controls, storage permissions, and
workload-specific cloud identity.

## Multi-tenancy decision

For trusted teams, namespaces plus RBAC/quota/policy/network separation may be
appropriate. Hostile code, regulatory separation, different administrators, noisy
neighbors, or high blast radius may require separate clusters/accounts/VPCs or
sandboxed runtimes. Compare isolation, control-plane/API contention, cost, fleet
management, and incident scope rather than default to “one cluster per team” or one
shared cluster for everything.

## Incident response

Preserve audit logs, object specs/managed fields, service-account and cloud audit,
image digests, admission decisions, node/runtime/process/network evidence, and secret
access. Isolate workload/node without destroying evidence, revoke identities, block
artifacts, rotate affected secrets, replace trusted infrastructure, and verify data/
customer impact. Restarting a compromised Pod is not remediation.
