# Case 7: AI Operations Copilot

[← Reliability and FinOps](reliability-finops.md) · [Next: Principal architect capstone →](capstone.md)

## Brief

A regulated enterprise wants an AI assistant for 24×7 cloud operations. It should
search runbooks and tickets, correlate telemetry, draft incident updates, and later
run selected remediations. Data spans 120 AWS accounts plus Azure and Google Cloud.
Leadership promises a 40% MTTR reduction in one quarter.

## Discovery prompts

- Which user decisions and workflow delays form the current MTTR baseline?
- What data classifications, entitlements, regions, retention, and provider terms apply?
- May the system search, recommend, draft, approve, or execute—and for which risk tier?
- How are source freshness, citations, quality, safety, latency, and value evaluated?
- What conventional path remains during model failure, quota exhaustion, or distrust?

## Candidate tasks

1. Define bounded use cases, prohibited actions, baseline, and success/harm metrics.
2. Design identity, gateway, model routing, entitlement-aware RAG, tools, and audit.
3. Specify prompt-injection, leakage, excessive-agency, and denial-of-wallet controls.
4. Build offline, adversarial, shadow, canary, and continuous evaluation paths.
5. Explain operations, cost per successful task, multi-cloud mapping, and retirement.

## Failure injects

- A retrieved ticket instructs the agent to ignore policy and reveal credentials.
- A semantic cache returns another team's incident summary.
- The model reports remediation failure after the action actually succeeded.
- A provider model alias changes behavior during an incident.
- Operators approve nearly every proposed action without checking evidence.

## Model direction

Start with read-only evidence retrieval and incident chronology, not autonomous
remediation. Authenticate the responder, authorize retrieval before context, label
facts and hypotheses, and cite timestamped sources. A controlled model gateway pins
approved releases, enforces budgets and redaction, and correlates traces. External
deterministic policy validates every typed tool call; short-lived workload identity,
approval, idempotency, verification, rollback, and audit control execution.

Version code, model, prompts, index, tools, policy, and evaluation data together.
Test retrieval and tenant isolation separately from answer quality; include indirect
injection and timeout-after-success. Roll out through shadow and advisory modes.
Measure time to useful evidence, accepted recommendations, harmful proposals,
override, MTTR, and cost per successful task. Preserve dashboards, search, runbooks,
and incident command when AI is unavailable. Translate control outcomes across
clouds without pretending service features are identical.

## Strong close

Replace the promised percentage with an experiment-backed target. State the initial
autonomy tier, zero-tolerance failures, kill switch, and evidence required before
any write capability is enabled.
