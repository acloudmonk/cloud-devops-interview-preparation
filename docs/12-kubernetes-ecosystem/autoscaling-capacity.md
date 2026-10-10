# Autoscaling and Capacity Control Loops

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

Scaling is a chain of delayed control loops: demand becomes a metric or event backlog,
workload replicas/resources change, unschedulable demand appears, nodes/cloud capacity
change, and downstream systems absorb new concurrency. Optimize the whole chain.

## Scaling layers

| Layer | Examples | Decision |
| --- | --- | --- |
| Workload horizontal | HPA | Desired replicas from resource/custom/external metrics |
| Workload vertical | VPA | Resource recommendations or request changes, often with restart |
| Event driven | KEDA and similar | Replicas/jobs from queue/event/external scaler state |
| Node/capacity | Cluster Autoscaler, Karpenter, managed modes | Provision/consolidate nodes for Pod requirements |
| Cloud/service | Load balancer, queue, database, quotas | Capacity outside Kubernetes must support the result |

## Metric contract

Define demand signal, unit, source, freshness, aggregation, missing-data behavior,
target meaning, readiness filtering, update period, stabilization, min/max, ownership,
and business guardrail. CPU is useful only when it correlates with capacity demand.
Queue depth without arrival rate, processing time, age, and downstream capacity can
produce unstable scaling.

External metrics create an availability dependency. Decide fail-open/last-value/
minimum behavior, authentication, rate limits, cardinality, and how the scaler avoids
overloading the source.

## Interacting loops

HPA and VPA can conflict if both change CPU/memory signals and targets without a
supported mode. Event scaling and HPA can fight over replicas. Node consolidation can
evict Pods while workload scaling changes demand. GitOps may revert autoscaler-written
fields if ownership is unclear.

Map which controller owns replicas, requests, node selection/capacity, and disruption.
Use stabilization/cooldowns, compatible recommendations, PDBs, topology, priority,
and explicit ignored/owned fields. Test response to a step increase and decrease.

## Node provisioning

Cluster Autoscaler scales predefined node groups. Dynamic provisioners such as
Karpenter can choose instance types/capacity from Pod requirements. Managed modes may
own more of the node lifecycle. Compare startup time, bin packing, availability-zone
and purchase options, constraints, quotas, disruption/consolidation, special hardware,
daemon overhead, images, security, and operating burden.

On EKS, EC2 capacity, subnet/IP availability, service quotas, AMI/bootstrap, add-ons,
labels/taints, architecture, zones, and interruption handling are dependencies. Cheap
spot capacity is not capacity until interruption, fallback, and workload tolerance are designed.

## Reliability guardrails

Maintain minimum serving/recovery capacity, rollout and zone-loss headroom, priority
for critical/system workloads, max replica/cost/downstream bounds, backpressure and
load shedding, idempotent workers, termination/draining, and forecast/scheduled capacity
for known events. Autoscaling does not replace capacity testing.

## Measures and troubleshooting

Measure queue/demand age, metric delay, desired/actual/ready replicas, pending duration,
node provision/start time, unschedulable reason, scale-limit events, throttling/OOM,
downstream saturation, interruption, consolidation savings/disruption, cost per useful
work, and customer objectives.

When scaling fails, trace demand → metric → adapter/scaler → desired replicas →
scheduler → node provisioner/cloud → readiness → traffic/work → downstream. Adding a
second autoscaler without fixing the broken link creates more controllers, not capacity.
