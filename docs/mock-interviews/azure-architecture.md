# Azure Architecture Mock Interview

[← Mock interview overview](index.md) · [Module 03 overview](../03-azure/index.md)

Duration: **50 minutes**
Level: **Senior / Architect**
Primary context: **Regulated global insurance platform on Azure**

## Candidate brief

A global insurer is consolidating multiple Azure tenants and subscriptions. Its portal,
broker APIs, claims processing, documents, relational systems, events, analytics, and
operators span three geographies. Severe weather causes demand spikes. Incidents
involved standing privilege, Policy drift, private DNS, SNAT exhaustion, database
connections, poison messages, untested backups, quotas, and unexplained cost. Design
the target workload and Azure operating model.

## Interview structure

### 0–7 minutes — Discovery and workload

Clarify users, journeys, demand, data/invariants, latency, SLOs, RTO/RPO, residency,
compliance, integrations, migration, skills, support, and economics. State assumptions
and decision criteria.

### 7–17 minutes — Landing zone and security

Design tenant, management groups, platform/workload subscriptions, vending, Entra,
managed identities, PIM, RBAC, Policy, keys, logs, Defender/Sentinel, emergency access,
exceptions, and platform/workload ownership.

### 17–28 minutes — Platform architecture

Choose Regions/zones, hub-spoke or vWAN, ingress/egress, private DNS/endpoints, edge and
hybrid paths; then select compute, app/container/serverless, storage, database,
analytics, API, messaging, event, and workflow services. Explain scope and limits.

### 28–38 minutes — Failure branches

Choose three:

- one zone cannot allocate the required VM SKU;
- a deny Policy blocks an emergency recovery deployment;
- on-premises cannot resolve a private endpoint correctly;
- outbound connections exhaust SNAT ports;
- Functions exhaust Azure SQL connections;
- a Service Bus poison message blocks an ordered session;
- Key Vault access fails during isolated restore;
- Regional failover creates ambiguous write authority.

### 38–45 minutes — Operations, recovery, and economics

Define Azure Monitor/SLOs, incident/change paths, backup/restore, failover/failback,
support, quotas, failure capacity, cost allocation, unit economics, commitments,
sustainability, and five-pillar review evidence.

### 45–50 minutes — Executive close

State the architecture and first delivery slice, top risks/assumptions, ownership,
measurable evidence, cost drivers, and conditions that would change the design.

## Scoring rubric

| Dimension | Points |
| --- | ---: |
| Discovery, workload model, outcomes, and assumptions | 7 |
| Hierarchy, landing zones, platform, identity, and governance | 10 |
| Global infrastructure, networking, hybrid, and edge | 8 |
| Compute, data, integration, and security decisions | 10 |
| Reliability, observability, operations, and recovery | 8 |
| Quotas, cost, sustainability, review, and evidence | 5 |
| Trade-offs and executive communication | 2 |
| **Total** | **50** |

Interpretation: **43–50** architect-ready; **35–42** strong with targeted gaps;
**25–34** incomplete scope, service semantics, or operational reasoning; **below 25**
rebuild from workload, hierarchy, failure, and evidence. A product list without
identity, network, recovery, quotas, operations, and economics cannot exceed 34.

## Improvement loop

Record the three weakest decisions, revisit the matching module pages and primary
sources, redraw hierarchy/dependencies, then repeat within seven days using different
failure branches.
