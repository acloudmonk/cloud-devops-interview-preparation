# APIs and Enterprise Identity

[← Curriculum overview](../curriculum/index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-11**
Level: **Senior / Architect**

APIs expose business capabilities across trust and ownership boundaries. Identity
establishes who or what is acting; authorization decides whether that actor may
perform a specific action on a specific resource in the current context. Strong
architecture designs the contract, trust, policy, failure, and lifecycle together.

!!! tip "Where to start"
    Start with **1. API and identity decision model** and follow the numbered path.
    AWS is the implementation anchor; open standards, Azure, and Google Cloud are
    translated explicitly. No executable lab is required.

## Learning objectives

- choose REST, gRPC, GraphQL, events, or webhooks from interaction requirements;
- design evolvable contracts, idempotency, pagination, errors, and lifecycle policy;
- place gateways, management planes, service boundaries, and traffic controls;
- distinguish authentication, delegation, federation, and authorization;
- explain OAuth 2.0, OpenID Connect, SAML, SCIM, JWT, and session boundaries;
- design RBAC, ABAC, relationship, and policy-based authorization;
- replace long-lived workload secrets with scoped, short-lived identity;
- threat-model token, consent, redirect, tenant, webhook, and API abuse paths;
- operate identity and API platforms through outages, changes, audits, and incidents.

## Recommended module path

### Phase 1 — Learn the contract and trust system

| Step | Page | Outcome |
| ---: | --- | --- |
| 1 | [API and identity decision model](concepts.md) | Connect capability, contract, actor, trust, policy, and evidence |
| 2 | [API contracts and lifecycle](api-design-contracts.md) | Design compatible HTTP APIs with explicit semantics and ownership |
| 3 | [Interaction styles and integration](api-styles-integration.md) | Choose REST, gRPC, GraphQL, events, and webhooks deliberately |
| 4 | [Gateways and API management](gateway-management.md) | Place routing, protection, quotas, products, and developer experience |
| 5 | [Identity and federation protocols](identity-protocols.md) | Separate OAuth, OIDC, SAML, SCIM, tokens, and sessions |
| 6 | [Authorization and policy](authorization-policy.md) | Model resource decisions, tenancy, delegation, and audit |
| 7 | [Workload identity and federation](workload-federation.md) | Remove static credentials and contain machine trust |
| 8 | [Security and threat modeling](security-threats.md) | Protect APIs, tokens, tenants, webhooks, and recovery paths |
| 9 | [Operations, governance, and resilience](operations-governance.md) | Run lifecycle, evidence, incidents, dependencies, and cost |

### Phase 2 — Apply the reasoning

| Step | Page | Outcome |
| ---: | --- | --- |
| 10 | [Enterprise API and identity design exercise](design-exercise.md) | Design an AWS-first partner platform with enterprise federation |
| 11 | [Scenario questions and model answers](scenarios.md) | Practise 15 senior API and identity scenarios |
| 12 | [Advanced trust-boundary drills](scenario-drills.md) | Handle 10 ambiguous security and availability events |
| 13 | [Ten-minute architecture review](presentation-template.md) | Present contracts, identity, policy, operation, and residual risk |

### Phase 3 — Revise and assess

| Step | Page | Outcome |
| ---: | --- | --- |
| 14 | [Rapid-fire revision](rapid-fire.md) | Test 50 concise explanations |
| 15 | [Active-recall flashcards](flashcards.md) | Revisit weak concepts with spaced repetition |
| 16 | [Timed API and identity mock interview](../mock-interviews/api-enterprise-identity.md) | Complete a scored 50-minute assessment |
| 17 | [References and videos](references.md) | Deepen weak areas with standards and primary sources |

## Relationship to adjacent modules

[Zero Trust](../16-zero-trust/index.md), [Microservices](../20-microservices/index.md),
[SaaS](../21-saas/index.md), [Event-Driven Systems](../22-event-driven/index.md),
and [Hybrid/Multi-Cloud](../28-hybrid-multicloud/index.md) provide adjacent depth.
This module focuses on API contracts and enterprise identity decisions.

## Completion checklist

- [ ] I can choose an API style and explain rejected alternatives.
- [ ] I can trace browser, service, token, policy, and data trust boundaries.
- [ ] I can distinguish ID, access, refresh, session, and workload credentials.
- [ ] I can design object- and tenant-level authorization with auditable decisions.
- [ ] I can explain degraded modes, revocation limits, rotation, and recovery.
- [ ] I answered all 25 scenarios aloud and completed the scored mock interview.
