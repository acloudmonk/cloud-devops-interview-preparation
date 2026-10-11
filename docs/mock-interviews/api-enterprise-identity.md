# APIs and Enterprise Identity Mock Interview

[← Mock interview index](index.md) · [Module 29 overview](../29-api-identity/index.md)

Duration: **50 minutes**
Primary context: **AWS with enterprise federation and multi-cloud workloads**

## Candidate brief

Design a regulated B2B platform exposing order, document, and webhook capabilities
to 200 partners. Employees authenticate with Microsoft Entra ID, customers use a
customer identity service, and workloads span AWS, Azure, and Google Cloud. The
platform needs tenant isolation, delegated administration, predictable lifecycle,
and containment of partner, token, policy, or signing-key compromise.

## Interview structure

### 0–6 minutes — Discovery

Identify journeys, actors, tenants, data, invariants, volumes, latency, availability,
consumer capability, compliance, current state, owners, and unknowns.

### 6–16 minutes — Contract and interaction

Choose REST, events, and webhooks; define idempotency, errors, pagination, versioning,
compatibility, partner onboarding, and retirement. Explain rejected alternatives.

### 16–28 minutes — Identity and authorization

Trace employee, customer, partner, and workload flows. Identify issuers, clients,
audiences, tokens, sessions, provisioning, key lifecycle, tenant/object policy,
delegation, privileged support, and evidence.

### 28–38 minutes — Security and failure branches

Interviewer selects three: cross-tenant access, compromised webhook key, identity
outage, policy latency, signing-key rotation failure, external workload compromise,
or authorization rollback. Contain, recover, reconcile, and prevent recurrence.

### 38–46 minutes — Platform and migration

Map AWS services and accurate Azure/Google translations. Cover gateway, policy,
observability, SLOs, cost, lifecycle governance, migration waves, and adoption.

### 46–50 minutes — Executive close

State recommendation, strongest alternative, accepted trade-off, highest residual
risk, accountable owner, proof required, and candidate questions.

## Scoring rubric

| Dimension | Strong evidence |
| --- | --- |
| Discovery | journeys, actors, invariants, constraints, owners, uncertainty |
| API design | interaction fit, semantics, retries, evolution, retirement |
| Identity | correct protocol/token purpose, federation, lifecycle, recovery |
| Authorization | tenant/object/context enforcement with owned policy and evidence |
| Security | threat paths, keys, privileged control, containment, privacy |
| Reliability | dependency budgets, degraded modes, recovery, reconciliation |
| Cloud architecture | AWS depth with accurate Azure and Google translation |
| Governance | inventory, onboarding, deprecation, exceptions, cost, measures |
| Communication | structured trade-offs, decision, residual risk, next proof |

Score each 0–4. Maximum **36**; 31–36 is strong architect signal, 24–30 is credible
with targeted gaps, and below 24 requires another review cycle. Record evidence,
not confidence or vocabulary alone.
