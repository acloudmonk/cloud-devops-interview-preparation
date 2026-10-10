# Docker and Container Engineering Scenarios

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

Answer aloud before reading the model answer. Identify the exact digest and platform,
lifecycle stage, namespace/cgroup boundary, customer impact, evidence, recovery, and
permanent control.

## 1. Container exits immediately with code 0

**Model answer:** Confirm the intended service command, image entrypoint/CMD,
overrides, and logs. A container lives while its foreground process lives; a daemon
may have backgrounded itself or a shell command may have completed. Correct the
exec-form foreground command, verify signals/health, rebuild, and redeploy by digest.

## 2. Works locally but fails on ARM production nodes

**Model answer:** Compare host/requested platform with the resolved manifest and
binaries. Stop the rollout; use a tested architecture-specific image or verified
multi-platform index. Build each target from controlled inputs, test natively where
needed, and expose platform identity in release evidence.

## 3. Image contains a deleted secret

**Model answer:** Revoke/rotate first and scope registry/cache/runtime exposure. A
later-layer deletion does not remove bytes from the earlier layer. Block and remove
the affected digest according to incident policy, rebuild from clean history/context
using secret mounts, and verify no logs, cache, attestations, or descendants leak it.

## 4. Container is repeatedly OOM-killed

**Model answer:** Protect traffic, confirm OOM evidence and cgroup scope, then compare
limit, working set, heap, native memory, page cache, concurrency, and node pressure.
Right-size or correct the leak with headroom; align language-runtime awareness and
alerts. A restart loop is containment, not a memory strategy.

## 5. CPU is low but latency is high

**Model answer:** Inspect cgroup CPU throttling, quota/period, run queue, node
contention, I/O waits, locks, downstream latency, and request concurrency. Host or
dashboard percentages may hide quota exhaustion. Adjust code, capacity, requests/
limits, and scaling using service objectives rather than remove limits blindly.

## 6. Service is reachable on host but not from another container

**Model answer:** Test from the failing namespace; verify application bind address,
container port, network membership, DNS endpoint, route, policy/firewall, published
mapping, and return path. `EXPOSE` is metadata and host success proves neither
container DNS nor policy. Correct the narrow boundary and retest TLS/application.

## 7. Persistent data disappears after replacement

**Model answer:** Stop writes and establish whether data lived in the writable layer,
anonymous/named volume, bind mount, or external service. Recover from the actual
backing store/backup if possible. Move business state to an owned durable service or
volume with topology, access, backup, restore testing, and replacement semantics.

## 8. Non-root container cannot write its mounted path

**Model answer:** Inspect effective UID/GID, host/volume ownership, user namespace,
mount flags, and SELinux/AppArmor labels. Fix ownership or platform provisioning for
the intended numeric identity; do not use `chmod 777` or return to root. Test on a
fresh mount and document the storage identity contract.

## 9. Health check creates a restart storm

**Model answer:** Pause rollout/restarts and separate application liveness from shared
dependency health. A database outage should usually remove readiness or degrade,
not kill every process. Add startup tolerance, bounded checks, failure thresholds,
dependency resilience, and external customer signals; verify recovery without surge.

## 10. Pulls fail despite a valid image tag

**Model answer:** Inspect registry/auth/token, repository policy, network/DNS/TLS,
rate limit, manifest platform, tag resolution, digest existence, and disk/unpack
capacity. Do not repush another image under the same tag. Restore the identified
dependency and deploy/pin the verified digest with pull observability.

## 11. Critical CVE has no vendor fix

**Model answer:** Determine affected component/version, reachability, exploit
conditions, exposure, privileges, and business impact. Reduce surface or disable the
feature, isolate, monitor, or replace the dependency/base where feasible. Record an
owned expiring exception and rebuild/rescan promptly when a trusted fix arrives.

## 12. A workload mounts the Docker socket

**Model answer:** Treat it as host-level control because the socket can create
privileged containers and mount host paths. Isolate the workload, revoke reachable
credentials, investigate daemon activity/images/containers, and replace the pattern
with a constrained build/service API or isolated builder without host socket access.

## 13. Graceful shutdown loses requests

**Model answer:** Trace load-balancer deregistration, readiness removal, SIGTERM
delivery/forwarding, application drain, connection/request duration, worker leases,
and grace timeout. Fix PID 1/exec form, stop new work before bounded completion,
coordinate platform timers, and test termination under representative load.

## 14. Image tag changed between regions

**Model answer:** Pause promotion, resolve actual digests per region, and choose one
approved digest based on evidence and compatibility. Restore or complete deployment
without rebuilding. Enforce immutable promotion/copy, digest-based definitions,
replication verification, and post-deploy identity checks.

## 15. Fargate cost increases after migration

**Model answer:** Segment cost by service/task size, utilization, architecture,
schedule, environment, storage/network/logging, and scaling behavior. Right-size
from percentiles and objectives, reduce idle replicas/startup overhead, consider ARM
after native testing, and compare ECS on EC2/EKS only with operating and capacity
risk—not compute price alone.
