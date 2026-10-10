# Load Balancing and Proxies

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

## Selection is only one responsibility

A traffic intermediary can terminate connections, authenticate clients, apply
policy, select targets, retry, transform protocols, add headers, cache, observe,
and encrypt the next hop. Name the exact responsibility and failure behavior
instead of saying “put a load balancer in front.”

| Dimension | Design question |
| --- | --- |
| Layer 4 or Layer 7 | Is routing based on addresses/ports or HTTP host/path/header? |
| Public or private | Which clients and networks may reach the listener? |
| Regional or global | Where is the entry point and how is a region selected? |
| Proxy or pass-through | Where do connections and TLS terminate? |
| Stateful or stateless service | Is affinity required, and can state be externalized? |
| Health | Does the check represent readiness for real traffic? |

## Health checks

Checks should be cheap, representative, protected from caching, and explicit
about dependencies. A shallow check avoids removing every target during a
shared dependency failure; a deep check better represents customer readiness
but can cause fleet-wide withdrawal. Often both are needed for different
decisions.

Define interval, timeout, healthy/unhealthy threshold, startup grace, and who
owns the endpoint contract. Health recovery must not admit a target before it
can sustain representative work.

## Draining and connection lifecycle

Removal from discovery does not terminate existing connections immediately.
Coordinate deregistration delay, keepalive, streaming sessions, deployment
grace, client retries, and in-flight work reconciliation. Forced termination
after a deadline may be necessary, but its business consequence must be known.

## Client identity

At a proxy, the backend often sees the proxy's address. Forwarded headers or
proxy protocol can convey the original client only across explicitly trusted
hops. Never trust client-supplied identity headers at an untrusted boundary.

## Failure and overload

- unhealthy-target removal can overload survivors;
- cross-zone distribution may improve capacity balance but add cost or latency;
- sticky sessions create hot targets and complicate recovery;
- retries at proxy and client can multiply traffic;
- connection reuse can hide per-target imbalance;
- a shared proxy is both a control point and a failure/blast-radius boundary.

## Reverse, forward, and transparent proxies

A reverse proxy represents servers to clients. A forward proxy represents
clients to destinations. Transparent interception changes traffic without the
endpoint explicitly selecting a proxy. Each model changes identity, trust,
certificate, routing, logging, and failure assumptions.

## CDN and edge caching

An edge layer can reduce origin load and latency but introduces cache keys,
purge behavior, regional propagation, stale-content policy, and another TLS/WAF
boundary. Verify both cache-hit and cache-miss paths and prevent personalized
or authorized data from entering shared cache accidentally.
