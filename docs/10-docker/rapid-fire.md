# Container Engineering Rapid-Fire Revision

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

Answer each in 30–60 seconds with a definition, failure mode, and condition that
changes the design.

## Architecture and image model

1. **Container?** Host process started with namespaces, cgroups, mounts, credentials, and runtime policy—not a lightweight VM.
2. **Image?** Immutable content-addressed filesystem layers plus runtime configuration.
3. **OCI image index?** Manifest pointing to platform-specific image manifests under one reference.
4. **Container engine?** User-facing build/image/network/volume/container management; not the kernel isolation itself.
5. **High-level versus OCI runtime?** Lifecycle/snapshots/integration versus creating the isolated process from a bundle.
6. **Layer?** Immutable filesystem change addressed as content; later deletion can hide but not erase earlier bytes.
7. **Writable layer?** Container-lifecycle copy-on-write state, normally unsuitable for durable data.
8. **Tag versus digest?** Mutable human name versus immutable manifest content identity.
9. **`EXPOSE`?** Image metadata describing intended port; it does not listen or publish.
10. **Container versus VM?** Shared host kernel and OS isolation versus guest kernel behind virtual hardware/hypervisor.

## Build and registry

1. **Build context?** Files available to the builder; minimize with `.dockerignore` to reduce leaks and cache churn.
2. **Multi-stage build?** Build/test in rich stages and copy only runtime outputs to the final stage.
3. **Cache invalidation?** A step reruns when its instruction or material inputs change; keys must represent every input.
4. **Build secret?** Ephemeral mount/input unavailable to final layers/history, not `ARG` or copied file.
5. **Hermetic build?** Declared controlled inputs without undeclared environment/network dependence.
6. **Reproducible build?** Same declared inputs/process can yield equivalent output.
7. **Base-image pin?** Stable digest plus update ownership; it freezes content but does not prove safety.
8. **Build once?** Promote one verified digest; do not rebuild independently for environments.
9. **SBOM?** Component/relationship inventory, not a vulnerability verdict or integrity proof.
10. **Signature/provenance limit?** Trust depends on authorized uncompromised identity, builder, policy, and complete claims.

## Runtime and security

1. **Namespace?** Kernel mechanism giving a process a scoped view of resources such as PIDs, mounts, or networking.
2. **Cgroup?** Resource accounting/control boundary for CPU, memory, PIDs, I/O, and related resources.
3. **Capability?** Split unit of Linux root privilege; drop all then add only justified units.
4. **Seccomp?** System-call filtering; reduces kernel attack surface but is not full authorization.
5. **Rootless?** Engine/container operation without host root; reduces privilege with compatibility/performance trade-offs.
6. **Non-root limit?** Helpful but unsafe mounts, capabilities, sockets, devices, or cloud role can remain critical.
7. **Read-only root?** Prevent root filesystem writes; provide narrow controlled writable mounts for legitimate paths.
8. **Docker socket risk?** Usually equivalent to host control through privileged container creation and host mounts.
9. **ECS task role?** AWS permissions for application code, separate from the execution role used by the agent.
10. **Fargate security value?** AWS manages host boundary; workload image, identity, network, data, and app risks remain.

## Network, storage, and lifecycle

1. **Bridge network?** Namespace linked to host bridge, often using NAT/port publication for external access.
2. **Host network?** Shared host network namespace; fewer translation layers but weaker port/network isolation.
3. **Container DNS test?** Query from actual namespace and verify resolver, name, answer/TTL, route, policy, and listener.
4. **Bind mount?** Direct host path exposure with portability, permission, and host-compromise risks.
5. **Volume?** Managed persistent path whose backup, ownership, topology, and migration still require design.
6. **`tmpfs`?** Memory-backed ephemeral mount; fast and non-persistent but counts toward memory pressure.
7. **PID 1 duty?** Receive/forward signals and reap child processes; exec form usually preserves lifecycle intent.
8. **Startup versus readiness?** Has initialization completed versus can this instance receive intended traffic now?
9. **Liveness?** Is restart likely to restore this instance—not whether every shared dependency is healthy.
10. **Graceful stop?** Remove readiness/traffic, handle SIGTERM, drain bounded work, release resources, exit before kill.

## Troubleshooting and architecture judgment

1. **Exit 137?** Often SIGKILL; confirm OOM or forced termination using platform/kernel evidence.
2. **Exit 127?** Command or interpreter not found; inspect entrypoint, PATH, shebang, and platform.
3. **CPU throttle symptom?** Latency with quota exhaustion even when host/dashboard CPU appears low.
4. **OOM analysis?** Cgroup events/current/peak plus heap, native memory, page cache, workload, and host pressure.
5. **Minimal-image debugging?** Authorized ephemeral diagnostic container/namespace entry and external telemetry, not permanent shell bloat.
6. **ECS Fargate choice?** Low host operations and task isolation, balanced against supported features, sizes, and cost.
7. **ECS EC2 choice?** More host/runtime/capacity control with greater patching, isolation, and scaling responsibility.
8. **EKS choice?** Kubernetes ecosystem/portability/control where its platform complexity is justified.
9. **Compromised digest response?** Isolate, revoke identities, block/find every copy, rebuild from trusted inputs, verify impact.
10. **Principal-level close?** Workload constraints, boundary decisions, evidence, recovery, adoption, measures, owner, next decision.
