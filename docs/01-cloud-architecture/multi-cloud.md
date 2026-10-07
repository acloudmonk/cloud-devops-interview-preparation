# Multi-Cloud Translation Guide

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-04**

Level: **Advanced / Architect**

AWS is the implementation baseline for this module. Azure and Google Cloud are
mapped by capability and semantics so that service names do not replace design
reasoning.

## Capability map

| Capability | AWS reference | Microsoft Azure | Google Cloud |
| --- | --- | --- | --- |
| Global DNS | Route 53 | Azure DNS + Traffic Manager | Cloud DNS |
| Edge, CDN, WAF | CloudFront + AWS WAF | Front Door + WAF | Global external Application Load Balancer + Cloud CDN + Cloud Armor |
| Managed containers | ECS on Fargate | Container Apps | Cloud Run |
| Kubernetes option | EKS | AKS | GKE |
| API management | API Gateway | API Management | API Gateway / Apigee |
| Key-value operational store | DynamoDB | Cosmos DB | Firestore or Bigtable; Spanner for relational consistency |
| Queue/load leveling | SQS | Service Bus queues | Pub/Sub |
| Workflow/saga | Step Functions | Durable Functions or Logic Apps | Workflows |
| Event routing | EventBridge | Event Grid | Eventarc |
| Secrets | Secrets Manager | Key Vault | Secret Manager |
| Native observability | CloudWatch + X-Ray | Azure Monitor + Application Insights | Cloud Monitoring + Cloud Trace |
| Managed chaos | Fault Injection Service | Chaos Studio | Validate current product support; use controlled application or Kubernetes experiments where appropriate |

## Differences that affect architecture

### Containers are not interchangeable

ECS on Fargate is a task-and-service scheduler, while Container Apps and Cloud
Run expose more application-platform behavior. Compare request duration,
scale-to-zero, background processing, networking, concurrency, deployment
revisions, and identity before choosing. EKS, AKS, and GKE are closer conceptual
matches when Kubernetes APIs and ecosystem portability are required.

### Messaging semantics differ

SQS, Service Bus, and Pub/Sub can all decouple producers and consumers, but
their ordering, sessions, deduplication, delivery attempts, dead-lettering,
visibility/acknowledgement, retention, and scaling controls differ. Design the
consumer for the documented delivery contract; do not assume exactly-once
business processing from a product label.

### Database labels hide consistency choices

DynamoDB, Cosmos DB, Firestore, Bigtable, and Spanner have different data
models, transaction boundaries, consistency options, partition behavior, and
multi-region conflict models. Start with access patterns and invariants. For the
ticket lab, the decisive capability is an atomic, conditional transition of a
seat plus an idempotency strategy.

### Global networking uses different abstractions

CloudFront, Front Door, and Google Cloud's global load-balancing stack package
origin selection, WAF, caching, TLS, private connectivity, and health behavior
differently. Test partial failures and origin bypass rather than drawing a
single generic "global load balancer" box.

### Identity is the portable control plane

Use workload identity and short-lived federation on every cloud:

- AWS IAM roles and GitHub Actions OIDC;
- Microsoft Entra workload identity / managed identities;
- Google Cloud Workload Identity Federation and service accounts.

Static access keys are not a multi-cloud strategy.

## Translation exercise

For an Azure or Google Cloud implementation, create a decision record containing:

1. the required capability and invariant;
2. the candidate service and its delivery/consistency contract;
3. limits, quotas, region availability, and recovery behavior;
4. identity, network, logging, and encryption integration;
5. the load and failure test that validates the choice;
6. switching and exit costs.

The goal is not three identical deployments. The goal is equivalent business
behavior with known platform-specific trade-offs.
