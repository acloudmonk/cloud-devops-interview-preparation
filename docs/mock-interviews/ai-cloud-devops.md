# AI for Cloud and DevOps Mock Interview

[← Mock interview overview](index.md) · [Module overview](../31-ai-for-devops/index.md)

Timebox: **50 minutes**. Answer aloud, draw boundaries, and record assumptions.

## Candidate brief

Design an enterprise operations copilot for a regulated multi-account AWS estate.
It should search authorized runbooks and incident evidence, summarize timelines,
recommend diagnostics, and eventually invoke selected remediation workflows. The
business expects measurable reduction in investigation time without increasing
production risk. Azure and Google Cloud teams may adopt the control model later.

## Interview flow

### 0–8 minutes — Discovery and decision

Clarify users, current workflow and baseline, criticality, prohibited uses, data,
latency, volume, value, acceptable error, and autonomy. Explain why AI is needed
and where deterministic search or automation remains preferable.

### 8–20 minutes — Architecture and data

Design identity, API/gateway, model selection and routing, prompt boundaries, RAG
ingestion, entitlement-aware retrieval, citations, tools, memory, approval, and
audit. Identify every trust boundary and source of state.

### 20–30 minutes — Evaluation and delivery

Define task, retrieval, agent, safety, operational, and value measures. Describe
dataset construction, human calibration, adversarial testing, release manifest,
shadow/canary rollout, stop conditions, and rollback.

### 30–40 minutes — Failure branches

The interviewer selects three:

- a retrieved document contains prompt injection;
- another tenant's runbook appears in an answer;
- a model upgrade changes tool-call behavior;
- token cost triples and latency misses the SLO;
- the provider is unavailable during a major incident;
- an approved remediation succeeds but the agent reports failure and retries;
- sensitive incident data appears in traces;
- self-hosted GPU capacity disappears in one Availability Zone.

### 40–46 minutes — Governance and multi-cloud

Cover system inventory, ownership, NIST AI RMF, supplier/data terms, privacy,
incident response, evidence, retirement, and the capability-based Azure/Google
translation. Explain what should remain provider-native.

### 46–50 minutes — Executive close

State the recommendation, first release boundary, success and stop metrics,
largest residual risks, and evidence required before expanding autonomy.

## Scoring rubric

| Dimension | Points |
| --- | ---: |
| Discovery, outcome, and appropriate AI decision | 8 |
| Data, RAG, identity, and architecture | 10 |
| Agent tools, security, safety, and human control | 10 |
| Evaluation, LLMOps, release, and rollback | 8 |
| Reliability, observability, cost, and GPU reasoning | 7 |
| Governance, multi-cloud trade-offs, and communication | 7 |
| **Total** | **50** |

Interpretation: **43–50** architect-ready; **35–42** strong with targeted gaps;
**25–34** incomplete control/evaluation reasoning; **below 25** rebuild from the
decision model. Any design that permits unrestricted production action or omits
tenant authorization cannot score above 34.

## Improvement loop

Write the three weakest decisions, revisit their primary references, update the
diagram and evaluation matrix, then repeat the interview within seven days using
different failure branches.
