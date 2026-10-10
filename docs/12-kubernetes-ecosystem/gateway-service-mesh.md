# Gateway API and Service Mesh

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

Ingress, Gateway API, cloud load balancers, API gateways, and service meshes solve
overlapping but different traffic problems. Add a layer only for a required outcome
that application libraries and existing platform controls do not meet cleanly.

## Traffic responsibility map

| Layer | Typical responsibility |
| --- | --- |
| Cloud load balancer/WAF | External reachability, TLS options, L4/L7 balancing, edge policy |
| Kubernetes Service | Stable endpoint and backend selection inside the cluster |
| Ingress | Widely supported HTTP(S) routing through an implementation-specific controller |
| Gateway API | Role-oriented, extensible L4/L7 routing APIs with explicit attachment |
| Service mesh | Workload-to-workload identity, mTLS, policy, telemetry, and traffic behavior |
| API gateway | Product-facing API authentication, quotas, transformations, lifecycle, analytics |

The exact product may combine layers, but ownership and failure paths should remain clear.

## Gateway API model

Gateway API separates infrastructure ownership from application routing through
GatewayClass, Gateway, Route types, and attachment/reference policy. Evaluate
implementation conformance and supported fields rather than assume every provider
supports every status, route, filter, policy, protocol, or extension.

Design listener/TLS certificate ownership, namespace attachment, allowed route kinds,
backend references, cross-namespace permission, status/conditions, controller class,
DNS, health, and deletion. An accepted Route is not proof that traffic or customer
behavior is healthy.

## Service mesh decision

A mesh may be justified for consistent workload identity/mTLS, fine-grained traffic
policy, cross-language telemetry, retries/timeouts/circuit breaking, or multi-cluster
service connectivity. It adds proxies or node data plane, control plane, certificate
authority, identity issuance, configuration APIs, resource overhead, latency, upgrade
skew, and new correlated failure modes.

Ask whether requirements apply to all services, only regulated paths, or just the edge.
Application libraries, language platforms, NetworkPolicy, cloud private connectivity,
and Gateway/API management may solve narrower needs more cheaply.

## Retry and timeout safety

Infrastructure retries can multiply application retries and duplicate non-idempotent
operations. Establish an end-to-end latency budget, request deadline propagation,
bounded retries with backoff/jitter, retryable methods/statuses, connection pools,
circuit/bulkhead behavior, and observability. Avoid default policies that hide failure
until queues and resources saturate.

## mTLS and identity

mTLS authenticates endpoints and encrypts a connection; authorization still needs
policy tied to trustworthy workload identity. Define root/intermediate CA, issuance,
rotation, trust domains, federation, revocation/expiry, clock, bootstrap, and outage
behavior. Protect control-plane and certificate identities; audit policy decisions.

## AWS and multi-cloud

On EKS, select load-balancer/Gateway integrations using target mode, subnet/topology,
security-group, source-IP, TLS, WAF, private/public, IPv4/IPv6, quota, and controller
identity requirements. Verify current AWS support rather than assuming an abandoned or
deprecated service remains strategic.

AKS and GKE offer provider-specific ingress/Gateway and managed mesh capabilities.
Portability depends on the conformance profile and policy/extension use, not merely
using a Kubernetes API name.

## Failure and removal

Plan for controller outage, stale routes, proxy/data-plane failure, certificate expiry,
CA loss, policy error, telemetry overload, control/data-plane version skew, and DNS/LB
drift. Keep a bypass only where risk accepts it, test migration, and know how to remove
injected proxies, finalizers, webhooks, CRDs, certificates, and cloud resources safely.
