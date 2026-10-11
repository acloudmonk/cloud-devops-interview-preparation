# Identity, Security, and Keys

[← Governance](governance.md) · [Next: Locations and resilience →](locations-resilience.md)

| Capability | AWS | Azure | Google Cloud |
| --- | --- | --- | --- |
| Workforce federation | IAM Identity Center / external IdP | Microsoft Entra ID | Cloud Identity/Workspace with external IdP |
| Workload identity | IAM roles, STS, IRSA/EKS Pod Identity | Managed identities, workload identity federation | Service accounts, Workload Identity Federation |
| Secrets | Secrets Manager / Parameter Store | Key Vault | Secret Manager |
| Key management | KMS / CloudHSM | Key Vault / Managed HSM | Cloud KMS / Cloud HSM |
| Posture/threat hub | Security Hub, GuardDuty | Defender for Cloud, Sentinel | Security Command Center, Google SecOps |

Federate one authoritative workforce identity lifecycle, but translate authorization
into least-privilege native roles. Avoid shared users and long-lived access keys,
client secrets, or service-account keys. Separate human, delivery, runtime, emergency,
and security-investigation identities.

Common policy intent does not imply identical enforcement. Map resource scope,
conditions, explicit deny behavior, privileged activation, token audience/lifetime,
service agents, and data-plane authorization. Test effective access in every provider.

For keys, define ownership, separation of duties, region, rotation, availability,
disable/delete recovery, audit, and emergency operation. Customer-managed keys add a
dependency whose failure must be included in RTO.
