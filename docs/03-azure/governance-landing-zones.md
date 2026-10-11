# Management Groups, Landing Zones, and Governance

[← Global infrastructure](global-infrastructure.md) · [Next: Enterprise platform →](enterprise-platform.md)

## Design the resource hierarchy

A Microsoft Entra tenant contains the identity boundary; management groups organize
subscriptions for inherited governance; subscriptions provide administration, quota,
billing, and workload boundaries; resource groups hold resources with a shared
lifecycle. Structure management groups around policy needs rather than copying the
business org chart or creating deep hierarchies without benefit.

## Use subscriptions as scale units

Separate platform capabilities and workload environments where isolation, ownership,
quota, networking, lifecycle, policy, or chargeback justify it. A subscription-per-
workload/environment pattern can provide autonomy within guardrails. Design cross-
subscription identity, network, DNS, keys, logs, deployment, support, and cost.

## Apply governance layers correctly

Azure RBAC grants management/data actions at scopes. Azure Policy audits, modifies,
deploys related configuration, or denies noncompliant resources according to effect;
it does not replace authorization. Resource locks protect against accidental management-
plane deletion/change but are not a security boundary. Tags support metadata and cost,
not confidential data or strong access isolation.

## Build Azure landing zones

Separate platform landing-zone subscriptions for identity, connectivity, and management
from workload landing zones. Address billing/tenant, identity, resource organization,
networking, security, management, governance, and platform automation/DevOps. Use the
Azure Landing Zone accelerator or a governed custom implementation based on needs.

## Govern exceptions and lifecycle

Exceptions need scope, rationale, risk owner, compensating control, evidence, expiry,
and remediation. Subscription vending and closure must handle data, locks, backups,
keys, legal hold, network/DNS, identities, budgets, ownership, and recovery periods.
Governance should enable safe self-service rather than drive hidden deployments.
