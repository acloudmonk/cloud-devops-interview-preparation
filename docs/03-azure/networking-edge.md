# Networking, Hybrid Connectivity, and Edge

[← Identity and security](identity-security.md) · [Next: Compute platforms →](compute-platforms.md)

## Start with address and flow intent

Plan nonoverlapping IPv4/IPv6, growth, subscription/Region boundaries, ingress, egress,
east-west paths, DNS, inspection, private service access, partners, and hybrid links.
For each flow name source, destination, protocol, identity, route, policy, encryption,
logging, failure behavior, and owner.

## Build VNet boundaries

A virtual network is Regional and contains subnets. Network security groups are stateful
controls; user-defined routes influence next hop; Azure NAT Gateway supplies scalable
outbound connectivity; Azure Firewall provides managed inspection. Service endpoints
extend a service’s network identity to a subnet, while Private Link exposes a private
endpoint in the VNet. Design private DNS with every Private Link decision.

## Connect networks deliberately

VNet peering provides direct nontransitive connectivity. Hub-spoke centralizes shared
network capabilities but can concentrate blast radius and cost. Azure Virtual WAN
provides managed global transit and routing. Compare routing, scale, segmentation,
inspection, DNS, ownership, latency, data processing, and failure behavior.

## Engineer hybrid connectivity

VPN Gateway provides encrypted internet tunnels; ExpressRoute provides private
connectivity but encryption requirements still need design. Use independent customer
devices, provider paths, peering locations, gateways, and circuits according to risk.
Plan BGP, route preference, asymmetric routing, MTU, DNS, identity, capacity, monitoring,
failover, and coexistence with VPN.

## Select ingress and edge capabilities

Azure Load Balancer provides layer-4 Regional load balancing; Application Gateway
provides Regional layer-7 delivery and optional WAF; Front Door provides global HTTP(S)
edge routing/acceleration and WAF; Traffic Manager provides DNS-based routing; CDN
addresses content delivery. Select from protocol, scope, origin, health, TLS, WAF,
caching, failover, private connectivity, and cost.

## Troubleshoot hop by hop

Follow DNS, client, Front Door/Traffic Manager, gateway/load balancer, listener, health,
route, NSG, firewall, NAT/SNAT, private endpoint, return path, and application. Use
Network Watcher, connection troubleshoot, effective routes/security rules, flow logs,
service diagnostics, and packet evidence. Distinguish name, route, policy, port, and
application failures.
