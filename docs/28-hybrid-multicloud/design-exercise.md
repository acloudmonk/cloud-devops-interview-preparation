# Enterprise Hybrid/Multi-Cloud Design Exercise

[← Module overview](index.md) · [Governance and cost](governance-cost.md)

## Brief

A regulated manufacturer runs SAP and factory control on-premises, customer APIs
on AWS, workforce identity on Azure, and analytics/ML on Google Cloud. Acquisitions
added overlapping networks and directories. Factories need local operation during
WAN loss. Leadership requests “full portability” and cloud-provider failover while
reducing data-center cost within two years.

## Produce

1. Business drivers, constraints, placement matrix, and rejected simplifications.
2. Target pattern and component/data placement with temporary versus steady state.
3. IP, routing, DNS, connectivity, encryption, inspection, and capacity design.
4. Workforce/workload identity, trust, keys, emergency access, and recovery model.
5. Data authority, integration, sovereignty, consistency, lineage, and exit design.
6. Platform/delivery standards and explicit provider-specific capabilities.
7. Service ownership, observability, incident, support, and drift model.
8. Failure tests, continuity, roadmap, unit economics, skills, and residual risks.

## Key constraints

- Factory safety cannot depend on WAN or public-cloud control planes.
- Payment/customer data has residency and deletion requirements.
- CIDR overlap prevents simple routed connectivity after acquisitions.
- Central identity is business-critical and has never been failed over.
- Cross-cloud analytics movement is large and expensive.
- SAP licenses and hardware depreciation affect migration economics.
- The organization cannot operate three identical platform stacks well.

## Strong answer outline

Reject universal portability and active-active failover. Define autonomous edge/factory
operation, portfolio-level provider placement, and asynchronous domain interfaces.
Use AWS as the primary customer platform, preserve Azure/Google capabilities behind
owned contracts, and isolate control planes. Build an IP/DNS and identity transition,
local data authority with governed replication, common artifact/telemetry standards,
provider-native authorization, and one service/incident model.

Sequence inventory and ownership, connectivity/trust foundations, data contracts,
factory disconnection tests, then workload migrations. Measure SLOs, recovery, egress,
unit cost, manual operations, and exit rehearsal. Retire transitional duplication.

## Self-scoring rubric

| Dimension | 0 | 2 | 4 |
| --- | --- | --- | --- |
| Strategy | provider list | drivers noted | placement and simplification tied to durable outcomes |
| Boundaries | vague diagram | connectivity shown | routing/DNS/trust/data/failure boundaries complete |
| Data/platform | “Kubernetes” | integration described | authority, consistency, delivery, portability tier, exit evidence |
| Operations | separate teams | common monitoring | service ownership, incident, drift, support, disconnected operation |
| Economics/governance | list price | TCO considered | lifecycle cost, authority, skills, exceptions, retirement |
| Evidence | design only | tests listed | measurable SLO, failure, recovery, exit, and value roadmap |

Maximum: **24**; aim for **19** before the mock interview.

Return to the [module overview](index.md) when ready to continue.
