# Resilience and Performance

[← Data ownership and consistency](data-consistency.md) · [Next: Security and identity →](security-identity.md)

## End-to-end budgets

Allocate latency, availability, and retry budgets across the critical journey.
Set deadlines at ingress and propagate remaining time. A local service meeting its
own SLO can still make the customer journey fail through serial dependencies.

## Failure controls

- timeouts shorter than the caller's remaining deadline;
- retries only for transient, safe-to-repeat work at one deliberate layer;
- exponential backoff, jitter, maximum attempts, and retry budgets;
- circuit breaking with tested recovery and meaningful fallback;
- bulkheads by tenant, dependency, priority, or workload class;
- bounded queues, concurrency, rate limits, admission control, and load shedding;
- graceful degradation that preserves core correctness.

Retries amplify overload and can repeat side effects after timeout-after-success.
Use business idempotency keys and persistent result lookup, not only transport retry.

## Capacity and performance

Model fan-out, payload, connection pools, database limits, broker partitions, queue
age, downstream quotas, and cold starts. Scale on the bottleneck and protect scarce
dependencies. Load tests should include realistic request mixes, skew, failures,
retries, cache-cold behavior, and recovery—not only steady average throughput.

## Isolation and cells

Partition tenants or workloads into cells when blast-radius reduction justifies
duplication and routing complexity. Multi-AZ compute does not remove regional,
identity, data, deployment, or dependency common modes. Define degraded behavior
before adding multi-region complexity.

## Resilience proof

Test dependency latency, partial responses, message duplicates, consumer lag,
quota exhaustion, service discovery errors, and recovery from backlog. Observe
customer outcomes and state correctness, not only process availability.
