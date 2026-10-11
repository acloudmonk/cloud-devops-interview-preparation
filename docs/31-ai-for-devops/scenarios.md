# Scenario Questions and Model Answers

[← Enterprise design exercise](design-exercise.md) · [Next: Advanced drills →](scenario-drills.md)

Answer aloud using outcome, evidence, architecture, trust, failure, operation, and
trade-offs before reading the model answer.

## 1. The CIO asks for an autonomous incident-remediation agent

**Model answer:** I would separate evidence collection, recommendation, approval,
and execution. Start read-only with cited telemetry and runbooks, measure diagnostic
value, then permit only parameterized, reversible runbooks through narrow roles.
Deterministic policy re-authorizes every action; high-impact changes retain human
approval, rate limits, verification, rollback, and a kill switch.

## 2. A team wants the largest model for every request

**Model answer:** I would benchmark representative tasks across quality, safety,
latency, throughput, and successful-task cost. Route extraction and classification
to smaller adequate models and reserve larger models for complex synthesis. Pin and
evaluate each route; price alone or a public leaderboard is insufficient.

## 3. The runbook assistant cites obsolete guidance

**Model answer:** I would inspect source ownership, ingestion lag, version metadata,
chunking, ranking, and cache invalidation. Responses must show source version and
date. Establish freshness SLOs, exclude superseded documents, regression-test known
queries, and fall back to search or abstention until the index is trustworthy.

## 4. RAG returns another business unit's document

**Model answer:** Treat it as a security incident, stop retrieval, preserve evidence,
and assess disclosure. Entitlement filters must run before model context assembly,
using the caller's verified identity and document metadata. Test revocation,
cross-tenant probes, caching, and index replicas; never rely on the model to redact.

## 5. An injected ticket tells the agent to reveal secrets

**Model answer:** Tickets are untrusted data, not instructions. The model should not
receive secrets, and tools must use scoped identities. Delimit content, restrict
tools, validate calls against external policy, test indirect injection, and require
approval for consequential actions. A stronger system prompt is not the security fix.

## 6. A model upgrade improves benchmarks but users complain

**Model answer:** Compare the frozen suite with recent task and cohort outcomes,
latency, refusals, formatting, retrieval, and tool behavior. Inspect selection bias
in the benchmark and feedback. Pause rollout, canary the old version, conduct blind
domain review, and promote only against predeclared task and harm thresholds.

## 7. Model-as-judge reports near-perfect quality

**Model answer:** A judge is another fallible model and may share bias with the
candidate. Calibrate it against blinded expert labels, track agreement by failure
class, use deterministic checks for citations and schemas, version the judge, and
retain human review for consequential or disputed cases.

## 8. Token spend triples after adding an agent

**Model answer:** Trace iterations, prompt size, retrieval volume, retries, tool
loops, and judge calls. Add step and token budgets, loop detection, context pruning,
task routing, caching with authorization, and per-tenant quotas. Optimize cost per
successful task; terminate paths that cannot make progress.

## 9. The model provider is unavailable during an incident

**Model answer:** AI cannot be on the critical path for incident command. Time out
quickly and preserve dashboards, search, alerts, and runbooks. An independently
evaluated fallback model may serve low-risk assistance; otherwise degrade visibly
to retrieval and human workflow rather than silently changing behavior.

## 10. Developers paste production logs into a public assistant

**Model answer:** Contain exposure, determine data classes and provider handling,
rotate leaked credentials, and follow incident obligations. Provide an approved
gateway with SSO, DLP/redaction, logging policy, contracts, and education. Block or
restrict unsanctioned paths proportionately and make the safe path usable.

## 11. An AI-generated Terraform change passes syntax checks

**Model answer:** Generated code follows the same or stronger path as human code:
review, IaC analysis, policy, plan inspection, tests, provenance, and progressive
apply. Validate against intent and state, not syntax. The model has no direct
credentials, and the normal deployment system owns approval, execution, and rollback.

## 12. A global team requests multi-cloud model portability

**Model answer:** Define task, data, evaluation, identity, and telemetry contracts,
then record a capability matrix for AWS, Azure, and Google. Avoid hiding native
safety and grounding benefits. Quantify exit cost versus abstraction complexity;
portability is justified by business risk, not assumed equivalence.

## 13. Self-hosted inference has poor tail latency

**Model answer:** Correlate queue time, input/output length, batching, accelerator
memory, utilization, cold loading, and downstream tools. Use admission control,
bounded concurrency, workload separation, appropriate batching, load shedding, and
capacity tests with real token distributions. Scale on queue and service metrics,
not GPU utilization alone.

## 14. Leadership asks whether the copilot is compliant

**Model answer:** I would not give a binary claim from the architecture alone.
Map applicable obligations to inventory, purpose, data lineage, risk assessment,
evaluation evidence, access, audit, supplier terms, human oversight, incident
process, and retirement. Compliance and legal owners validate evidence for the
specific jurisdiction and use.

## 15. Operators accept almost every proposed action

**Model answer:** High acceptance may indicate value or automation bias. Sample
decisions for independent review, compare outcomes and near misses, show evidence
and alternatives, and test whether reviewers detect planted unsafe proposals.
Risk-tier approvals, separation of duties, and periodic re-authorization prevent
the human checkpoint becoming ceremonial.
