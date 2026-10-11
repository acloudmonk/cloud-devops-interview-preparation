# Rapid-Fire Revision

[← Ten-minute review](presentation-template.md) · [Next: Active-recall flashcards →](flashcards.md)

Answer each in one or two sentences before revealing the text after the dash.

1. **When should deterministic code beat an LLM?** — When rules and outputs must be exact, explainable, repeatable, and cheaply verified.
2. **What is generative AI's central operational risk?** — Plausible but incorrect or unsafe output can vary with context and version.
3. **What is an autonomy ladder?** — A staged progression from search and advice toward increasingly bounded execution.
4. **Why define a baseline?** — It proves whether AI improves the existing workflow rather than merely creating an impressive demo.
5. **What is a model gateway?** — A controlled entry point for identity, routing, policy, quotas, telemetry, and shutdown.
6. **Why pin a model version?** — Reproducible evaluation and rollback require knowing which behavior was released.
7. **What is graceful degradation?** — A visible fallback to search, templates, queues, or humans when AI is unsafe or unavailable.
8. **What is RAG?** — Retrieval of relevant external evidence that is supplied to a model at inference time.
9. **Does RAG guarantee truth?** — No; source, retrieval, authorization, and generation can each fail.
10. **Why evaluate retrieval separately?** — A good generator cannot compensate reliably for absent or unauthorized evidence.
11. **What belongs in retrieval metadata?** — Ownership, tenant, classification, version, geography, freshness, and entitlement attributes.
12. **Where must RAG authorization occur?** — Before retrieved content enters model context, using verified caller entitlements.
13. **What is reranking?** — Reordering retrieved candidates with a second relevance method before context assembly.
14. **What is an agent?** — A control loop that selects tools and steps toward a goal based on observations.
15. **What is excessive agency?** — Giving a model more tools, permissions, scope, or time than the outcome requires.
16. **Why separate read and write tools?** — Their blast radius, approval, credentials, and audit requirements differ.
17. **Can a system prompt enforce IAM?** — No; deterministic authorization must enforce every retrieval and tool call.
18. **What is indirect prompt injection?** — Malicious instructions embedded in data the system retrieves or processes.
19. **What should a tool schema provide?** — Narrow typed arguments, bounded resources, errors, timeout, and idempotency semantics.
20. **Why bound agent iterations?** — To limit loops, latency, resource exhaustion, and denial-of-wallet risk.
21. **What is LLMOps?** — Versioning, evaluating, releasing, observing, governing, and retiring AI application behavior.
22. **What must an AI release manifest contain?** — Code, model, prompts, tools, retrieval/index, policies, and evaluation evidence.
23. **What is a golden dataset?** — A reviewed, versioned set of representative cases and expected properties for regression testing.
24. **Why include adversarial cases?** — Normal success cases do not expose injection, leakage, abuse, or boundary failures.
25. **What is model-as-judge?** — A model scoring another output; it requires human calibration and version tracking.
26. **What is groundedness?** — The degree to which an answer is supported by supplied evidence.
27. **What is citation validity?** — Whether a cited source exists and actually supports the associated claim.
28. **What is continuous evaluation?** — Repeated quality and safety measurement on privacy-controlled production samples.
29. **Why is a prompt change a release?** — It can alter behavior, tool use, safety, latency, and cost without code changes.
30. **What is shadow mode?** — Running the new path without exposing its decisions or actions to users or production state.
31. **Why can fallback be dangerous?** — An untested alternate model may have different safety, format, and tool behavior.
32. **What is automation bias?** — Humans over-trusting automated recommendations even when contrary evidence exists.
33. **What should an incident copilot distinguish?** — Timestamped facts, missing evidence, hypotheses, and proposed actions.
34. **Why preserve raw incident evidence?** — A generated summary can omit, distort, or reorder important facts.
35. **Who owns an AI-generated change?** — The team approving and operating it; generation does not transfer accountability.
36. **What does AI observability add to service telemetry?** — Model/prompt versions, retrieval, tool paths, quality, safety, and outcomes.
37. **Why avoid logging all prompts?** — They may contain secrets, personal data, customer content, or incident details.
38. **What is cost per successful task?** — Total AI, platform, and review cost divided by tasks that achieve the intended outcome.
39. **What drives token cost?** — Context, generated output, retries, agent steps, evaluations, and traffic volume.
40. **What is denial of wallet?** — Abuse or loops that consume metered AI resources and create excessive spend.
41. **Why use the smallest adequate model?** — It can reduce latency, cost, capacity, and environmental impact.
42. **When is self-hosted inference justified?** — When control, customization, data, latency, scale, or economics outweigh operations burden.
43. **What is time to first token?** — Delay before streaming begins; it is distinct from total response latency.
44. **Why scale on queue metrics?** — GPU utilization alone may hide waiting requests and latency pressure.
45. **What does dynamic batching trade?** — Greater throughput and utilization against potential waiting latency.
46. **Why use admission control?** — It protects capacity and priority work instead of allowing overload collapse.
47. **Does Multi-AZ guarantee accelerator capacity?** — No; model quotas and accelerator supply need explicit planning.
48. **What is the NIST AI RMF cycle?** — Govern, Map, Measure, and Manage AI risk.
49. **What makes multi-cloud AI translation credible?** — Preserving control outcomes while documenting native differences and exit cost.
50. **What is the architect's strongest AI answer?** — A bounded outcome with evidence, controls, evaluation, ownership, failure behavior, and trade-offs.
