# Zero Trust Architecture

[← Curriculum overview](../curriculum/index.md) ·
[Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**
Level: **Senior / Architect**

Zero Trust is an architecture and operating model for making explicit,
least-privilege access decisions around resources. It replaces implicit trust
based on location with identity, device, workload, data, behavior, and risk
signals—without pretending that networks, strong authentication, or defense in
depth are no longer necessary.

!!! tip "Where to start"
    Start with **1. Zero Trust decision model** and follow the numbered path.
    AWS is the primary cloud context; Azure and Google Cloud are translated where
    controls differ. No executable lab or cloud deployment is required.

## Learning objectives

By the end of this module, you should be able to:

- explain NIST Zero Trust Architecture without slogans or product bias;
- define protect surfaces, transaction flows, trust signals, and policy boundaries;
- design phishing-resistant workforce identity and governed privileged access;
- select RBAC, ABAC, relationship, and risk-aware authorization appropriately;
- authenticate workloads and eliminate unnecessary long-lived credentials;
- use device posture as one bounded input rather than proof of trustworthiness;
- combine identity-aware access with segmentation and application-layer controls;
- operate secrets, keys, certificates, and emergency access safely;
- map an AWS-first design to Microsoft Azure and Google Cloud;
- measure adoption, access exposure, policy quality, and incident containment.

## Recommended module path

### Phase 1 — Learn the decision system

| Step | Page | Outcome |
| ---: | --- | --- |
| 1 | [Zero Trust decision model](concepts.md) | Connect resources, subjects, signals, policy, enforcement, and feedback |
| 2 | [Workforce identity and federation](workforce-identity.md) | Design lifecycle, authentication, federation, sessions, and privilege |
| 3 | [Authorization and policy](authorization-policy.md) | Choose access models and place understandable enforcement |
| 4 | [Devices, context, and adaptive access](device-context.md) | Evaluate posture and risk without brittle policy |
| 5 | [Workload identity and service access](workload-identity.md) | Authenticate software and constrain machine-to-machine access |
| 6 | [Segmentation and application access](segmentation-access.md) | Limit paths and lateral movement across user and workload traffic |
| 7 | [Credentials, secrets, keys, and PKI](credentials-secrets-pki.md) | Minimize bearer secrets and operate trust lifecycles |
| 8 | [AWS-first and multi-cloud architecture](cloud-architecture.md) | Apply organization, identity, resource, network, and data guardrails |
| 9 | [Telemetry, response, and adoption](operations-adoption.md) | Operate policy, incidents, exceptions, maturity, and measures |

### Phase 2 — Apply the reasoning

| Step | Page | Outcome |
| ---: | --- | --- |
| 10 | [Enterprise Zero Trust design exercise](design-exercise.md) | Modernize hybrid access with an AWS-first target state |
| 11 | [Scenario questions and model answers](scenarios.md) | Practise 15 senior Zero Trust scenarios |
| 12 | [Advanced incident drills](scenario-drills.md) | Handle 10 ambiguous identity and policy incidents |
| 13 | [Ten-minute Zero Trust review](presentation-template.md) | Present risk, architecture, migration, and measurable value |

### Phase 3 — Revise and assess

| Step | Page | Outcome |
| ---: | --- | --- |
| 14 | [Rapid-fire revision](rapid-fire.md) | Test 50 concise verbal explanations |
| 15 | [Active-recall flashcards](flashcards.md) | Revisit weak concepts with spaced repetition |
| 16 | [Timed Zero Trust mock interview](../mock-interviews/zero-trust-architecture.md) | Complete a scored 50-minute assessment |
| 17 | [References and videos](references.md) | Deepen weak areas with standards and primary sources |

## Scope boundary

General network mechanics belong to [Module 07](../07-networking/index.md),
Kubernetes controls to [Module 11](../11-kubernetes/index.md), delivery-chain
security to [Module 15](../15-devsecops/index.md), and broader API/identity design
to planned Module 29. This module focuses on access decisions, trust reduction,
policy enforcement, and migration across workforce and workload environments.

## Completion checklist

- [ ] I can describe Zero Trust without saying "trust nothing."
- [ ] I can trace an access request from signals through decision and enforcement.
- [ ] I can design separate workforce, privileged, and workload identity paths.
- [ ] I can explain what segmentation, mTLS, and device posture do not prove.
- [ ] I can contain identity, session, policy, and certificate compromise.
- [ ] I can propose a phased migration with usable emergency access.
- [ ] I answered all 25 scenarios aloud and completed the scored mock interview.
