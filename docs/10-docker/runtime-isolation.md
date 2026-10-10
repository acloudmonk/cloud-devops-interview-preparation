# Runtime Isolation and Resource Control

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

Container isolation is composed from kernel mechanisms and runtime policy. No
single namespace, flag, or “runs as non-root” statement defines the security or
performance boundary.

## Namespace views

- **PID:** separate process-number view; the first process has special lifecycle
  responsibilities.
- **Mount:** independent mount table and root filesystem view.
- **Network:** interfaces, addresses, routes, ports, and firewall context.
- **IPC:** System V IPC and POSIX message-queue isolation.
- **UTS:** hostname/domain-name view.
- **User:** maps container user/group IDs to different host IDs.
- **Cgroup/time:** additional resource-tree and clock views where supported.

Namespaces limit visibility; they are not authorization by themselves. Mounting a
host socket or filesystem, using host networking/PID, or adding powerful
capabilities can cross the intended boundary.

## Cgroups and resource behavior

Cgroups account for and constrain CPU, memory, process count, and I/O. Understand
the distinction between request/reservation and hard limit at the orchestrator
layer. CPU throttling, memory reclaim, OOM termination, and host pressure produce
different symptoms.

- CPU quota limits usable time and may cause latency without high application CPU.
- Memory includes heap, page cache, native allocations, stacks, and runtime overhead.
- OOM selection may kill a container process or another process depending on scope.
- PID limits contain fork bombs and reveal thread/process leakage.
- Ephemeral-storage limits protect nodes from logs or writable-layer growth.

On ECS, task/container CPU and memory semantics differ between EC2 and Fargate.
On Kubernetes, requests affect scheduling and limits affect runtime. Translate the
invariant: placement capacity, contention policy, hard boundary, measurement, and
failure behavior.

## Identity and capabilities

Container UID 0 is privileged inside its namespace and can become dangerous when
combined with capabilities, devices, mounts, sockets, or kernel vulnerabilities.
Run as a purpose-built non-root UID/GID, drop capabilities by default, add only the
specific capability required, and use user namespaces or rootless execution where
compatible.

Rootless mode reduces daemon and container privilege but has trade-offs in ports,
networking, storage drivers, cgroups, and performance. It complements rather than
replaces kernel patching, seccomp, mandatory access control, and workload isolation.

## PID 1 and lifecycle

The initial process must receive/forward termination signals and reap orphaned
children. Shell-form commands can insert a shell that fails to forward signals.
Prefer exec-form commands and use a minimal init only when the workload needs it.

Shutdown must fit the platform grace period: stop accepting work, drain or
checkpoint, finish bounded operations, close resources, and exit. Test termination
under load.

## Runtime contract

Define image digest/platform; entrypoint/arguments; UID/GID and capabilities;
seccomp/AppArmor/SELinux profile; read-only root filesystem; CPU, memory, PID,
storage, and file-descriptor budgets; mounts, devices, sockets, network/egress;
health behavior; and graceful termination. This contract belongs in reviewed
platform configuration, not undocumented operator knowledge.
