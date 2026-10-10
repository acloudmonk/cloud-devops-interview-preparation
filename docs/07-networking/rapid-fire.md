# Networking Rapid-Fire Revision

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

Answer each in 30–60 seconds with a definition, operational consequence, and
one condition that changes the answer.

## Addressing and routing

1. **What does `/24` mean?** The first 24 IPv4 bits identify the prefix, leaving 8 address bits before reservations.
2. **Longest-prefix match?** The most specific matching route normally wins before platform-specific precedence.
3. **Route versus reachability?** A route selects a next hop; policy, return path, listener, and health still matter.
4. **Private address means secure?** No; it is an Internet-routing property, not authorization.
5. **Why avoid CIDR overlap?** It makes destination routing ambiguous and constrains connectivity options.
6. **Stateful versus stateless firewall?** Stateful controls remember flows; stateless controls require rules for both directions.
7. **NAT gateway purpose?** Address/port translation for flows; it is not a general application firewall.
8. **NAT exhaustion symptom?** New outbound connections time out while established flows may continue.
9. **Asymmetric routing risk?** Return traffic can bypass the device holding required flow state.
10. **MTU black hole?** Oversized traffic fails because fragmentation/path-MTU signaling is ineffective.

## DNS

1. **Recursive versus authoritative server?** A recursive resolver obtains/caches answers; an authority publishes zone data.
2. **TTL guarantee?** It limits cache validity but does not guarantee universal convergence at that time.
3. **NXDOMAIN versus NODATA?** Name absent versus name present without the requested type.
4. **SERVFAIL?** Resolver could not complete resolution, often due to delegation, authority, reachability, or validation failure.
5. **CNAME concern?** Adds another lookup and usually cannot be used at a standards-based zone apex.
6. **Split-horizon DNS?** Different answers by resolver/network context, with consistency and recovery risks.
7. **Negative caching?** Resolvers can cache absence, delaying visibility after a name is created.
8. **DNS health-check limit?** It cannot remove cached answers or prove established/application flows.
9. **DNSSEC provides?** Origin authentication and integrity of DNS data, not query confidentiality.
10. **Safe cutover?** Lower TTL in advance, validate both paths, change, observe representative resolvers, retain rollback.

## Transport, HTTP, and TLS

1. **TCP provides?** Reliable ordered byte-stream delivery between transport endpoints, not application processing.
2. **Connect timeout versus refusal?** Silent/no completed handshake versus reachable active rejection/no listener.
3. **TCP reset?** A peer or intermediary actively terminated connection state.
4. **Why use connection pools?** Reduce handshake cost and port usage, while managing stale/imbalanced connections.
5. **UDP trade-off?** Low-overhead datagrams but application-owned delivery, ordering, retry, and congestion behavior.
6. **TCP/53 requirement?** DNS may need TCP for large/truncated answers and operations such as zone transfer.
7. **TLS SNI?** Client indicates intended server name so a shared endpoint can select certificate/configuration.
8. **Certificate chain?** Leaf identity links through intermediates to a trusted root with policy and validity checks.
9. **HTTP 502 meaning?** A gateway/proxy received an invalid or unusable upstream response; locate the responder.
10. **Retry danger?** Non-idempotent duplication and multiplicative load across layers.

## Balancing and cloud networking

1. **Layer 4 versus Layer 7 balancing?** Transport tuple selection versus application-aware HTTP routing/termination.
2. **Liveness versus readiness?** Replace/restart eligibility versus ability to receive traffic now.
3. **Deep health-check risk?** Shared dependency failure can withdraw every otherwise useful target.
4. **Connection draining?** Stop new assignment while allowing bounded completion of established work.
5. **Sticky-session cost?** Hotspots, state coupling, and harder failover/deployment.
6. **AWS security group?** Stateful allow policy attached to network interfaces.
7. **AWS network ACL?** Ordered stateless subnet policy requiring directional rules.
8. **Public subnet?** A subnet whose effective route supports an Internet gateway path; workload exposure still needs addressing/policy.
9. **Private endpoint value?** Service access without broad routed/public exposure, with DNS and policy dependencies.
10. **Flow-log limit?** Observation-point metadata may be filtered/aggregated; absence is not universal packet proof.

## Operations and architecture

1. **First incident question?** Which customer journey fails, since when, and across which scope?
2. **Why compare a healthy peer?** It identifies material differences faster than an unconstrained checklist.
3. **Control plane versus data plane?** Stored/programmed intent versus actual traffic forwarding.
4. **Why draw return path?** Stateful and routing failures often exist only on the response direction.
5. **Dedicated link means encrypted?** No; privacy of transport and end-to-end encryption are separate decisions.
6. **BGP proves health?** No; it exchanges reachability policy, not application readiness.
7. **Redundant links requirement?** Independent failure domains and enough post-failure capacity.
8. **Centralized inspection trade-off?** Consistent policy versus latency, cost, route complexity, and shared blast radius.
9. **What verifies recovery?** Original customer flow plus error, latency, state, capacity, and reconciliation evidence.
10. **Principal-level close?** Impact, evidence, mitigation, remaining risk, owner, validation, and next decision.
