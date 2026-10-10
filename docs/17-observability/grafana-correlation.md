# Grafana and Signal Correlation

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Grafana queries and visualizes many data sources and can support dashboards,
exploration, alerting, and cross-signal links. It does not make inconsistent
telemetry meaningful automatically; signal contracts and investigation workflows
must come first.

## Dashboard hierarchy

1. **Executive/service health:** user journeys, SLOs, demand, impact, and ownership.
2. **Service operations:** RED signals—rate, errors, duration—by bounded dimensions.
3. **Resource/platform:** USE signals—utilization, saturation, errors—and capacity.
4. **Dependency:** upstream/downstream health, queues, databases, external providers.
5. **Investigation:** high-detail drill-down, logs, traces, changes, and profiles.

Every dashboard should name purpose, audience, service/owner, environment, time
semantics, units, data source, freshness, and expected response. Provision
dashboards as code where reproducibility and review matter; maintain an emergency
minimal view when the primary dashboard path is impaired.

## Grafana practices

- Use variables for bounded navigation, not queries that enumerate unbounded tenants.
- Keep units, legends, thresholds, and aggregation explicit.
- Prefer shared library panels/templates carefully; hidden coupling can spread errors.
- Link panels to runbooks, alert rules, logs, traces, deployments, and owners.
- Version data-source and folder permissions; separate viewer, editor, and admin roles.
- Test query cost and behavior when data is missing, delayed, partial, or duplicated.

## Correlation workflow

A responder might start with an SLO burn panel, segment a Prometheus metric by
region/version, select an exemplar into a Tempo, X-Ray, or other trace backend,
open trace-correlated Loki/OpenSearch/CloudWatch logs, compare a deployment
annotation, then inspect a profile. The links are valuable only when identity,
time, service naming, and access controls align across data sources.

## Grafana ecosystem boundaries

- **Grafana:** visualization, exploration, alerting, and correlation experience.
- **Loki:** label-indexed log backend; unbounded labels remain dangerous.
- **Tempo:** distributed-trace backend designed for object-storage economics.
- **Mimir:** horizontally scalable Prometheus-compatible metrics backend.
- **Pyroscope:** continuous-profiling backend and visualization integration.

These are options, not mandatory components. Compare self-managed upstream tools,
Grafana Cloud, and provider-managed services by operational ownership, scale,
tenancy, data residency, integrations, query needs, portability, and total cost.

## Alert ownership

Choose whether rules are evaluated by Prometheus-compatible backends or Grafana
Alerting. Avoid two authorities evaluating equivalent rules unless duplication is
intentional. Version rule ownership, notification policy, silences, inhibition,
no-data/error behavior, and dashboard/runbook links.

Return to the [module overview](index.md) when ready to continue.
