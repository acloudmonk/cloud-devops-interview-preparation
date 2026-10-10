# Networking Active-Recall Flashcards

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Use each prompt without viewing the cue. Explain mechanism, failure implication,
and the next discriminating question.

| Prompt | Answer cue |
| --- | --- |
| Request-path boundaries | DNS, route, policy, transport, TLS, proxy, service, dependency, return |
| Address-plan reserve | peak, surge, managed interfaces, zones, growth, integration |
| Longest-prefix match | most specific destination prefix, then platform precedence |
| Route is insufficient | return route, policy, state, listener, health |
| NAT pressure | translations/ports, destination concentration, reuse, timeouts |
| MTU symptom | small succeeds, large stalls; PMTU/ICMP/MSS/tunnel |
| Recursive DNS evidence | server, type, response code, answer, authority, TTL, cache |
| DNS cutover safety | lower early, validate, observe, retain old path, restore TTL |
| Split-horizon risk | resolver context, forwarding, inconsistent views, recovery |
| DNSSEC boundary | integrity/authenticity, not encryption or application identity |
| TCP timeout/refusal/reset | no handshake / active reject / active state termination |
| Port exhaustion | many new flows sharing finite source/state capacity |
| TLS identity | SNI, name, chain, trust, time, policy, mTLS |
| Timeout budget | customer deadline allocated inward with bounded recovery |
| Retry safety | idempotency, ownership, backoff/jitter, shared deadline, amplification |
| Health-check design | representative, cheap, uncached, dependency and threshold choices |
| Draining | stop assignment, bound completion, reconcile unfinished work |
| Trusted client address | accept forwarding metadata only from known proxy hops |
| AWS SG versus NACL | stateful ENI allow policy versus stateless subnet ordered policy |
| Private endpoint dependencies | DNS, endpoint/consumer policy, route/platform support, quotas |
| Hybrid redundancy | independent underlay/edge/device plus post-failure capacity |
| BGP review | prefixes, filters, preference, path, convergence, maximum-prefix |
| Evidence sensitivity | captures/logs expose identities, destinations, tokens, payloads |
| Safe mitigation | smallest reversible change, owner, rollback, expiry, verification |
| Recovery proof | representative customer outcome and normalized capacity/error state |

Review missed cards after one day, three days, and seven days.
