# Resilience and Operations

[← Processing state and replay](processing-state-replay.md) · [Next: Security and governance →](security-governance.md)

## Retry taxonomy

Classify transient dependency failure, throttling, consumer bug, invalid schema,
business rejection, missing prerequisite, and permanent authorization failure. Retry
only likely-transient classes with exponential backoff, jitter, bounded attempts, and
an end-to-end budget. Immediate retries across many consumers create amplification.

## Dead-letter handling

A DLQ is quarantine, not resolution. Preserve original destination, ID, payload or
claim, failure class, attempt count, first/last failure times, consumer version, and
trace context. Alert on arrival and age, restrict access, provide inspect/fix/re-drive
workflow, and prove the corrected record reaches business convergence. DLQs require
retention and capacity management too.

## Observability

Measure publish success and latency, broker storage and availability, ingress/egress,
queue depth, oldest age, partition lag and skew, consumer throughput/error/latency,
retry and DLQ rate, outbox age, schema rejection, rebalance, replay progress, and
business completion. Propagate trace context but use links where fan-out or batching
breaks a simple parent-child model.

## Freshness and correctness SLOs

Broker uptime is not the user outcome. Define time from authoritative commit to
consumer effect or projection visibility, plus tolerated loss, duplication, and stale
state. Alert on burn and business backlog. A stable queue depth can still violate
freshness if old records remain blocked behind poison or partition skew.

## Incident sequence

Protect correctness, stop unsafe producers or consumers, bound retry load, preserve
broker and offset evidence, and identify affected message classes and business
entities. Restore controlled flow, reconcile state, re-drive selectively, communicate
impact, then fix contract, capacity, code, or runbook. Purging a queue to make a graph
green is data loss unless explicitly authorized by business policy.

## Broker and region recovery

Define acknowledged-write durability, replication failure behavior, RPO/RTO, consumer
offset recovery, destination metadata, schema registry, keys, and DNS/network cutover.
Active-active publishing needs conflict, duplicate, and order rules. Test regional
recovery while consumers are lagging and external effects are partially complete.

## Cost controls

Model requests, throughput units, partitions, brokers, storage/retention, replication,
cross-zone/region egress, schema services, connectors, observability, and replay.
Batching and compression reduce cost but affect latency, memory, and failure scope.
Retain only the history justified by recovery, audit, analytics, or product value.
