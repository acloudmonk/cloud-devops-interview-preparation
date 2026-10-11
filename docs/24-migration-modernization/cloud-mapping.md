# AWS-First Multi-Cloud Capability Map

[← Modernization and value](modernization-value.md) · [Next: Design exercise →](design-exercise.md)

Use this as a discovery aid, not a promise of feature equivalence. Verify current
Regions, quotas, protocols, service tiers, pricing, migration paths, and support.

| Need | AWS-first capability | Azure direction | Google Cloud direction | Portable consideration |
| --- | --- | --- | --- | --- |
| Portfolio discovery | Migration Evaluator, Application Discovery Service, Migration Hub | Azure Migrate | Migration Center | CMDB, network telemetry, interviews |
| Governance foundation | Organizations, Control Tower, IAM Identity Center, SCPs | Landing zones, Management Groups, Policy, Entra ID | Landing zone, resource hierarchy, Organization Policy, Cloud Identity | Policy as code and federated identity |
| Server migration | Application Migration Service | Azure Migrate: Server Migration | Migrate to Virtual Machines | Images/config automation; validate drivers/licenses |
| VMware relocation | VMware Cloud on AWS patterns | Azure VMware Solution | Google Cloud VMware Engine | Vendor lifecycle, network, license, exit |
| Database movement | DMS, SCT and service-native replication | Azure Database Migration Service | Database Migration Service | Native replication/CDC and reconciliation |
| Bulk/edge transfer | DataSync, Transfer Family, Snow Family | Storage Mover, Data Box | Storage Transfer Service, Transfer Appliance | Encrypt, inventory, chain of custody |
| Containers/platform | EKS, ECS, App Runner, Lambda | AKS, Container Apps, Functions | GKE, Cloud Run, Cloud Functions | Kubernetes/OCI where justified |
| Observability | CloudWatch, CloudTrail, Config, X-Ray | Azure Monitor, Activity Log, Policy | Cloud Monitoring, Cloud Logging, Cloud Audit Logs | OpenTelemetry and portable SLOs |
| Security posture | Security Hub, GuardDuty, Inspector | Defender for Cloud | Security Command Center | Common control objectives and evidence |
| Backup/recovery | AWS Backup, service-native recovery | Azure Backup/Site Recovery | Backup and DR, service-native recovery | Isolated copies and tested restoration |
| Cost governance | Cost Explorer, Budgets, CUR, Compute Optimizer | Cost Management, Advisor | Cloud Billing, Recommender | FinOps allocation and unit metrics |

## Translation questions

For every mapped capability ask: Does it preserve semantics and control objectives?
Who operates it? What data and identity cross boundaries? What are limits, failure
modes, recovery, export, skills, and total cost? What evidence demonstrates readiness?

## Multi-cloud migration posture

Do not split workloads across providers merely to claim portability. Choose placement
from business, regulatory, latency, ecosystem, acquisition, resilience, and skills
requirements. Standardize principles and evidence while allowing provider-specific
implementation. Design connectivity, identity, DNS, observability, incident ownership,
data authority, and cost allocation across the whole transition.
