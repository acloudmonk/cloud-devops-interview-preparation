# Kubernetes Ecosystem Rapid-Fire Revision

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

Answer each in 30–60 seconds with a definition, ownership boundary, failure mode,
and condition that changes the choice.

## Packaging and GitOps

1. **Helm chart?** Versioned package of templates, defaults, metadata, dependencies, schema, and optional hooks/tests.
2. **Helm release?** Installed chart/config revision state; rollback does not reverse external data or every side effect.
3. **Chart values risk?** Unbounded low-level parameters create unstable public API and invalid combinations.
4. **Helm hook risk?** Side-effectful lifecycle action may be non-idempotent and outside safe rollback.
5. **Kustomize base?** Reusable ordinary Kubernetes resources composed by overlays.
6. **Overlay risk?** Deep inheritance and brittle patches obscure final state and cause cross-environment drift.
7. **Rendered evidence?** Exact chart/base/values/overlay/renderer output linked to review and target.
8. **GitOps?** Versioned declarative source plus automated reconciliation, drift handling, health, and recovery.
9. **Synced versus healthy?** Desired comparison matches versus controller/workload health; neither proves customer success.
10. **Emergency GitOps change?** Bounded authority, pause/update source, evidence, verify, commit desired state, resume/converge.

## Network and traffic ecosystem

1. **CNI?** Runtime/plugin contract and implementation for Pod network setup; broader products may add routing/policy/IPAM.
2. **eBPF?** Kernel programmability mechanism used for networking/security/observability, not a product outcome by itself.
3. **Underlay versus overlay?** Routable infrastructure addresses versus encapsulated logical network, with scale/MTU trade-offs.
4. **kube-proxy replacement?** Alternative Service data plane; validate semantics, upgrade, debugging, and fallback.
5. **CNI migration risk?** Node bootstrap and Pod connectivity depend on it; mixed modes/policy/MTU/IP must be proven.
6. **GatewayClass?** Infrastructure/controller implementation class for Gateway API resources.
7. **Route attachment?** Explicit relationship and permissions between routes and gateways/listeners across roles/namespaces.
8. **Mesh justification?** Required workload identity/mTLS/traffic/telemetry outcome outweighs data-plane and operational cost.
9. **Mesh retry risk?** Multiplies app retries and non-idempotent work, saturating downstreams without shared budget.
10. **mTLS proves?** Peer certificate identity and encrypted channel; authorization and application correctness remain separate.

## Scaling and trust services

1. **Event-driven scaler?** Converts queue/event/external signal into replicas/jobs through a scaling control loop.
2. **External metric risk?** Freshness, availability, auth, rate/cardinality, missing-data policy, and semantic validity.
3. **Autoscaler ownership?** One authoritative controller per replicas/requests/nodes; coordinate GitOps ignored fields.
4. **Node provisioner trade-off?** Flexible capacity and bin packing versus cloud coupling, disruption, and operating complexity.
5. **Scale-to-zero prerequisite?** Trigger can detect new work, startup meets latency, dependencies handle burst, state is safe.
6. **Admission failure policy?** Fail closed/open by risk, with bounded timeout, scope, HA, monitoring, and break-glass.
7. **Mutation concern?** Hidden final state and field conflict; keep deterministic, idempotent, and intentionally owned.
8. **External secret sync?** Controller copies external value into Kubernetes Secret; native use but duplicated exposure.
9. **CSI secret delivery?** Mounted external value reduces API storage but adds startup/mount/reload dependency.
10. **Certificate Ready limit?** Does not prove endpoint serves it, client trust, DNS, or workload reload.

## Operators and lifecycle

1. **Operator?** Custom API plus controller encoding domain reconciliation and lifecycle knowledge.
2. **CRD?** Cluster-wide API definition with schema/version/storage/conversion/deletion responsibilities.
3. **Conversion webhook risk?** API reads/writes may depend on its availability, TLS, and compatible conversion logic.
4. **Stored version?** API version used in storage; serving another version may require conversion and migration.
5. **Finalizer ownership?** Controller must complete external cleanup; manual removal can orphan or corrupt resources.
6. **Managed add-on benefit?** Provider-managed packaging/support integration; customer still owns configuration and impact.
7. **Add-on inventory?** Version, config, identity, privilege, dependencies, owner, SLO, backup, upgrade, and removal.
8. **Chart rollback limit?** Cannot undo CRD migration, data, cloud resource, cert, or hook side effect automatically.
9. **Safe removal?** Stop consumers, export/convert, reconcile finalizers/resources, remove webhooks/controller, then CRD/RBAC/cloud.
10. **Dependency-cycle risk?** Trust/network/secret/admission components can block one another during bootstrap or recovery.

## Architecture and leadership

1. **Build versus adopt?** Compare unique need/advantage with lifecycle cost, maturity, support, and exit—not engineering preference.
2. **Project maturity evidence?** Governance, maintainers, releases/security, compatibility, tests, incidents, support, limits.
3. **Portability?** Upstream conformance plus restrained extensions and tested migration, not identical YAML alone.
4. **Control versus data plane?** Decision/reconciliation versus workload traffic/execution path; failure and upgrade differ.
5. **Platform paved path?** Small supported self-service interface with SLOs, ownership, docs, metrics, and exceptions.
6. **Tool sprawl response?** Inventory outcomes/owners/dependencies/cost, freeze additions, consolidate by evidence, migrate safely.
7. **Controller compromise?** Isolate, revoke identities, compare state, scope targets/data, restore trusted version, verify impact.
8. **Ecosystem SLO?** Measure user-visible reconcile/admission/secret/network/scaling outcomes, not controller uptime alone.
9. **Cost model?** Compute, network/LB/IP, storage, telemetry, license, toil, training, failure, and opportunity cost.
10. **Principal-level close?** Outcome, selected minimum stack, ownership, lifecycle risk, adoption, measure, owner, next decision.
