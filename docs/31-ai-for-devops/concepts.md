# AI Systems Decision Model

[← Module overview](index.md) · [Next: Use cases and operating model →](use-cases-operating-model.md)

## Start with the decision, not the model

An architect should describe an AI system as **outcome → evidence → model → context
→ tools → controls → feedback**, not as a chatbot. The model is one fallible
component inside a deterministic control plane.

| Approach | Best fit | Main limitation |
| --- | --- | --- |
| Rules or code | Known logic, exact output, auditable changes | Brittle for ambiguous language |
| Classical ML | Classification, forecasting, anomaly scores | Needs representative data and drift control |
| Generative model | Summarization, explanation, synthesis | Non-deterministic and may fabricate |
| Retrieval-augmented generation | Answers grounded in changing private sources | Retrieval and authorization can fail |
| Agent with tools | Multi-step discovery or action | Expands authority and failure paths |

Prefer the least complex approach that meets the outcome. A language model should
not calculate a billing total, decide IAM policy, or execute a destructive runbook
when deterministic logic can do so reliably.

## Seven architecture questions

1. **Outcome:** what measurable decision or task improves?
2. **Evidence:** which data proves correctness and business value?
3. **Uncertainty:** what errors are acceptable, detectable, and reversible?
4. **Authority:** may the system advise, propose, approve, or execute?
5. **Context:** which trusted sources, freshness, and user permissions apply?
6. **Control:** where do policy, validation, budgets, and humans intervene?
7. **Recovery:** how are versions pinned, actions stopped, and changes reversed?

## Autonomy ladder

Move upward only with evidence: **search → summarize → recommend → draft action →
approved execution → bounded autonomous execution**. Each step requires stronger
evaluation, identity, observability, rate limits, and recovery. Confidence text
from a model is not calibrated proof.

## Shared responsibility

The provider secures managed infrastructure and documents service behavior. The
customer remains responsible for use-case suitability, prompts, retrieved data,
access control, tool permissions, evaluation, output handling, and operator action.

## Interview signal

A strong answer states the baseline, success and harm metrics, trust boundaries,
human role, failure behavior, and exit plan before naming AWS services.
