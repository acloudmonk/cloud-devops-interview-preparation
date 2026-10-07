# Cloud & DevOps Architect Knowledge Base

This is a scenario-driven learning and interview-preparation system for senior
Cloud/DevOps Architects, Principal Engineers, Platform/SRE leaders, and
technical consultants.

It is intentionally organized around decisions rather than product trivia.
Knowing that a service exists is useful; knowing when it is appropriate, how it
fails, how it is secured and operated, and what it costs is architect-level
knowledge.

!!! tip "Start the available course here"
    Open the [Cloud Architecture & Distributed Systems pilot](01-cloud-architecture/index.md)
    and follow its numbered learning path. It is the only complete module in
    the current release; other numbered modules are visible placeholders for
    future milestones.

## How to use this knowledge base

1. Begin at the [pilot module overview](01-cloud-architecture/index.md).
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

The repository foundation and the Cloud Architecture & Distributed Systems
pilot module form the first release. Remaining modules are tracked in the
competency map and will be delivered in priority waves.

!!! note "Version-aware content"
    Cloud services and open-source platforms change continuously. Each module
    records a review date and links to authoritative sources rather than
    duplicating fast-changing reference material.
