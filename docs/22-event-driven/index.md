# Messaging and Event-Driven Architecture

[← Curriculum overview](../curriculum/index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-11**
Level: **Senior / Architect**

Messaging replaces temporal and availability coupling with explicit contracts,
durability, delivery, ordering, state, and operational responsibilities. A broker
can absorb bursts and enable independent consumers, but it cannot define business
correctness, make side effects exactly once, or eliminate dependency ownership.

!!! tip "Where to start"
    Start with **1. Asynchronous architecture decision model** and follow the
    numbered path. AWS is the architecture anchor, with Apache Kafka, Azure, and
    Google Cloud translations. No deployment lab is required.

## Learning objectives

- decide when synchronous calls, queues, pub/sub, event buses, or logs fit;
- distinguish commands, domain events, integration events, notifications, and facts;
- reason precisely about durability, acknowledgment, delivery, and side effects;
- choose partition keys, ordering scope, consumer groups, retention, and replay;
- evolve event contracts with compatibility, ownership, and governance;
- build idempotent consumers, outbox/inbox boundaries, projections, and workflows;
- contain poison messages, lag, retry storms, hot partitions, and broker failure;
- secure producers, consumers, destinations, schemas, payloads, and operations;
- observe end-to-end freshness, correctness, capacity, and business convergence;
- translate capabilities across AWS, Kafka, Azure, and Google Cloud without false parity.

## Recommended module path

### Phase 1 — Learn the event system

| Step | Page | Outcome |
| ---: | --- | --- |
| 1 | [Asynchronous architecture decision model](concepts.md) | Identify when messaging reduces coupling and when it adds risk |
| 2 | [Patterns and platform selection](patterns-platforms.md) | Choose queue, pub/sub, event bus, log, or workflow deliberately |
| 3 | [Delivery, acknowledgment, and ordering](delivery-ordering.md) | Define guarantees at producer, broker, consumer, and effect boundaries |
| 4 | [Partitioning and consumer scaling](partitioning-scaling.md) | Balance order, throughput, skew, groups, and rebalancing |
| 5 | [Event contracts and schema evolution](contracts-schemas.md) | Design owned, compatible, discoverable event contracts |
| 6 | [Processing state, replay, and consistency](processing-state-replay.md) | Apply idempotency, outbox/inbox, projections, and reconciliation |
| 7 | [Resilience and operations](resilience-operations.md) | Operate lag, retries, DLQs, backpressure, recovery, and capacity |
| 8 | [Security and governance](security-governance.md) | Protect access, payloads, privacy, lineage, and lifecycle |
| 9 | [AWS-first multi-cloud capability map](cloud-mapping.md) | Translate messaging semantics across managed and Kafka platforms |

### Phase 2 — Apply the reasoning

| Step | Page | Outcome |
| ---: | --- | --- |
| 10 | [Enterprise event-platform design exercise](design-exercise.md) | Design a global AWS-first order and telemetry platform |
| 11 | [Scenario questions and model answers](scenarios.md) | Practise at least 15 senior messaging scenarios |
| 12 | [Advanced architecture and incident drills](scenario-drills.md) | Resolve at least 10 ambiguous event-system failures |
| 13 | [Ten-minute event architecture review](presentation-template.md) | Present semantics, scale, failure, trust, and operation |

### Phase 3 — Revise and assess

| Step | Page | Outcome |
| ---: | --- | --- |
| 14 | [Rapid-fire revision](rapid-fire.md) | Test at least 50 concise explanations |
| 15 | [Active-recall flashcards](flashcards.md) | Revisit at least 25 weak concepts |
| 16 | [Timed event-driven architecture mock interview](../mock-interviews/event-driven-architecture.md) | Complete a scored 50-minute assessment |
| 17 | [References and videos](references.md) | Deepen weak areas with authoritative sources |

## Scope boundary

[Microservices](../20-microservices/index.md) covers domain and service boundaries,
[SaaS](../21-saas/index.md) covers tenant-aware operation, and Module 23 will cover
database internals and data-platform choices. This module owns asynchronous contracts,
brokers, logs, delivery, processing, replay, and event-system operations.

## Completion checklist

- [ ] I can justify asynchronous messaging against a synchronous alternative.
- [ ] I can state delivery, ordering, retention, and replay boundaries precisely.
- [ ] I can design idempotency and reconciliation for external side effects.
- [ ] I can select a partition key and explain skew and migration consequences.
- [ ] I can evolve a contract without coordinating every consumer release.
- [ ] I can diagnose lag, poison messages, retry amplification, and hot partitions.
- [ ] I answered all scenarios aloud and completed the scored mock interview.
