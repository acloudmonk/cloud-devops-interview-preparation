# Docker and Container References and Videos

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last verified: **2026-10-10**

Prefer specifications and official platform documentation for behavior that changes.
The module teaches durable mental models; verify current defaults, limits, feature
support, and service availability before implementation.

## OCI and container foundations

- [Open Container Initiative](https://opencontainers.org/)
  — governance and the image, runtime, and distribution specification boundaries.
- [OCI specifications](https://specs.opencontainers.org/)
  — current normative image, runtime, and distribution releases.
- [containerd documentation](https://containerd.io/docs/)
  — image transfer/storage, execution, supervision, snapshots, and runtime integration.
- [runc repository and documentation](https://github.com/opencontainers/runc)
  — OCI runtime implementation, security advisories, and release behavior.
- [Linux namespaces](https://man7.org/linux/man-pages/man7/namespaces.7.html),
  [cgroups v2](https://docs.kernel.org/admin-guide/cgroup-v2.html), and
  [capabilities](https://man7.org/linux/man-pages/man7/capabilities.7.html)
  — operating-system mechanisms behind container isolation and resource control.

## Docker build and runtime

- [Docker build overview](https://docs.docker.com/build/)
  — BuildKit, cache, exporters, multi-stage, and multi-platform workflows.
- [Building best practices](https://docs.docker.com/build/building/best-practices/)
  — base images, context, cache, package installation, users, and Dockerfile guidance.
- [Dockerfile reference](https://docs.docker.com/reference/dockerfile/)
  — exact instruction, shell/exec form, mount, variable, and build-check behavior.
- [Multi-stage builds](https://docs.docker.com/build/building/multi-stage/)
  — stage boundaries and copying selected build outputs.
- [Multi-platform builds](https://docs.docker.com/build/building/multi-platform/)
  — image indexes, emulation, native nodes, cross-compilation, and platform arguments.
- [Build secrets](https://docs.docker.com/build/building/secrets/)
  — ephemeral secret and SSH mounts that avoid image-layer persistence.
- [Docker Engine security](https://docs.docker.com/engine/security/)
  — daemon attack surface, namespaces, cgroups, and capabilities.
- [Rootless mode](https://docs.docker.com/engine/security/rootless/)
  — daemon and container execution in a user namespace plus prerequisites/limitations.
- [Seccomp security profiles](https://docs.docker.com/engine/security/seccomp/)
  — default syscall policy and profile customization.
- [Docker networking](https://docs.docker.com/engine/network/)
  and [storage](https://docs.docker.com/engine/storage/)
  — drivers, port publication, volumes, bind mounts, and writable layers.

## AWS container anchor

- [Amazon ECS best practices guide](https://docs.aws.amazon.com/AmazonECS/latest/bestpracticesguide/intro.html)
  — architecture, security, networking, autoscaling, observability, and operations.
- [ECS container-image best practices](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/container-considerations.html)
  — image completeness, process lifecycle, tagging, and task grouping.
- [ECS task and container security](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security-tasks-containers.html)
  — minimal images, scanning, privileges, capabilities, filesystems, and limits.
- [IAM roles for Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security-iam-roles.html)
  — task, task-execution, infrastructure, instance, and service-linked role boundaries.
- [Fargate task networking](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-task-networking.html)
  — task ENIs, VPC routing, DNS, flow visibility, image pulls, and role behavior.
- [Fargate task storage](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-task-storage.html)
  — image and ephemeral-storage allocation and visibility.
- [Amazon ECR tag mutability](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-tag-mutability.html)
  — immutable/mutable tag policy and current exclusion behavior.
- [Amazon ECR image scanning](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html)
  — basic/enhanced scanning configuration and finding lifecycle.
- [Amazon ECR image signing](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-signing.html)
  and [verification](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-signing-verification.html)
  — managed/manual signing, reference artifacts, and deployment verification.

## Security and multi-cloud translation

- [NIST SP 800-190: Application Container Security Guide](https://csrc.nist.gov/pubs/sp/800/190/final)
  — image, registry, orchestrator, container, and host threat/control guidance.
- [Kubernetes container security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/)
  — relevant runtime, workload, policy, and supply-chain checks for the next module.
- [Azure Container Apps security](https://learn.microsoft.com/azure/container-apps/security)
  — managed identities, secrets, network boundaries, and platform responsibilities.
- [Azure Container Registry best practices](https://learn.microsoft.com/azure/container-registry/container-registry-best-practices)
  — registry geography, authentication, image management, and security.
- [Google Cloud Run container runtime contract](https://cloud.google.com/run/docs/container-contract)
  — supported image/platform, listener, filesystem, signals, resources, and sandbox behavior.
- [Google Artifact Registry container images](https://cloud.google.com/artifact-registry/docs/docker)
  — repository access, image formats, authentication, and lifecycle.

## Videos

- [AWS re:Invent 2024 — Building event-driven architectures using Amazon ECS with AWS Fargate](https://www.youtube.com/watch?v=-oXkuy_21BI)
  — official AWS session connecting Fargate tasks with queues, events, workflow, and
  fault-tolerant processing. Validate details against current service documentation.
- [AWS Fargate: Are serverless containers right for you?](https://www.youtube.com/watch?v=Vtymod0nPBo)
  — decision-oriented AWS session; use for concepts and confirm current capabilities
  and pricing separately.

Official channels for newer material:

- [Docker](https://www.youtube.com/@Docker)
- [AWS Events](https://www.youtube.com/@AWSEventsChannel)
- [Cloud Native Computing Foundation](https://www.youtube.com/@cncf)
- [Microsoft Developer](https://www.youtube.com/@MicrosoftDeveloper)
- [Google Cloud Tech](https://www.youtube.com/@googlecloudtech)

## Books

- Nigel Poulton, *Docker Deep Dive*
- Liz Rice, *Container Security*
- Sean P. Kane and Karl Matthias, *Docker: Up & Running*
- Justin Garrison and Kris Nova, *Cloud Native Infrastructure*

Check edition, publication date, and supported runtime/platform versions before
purchasing or following command examples.

## Suggested reading order

1. OCI boundaries, namespaces, cgroups, and capabilities
2. Docker build, Dockerfile, multi-stage/platform, secret, network, and storage docs
3. ECS image/security/IAM/network/storage and ECR lifecycle documentation
4. NIST security guide and Azure/Google platform contracts
5. Official talks and selected book chapters for design and operational depth
