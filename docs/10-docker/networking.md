# Container Networking and Service Connectivity

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

A container network joins a process namespace to other namespaces and external
networks. Debug it as interfaces, addresses, routes, DNS, policy, translation,
proxies, load balancing, and application listeners—not as Docker magic.

## Local network modes

| Mode | Behavior | Main trade-off |
| --- | --- | --- |
| Bridge | Namespace/interface; host forwards/NATs published ports | Isolation with translation and host-port management |
| Host | Process shares host network namespace | Performance/simplicity but weak port/network isolation |
| None | Loopback only unless separately configured | Strong default isolation but no connectivity |
| Overlay/plugin | Multi-host connectivity from a control/data plane | Portability and policy depend on platform/plugin |

In a typical Linux bridge path, a virtual Ethernet pair connects the container
namespace to a host bridge. The container has an IP, default route, and DNS
configuration; host firewall/NAT rules implement published ports and egress.

## Listen versus publish

`EXPOSE` is image metadata; it does not create a listener or publish a host port.
The application must bind the correct address and port. Binding only `127.0.0.1`
inside the container prevents traffic arriving on the container interface. Port
publication can accidentally expose a service on every host interface.

## DNS and discovery

Resolve the actual name, search domains, resolver address, caching layer, TTL,
negative caching, and upstream health. A successful DNS response does not prove a
route, policy, listener, TLS identity, or application health.

Use service identities and stable discovery endpoints rather than persisting
container IP addresses. Instances are replaceable; clients must tolerate endpoint
change and graceful draining.

## AWS translations

- **ECS `awsvpc`:** each task receives an elastic network interface; security
  groups can apply at task level without bridge host-port translation.
- **ECS bridge/host:** EC2 tasks share host network resources with different port
  and isolation trade-offs.
- **Fargate:** uses `awsvpc`; AWS manages the worker host boundary.
- **EKS:** pod networking commonly uses VPC addresses through the AWS VPC CNI;
  Services, ingress/Gateway, and policy add further layers.

Azure Container Apps/AKS and Google Cloud Run/GKE expose comparable service,
ingress, egress, identity, and policy decisions with different implementations.

## Troubleshooting path

1. Confirm process state and listener address/port inside the namespace.
2. Confirm interface, address, routes, MTU, and resolver configuration.
3. Resolve the name and inspect endpoint and TTL.
4. Test transport from the actual source namespace.
5. Trace bridge/CNI, routing, NAT, firewall/security group, proxy/load balancer,
   and return path.
6. Validate TLS identity/SNI and application protocol.
7. Compare healthy and failing task, node, zone, architecture, and rollout cohort.

“It works on the host” does not prove the container namespace has the same route,
resolver, identity, or policy.
