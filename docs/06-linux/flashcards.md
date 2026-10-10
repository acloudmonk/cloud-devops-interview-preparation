# Linux Active-Recall Flashcards

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Use each prompt without viewing the cue. Mark it known only when you can explain
the mechanism, failure implication, and safe next question.

| Prompt | Answer cue |
| --- | --- |
| Why can load rise without high CPU? | Uninterruptible waits, runnable imbalance, quotas, or locks can contribute; correlate states and pressure |
| Why is low free memory not enough to diagnose pressure? | Page cache is reclaimable; inspect available memory, reclaim, faults, swap activity, and PSI |
| Why can a container OOM while the node has memory? | The cgroup can hit its own `memory.max` or allocation scope |
| What does sustained PSI reveal? | Work is being delayed by resource contention, even if utilization looks moderate |
| Why is a restart not root cause? | It clears state and may destroy evidence without explaining why the state formed |
| What makes readiness truthful? | It represents ability to serve admitted work, including only dependencies required for that decision |
| How can restart policy amplify an outage? | Repeated initialization, allocation, dependency traffic, or side effects add load |
| Why can deleting a log fail to free space? | The process may still hold an open descriptor to the unlinked inode |
| What else can exhaust besides disk bytes? | Inodes, quota, IOPS, throughput, queue, metadata, and provider burst limits |
| Why treat read-only remount as a data-risk signal? | It may follow filesystem/device errors; forcing writes can worsen corruption |
| What proves a backup strategy? | Successful, measured restore of consistent data within RTO/RPO |
| Why does parent-directory permission matter? | Entry creation/deletion is an operation on the directory namespace |
| Capabilities versus root? | Capabilities split privileges but can still provide powerful escalation paths |
| Why can managed access fail? | Agent, guest health, identity, endpoints, network, and provider service are dependencies |
| What belongs in break-glass design? | Tested path, approval, limited duration/scope, attribution, audit, and review |
| Why can a VM be running but unavailable? | Control plane, guest OS, service, dependency, and customer path are different layers |
| When is replacement preferable? | Stateless/image-driven host, safe drain, spare capacity, and no unique evidence/state |
| When is repair justified? | Unique state/evidence, replacement violates RTO, or systemic defect would recreate failure |
| What is configuration drift? | Actual host state diverges from declared and reviewed desired state |
| How should a fleet patch roll out? | Trusted image, validation, canary, progressive gates, drain, removal, inventory verification |
| What is the first performance comparison? | Affected versus healthy time/host/version/failure domain under comparable demand |
| Why segment per CPU or device? | Aggregate averages hide hot single resources and imbalance |
| What is a falsifiable hypothesis? | It predicts specific evidence that can confirm or reject a proposed cause |
| What makes mitigation safe? | Authorized, reversible, bounded blast radius, preserves invariants and recovery evidence |
| What follows service recovery? | Reconcile unfinished work, measure objective, capture evidence, and prevent recurrence |

Review missed cards after one day, three days, and seven days.
