# DevSecOps and Software Supply Chain

[← Curriculum overview](../curriculum/index.md) ·
[Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**
Level: **Senior / Architect**

DevSecOps is a secure delivery operating model, not a collection of scanners.
It combines secure design, protected development and build systems, trustworthy
artifacts, risk-based release controls, runtime feedback, and accountable response.

!!! tip "Where to start"
    Start with **1. Secure-delivery decision model** and follow the numbered path.
    AWS is the primary cloud context; Azure and Google Cloud are translated where
    controls differ. No executable lab or cloud deployment is required.

## Learning objectives

By the end of this module, you should be able to:

- define security outcomes, ownership, trust boundaries, and usable guardrails;
- facilitate threat modeling and convert threats into owned requirements and tests;
- combine SAST, SCA, secret, DAST, IaC, container, and API testing appropriately;
- secure repositories, CI identity, runners, build inputs, dependencies, and outputs;
- explain SBOMs, provenance, attestations, signatures, verification, and policy;
- design container, Kubernetes, IaC, and cloud configuration controls;
- introduce admission and policy without creating unsafe bypass pressure;
- prioritize vulnerabilities by exploitability, exposure, asset, and business impact;
- operate exception, disclosure, incident, recovery, and measurement processes;
- translate an AWS-first model to Azure and Google Cloud.

## Recommended module path

### Phase 1 — Learn the secure-delivery operating system

| Step | Page | Outcome |
| ---: | --- | --- |
| 1 | [Secure-delivery decision model](concepts.md) | Connect outcomes, trust, prevention, detection, response, and evidence |
| 2 | [Threat modeling and security requirements](threat-modeling.md) | Turn architecture threats into owned mitigations and tests |
| 3 | [Source, code, dependencies, and secrets](code-dependencies.md) | Layer code and dependency assurance without alert dumping |
| 4 | [Pipeline, identity, and build security](pipeline-security.md) | Protect repositories, runners, credentials, and build isolation |
| 5 | [SBOMs, provenance, attestations, and signing](artifacts-provenance.md) | Verify artifact identity, origin, process, and policy |
| 6 | [Container and Kubernetes security](containers-kubernetes.md) | Secure images, registries, workloads, clusters, and runtime feedback |
| 7 | [IaC and cloud security](iac-cloud-security.md) | Govern infrastructure changes and cloud posture with ownership |
| 8 | [Policy, admission, and release decisions](policy-admission.md) | Design enforceable controls, exceptions, and failure modes |
| 9 | [Vulnerability response and governance](vulnerability-response.md) | Prioritize, remediate, disclose, measure, and improve |

### Phase 2 — Apply the reasoning

| Step | Page | Outcome |
| ---: | --- | --- |
| 10 | [Enterprise DevSecOps design exercise](design-exercise.md) | Design an AWS-first secure delivery platform |
| 11 | [Scenario questions and model answers](scenarios.md) | Practise 15 senior DevSecOps scenarios |
| 12 | [Advanced incident drills](scenario-drills.md) | Handle 10 ambiguous supply-chain incidents |
| 13 | [Ten-minute secure-delivery review](presentation-template.md) | Present trust, controls, recovery, adoption, and value |

### Phase 3 — Revise and assess

| Step | Page | Outcome |
| ---: | --- | --- |
| 14 | [Rapid-fire revision](rapid-fire.md) | Test 50 concise verbal explanations |
| 15 | [Active-recall flashcards](flashcards.md) | Revisit weak concepts with spaced repetition |
| 16 | [Timed DevSecOps mock interview](../mock-interviews/devsecops-supply-chain.md) | Complete a scored 50-minute assessment |
| 17 | [References and videos](references.md) | Deepen weak areas with primary sources |

## Scope boundary

Pipeline delivery architecture belongs to [Module 09](../09-cicd/index.md),
container engineering to [Module 10](../10-docker/index.md), Kubernetes platform
operations to [Module 11](../11-kubernetes/index.md), and IaC lifecycle to
[Module 13](../13-terraform/index.md). This module focuses on security assurance
and trust across those delivery systems.

## Completion checklist

- [ ] I can connect each security control to a threat and owner.
- [ ] I can distinguish a vulnerability finding from a release decision.
- [ ] I can explain artifact signatures, provenance, SBOMs, and verification.
- [ ] I can contain and investigate a compromised pipeline or dependency.
- [ ] I can design risk-based admission, exceptions, and break-glass recovery.
- [ ] I can measure exposure reduction without rewarding scan volume.
- [ ] I answered all 25 scenarios aloud and completed the scored mock interview.
