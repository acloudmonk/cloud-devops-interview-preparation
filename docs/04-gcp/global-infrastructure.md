# Global Infrastructure and Service Scope

[← Decision model](concepts.md) · [Next: Resource hierarchy →](resource-hierarchy-governance.md)

Google Cloud locations include regions and zones. A zone is a failure domain within a
region; a region is an independent geographic area. Services may be zonal, regional,
multi-regional, or global, and product availability differs by location.

| Scope | Typical examples | Design question |
| --- | --- | --- |
| Global | VPC networks, global external Application Load Balancer | Which regional dependencies remain? |
| Regional | Subnets, Cloud Run, many managed data deployments | How is regional loss handled? |
| Zonal | VM instances, zonal disks, many GKE nodes | Can another zone carry demand? |
| Multi-region | Selected Cloud Storage/Spanner configurations | What consistency, cost, and residency apply? |

A global control surface does not prove global data-plane availability. Inventory DNS,
load balancing, certificates, identity, keys, network paths, compute, state, quotas,
observability, deployment, and operator access end to end.

## Placement method

1. Locate users, data, dependencies, and legal constraints.
2. Verify current service, feature, accelerator, and quota availability.
3. Place latency-sensitive synchronous paths close together.
4. Choose resilience from the SLO and loss tolerance.
5. Model steady state, maintenance, zone loss, region loss, and recovery capacity.

Ask whether failover is automatic or coordinated, writes remain correct, surviving
capacity includes quotas and dependencies, and exercises prove RTO and RPO.
