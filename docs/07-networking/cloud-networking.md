# Cloud Network Architecture

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

## AWS reference architecture

For a regional three-tier service:

- allocate a non-overlapping VPC CIDR with growth space;
- use multiple Availability Zones and separate subnets by routing purpose;
- expose only managed ingress endpoints, not application instances;
- keep workloads private and use controlled, observable egress;
- use security groups for stateful least-privilege relationships;
- use network ACLs only where subnet-level stateless control has a clear purpose;
- prefer private service endpoints when they reduce exposure and egress dependency;
- centralize DNS ownership, resolver rules, IP allocation, and route governance;
- enable flow, DNS, load-balancer, firewall, and change evidence with retention controls.

“Public subnet” means its effective route can reach an Internet gateway; an
instance also needs an appropriate address and policy. “Private subnet” is a
routing description, not proof of confidentiality.

## AWS control distinctions

| Capability | Important semantics |
| --- | --- |
| Security group | Stateful, attached to network interfaces, allow rules only |
| Network ACL | Stateless subnet boundary with ordered allow/deny rules |
| Route table | Longest-prefix route selection to a next hop |
| Internet gateway | VPC Internet routing component; not a standalone firewall |
| NAT gateway | Outbound IPv4 translation; zonal design and port state matter |
| VPC endpoint | Private path to supported services; endpoint/DNS/policy all matter |
| Transit Gateway | Hub routing with attachments, route tables, propagation, and cost |
| Route 53 Resolver | VPC DNS and hybrid inbound/outbound forwarding rules |

## Multi-cloud translation

| Need | AWS | Azure | Google Cloud | Semantic caution |
| --- | --- | --- | --- | --- |
| Private network | VPC | VNet | VPC network | GCP VPC is global; AWS VPC and Azure VNet are regional constructs |
| Subnet | AZ-scoped subnet | Regional VNet subnet | Regional subnet | Availability-zone association differs |
| Workload policy | Security groups | Network security groups / ASGs | VPC firewall policies/rules | State, attachment, priority, and default behavior differ |
| Hub routing | Transit Gateway / Cloud WAN | Virtual WAN / hub-spoke | Network Connectivity Center | Propagation and transitivity differ |
| Private service access | PrivateLink/VPC endpoints | Private Link/private endpoints | Private Service Connect | DNS and provider/consumer models differ |
| Managed DNS | Route 53 | Azure DNS / Private DNS | Cloud DNS | Resolver, forwarding, and private-zone association differ |

Do not map product names alone. Compare scope, route exchange, policy state,
DNS behavior, high availability, quotas, logging, ownership, and cost.

## Ingress and egress architecture

Ingress design defines public/private entry points, DDoS and WAF controls, TLS
ownership, routing, target health, and client identity. Egress design defines
allowed destinations, name resolution, translation, inspection, private
endpoints, logging, and failure behavior.

Centralized inspection simplifies policy but can add latency, cost, route
complexity, asymmetric-path risk, and shared blast radius. Distributed egress
improves isolation but increases governance demands. State the trade-off.

## Shared-services governance

Use automated IP allocation, route/policy review, ownership tags, quota
monitoring, and change audit. Prevent overlapping CIDRs before attachment, test
routes in both directions, and maintain emergency access independent of the
primary application path.
