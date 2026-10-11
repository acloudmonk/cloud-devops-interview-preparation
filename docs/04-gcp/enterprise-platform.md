# Enterprise Platform and Shared Services

[← Resource hierarchy](resource-hierarchy-governance.md) · [Next: Identity and security →](identity-security.md)

A cloud foundation is a product: an organization structure, project-vending workflow,
identity integration, policies, networks, logging, security, billing, and automation.

## Platform capabilities

- approved project archetypes with owner, environment, data class, and cost metadata;
- Shared VPC host projects and deliberately attached service projects;
- centralized DNS, hybrid connectivity, egress, logs, findings, keys, and artifacts;
- workload identity patterns that avoid long-lived service-account keys;
- versioned infrastructure code, policy tests, drift detection, and rollback;
- service catalog, support model, exceptions, SLOs, adoption, and feedback metrics.

Shared VPC centralizes network administration while service projects retain workload
resources and IAM. Define subnet delegation, firewall ownership, DNS, routes, NAT,
private access, and incident responsibilities; avoid making one team a bottleneck.

## Project vending flow

Request → validate metadata and risk → allocate project and billing → apply policies →
attach networking → configure logging/security → bootstrap delivery identities → test
controls → hand over ownership → continuously reconcile.

Measure safe lead time, adoption, exception age, drift, incident outcomes, developer
effort, and unit cost—not the number of controls.
