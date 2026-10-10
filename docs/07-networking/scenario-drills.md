# Advanced Networking Incident Drills

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

These ten drills bring the module total to 25 scenarios. Give a five-minute
answer before reading the coaching cues.

## 1. Resolver latency after a regional event

Corporate users see long delays, then successful answers.

**Coaching cues:** Separate stub, forwarder, recursive, authoritative, and link
latency. Inspect timeouts/retries, forwarding order, unavailable private zones,
TCP fallback, and cache-hit ratio. Remove the failing upstream safely and verify
both public and private names.

## 2. Sporadic connection resets after proxy upgrade

**Coaching cues:** Segment by proxy version/node and connection age. Compare
idle/keepalive timeouts, protocol negotiation, draining, backend resets, and
connection-pool reuse. Roll back or remove a cohort and preserve request IDs.

## 3. Route exists but flow logs show rejects

**Coaching cues:** A route proves only next-hop selection. Identify the rejecting
interface/policy, stateful versus stateless semantics, identity attachment,
direction, port, and return path. Avoid broad allow rules.

## 4. No flow-log entry for a failed request

**Coaching cues:** Confirm logging scope, capture point, aggregation, filters,
delivery delay, and whether DNS/host routing prevented a packet from reaching
that interface. Absence at one point narrows a hypothesis; it is not universal
proof that traffic was never sent.

## 5. CDN serves private content to another user

**Coaching cues:** Treat as a security incident. Stop/disable the unsafe cache
path, preserve access evidence, identify cache-key and authorization behavior,
purge affected objects, assess exposure, and redesign so private responses are
non-shared by construction.

## 6. Backup VPN advertises more-specific routes

**Coaching cues:** Longest-prefix selection can override intended primary-path
preference. Inspect accepted/advertised prefixes, filters, propagation, and
return routing. Withdraw/filter the erroneous specifics with a controlled
rollback and validate application flows.

## 7. HTTP retries amplify a partial outage

**Coaching cues:** Map retry count and timeout at client, proxy, gateway, and
service. Reduce admission/retry pressure, protect healthy dependencies, require
idempotency, introduce jitter/backoff and a shared deadline, then reconcile
possibly duplicated work.

## 8. Private endpoint resolves publicly on premises

**Coaching cues:** Test the resolver actually used, private-zone association,
conditional forwarding, inbound resolver reachability, and search behavior.
Repair the DNS view without exposing the service publicly and test link-failure
behavior.

## 9. Firewall inspection creates asymmetric routing

**Coaching cues:** Draw both directions with route tables and appliance state.
Use symmetric routing constructs or supported appliance mode, verify failover,
and ensure the fix does not bypass inspection.

## 10. Regional failover passes synthetic checks but overloads

**Coaching cues:** Health is not capacity. Compare steady and failover demand,
connection ramp, cache warmth, quotas, egress/NAT state, dependencies, and data
readiness. Shed low-priority traffic, scale safely, and make failover capacity a
regular tested objective.
