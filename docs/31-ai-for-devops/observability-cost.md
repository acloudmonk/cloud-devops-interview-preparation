# Observability, Cost, and Sustainability

[← Security, safety, and governance](security-governance.md) · [Next: GPU platforms and resilience →](gpu-platforms-resilience.md)

## Observe four dimensions

1. **Service:** requests, errors, throttles, latency percentiles, queue depth.
2. **AI behavior:** model/prompt/version, refusals, quality and safety samples.
3. **RAG/agent path:** retrieval candidates, citations, tool calls, iterations.
4. **Outcome:** completion, acceptance, escalation, rework, harm, business value.

Use trace correlation across gateway, retrieval, model, and tools, but do not expose
hidden reasoning or sensitive content indiscriminately. Store hashes, metadata, or
redacted samples when full payload logging is unnecessary. Define access and
retention separately for operations, evaluation, audit, and analytics.

## Cost model and controls

Include input/output tokens, embeddings, reranking, vector/search storage, model
endpoints or provisioned throughput, GPU idle time, transfer, safety and judge
calls, telemetry, and human review. Report **cost per successful task**.

Controls include task-to-model routing, context budgets, authorization-aware
caching, batching, prompt compression, output limits, bounded agent iterations,
tenant quotas, anomaly budgets, and scheduled endpoints. Caching must define
freshness, authorization, and invalidation.

## Capacity, reliability, and sustainability

Define timeouts, retry budgets, admission control, priority, backpressure,
concurrency, and degraded behavior. Load-test realistic token distributions because
averages hide tail latency. Avoid needless generation, select the smallest adequate
model, batch suitable work, reuse evaluated outputs safely, and monitor utilization;
never reduce safety testing or resilience merely to improve efficiency.
