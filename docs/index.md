# Cloud & DevOps Architect Knowledge Base

This is a scenario-driven learning and interview-preparation system for senior
Cloud/DevOps Architects, Principal Engineers, Platform/SRE leaders, and
technical consultants.

It is intentionally organized around decisions rather than product trivia.
Knowing that a service exists is useful; knowing when it is appropriate, how it
fails, how it is secured and operated, and what it costs is architect-level
knowledge.

!!! tip "Start the available course here"
    Open [Module 01: Cloud Architecture & Distributed Systems](01-cloud-architecture/index.md)
    and follow its numbered learning path. Return to the table below when you are
    ready for the next released module.

## Current learning path

This is the canonical order for currently released learning material. Module IDs
preserve the full curriculum structure.

| Study step | Module ID | Module |
| ---: | ---: | --- |
| 1 | 01 | [Cloud Architecture & Distributed Systems](01-cloud-architecture/index.md) |
| 2 | 02 | [AWS Architecture](02-aws/index.md) |
| 3 | 03 | [Azure Architecture](03-azure/index.md) |
| 4 | 04 | [GCP Architecture](04-gcp/index.md) |
| 5 | 05 | [Cross-Cloud Capability Mapping](05-multi-cloud-mapping/index.md) |
| 6 | 06 | [Linux & OS Fundamentals](06-linux/index.md) |
| 7 | 07 | [Cloud Networking & DNS](07-networking/index.md) |
| 8 | 08 | [Git & Source-Control Strategy](08-git/index.md) |
| 9 | 09 | [CI/CD & Progressive Delivery](09-cicd/index.md) |
| 10 | 10 | [Docker & Container Engineering](10-docker/index.md) |
| 11 | 11 | [Kubernetes](11-kubernetes/index.md) |
| 12 | 12 | [Kubernetes Ecosystem](12-kubernetes-ecosystem/index.md) |
| 13 | 13 | [Terraform, OpenTofu & Infrastructure as Code](13-terraform/index.md) |
| 14 | 14 | [Ansible & Configuration Management](14-ansible/index.md) |
| 15 | 15 | [DevSecOps & Software Supply Chain](15-devsecops/index.md) |
| 16 | 16 | [Zero Trust Architecture](16-zero-trust/index.md) |
| 17 | 17 | [Observability, OpenTelemetry, Prometheus & Grafana](17-observability/index.md) |
| 18 | 18 | [Site Reliability Engineering](18-sre/index.md) |
| 19 | 19 | [Platform Engineering and Internal Developer Platforms](19-platform-engineering/index.md) |
| 20 | 20 | [Microservices Architecture](20-microservices/index.md) |
| 21 | 21 | [SaaS Architecture](21-saas/index.md) |
| 22 | 22 | [Messaging and Event-Driven Architecture](22-event-driven/index.md) |
| 23 | 23 | [Database Architecture](23-databases/index.md) |
| 24 | 24 | [Cloud Migration and Modernization](24-migration-modernization/index.md) |
| 25 | 25 | [High Availability, Disaster Recovery & Business Continuity](25-ha-dr-bcp/index.md) |
| 26 | 26 | [FinOps and Cost Architecture](26-finops/index.md) |
| 27 | 27 | [Cross-Cloud Well-Architected Reviews](27-well-architected/index.md) |
| 28 | 28 | [Hybrid and Multi-Cloud Architecture](28-hybrid-multicloud/index.md) |
| 29 | 29 | [APIs and Enterprise Identity](29-api-identity/index.md) |
| 30 | 30 | [Python Automation for Cloud and DevOps](30-python-automation/index.md) |
| 31 | 31 | [AI for Cloud and DevOps](31-ai-for-devops/index.md) |

## Applied architecture practice

After completing several relevant modules, use the
[Cross-Domain Architecture Case Studies](case-studies/index.md) to combine
discovery, option analysis, security, delivery, reliability, operations, cost,
migration, and stakeholder communication. The cases have a numbered practice path,
common scorecard, failure injects, model reasoning, and a principal-level capstone.

## How to use this knowledge base

1. Begin at the [Module 01 overview](01-cloud-architecture/index.md).
2. Follow the numbered module path; use the
   [master competency map](master-competency-map.md) only to inspect broader
   coverage and status.
3. Read the concepts without memorizing service lists.
4. Complete the design and troubleshooting exercises.
5. Answer scenarios aloud before reading the model answer.
6. Score yourself using the
   [scenario answer framework](interview-playbook/scenario-answer-framework.md).
7. Finish with active recall and the timed mock interview.
8. Revisit weak decisions with the linked primary sources.

## Architect decision loop

```mermaid
flowchart LR
    A[Business outcome] --> B[Requirements and constraints]
    B --> C[Architecture options]
    C --> D[Decision and trade-offs]
    D --> E[Secure and deliver]
    E --> F[Observe and operate]
    F --> G[Measure value and risk]
    G --> B
```

## Current release

The current release contains the repository foundation, Cloud Architecture &
Distributed Systems, AWS Architecture, Azure Architecture, GCP Architecture,
Cross-Cloud Capability Mapping, Linux & OS Fundamentals,
Cloud Networking & DNS, Git & Source-Control Strategy, CI/CD & Progressive Delivery,
Docker & Container
Engineering, Kubernetes, Kubernetes Ecosystem, and Terraform/OpenTofu
Infrastructure as Code, Ansible Configuration Management, DevSecOps and Software
Supply Chain, Zero Trust Architecture, Observability, Site Reliability
Engineering, Platform Engineering, Microservices Architecture, SaaS Architecture,
Messaging and Event-Driven Architecture, Database Architecture, Cloud Migration and
Modernization, High Availability,
Disaster Recovery, Business Continuity, FinOps,
Cross-Cloud Well-Architected Reviews, Hybrid and Multi-Cloud Architecture, APIs
and Enterprise Identity, Python Automation for Cloud and DevOps, AI for Cloud and
DevOps, and the Cross-Domain Architecture Case Studies.
Remaining modules are tracked in the competency map and will be
delivered in priority waves.

!!! note "Version-aware content"
    Cloud services and open-source platforms change continuously. Each module
    records a review date and links to authoritative sources rather than
    duplicating fast-changing reference material.
