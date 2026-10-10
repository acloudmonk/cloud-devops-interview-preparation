# Policy, Secrets, and Certificates

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

Policy, secret delivery, and certificates are platform trust services. Their controllers
and webhooks often hold broad read/mutate or cloud permissions, so availability,
identity, audit, upgrade, and compromise response matter as much as feature syntax.

## Policy architecture

Use built-in defaults and Pod Security Admission where they meet the requirement.
External engines such as Kyverno or OPA Gatekeeper can validate, mutate, generate, or
audit richer policy, with different language, data, caching, background-scan, and
reporting models.

For each policy define threat/control objective, scope/selectors, evidence, mode
(audit/warn/enforce), exception owner/expiry, test cases, mutation ownership, webhook
timeout/failure policy, and rollout/rollback. Avoid rules whose output depends on a
slow/unavailable network lookup in the admission path.

Mutation can simplify defaults but hides final state and can conflict with GitOps,
sidecar injection, field ownership, or another mutator. Prefer explicit configuration
for security-critical behavior and deterministic idempotent mutation when needed.

## Secret-delivery models

| Model | Strength | Main risk |
| --- | --- | --- |
| Encrypted value in Git | Versioned reviewable ciphertext | Key/decryption identity, plaintext at render/apply, rotation |
| External controller syncs Kubernetes Secret | Native consumption and decoupled store | Secret duplication in API/etcd/cache; controller privilege |
| CSI/file mount from external store | Reduced API-object storage, provider integration | Mount/start dependency, rotation/reload, file semantics |
| Application retrieves directly | Fine-grained runtime identity and fresh values | SDK coupling, availability/latency, cache/error handling |

Choose by application interface, exposure boundary, rotation latency, availability,
audit, offline recovery, scale, and cloud portability. Never claim external storage
alone solves log, environment, process, memory, backup, or workload-identity leakage.

On EKS, use Pod-specific AWS identity and narrow Secrets Manager/Parameter Store/KMS
permissions. Protect controller service accounts and cloud roles; separate tenant
paths; set request/cache/rate behavior; and audit value access without logging secrets.

## Certificate management

Certificate controllers such as cert-manager automate requests, issuance, renewal,
storage, and status against configured issuers. Define issuer trust boundary, account/
key custody, DNS or HTTP challenge permissions, names, lifetime/renewal window, rate
limits, revocation expectations, trust distribution, reload, monitoring, and backup.

A certificate `Ready` condition does not prove clients trust the chain, DNS points to
the endpoint, the workload loaded the new keypair, or the old certificate is unused.
Test the served certificate and end-to-end identity.

## Availability and compromise

Existing admitted workloads may keep running when policy or secret/certificate
controllers fail, while new Pods/deployments fail. Define failure policy by risk,
bounded caches, HA/topology, resource priority, dependency objectives, expiry alerts,
known-good recovery, and break-glass.

For compromise, isolate controller/webhook, revoke cloud/issuer/signing identity,
scope resources read or mutated, rotate affected secrets/certificates, restore trusted
configuration and controller image, and verify workload/customer impact. Reinstalling
without identity rotation and scope analysis is insufficient.
