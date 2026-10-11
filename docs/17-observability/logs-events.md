# Logs and Events

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Logs and events record discrete facts. Useful records have a stable schema,
consistent meaning, trustworthy time, correlation context, and an owner. Free-text
messages remain valuable for humans, but should not be the only query interface.

## Event contract

Capture timestamp, event name, severity, service/resource identity, environment,
version, region/zone, outcome, stable error class, request/trace correlation,
relevant business key in privacy-safe form, and schema version. State whether the
event represents intent, acceptance, completion, failure, retry, or compensation.

Avoid secrets, credentials, tokens, full request/response bodies, and unnecessary
personal data. Redaction at the collector is a safety net; prevention at the
producer is safer because sensitive data may already have crossed a boundary.

## Severity and ownership

Severity expresses the event's nature, not whether someone should be paged. A
single request error may be `ERROR` without requiring an alert; a missing heartbeat
may create user impact without any application error log. Define field and severity
semantics centrally, then let service owners add domain context.

## Pipeline choices

Application writes to standard output, a local agent/daemon tails or receives it,
collectors parse/enrich/filter/batch, and a backend indexes selected fields while
retaining the record under policy. Alternatives include direct OTLP log export,
managed service integrations, and audit pipelines. Do not couple application
availability to a remote logging endpoint.

## Indexing and cost

Index fields used for filtering, routing, joining, and compliance; store rarely
queried content in cheaper tiers. High-cardinality indexing, verbose debug logs,
duplicated ingestion, long hot retention, and uncontrolled tenant queries dominate
cost. Sampling may fit repetitive debug events but must preserve security, audit,
rare-error, and incident evidence.

## Correlation

Propagate trace/span IDs and stable resource identity into logs, but do not assume
all records will have a trace. Correlate deployments, configuration, feature flags,
and infrastructure events on a shared time line. Synchronize time and record
ingestion delay so responders do not mistake late arrival for causality.

## Audit versus diagnostic logs

Audit evidence needs stronger completeness, immutability, access control,
retention, and subject/action/resource semantics than ordinary diagnostic logs.
Separate policy and storage where required; a developer-friendly search cluster is
not automatically an authoritative audit trail.

Return to the [module overview](index.md) when ready to continue.
