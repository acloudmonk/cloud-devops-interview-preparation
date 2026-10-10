# Container Mental Model

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

A container is an ordinary operating-system process started with isolation and
resource controls. It does not contain a guest kernel. This fact explains its fast
startup, density, host-kernel dependency, and much of its security model.

## System boundaries

| Term | Responsibility |
| --- | --- |
| Image | Immutable content-addressed filesystem and runtime configuration |
| Container | Runtime instance of an image plus writable state and isolation configuration |
| Registry | Distribution, identity, metadata, access, and lifecycle for image content |
| Engine/manager | Builds, image lifecycle, networks, volumes, and containers |
| High-level runtime | Pull/unpack images, manage lifecycle, snapshots, and integration |
| OCI runtime | Create the isolated process from an OCI runtime bundle/specification |
| Kernel | Enforce namespaces, cgroups, capabilities, filesystems, networking, and syscalls |
| Orchestrator | Schedule, reconcile, expose, scale, update, and recover workloads |

Docker commonly uses containerd, which invokes an OCI runtime such as `runc`.
Alternatives can implement the same standards with different trust and operating
models. Docker is not the definition of a container, and Kubernetes is not a
container runtime.

## From image to process

```mermaid
flowchart LR
    A[Registry manifest] --> B[Platform manifest]
    B --> C[Content layers]
    C --> D[Merged root filesystem]
    D --> E[OCI runtime configuration]
    E --> F[Isolated host process]
    F --> G[Network, mounts, limits, identity]
```

The registry digest identifies content. Pulling resolves the manifest for the
requested operating system and architecture, verifies content, unpacks layers,
and prepares a snapshot. The runtime then asks the host kernel to start a process
with the requested namespaces, mounts, credentials, capabilities, limits, and
security profile.

## OCI responsibilities

The OCI Image Specification defines image manifests, indexes, configuration, and
layer layout. The Distribution Specification defines registry interactions. The
Runtime Specification defines the bundle and process configuration used to create
a container. The standards provide interoperability boundaries; they do not make
all engines, platforms, or security defaults identical.

## Containers versus virtual machines

| Dimension | Container | Virtual machine |
| --- | --- | --- |
| Kernel | Shares host kernel | Runs guest kernel |
| Isolation boundary | OS process and kernel controls | Hypervisor and virtual hardware |
| Startup/density | Usually faster and denser | Usually heavier |
| OS compatibility | Must match kernel family/architecture | Guest OS can differ from host |
| Security decision | Strong process isolation when hardened; kernel remains shared | Often stronger workload boundary |

Managed platforms may add a microVM or sandbox around containers. AWS Fargate
abstracts the worker boundary, while ECS on EC2 and EKS expose more host choices.
The application is still packaged as a container, but tenancy, kernel, and
operational responsibility differ.

## Desired invariants

- The deployed image is addressed by immutable digest.
- The container has one clear foreground lifecycle and handles termination.
- Writable state is intentional, bounded, and recoverable.
- Identity, network, filesystem, syscall, and resource access are least privilege.
- Build-time content and runtime configuration are traceable.
- Health signals represent the workload, not merely a running process.

## Interview test

When somebody says “the container crashed,” ask which layer failed: image
resolution, unpack, runtime creation, entrypoint, application, health check,
resource control, host kernel, network, storage, or orchestrator decision.
