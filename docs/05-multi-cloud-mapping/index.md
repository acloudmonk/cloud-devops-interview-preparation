# AWS–Azure–GCP Capability Mapping

[← Curriculum overview](../curriculum/index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-11**

Level: **Senior / Architect**

This module compares AWS, Azure, and Google Cloud by architectural capability,
scope, semantics, failure behavior, operations, and economics. Similar names do not
prove equivalent behavior. Use every mapping as a shortlist that must be validated
against current requirements and provider documentation.

!!! tip "Where to start"
    Start with **1. Capability-first decision model** and follow the numbered path.
    Complete Modules 02–04 first when you need provider-specific depth.

## Learning objectives

- translate requirements between AWS, Azure, and Google Cloud without false equivalence;
- compare hierarchy, identity, governance, location, networking, runtime, and data semantics;
- choose single-cloud, workload-per-cloud, portable-platform, or distributed patterns;
- expose cross-cloud latency, consistency, recovery, security, operations, and cost risks;
- present placement decisions with evidence, alternatives, and exit triggers.

## Recommended module path

### Phase 1 — Learn cross-cloud decisions

| Step | Page | Outcome |
| ---: | --- | --- |
| 1 | [Capability-first decision model](concepts.md) | Compare semantics, not labels |
| 2 | [Hierarchy, landing zones, and governance](governance.md) | Translate resource and policy boundaries |
| 3 | [Identity, security, and keys](identity-security.md) | Federate identity and preserve least privilege |
| 4 | [Locations, scope, and resilience](locations-resilience.md) | Compare failure domains and resource scope |
| 5 | [Networking, edge, and private connectivity](networking.md) | Translate connectivity without topology errors |
| 6 | [Compute, containers, and serverless](compute-platforms.md) | Select runtimes by responsibility and limits |
| 7 | [Storage, databases, and analytics](data-platforms.md) | Compare data semantics and movement costs |
| 8 | [APIs, messaging, events, and workflows](integration.md) | Preserve delivery and ordering behavior |
| 9 | [Delivery, artifacts, and infrastructure as code](delivery-iac.md) | Standardize safely across provider control planes |
| 10 | [Observability, operations, and incident response](operations.md) | Unify outcomes without losing native evidence |
| 11 | [Cost, contracts, capacity, and sustainability](cost-commercial.md) | Model total portfolio economics |
| 12 | [Portability, interoperability, and placement](portability-placement.md) | Decide where abstraction adds value |
| 13 | [Cross-cloud capability matrices](capability-matrices.md) | Build a validated service shortlist |

### Phase 2 — Apply the reasoning

| Step | Page | Outcome |
| ---: | --- | --- |
| 14 | [Enterprise portfolio design exercise](design-exercise.md) | Place regulated workloads across three clouds |
| 15 | [Scenario questions and model answers](scenarios.md) | Practise at least 15 architect scenarios |
| 16 | [Advanced architecture and incident drills](scenario-drills.md) | Resolve at least 10 cross-cloud failures |
| 17 | [Ten-minute cross-cloud architecture review](presentation-template.md) | Present placement and trade-offs |

### Phase 3 — Revise and assess

| Step | Page | Outcome |
| ---: | --- | --- |
| 18 | [Rapid-fire revision](rapid-fire.md) | Test at least 50 explanations |
| 19 | [Active-recall flashcards](flashcards.md) | Revisit at least 25 weak concepts |
| 20 | [Timed cross-cloud mapping mock interview](../mock-interviews/cross-cloud-mapping.md) | Complete a scored 50-minute assessment |
| 21 | [References, books, and videos](references.md) | Validate decisions with primary sources |

## Scope boundary

This module translates capabilities. Use [Hybrid & Multi-Cloud](../28-hybrid-multicloud/index.md)
for deeper distributed patterns, [Well-Architected Reviews](../27-well-architected/index.md)
for formal assessments, and Modules [02](../02-aws/index.md), [03](../03-azure/index.md),
and [04](../04-gcp/index.md) for provider-specific architecture.

## Completion checklist

- [ ] I compare scope, semantics, limits, failure, and operations—not only names.
- [ ] I can translate hierarchy, identity, network, runtime, and data boundaries.
- [ ] I can reject unjustified active-active multicloud.
- [ ] I model data transfer, duplicated skills/tooling, quota, and recovery capacity.
- [ ] I validate current availability, pricing, compliance, and documentation.
- [ ] I completed the scenarios, drills, flashcards, and scored mock interview.
