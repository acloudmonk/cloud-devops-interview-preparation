# Foundation-Model Architecture

[← Use cases and operating model](use-cases-operating-model.md) · [Next: RAG, agents, and tool use →](rag-agents-tool-use.md)

## Architectural layers

A production path commonly contains client authentication, API/WAF controls, an
application service, a model gateway, policy and redaction, prompt assembly,
retrieval or tools, the model endpoint, output validation, telemetry, and feedback.
Keep business authorization outside the model.

## Model selection

Evaluate models on the real task, not public leaderboards alone. Consider quality,
context length, structured-output and tool support, latency, throughput, regional
availability, data terms, safety, price, and portability. Smaller models often win
for classification, extraction, and high-volume constrained tasks.

AWS-first choices include Amazon Bedrock for managed model access and Amazon
SageMaker AI when deeper training, hosting, or ML lifecycle control is required.
Translate the capability—not the name—to Microsoft Foundry/Azure Machine Learning
or Google Vertex AI. Verify current models, Regions, quotas, and data terms.

## Gateway and routing

Centralize authentication, approved model/version aliases, quotas, tenant budgets,
timeouts, retry policy, safety checks, telemetry, and emergency disablement. Route
by task and policy, not merely cheapest token. Retries require bounded backoff and
budgets; a retry can duplicate tool calls or multiply spend.

## Context and state

Separate immutable system policy, developer instructions, user content, retrieved
content, tool results, and conversation history. Treat all external text as data,
never authority. Limit context by relevance and sensitivity; more context can
increase cost, latency, distraction, and disclosure risk.

## Deployment and fallback

Pin a tested model identifier or controlled alias. Canary changes against frozen
and recent evaluation sets. Fallbacks must be independently evaluated. Prefer
graceful degradation—search results, templates, or human routing—over invisible
quality loss.
