# Compute, Containers, Serverless, and App Platforms

[← Networking](networking-edge.md) · [Next: Data platforms →](data-platforms.md)

| Platform | Strong fit | Main responsibility retained |
| --- | --- | --- |
| Compute Engine/MIG | OS control, legacy, specialized hardware | Images, OS, runtime, scaling |
| GKE | Kubernetes ecosystem and portable orchestration | Workloads, cluster choices, upgrades |
| Cloud Run | Stateless HTTP/event containers and jobs | Container, concurrency, downstream safety |
| Cloud Run functions | Bounded event/function handlers | Limits, retries, dependencies |
| App Engine | Opinionated managed web applications | Runtime constraints and configuration |

Select from protocol, state, duration, latency, scale shape, isolation, accelerator,
network, storage, deployment, portability, skill, quota, and cost requirements.

Managed instance groups need health checks, update policy, distribution, capacity, and
state separation. GKE needs release/version, node, identity, network policy, disruption,
autoscaling, and observability decisions. Cloud Run concurrency and maximum instances
must protect downstream connections. Serverless retries require idempotency.

Use trusted images, Artifact Registry, provenance and vulnerability evidence, immutable
promotion, progressive rollout, and rollback. Separate build, deployment, and runtime
identities. Test cold starts, zone loss, quota, dependency latency, and rollback.
