# Networking References and Videos

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last verified: **2026-10-10**

Prefer standards bodies and cloud-provider documentation for behavior that can
change. Use the exact operating-system and platform documentation for the
version involved in an incident.

## Internet standards

- [RFC 4632: Classless Inter-domain Routing](https://www.rfc-editor.org/rfc/rfc4632)
  — CIDR addressing and aggregation.
- [RFC 8200: Internet Protocol, Version 6](https://www.rfc-editor.org/rfc/rfc8200)
  — IPv6 base protocol.
- [RFC 9293: Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc9293)
  — current TCP functional specification.
- [RFC 1034: DNS concepts and facilities](https://www.rfc-editor.org/rfc/rfc1034)
  and [RFC 1035: DNS implementation and specification](https://www.rfc-editor.org/rfc/rfc1035)
  — foundational DNS architecture and wire behavior.
- [RFC 2308: Negative caching of DNS queries](https://www.rfc-editor.org/rfc/rfc2308)
  — caching of nonexistence and negative answers.
- [RFC 9110: HTTP semantics](https://www.rfc-editor.org/rfc/rfc9110)
  — methods, status codes, fields, and shared semantics.
- [RFC 8446: TLS 1.3](https://www.rfc-editor.org/rfc/rfc8446)
  — modern TLS protocol behavior.

## AWS anchor references

- [Amazon VPC User Guide](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
  — VPCs, subnets, addressing, routes, gateways, security, and connectivity.
- [Security groups for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html)
  — stateful interface-level traffic policy.
- [Network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html)
  — stateless subnet-level policy.
- [Reachability Analyzer](https://docs.aws.amazon.com/vpc/latest/userguide/reachability-analyzer.html)
  — static configuration-path analysis and its scope.
- [Amazon Route 53 concepts](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/route-53-concepts.html)
  — DNS, hosted zones, routing policies, TTL, and control/data planes.
- [Elastic Load Balancing User Guide](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html)
  — listeners, targets, health, connection, and load-balancer types.
- [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html)
  — hub connectivity, attachments, and route tables.

## Azure translation

- [Azure networking architecture design](https://learn.microsoft.com/azure/architecture/networking/get-started)
  — Microsoft architecture guidance and topology choices.
- [Azure virtual networks](https://learn.microsoft.com/azure/virtual-network/virtual-networks-overview)
  — VNet, subnet, routing, security, and connectivity scope.
- [Azure Private Link in hub-and-spoke networks](https://learn.microsoft.com/azure/architecture/networking/guide/private-link-hub-spoke-network)
  — private endpoints and DNS integration.
- [Azure Network Watcher](https://learn.microsoft.com/azure/network-watcher/network-watcher-overview)
  — topology, flow, reachability, capture, and troubleshooting tools.

## Google Cloud translation

- [VPC networks](https://cloud.google.com/vpc/docs/vpc)
  — global network scope, regional subnets, routes, and firewall behavior.
- [Google Cloud routes](https://cloud.google.com/vpc/docs/routes)
  — route types and selection semantics.
- [Private Service Connect](https://cloud.google.com/vpc/docs/private-service-connect)
  — service-oriented private producer/consumer connectivity.
- [Network Intelligence Center](https://cloud.google.com/network-intelligence-center/docs/overview)
  — connectivity tests, topology, performance, firewall insights, and observability.

## Video

- [AWS re:Invent 2018: Advanced VPC Design and New Capabilities](https://www.youtube.com/watch?v=fnxXNZdf6ew)
  — an official AWS architecture session. Use it for design reasoning; verify
  product capabilities and limits against current documentation.

Official channels for newer material:

- [AWS Events](https://www.youtube.com/@AWSEventsChannel)
- [Microsoft Azure](https://www.youtube.com/@MicrosoftAzure)
- [Google Cloud Tech](https://www.youtube.com/@googlecloudtech)
- [Internet Society](https://www.youtube.com/@InternetSociety)

Recommended searches: packet journey, DNS delegation and DNSSEC, TCP
troubleshooting, TLS handshake, cloud egress, hybrid BGP, load-balancer health,
and multi-cloud private service connectivity.

## Books

- James Kurose and Keith Ross, *Computer Networking: A Top-Down Approach*
- Richard Stevens, Kevin Fall, and Gary Wright, *TCP/IP Illustrated*
- Cricket Liu and Paul Albitz, *DNS and BIND*
- Michael Lucas, *Networking for Systems Administrators*

Check the edition and standards/platform versions before purchasing.

## Suggested reading order

1. Request-path mental model and TCP/DNS/HTTP standards
2. AWS VPC, security controls, Route 53, and load balancing
3. Azure and Google Cloud network-scope and private-access differences
4. Hybrid routing and operational troubleshooting documentation
5. Advanced VPC video and selected book chapters
