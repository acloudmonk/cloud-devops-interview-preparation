# Microservices Architecture Mock Interview

[← Mock interview overview](index.md) · [Module 20 overview](../20-microservices/index.md)

Duration: **50 minutes**
Level: **Senior / Architect**
Primary context: **AWS-first global commerce platform with multi-cloud dependencies**

## Candidate brief

A retailer's catalogue, inventory, order, payment, shipping, and notification logic
runs in a modular monolith released weekly by 14 teams. Peak traffic is 50 times
normal, payment timeouts caused duplicate charges, and database changes blocked
checkout. Leadership requests microservices within nine months. Design the target
and an evidence-led migration.

## Interview structure

### 0–7 minutes — Discovery and architecture decision

Clarify business outcomes, domain workflows, invariants, demand, latency, SLO,
RTO/RPO, consistency, team ownership, current change pain, skills, and constraints.
Compare remaining modular with selective or broad decomposition.

### 7–18 minutes — Boundaries, communication, and data

Define bounded contexts, service/team/data ownership, sync versus async contracts,
gateway/discovery, versioning, order workflow, saga/outbox, idempotency, derived
reads, compensation, and reconciliation.

### 18–28 minutes — Security, resilience, and delivery

Cover user/workload/tenant identity, authorization, secrets, deadlines, retries,
overload, isolation, capacity, supply chain, contract testing, schema overlap,
progressive delivery, and rollback.

### 28–38 minutes — Failure branches

Choose three:

- payment times out after accepting a charge;
- the outbox backlog grows for forty minutes;
- an event change breaks a lagging consumer;
- retries amplify an identity-provider brownout;
- one service restore creates inconsistent business state;
- a shared IAM role is compromised;
- service discovery targets terminating instances;
- the regional coordinator fails midway through a saga.

### 38–45 minutes — Operations and migration

Define journey/service SLOs, telemetry, catalog, on-call, recovery, cost, team
topology, platform needs, strangler waves, data-authority transfer, rollback, and
retirement. Translate Azure identity and Google analytics dependencies safely.

### 45–50 minutes — Executive close

State the recommended boundary, first extraction, benefits, distributed costs,
nine-month sequence, residual risks, and evidence that could change the plan.

## Scoring rubric

| Dimension | Points |
| --- | ---: |
| Decision, discovery, domain, and ownership | 9 |
| Communication and contract evolution | 7 |
| Data, consistency, workflow, and reconciliation | 9 |
| Resilience, performance, and failure reasoning | 8 |
| Security, delivery, testing, and supply chain | 7 |
| Observability, recovery, organization, and migration | 7 |
| Trade-offs and communication | 3 |
| **Total** | **50** |

Interpretation: **43–50** architect-ready; **35–42** strong with targeted gaps;
**25–34** incomplete distributed-state or operating reasoning; **below 25** rebuild
from domain boundaries and invariants. A service-count-first answer cannot exceed 34.

## Improvement loop

Record the three weakest decisions, revisit the matching pages and sources, redraw
authority and failure boundaries, then repeat within seven days using different
failure branches.
