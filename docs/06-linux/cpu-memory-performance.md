# CPU and Memory Reasoning

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-07**

## Start with the symptom

“The host is slow” is not a diagnosis. Define the affected journey, time window,
hosts, requests, and latency component. Then ask whether work waits for CPU,
memory reclaim, storage, network, locks, or a downstream dependency.

## CPU and scheduling

CPU time is divided among user work, kernel work, interrupt handling, virtual
machine steal time, idle time, and I/O wait accounting. Meanings vary slightly
by tool and kernel, so state what a metric represents before acting on it.

### Load average

Linux load average includes runnable tasks and tasks in certain uninterruptible
states. It is not CPU utilization. Interpret it with:

- logical CPU count and per-CPU imbalance;
- run-queue depth and duration;
- uninterruptible tasks and storage latency;
- CPU quotas, affinity, and cgroup throttling;
- virtualization steal or provider-side symptoms.

### CPU failure patterns

| Evidence | Possible hypotheses | Next distinction |
| --- | --- | --- |
| High user CPU and run queue | Demand, hot loop, expensive runtime work | Expected throughput or regression? One process or fleet-wide? |
| High system CPU | Syscall, networking, filesystem, or kernel overhead | Which kernel path and workload change correlate? |
| High steal time | Hypervisor contention or scheduling | Guest-wide or provider/host-specific? |
| Low CPU with high latency | I/O, lock, queue, dependency, or quota wait | Process state, pressure, trace, and downstream evidence |
| One CPU saturated | Single-thread bottleneck, affinity, interrupt concentration | Thread and per-CPU view |

## Virtual memory

Each process sees a virtual address space mapped to physical memory or backing
storage. Resident memory, anonymous memory, shared mappings, page cache, kernel
memory, and reclaim behavior all matter.

Low “free” memory is normal when otherwise unused memory improves filesystem
cache. Better questions are:

- Is available memory falling?
- Is reclaim consuming CPU and latency?
- Is swap activity sustained and harmful?
- Are major faults rising?
- Is one process or cgroup growing unexpectedly?
- Is the kernel approaching or invoking OOM behavior?
- Is memory pressure correlated with customer latency?

## Swap is not automatically failure

Swap can preserve infrequently used anonymous pages and protect useful cache.
The risk is sustained paging or reclaim that causes latency and throughput loss.
Interpret swap capacity separately from swap-in/swap-out activity and pressure.

## OOM reasoning

An out-of-memory kill can result from global memory exhaustion, a cgroup limit,
allocation constraints, or policy. Determine:

1. which scope ran out of memory;
2. which process was selected and why;
3. whether a limit, leak, traffic increase, or workload shape changed;
4. what customer work was lost or duplicated;
5. whether restart creates another allocation spike;
6. whether capacity, limits, admission, or application behavior must change.

Increasing memory may restore service but does not explain unbounded growth.

## Pressure Stall Information

Pressure metrics measure time in which tasks are delayed because CPU, memory,
or I/O resources are unavailable. They complement utilization by showing the
impact of contention. Use sustained windows and correlate them with application
latency; avoid alerting on every short burst.

## cgroup limits and containers

A host may have free memory while a workload hits `memory.max`, or spare CPU
while a cgroup is throttled by quota. Always inspect both host and workload
scope. Resource requests, limits, and autoscaling signals can interact to create
repeated throttling or OOM cycles.

## Performance method

1. Establish the workload and customer symptom.
2. Compare an affected period with a healthy baseline.
3. Check demand, errors, utilization, saturation, and limits.
4. Segment by process, thread, cgroup, CPU, host, zone, and version.
5. Form one hypothesis and predict what evidence would confirm it.
6. Apply one reversible mitigation.
7. Verify customer recovery and resource-pressure reduction.
8. Capture a profile or deeper trace only when overhead and data sensitivity are controlled.

## Anti-patterns

- Tuning scheduler or VM parameters before identifying the bottleneck.
- Alerting on CPU percentage without latency, queue, or throughput context.
- Treating cached memory as unavailable capacity.
- Disabling swap universally without understanding workload and failure behavior.
- Raising cgroup limits without checking node capacity and noisy-neighbor risk.
- Capturing unrestricted profiles or dumps that may contain sensitive data.
