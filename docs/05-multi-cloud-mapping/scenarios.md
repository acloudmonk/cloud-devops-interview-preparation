# Scenario Questions and Model Answers

[← Design exercise](design-exercise.md) · [Next: Advanced drills →](scenario-drills.md)

Answer aloud before reading the model answer.

## 1. The CIO mandates cloud agnosticism

**Model answer:** I clarify the risk or value being purchased and define measurable
exit objectives. I compare portfolio placement, portable layers, and duplicated
runtime/data/operations. I standardize outcomes and interfaces where valuable while
retaining native services when their benefit exceeds migration cost.

## 2. Map AWS accounts to Azure and GCP

**Model answer:** Azure subscriptions and GCP projects are closest workload boundaries,
but not equivalents. I map policy inheritance, IAM, API/service enablement, quotas,
network scope, billing, and lifecycle before designing landing-zone vending.

## 3. Build common governance

**Model answer:** I define common intent, ownership, classification, evidence, and
exceptions, then implement tested native SCP/Control Tower, Azure Policy/landing-zone,
and Organization Policy controls. I never rely solely on a central dashboard.

## 4. Federate workforce and workloads

**Model answer:** I use an authoritative identity lifecycle, groups, strong auth, and
short-lived federation. Provider-native roles remain least privilege. Build, deploy,
runtime, emergency, and investigation identities are separated and audited.

## 5. Connect all three clouds

**Model answer:** I begin with required flows, latency, bandwidth, availability, and
data sensitivity. I compare VPN, private circuits, exchange/provider hubs, and SD-WAN;
design BGP, DNS, overlapping IPs, encryption, return paths, egress, monitoring, and
diverse failures. I avoid full mesh without need.

## 6. Standardize Kubernetes

**Model answer:** I standardize application contracts, policy intent, GitOps, and
telemetry where useful, while documenting differences in identity, networking, storage,
load balancers, upgrades, nodes, and support. Kubernetes portability does not include
managed data or operational competence automatically.

## 7. Choose cross-cloud serverless equivalents

**Model answer:** I compare trigger/protocol, duration, concurrency, scaling, cold start,
network, identity, limits, retries, observability, quota, and cost across Lambda,
Functions, and Cloud Run functions. I use contract and load tests, not name matching.

## 8. Replicate customer data across clouds

**Model answer:** I identify authority, residency, consistency, acceptable lag, schema,
deletion, encryption, egress, and recovery. I avoid synchronous dual writes, prefer
CDC/outbox and idempotent consumers, and prove reconciliation and failback.

## 9. Create unified observability

**Model answer:** I standardize service ownership, trace context, SLIs, severity, and
retention; use OpenTelemetry where suitable; preserve native audit/resource evidence
and consoles; monitor ingestion gaps; and budget egress and cardinality.

## 10. Design cross-cloud disaster recovery

**Model answer:** I validate the threat model first. I define authoritative data,
replication lag, fencing, failover trigger, DNS, identity, keys, capacity, quota,
operations, reconciliation, and failback, then exercise the business journey.

## 11. Compare managed relational databases

**Model answer:** I start with engine compatibility, transactions, consistency, scale,
HA, backup, replication, RTO/RPO, connection behavior, network, operations, and cost.
RDS/Aurora, Azure SQL/managed engines, and Cloud SQL/AlloyDB are families, not swaps.

## 12. Reduce multicloud cost by 20%

**Model answer:** I normalize billing exports, ownership, and unit costs; isolate waste,
egress, duplicate tools, idle recovery, licensing, support, and commitment coverage;
then rightsizing and architecture changes precede discounts. I protect SLOs.

## 13. Select a cross-cloud IaC strategy

**Model answer:** I use Terraform/OpenTofu where common workflow adds value, with small
provider-specific modules, isolated state, federated identities, plans, policy tests,
drift, and versioning. Native tools remain valid for provider-specific capabilities.

## 14. A provider service has no equivalent

**Model answer:** I record the required capability and gap, then compare composition,
application change, different placement, accepted constraint, or provider-specific use.
I prototype the critical semantics and define migration/exit implications.

## 15. Acquisitions created three landing zones

**Model answer:** I inventory ownership, identity, networks, policy, data, contracts,
and dependencies; define minimum controls; remediate critical exposure; then converge
through waves without breaking workloads. Exceptions have owners and expiry.

## 16. Lead the executive decision

**Model answer:** I present drivers, options, weighted scorecard, target portfolio,
cost/risk, transition states, evidence, top assumptions, and exit triggers. I state
where multicloud adds value and where consolidation reduces complexity.
