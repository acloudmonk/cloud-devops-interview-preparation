# Cost, Capacity, Quotas, and Sustainability

[← Reliability and operations](reliability-operations.md) · [Next: Well-Architected review →](well-architected.md)

## Model Azure pricing dimensions

Include compute/plan time, requests, provisioned throughput, storage capacity and
transactions, backup, observability ingestion/retention, Defender/Sentinel, licenses,
support, marketplace products, public/zone/Region egress, NAT/Firewall processing, and
hybrid connectivity. Use representative demand and ranges; a low unit price can amplify
through architecture or retry behavior.

## Build allocation and accountability

Use subscriptions, management groups, resource groups, tags, billing scopes, Cost
Management exports, budgets, alerts, and cost allocation rules as appropriate. Define
shared platform allocation and unit metrics such as cost per transaction, customer,
environment, or protected GiB. Tags need standards, enforcement, ownership, and handling
for resources that do not inherit or support them as expected.

## Optimize safely

Remove idle resources/data, schedule nonproduction, right-size from evidence, choose
appropriate service tiers and storage lifecycle, tune architecture/demand, then purchase
Reservations or Savings Plan for Compute for stable eligible usage. Spot VMs suit
interruptible workloads with diversification, checkpointing, and eviction handling.
Azure Hybrid Benefit and licenses require verified eligibility and governance.

## Treat quotas and capacity as architecture

Inventory adjustable and hard limits by tenant, subscription, Region, zone, resource
provider, SKU, API, network, and service. Model cores, IPs, SNAT ports, private endpoints,
connections, throughput units, partitions, deployments, and Regional/SKU capacity for
normal, burst, rollout, and failure. Register providers and request increases early;
test throttling and degradation.

## Improve sustainability through efficiency

Remove idle capacity, increase utilization, choose efficient managed services/SKUs,
minimize unnecessary movement and copies, apply lifecycle, and match availability to
actual need. Use Azure sustainability and carbon-emissions reporting where available,
but measure useful work per resource and preserve required security and reliability.
