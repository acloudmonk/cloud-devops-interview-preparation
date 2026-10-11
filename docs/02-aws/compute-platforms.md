# Compute, Containers, and Serverless

[← Networking and edge](networking-edge.md) · [Next: Data platforms →](data-platforms.md)

## Choose from workload behavior

Assess runtime and OS control, execution duration, state, concurrency, latency, demand
shape, scaling, isolation, deployment, portability, hardware, licensing, networking,
storage, observability, skill, and cost. Prefer the simplest responsibility boundary
that meets requirements; do not standardize every workload onto one runtime.

## EC2 and Auto Scaling

EC2 provides the most host-level control. Design immutable or controlled images,
instance profiles, metadata protection, patching, EBS, placement, load balancing,
Auto Scaling health, mixed instance policies, graceful lifecycle, capacity strategy,
and recovery. Multi-AZ Auto Scaling still depends on correct subnet capacity, quotas,
launch templates, dependencies, and application behavior.

## Containers

ECS integrates AWS-native orchestration; EKS provides Kubernetes APIs and ecosystem;
Fargate removes worker-node management for supported ECS/EKS workloads. Compare
control-plane and node responsibility, portability, density, startup, networking,
identity, storage, add-ons, upgrades, quotas, observability, and team expertise.

## Serverless and managed application runtimes

Lambda suits event-driven bounded execution; App Runner and other managed runtimes can
reduce platform work. Design concurrency, cold starts, time limits, payload limits,
retries, idempotency, destinations, VPC access, secrets, deployment, observability, and
cost. Reserved concurrency can protect dependencies as well as guarantee capacity.

## Capacity and deployment

Use horizontal scaling only when state and dependencies allow it. Model steady, burst,
and failure demand plus database connections and downstream quotas. Choose rolling,
blue/green, canary, immutable, or function-alias deployment with health, telemetry,
compatibility, rollback, and data-change coordination.
