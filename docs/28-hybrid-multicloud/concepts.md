# Distributed-Estate Decision Model

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Use multiple environments only when the business outcome outweighs coordination
cost. Provider count is not an architecture objective.

## Seven-part model

1. **Driver** — sovereignty, latency, acquisition, capability, continuity, regulation, or exit need.
2. **Placement** — workload component and data location with explicit rationale.
3. **Boundary** — network, identity, data, management, provider, and organizational failure domains.
4. **Interaction** — APIs, events, replication, DNS, routing, and consistency behavior.
5. **Operation** — ownership, delivery, telemetry, incident, inventory, and support model.
6. **Economics** — duplicated platforms, egress, licenses, contracts, people, and migration cost.
7. **Evidence** — SLOs, tests, incidents, unit cost, portability exercise, and risk acceptance.

```mermaid
flowchart LR
    B[Business driver] --> P[Placement and pattern]
    P --> BND[Trust failure and data boundaries]
    BND --> O[Cross-environment operation]
    O --> E[Outcomes cost and evidence]
    E --> B
```

## Vocabulary

- **Hybrid cloud:** public cloud combined with private/on-premises/edge environments.
- **Multi-cloud:** deliberate use of multiple public-cloud providers.
- **Distributed cloud:** cloud capability extended to different physical locations under a provider or unified model.
- **Edge:** compute/data placed near devices, users, or physical processes.
- **SaaS dependency:** using SaaS does not alone imply a multi-cloud application architecture.

## Common false promises

Kubernetes does not make state, identity, managed services, networks, or operations
portable. Two providers do not guarantee independent failure. Private connectivity
does not create trust. A single pane of glass does not create a single operating
model. Exit plans without data transfer, replacement services, skills, contracts,
and rehearsal are aspirations.

## Architecture test

What durable driver requires each location? Which component and data live there?
What happens when links, identity, DNS, control planes, or one provider fail? Who
operates each path? What is duplicated? How is security and consistency preserved?
What evidence proves the benefit, and what would cause simplification or exit?

Return to the [module overview](index.md) when ready to continue.
