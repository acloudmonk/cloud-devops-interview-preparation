# Enterprise API and Identity Design Exercise

[← Module overview](index.md) · [Scenario questions →](scenarios.md)

## Brief

A regulated B2B platform runs primarily on AWS. Employees use Microsoft Entra ID,
partners bring OIDC or SAML identity, customers use local/social identity, and
services run on EKS and Lambda. The platform exposes order, document, and webhook
APIs to 200 partners. It must isolate tenants, support delegated administration,
avoid static workload secrets, survive identity-provider degradation, and retire
API versions predictably.

## Constraints

- 99.95% critical API objective; authorization adds no more than 40 ms at p95.
- Documents contain regulated data; support access requires approval and evidence.
- Partner systems retry unpredictably and some support only SAML or signed webhooks.
- A compromised partner, tenant admin, workload, or signing key must be containable.
- Azure-hosted analytics and Google Cloud batch workloads need selected APIs.

## Deliverable

Present a ten-minute design covering:

1. consumer journeys, business invariants, data and tenant boundaries;
2. REST/event/webhook choices, contracts, idempotency, versioning, and retirement;
3. edge, gateway, routing, quotas, abuse protection, and service boundaries;
4. workforce, partner, customer, and workload identity flows;
5. token types, issuers, audiences, claims, sessions, and key lifecycle;
6. coarse scopes plus object/tenant authorization and policy ownership;
7. AWS services and accurate Azure/Google Cloud translations;
8. identity, policy, gateway, partner, and Region failure behavior;
9. logs, metrics, traces, audit evidence, privacy, and incident command;
10. migration waves, consumer onboarding, cost, measures, and residual risk.

## Strong direction

Use API Gateway and WAF at the public boundary, Cognito or federated enterprise
identity by population, and workload roles/federation rather than stored keys.
Validate exact issuer/audience/token purpose; enforce tenant/object permissions in
services or Verified Permissions with explicit failure behavior. Use idempotency and
asynchronous boundaries around partner uncertainty, signed replay-resistant webhooks,
and telemetry-led version retirement. Preserve native cross-cloud identity semantics.

## Scoring rubric

| Dimension | 0 | 2 | 4 |
| --- | --- | --- | --- |
| Discovery | product list | some constraints | journeys, invariants, actors, risk, ownership |
| Contract | endpoints only | basic schema/version | semantics, retry, errors, evolution, retirement |
| Identity | “use OAuth” | flows named | populations, token purpose, claims, lifecycle, recovery |
| Authorization | roles only | resource checks | tenant/object/context policy with evidence |
| Security | WAF/MFA list | common controls | end-to-end threats, keys, recovery, containment |
| Operation | dashboards | failure mentioned | SLOs, degraded modes, incident and reconciliation |

Maximum: **24**; aim for **19** before the mock interview.
