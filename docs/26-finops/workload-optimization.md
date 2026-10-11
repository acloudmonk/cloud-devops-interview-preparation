# Workload and Architecture Optimization

[← Module overview](index.md) · [Planning and anomalies](planning-anomalies.md)

Usage optimization changes what and how much technology is consumed. It should
remove waste or improve efficiency while preserving explicit reliability,
security, performance, compliance, and delivery constraints.

## Optimization sequence

1. Confirm the business outcome, owner, architecture, SLOs, and demand pattern.
2. Establish total and unit-cost baselines with quality guardrails.
3. Remove resources with no valid owner or purpose through a safe quarantine process.
4. Schedule non-production and elastic work around actual need.
5. Right-size compute, memory, storage, database, and data-processing configuration.
6. Improve autoscaling, bin packing, caching, compression, retention, and data movement.
7. Select a more appropriate managed service, architecture, Region, or purchase model.
8. Validate technical and financial results; update standards and automation.

## Architecture cost drivers

- Compute: utilization shape, licensing, accelerators, idle baseline, scaling delay.
- Storage: capacity, requests, performance tier, copies, snapshots, retention, retrieval.
- Databases: instance/compute, I/O, storage, replicas, backup, licensing, and data transfer.
- Network: cross-zone, cross-Region, internet egress, NAT, load balancing, and inspection.
- Observability: signal volume, cardinality, retention, indexing, sampling, and queries.
- Resilience: redundancy, standby capacity, replication, backup, testing, and recovery.

Avoid local optimizations that increase total cost—for example, cheaper compute
that increases licenses, egress, latency, engineering work, or incident exposure.

## AWS-first controls

Use Cost Optimization Hub and AWS Trusted Advisor as evidence inputs, not automatic
authority. Combine recommendations with CloudWatch/workload metrics, SLOs, seasonality,
deployment schedules, and owner context. Evaluate Graviton, Spot, serverless,
storage classes, lifecycle policies, database modernization, and network topology
according to workload compatibility and total migration cost.

## Safe remediation

Require ownership, change records, backups where needed, canary or staged rollout,
rollback, observation window, and realized-savings validation. For idle resources,
quarantine or snapshot before deletion when recovery value justifies it. Expire
temporary exceptions and prevent recurrence through platform defaults and policy.

## Value over minimum spend

An intentional cost may buy lower latency, higher conversion, rapid experimentation,
resilience, security, or reduced engineering load. The goal is to make that trade
visible and approved—not to force every workload toward the lowest bill.

Return to the [module overview](index.md) when ready to continue.
