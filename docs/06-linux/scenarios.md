# Linux Scenario Questions and Model Answers

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-07**

Answer each prompt aloud before reading the model answer. Structure the response
as symptom → scope → hypotheses → evidence → mitigation → verification → prevention.

## 1. Load average is 40, but CPU is only 35%

**Model answer:** Load includes runnable tasks and tasks in certain
uninterruptible states, so I would not scale CPU from that number alone. I would
compare logical CPU count, run queue, process states, I/O pressure, disk latency,
cgroup throttling, and the customer latency window. Persistent uninterruptible
tasks would shift the hypothesis toward storage, filesystem, or device waits.

**Follow-up:** What changes if only one CPU is saturated?

## 2. Free memory is near zero

**Model answer:** Low free memory can reflect useful page cache. I would inspect
available memory, reclaim, major faults, swap activity, pressure, process/cgroup
growth, and customer latency. If memory is stable without pressure, no action may
be needed. If reclaim or OOM risk is rising, I would constrain admission or the
offending workload and investigate the growth source before adding capacity.

**Follow-up:** When is swap helpful rather than harmful?

## 3. A worker was killed during peak traffic

**Model answer:** I would determine exit code and whether the kill came from the
global OOM killer, a cgroup limit, systemd timeout, operator, or deployment
controller. I would preserve kernel and unit evidence, quantify interrupted
work, stop unsafe restart loops, and verify idempotent recovery. The permanent
fix may be a leak correction, a right-sized limit, admission control, or capacity.

**Follow-up:** Why can the host have free memory during a cgroup OOM?

## 4. The root filesystem is full

**Model answer:** I would identify the mount, byte and inode use, growth rate,
writer, and deleted-but-open files. I would stop unsafe growth and free only
approved data with retention ownership. After customer recovery, I would fix
rotation, quotas, partitioning, capacity, and alerts. Broad deletion or an
unplanned restart could destroy evidence or critical data.

**Follow-up:** Why might deleting a large log not release space?

## 5. systemd reports active, but the load balancer marks the host unhealthy

**Model answer:** Active proves lifecycle state, not readiness. I would test the
readiness path locally, listener address/port, dependencies, credentials,
firewall/network path, and load-balancer health-check contract. I would remove
the instance from service while preserving evidence and correct readiness so it
reflects the ability to serve representative work.

**Follow-up:** What should readiness do during a temporary dependency failure?

## 6. A service repeatedly restarts

**Model answer:** I would inspect exit reason, restart count, start-limit events,
configuration, dependencies, permissions, and resource limits before raising
the restart threshold. The loop may amplify load or duplicate work. I would
stop admission or isolate the instance, correct the triggering failure, and use
bounded restart with alerting and a truthful failure state.

**Follow-up:** When is automatic restart appropriate?

## 7. SSH is unavailable on one EC2 instance

**Model answer:** I would separate client/DNS/network/IAM issues from guest boot,
sshd, disk, CPU, or firewall failures. I would compare EC2 system and instance
status, fleet scope, serial output, and managed-session availability. For a
replaceable stateless host, draining and replacing may be safest; unique state
or evidence may justify serial or offline-volume recovery.

**Follow-up:** What if every host from one image has the same symptom?

## 8. Disk latency rises while throughput remains modest

**Model answer:** Throughput is only one dimension. I would inspect request size,
IOPS, queue depth, latency distribution, sync/metadata workload, filesystem
events, per-process I/O, cloud-volume limits, and burst behavior. One hot device
or latency-sensitive synchronous workload can fail before aggregate throughput
looks high.

**Follow-up:** Why is device `%util` not a universal saturation measure?

## 9. An application cannot write despite free disk space

**Model answer:** I would check the actual mount, inodes, read-only remount,
quota, directory permissions/ACLs, security-module denial, file-descriptor
limits, and application identity. “Free space” may describe the wrong
filesystem and does not cover these other constraints.

**Follow-up:** Which permission controls file deletion?

## 10. A patch is urgent but requires reboot

**Model answer:** I would assess exploitability and compensating controls, build
or patch a known image, validate boot/readiness/telemetry, canary across a small
failure domain, expand with SLO gates, and drain old hosts. I would verify that
no vulnerable instances remain. In-place patching needs equivalent rollout,
rollback, and drift controls.

**Follow-up:** When would live patching be insufficient?

## 11. One host is slow after deployment

**Model answer:** I would compare version, configuration, placement, workload,
process/cgroup limits, and resource pressure with a healthy peer. If isolated,
I would drain it and preserve targeted evidence; if the new version correlates,
I would stop rollout or rollback. Replacement is mitigation, while the
comparison identifies whether the defect is host-specific or systemic.

**Follow-up:** What evidence proves rollback worked?

## 12. A process has thousands of file descriptors

**Model answer:** I would compare the count with limits and baseline, classify
descriptor types, identify growth rate and ownership, and check connection or
file lifecycle. Raising the limit may defer failure but can move exhaustion to
system memory, ports, or a downstream service. Correct the leak or bound concurrency.

**Follow-up:** Why are sockets also file descriptors?

## 13. Logs contain authentication tokens

**Model answer:** I would restrict access, stop further exposure through safe
redaction or rollback, rotate affected credentials, determine collection and
retention scope, and follow incident/privacy procedures. Then I would add
structured allow-list logging, tests, scanning, and retention controls. I would
not copy the tokens into another incident system.

**Follow-up:** What other diagnostic artifacts may contain secrets?

## 14. A filesystem remounts read-only

**Model answer:** I would treat this as a data-integrity signal, check kernel and
device errors plus cloud-volume health, stop unsafe writes, and preserve state.
I would follow the filesystem’s documented offline repair or restore procedure,
or replace the host if state is external. Blindly remounting read-write can
worsen corruption.

**Follow-up:** How do you verify application consistency afterward?

## 15. Should production engineers have root SSH?

**Model answer:** I would start from required tasks, not a universal yes/no.
Routine operations should use centralized identity, least-privilege roles,
managed automation, and attributable sessions. Break-glass privilege needs
approval, short duration, audit, tested access when normal tooling fails, and
post-use review. Shared keys and permanent unrestricted accounts are poor controls.

**Follow-up:** What dependencies does a managed-session service introduce?

## Scoring guide

Score each answer from 0 to 4.

| Score | Evidence |
| ---: | --- |
| 0 | Guesses or proposes a dangerous action without evidence |
| 1 | Names a familiar command or cause only |
| 2 | Checks several relevant signals and suggests a plausible mitigation |
| 3 | Scopes impact, tests hypotheses, mitigates safely, and verifies recovery |
| 4 | Adds failure boundaries, security, unfinished-work reconciliation, ownership, and prevention |

An average of 3 is a strong senior signal. Tool names do not increase the score
unless the answer explains the question each tool answers.
