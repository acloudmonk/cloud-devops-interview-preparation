# Enterprise Observability Design Exercise

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

This is a paper exercise. Begin with business questions, reliability, ownership,
and failure behavior—not a tool shopping list.

## Scenario

A digital-commerce company runs 250 services across EKS, ECS, Lambda, EC2, and
on-premises systems, with smaller Azure and GCP estates. Teams use five agents,
three logging platforms, inconsistent Prometheus labels, and dashboard copies.
CloudWatch cost doubled, traces cover only 15% of requests, critical alerts are
noisy, and a recent checkout incident took 95 minutes to isolate. The company
wants OpenTelemetry, Prometheus, and Grafana without an unsafe "collect everything"
migration.

## Deliverables

1. **Discovery:** user journeys, services, SLOs, incidents, telemetry inventory,
   schemas, owners, platforms, volume, cost, privacy, and regulatory constraints.
2. **Question map:** availability, latency, correctness, affected cohort,
   dependency, change, capacity, and mitigation questions for checkout.
3. **Signal contract:** RED/USE metrics, bounded labels/histograms, structured
   events, trace spans/context, profiles, deployment and ownership metadata.
4. **Collection:** SDK/auto-instrumentation, Prometheus discovery/scraping, ADOT/
   OTel agents and gateways, receivers/processors/exporters, queues, and tenancy.
5. **Backends:** CloudWatch, X-Ray, AMP, AMG, log/search, retention, archive,
   multi-cloud locality, and portability boundaries.
6. **Reliability:** overload, backend outage, WAN failure, configuration rollback,
   loss/duplication, replay, regional isolation, and independent health evidence.
7. **Experience:** SLOs, burn alerts, service/diagnostic dashboards, exemplars,
   trace-log-change-profile correlation, runbooks, and incident access.
8. **Security/cost:** secrets and personal-data prevention, IAM, tenancy, audit,
   cardinality, sampling, indexing, retention, egress, and chargeback.
9. **Migration:** one journey pilot, dual-run boundaries, data parity, agent
   retirement, observe/warn/enforce standards, training, and legacy exceptions.
10. **Measures:** detection/isolation/mitigation time, SLO coverage, alert quality,
    trace completeness, dropped telemetry, query success, adoption, and unit cost.

## Decision worksheets

| Question | Signal and source | Dimensions/context | Retention | Owner/action |
| --- | --- | --- | --- | --- |
| Why are checkouts slow? | duration histogram + sampled traces | region, route, version, dependency | metrics 15 months; traces 14 days | checkout team investigates burn |

| Pipeline failure | Application behavior | Buffer/retry/loss | Recovery evidence |
| --- | --- | --- | --- |
| Trace backend unavailable | requests continue | bounded queue then sampled drop | exporter counters and synthetic trace |

## Review rubric

Score 0–4 for discovery/questions, signal design, Prometheus, OpenTelemetry,
Grafana/correlation, SLO/alerting, platform reliability, security/cost, migration/
measures, and executive communication. A strong answer states what will not be
collected and how application reliability is protected from telemetry failure.

Return to the [module overview](index.md) when ready to continue.
