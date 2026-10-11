# Scenario Questions and Model Answers

[← Design exercise](design-exercise.md) · [Next: Advanced drills →](scenario-drills.md)

Answer aloud before reading the model answer. Clarify, decide, explain failure and
operations, name evidence, and close with trade-offs.

## 1. Design an Azure foundation for 100 product teams

**Model answer:** I clarify tenant, regulatory, isolation, network, ownership, billing,
and delivery needs. I design a shallow management-group hierarchy, platform and
workload subscriptions, landing-zone vending, Entra groups, PIM, Azure RBAC, Policy,
central security/management evidence, hub/vWAN connectivity as justified, and governed
self-service. Platform and workload responsibilities, service levels, exceptions,
subscription lifecycle, and flow/adoption metrics are explicit.

## 2. One subscription or many subscriptions

**Model answer:** Subscriptions are administration, quota, policy, billing, and blast-
radius units. I separate workload environments and platform capabilities where
ownership, policy, data, network, lifecycle, quota, or chargeback justify it, without
creating fragmentation for every component. I design cross-subscription identity,
DNS, network, keys, logs, deployments, support, and cost. Resource groups then reflect
resource lifecycle—not an alternative to subscription isolation.

## 3. Explain Entra roles, Azure RBAC, and Azure Policy

**Model answer:** Entra roles authorize directory operations; Azure RBAC grants
management or data actions over Azure scopes; Azure Policy evaluates/enforces resource
state through effects such as audit or deny and does not grant access. I use groups,
managed identities, least privilege, PIM/JIT, Conditional Access, scoped assignments,
and tested Policy initiatives. I trace effective access and policy independently rather
than adding Owner to solve every denial.

## 4. Choose VM Scale Sets, AKS, Container Apps, App Service, or Functions

**Model answer:** I compare OS/runtime control, state, duration, protocol, scale shape,
latency, isolation, networking, storage, deployment, portability, limits, skills, and
cost. VMs suit control/compatibility; AKS suits justified Kubernetes needs; Container
Apps suits managed container microservices/jobs; App Service suits managed web/API;
Functions suits event-driven bounded execution. I model plan/SKU capacity, quotas,
downstream pressure, failure, and team ownership.

## 5. The workload must survive an Availability Zone failure

**Model answer:** I classify every component as zonal, zone-redundant, or nonzonal and
verify service/SKU/Region support. I distribute independent compute, ingress, data, and
network paths; remove single-zone appliances/endpoints; and retain remaining-zone
capacity. I test zone loss, autoscale, connections, retries, data integrity, and
operations. Three subnets or a zone label do not prove end-to-end resilience.

## 6. Private endpoints work in Azure but not from on-premises

**Model answer:** I trace the private endpoint IP, private DNS zone records and links,
conditional forwarders/resolvers, hybrid routes, NSGs, Firewall, return path, and the
service’s public-access/approval state. I compare resolution from each client boundary
and use Network Watcher/effective routes and diagnostics. I centralize DNS ownership
with tested registration and hybrid resolution; hard-coded hosts-file fixes hide the
architecture problem.

## 7. A user has Contributor but cannot read secrets

**Model answer:** Contributor is primarily management-plane access and does not
automatically grant Key Vault data-plane rights. I identify whether the vault uses
Azure RBAC or access policies, the principal and token, scope, role/action, network
access/private DNS, firewall, deny assignments, PIM activation, and audit logs. I grant
only the required secret operation through the chosen authorization model and separate
key/secret administration from use.

## 8. Functions overwhelm Azure SQL connections

**Model answer:** I cap concurrency or event consumption and buffer/throttle to protect
the database. I inspect hosting plan, trigger batching, retry behavior, pool reuse,
connection lifetime, transaction duration, query latency, and burst shape. I apply
connection pooling/proxy or architecture changes only with compatibility evidence. I
load-test downstream budgets, make handlers idempotent, and alarm on saturation plus
business completion delay.

## 9. Select Service Bus, Event Grid, or Event Hubs

**Model answer:** Service Bus handles enterprise commands/work with queues/topics,
sessions and broker features; Event Grid routes discrete events to handlers; Event Hubs
ingests retained partitioned streams for consumers. I choose from delivery, ordering,
retention/replay, throughput, routing, transactions, consumer model, and operations.
I define schema, identity, private access, idempotency, DLQ/redrive, backpressure,
partitioning, quotas, and end-to-end delay.

## 10. Front Door or Application Gateway

**Model answer:** Front Door is global HTTP(S) edge routing/acceleration with origins,
WAF and optional caching; Application Gateway is Regional layer-7 ingress with WAF and
VNet integration. They can be combined. I decide from global versus Regional scope,
private origins, protocols, TLS, WAF policy, health, failover, latency, observability,
and cost. Traffic Manager is DNS-based and Load Balancer is layer 4, so neither is an
automatic equivalent.

## 11. Backups are successful but no restore has been tested

**Model answer:** Recoverability is unproven. I restore into an isolated subscription/
network, validate identities, Key Vault, private DNS, dependencies, configuration,
integrity, performance, and business journeys, and measure RTO/RPO. I verify vault
immutability/soft delete and separation from the failure or compromise. Findings update
runbooks, permissions, architecture, and continuity objectives.

## 12. A Policy assignment blocks an emergency deployment

**Model answer:** I identify the assignment, initiative/definition, effect, scope,
exemption, resource state, and deployment evidence. I use an authorized, narrowly
scoped, time-bound exemption or corrected policy rather than disabling governance at
the root. I log the decision, preserve compensating controls, restore service, expire
the exception, and test recovery actions plus policy changes in a staging hierarchy.

## 13. An Azure service quota blocks campaign scaling

**Model answer:** I protect the journey through admission control, queues, throttling,
or degradation. I confirm the exact tenant/subscription/Region/zone/SKU/resource-
provider scope, current use, capacity availability, and increase lead time. I request
adjustment if possible and use alternate SKU/Region only when semantics and testing
permit. Quota/capacity forecasts, registrations, alarms, and release gates then include
normal, burst, deployment, and failure demand.

## 14. Design secure cross-subscription delivery

**Model answer:** The pipeline uses workload identity federation or managed identity to
obtain short-lived access to a narrow deployment role. Build, deployment, and runtime
identities are separate; artifacts/modules are reviewed, versioned, and promoted rather
than rebuilt. Policy is evaluated before rollout, broad changes are staged, production
approval and audit are protected, secrets stay out of pipelines, and break-glass
recovery works when Azure DevOps/GitHub or the deployment subscription is impaired.

## 15. The cheapest Region lacks a required service or zone SKU

**Model answer:** I rank residency, compliance, user latency, service and zone
availability, quota/capacity, dependencies, connectivity, recovery, support, skills,
and total cost. Options include another Region, another tier/service, self-managed
deployment, hybrid placement, or an accepted constraint. I evaluate paired/secondary
Region needs independently. Price does not override required qualities, and the ADR
records a trigger to reassess.

## 16. How do you conduct an Azure architecture review

**Model answer:** I define workload scope, journeys, evidence, stakeholders, and risk
owners; separate landing-zone/platform controls from workload responsibilities; then
review reliability, security, cost optimization, operational excellence, and
performance efficiency. I validate claims with configuration, metrics, incidents,
tests, restore/failover and cost evidence. Findings have business impact, owner,
priority, treatment, and completion criteria; the review is not an audit score.
