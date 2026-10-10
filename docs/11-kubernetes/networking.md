# Kubernetes Networking and Traffic

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

Kubernetes defines network outcomes while CNI, kube-proxy or replacements, cloud
load balancers, DNS, and ingress/Gateway implementations realize them. Trace the
actual data path before blaming “the cluster network.”

## Core model

Each Pod receives an IP in a network namespace. Containers in one Pod share that
network and communicate over `localhost`. Pod IPs are replaceable. Services provide
a stable virtual address/name and select ready endpoints; EndpointSlices represent
those backends at scale.

| Resource | Purpose | Common misconception |
| --- | --- | --- |
| ClusterIP Service | Stable internal virtual endpoint | It is not a proxy process inside every Pod |
| Headless Service | DNS discovery without a cluster virtual IP | It does not itself make stateful membership safe |
| NodePort | Expose a port on eligible nodes | It is not usually the desired public architecture |
| LoadBalancer Service | Ask integration to provision/configure external load balancing | Provisioning success is not backend health |
| Ingress/Gateway | HTTP/TLS or richer traffic configuration interpreted by a controller | API object does nothing without an implementation |

## Traffic path

For a request, identify client DNS, external load balancer, listener/TLS, target
type, node or Pod route, Service selection, EndpointSlice readiness, network policy,
application listener, and return path. Source IP preservation, SNAT, session affinity,
connection draining, dual-stack, and topology routing can change behavior.

In EKS, AWS VPC CNI commonly gives Pods VPC-routable addresses. Pod density depends
on instance/network-interface/address capacity unless newer supported modes change
the calculation. Security groups for Pods, load-balancer controllers, VPC routes,
subnets, NACLs, and quotas add AWS-specific boundaries. Validate current add-on and
target-mode behavior rather than assume generic Kubernetes networking.

## DNS

CoreDNS normally serves cluster names and forwards other queries. Debug the queried
name, search list and `ndots`, resolver configuration, CoreDNS health/capacity, cache,
upstream DNS, network path, TTL, and application caching. Search expansion can create
unexpected query volume and latency.

A resolvable Service may still have no ready endpoints. A working IP request may
still fail through DNS, TLS SNI, proxy, or policy. Test from the failing Pod namespace.

## NetworkPolicy

NetworkPolicy selects Pods and describes allowed ingress/egress. Enforcement and
supported features depend on the network plugin. Policies are additive; selecting a
Pod for a direction creates isolation for that direction, and allowed traffic is the
union of applicable policies.

Start with required flows: DNS, identity/secret endpoints, telemetry, dependencies,
health/control traffic, and cloud APIs. Roll out with flow visibility and ownership.
A YAML policy that the installed plugin does not enforce is documentation, not control.

## Troubleshooting sequence

1. Confirm application process/listener and Pod readiness.
2. Confirm Pod IP, routes, MTU, DNS configuration, and node/CNI health.
3. Inspect Service selector, ports, EndpointSlices, and endpoint readiness.
4. Test DNS and transport from the actual source Pod.
5. Inspect policy enforcement, cloud security rules, load balancer targets, and return path.
6. Validate TLS/SNI/HTTP routing and application identity.
7. Compare node, zone, subnet, address family, digest, and rollout cohort.

Packet capture, eBPF telemetry, flow logs, and conntrack inspection are useful only
when attached to a specific boundary and hypothesis. Ecosystem products belong to
Module 12; the interview skill here is disciplined path decomposition.
