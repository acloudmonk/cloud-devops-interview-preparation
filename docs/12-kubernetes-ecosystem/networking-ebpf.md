# CNI, eBPF, and Network Platforms

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

Kubernetes defines networking outcomes; CNI plugins and service/network-policy data
planes implement them. eBPF is a kernel capability used by some implementations—not
automatically a complete network, security policy, service mesh, or observability system.

## Decision layers

| Layer | Questions |
| --- | --- |
| IP address management | Pod address source, subnet/prefix capacity, release delay, dual-stack? |
| Routing/encapsulation | Underlay or overlay, routes, tunnels, MTU, cross-zone/on-prem behavior? |
| Service data plane | kube-proxy mode or replacement, session/source-IP behavior, scale? |
| Policy | Kubernetes NetworkPolicy coverage, identity/FQDN/L7 extensions, host enforcement? |
| Encryption | Node/Pod path, key lifecycle, performance, hardware/cloud interaction? |
| Observability | Flow/drop/DNS/service evidence, retention, cardinality, privacy, cost? |
| Operations | Kernel/runtime support, upgrade order, fallback, node bootstrap, support? |

## AWS anchor

The Amazon VPC CNI commonly assigns VPC-routable addresses to EKS Pods. Design subnet
and prefix/address capacity, instance ENI limits, warm pools, security groups for Pods,
network-policy mode, SNAT, IPv4/IPv6, custom networking, node bootstrap, and EC2 API
quota. EKS managed add-ons can reduce packaging toil but still require compatible
version/configuration and customer-owned rollout decisions.

Alternative CNIs or chaining can change address, routing, policy, kube-proxy, and
support boundaries. Confirm EKS support and integration with load balancers, Fargate,
Windows, hybrid nodes, security groups, and observability for the exact version.

AKS and GKE managed dataplanes expose different CNI, eBPF, policy, IP, and maintenance
choices. Keep application Service/NetworkPolicy contracts portable where feasible and
record required implementation-specific policy separately.

## eBPF trade-offs

eBPF can implement efficient networking, policy, load balancing, runtime signals, and
tracing with deep kernel visibility. Benefits depend on kernel features, program/map
limits, verifier/JIT behavior, privileges, and the product architecture. Risks include
node-wide blast radius, version/kernel coupling, opaque resource use, high-cardinality
telemetry, and specialized troubleshooting.

“Fewer iptables rules” is not enough justification. Define the bottleneck or missing
control, representative performance/security evidence, operating competence, and a
migration/rollback strategy.

## Migration safety

Inventory Pod/Service CIDRs, policy semantics, host traffic, source-IP/session behavior,
DNS, NodePort/load balancers, MTU, encryption, observability, Windows/Fargate/special
nodes, and cloud integration. Test new and old nodes, mixed-version support, policy
equivalence, disruption, connection behavior, and node replacement.

Avoid in-place data-plane replacement across the whole fleet without a proven cohort
and recovery route. Because CNI starts Pods and node readiness depends on it, a failed
upgrade can strand both applications and the tooling needed to repair them.

## Troubleshooting

Establish the actual packet path and policy identity. Compare failing nodes/zones,
routes, interfaces, addresses/prefixes, MTU, BPF programs/maps or proxy rules,
conntrack, policy verdicts, security groups, load-balancer targets, and return path.
Preserve node/plugin/controller versions and configuration before restart or cleanup.
