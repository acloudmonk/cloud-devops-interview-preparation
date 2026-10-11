# Observability Platform Mock Interview

[← Mock interview overview](index.md) ·
[Module 17 overview](../17-observability/index.md) ·
[Scenario answer framework](../interview-playbook/scenario-answer-framework.md)

Duration: **50 minutes**

Level: **Senior / Architect**

Primary context: **AWS-first platform using OpenTelemetry, Prometheus, and Grafana**

## Candidate brief

A commerce company runs 250 services across EKS, ECS, Lambda, EC2, and on-premises
systems, with smaller Azure and GCP estates. Telemetry is fragmented, CloudWatch
cost doubled, Prometheus labels are inconsistent, traces cover 15% of requests,
and alerts are noisy. A checkout incident took 95 minutes to isolate. Design the
target observability platform and migration.

## Interview structure

### 0–5 minutes — Discovery

Ask about customer journeys, SLOs, architecture, incidents, signals, agents,
backends, owners, volume, cost, privacy, residency, availability, and constraints.

### 5–15 minutes — Signal and decision design

Define the checkout questions, SLIs, metric types/labels/histograms, structured
events, trace spans/propagation/sampling, profiles, resource identity, deployment
context, ownership, and prohibited data.

### 15–25 minutes — Platform architecture

Design Prometheus discovery/scraping/rules/remote write; OTel/ADOT SDKs, agents,
gateways, processing, queues, and exporters; AWS backends; Grafana investigation;
cross-account/cloud identity; tenancy; and alert authority.

### 25–35 minutes — Incident branches

Choose two:

1. A release causes a metric-label cardinality explosion.
2. Tail sampling drops the only traces from failing checkouts.
3. A collector rollout duplicates all telemetry and cost.
4. Grafana dashboards are unavailable during a regional incident.
5. Alert rules fire, but routing sends no notification.

Protect applications, use independent evidence, contain platform impact, restore
decision capability, reconcile loss/duplicates, and prevent recurrence.

### 35–42 minutes — Trade-offs and multi-cloud

Discuss CloudWatch versus Prometheus, head versus tail sampling, agent versus
gateway, central versus local storage, self-managed versus SaaS/managed services,
cost versus evidence, and AWS/Azure/Google Cloud translation.

### 42–47 minutes — Executive recommendation

Summarize the business problem, first journey, target capability, migration waves,
ownership, reliability, privacy, investment, residual risk, and measures in two minutes.

### 47–50 minutes — Candidate questions

Ask about incident history, SLO ownership, privacy/residency, platform team mandate,
cost allocation, on-call health, or the first operational outcome to improve.

## Scoring rubric

| Dimension | Expected evidence |
| --- | --- |
| Discovery and questions | journeys, decisions, incidents, estate, constraints, owners |
| Signal design | metrics, logs/events, traces, profiles, context, semantics |
| Prometheus | discovery, labels, PromQL/rules, alerting, remote storage, scale |
| OpenTelemetry | instrumentation, Collector topology, resilience, governance |
| Grafana and correlation | dashboard hierarchy, exploration, cross-signal workflow |
| SLOs and response | valid SLIs, burn alerts, routing, runbook, alert quality |
| Platform operations | failure, capacity, tenancy, security, privacy, cost, recovery |
| Cloud translation | AWS depth with accurate Azure and Google Cloud outcomes |
| Migration and communication | pilot, retirement, measures, trade-offs, executive clarity |

Score each 0–4. Maximum: **36**. Scores of 31–36 show strong architect signal;
24–30 are credible with gaps; 17–23 need deeper signal and platform reasoning;
below 17 should revisit the concepts and scenarios.

Return to the [module overview](../17-observability/index.md) after scoring.
