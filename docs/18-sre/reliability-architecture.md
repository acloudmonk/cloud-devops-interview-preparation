# Reliability Architecture and Risk

[← Module overview](index.md) · [Module 01: Architecture](../01-cloud-architecture/index.md)

Reliability architecture connects business promises to failure modes, dependency
behavior, capacity, detection, mitigation, and recovery. Redundancy helps only
when replicas do not share the failure and failover is correct and tested.

## Quantitative reasoning

- For independent serial dependencies required for success, approximate end-to-end
  availability by multiplying component availability.
- Parallel redundancy can improve availability only when failover, shared control
  planes, data, configuration, identity, network, quotas, and operators do not
  create common-mode failure.
- Mean time between failures and mean time to restore summarize history but can
  hide impact distribution and are not promises.
- Recovery time objective and recovery point objective express restoration time
  and tolerable data loss; actual recovery capability must be exercised.

State independence assumptions. Availability percentages alone do not describe
correctness, latency, durability, safety, affected users, or correlated regional events.

## Failure-mode analysis

For each critical flow, identify component/dependency, failure mode, cause,
user effect, detection, prevention, containment, fallback, recovery, owner, and
validation. Prioritize by impact, likelihood/exposure, detectability, recovery
difficulty, and uncertainty rather than generating an unowned risk register.

## Resilience patterns

Use timeouts, bounded retries with jitter, idempotency, circuit breakers, load
shedding, bulkheads, queues, backpressure, graceful degradation, caching, redundancy,
autoscaling, and tested failover according to failure semantics. Retries can
amplify overload; caches can serve stale or unauthorized data; queues can hide
growing latency; fallbacks can silently corrupt business outcomes.

## AWS-first architecture

- Isolate workloads and environments across accounts; use multiple Availability
  Zones for failures the service and data model can tolerate.
- Select Regional/multi-AZ managed-service features deliberately and understand
  their control-plane, quota, backup, and failover behavior.
- Use Elastic Load Balancing, Route 53/Global Accelerator, Auto Scaling, queues,
  and health-based routing where the workload semantics fit.
- Monitor quotas and capacity, automate recovery, protect deployment and recovery
  roles, and validate backups with restoration—not job completion alone.
- Use Resilience Hub and Well-Architected reviews as inputs, not substitutes for
  workload-specific analysis and exercises.

Azure equivalents include Availability Zones, scale sets, Front Door/Traffic
Manager, Service Bus, Backup/Site Recovery, and Chaos Studio. Google Cloud maps
to zonal/regional services, managed instance groups, Cloud Load Balancing, Pub/Sub,
Backup and DR, and fault-injection/testing capabilities. Provider SLAs describe
provider commitments, not end-to-end application reliability.

## Multi-region decision

Add a region only when business/recovery needs justify data consistency, deployment,
identity, dependency, observability, testing, and operating complexity. Choose
active/active, active/passive, pilot light, or backup/restore from required user
behavior and data semantics. Untested multi-region architecture may create a
larger failure surface without reducing recovery time.

Return to the [module overview](index.md) when ready to continue.
