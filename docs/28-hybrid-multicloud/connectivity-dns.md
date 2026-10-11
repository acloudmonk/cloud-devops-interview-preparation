# Connectivity, Routing, and DNS

[← Module overview](index.md) · [Strategy and placement](strategy-placement.md)

Cross-environment connectivity is production infrastructure. Design topology,
addressing, routing, name resolution, encryption, inspection, capacity, ownership,
and failure behavior together.

## AWS-first topology

Use site-to-site VPN for rapid or backup connectivity and AWS Direct Connect when
private transport and more predictable capacity are required. Transit Gateway or
Cloud WAN can centralize supported routing patterns. Design separate devices,
connections, locations, and carriers where the objective needs independence.

Azure ExpressRoute/VPN and Google Cloud Interconnect/VPN provide comparable intents,
not identical routing, SLA, encryption, or operational behavior. Cross-cloud links
can use carrier exchange, provider interconnect products, SD-WAN, VPN, or public TLS.

## Design checklist

- allocate non-overlapping IPv4/IPv6 space and govern future acquisition;
- define BGP advertisements, route preference, summarization, propagation, and filtering;
- avoid unintended transit and asymmetric inspection paths;
- size bandwidth for failure mode, replication, backup, observability, and recovery;
- measure latency, jitter, loss, MTU, throughput, flow, and cost;
- encrypt at application or network layer according to threat and compliance needs;
- test failover and restoration without route flapping or loops.

## DNS

Define authoritative zones, private namespaces, conditional forwarding/resolution,
split-horizon behavior, delegation, caching, TTLs, DNSSEC requirements, ownership,
and resolver failure. Avoid ambiguous duplicate names and cyclic forwarding.
Treat DNS and certificate distribution as cross-environment dependencies.

## Failure model

Test one tunnel, device, metro, carrier, provider edge, resolver, inspection tier,
and management plane. Confirm applications tolerate transient path changes and that
fallback paths have security policy and capacity equivalent to the primary.

Return to the [module overview](index.md) when ready to continue.
