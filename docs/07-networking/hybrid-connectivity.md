# Hybrid and Private Connectivity

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

## Connectivity options

| Pattern | Strength | Main risks |
| --- | --- | --- |
| Site-to-site VPN | Fast encrypted setup over Internet | Variable latency, tunnel limits, shared underlay |
| Dedicated circuit | Predictable private transport and capacity | Lead time, cost, provider/cross-connect dependencies |
| Peering | Direct private connectivity with simple scope | Non-transitive assumptions, route/DNS sprawl |
| Transit hub | Central route and policy governance | Shared blast radius, route-table complexity, cost |
| Private service endpoint | Consumer reaches a service without broad network reachability | DNS coupling, provider support, endpoint policy/quotas |

Redundancy requires independent failure domains: devices, tunnels, provider
edges, facilities, circuits, regions, and routing sessions—not two logical
connections sharing one physical path.

## Dynamic routing and BGP

BGP exchanges reachability and selects paths using policy and attributes; it
does not measure application health. Review advertised and accepted prefixes,
filters, local preference, AS path, communities, convergence, and maximum-prefix
protection. Route acceptance without authorization can expand blast radius.

Avoid advertising a prefix from a site that cannot actually serve or forward
it. Withdrawal speed, session timers, and application recovery capacity jointly
determine failover.

## DNS across environments

Hybrid name resolution requires explicit ownership and forwarding direction.
Document authoritative zones, conditional forwarders, resolver endpoints,
search suffixes, private views, loop prevention, and behavior when a link or
resolver fails. Network connectivity without DNS—or DNS without return routing—
is not a usable service path.

## Encryption and trust

Private transport is not necessarily encrypted or authenticated end to end.
Define link encryption, TLS/mTLS, key ownership, certificate lifecycle, and
which intermediaries can observe traffic. Segment partner connectivity and
authorize only required destinations and ports.

## Availability design

For each path, state detection signal, failover trigger, convergence target,
capacity after failure, session consequence, and failback procedure. Test under
representative load; a backup path that establishes routes but lacks capacity
does not satisfy the recovery objective.

## Cost and operations

Account for circuit ports, provider transit, cross-connects, gateways,
processing, inter-zone/inter-region transfer, egress, logs, and support. More
paths improve options but also increase configuration states and operational
testing obligations.
