# AI for Cloud and DevOps

[← Curriculum overview](../curriculum/index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-11**
Level: **Senior / Architect**

AI can shorten diagnosis and delivery, but probabilistic output must never become
unbounded production authority. This module covers AI-assisted operations and the
platform engineering needed to run generative-AI systems safely.

!!! tip "Where to start"
    Start with **1. AI systems decision model** and follow the numbered path. AWS
    is the architecture anchor; Azure and Google Cloud equivalents are compared.
    The path is documentation- and scenario-focused, with no deployment lab.

## Learning objectives

- distinguish deterministic automation, predictive ML, generative AI, and agents;
- select bounded use cases using value, risk, evidence, and reversibility;
- design model gateways, RAG, tools, memory, and human approval boundaries;
- evaluate quality, safety, retrieval, tool use, latency, and cost before release;
- operate prompts, models, datasets, policies, and evaluations as versioned assets;
- apply least privilege, data controls, prompt-injection defenses, and auditability;
- use AI for incident and change assistance without weakening accountability;
- architect observable, resilient, cost-aware CPU/GPU inference platforms;
- translate AWS-first decisions to Azure and Google Cloud without false parity.

## Recommended module path

### Phase 1 — Learn the AI system

| Step | Page | Outcome |
| ---: | --- | --- |
| 1 | [AI systems decision model](concepts.md) | Connect outcome, evidence, autonomy, risk, and recovery |
| 2 | [Use cases and operating model](use-cases-operating-model.md) | Prioritize assistive use cases and establish ownership |
| 3 | [Foundation-model architecture](foundation-model-architecture.md) | Select models, gateways, routing, context, and deployment patterns |
| 4 | [RAG, agents, and tool use](rag-agents-tool-use.md) | Ground answers and constrain actions across trust boundaries |
| 5 | [LLMOps, evaluation, and delivery](llmops-evaluation-delivery.md) | Version, test, release, observe, and roll back AI behavior |
| 6 | [AIOps and incident assistance](aiops-incident-automation.md) | Apply AI safely to signals, diagnosis, change, and remediation |
| 7 | [Security, safety, and governance](security-governance.md) | Control data, identity, injection, supply chain, and accountability |
| 8 | [Observability, cost, and sustainability](observability-cost.md) | Measure service health, quality, tokens, value, and spend |
| 9 | [GPU platforms and resilience](gpu-platforms-resilience.md) | Reason about capacity, scheduling, inference, failure, and portability |

### Phase 2 — Apply the reasoning

| Step | Page | Outcome |
| ---: | --- | --- |
| 10 | [Enterprise design exercise](design-exercise.md) | Design a governed AWS-first operations copilot |
| 11 | [Scenario questions and model answers](scenarios.md) | Practise at least 15 senior AI/DevOps scenarios |
| 12 | [Advanced architecture and incident drills](scenario-drills.md) | Resolve at least 10 ambiguous failures and trade-offs |
| 13 | [Ten-minute architecture review](presentation-template.md) | Present value, trust, evaluation, operation, and residual risk |

### Phase 3 — Revise and assess

| Step | Page | Outcome |
| ---: | --- | --- |
| 14 | [Rapid-fire revision](rapid-fire.md) | Test at least 50 concise explanations |
| 15 | [Active-recall flashcards](flashcards.md) | Revisit at least 25 weak concepts |
| 16 | [Timed AI for Cloud and DevOps mock interview](../mock-interviews/ai-cloud-devops.md) | Complete a scored 50-minute assessment |
| 17 | [References and videos](references.md) | Deepen weak areas with primary sources |

## Scope boundary

This is not a data-science or model-training course. It focuses on architecture,
delivery, operations, governance, and interviews. Module 17 supplies observability,
Module 18 reliability practice, Module 29 API and identity boundaries, and Module
30 safe automation. AI augments those disciplines; it does not replace them.

## Completion checklist

- [ ] I can reject an AI use case when deterministic automation is safer.
- [ ] I can define autonomy, approval, data, evaluation, and rollback boundaries.
- [ ] I can explain model, RAG, agent, gateway, and GPU platform trade-offs.
- [ ] I can test quality and safety with representative and adversarial datasets.
- [ ] I can observe model behavior, retrieval, tools, latency, cost, and outcomes.
- [ ] I answered all 25 scenarios aloud and completed the scored mock interview.
