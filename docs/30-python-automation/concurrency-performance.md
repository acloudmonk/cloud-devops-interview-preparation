# Concurrency and Performance

[← Reliability](reliability-idempotency.md) · [Next: Testing →](testing-verification.md)

Concurrency increases throughput and blast radius. Start sequentially, measure, then
add the smallest bounded model that meets the objective.

| Work | Likely model | Primary risk |
| --- | --- | --- |
| simple low-volume calls | synchronous loop | slow but understandable |
| blocking I/O with sync SDK | bounded thread pool | shared state, quota bursts |
| many native async I/O calls | asyncio | cancellation and blocking code in event loop |
| CPU-heavy transformation | process pool/batch compute | serialization, memory, startup |
| durable distributed work | queue/workflow workers | duplicates, leases, poison items |

## Safety controls

Set global and per-service concurrency, rate limit, queue depth, deadlines, and memory
budgets. Use backpressure rather than unbounded task creation. Protect shared state or
avoid it; never share a non-thread-safe client accidentally. Preserve item identity
and result regardless of completion order.

## Cancellation and shutdown

Stop accepting work, signal cancellation, let atomic units finish or checkpoint,
release resources, flush evidence, and return partial status. A timeout does not prove
remote cancellation. Query outcome before retrying ambiguous requests.

## Performance method

Measure end-to-end throughput, p50/p95/p99 latency, throttle/error rate, memory, CPU,
connection pools, provider quota, and cost. Batch only where service semantics support
partial results and item-level retry. Optimize API calls and algorithms before syntax.

## Interview trap

The Global Interpreter Lock is not a universal “threads are useless” rule: threads
can help blocking I/O, processes help CPU-bound work, and async helps compatible I/O.
The operating limit is often the remote service, not Python.
