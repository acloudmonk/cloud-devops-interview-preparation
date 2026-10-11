# Observability Rapid-Fire Revision

[← Module overview](index.md) · [Active-recall flashcards](flashcards.md)

Answer each in one or two sentences, then add a failure mode or trade-off.

1. **Observability?** Ability to ask useful questions about a running system from its outputs.
2. **Monitoring?** Evaluation of known conditions to detect and communicate expected failure modes.
3. **Telemetry?** Signals and context emitted or collected from a system.
4. **Why not collect everything?** Cost, noise, privacy, risk, and query complexity grow without guaranteed decision value.
5. **Four common signals?** Metrics, logs/events, traces, and profiles; changes/topology add crucial context.
6. **RED?** Request rate, errors, and duration for request-driven services.
7. **USE?** Utilization, saturation, and errors for resources.
8. **Counter?** Cumulative monotonic event total, normally queried with rate or increase.
9. **Gauge?** Current value that can rise and fall.
10. **Histogram?** Bucketed distribution with count and sum, suitable for aggregation and SLO thresholds.
11. **Summary limitation?** Client-side quantiles generally cannot aggregate meaningfully across instances.
12. **Prometheus series identity?** Metric name plus the complete label set.
13. **Cardinality risk?** Series count grows with combinations of label values and target replicas.
14. **Unsafe metric labels?** Request ID, user ID, email, raw URL, timestamp, and free-form error.
15. **What is churn?** Rapid creation and disappearance of time series, increasing ingestion and memory pressure.
16. **Recording rule?** Scheduled precomputation that stores a PromQL result as a new series.
17. **What does `up` show?** Whether Prometheus successfully scraped a target, not whether the service works for users.
18. **Remote write?** Protocol/path for sending samples to a compatible remote receiver or long-term store.
19. **Alertmanager role?** Group, route, inhibit, silence, and notify for Prometheus alerts.
20. **Structured log?** Event with stable named fields and semantics, not merely JSON formatting.
21. **Audit versus diagnostic log?** Audit evidence requires stronger completeness, immutability, access, and retention guarantees.
22. **Trace?** Causal representation of a distributed request or transaction made of spans.
23. **Span?** Timed operation with identity, relationships, attributes, status, and events.
24. **Context propagation?** Carrying trace and related context across process/service boundaries.
25. **Baggage risk?** It propagates application context and can leak sensitive data or increase request size.
26. **Head sampling?** Sampling decision near trace start—cheap but unaware of final outcome.
27. **Tail sampling?** Decision after observing spans—outcome-aware but stateful and operationally expensive.
28. **Exemplar?** Reference from a metric observation to representative detailed evidence such as a trace.
29. **Profile?** Statistical code-level view of CPU, allocation, memory, lock, or wall-time use.
30. **OpenTelemetry is what?** APIs, SDKs, semantics, context, protocol, and collection—not an observability backend.
31. **OTLP?** OpenTelemetry Protocol for moving telemetry between components.
32. **Semantic conventions?** Shared names and meanings for resources, operations, and attributes.
33. **Collector receiver?** Component that accepts or obtains telemetry.
34. **Collector processor?** Component that batches, filters, transforms, samples, enriches, or limits telemetry.
35. **Collector exporter?** Component that sends telemetry to another collector or backend.
36. **Agent versus gateway?** Agent is local and distributes load; gateway centralizes policy but becomes shared infrastructure.
37. **Memory limiter purpose?** Refuse/shed telemetry before the collector exhausts memory; it does not add capacity.
38. **Grafana role?** Query, visualize, explore, correlate, and alert across data sources.
39. **Loki?** Log backend indexing labels/metadata rather than every log field.
40. **Tempo?** Distributed-trace backend designed around object-storage scale/economics.
41. **SLI?** Quantitative measure of a service behavior that matters to users.
42. **SLO?** Target value/range for an SLI over a defined window.
43. **Error budget?** Allowed unreliability: one minus the SLO target for ratio objectives.
44. **Burn rate?** Observed bad-event rate divided by the SLO's allowed bad-event rate.
45. **Why multi-window alerts?** Combine urgency with persistence to reduce noise while detecting rapid budget loss.
46. **Page criterion?** Urgent, actionable risk requiring immediate human judgment.
47. **Telemetry platform golden signals?** Ingest success/drop/lag, queue pressure, storage, query/rule latency/errors, and notification delivery.
48. **First cost controls?** Cardinality, duplicate collection, sampling, indexed fields, retention tiers, query range, and egress.
49. **AWS managed Prometheus/Grafana?** AMP and AMG; ADOT provides AWS-supported OTel distribution/integration.
50. **Best architecture question?** Which decision will this signal enable, and what happens when the signal or pipeline fails?

Return to the [module overview](index.md) when ready to continue.
