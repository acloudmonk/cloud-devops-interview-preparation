# Design Exercise: Governed AWS Container Platform

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

Use this no-code exercise to convert container mechanics into an architect-level
design. Complete it on paper or in a Markdown note.

## Brief

A company will migrate 35 Java, Node.js, and Python services from long-lived EC2
instances to containers. GitHub Actions publishes to Amazon ECR. Workloads include
public APIs, asynchronous workers, scheduled jobs, a licensed stateful component,
and an untrusted customer-code processor.

Current problems:

- images use `latest`, are rebuilt in every environment, and average 1.8 GB;
- Dockerfiles copy the entire repository, including local configuration;
- most containers run as root with no resource limits;
- production tasks share one broad AWS role and unrestricted egress;
- logs and uploads are written to the container layer;
- health checks restart services when a shared database is slow;
- teams cannot explain base-image ownership, patching, or rollback retention;
- x86 and ARM workers receive the same untested tag.

Constraints: AWS is primary, recovery time for bad releases is ten minutes, customer
code requires a stronger isolation boundary, two regions are required, and the
organization has not yet selected ECS or EKS.

## Your deliverable

Draw and explain:

1. source, builder, registry, runtime, workload, network, data, and cloud-identity
   trust boundaries;
2. image standards for context, base images, multi-stage builds, non-root runtime,
   platform manifests, and runtime configuration;
3. immutable ECR promotion and evidence from source to deployed digest;
4. ECS/Fargate versus ECS/EC2 versus EKS decision by workload—not fashion;
5. task/pod identity, ingress/egress, security-group/policy, secret, and mount controls;
6. CPU, memory, PID, storage, startup, readiness, liveness, and termination contracts;
7. state placement, backups, restore proof, logging, and upload handling;
8. stronger isolation for customer-controlled code;
9. observability, incident evidence, regional continuity, and registry outage behavior;
10. adoption stages, developer experience, controls, measures, and exception expiry.

## Decision matrix

| Decision | State your choice and trade-off |
| --- | --- |
| Orchestration | ECS/Fargate, ECS/EC2, EKS, or workload-specific combination |
| Base-image program | Owners, approved families, update signal, rebuild objective |
| Artifact identity | Tag/digest policy, signing/provenance, scanning, retention |
| Runtime boundary | Non-root, capabilities, profiles, host access, tenant separation |
| Networking | Endpoint/discovery, ingress, egress, TLS, policy, observability |
| State | Ephemeral, EFS/EBS/S3/database, consistency, backup, restore |
| Resources/health | Placement capacity, limits, checks, shutdown, autoscaling signal |
| Recovery | Bad image, compromised image, region/registry outage, data impact |

## Evidence matrix

For source revision, base digest, build identity, output digest, SBOM, scan,
signature/provenance, runtime configuration, deployment, and recovery, record the
producer, trusted identity, storage, consumer, retention, and failure behavior.

## Adoption plan

A defensible sequence is inventory; define image/runtime standards; establish base
image ownership; pilot immutable ECR promotion; introduce workload-specific IAM;
move state/logs out of writable layers; set measured resources and lifecycle probes;
enforce build/runtime policy; then migrate service cohorts and high-risk isolation.

For every increment name a pilot, owner, success metric, exception path and expiry,
and process rollback. Do not migrate all services or choose Kubernetes merely to
signal maturity.

## Review rubric

- **Artifact:** one reviewed digest and evidence set is promoted.
- **Isolation:** kernel, identity, filesystem, network, data, and tenant boundaries
  match risk.
- **Operability:** resource, health, signal, state, and debugging contracts are explicit.
- **Recovery:** triggers, authority, actions, retention, and verification are testable.
- **Portability:** OCI invariants are separated from AWS/platform-specific behavior.
- **Adoption:** standards improve safety without creating an unusable golden path.

Finish with a two-minute recommendation: context, top risks, platform choices,
migration, recovery, measures, and the first decision required from leadership.
