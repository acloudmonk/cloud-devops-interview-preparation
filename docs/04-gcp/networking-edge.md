# Networking, Hybrid Connectivity, and Edge

[← Identity and security](identity-security.md) · [Next: Compute platforms →](compute-platforms.md)

Google Cloud VPC networks are global; subnets are regional. Draw routing, DNS,
firewalls, ingress, egress, return paths, and service endpoints separately.

- Choose Shared VPC, standalone VPCs, Network Connectivity Center, or peering from
  ownership, transitivity, segmentation, scale, and operations.
- Use hierarchical and VPC firewall policies with explicit ownership and logging.
- Use HA VPN or Cloud Interconnect according to throughput, availability, encryption,
  lead time, and provider diversity.
- Cloud Router exchanges dynamic routes; validate advertisements and return paths.
- Cloud NAT supplies outbound translation for supported private resources, not inbound
  connectivity. Model ports, addresses, endpoints, and saturation.

Private Google Access reaches supported Google APIs from resources without external IPs.
Private Service Connect supplies private consumer/producer endpoints. Private services
access uses allocated ranges for certain managed services. Confirm the product pattern.

Choose global or regional, external or internal Cloud Load Balancing from client,
protocol, backend scope, sovereignty, failover, and cost. Add Cloud DNS, certificates,
Cloud CDN, and Cloud Armor where their semantics fit.

Troubleshoot in order: resolve name → endpoint/health → route and return → firewall and
policy → NAT/private access → TLS/application → compare locations.
