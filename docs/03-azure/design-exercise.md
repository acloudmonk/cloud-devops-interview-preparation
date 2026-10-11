# Enterprise Azure Design Exercise

[← Well-Architected review](well-architected.md) · [Next: Scenarios →](scenarios.md)

## Brief

A regulated global insurer is consolidating multiple Azure tenants and subscriptions.
Its customer portal, broker APIs, claims processing, documents, relational systems,
event streams, analytics, and internal operators serve three geographies. Demand spikes
after severe weather. Recent incidents involved standing privileges, policy drift,
private-DNS failure, SNAT exhaustion, database connections, unprocessed messages,
untested backups, quota limits, and poorly allocated cost.

## Candidate tasks

1. Clarify journeys, demand, data, SLOs, RTO/RPO, residency, and economics.
2. Design tenant, management-group, subscription, landing-zone, and ownership boundaries.
3. Select Regions/zones, hub-spoke or vWAN, hybrid/edge paths, ingress, egress, and DNS.
4. Choose compute, containers/serverless, storage, database, analytics, and integration.
5. Design Entra identity, RBAC, Policy, keys, security operations, and incident access.
6. Define observability, delivery, recovery evidence, operations, quotas, and capacity.
7. Model cost allocation, unit economics, sustainability, and Well-Architected review.

## Required artifacts

- hierarchy/context diagram with tenant, subscription, Region, and zone boundaries;
- identity, trust, data authority, key, and audit model;
- request, event, analytical, hybrid, and administrative paths;
- landing-zone/shared-service responsibility and SLO model;
- availability/degradation, quota/capacity, and recovery matrix;
- deployment, observability, incident, and support model;
- cost drivers, allocation, unit metric, risks, and decision log.

## Failure injects

- one zone lacks VM SKU capacity during a catastrophe;
- a deny Policy blocks the production recovery deployment;
- private endpoint DNS resolves incorrectly in a branch office;
- Function concurrency overwhelms Azure SQL connections;
- a Service Bus poison message blocks a session;
- Key Vault access fails during isolated restore;
- a Region fails while Cosmos DB/application write ownership is ambiguous;
- the shared hub firewall changes and affects every workload landing zone.

## Evaluation rubric

| Dimension | Points |
| --- | ---: |
| Discovery, workload model, outcomes, and assumptions | 7 |
| Hierarchy, landing zones, platform, identity, and governance | 10 |
| Global infrastructure, networking, hybrid, and edge | 8 |
| Compute, data, integration, and security decisions | 10 |
| Reliability, observability, operations, and recovery | 8 |
| Quotas, cost, sustainability, review, and communication | 7 |
| **Total** | **50** |

A strong answer separates tenant/platform governance from workload architecture,
explains Azure service semantics, identifies shared dependencies, defines failure and
recovery evidence, and records alternatives. A product list is incomplete.
