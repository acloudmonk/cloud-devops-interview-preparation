# Identity, Security, and Data Protection

[← Enterprise platform](enterprise-platform.md) · [Next: Networking and edge →](networking-edge.md)

## Separate identity planes

Microsoft Entra roles govern directory capabilities; Azure RBAC governs Azure resources.
Federate workforce access, require strong authentication and Conditional Access, use
Privileged Identity Management for just-in-time privilege, protect emergency-access
accounts, separate duties, and review access. Tenant design affects collaboration,
acquisitions, B2B, policy, support, and isolation.

## Give workloads identities

Prefer system- or user-assigned managed identities for Azure workloads and workload
identity federation for external CI/CD or Kubernetes scenarios. Avoid client secrets
and certificates where federation/managed identity works. Scope RBAC narrowly, protect
federated subject/issuer/audience rules, and monitor service principals, consent,
credential changes, and dormant privileges.

## Protect data and keys

Classify and minimize data; encrypt transport and storage; use platform-managed,
customer-managed, or customer-provided keys only when requirements justify the added
responsibility. Design Key Vault/Managed HSM authorization, network access, soft delete,
purge protection, rotation, backup/recovery, Region, quota, and administration. A lost
or denied key can make healthy data unavailable.

## Manage posture, detection, and response

Defender for Cloud provides posture and workload protection capabilities; Microsoft
Sentinel can provide SIEM/SOAR; Azure Monitor, Activity Log, Policy, Resource Graph,
network logs, and service diagnostics supply evidence. Define scope, connectors,
retention, routing, triage, automation, incident roles, and cross-tenant visibility.
Tools without coverage and response ownership do not create security.

## Apply shared responsibility precisely

Responsibilities change across VMs, AKS, App Service, Functions, databases, and SaaS.
Record ownership for identities, configuration, network, code/runtime, images, patching,
data, keys, logging, backup, vulnerabilities, incidents, compliance, and supplier risk.
Validate control effectiveness rather than treating Azure certification as workload
compliance.
