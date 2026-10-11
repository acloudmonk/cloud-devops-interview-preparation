# Azure Architecture Decision Model

[← Module overview](index.md) · [Next: Global infrastructure and service scope →](global-infrastructure.md)

## Begin with the workload

Define users, business journeys, data, invariants, demand, latency, availability,
durability, RTO/RPO, security, compliance, residency, delivery, skills, support, and
economics. Separate mandatory qualities from preferences, then choose Azure services.
Do not infer requirements from an existing Microsoft license or favored product.

## Select the responsibility boundary

Compare managed services, platform services, containers, serverless, and VMs by control,
compatibility, scaling, patching, deployment, isolation, observability, recovery,
limits, portability, skill, and total cost. Azure manages more at higher abstraction,
but the customer retains responsibility for identity, data, configuration, architecture,
and appropriate use.

## Understand Azure Resource Manager scope

Model tenant, management group, subscription, resource group, and resource boundaries.
Know whether a service/resource is global, regional, zonal, or nonzonal and whether its
control plane differs from its data plane. Resource group location stores deployment
metadata and does not require every contained resource to share that location.

## Model service semantics

For each service, capture consistency, availability, scaling unit, quotas, maintenance,
deployment, network integration, identity, encryption, logging, backup, failure modes,
pricing dimensions, and dependencies. “Zone-redundant,” “global,” and “serverless” need
service-specific verification.

## Validate decisions with evidence

Use decision records, threat models, Azure pricing estimates, quota inventories, load
and failure tests, restore exercises, SLOs, deployment results, and cost allocation.
Record assumptions and triggers for reconsideration. A reference architecture is a
starting point, not proof that a workload meets its requirements.

## Azure decision record

Capture outcome, workload boundary, tenant/subscription/Region placement, services,
alternatives, identity and data authority, network paths, resilience, recovery,
observability, delivery, quotas, cost, shared responsibility, risks, owner, and evidence.
