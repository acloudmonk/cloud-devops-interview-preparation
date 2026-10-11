# Enterprise Platform and Shared Services

[← Governance and landing zones](governance-landing-zones.md) · [Next: Identity and security →](identity-security.md)

## Treat the platform as a product

Provide supported paths for subscription vending, identity, networking, private DNS,
certificates, keys, logs, security, backup, delivery, observability, cost allocation,
quota requests, and incident access. Define consumers, owners, service levels, versions,
support, adoption, feedback, and retirement. A landing zone must evolve as an operating
capability rather than remain a one-time deployment.

## Automate subscription lifecycle

Intake should capture owner, environment, data classification, management-group
placement, network, Region, cost center, controls, and lifecycle. Use an Azure Landing
Zone accelerator, subscription-vending automation, or a governed custom workflow.
Apply baselines idempotently, detect drift, stage broad policy changes, and provide
quarantine, transfer, and closure paths.

## Deliver repeatable platform products

ARM templates and Bicep provide Azure-native infrastructure definitions; Template
Specs can version templates, Deployment Stacks can manage resource collections, and
Azure Verified Modules provide reusable building blocks. Terraform/OpenTofu may remain
appropriate. Protect deployment identities, promote reviewed artifacts, bound rollout,
and preserve recovery if the central delivery system is unavailable.

## Design shared services explicitly

Potential shared capabilities include hub/vWAN connectivity, Firewall, DDoS protection,
private DNS, ExpressRoute/VPN gateways, Bastion, Key Vault patterns, Container Registry,
Monitor workspaces, Sentinel, Defender for Cloud, backup, automation, and update
management. Define tenancy, authorization, quota, cost allocation, SLO, change
compatibility, failure isolation, recovery, and consumer escape for every shared service.

## Balance central and workload ownership

Centralize high-risk repeated controls and enterprise connectivity; delegate workload
decisions that teams can safely own. Azure Lighthouse can support delegated management
across tenants/subscriptions when justified. Measure vending lead time, platform
availability, adoption, exceptions, failed changes, satisfaction, and toil—not resource
counts or policy totals.
