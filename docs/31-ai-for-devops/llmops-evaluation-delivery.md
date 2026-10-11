# LLMOps, Evaluation, and Delivery

[← RAG, agents, and tool use](rag-agents-tool-use.md) · [Next: AIOps and incident assistance →](aiops-incident-automation.md)

## Version the complete behavior

Track application code, model/provider/version, system and developer prompts,
tool schemas, retrieval configuration, source snapshot, embedding model, safety
policy, and evaluation dataset. A prompt change is a production change.

## Evaluation portfolio

| Layer | Example measures |
| --- | --- |
| Task quality | Correctness, completeness, format, expert acceptance |
| Retrieval | Relevant evidence found, ranking, access-control correctness |
| Agent | Tool selection, argument accuracy, completion, unnecessary steps |
| Safety | Injection resistance, harmful output, leakage, refusal quality |
| Operations | Latency percentiles, errors, throttles, availability, tokens |
| Value | Time saved, successful-task cost, escalation and rework rates |

Build frozen regression cases, recent privacy-reviewed cases, edge cases, and
adversarial cases. Use deterministic assertions where possible, domain reviewers
for consequential quality, and model-as-judge only after calibration against human
labels. Track judge version and disagreement.

## Release path

Run unit and contract tests, offline evaluation, security testing, shadow traffic,
canary or A/B exposure, and continuous sampled evaluation. Define thresholds and
critical zero-tolerance failures before seeing results. Promotion creates an
immutable release manifest and immediate rollback path.

## Drift, feedback, and rollback

Separate model drift, knowledge freshness, retrieval degradation, prompt regression,
tool/API change, and user-population change. Combine task outcomes, sampled expert
review, explicit feedback, and operational signals. Rollback may require reverting
prompt, model, index, embedding, tool, or policy; keep compatible versions. When
risk is uncertain, disable write tools or fall back to search and human escalation.
