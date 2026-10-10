# IP, CIDR, Subnetting, and Routing

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

## Address-plan reasoning

An IPv4 prefix `/n` contains `2^(32-n)` addresses before provider reservations
and workload consumption. Do not design only for today's instances. Include
load balancers, managed interfaces, endpoints, failover, rolling deployment,
autoscaling, and future integration.

| Decision | Review question |
| --- | --- |
| Network range | Does it overlap with current or likely connected networks? |
| Subnet size | Can it support peak plus surge, managed interfaces, and reservations? |
| Segmentation | Is the boundary based on trust, failure domain, routing, or only convention? |
| IPv6 | Is dual-stack behavior tested across DNS, policy, observability, and dependencies? |
| Growth | Can new zones, regions, acquisitions, and partners be added without renumbering? |

Over-allocation consumes scarce private space; under-allocation causes disruptive
renumbering. Central allocation records and overlap checks are architectural
controls, not spreadsheet housekeeping.

## Route selection

Routers normally choose the most specific matching prefix, then apply the
platform's route precedence rules. A route states a next hop; it does not prove
that the destination accepts traffic or that a return path exists.

For a failing flow, inspect:

1. effective route at the source;
2. every transit and translation hop;
3. destination-side policy and listener;
4. effective return route;
5. state maintained by NAT, firewall, proxy, or load balancer.

Asymmetric routing is not automatically wrong, but stateful devices can drop a
return flow that does not traverse the device holding its state.

## Public and private addressing

Private addressing prevents direct Internet routing; it does not provide access
control by itself. Public addressing does not require unrestricted inbound
access. Security comes from explicit identity, policy, controlled ingress and
egress, hardened endpoints, and monitoring.

## NAT and port capacity

Source NAT translates many internal flows to fewer public identities. Its
failure modes include exhausted translation ports, idle-timeout mismatch,
uneven destination concentration, and zonal dependency. Adding bandwidth does
not fix exhausted ports.

Reduce risk with distributed egress, connection reuse, appropriate timeouts,
private service endpoints, destination diversity where valid, and port/allocation
metrics. Do not treat a NAT gateway as a generic security appliance.

## MTU and fragmentation

Encapsulation reduces usable payload size. Path MTU discovery can fail when
required ICMP messages are blocked, causing small requests to work while larger
ones stall. Compare packet size, protocol, tunnel path, MSS behavior, and IPv4
versus IPv6 rather than assuming an application timeout.

## IPv6 considerations

IPv6 restores abundant addressing but not automatic security. Plan address
assignment, neighbor discovery, DNS AAAA records, egress policy, logging, and
dual-stack preference. A partially enabled IPv6 path can create delayed fallback
or environment-specific failures.

## Routing design principles

- summarize routes where it does not hide ownership or incorrect propagation;
- minimize overlapping address space;
- separate reachability from authorization;
- define deterministic ingress and egress paths;
- avoid transitive-routing assumptions for peering products;
- constrain route propagation and inspect effective routes;
- design rollback before changing shared route tables.
