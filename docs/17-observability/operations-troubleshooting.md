# Operations, Cost, Security, and Troubleshooting

[← Module overview](index.md) · [Scenario answer framework](../interview-playbook/scenario-answer-framework.md)

Telemetry is a production data platform. It needs availability objectives,
capacity, tenancy, change control, security, disaster recovery, cost allocation,
and its own observability—without creating circular dependence on itself.

## Platform reliability

Model the full path: producer → local buffer/agent → collector → network → ingest
→ index/store → query/rule engine → notification → responder. Define loss,
duplication, ordering, delay, and replay tolerance for each signal. Metrics may
accept small gaps; audit evidence may require durable delivery and independent
archive. Never block the application indefinitely to preserve diagnostic telemetry.

Monitor collectors and backends with independent health checks and minimal local
evidence. Track accepted/refused/dropped items, queue length, retry age, export
failures, scrape health, ingestion delay, index lag, query latency/errors, rule
evaluation, notification delivery, storage, and cost.

## Security and privacy

- authenticate producers, collectors, query users, and backend integrations;
- encrypt transport/storage and isolate tenant data and administrative planes;
- prevent secret, token, payload, and personal-data collection by default;
- apply field-level redaction, access logging, retention, legal hold, and deletion;
- protect dashboards and queries from exposing restricted dimensions;
- validate collectors, plugins, agents, and configuration as privileged software.

Telemetry often sees more of the estate than any single application. Compromise
can reveal topology, customer behavior, source paths, queries, credentials, and
incident activity—or allow evidence tampering.

## Cost controls

Allocate cost by service/team/tenant and signal. Control metric series/cardinality,
scrape interval, histogram buckets, log level/fields, trace sample rate, profile
frequency, duplication, hot retention, index selection, query range, and egress.
Use tiered storage and recording/downsampling where semantics remain acceptable.
Do not optimize solely on volume; preserve high-value rare failures and audit needs.

## Troubleshooting workflow

1. **Confirm the question:** user symptom, time, scope, change, and expected signal.
2. **Check producer:** instrumentation loaded, resource identity, sample decision,
   endpoint, credentials, limits, and local errors.
3. **Check collection:** discovery/scrape, receiver counters, parsing, filtering,
   memory limiter, queue, backpressure, retries, and drops.
4. **Check transport/backend:** DNS, TLS, IAM, quota, ingest rejection, partition,
   retention, index, compaction, and replication.
5. **Check query:** time zone/range, data source, label/filter, aggregation, units,
   missing-data semantics, permissions, cache, and query limits.
6. **Check correlation:** trace propagation, service naming, clocks, deployment
   metadata, sampling, tenant mapping, and cross-account/project identity.
7. **Mitigate and verify:** protect applications first, reduce telemetry load or
   bypass faulty processing safely, preserve evidence, replay if supported, and
   confirm end-to-end recovery with a known synthetic signal.

## Adoption model

Provide paved instrumentation libraries, semantic conventions, collector
templates, dashboard/SLO patterns, cost budgets, and self-service validation.
Platform teams own common capability; service teams own domain signals, SLOs,
alerts, and runbooks; security/privacy teams own mandatory handling boundaries.

Return to the [module overview](index.md) when ready to continue.
