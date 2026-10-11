# AIOps and Incident Assistance

[← LLMOps, evaluation, and delivery](llmops-evaluation-delivery.md) · [Next: Security, safety, and governance →](security-governance.md)

## Where AI helps

Classical techniques can group alerts, detect anomalies, forecast capacity, and
identify correlations. Generative AI can retrieve runbooks, summarize evidence,
construct timelines, translate queries, explain hypotheses, and draft
communications. Neither establishes causality without evidence.

## Safe incident-assistant flow

1. Authenticate the responder and incident scope.
2. Retrieve authorized telemetry, topology, changes, tickets, and runbooks.
3. Cite timestamps and sources; distinguish facts from hypotheses.
4. Propose diagnostic queries before remediation.
5. Validate commands and parameters through deterministic policy.
6. Require approval for state change and execute with a bounded role.
7. Record request, evidence, recommendation, approver, action, and result.

An LLM must not receive unrestricted shell, cluster-admin, or organization-wide
cloud credentials. Prefer curated read APIs and parameterized runbooks. Automation
owns execution semantics, idempotency, verification, and rollback.

## Change and delivery assistance

AI can summarize pull requests, identify missing tests, draft IaC, or explain policy
failures. Treat output as untrusted contribution: normal review, analysis, tests,
policy, provenance, and deployment controls still apply.

## Failure modes and measures

Alert storms can overflow context; stale topology creates bad advice; sensitive
logs may leak; confident summaries may omit counter-evidence; and throttling can
fail during the incident peak. Maintain conventional dashboards and runbooks. Track
accepted recommendations, time to evidence, false proposals, operator override,
repeated queries, recovery time, and cost per incident.
