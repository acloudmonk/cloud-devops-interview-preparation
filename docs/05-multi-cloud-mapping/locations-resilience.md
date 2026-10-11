# Locations, Scope, and Resilience

[← Identity and security](identity-security.md) · [Next: Networking →](networking.md)

Region and zone labels do not establish equal failure independence. Verify current
provider documentation, service scope, feature availability, and shared dependencies.

| Question | AWS | Azure | Google Cloud |
| --- | --- | --- | --- |
| Common zone term | Availability Zone | Availability Zone | Zone |
| Regional network scope | VPC is regional | VNet is regional | VPC is global; subnet regional |
| Cross-region construct | Service-specific/global services | Service-specific/global services | Service-specific/global services |

Inventory DNS, edge, identity, control plane, keys, network, compute, data,
observability, deployment, quotas, and operators for the whole journey. “Three zones”
or “global service” does not prove end-to-end availability.

## Cross-cloud recovery

Cross-cloud recovery is justified only when its threat model and business value exceed
the costs of duplicated platforms, data movement, consistency, testing, skills, and
reduced use of native capabilities. Define authority, replication lag, fencing,
failover trigger, DNS/client behavior, security controls, capacity, reconciliation,
failback, and exercise evidence.

A second cloud that cannot receive current data, authenticate users, obtain quota, or
be operated during an incident is not a recovery strategy.
