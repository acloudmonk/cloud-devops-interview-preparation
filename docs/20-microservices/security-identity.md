# Security and Identity

[← Resilience and performance](resilience-performance.md) · [Next: Delivery and testing →](delivery-testing.md)

## Trust boundaries

Identify user, edge, service, workload, tenant, data, build, control-plane, and
operator boundaries. A private network is not identity. Authenticate workloads with
short-lived credentials and authorize the specific business action and resource.

## Edge and service authorization

Validate external tokens at a trusted boundary and propagate only required verified
claims or token exchange. Each service enforces authorization for the data and
operation it owns; a gateway cannot authorize object-level decisions it does not
understand. Prevent confused-deputy behavior when one service acts for a user.

## Workload identity and secrets

On AWS use scoped IAM roles for workloads rather than embedded keys; use analogous
managed/workload identities in Azure and Google Cloud. Rotate credentials, isolate
service roles, protect signing material, and keep secrets out of images, events,
logs, traces, and client-visible errors.

## Tenant and data protection

Carry verified tenant context through API, events, cache keys, storage, telemetry,
and cost. Test cross-tenant denial and revocation. Classify/minimize data, encrypt,
define residency and retention, authorize derived views, and propagate deletion to
replicas, search, caches, events, and backups according to policy.

## East-west controls

Transport encryption, network policy, and service mesh reduce network attack paths
but do not replace application authorization. Limit egress and metadata access,
patch runtimes, verify artifacts, and observe unusual service relationships. Avoid
one organization-wide service credential that turns compromise into fleet access.
