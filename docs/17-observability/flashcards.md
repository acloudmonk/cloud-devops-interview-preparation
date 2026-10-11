# Observability Active-Recall Flashcards

[← Module overview](index.md) · [Rapid-fire revision](rapid-fire.md)

Use these cards without looking at the answer. Mark a card weak if you cannot add
one failure mode and one cost or reliability trade-off.

| Front | Back |
| --- | --- |
| Observability decision chain | Outcome → question → signal/context → pipeline → experience → decision/action → feedback. |
| Monitoring versus observability | Monitoring checks known conditions; observability supports investigation of known and unanticipated questions. |
| Metric type choice | Counter for cumulative events, gauge for current state, histogram for aggregatable distributions. |
| Series cardinality estimate | Product of distinct label combinations × targets/replicas; account for churn and future growth. |
| Metric detail boundary | Bounded dimensions in metrics; per-request or high-cardinality detail in logs/traces. |
| Prometheus rule split | Recording rules precompute series; alert rules create alert state; Alertmanager routes/notifies. |
| Useful log contract | Time, event, service/resource, environment/version, outcome/error class, correlation, schema, owner. |
| Trace completeness prerequisites | Instrumentation, propagation, stable resource identity, sampling, export, backend ingest, and correct query. |
| Head versus tail sampling | Head is predictable/cheap but outcome-blind; tail keeps valuable outcomes but needs trace state/affinity/capacity. |
| Exemplar value | Moves from an aggregate metric observation to representative detailed trace evidence. |
| OpenTelemetry boundary | Vendor-neutral generation, semantics, context, protocol, and collection—not storage, query, or dashboards. |
| Collector pipeline | Receivers → processors → exporters; connectors can bridge pipelines and extensions add supporting functions. |
| Safe exporter failure | Application continues; bounded queue/retry absorbs briefly, then value-aware shedding with visible loss. |
| Agent plus gateway | Agent provides local offload/context; gateway provides centralized routing/policy at added shared complexity. |
| Dashboard hierarchy | User/service health → service RED → resource USE → dependencies → investigation detail. |
| SLI contract | Population, good/valid event, measurement point, window, source, delay, exclusions, and owner. |
| Error-budget formula | Allowed bad fraction = 1 − SLO target; consumed relative rate is burn rate. |
| High-quality page | Urgent, actionable user/system risk with owner, impact, evidence, runbook, and tested delivery. |
| AWS observability anchors | ADOT/OTel, CloudWatch, X-Ray, AMP, AMG, OpenSearch where justified, plus change/audit events. |
| Cross-cloud portability | Common instrumentation and semantics, with provider-native identity, resources, backends, and failure behavior. |
| Telemetry security priority | Prevent sensitive collection, isolate tenants, least privilege, encrypt, audit access, govern retention/deletion. |
| Cost allocation dimensions | Service/team/tenant × signal × ingest/storage/query/egress; optimize value rather than volume alone. |
| Missing telemetry workflow | Producer → collection → transport/backend → query → correlation → mitigation/recovery verification. |
| Platform health evidence | Accepted/refused/dropped, queue/retry age, ingest delay, query/rule health, notification, storage, and cost. |
| Strong design closing test | State questions answered, evidence quality, ownership, failure behavior, unit cost, and measurable incident improvement. |

Return to the [module overview](index.md) when ready to continue.
