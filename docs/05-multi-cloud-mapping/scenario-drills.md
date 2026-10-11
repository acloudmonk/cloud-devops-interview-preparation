# Advanced Architecture and Incident Drills

[← Scenarios](scenarios.md) · [Next: Presentation →](presentation-template.md)

State evidence, stabilization, hypotheses, recovery, validation, prevention, and owner.

## 1. Federation fails in one provider

Check IdP health, metadata/keys, audience, claims, clock, token exchange, role mapping,
and audit logs. Freeze risky change, use monitored break glass, restore trust, validate
least privilege, and exercise federation/key rotation regularly.

## 2. Intercloud route leak

Contain propagation, preserve management access, inspect BGP advertisements and route
tables, restore approved prefixes, and verify return paths. Add prefix filters, maximum
routes, staged changes, ownership, and reachability tests.

## 3. DNS gives provider-dependent answers

Trace authoritative zones, forwarding, split horizon, caches, TTL, resolver paths, and
health logic from each location. Restore one intended authority and add synthetic tests
without hard-coded host overrides.

## 4. Cross-cloud replication silently lags

Measure source position, connector health, schema errors, throttling, bandwidth, and
destination apply delay. Protect downstream decisions, recover safely, reconcile
business invariants, and alert on freshness rather than process uptime.

## 5. Failover creates dual writers

Fence one side, stop unsafe writes, establish authority, preserve evidence, and
reconcile with business rules. Redesign leases/epochs, trigger ownership, idempotency,
and failback testing to prevent split brain.

## 6. Unified telemetry pipeline fails

Use native consoles and audit paths, declare reduced visibility, buffer where safe, and
limit risky change. Restore ingestion, verify gaps, then improve redundancy, sampling,
backpressure, cost controls, and runbooks.

## 7. Portable container fails only on one cloud

Compare CPU architecture, kernel/runtime, identity, DNS, MTU, load balancer, storage,
policy, limits, and health probes. Reproduce with conformance tests and document the
provider adapter rather than weakening all platforms.

## 8. Commitment savings become waste

Reconcile utilization, scope, term, purchase owner, migration forecast, and allocation.
Avoid unsafe load shifts; use eligible demand and marketplace options where valid, then
add forecasting, approval, coverage/utilization targets, and exit-aware purchasing.

## 9. Shared security policy blocks recovery

Identify the native policy and inherited scope, validate the recovery design, and use
only a pre-authorized expiring exception. Add policy simulation, recovery conformance,
and evidence before the next exercise.

## 10. Provider outage status conflicts with telemetry

Trust measured user impact, compare multiple regions/providers and external probes,
open support cases, stabilize via tested degradation, and communicate uncertainty.
Preserve a timeline and improve independent detection.

## 11. Egress cost spikes after architecture change

Use native billing and flow logs to identify path, source, destination, and SKU.
Correct unintended routing/cross-zone/cloud chatter, preserve reliability, and add
topology-aware cost tests and unit-cost alerts.
