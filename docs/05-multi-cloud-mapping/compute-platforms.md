# Compute, Containers, and Serverless

[← Networking](networking.md) · [Next: Data platforms →](data-platforms.md)

| Capability | AWS | Azure | Google Cloud |
| --- | --- | --- | --- |
| Virtual machines | EC2 | Virtual Machines | Compute Engine |
| Managed VM fleet | Auto Scaling groups | Virtual Machine Scale Sets | Managed instance groups |
| Kubernetes | EKS | AKS | GKE |
| Managed containers | ECS/Fargate, App Runner | Container Apps | Cloud Run |
| Functions | Lambda | Azure Functions | Cloud Run functions |
| Batch | AWS Batch | Azure Batch | Batch |

These are candidate families. Compare OS/runtime control, protocol, duration, state,
scale-to-zero, cold start, concurrency, accelerators, networking, storage, isolation,
deployment, quota, skill, and cost.

Kubernetes provides a common API but not identical clusters: identity, load balancers,
storage classes, node lifecycle, upgrades, observability, policy, and integrations
remain provider-specific. Portable containers do not make state and operations portable.

Serverless defaults and limits differ. For every platform, model downstream connection
budgets, retry/idempotency, maximum scale, regional scope, private networking, startup,
and failure-mode capacity. Choose the least complex platform satisfying the workload;
do not select the lowest common denominator solely for theoretical portability.
