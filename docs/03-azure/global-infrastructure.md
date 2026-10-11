# Global Infrastructure and Service Scope

[← Decision model](concepts.md) · [Next: Governance and landing zones →](governance-landing-zones.md)

## Understand placement constructs

Azure geographies address data-residency and compliance boundaries; Regions contain
one or more data centers; many Regions provide physically separated Availability Zones.
Region pairs exist for many Regions but service behavior and recovery priority vary.
Edge, Extended Zones, and Azure Local address latency or on-premises needs with distinct
service, capacity, and operational constraints.

## Classify resource scope

Resources and services may be global, regional, zonal, zone-redundant, or nonzonal.
The Azure Resource Manager control plane can have different availability from workload
data planes. Document where configuration, identities, metadata, data, keys, logs, and
dependencies reside rather than assuming a portal view indicates placement.

## Select Regions deliberately

Evaluate users and latency, residency, service/feature availability, Availability Zone
support, quotas and capacity, compliance, connectivity, cost, support, sustainability,
skills, and dependencies. Check exact SKU availability. Multi-Region designs introduce
data replication, conflict, failover, deployment, security, test, and cost obligations.

## Use Availability Zones correctly

Choose zone-redundant services or distribute independent zonal instances and data paths
according to service semantics. Verify load balancers, gateways, disks, databases,
clusters, private endpoints, firewalls, and dependency topology. Maintain capacity for
zonal failure and test it; selecting three subnet names does not create resilience.

## Design for control-plane impairment

Existing data-plane resources may continue while deployments, scaling, identity or
configuration changes are impaired. Avoid requiring urgent control-plane mutation for
steady-state service, pre-provision critical capacity, keep safe cached configuration,
and rehearse response with documented assumptions and emergency access.
