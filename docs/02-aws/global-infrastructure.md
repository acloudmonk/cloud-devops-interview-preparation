# Global Infrastructure and Service Scope

[← Decision model](concepts.md) · [Next: Organizations and governance →](multi-account-governance.md)

## Understand the hierarchy

A Region is a separate geographic area containing multiple isolated Availability
Zones. An AZ contains one or more data centers with independent facilities and
redundant connectivity. Points of presence support edge services. Local Zones,
Wavelength Zones, and Outposts address specific latency or residency needs but change
dependencies, capacity, operations, and service availability.

## Classify service scope

Resources may be global, Regional, zonal, or edge-scoped. The management interface may
look global while data-plane resources remain Regional. Document where configuration,
identity, control-plane operations, data, encryption keys, logs, and dependencies live.
Never infer failure independence from a console URL.

## Choose Regions from constraints

Evaluate users and latency, data residency, service and feature availability, quotas,
compliance, connectivity, carbon and energy information, cost, support, skill, disaster
risk, and partner dependencies. Multi-Region adds replication, consistency, failover,
security, deployment, test, and cost complexity; require business justification.

## Use multiple AZs correctly

Distribute independent capacity and state across AZs, but verify whether the selected
service and topology actually do so. Avoid a hidden single-AZ database, NAT path,
endpoint, appliance, node group, or storage dependency. Balance resilience against
cross-AZ data transfer, latency, and operational complexity.

## Design for control-plane impairment

Existing resources and data paths may continue when management APIs are degraded, but
scaling, replacement, deployment, credential operations, or recovery can fail. Keep
steady-state operation dependent on the data plane where possible, pre-provision
critical capacity, cache safe configuration, and rehearse with realistic assumptions.
