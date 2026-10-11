# Cost, Capacity, Quotas, and Sustainability

[← Reliability and operations](reliability-operations.md) · [Next: Well-Architected review →](well-architected.md)

## Model the bill before optimizing it

Identify pricing dimensions for compute time, requests, storage, operations,
provisioned capacity, backup, observability, support, licenses, public/cross-AZ/cross-
Region data transfer, NAT processing, and third-party products. Use representative
demand and sensitivity ranges. Low unit price can still produce high architecture cost.

## Create allocation and accountability

Use accounts, cost categories, tags, CUR/Data Exports, Cost Explorer, and budgets to
connect spend to owners and business units. Define shared-cost allocation and unit
metrics such as cost per transaction, tenant, build, or protected GiB. Unallocated
cost prevents reliable optimization and accountability.

## Optimize in a safe order

Eliminate unused resources and data; schedule nonproduction; right-size from evidence;
select suitable storage and data lifecycle; tune architecture and demand; then purchase
Savings Plans or Reservations for stable eligible usage. Spot can lower interruptible
compute cost when checkpointing, diversification, and interruption behavior are sound.

## Treat quotas and capacity as architecture

Inventory adjustable and hard quotas per account and Region, scaling rates, IP space,
subnet addresses, ENIs, concurrent execution, API throttles, connection limits, and
AZ/instance capacity. Forecast normal, burst, deployment, and failure demand; request
increases early and test throttling/degradation. Quota dashboards without owners and
response actions are incomplete.

## Improve sustainability through efficiency

Remove idle resources, increase utilization, choose efficient managed services and
hardware where appropriate, minimize unnecessary movement and copies, apply data
lifecycle, and match availability to actual need. Measure useful work per resource;
do not trade away required reliability, security, or accessibility for an isolated
efficiency metric.
