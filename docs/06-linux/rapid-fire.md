# Linux Rapid-Fire Revision

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-07**

Answer each in 30–60 seconds. Give a definition, operational consequence, and
one condition that changes the answer.

## Processes and services

1. **Process versus thread?** A process owns an address space and resource context; threads share much of it but are independently schedulable.
2. **What is PID 1 responsible for?** Early user-space lifecycle, service orchestration, signal/reaping behavior, and system state.
3. **Zombie process?** Exited child whose parent has not collected status; growth indicates parent lifecycle failure.
4. **Uninterruptible sleep?** Kernel wait, commonly I/O; persistent counts can indicate device or filesystem delay.
5. **Why are sockets file descriptors?** Linux exposes many I/O resources through descriptor handles and common operations.
6. **Graceful shutdown?** Stop admission, drain bounded work, persist/reconcile state, then exit before forced termination.
7. **`After=` versus `Requires=`?** Ordering versus dependency; neither proves application readiness.
8. **Why can restart loops worsen failure?** They repeat initialization, connection, allocation, and side effects while hiding a stable failed state.
9. **Liveness versus readiness?** Liveness asks whether replacement may be needed; readiness asks whether traffic should be sent now.
10. **Why can service “active” be misleading?** The process may not be ready, correct, reachable, or able to serve dependencies.

## CPU and memory

1. **Load average?** Average runnable plus selected uninterruptible tasks; not CPU percentage.
2. **Utilization versus saturation?** Busy proportion versus work waiting because capacity is constrained.
3. **High latency with low CPU?** Check I/O, locks, downstream waits, quotas, pools, and single-thread/per-CPU bottlenecks.
4. **Steal time?** Guest-visible time CPU was unavailable due to hypervisor scheduling; correlate with provider/fleet evidence.
5. **Why can free memory be low on a healthy host?** Linux uses otherwise idle memory for useful cache.
6. **Available memory?** Estimate of memory usable without harmful swapping, more relevant than free alone.
7. **Major page fault?** Required page content was not resident and needed backing-store I/O.
8. **Is swap always bad?** No; sustained paging and pressure are the concern, not allocated swap alone.
9. **Global versus cgroup OOM?** Whole-system memory exhaustion versus a workload-specific limit or scope.
10. **PSI value?** Measures time tasks are stalled by CPU, memory, or I/O contention and complements utilization.

## Storage and filesystems

1. **Bytes free but writes fail?** Check inodes, quota, read-only mount, permissions, descriptors, and the actual target filesystem.
2. **Deleted file still uses space?** An open descriptor retains the underlying inode and blocks until closed.
3. **IOPS versus throughput?** Operation count versus bytes per time; request size and latency shape which limit matters.
4. **Queue depth?** Outstanding I/O; interpret with device parallelism and latency.
5. **Why use stable mount identifiers?** Device names can change across boot or attachment order.
6. **Snapshot versus backup?** A snapshot is point-in-time storage state; a backup includes recoverability, retention, isolation, and restore proof.
7. **Crash-consistent versus application-consistent?** Storage-time coherence versus coordinated application transaction state.
8. **Read-only remount response?** Protect data, inspect kernel/device evidence, and follow documented offline repair or restore.
9. **Why test restore?** Backup success does not prove usable data or achievable RTO/RPO.
10. **Root filesystem design concern?** Logs/temp growth can break OS and access; separate, bound, rotate, and alert.

## Security and access

1. **Directory execute permission?** Allows traversal/search; it differs from listing and entry creation.
2. **What governs deletion?** Parent directory permissions and policy, not primarily target file write permission.
3. **`umask`?** Removes permissions from creation defaults; it does not retroactively change existing objects.
4. **Linux capability?** A split privilege formerly associated with root; still grant only what is required.
5. **Why not recursive `777`?** It destroys least privilege without identifying the subject, object, operation, or policy layer.
6. **SELinux/AppArmor denial response?** Confirm expected behavior and policy context; do not disable the control as diagnosis.
7. **Managed session advantage?** Central identity and reduced inbound access, with agent/IAM/network/service dependencies.
8. **Break-glass access?** Tested, approved, time-bounded emergency privilege with attribution and review.
9. **Secret in process arguments?** It may appear in process inspection, audit, or support output; use safer delivery.
10. **Support-bundle risk?** It can contain identities, network data, environment, logs, keys, and customer information.

## Cloud operations and judgment

1. **VM running versus healthy?** Control-plane lifecycle does not prove guest boot, service readiness, or customer success.
2. **AWS system versus instance check?** Platform/host reachability versus guest-level responsiveness; neither proves application correctness.
3. **Repair versus replace?** Choose from state, evidence, automation, capacity, RTO, and systemic-defect risk.
4. **Immutable fleet benefit?** Repeatability and lower drift; it still needs image security, rollout, and state externalization.
5. **Canary patch gate?** Representative readiness, customer SLI, resource, error, and security signals before expansion.
6. **First incident question?** Which customer journey is failing, since when, and across which scope?
7. **Why compare a healthy peer?** It controls for workload and environment and narrows material differences.
8. **When is reboot acceptable?** Urgent reversible mitigation when impact outweighs evidence loss and recovery consequences are understood.
9. **What verifies recovery?** Customer outcome plus resource/queue normalization and reconciliation of interrupted work.
10. **Principal-level close?** State impact, evidence, mitigation, remaining risk, owner, validation, and next decision.
