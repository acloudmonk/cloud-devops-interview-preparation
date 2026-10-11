# Microservices Architecture

[← Curriculum overview](../curriculum/index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-11**
Level: **Senior / Architect**

Microservices trade local simplicity and independent change for distributed-system,
data, testing, security, and operational complexity. They are appropriate only when
business boundaries, team ownership, and delivery maturity justify that cost.

!!! tip "Where to start"
    Start with **1. Microservices decision model** and follow the numbered path.
    AWS is the architecture anchor with Azure and Google Cloud translations. The
    module is theoretical and scenario-driven; no deployment lab is required.

## Learning objectives

- decide between modular monolith, services, functions, and other boundaries;
- find bounded contexts using domain language, invariants, change, and ownership;
- design synchronous APIs and asynchronous events with evolvable contracts;
- assign data ownership and reason about consistency, sagas, outbox, and queries;
- prevent cascading failure with deadlines, budgets, isolation, and backpressure;
- secure workforce, workload, tenant, network, secret, and data boundaries;
- test, release, migrate, observe, troubleshoot, and recover distributed changes;
- align service ownership, platform capability, governance, and team topology;
- modernize incrementally and recognize a distributed monolith;
- translate AWS-first capabilities to Azure and Google Cloud without false parity.

## Recommended module path

### Phase 1 — Learn the distributed application

| Step | Page | Outcome |
| ---: | --- | --- |
| 1 | [Microservices decision model](concepts.md) | Connect business change, boundaries, independence, and distributed cost |
| 2 | [Domain and service boundaries](domain-boundaries.md) | Define cohesive bounded contexts, invariants, ownership, and granularity |
| 3 | [Communication and contracts](communication-contracts.md) | Choose sync/async interactions and evolve APIs/events safely |
| 4 | [Data ownership and consistency](data-consistency.md) | Design private data, sagas, outbox, reads, and reconciliation |
| 5 | [Resilience and performance](resilience-performance.md) | Control deadlines, retries, overload, isolation, latency, and capacity |
| 6 | [Security and identity](security-identity.md) | Protect edge, service, workload, tenant, secret, and data boundaries |
| 7 | [Delivery and testing](delivery-testing.md) | Release independent changes with contract, integration, and production evidence |
| 8 | [Observability and operations](observability-operations.md) | Trace journeys, own SLOs, diagnose failures, and recover safely |
| 9 | [Organization and migration](organization-migration.md) | Align teams and incrementally escape monolith or distributed-monolith traps |

### Phase 2 — Apply the reasoning

| Step | Page | Outcome |
| ---: | --- | --- |
| 10 | [Enterprise microservices design exercise](design-exercise.md) | Design an AWS-first order platform with explicit consistency and failure behavior |
| 11 | [Scenario questions and model answers](scenarios.md) | Practise at least 15 senior microservices scenarios |
| 12 | [Advanced architecture and incident drills](scenario-drills.md) | Resolve at least 10 ambiguous distributed-system failures |
| 13 | [Ten-minute architecture review](presentation-template.md) | Present boundaries, contracts, data, failure, operation, and change |

### Phase 3 — Revise and assess

| Step | Page | Outcome |
| ---: | --- | --- |
| 14 | [Rapid-fire revision](rapid-fire.md) | Test at least 50 concise explanations |
| 15 | [Active-recall flashcards](flashcards.md) | Revisit at least 25 weak concepts |
| 16 | [Timed microservices mock interview](../mock-interviews/microservices-architecture.md) | Complete a scored 50-minute assessment |
| 17 | [References and videos](references.md) | Deepen weak areas with primary sources |

## Scope boundary

[Cloud Architecture](../01-cloud-architecture/index.md) supplies general distributed
patterns, [API and Identity](../29-api-identity/index.md) provides protocol depth,
and [Kubernetes](../11-kubernetes/index.md) covers one runtime platform. Module 22
will cover brokers, streams, partitions, replay, and schemas in greater depth.

## Completion checklist

- [ ] I can justify microservices over a modular monolith for this organization.
- [ ] I can draw business, data, identity, team, and failure boundaries.
- [ ] I can explain consistency and recovery without claiming “exactly once.”
- [ ] I can design compatible contracts and independently releasable change.
- [ ] I can diagnose cross-service latency, overload, and partial failure.
- [ ] I answered all 25 scenarios aloud and completed the scored mock interview.
