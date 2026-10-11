# Azure Architecture References and Videos

[← Active-recall flashcards](flashcards.md) · [Module overview](index.md)

Azure services, SKUs, quotas, Region/zone availability, pricing, and recommended
practices change. Verify current Microsoft documentation, subscription limits, pricing,
and compliance eligibility before production decisions.

## Suggested reading order

1. [Azure Architecture Center](https://learn.microsoft.com/azure/architecture/)
2. [Microsoft Cloud Adoption Framework for Azure](https://learn.microsoft.com/azure/cloud-adoption-framework/)
3. [Azure landing zones](https://learn.microsoft.com/azure/cloud-adoption-framework/ready/landing-zone/)
4. [Azure landing-zone design areas](https://learn.microsoft.com/azure/cloud-adoption-framework/ready/landing-zone/design-areas)
5. [Azure Well-Architected Framework](https://learn.microsoft.com/azure/well-architected/what-is-well-architected-framework)

## Foundation, governance, identity, and security

- [Azure regions and availability zones](https://learn.microsoft.com/azure/reliability/regions-overview)
- [Azure Resource Manager overview](https://learn.microsoft.com/azure/azure-resource-manager/management/overview)
- [Management groups overview](https://learn.microsoft.com/azure/governance/management-groups/overview)
- [Azure Policy overview](https://learn.microsoft.com/azure/governance/policy/overview)
- [Azure RBAC overview](https://learn.microsoft.com/azure/role-based-access-control/overview)
- [Managed identities overview](https://learn.microsoft.com/entra/identity/managed-identities-azure-resources/overview)
- [Privileged Identity Management](https://learn.microsoft.com/entra/id-governance/privileged-identity-management/pim-configure)
- [Azure Key Vault overview](https://learn.microsoft.com/azure/key-vault/general/overview)
- [Microsoft Defender for Cloud](https://learn.microsoft.com/azure/defender-for-cloud/defender-for-cloud-introduction)
- [Microsoft Sentinel overview](https://learn.microsoft.com/azure/sentinel/overview)

## Networking and application platforms

- [Azure Virtual Network overview](https://learn.microsoft.com/azure/virtual-network/virtual-networks-overview)
- [Azure Private Link overview](https://learn.microsoft.com/azure/private-link/private-link-overview)
- [Azure Virtual WAN overview](https://learn.microsoft.com/azure/virtual-wan/virtual-wan-about)
- [Azure ExpressRoute overview](https://learn.microsoft.com/azure/expressroute/expressroute-introduction)
- [Azure Front Door overview](https://learn.microsoft.com/azure/frontdoor/front-door-overview)
- [Azure Virtual Machine Scale Sets](https://learn.microsoft.com/azure/virtual-machine-scale-sets/overview)
- [Azure Kubernetes Service concepts](https://learn.microsoft.com/azure/aks/core-aks-concepts)
- [Azure Container Apps overview](https://learn.microsoft.com/azure/container-apps/overview)
- [Azure App Service overview](https://learn.microsoft.com/azure/app-service/overview)
- [Azure Functions overview](https://learn.microsoft.com/azure/azure-functions/functions-overview)

## Data, integration, operations, and cost

- [Azure Storage introduction](https://learn.microsoft.com/azure/storage/common/storage-introduction)
- [Azure SQL documentation](https://learn.microsoft.com/azure/azure-sql/)
- [Azure Cosmos DB introduction](https://learn.microsoft.com/azure/cosmos-db/introduction)
- [Azure Service Bus messaging overview](https://learn.microsoft.com/azure/service-bus-messaging/service-bus-messaging-overview)
- [Azure Event Grid overview](https://learn.microsoft.com/azure/event-grid/overview)
- [Azure Event Hubs overview](https://learn.microsoft.com/azure/event-hubs/event-hubs-about)
- [Azure Monitor overview](https://learn.microsoft.com/azure/azure-monitor/fundamentals/overview)
- [Azure Backup overview](https://learn.microsoft.com/azure/backup/backup-overview)
- [Azure subscription and service limits](https://learn.microsoft.com/azure/azure-resource-manager/management/azure-subscription-service-limits)
- [Microsoft Cost Management documentation](https://learn.microsoft.com/azure/cost-management-billing/)

## Video sources

- [Microsoft Azure](https://www.youtube.com/@MicrosoftAzure)
- [Microsoft Mechanics](https://www.youtube.com/@MicrosoftMechanicsSeries)
- [Azure Friday](https://www.youtube.com/@AzureFriday)
- [Microsoft Security](https://www.youtube.com/@MicrosoftSecurity)

Search official channels for recent sessions on Azure Landing Zones, Entra and managed
identities, Policy, private networking, AKS, Container Apps, Functions, data services,
resilience, Monitor, Well-Architected, quotas, and Cost Management. Prefer current
sessions because product names, tiers, and capabilities evolve.

## Books for deeper study

- *Azure Architecture Explained* by David Rendón
- *Exam Ref AZ-305 Designing Microsoft Azure Infrastructure Solutions* by Ashish Agrawal
- *Designing Distributed Systems* by Brendan Burns
- *Cloud Strategy* by Gregor Hohpe
- *Designing Data-Intensive Applications* by Martin Kleppmann
- *Site Reliability Engineering* by Betsy Beyer and others

## Suggested review loop

1. Choose a workload and write its journeys, qualities, demand, and constraints.
2. Draw tenant, management-group, subscription, Region/zone, network, and ownership boundaries.
3. Compare two runtime, data, integration, and ingress options using service semantics.
4. Inject zone capacity, Policy, identity, private DNS, quota, data, and Region failures.
5. Restore an isolated backup and define business-integrity evidence conceptually.
6. Model top meters, failure capacity, allocation, and one unit-cost metric.
7. Answer scenarios aloud, score the mock, and revisit only weak primary sources.
