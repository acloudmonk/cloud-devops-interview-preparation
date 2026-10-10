# Segmentation and Application Access

[← Module overview](index.md) · [Module 07: Networking](../07-networking/index.md)

Zero Trust augments network controls; it does not remove them. Segmentation limits
reachable paths and blast radius, while identity-aware and application controls
decide which transactions are permitted.

## Choose the boundary from the threat

| Boundary | Typical enforcement | Useful outcome |
| --- | --- | --- |
| Internet edge | WAF, DDoS protection, API gateway, identity-aware proxy | reduce public attack surface and authenticate requests |
| User-to-application | ZTNA proxy, application, VDI | replace broad network access with resource access |
| Environment/account | cloud accounts, projects, VPCs/VNets, routing | separate administration, risk, and failure domains |
| Workload-to-workload | security groups, firewalls, Kubernetes policy, mesh | restrict lateral movement and dependency calls |
| Data/resource | resource policy, service endpoint, application authorization | enforce owner and action-level intent |

Begin with flows required by critical transactions. Default-deny policy is useful
only when dependencies, DNS, time, certificate validation, management, monitoring,
and recovery paths are understood. Otherwise emergency bypasses become permanent.

## Private access is not authorization

Private addressing and endpoints reduce exposure and can add policy context, but
anything on the path may still be overprivileged or compromised. Conversely, a
publicly reachable endpoint can be strongly authenticated and narrowly authorized.
Evaluate exposure, identity, authorization, data protection, detection, and
availability separately.

## Remote and administrative access

Prefer access to named applications and brokered administrative sessions over a
VPN that exposes an entire subnet. For servers, consider session brokers with
identity, approval, recording, and command evidence instead of inbound SSH/RDP.
Retain a segmented recovery path that works during identity or proxy failure.

## East-west policy

Inventory flows, classify workloads and data, express policy in stable service
identity where possible, and observe before enforcing. Roll out by protect surface,
test partial failures, and monitor denied connections. Network policy should
complement destination authorization rather than duplicate business permissions.

## Availability trade-off

Identity proxies, service meshes, DNS, certificate services, and policy engines
enter critical request paths. Design regional redundancy, bounded caches, policy
version rollback, overload behavior, and explicit fail-open/fail-closed decisions
per resource. "Always deny on error" is unsafe when it prevents incident recovery.

Return to the [module overview](index.md) when ready to continue.
