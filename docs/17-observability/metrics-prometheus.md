# Metrics and Prometheus

[← Module overview](index.md) · [Scenario answer framework](../interview-playbook/scenario-answer-framework.md)

Metrics are numeric measurements aggregated across dimensions and time. Prometheus
provides a widely adopted data model, pull-based collection, service discovery,
PromQL, recording/alerting rules, exporters, and an ecosystem of compatible stores.

## Metric types and intent

- **Counter:** cumulative events such as requests or errors; analyze with rate or increase.
- **Gauge:** current value that may rise or fall, such as queue depth or concurrency.
- **Histogram:** bucketed distribution with count and sum; aggregate and estimate quantiles.
- **Summary:** client-calculated observations/quantiles; quantiles generally cannot
  be meaningfully aggregated across instances.

Choose units and monotonicity, define what was counted, and test restart/reset
behavior. Prefer request duration histograms and outcome counters over averaging
already-aggregated values.

## Series and cardinality

A Prometheus time series is a metric name plus a unique label set. Series count
grows approximately as the product of label-value combinations. Never use raw
user ID, request ID, email, unbounded URL, timestamp, or error message as a metric
label. Normalize routes and errors; keep high-cardinality detail in logs or traces.

Before adding a label, estimate current and future values, combinations, scrape
targets, retention, replicas, and query patterns. Set budgets and detect churn,
unused metrics, and expensive queries.

## Collection architecture

Prometheus commonly discovers and scrapes targets. Exporters translate systems
that do not expose native metrics. Pushgateway is for limited short-lived batch
jobs, not a general replacement for scraping. Preserve target health through the
`up` metric and distinguish "zero" from "not collected."

For scale or durability, use federation selectively or remote write to a
Prometheus-compatible system such as Amazon Managed Service for Prometheus,
Thanos, Cortex/Mimir, or another managed backend. Understand out-of-order data,
deduplication, tenancy, write queues, query fan-out, and retention semantics.

## PromQL reasoning

- select the smallest label set and time range that answers the question;
- use `rate()` on counters and aggregate with business-relevant dimensions;
- preserve labels required for routing or diagnosis and intentionally drop others;
- use recording rules for repeated expensive expressions and stable SLI primitives;
- detect missing series explicitly where absence matters;
- test counter resets, low traffic, sparse histograms, and deployment changes.

## Histograms and exemplars

Choose buckets around SLO and diagnostic boundaries, not convenient powers of ten.
Classic histograms multiply series by bucket count; native histograms can reduce
some trade-offs but require compatible producers, backends, and query behavior.
Exemplars attach a trace reference to selected metric observations, enabling a
latency spike to lead to a representative trace without storing trace IDs as labels.

## Prometheus alerting

Prometheus alert rules evaluate conditions; Alertmanager groups, routes, inhibits,
silences, and notifies. Keep rule ownership and runbook annotations in version
control. Test rule evaluation and notification paths independently—an active alert
is not useful if routing or the on-call destination fails.

Return to the [module overview](index.md) when ready to continue.
