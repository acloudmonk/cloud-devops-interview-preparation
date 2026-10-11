# Tenancy, Isolation, and Placement

[← SaaS decision model](concepts.md) · [Next: Control plane and lifecycle →](control-plane-lifecycle.md)

## Pool, silo, and bridge

| Model | Shape | Strength | Cost or risk |
| --- | --- | --- | --- |
| Pool | Tenants share a resource | Efficiency and rapid scale | Strong application isolation and noisy-neighbor controls needed |
| Silo | Resource stack dedicated to a tenant | Clear isolation and customization boundary | Fleet cost, capacity waste, and operational scale |
| Bridge | Models differ by component or tier | Balances economics and obligations | Placement, migration, and operations become more complex |

Choose separately for edge, compute, cache, queue, database, object storage, keys,
telemetry, and analytics. A premium tenant might share compute but use a dedicated
database and encryption key. “Dedicated” must name the exact boundary.

## Cells and deployment stamps

A cell is a bounded copy of the data plane serving a subset of tenants. A placement
service maps tenant to cell; routing uses that mapping. Cells constrain blast radius,
capacity, and deployment exposure while enabling geographic placement. They add
fleet orchestration, catalog consistency, version skew, rebalancing, and uneven-load
challenges. Define maximum cell size and evacuation strategy before saturation.

## Isolation is a chain

Isolation requires all of the following to agree:

- identity binds a principal to tenant memberships;
- the edge resolves tenant from a trusted domain, token, or explicit route;
- policy authorizes the action for the resolved tenant;
- service code does not accept a caller-supplied tenant identifier as truth;
- queries and object keys include the tenant partition;
- caches, queues, search indexes, exports, and logs preserve the boundary;
- background jobs and support tools carry tenant context;
- tests attempt horizontal cross-tenant access.

Use deny-by-default policy, immutable context, scoped credentials, database controls
where available, and negative isolation tests. Encryption is valuable but does not
replace correct authorization and partitioning.

## Placement and migration

The tenant catalog should identify region, cell, data partition, tier, lifecycle
state, identity configuration, and policy version. Routing must handle stale catalog
data deliberately. Tenant moves need dual-write or change-capture boundaries,
validation, a cutover token, rollback conditions, and proof that old copies are
retired. Never improvise a large-tenant move during an incident.

## AWS-first translation

On AWS, possible boundaries include account, VPC, cluster, namespace, service,
database, schema, table partition, S3 prefix or bucket, queue, and KMS key. Azure
deployment stamps and subscriptions/resource groups offer analogous placement
options; Google Cloud projects and Identity Platform tenants provide other useful
boundaries. These constructs are not automatically equivalent—verify quotas,
identity semantics, regional behavior, and operational effort.
