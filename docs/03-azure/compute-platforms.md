# Compute, Containers, Serverless, and App Platforms

[← Networking and edge](networking-edge.md) · [Next: Data platforms →](data-platforms.md)

## Choose from workload behavior

Assess OS/runtime control, compatibility, duration, state, concurrency, latency, demand,
scaling, isolation, deployment, portability, hardware, licensing, networking, storage,
observability, skill, and cost. Prefer the simplest responsibility boundary meeting the
need; do not move every workload to AKS or Functions by default.

## Virtual machines and scale sets

Azure VMs offer host-level control; Virtual Machine Scale Sets manage groups of VMs
with scaling and upgrade policies. Design images, managed identities, disks, placement,
Availability Zones/sets, health, load balancing, patching, extensions, instance repair,
capacity, quotas, graceful lifecycle, and recovery. Extensions and custom scripts can
be hidden availability and security dependencies.

## Containers

AKS supplies managed Kubernetes control-plane capabilities while customers retain node,
add-on, policy, workload, and upgrade responsibilities according to configuration.
Azure Container Apps offers managed container applications with revisions and event-
driven scaling; Azure Container Instances suits simpler isolated container execution.
Compare orchestration, control, networking, identity, storage, scale, GPU, portability,
operations, limits, and skills.

## App Service and Functions

App Service hosts web apps and APIs with managed runtime plans, deployment slots, scale,
network integration, and platform features. Azure Functions handles event-driven
execution across hosting plans. Design plan capacity, cold start, duration, concurrency,
triggers, retries, idempotency, networking, secrets, deployment, observability, and
downstream budgets. “Serverless” does not mean no SKU or quota decisions.

## Deployment and capacity

Choose rolling, slot swap, canary, blue/green, or revision-based release with health,
telemetry, compatibility, rollback, and data-change coordination. Model steady, burst,
deployment, and zone-failure demand, plus SNAT ports, IPs, database connections, quotas,
and Regional/SKU capacity. Autoscaling cannot repair a hard downstream limit.
