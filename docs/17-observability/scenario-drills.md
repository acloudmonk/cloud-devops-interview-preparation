# Advanced Observability Incident Drills

[← Module overview](index.md) ·
[Scenario answer framework](../interview-playbook/scenario-answer-framework.md)

For each drill, state service protection, telemetry-platform containment,
independent evidence, affected decisions, recovery, communication, and prevention.

## 1. A label explosion overloads the metrics backend

Limit or drop the offending series at the nearest safe boundary, protect rule and
query capacity, preserve cardinality evidence, identify producer/version/tenants,
and normalize the label in code. Add budgets, ingestion limits, churn alerts,
instrumentation tests, and ownership; verify SLO metrics were not lost.

## 2. All dashboards go blank during a customer incident

Use independent edge/synthetic, local service, cloud-native, and incident evidence;
check Grafana, identity, data sources, DNS, backend query health, and time settings.
Restore a minimal emergency view, keep responders informed about uncertainty, and
design isolated health paths and cached/runbook access.

## 3. Tail sampling drops the only failing traces

Preserve collector counters/config, lower load or disable faulty policy safely,
route errors through a deterministic keep rule, and use logs/metrics to reconstruct
impact. Repair trace affinity, decision wait, policy ordering, memory/capacity, and
tests for rare errors, long traces, and incomplete spans.

## 4. Alertmanager accepts alerts but no one is paged

Use secondary communication for confirmed impact, inspect rule state, Alertmanager
routing/inhibition/silence, notification integration, credentials, quotas, and
delivery receipts. Restore routing, expire accidental silences, replay/test a known
alert, and add end-to-end synthetic notification monitoring.

## 5. Collector rollout doubles telemetry and cost

Stop the rollout, identify duplicate receivers/exporters or overlapping old agents,
and deduplicate at the safest point without hiding real retries. Quantify affected
metrics/logs/traces and billing, restore single ownership, then add canary volume
comparison, idempotent config generation, and agent-retirement gates.

## 6. Prometheus reports targets down after certificate rotation

Validate target service separately, inspect scrape TLS/auth errors, certificate
chain/name/time, mounted reload, trust bundle, and rollout scope. Restore compatible
overlap or roll back, verify `up` and fresh samples, then automate staged rotation,
expiry alerts, reload validation, and ownership.

## 7. Query load delays SLO rule evaluation

Protect rule capacity from interactive queries, reduce or terminate pathological
work, validate recording-rule freshness and missed evaluations, and communicate SLO
uncertainty. Isolate rule/query resources, precompute common expressions, limit
range/concurrency, improve sharding/caching, and alert on evaluation delay itself.

## 8. Logs arrive 25 minutes late with incorrect timestamps

Preserve source and ingest times, determine clock versus queue/backpressure error,
and use metrics/traces/change systems for current response. Restore time sync and
pipeline capacity, prevent unsafe retrospective alerting, and expose event time,
ingest time, lag, queue age, and late-data handling explicitly.

## 9. Cross-tenant Grafana query exposes customer data

Revoke access/session, disable the data source or vulnerable path, preserve query,
permission, proxy, and backend evidence, identify viewers/data, and notify owners.
Repair backend-enforced tenancy—not only dashboard filters—then test identities,
folders, data-source credentials, query variables, cache, and audit trails.

## 10. Region loss removes the centralized telemetry gateway

Keep applications serving, route to a tested regional gateway or buffer/shedding
mode, preserve local/cloud-native evidence, and constrain cross-region flood. Scale
recovery, reconcile gaps/duplicates, validate alerts, and improve regional autonomy,
DNS/routing, queues, capacity, and disaster exercises.

Return to the [module overview](index.md) when ready to continue.
