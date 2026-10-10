# CI/CD Active-Recall Flashcards

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Use each prompt without viewing the cue. Explain the invariant, failure mode, and
one design choice that depends on context.

| Prompt | Answer cue |
| --- | --- |
| CI versus delivery | integrate/verify frequently versus keep a releasable artifact ready |
| Deployment versus exposure | install capability versus decide which users receive it |
| Control/execution planes | trusted decision logic versus workers/tools/networks doing work |
| Build once | promote the same immutable digest and accumulate evidence |
| Green limit | configured execution succeeded; relevance, trust, and customer correctness remain questions |
| Gate design | purpose, evidence, threshold, owner, failure behavior, expiry |
| Flaky failure | preserve signal; classify, own, fix or visibly time-bound quarantine |
| Artifact identity | digest is immutable identity; tag is a mutable name |
| Cache boundary | optimization, trust-partitioned and disposable—not promotion evidence |
| Provenance boundary | claims about origin/process rely on authorized uncompromised builder and policy |
| OIDC to AWS | short-lived token claims constrained by IAM trust policy and role permissions |
| Workflow token | read-only default; grant minimum per job |
| Fork execution | isolated ephemeral, no privileged token/secret/network/cache |
| Third-party action | immutable pin plus review, approved catalog, monitoring, and update process |
| Runner isolation | separate trust levels; prefer disposable workers and bounded network/identity |
| Rolling | controlled replacement with old/new compatibility |
| Blue/green | parallel environment, traffic switch, spare capacity, fast fallback |
| Canary | representative cohort, baseline, signals, window, promotion/abort owner |
| Feature-flag debt | owner, safe default, telemetry, security, outage behavior, removal date |
| Expand–migrate–contract | compatible addition, bounded movement, observed retirement, later removal |
| Rollback decision | validate artifact, schema, data, config, messages, and external effects |
| Retry safety | inspect partial state; idempotency key, bounds, backoff, reconciliation |
| Stale-run control | environment concurrency plus monotonic version/digest guard |
| Pipeline SLOs | queue/lead time and reliability segmented by workflow/team/trust level |
| Executive recommendation | context, risk, invariant-based design, adoption, measures, decision owner |

Review missed cards after one day, three days, and seven days.
