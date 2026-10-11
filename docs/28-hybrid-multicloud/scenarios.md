# Scenario Questions and Model Answers

[← Module overview](index.md) · [Scenario answer framework](../interview-playbook/scenario-answer-framework.md)

Answer aloud before reading. State driver, placement, boundaries, failure behavior,
operation, economics, decision owner, evidence, and residual risk.

## 1. Leadership mandates multi-cloud to avoid lock-in

**Model answer:** Define which lock-in creates unacceptable business risk and required
exit time. Compare contractual, data, identity, skills, managed-service, and operational
coupling with a single-provider multi-Region option. Set portability tiers per workload,
preserve data export and open interfaces, and test one representative exit. Avoid paying
for identical live stacks without a continuity requirement and operating evidence.

## 2. Kubernetes is proposed as the portability solution

**Model answer:** Kubernetes standardizes part of the workload API, not databases,
identity, networking, storage, load balancing, observability, managed services, or
operations. Define the actual move target and time, isolate provider adapters, use
portable artifacts/contracts where valuable, and prove deployment plus data migration.

## 3. CIDR ranges overlap after an acquisition

**Model answer:** Inventory routes, names, traffic, ownership, and transition deadline.
Prefer strategic re-addressing for a permanent estate; use NAT, proxies, service mesh,
or application gateways as controlled transition patterns. Prevent ambiguous routing,
preserve source identity/observability, test return paths, and retire translation debt.

## 4. Direct Connect fails but VPN backup is undersized

**Model answer:** Prioritize critical traffic, apply admission control, pause bulk
replication/backups, and monitor latency/loss. Validate BGP convergence and inspection.
Resize and diversify backup paths against failure demand, test regularly, and state
whether carrier/metro/device dependencies are genuinely independent.

## 5. Central identity outage affects all clouds

**Model answer:** Invoke one incident, preserve security, use constrained provider-local
emergency roles, stop risky changes, and restore federation deliberately. Pre-provision
phishing-resistant break-glass access, logging, expiry, alternate communication, and
recovery tests. Diversity without identity recovery is not independent resilience.

## 6. Cross-cloud latency breaks a synchronous API chain

**Model answer:** Measure geography, path, DNS, TLS, queues, retries, and downstream
time. Co-locate tightly coupled components/data or redesign to asynchronous messaging,
caching, local reads, and bounded consistency. Do not solve physics with larger timeouts;
test degraded and disconnected modes.

## 7. Analytics egress cost triples

**Model answer:** Trace datasets, direction, frequency, duplication, queries, compression,
and business owner. Move processing to data where possible, transfer aggregates/increments,
cache/batch/compress, or renegotiate placement. Include privacy, freshness, lineage,
commitments, and migration cost; validate unit cost per useful analytics outcome.

## 8. A provider Region lacks a required service

**Model answer:** Revisit the placement driver and quality requirements. Options include
another Region/provider, a portable component, alternate managed service, on-prem/edge,
or changed feature. Compare data residency, latency, operations, support, cost, and
exit. Avoid inserting a remote synchronous dependency that defeats the original goal.

## 9. Multi-cloud DR accepts writes in both providers

**Model answer:** Fence unsafe writers, establish authoritative state, preserve logs,
and reconcile by domain semantics. Redesign single-writer promotion, sharding, or
explicit conflict resolution with idempotency and RPO. Test data readiness before
routing and include failback; DNS failover alone is insufficient.

## 10. One observability platform loses visibility everywhere

**Model answer:** Retain local/provider telemetry and incident access, buffer critical
signals, and use independent health paths. Restore the central view without making it
the sole detector. Define minimum telemetry, retention, time sync, semantic mapping,
and drills where the aggregation plane is unavailable.

## 11. Security wants identical policy across providers

**Model answer:** Standardize control objectives, evidence, severity, and exception
process, then implement with provider-native semantics. Map gaps explicitly and use
policy as code where reliable. Lowest-common-denominator syntax can discard stronger
controls; identical text does not guarantee equivalent enforcement.

## 12. A factory loses WAN connectivity

**Model answer:** Safety and critical process control must remain local. Switch to
predefined autonomous mode with local identity/policy/data, bounded queues, operator
procedures, and safe capacity. On reconnection, authenticate, validate time/order,
replay idempotently, resolve conflicts, and monitor reconciliation.

## 13. Teams deploy independently and schemas diverge

**Model answer:** Stop incompatible rollout, use versioned contracts and compatibility
tests, identify authoritative schema and affected messages/data, then reconcile safely.
Create ownership, registry/version policy, consumer-driven testing, phased evolution,
and replay evidence across environments.

## 14. Multi-cloud cost exceeds forecast by 40%

**Model answer:** Reconcile provider bases and allocate connectivity, egress, duplicated
platforms, support, licenses, people, and idle resilience. Separate valuable growth
from unintended coupling. Optimize placement and lifecycle, retire transition paths,
and revisit whether each original driver still justifies full TCO.

## 15. The board requests provider exit in six months

**Model answer:** Define scope and trigger, inventory data/features/contracts/commitments,
select target and minimum service, and sequence foundations, data, applications, traffic,
and deletion. Test export/import and dual-run reconciliation, fund skills and operations,
communicate risk, and negotiate scope if evidence shows six months is not achievable.

Return to the [module overview](index.md) when ready to continue.
