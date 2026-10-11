# Enterprise AI Operations Copilot Design Exercise

[← GPU platforms and resilience](gpu-platforms-resilience.md) · [Next: Scenario questions →](scenarios.md)

## Brief

A regulated enterprise operates 120 AWS accounts and smaller Azure and Google
Cloud estates. It wants a copilot that answers platform questions, summarizes
incidents, proposes diagnostics, and—with approval—runs a small catalogue of safe
remediations. Runbooks, telemetry, tickets, and ownership data contain mixed
sensitivity. The target is 30% faster evidence collection without increasing
production change incidents.

## Constraints

- employee SSO, tenant/team boundaries, regional data restrictions, and audit;
- runbooks update daily and access revocation must take effect quickly;
- no unrestricted shell, arbitrary query, or organization-wide cloud role;
- 99.9% interface availability; model failure must not block incident response;
- quality, safety, latency, and successful-task cost must be measurable;
- Azure and Google teams need the same control model, not identical services.

## Candidate AWS-first design

Use enterprise federation to authenticate the responder. An API tier authorizes
the incident/team scope and calls a model gateway. The gateway pins approved
Amazon Bedrock models, enforces quotas, redaction, policy, timeouts, and telemetry.
An ingestion pipeline classifies, versions, chunks, and indexes permitted runbooks
and tickets in an authorization-aware knowledge base. Telemetry tools expose
curated read-only queries; remediation tools invoke versioned, parameterized
automation through short-lived roles and approval workflow.

The response separates evidence, hypothesis, and proposed action, with citations
and timestamps. A deterministic policy service validates every tool request. An
immutable audit event records identity, incident, release manifest, evidence,
proposal, approval, action, and verification. Search, dashboards, and runbooks
remain available when AI is disabled.

## Evaluation and rollout

Build a dataset from resolved incidents, access-boundary tests, stale/conflicting
runbooks, injection payloads, and unsafe requests. Gate retrieval authorization,
citation validity, diagnostic usefulness, tool arguments, leakage, latency, and
cost. Roll out in shadow mode, read-only advisory mode, approved low-risk actions,
then selectively expand. Stop on any cross-tenant retrieval or unauthorized action.

## Candidate cloud translation

Map managed model, search/grounding, gateway, identity, policy, telemetry, and
workflow capabilities to Microsoft Foundry/Azure services and Vertex AI/Google
Cloud services. Preserve the same entitlement, evaluation, approval, audit, and
fallback contracts. Document native differences in model availability, regions,
networking, quotas, safety, and data handling.

## Scored deliverable (50 points)

| Area | Points | Strong evidence |
| --- | ---: | --- |
| Outcome and scope | 5 | Baseline, target, users, prohibited uses |
| Data and retrieval | 8 | Provenance, entitlements, freshness, deletion, evaluation |
| Model and agent architecture | 8 | Gateway, routing, bounded tools, explicit state |
| Security and governance | 10 | Threats, identities, policy, privacy, audit, ownership |
| Reliability and operations | 7 | SLOs, quotas, fallback, rollback, incident response |
| Evaluation and delivery | 7 | Dataset, thresholds, adversarial tests, progressive rollout |
| Cost and multi-cloud | 5 | Unit economics, budgets, translation, exit trade-offs |

Score 40+ only when the design contains evidence and controls, not just services.
