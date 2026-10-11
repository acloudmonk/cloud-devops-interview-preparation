# Advanced Architecture and Incident Drills

[← Scenario questions](scenarios.md) · [Next: Ten-minute review →](presentation-template.md)

For each drill, state immediate containment, evidence, likely failure classes,
durable correction, validation, and residual risk.

## Drill 1 — Cross-tenant answer after a cache change

Disable the affected route and preserve request, identity, cache-key, retrieval,
and release evidence without spreading sensitive content. Investigate whether the
cache omitted tenant, entitlement, model, prompt, or source version. Purge affected
entries, assess disclosure, and notify through the incident process. Fix with
authorization-aware keys or no shared semantic cache, negative cross-tenant tests,
short retention, and a canary that proves revocation behavior.

## Drill 2 — Agent repeatedly invokes a costly diagnostic

Stop the execution and revoke or throttle the tool session. Correlate plan steps,
tool results, retry semantics, timeouts, and termination logic. Add per-task call,
token, time, and money budgets; idempotency; loop detection; backoff; and a terminal
state for no progress. Replay the trace in evaluation and prove that partial
failure cannot restart an expensive or mutating action invisibly.

## Drill 3 — A provider changes a model behind an alias

Freeze rollout and compare current behavior with the recorded release manifest and
baseline dataset. Pin supported versions where possible or treat provider alias
change as an external release event. Maintain contract probes, quality/safety
canaries, alerts, and evaluated fallback. Supplier monitoring does not replace
application-level evaluation because identical APIs can produce different behavior.

## Drill 4 — Retrieval quality falls after a new parser

Separate ingestion completeness, document structure, chunking, metadata, embedding,
ranking, and generation. Compare index versions on a ground-truth retrieval set and
inspect failures by document type. Roll back the parser/index pair, quarantine bad
documents, and add parsing fixtures, ingestion reconciliation, source counts, and
retrieval gates before activating future indexes.

## Drill 5 — Incident summaries omit contradictory evidence

Do not optimize only for fluent summaries. Require timestamped citations, display
important raw evidence, and label facts, uncertainty, and hypotheses. Add cases
with conflicting signals to evaluation; score coverage and contradiction handling
with domain reviewers. Preserve incident command and decision logs so the summary
cannot become the sole record or silently declare root cause.

## Drill 6 — Safety filters block legitimate operations terms

Characterize false positives by user, language, workflow, and policy category.
Do not simply disable all filtering. Layer domain-specific evaluation, narrowly
scoped policy exceptions, input/output handling, audit, and escalation. Test that
the exception does not enable injection, harmful tool calls, or cross-tenant data;
monitor both blocked legitimate tasks and escaped unsafe responses.

## Drill 7 — GPU node loss causes a retry storm

Shed load, cap retries, protect priority traffic, and drain failed capacity.
Inspect queue age, replica readiness, batching, timeouts, and client amplification.
Use admission control, retry budgets, jitter, circuit breaking, evaluated degraded
models, and capacity across failure domains. Validate with zone/node disruption and
realistic token-length load, including recovery without synchronized retry bursts.

## Drill 8 — Sensitive prompts appear in telemetry

Restrict access, stop the logging path, preserve audit evidence, and execute privacy
and credential response. Identify SDK, gateway, trace, and vendor retention copies.
Replace full content with classified metadata, hashes, or sampled redacted payloads;
separate operational and evaluation stores. Test deletion and access boundaries,
then document the remaining diagnostic trade-off.

## Drill 9 — Copilot recommendations increase recovery time

Compare incidents with and without assistance, segment by severity and team, and
inspect time-to-first-evidence, repeated queries, overrides, and bad hypotheses.
Return the tool to shadow or limited advisory mode. Improve source freshness,
presentation, and task scope; train responders on limitations. Re-expand only when
a controlled evaluation shows improved decisions, not merely positive sentiment.

## Drill 10 — Business demands autonomous remediation by Friday

State that calendar pressure does not remove production accountability. Offer a
phased outcome: cited read-only diagnosis, then dry-run proposals, then approved
execution of one reversible runbook. Define success and stop conditions, narrow
identity and resources, deterministic validation, audit, verification, rollback,
and on-call ownership. Record deferred risks and refuse broad arbitrary execution
until evidence supports a higher autonomy tier.
