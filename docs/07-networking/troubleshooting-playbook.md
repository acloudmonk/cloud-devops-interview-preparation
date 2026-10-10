# Network Troubleshooting Playbook

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

## Universal sequence

1. Define the failed customer journey, start time, scope, and expected result.
2. Identify the last known success and recent DNS, route, policy, certificate,
   deployment, provider, or dependency changes.
3. Draw the expected forward and return path with ownership boundaries.
4. Reproduce from a representative source without broadening impact.
5. Find the lowest layer that succeeds and the first boundary that fails.
6. Compare affected and healthy client, resolver, address, zone, path, or target.
7. Test a falsifiable hypothesis with the least invasive evidence.
8. Apply a reversible mitigation with owner, rollback, and expiry.
9. Verify the original customer journey and watch saturation/error signals.
10. Reconcile temporary controls and prevent recurrence.

## Symptom-to-boundary map

| Observation | Next boundary to test |
| --- | --- |
| Name fails | resolver selection, response code, delegation, private view, DNSSEC |
| Correct address, connect timeout | route, forward/return policy, translation/state, target reachability |
| Immediate refusal/reset | listener, target selection, reject policy, proxy/backend reset |
| TLS error | SNI, certificate identity/chain/time, protocol, mTLS, termination point |
| HTTP 4xx/5xx | response origin, proxy route, identity/WAF, backend and dependency evidence |
| Only large transfers fail | MTU/MSS, fragmentation, loss, proxy/body limits |
| Only some clients fail | resolver/cache, IPv4/IPv6, geography, ISP, policy identity, path |
| Degrades under load | ports/state, queues, targets, retry amplification, bandwidth, dependencies |

## Evidence map

Commands are examples of questions, not a blind script.

| Question | Common evidence |
| --- | --- |
| What answer did this client receive? | resolver query with explicit server/type, cache and authoritative comparison |
| Which route and source address are selected? | effective cloud routes and host route lookup |
| Is transport established? | socket state, bounded connection test, SYN/SYN-ACK behavior |
| What certificate/protocol was negotiated? | TLS handshake metadata using correct SNI |
| Which intermediary responded? | response headers, request ID, load-balancer/proxy/WAF logs |
| Was traffic accepted or rejected? | flow/firewall logs plus policy and route analysis |
| Is loss or MTU involved? | interface errors, retransmissions, size-controlled tests, bounded capture |

Flow logs are metadata and may sample or aggregate; absence is not universal
proof that no packet existed. Packet captures show traffic at one observation
point, not the whole path.

## Safe mitigation patterns

- rollback the smallest recent policy, route, DNS, or certificate change;
- shift a bounded portion of traffic to a known-good target/path;
- remove one unhealthy target while preserving fleet capacity;
- reduce retry/admission pressure before scaling a constrained intermediary;
- restore a previous DNS answer while keeping both endpoints healthy;
- use an approved private break-glass path rather than opening broad public access.

## Anti-patterns

- opening all ports/CIDRs “to test”;
- flushing every cache or rebooting every endpoint before collecting evidence;
- disabling TLS verification or security controls without bounded approval;
- changing DNS, routes, and firewall rules simultaneously;
- trusting one client, one resolver, ping, or a green control-plane status;
- collecting unrestricted packet payloads into tickets or chat.

## Incident close

Report impact, affected path, evidence, root/triggering conditions, mitigation,
verification, remaining risk, temporary-control expiry, owner, and next decision.
