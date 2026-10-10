# Ten-Minute Observability Architecture Review

[← Module overview](index.md) · [Design exercise](design-exercise.md)

Use this structure to present an observability recommendation. Lead with customer
outcomes and operational decisions, not signal volume or product inventory.

## 0:00–1:00 — Outcome and current gap

State the critical journey, SLO, recent incident, unanswered questions, response
delay, constraints, and measurable target.

## 1:00–2:00 — Signal contract

Show bounded metrics/labels/histograms, structured events, traces/context/sampling,
profiles, topology, changes, resource identity, ownership, and prohibited data.

## 2:00–4:00 — Collection and backend architecture

Trace application and Prometheus telemetry through OTel/ADOT agents and gateways,
processing, queues, identities, and AWS backends—CloudWatch, X-Ray, AMP, AMG, and
log/search choices. State portability and multi-cloud boundaries.

## 4:00–5:30 — Investigation and response

Demonstrate SLO burn → Grafana segmentation → exemplar/trace → correlated logs
and changes → profile. Explain alert owner, runbook, notification, and safe action.

## 5:30–6:30 — Reliability

Cover application decoupling, collector overload, queues/retries/shedding, backend
and region failure, data loss/duplication, independent health, and recovery proof.

## 6:30–7:30 — Security and cost

Address identity, tenancy, sensitive-data prevention, access/audit, cardinality,
sampling, indexing, retention, query and egress controls, and cost attribution.

## 7:30–9:00 — Migration and ownership

Show one-journey pilot, common semantic and platform contracts, bounded dual run,
agent/backend retirement, training, service/platform/security owners, and exceptions.

## 9:00–10:00 — Measures and decision

Report detection/isolation/mitigation time, SLO coverage, alert quality, trace
completeness, dropped telemetry, query success, adoption, unit cost, and the next
decision or experiment.

Return to the [module overview](index.md) when ready to continue.
