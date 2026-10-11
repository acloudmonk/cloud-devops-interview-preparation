# Networking, Hybrid Connectivity, and Edge

[← Identity and security](identity-security.md) · [Next: Compute platforms →](compute-platforms.md)

## Start with address and traffic intent

Plan non-overlapping IPv4/IPv6 addressing, growth, account/Region boundaries, ingress,
egress, east-west paths, DNS, inspection, private service access, partners, and hybrid
connectivity. For every flow name source, destination, protocol, identity, route,
policy, encryption, logging, failure behavior, and owner.

## Build VPC boundaries

A VPC is Regional; subnets are zonal. Route tables select paths, security groups are
stateful resource firewalls, and network ACLs are stateless subnet controls. Internet
gateways, NAT gateways, egress-only internet gateways, endpoints, load balancers, and
appliances solve different problems. Avoid routing asymmetry and centralized single
points of failure.

## Connect networks deliberately

VPC peering is direct and non-transitive. Transit Gateway provides hub-style routing
at scale. PrivateLink exposes services privately without broad network reachability.
Cloud WAN supports managed wide-area connectivity. Compare routing, scale, inspection,
DNS, bandwidth, failure domains, data transfer, ownership, and cost.

## Engineer hybrid paths

Site-to-Site VPN provides encrypted internet connectivity; Direct Connect supplies
dedicated connectivity but not encryption by default. Use redundant devices,
locations, circuits, and paths according to business need. Design BGP, route
preference, MTU, DNS, identity, monitoring, capacity, failover, and tested degraded
operation; two logical links on one physical dependency are not resilient.

## Separate edge capabilities

Route 53 answers DNS and can apply health/routing policies; CloudFront caches and
delivers content; Global Accelerator provides static anycast ingress and AWS backbone
routing; WAF filters application traffic; Shield addresses DDoS protection. Select
from protocol, caching, origin, latency, security, health, failover, and cost needs.

## Troubleshoot hop by hop

Follow DNS, client, edge, load balancer, listener, target health, route, security group,
NACL, endpoint, firewall, return path, and application dependency. Use VPC Flow Logs,
Reachability Analyzer, load-balancer logs, Resolver query logs, and packet evidence;
timeouts and rejects require different hypotheses.
