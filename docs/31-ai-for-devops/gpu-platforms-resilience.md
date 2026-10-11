# GPU Platforms and Resilience

[← Observability, cost, and sustainability](observability-cost.md) · [Next: Enterprise design exercise →](design-exercise.md)

## Managed API or self-hosted inference

Managed model APIs reduce capacity, serving, patching, and lifecycle work.
Self-hosting may be justified by model control, customization, predictable scale,
data constraints, latency, or economics. It introduces accelerator procurement,
drivers, runtime compatibility, serving, scheduling, scaling, and model security.

## Inference platform concerns

- match model precision and memory footprint to accelerator type;
- separate online latency-sensitive and batch throughput workloads;
- use queues, admission control, dynamic batching, and bounded concurrency;
- monitor first-token and inter-token latency, throughput, utilization, memory,
  queue time, eviction, errors, and cost per successful request;
- package immutable model/runtime artifacts and verify provenance;
- isolate tenants and prevent untrusted code from sharing sensitive accelerators;
- drain safely and test node and Availability Zone replacement.

AWS choices include Bedrock for managed inference and SageMaker AI, EKS, or EC2
accelerators for greater control. Azure Machine Learning/AKS and Vertex AI/GKE map
to similar capabilities, but quotas, supply, networking, and serving differ.

## Resilience and portability

Multi-AZ application tiers do not guarantee model capacity. Decide whether to keep
warm capacity, route to another evaluated model or Region, queue work, or degrade
to retrieval and human support. Protect scarce accelerators with priority and load
shedding; retries can amplify overload. Use stable application contracts and an
explicit capability matrix, without hiding valuable native controls behind a
lowest-common-denominator abstraction.
