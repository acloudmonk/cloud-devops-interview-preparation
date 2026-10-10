# Container Security Hardening

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

Container security spans source and build, registry, runtime configuration, host
kernel, network, data, identity, and operations. A small image helps, but it cannot
compensate for a mounted engine socket or an overprivileged workload role.

## Threat paths

Consider attackers controlling source, a dependency/base image, build context,
builder, registry account, deployment configuration, application input, or host.
Trace what each can reach: credentials, signing identity, cache, internal network,
host devices/files, cloud metadata, control-plane APIs, and customer data.

## Build-time controls

- Isolate untrusted builds from privileged networks, credentials, and writable cache.
- Use build-secret/SSH mounts rather than build arguments or copied credential files.
- Pin and review base/dependency sources; generate provenance and SBOM.
- Keep the context minimal and scan Dockerfile/build configuration for unsafe paths.
- Separate build identity from registry publication and production deployment.
- Protect the builder image and verify all material inputs, not only application source.

## Runtime least privilege

- Run as a dedicated non-root numeric UID/GID and prevent privilege escalation.
- Drop all Linux capabilities, then add only justified capabilities.
- Apply the platform's default or stricter seccomp profile and AppArmor/SELinux policy.
- Use a read-only root filesystem plus narrowly scoped writable mounts.
- Avoid privileged mode, host PID/IPC/network, host devices, and broad bind mounts.
- Never mount the Docker/container-runtime socket into ordinary workloads.
- Set CPU, memory, PID, file-descriptor, and ephemeral-storage limits.
- Restrict ingress and egress; give each workload a least-privilege cloud identity.

Running as non-root is necessary for many workloads but not sufficient. A non-root
process with a dangerous capability, writable host path, runtime socket, or excessive
cloud role can still compromise the environment.

## Secrets and cloud identity

Do not bake secrets into images, labels, environment defaults, or build history.
At runtime, retrieve them through an authorized secret-delivery mechanism and keep
scope, rotation, revocation, audit, and failure behavior explicit. Environment
variables can leak through diagnostics, child processes, or crash reports; file or
agent delivery also needs permissions and cleanup.

On ECS, distinguish task role (application AWS permissions) from task execution role
(agent actions such as image pulls/log delivery). On EKS, use workload identity such
as IAM roles for service accounts or the current EKS mechanism rather than node-wide
credentials. Fargate reduces host management but does not fix application, image,
identity, network, or data permissions.

## Host and tenancy

Patch the kernel, runtime, and node image; minimize installed host services; protect
metadata and management endpoints; monitor runtime behavior; and rebuild nodes from
known configuration. Place hostile or high-impact workloads across stronger tenant
boundaries—separate accounts, clusters, node groups, or sandboxed/microVM runtimes—as
risk requires.

## Detection and response

Collect image digest, runtime configuration, workload identity, node/task identity,
process execution, network flow, filesystem changes, cloud audit, and deployment
events with appropriate privacy/retention. Alert on unexpected shells/tools,
privilege changes, sensitive mounts, unusual egress, cryptomining/resource patterns,
and drift from approved configuration.

For compromise: isolate without destroying evidence, revoke reachable identities,
block the digest, identify every running/pulled copy, replace from known-good inputs,
patch the root cause, and verify customer/data impact. Restarting the same digest on
the same trust boundary is not remediation.
