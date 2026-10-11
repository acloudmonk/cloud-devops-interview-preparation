# Hierarchy, Landing Zones, and Governance

[← Decision model](concepts.md) · [Next: Identity and security →](identity-security.md)

| Concern | AWS | Azure | Google Cloud |
| --- | --- | --- | --- |
| Top enterprise scope | Organization | Microsoft Entra tenant | Organization |
| Policy grouping | Organizational units | Management groups | Folders |
| Primary workload boundary | Account | Subscription | Project |
| Lower grouping | Tags/resource constructs | Resource group | Resources/tags |
| Guardrails | SCPs, tag policies, Control Tower controls | Azure Policy, initiatives, landing zones | Organization Policy, tags |

These rows are conceptual, not one-to-one. An AWS account, Azure subscription, and
Google Cloud project differ in quotas, networking defaults, identity inheritance,
service enablement, billing, and lifecycle.

## Cross-cloud foundation

Define provider-native landing zones plus a shared enterprise control model for
identity federation, naming, ownership, data classification, cost allocation,
security evidence, exceptions, and decommissioning. Automate account/subscription/
project vending while retaining each provider's native guardrails and audit trail.

Keep policy intent common where useful—such as “no public object storage”—but compile
and test provider-specific enforcement. A green central dashboard does not prove each
native policy engine evaluated the desired resource.

## Governance questions

Who owns root/tenant/organization access? Which boundary contains blast radius and
quota? How are exceptions approved and expired? Can a recovery environment be created
under normal guardrails? Which native evidence proves compliance?
