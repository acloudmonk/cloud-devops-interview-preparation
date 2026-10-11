# Rapid-Fire Revision

[← Presentation template](presentation-template.md) · [Next: Flashcards →](flashcards.md)

Answer each in one or two sentences before adding an example.

1. **What is an Azure geography?** A market/data-residency boundary containing one or more Azure Regions.
2. **What is an Azure Region?** A set of data centers deployed within a latency-defined perimeter and connected through a dedicated network.
3. **What is an Availability Zone?** A physically separated data-center grouping within a supported Region with independent facilities.
4. **Does every Region support zones?** No; verify Region, service, SKU, and feature support.
5. **What is zone-redundant?** The service distributes responsibility across zones according to its documented semantics.
6. **Why document service scope?** Global, Regional, zonal, and nonzonal scope changes failure, residency, quota, and recovery.
7. **What is the Azure control plane?** Azure Resource Manager APIs used to create, configure, authorize, and manage resources.
8. **What is a Microsoft Entra tenant?** An identity and directory boundary used by Azure and Microsoft services.
9. **What is a management group?** A governance scope organizing subscriptions with inherited Policy and RBAC.
10. **What is a subscription?** An administration, quota, billing, policy, and resource boundary within a tenant.
11. **What is a resource group?** A management container for resources that usually share lifecycle and ownership.
12. **Must resources match the resource-group Region?** No; the resource-group location stores metadata while contained resources can use supported Regions.
13. **What does Azure RBAC do?** Grants permitted actions at management or data scopes through role assignments.
14. **What does Azure Policy do?** Evaluates and can audit, modify, deploy related configuration, or deny resource state; it does not grant access.
15. **What is PIM?** Privileged Identity Management provides governed eligible and just-in-time privileged access.
16. **What is Conditional Access?** Entra policy evaluating signals to control authentication/access conditions.
17. **What is a managed identity?** An Azure-managed service principal that a resource uses to obtain tokens without stored credentials.
18. **Why is Key Vault a dependency?** Identity, network, throttling, deletion, or unavailable key/secret access can stop otherwise healthy workloads.
19. **What is Defender for Cloud?** Cloud security posture and workload protection capabilities for supported resources/environments.
20. **What is Microsoft Sentinel?** Cloud-native SIEM and security orchestration/response capability.
21. **Is a VNet Regional?** Yes; it is scoped to one Azure Region.
22. **Are NSGs stateful?** Yes; return traffic for an allowed connection is handled statefully.
23. **Is VNet peering transitive?** No; transit requires explicit routing/appliance or managed hub design.
24. **Private Link versus service endpoint?** Private Link assigns a private endpoint IP; service endpoints secure service access from selected subnet identity while using the service endpoint.
25. **Why does Private Link require DNS design?** The service name must resolve to the private endpoint from every intended client boundary.
26. **What does Virtual WAN provide?** Managed hubs and global transit for branches, VNets, routing, and supported security integration.
27. **Does ExpressRoute automatically encrypt traffic?** No; design encryption when the requirement applies.
28. **What causes SNAT exhaustion?** Too many outbound connection translations relative to available ports and reuse behavior.
29. **Front Door versus Application Gateway?** Front Door is global HTTP edge; Application Gateway is Regional layer-7 VNet ingress.
30. **Traffic Manager versus Front Door?** Traffic Manager is DNS routing; Front Door proxies and accelerates HTTP(S) traffic at the edge.
31. **When are VMs appropriate?** When OS/runtime control, compatibility, hardware, or agents require infrastructure-level responsibility.
32. **What are VM Scale Sets?** A managed group of similar VMs with scaling, health, and upgrade capabilities.
33. **When is AKS justified?** When Kubernetes APIs/ecosystem and team capability provide value exceeding platform complexity.
34. **What are Container Apps suited to?** Managed container applications/jobs with revisions, environments, and event-driven scaling.
35. **What is App Service suited to?** Managed web applications and APIs using supported runtimes or containers.
36. **What changes Azure Functions behavior?** Hosting plan, trigger, concurrency, duration, networking, scaling, and downstream capacity.
37. **Blob versus Managed Disk?** Blob is object storage; Managed Disks provide VM block storage.
38. **What does ADLS Gen2 add?** Hierarchical namespace and data-lake semantics over Blob Storage capabilities.
39. **Azure SQL Database versus Managed Instance?** They provide different SQL Server compatibility, instance scope, features, networking, and management boundaries.
40. **What is the key Cosmos DB design decision?** Data model/API, partition key, consistency, Regions, throughput, and cost must match access patterns.
41. **What is a derived store?** A cache, index, projection, or analytical copy rebuilt from an authoritative source.
42. **What does Service Bus provide?** Brokered enterprise queues/topics with tier-dependent messaging features.
43. **What does Event Grid provide?** Routing of discrete events to handlers using subscriptions and filters.
44. **What does Event Hubs provide?** High-throughput retained partitioned event ingestion for consumer groups.
45. **What does API Management provide?** API gateway, policy, publication, lifecycle, and developer-consumption capabilities by tier/model.
46. **Why must consumers be idempotent?** Retries and at-least-once delivery can repeat operations.
47. **What should backlog monitoring include?** Oldest age, ingress/egress, active/locked/dead-letter work, failures, and business delay.
48. **What is Azure Monitor?** The platform for collecting, analyzing, alerting, and visualizing Azure/workload telemetry.
49. **Activity Log versus resource logs?** Activity Log records subscription control-plane events; resource logs expose service-specific data-plane/operation details.
50. **Why is a replica not a backup?** It can replicate accidental deletion, corruption, or malicious change.
51. **What proves RTO/RPO?** Timed recovery plus validated service and data integrity under representative failure.
52. **What is a service quota?** A limit scoped by tenant, subscription, Region, zone, SKU, provider, API, or resource dimension.
53. **Why model failure capacity?** Remaining zones/Regions/services must carry priority demand after failure.
54. **What does Cost Management provide?** Billing analysis, exports, budgets, allocation, and related cost-governance capabilities.
55. **Why use unit economics?** Cost per business outcome distinguishes efficiency from volume growth.
56. **When use Reservations or Savings Plan?** After stable eligible usage and flexibility/risk are understood.
57. **Name the five Azure Well-Architected pillars.** Reliability, Security, Cost Optimization, Operational Excellence, and Performance Efficiency.
58. **How does CAF differ from Well-Architected?** CAF guides adoption/platform/portfolio; Well-Architected guides workload quality and trade-offs.
59. **Is Well-Architected an audit?** No; it is an evidence-based risk and improvement conversation.
60. **What makes an Azure design architect-level?** Traceable outcomes, deliberate scopes, service semantics, failure behavior, evidence, operations, and economics.
