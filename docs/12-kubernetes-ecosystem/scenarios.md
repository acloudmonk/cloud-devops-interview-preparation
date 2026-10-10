# Kubernetes Ecosystem Scenarios

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

Answer aloud before reading the model answer. Identify source of truth, field and
controller owner, failure boundary, customer effect, containment, recovery, evidence,
and lifecycle improvement.

## 1. Helm upgrade fails after a successful hook

**Model answer:** Stop retries and determine hook side effects, rendered manifest,
release revision, external/database state, and workload health. Helm rollback may not
reverse the hook. Recover with an idempotent forward or explicit data procedure, then
move irreversible migrations out of opaque hooks and record their evidence separately.

## 2. Kustomize overlay patches the wrong resource

**Model answer:** Pause promotion, compare base/overlay/version and rendered output,
then restore the intended reviewed manifest. Replace brittle name/path patches with
specific selectors/components or clearer bases, keep overlays shallow, validate schema/
policy/diffs, and promote rendered identity as evidence.

## 3. GitOps controller reverses an incident fix

**Model answer:** Invoke the documented break-glass path: pause/narrow reconciliation
or update authoritative source, preserve evidence, apply the bounded change, verify
customers, commit/review final desired state, resume, and confirm convergence. Define
emergency authority, expiry, and fields/controllers so manual work is not silently lost.

## 4. Git commit is synced but application is unhealthy

**Model answer:** `Synced` proves desired resources match comparison, not customer
health. Inspect rendered artifact, status/conditions, rollout, routes/endpoints, data,
dependencies, and business signals. Stop promotion or revert/forward the source only
after data compatibility; improve health assessment and post-sync verification.

## 5. Admission webhook blocks all creates

**Model answer:** Protect running workloads; inspect service/endpoints, TLS/certificate,
API reachability, resource pressure, timeout, selectors, failure policy, and recent
change. Restore HA service or use a narrowly scoped audited break-glass if risk accepts.
Add bounded timeouts, topology/priority, monitoring, tests, and explicit failure policy.

## 6. Mesh retries overload the database

**Model answer:** Reduce/disable the retry policy and shed load; establish application
plus proxy retries, timeouts, deadlines, concurrency, and non-idempotent operations.
Recover downstream capacity, then set one end-to-end budget with bounded retryable
conditions, backoff/jitter, circuit/bulkhead controls, and customer signals.

## 7. CNI upgrade leaves new nodes NotReady

**Model answer:** Halt rollout/consolidation and keep healthy nodes. Inspect DaemonSet
image/config/RBAC, kernel/runtime, IP/prefix/subnet capacity, interfaces/routes/MTU,
logs, and version compatibility. Restore the known-good plugin/node image or roll
forward a fix through a cohort; improve mixed-version and bootstrap testing.

## 8. NetworkPolicy is portable but behavior differs

**Model answer:** Compare policy API semantics plus each implementation's enforcement,
unsupported extensions, host traffic, default behavior, identity, and test evidence.
Contain unwanted flow, express a portable baseline and isolated provider-specific
extension, and run conformance/connectivity tests before claiming multi-cloud parity.

## 9. HPA and event scaler fight over replicas

**Model answer:** Protect service and assign one replica owner. Inspect generated HPA/
target, metrics, polling/cooldown/stabilization, min/max, readiness, and GitOps fields.
Combine supported triggers under one scaling object or separate responsibilities;
test step load and missing metrics with downstream/cost guardrails.

## 10. Dynamic node provisioner chooses unavailable capacity

**Model answer:** Inspect Pod constraints, allowed instance/zone/capacity types, quotas,
cloud availability, subnet IP, daemon overhead, limits, and fallback. Broaden only
approved alternatives, reserve critical capacity, and ensure interruption/consolidation
policies respect PDB, topology, state, and recovery objectives.

## 11. External secret controller stops rotating values

**Model answer:** Determine store value/version, controller reconcile/auth/rate limit,
Kubernetes Secret or mount, application reload, and credential expiry. Protect service,
restore least-privilege identity/connectivity, force safe reconciliation, rotate if
exposed, and alert on secret age plus end-to-end consumption—not controller health alone.

## 12. Certificate shows Ready but clients see expiry

**Model answer:** Inspect the certificate actually served at each endpoint, secret/key,
issuer/order/challenge, controller status, load balancer/proxy copies, Pod reload,
DNS/cache, and trust chain. Replace/reload safely, verify externally, then monitor served
expiry and distribution, not only the Certificate object condition.

## 13. Operator upgrade corrupts custom-resource status

**Model answer:** Stop the controller rollout and mutation; preserve CR specs/status,
managed fields, stored versions, conversion, controller versions/logs, and external
state. Restore a compatible controller or roll forward schema/conversion after testing.
Add version-skew, storage-migration, backup/restore, and cohort upgrade evidence.

## 14. Removing a CRD deletes cloud resources

**Model answer:** Stop deletion and backups/exports; determine CR instances, finalizers,
owner/deletion policies, controller behavior, and external-resource state. Restore the
controller/CRD only if schema/storage compatibility is proven, reconcile deliberately,
and replace uninstall with consumer migration and ordered safe removal.

## 15. Platform add-on cost doubles

**Model answer:** Attribute compute/memory, cross-zone/egress, load balancers, addresses,
storage, telemetry/cardinality, licenses, and operator toil by component/tenant. Remove
duplicate capability and right-size after reliability evidence; validate that savings
do not reduce isolation, recovery, or customer objectives. Add showback and value/SLOs.
