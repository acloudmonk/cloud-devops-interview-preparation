# Observability Scenario Questions and Model Answers

[← Module overview](index.md) ·
[Scenario answer framework](../interview-playbook/scenario-answer-framework.md)

Answer each aloud before reading the model. Begin with the user/business question,
then cover signals, pipeline, failure modes, ownership, cost, and validation.

## 1. Design observability for a checkout journey

**Model answer:** Define availability, correctness, and latency SLIs at the edge
and application boundary; map service and external dependencies; emit bounded RED
metrics, structured outcome events, distributed traces with stable resource/version
attributes, deployment changes, and profiles where needed. Route through resilient
OTel/ADOT collectors to AWS and Prometheus-compatible backends, expose SLO burn
and drill-down in Grafana, and verify the complete workflow with failure tests.

## 2. Prometheus memory rises rapidly after a release

**Model answer:** Protect the metrics platform, compare active series and churn by
metric/label/target/version, and find unbounded values such as request IDs or raw
paths. Drop or relabel the offending dimension at ingestion as a temporary guard,
fix instrumentation to normalize it, remove obsolete series where possible, and
add cardinality budgets, pre-release tests, ownership, and per-tenant limits.

## 3. Logs are present but responders cannot isolate an incident

**Model answer:** Start with failed investigation questions. Standardize resource,
service, environment, version, outcome, error class, trace/request correlation,
schema version, and change events; fix time synchronization and ingestion delay;
index the fields actually used; and link Grafana views to traces and deployments.
More log volume will not repair inconsistent semantics.

## 4. Only 10% of traces are retained

**Model answer:** A percentage alone says little. Confirm sampling location and
probability, traffic distribution, rare-error retention, route/service coverage,
propagation, partial traces, and analysis intent. Use head sampling for predictable
cost or tail sampling for outcome-aware retention, preserve representative normal
traffic, apply tenant/cost limits, and track accepted versus exported spans.

## 5. Choose CloudWatch or Prometheus

**Model answer:** It is often both, with deliberate boundaries. CloudWatch fits
AWS-native services, logs, alarms, and operational integrations; Prometheus fits
application/Kubernetes metrics, PromQL, exporters, and portable conventions. Use
ADOT/OTel and AMG for correlation where appropriate, avoid duplicating every
metric, define the alert authority, and compare cost, scale, availability, IAM,
retention, and team skills.

## 6. Design OpenTelemetry Collector topology for EKS

**Model answer:** Use agents/DaemonSets for node-local collection and host context,
gateways for centralized enrichment, routing, egress, and tail sampling where
required. Separate pipelines/tenants and scale on throughput and queue pressure.
Configure memory limiting, batching, bounded queues, retries, health, disruption
budgets, zone spread, least-privilege roles, config canaries, and internal telemetry.

## 7. The trace backend is unavailable

**Model answer:** Application requests must continue. Use asynchronous bounded
export, local/gateway queues, exponential backoff, and persistent queues only when
loss needs justify disk/operations. Shed lower-value telemetry before exhausting
memory, preserve exporter/drop counters independently, reduce sampling if needed,
recover the backend, replay supported data, and validate with a synthetic trace.

## 8. Build alerts for a 99.9% availability SLO

**Model answer:** Define valid and good events plus measurement source/window, then
compute budget as 0.1% bad events. Use multi-window burn alerts: a fast/high-burn
page for severe consumption and a slower/lower-burn path for sustained risk.
Attach affected service/journey, owner, evidence, dashboard, runbook, and safe
actions; test low traffic, missing data, alert routing, inhibition, and recovery.

## 9. Grafana dashboards disagree with alerts

**Model answer:** Compare data source, query, time range, step, aggregation, labels,
recording-rule freshness, variables, timezone, and no-data behavior. Alert rules
may evaluate server-side without dashboard variables or from a different backend.
Choose one version-controlled rule authority, link the exact query/panel, and test
both against known data rather than assuming the visualization is correct.

## 10. Reduce observability cost by 40%

**Model answer:** Allocate cost and value by service, signal, tenant, and query.
Remove unused/high-cardinality metrics, tune scrape intervals and buckets, reduce
duplicate pipelines, control debug logs and indexed fields, apply value-aware trace
sampling, tier retention, govern query ranges, and reduce cross-region/cloud egress.
Protect SLO, security, audit, and rare-failure evidence and measure incident impact.

## 11. Support AWS, Azure, and GCP from one platform

**Model answer:** Standardize OTel resource/semantic conventions, service ownership,
SLOs, and investigation workflows; deploy regional collectors and provider-native
identities; and preserve native cloud resource attributes. Choose local storage,
central copy, or federated query per residency, latency, availability, and cost.
Map capabilities without claiming identical query or alert semantics.

## 12. Metrics show success but customers report errors

**Model answer:** Validate where the metric is measured and whether retries,
asynchronous completion, client failures, stale caches, or business correctness are
excluded. Compare edge/client synthetics, application outcome events, traces, logs,
and support evidence. Repair the SLI population/good-event definition and add a
journey measurement point rather than merely lowering a threshold.

## 13. A collector transform leaked personal data

**Model answer:** Stop or quarantine the export, restrict access, preserve config
and audit evidence, determine affected fields/backends/tenants/time, involve privacy
and data owners, delete or protect data under policy, and rotate secrets if exposed.
Prevent at source, add schema allowlists/redaction tests, canary transforms, least
privilege, retention controls, and detection for prohibited fields.

## 14. Alert volume overwhelms the on-call team

**Model answer:** Protect response capacity: group related alerts, inhibit dependent
noise, pause clearly unsafe rules with ownership, and focus on user-impact symptoms.
Analyze pages by service/rule/cause/action, move non-urgent work to tickets, delete
ownerless alerts, add SLO burn alerts, fix flapping/no-data behavior, and measure
pages, duplicates, false outcomes, and runbook effectiveness.

## 15. Plan an observability modernization

**Model answer:** Inventory journeys, tools, signals, costs, incidents, owners, and
constraints. Establish semantic/resource conventions and paved OTel, Prometheus,
Grafana, SLO, and dashboard patterns. Pilot one critical journey, prove query and
incident value, reliability, privacy, and unit cost; migrate in waves with bounded
dual run; retire redundant agents/backends; and measure detection/isolation time,
alert quality, coverage, drops, adoption, and cost.

Return to the [module overview](index.md) when ready to continue.
