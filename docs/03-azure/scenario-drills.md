# Advanced Azure Architecture and Incident Drills

[← Scenario questions](scenarios.md) · [Next: Presentation template →](presentation-template.md)

For each drill, state containment, investigation, authority, recovery, communication,
evidence, and prevention. Practise a three-minute response.

## Drill 1 — Deny Policy blocks recovery

Confirm the Policy assignment, definition, effect, scope, evaluation, and denied field
from Activity Log/deployment evidence. Use a preauthorized, narrow, expiring exemption
or corrected version through accountable owners; do not disable the initiative for all
subscriptions. Restore service, record compensating controls, remove the exemption,
and stage/test organization-wide Policy changes plus recovery actions in nonproduction.

## Drill 2 — One zone lacks VM SKU capacity

Inspect allocation errors, SKU, zone, VMSS orchestration, quota, proximity/placement,
disk/network needs, and image/extensions. Shift safely to proven remaining-zone or
alternate-SKU capacity, protect downstreams, and degrade lower-priority work if needed.
Future design should diversify compatible SKUs/zones, maintain failure headroom, use
capacity reservations only when justified, and exercise zonal scarcity.

## Drill 3 — Private DNS breaks hybrid access

Compare the service FQDN and CNAME chain from Azure and on-premises resolvers. Verify
private DNS zone, records, VNet links, Azure DNS Private Resolver endpoints/rulesets or
forwarders, routes, firewall, and return traffic. Restore correct authoritative
resolution without public fallback that violates policy. Add automated registration,
split-horizon tests, ownership, and monitoring for every private endpoint lifecycle.

## Drill 4 — SNAT port exhaustion causes intermittent calls

Confirm with NAT/load-balancer/App Service metrics, connection counts, destination,
reuse, timeouts, and network topology. Reduce needless new connections, fix pooling and
timeouts, apply NAT Gateway or appropriate outbound design, and control concurrency.
Do not merely add public IPs without modeling demand and failure. Add connection/SNAT
budgets, alerts, load tests, and private service paths where justified.

## Drill 5 — Key Vault is unavailable during restore

Identify whether failure is identity, RBAC/access policy, private DNS/network, firewall,
vault/Region, soft-delete state, key version, throttling, or dependency order. Preserve
data, use controlled emergency access, and restore key/secret availability before broad
changes. Validate the recovered application, then improve dependency inventory,
authorization separation, purge protection, network/DNS recovery, caching policy, and
isolated restore exercises.

## Drill 6 — Service Bus session is blocked by poison work

Measure oldest age, active/dead-letter messages, delivery count, lock loss, session
state, consumer health, downstream latency, and duplicate effects. Quarantine the
poison message/session according to business ordering rules; scale only within
downstream budgets. Correct validation, idempotency, lock renewal, retry/DLQ handling,
safe redrive, and monitoring of business completion rather than namespace health.

## Drill 7 — Azure SQL failover completes but checkout stays down

Trace connection-string endpoint, DNS/cache, driver retry, pool state, authentication,
managed identity token, firewall/private endpoint, TLS, transaction outcome, and
dependency capacity. Stop retry amplification and determine whether writes committed.
Restore bounded idempotent behavior and reconcile orders/payments. Test failover with
the application, network, identity, alerts, and business invariants—not only SQL status.

## Drill 8 — Hub firewall change affects all subscriptions

Freeze further rollout, identify route/policy version and affected spokes/flows, and
restore the last known safe configuration through the audited delivery path or bounded
break-glass. Validate asymmetric routes, DNS, health, and return traffic. Reduce future
blast radius using staged rings, policy tests, synthetic flows, change bounds, regional
independence, consumer fallbacks, and explicit shared-service SLO/ownership.

## Drill 9 — Regional failover creates split writes

Fence one writer and preserve logs before changing routing. Determine committed writes,
replication state, consistency choice, conflict policy, timestamps/order assumptions,
and business invariants. Data owners select authority; reconcile or compensate and
restore controlled service. Redesign write ownership, health criteria, failover rights,
idempotency, conflict resolution, failback, and regular game-day evidence.

## Drill 10 — Cost anomaly follows a release

Correlate Cost Management exports, deployment time, meter/resource IDs, usage, requests,
egress, Firewall/NAT, logs, retries, scaling, licensing, and marketplace charges.
Contain runaway behavior with safe rollback, budgets, quotas, or concurrency while
preserving priority journeys. Compare unit economics and performance. Add cost forecast,
telemetry, ownership tags, anomaly routing, and transfer/retry tests to delivery gates.

## Drill 11 — Entra or federation is unavailable

Separate existing workload tokens/data planes from new workforce sessions. Preserve
service, invoke protected and tested emergency-access accounts for essential actions,
and avoid uncontrolled local identities. Coordinate with identity owners, monitor every
session, and revoke/rotate after recovery. Regularly validate emergency access,
Conditional Access exclusions, tenant contacts, managed-identity dependencies, token
lifetime assumptions, and support escalation.
