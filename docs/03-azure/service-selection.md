# Azure Service-Selection Matrices

[← Integration services](integration-services.md) · [Next: Reliability and operations →](reliability-operations.md)

These matrices prompt comparison; they do not replace workload analysis. Verify current
SKUs, Regions, quotas, availability features, networking, and pricing.

## Compute and application runtime

| Option | Strong fit | Principal trade-off to test |
| --- | --- | --- |
| VMs/Scale Sets | OS control, compatibility, special hardware, custom agents | Images, patching, capacity, scaling, extensions, and recovery |
| AKS | Kubernetes APIs, ecosystem, complex container platform | Nodes, add-ons, upgrades, policy, networking, and skill |
| Container Apps | Managed microservices/jobs with revisions and event scale | Environment model, network, limits, startup, observability, cost |
| Container Instances | Simple isolated container execution | Orchestration, durability, scaling, and integration boundaries |
| App Service | Managed web/API hosting and deployment slots | Plan/SKU capacity, runtime support, networking, platform limits |
| Functions | Event-driven, bounded execution | Hosting plan, duration, concurrency, cold start, state, downstream load |

## Storage and database

| Requirement | Typical Azure options | Decision evidence |
| --- | --- | --- |
| Object/lake data | Blob Storage or ADLS Gen2 | Namespace, access, redundancy, lifecycle, immutability, transactions |
| VM block storage | Managed Disks | Zone, performance tier, bursting, snapshot/backup, attachment |
| Shared files | Azure Files or Azure NetApp Files where justified | Protocol, latency, throughput, identity, backup, cost |
| SQL Server workloads | Azure SQL Database, Managed Instance, SQL on VM | Compatibility, control, features, HA, maintenance, license |
| PostgreSQL | Azure Database for PostgreSQL or VM-based alternatives | Extensions, topology, connections, HA, migration, operations |
| Globally distributed NoSQL | Cosmos DB | API/model, partition key, consistency, Regions, throughput, cost |
| Cache/in-memory | Azure Managed Redis | Authority, persistence, eviction, topology, failover |
| Search/vector | Azure AI Search | Indexing, freshness, query, scale, security, cost |

## Integration and workflow

| Need | Typical choice | Critical question |
| --- | --- | --- |
| Enterprise queues/topics | Service Bus | Tier, sessions/order, transactions, lock, duplicate detection, DLQ? |
| Discrete event routing | Event Grid | Schema, filters, delivery, dead letter, private access, ownership? |
| Retained partitioned stream | Event Hubs | Partitions, throughput, consumer groups, retention, capture, replay? |
| Integration workflow | Logic Apps | Hosting, connectors, identity, state, network, limits, cost? |
| Code orchestration | Durable Functions | Determinism, replay, state, compensation, versioning, diagnostics? |
| Managed API gateway | API Management | Tier, gateway topology, policies, auth, quotas, latency, lifecycle? |

## Connectivity and edge

| Need | Typical choice | Principal distinction |
| --- | --- | --- |
| Connect a few VNets | VNet peering | Direct nontransitive connectivity and pairwise management |
| Managed transit | Virtual WAN | Managed hubs, routing, branches, Regions, security integration |
| Private PaaS access | Private Link/private endpoints | Private IP plus DNS and service-specific approval behavior |
| Encrypted internet hybrid path | VPN Gateway | Internet variability, active-active/BGP, tunnel/site diversity |
| Private hybrid connectivity | ExpressRoute | Circuit/provider/peering diversity and encryption requirements |
| Regional layer-7 ingress | Application Gateway | HTTP routing, TLS, autoscale, WAF, zone design |
| Global HTTP edge | Front Door | Global routing, acceleration, origins, WAF, caching, private link |
| DNS-based global routing | Traffic Manager | Resolver/TTL behavior and endpoint-health routing |

## Final selection test

For every option state authority, scope, consistency, scaling unit, quotas, failure and
degradation, security boundary, observability, backup/recovery, deployment, ownership,
pricing dimensions, skills, portability, and evidence that changes the choice.
