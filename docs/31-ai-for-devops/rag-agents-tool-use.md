# RAG, Agents, and Tool Use

[← Foundation-model architecture](foundation-model-architecture.md) · [Next: LLMOps, evaluation, and delivery →](llmops-evaluation-delivery.md)

## Retrieval-augmented generation

RAG supplies current, private evidence at inference time. Its pipeline includes
source governance, parsing, chunking, metadata, embeddings, indexing, query
transformation, authorization-aware retrieval, reranking, generation, citations,
and evaluation. A vector database is only one component.

Measure retrieval separately with relevance and recall/precision-style metrics;
then measure answer groundedness, completeness, and citation validity. No answer is
better than a confident answer based on missing or unauthorized evidence. Preserve
source version and timestamp.

## Permissions and tenancy

Filter with the caller's entitlement before content reaches the model. Do not ask
the model to remove forbidden passages after retrieval. Carry tenant, document,
classification, geography, and freshness metadata through ingestion and query.
Test revocation and deletion propagation as first-class requirements.

## Agent control loop

An agent plans, selects a tool, supplies arguments, observes the result, and
continues until a stop condition. Every tool needs a narrow schema, workload
identity, resource scope, timeout, rate limit, idempotency behavior, and auditable
result. Separate read tools from write tools and use short-lived credentials.

AWS currently offers Bedrock AgentCore capabilities for production agent systems;
managed knowledge bases can simplify retrieval. Azure and Google provide analogous
agent and grounding platforms. Keep orchestration contracts portable when useful.

## Prompt injection and confused deputies

Retrieved pages, logs, tickets, and tool output are untrusted. Delimit content,
minimize tools, validate arguments against policy, require approval for consequential
actions, and never expose secrets to the prompt. A system prompt cannot enforce
IAM; the executor must re-authorize every action.

## Memory

Conversation history, durable user preference, and operational state have different
retention and authority. Make memory explicit, scoped, inspectable, correctable,
and deletable. Never let remembered text silently become a production instruction.
