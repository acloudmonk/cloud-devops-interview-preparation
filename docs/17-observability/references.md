# Observability References and Videos

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Prefer specifications and official project/provider documentation. Verify current
component maturity, service limits, retention, and pricing before a real design.

## Core reading order

1. [OpenTelemetry concepts](https://opentelemetry.io/docs/concepts/)
2. [Prometheus overview](https://prometheus.io/docs/introduction/overview/)
3. [Prometheus data model](https://prometheus.io/docs/concepts/data_model/)
4. [Grafana fundamentals](https://grafana.com/docs/grafana/latest/fundamentals/)
5. [Google SRE: Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/)

## OpenTelemetry

- [OpenTelemetry specification](https://opentelemetry.io/docs/specs/otel/)
- [Specification status](https://opentelemetry.io/docs/specs/status/)
- [Signals](https://opentelemetry.io/docs/concepts/signals/)
- [Semantic conventions](https://opentelemetry.io/docs/specs/semconv/)
- [Context propagation](https://opentelemetry.io/docs/concepts/context-propagation/)
- [Sampling](https://opentelemetry.io/docs/concepts/sampling/)
- [Collector](https://opentelemetry.io/docs/collector/)
- [Collector configuration](https://opentelemetry.io/docs/collector/configuration/)
- [Collector deployment patterns](https://opentelemetry.io/docs/collector/deployment/)
- [Collector resiliency](https://opentelemetry.io/docs/collector/resiliency/)

## Prometheus

- [Metric and label naming](https://prometheus.io/docs/practices/naming/)
- [Instrumentation practices](https://prometheus.io/docs/practices/instrumentation/)
- [Histograms and summaries](https://prometheus.io/docs/practices/histograms/)
- [PromQL basics](https://prometheus.io/docs/prometheus/latest/querying/basics/)
- [Recording rules](https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/)
- [Alerting overview](https://prometheus.io/docs/alerting/latest/overview/)
- [Alerting practices](https://prometheus.io/docs/practices/alerting/)
- [Remote write tuning](https://prometheus.io/docs/practices/remote_write/)

## Grafana and related projects

- [Grafana dashboards](https://grafana.com/docs/grafana/latest/dashboards/)
- [Grafana Alerting](https://grafana.com/docs/grafana/latest/alerting/)
- [Prometheus data source](https://grafana.com/docs/grafana/latest/datasources/prometheus/)
- [Loki documentation](https://grafana.com/docs/loki/latest/)
- [Tempo documentation](https://grafana.com/docs/tempo/latest/)
- [Mimir documentation](https://grafana.com/docs/mimir/latest/)
- [Pyroscope documentation](https://grafana.com/docs/pyroscope/latest/)

## Reliability and SLOs

- [Google SRE book](https://sre.google/sre-book/table-of-contents/)
- [Google SRE Workbook: Implementing SLOs](https://sre.google/workbook/implementing-slos/)
- [Google SRE Workbook: Alerting on SLOs](https://sre.google/workbook/alerting-on-slos/)
- [OpenSLO specification](https://openslo.com/)

## AWS anchor

- [AWS observability best practices](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/observability.html)
- [AWS Distro for OpenTelemetry](https://aws-otel.github.io/)
- [ADOT with AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/xray-services-adot.html)
- [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
- [Amazon Managed Service for Prometheus](https://docs.aws.amazon.com/prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus.html)
- [Amazon Managed Grafana](https://docs.aws.amazon.com/grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.html)
- [CloudWatch cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html)

## Azure and Google Cloud translation

- [Azure Monitor overview](https://learn.microsoft.com/en-us/azure/azure-monitor/fundamentals/overview)
- [Azure Monitor OpenTelemetry](https://learn.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-overview)
- [Azure managed Prometheus](https://learn.microsoft.com/en-us/azure/azure-monitor/metrics/prometheus-metrics-overview)
- [Azure Managed Grafana](https://learn.microsoft.com/en-us/azure/managed-grafana/overview)
- [Google Cloud Observability](https://cloud.google.com/products/observability)
- [Google Cloud Managed Service for Prometheus](https://cloud.google.com/stackdriver/docs/managed-prometheus)
- [Google Cloud: Instrument for Cloud Trace](https://docs.cloud.google.com/trace/docs/setup)

## Video channels

- [OpenTelemetry](https://www.youtube.com/@OpenTelemetry)
- [Prometheus](https://www.youtube.com/@PrometheusMonitoring)
- [Grafana](https://www.youtube.com/@Grafana)
- [CNCF](https://www.youtube.com/@cncf)
- [AWS Events](https://www.youtube.com/@AWSEventsChannel)
- [Microsoft Azure](https://www.youtube.com/@MicrosoftAzure)
- [Google Cloud Tech](https://www.youtube.com/@googlecloudtech)

## Books

- *Observability Engineering* by Charity Majors, Liz Fong-Jones, and George Miranda
- *Distributed Systems Observability* by Cindy Sridharan
- *Prometheus: Up & Running* by Brian Brazil
- *Site Reliability Engineering* and *The Site Reliability Workbook* by Google

Use books for durable reasoning and current official documentation for component
behavior. After each source, explain the question it helps answer, its blind spots,
and what happens when the telemetry path fails.

Return to the [module overview](index.md) when ready to continue.
