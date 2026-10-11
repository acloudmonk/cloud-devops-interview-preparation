# Networking, Edge, and Private Connectivity

[← Locations and resilience](locations-resilience.md) · [Next: Compute platforms →](compute-platforms.md)

| Capability | AWS | Azure | Google Cloud |
| --- | --- | --- | --- |
| Virtual network | VPC (regional) | VNet (regional) | VPC (global) |
| Private circuit | Direct Connect | ExpressRoute | Cloud Interconnect |
| Encrypted VPN | Site-to-Site VPN | VPN Gateway | Cloud VPN |
| Routing hub | Transit Gateway / Cloud WAN | Virtual WAN / Route Server | Network Connectivity Center |
| Private service endpoint | PrivateLink / endpoints | Private Link / private endpoints | Private Service Connect / private access patterns |
| DNS | Route 53 | Azure DNS / Private DNS | Cloud DNS |
| CDN/edge | CloudFront, Global Accelerator | Front Door, CDN | Cloud CDN, global load balancing |

Never translate CIDR, subnet, zone, route, NAT, firewall, endpoint, or load-balancer
assumptions mechanically. Azure subnets and Google Cloud subnets have different zone
relationships from AWS subnets. Peering transitivity and service endpoint semantics
also differ.

For intercloud connectivity, model provider circuits or VPNs, carrier/cloud exchange,
BGP, route ownership, overlapping address space, DNS authority, encryption, MTU,
asymmetric return, egress charges, bandwidth, monitoring, and diverse failure paths.

Keep synchronous chatty tiers together unless measured latency and failure coupling are
acceptable. Prefer controlled APIs/events over stretching layer-3 connectivity merely
to make environments appear uniform.
