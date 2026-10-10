# Observability, OpenTelemetry, Prometheus, and Grafana

[← Curriculum overview](../curriculum/index.md) ·
[Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**
Level: **Senior / Architect**

Observability is the capability to ask useful questions about a running system
from its outputs. It combines intentional instrumentation, reliable telemetry
pipelines, queryable backends, service-level objectives, and investigation
workflows. It is not achieved by installing agents or collecting everything.

!!! tip "Where to start"
    Start with **1. Observability decision model** and follow the numbered path.
    OpenTelemetry, Prometheus, and Grafana provide the vendor-neutral foundation;
    AWS is the primary managed-cloud context. No executable lab is required.

## Learning objectives

By the end of this module, you should be able to:

- distinguish observability, monitoring, telemetry, and reliability outcomes;
- design metrics and Prometheus labels without uncontrolled cardinality;
- structure logs and events for correlation, privacy, and investigation;
- trace distributed requests and choose head, tail, and adaptive sampling;
- explain OpenTelemetry APIs, SDKs, semantic conventions, OTLP, and Collector;
- design resilient Collector pipelines with batching, filtering, routing, and queues;
- use Grafana for governed dashboards, exploration, correlation, and alert context;
- derive SLIs, SLOs, error budgets, and multi-window burn-rate alerts;
- operate secure, cost-aware telemetry platforms and troubleshoot missing signals;
- translate an AWS-first design to Azure and Google Cloud.

## Recommended module path

### Phase 1 — Learn the telemetry and decision system

| Step | Page | Outcome |
| ---: | --- | --- |
| 1 | [Observability decision model](concepts.md) | Connect user outcomes, questions, signals, decisions, and feedback |
| 2 | [Metrics and Prometheus](metrics-prometheus.md) | Design metric types, labels, PromQL, recording rules, and scalable storage |
| 3 | [Logs and events](logs-events.md) | Create structured, correlated, privacy-aware event evidence |
| 4 | [Traces and profiles](traces-profiles.md) | Follow distributed causality and investigate code-level resource use |
| 5 | [OpenTelemetry and Collector pipelines](opentelemetry-collector.md) | Instrument once and operate resilient receiver–processor–exporter paths |
| 6 | [Grafana and signal correlation](grafana-correlation.md) | Build investigation-first dashboards and cross-signal workflows |
| 7 | [SLIs, SLOs, alerting, and response](slos-alerting.md) | Alert on user-impacting risk with owned response and error budgets |
| 8 | [AWS-first and multi-cloud architecture](cloud-architecture.md) | Map open standards to managed AWS, Azure, and Google Cloud services |
| 9 | [Operations, cost, security, and troubleshooting](operations-troubleshooting.md) | Run telemetry as a reliable governed platform |

### Phase 2 — Apply the reasoning

| Step | Page | Outcome |
| ---: | --- | --- |
| 10 | [Enterprise observability design exercise](design-exercise.md) | Modernize fragmented telemetry for an AWS-first platform |
| 11 | [Scenario questions and model answers](scenarios.md) | Practise 15 senior observability scenarios |
| 12 | [Advanced incident drills](scenario-drills.md) | Handle 10 ambiguous telemetry and alerting failures |
| 13 | [Ten-minute observability review](presentation-template.md) | Present outcomes, architecture, reliability, cost, and adoption |

### Phase 3 — Revise and assess

| Step | Page | Outcome |
| ---: | --- | --- |
| 14 | [Rapid-fire revision](rapid-fire.md) | Test 50 concise verbal explanations |
| 15 | [Active-recall flashcards](flashcards.md) | Revisit weak concepts with spaced repetition |
| 16 | [Timed observability mock interview](../mock-interviews/observability-platform.md) | Complete a scored 50-minute assessment |
| 17 | [References and videos](references.md) | Deepen weak areas with standards and primary sources |

## Tooling position

- **OpenTelemetry** is the primary instrumentation, context, protocol, and
  collection standard—not a storage or visualization backend.
- **Prometheus** is the primary metrics and PromQL ecosystem, including exporters,
  rules, Alertmanager, federation, remote write, and compatible long-term stores.
- **Grafana** is the primary visualization, exploration, correlation, and alert
  context layer; Loki, Tempo, and other backends are explained where useful.
- **AWS managed services** are implementation choices, not replacements for the
  signal models and operational decisions above.

## Scope boundary

General production reliability belongs to planned [Module 18](../18-sre/index.md),
Kubernetes platform mechanics to [Module 11](../11-kubernetes/index.md), and
incident-specific host/network troubleshooting to Modules
[06](../06-linux/index.md) and [07](../07-networking/index.md). This module focuses
on telemetry design, platforms, investigation, alerting, and decision quality.

## Completion checklist

- [ ] I can begin with a user question rather than a dashboard or tool.
- [ ] I can predict and control Prometheus series cardinality.
- [ ] I can trace context and correlation across metrics, logs, and traces.
- [ ] I can design Collector and backend failure behavior without losing services.
- [ ] I can build SLO-based alerts with ownership and runbook context.
- [ ] I can explain self-managed, SaaS, and cloud-managed trade-offs.
- [ ] I answered all 25 scenarios aloud and completed the scored mock interview.
