# Networking Scenario Questions

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

Answer aloud before reading the model answer. State impact, expected path,
hypotheses, discriminating evidence, safe mitigation, and verification.

## 1. DNS cutover is inconsistent

Some customers reach the old endpoint six hours after a change.

**Model answer:** Segment clients by resolver, geography, record type, and old
TTL. Compare recursive and authoritative answers, including negative/alias
caches and application connection reuse. Keep both endpoints safe, restore the
old record if impact demands it, and plan future TTL reduction before cutover.

## 2. Private service works from one subnet only

**Model answer:** Compare effective routes, security groups, stateless ACLs,
DNS answer, endpoint association/policy, and return path between healthy and
affected subnets. Change the smallest divergent control and validate from the
original workload identity.

## 3. High load causes outbound timeouts

**Model answer:** Test NAT translation-port/state exhaustion, connection reuse,
destination concentration, retries, and zonal path—not only bandwidth. Reduce
retry/admission pressure, distribute egress or use private endpoints, then
verify port allocation and customer latency.

## 4. Ping fails but HTTPS works

**Model answer:** ICMP and HTTPS have different protocols and policies. HTTPS
success proves a specific name/address/port path, not universal reachability.
Use the application protocol for health and inspect ICMP only if it is required.

## 5. TCP connects but TLS fails

**Model answer:** Transport reachability is established. Check SNI, hostname,
chain, trust store, validity time, protocol/cipher compatibility, mTLS, and the
actual termination point. Never solve it by disabling verification.

## 6. One Availability Zone has intermittent 502s

**Model answer:** Correlate errors with load-balancer node, target zone, target
version, health transitions, connection resets, and dependencies. Drain a
bounded unhealthy cohort while preserving capacity; verify real requests and
fix readiness or zonal dependency rather than masking the symptom.

## 7. Large uploads stall through VPN

**Model answer:** Suspect MTU/MSS or loss when small requests succeed. Compare
direct/tunnel paths and packet sizes; inspect fragmentation-needed behavior and
retransmissions. Correct tunnel/interface MTU or MSS handling rather than
allowing unsafe broad traffic.

## 8. New VPC cannot peer with an acquisition

**Model answer:** Check overlapping CIDRs first. Peering cannot route ambiguous
overlap and is generally non-transitive. Consider renumbering, translation,
service-level private endpoints, or an application proxy, documenting long-term
complexity and identity implications.

## 9. Health checks pass while customers fail

**Model answer:** Compare the shallow health path with real host/path, TLS,
identity, payload, and dependencies. Add customer-journey telemetry and a
representative readiness signal without making a shared dependency withdraw
the entire fleet uncontrollably.

## 10. Only IPv6-enabled clients are slow

**Model answer:** Compare A/AAAA answers, address-family preference, IPv6 route
and policy, PMTU, listener, and fallback delay. Fix the incomplete IPv6 path or
withdraw AAAA deliberately; do not assume clients will immediately prefer IPv4.

## 11. Firewall rollout blocks return traffic

**Model answer:** Determine whether the control is stateful, inspect forward and
return routes/rules and ephemeral ports, and compare changed policy revisions.
Roll back the narrow rule set, restore sessions if required, and test policy as
directional flows before the next rollout.

## 12. Partner allow-list breaks after scaling

**Model answer:** Identify every possible egress identity and zone. Autoscaling
behind multiple NAT paths may change source addresses. Stabilize documented
egress, prefer authenticated private/API connectivity, monitor address drift,
and coordinate change windows with the partner.

## 13. Hybrid primary path fails over slowly

**Model answer:** Separate failure detection, BGP convergence, DNS/application
timeouts, and backup capacity. Validate prefix advertisements and route policy,
shift noncritical demand if capacity is limited, and measure end-to-end recovery
rather than only session establishment.

## 14. Cross-zone traffic cost rises suddenly

**Model answer:** Attribute bytes to flows and topology changes: target
distribution, centralized NAT/firewall, service discovery, replication, or
zonal imbalance. Optimize locality only if it preserves failure capacity and
does not create sticky single-zone dependencies.

## 15. A DNSSEC-enabled zone returns SERVFAIL

**Model answer:** Compare validating and non-validating resolvers, delegation,
DS/DNSKEY chain, signatures, time, and recent key/registrar changes. Roll back
the broken chain using the documented ceremony; do not disable validation
globally. Verify authoritative data and representative validating resolvers.
