# Ten-Minute AI Architecture Review

[← Advanced drills](scenario-drills.md) · [Next: Rapid-fire revision →](rapid-fire.md)

Use this structure for an interview whiteboard or executive review.

## Minute 0–1 — Outcome and boundary

State users, workflow, deterministic baseline, measurable value, prohibited uses,
and why AI is appropriate.

## Minute 1–3 — Data and trust

Show identities, data classifications, source ownership, retrieval entitlements,
freshness, retention, injection boundary, and tenant isolation.

## Minute 3–5 — Runtime path

Walk through gateway, model routing, prompts, RAG, agent tools, validation, approval,
execution, and audit. Separate probabilistic recommendations from authorization.

## Minute 5–7 — Evaluation and delivery

Describe representative and adversarial datasets, thresholds, human calibration,
version manifest, shadow/canary release, rollback, and continuous evaluation.

## Minute 7–9 — Operations and economics

Cover SLOs, traces, quality, safety, quotas, token/GPU cost, successful-task cost,
capacity, degradation, incident response, and ownership.

## Minute 9–10 — Decision and residual risk

Name the selected autonomy tier, cloud/service trade-offs, assumptions, risks that
remain, evidence required for expansion, and the next reversible decision.
