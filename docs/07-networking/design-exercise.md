# Network Architecture Design Exercise

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**
Estimated time: **3–4 hours**
Expected cloud cost: **None**

## Brief

Design the network for a customer portal deployed in two AWS Regions. Each
Region has three Availability Zones, private application and data services, a
public web entry point, corporate administration, partner API access, outbound
vendor calls, and connectivity to one data center. Recovery objectives are
RTO 30 minutes and RPO 5 minutes. The design must be translatable to Azure and
Google Cloud.

Do not deploy resources. Produce diagrams, tables, and decision notes.

## Requirements to clarify

- expected users, geography, protocols, peak connections, throughput, and growth;
- public, employee, partner, machine, and operations trust boundaries;
- data classification, residency, inspection, and logging constraints;
- dependencies on DNS, identity, certificates, vendors, and on-premises systems;
- availability targets, zonal/regional failure behavior, RTO/RPO, and failback;
- current/future address space and network connections;
- ownership, deployment frequency, incident access, and budget.

## Required deliverables

1. **Request-flow diagram:** DNS through edge, load balancer, service, data, and
   outbound dependency, including TLS termination and trust boundaries.
2. **IP plan:** VPC and subnet prefixes, zones, growth reserve, IPv6 position,
   and overlap controls.
3. **Route and policy table:** source, destination, protocol, route path,
   authorization control, owner, and evidence.
4. **DNS design:** public/private zones, delegation, resolver forwarding,
   failover records, TTL policy, and cutover/rollback.
5. **Ingress/egress design:** DDoS/WAF, client identity, NAT/private endpoints,
   inspection, allow-listing, and failure behavior.
6. **Hybrid design:** redundant paths, routing policy, DNS integration,
   capacity after failure, and test schedule.
7. **Operational plan:** telemetry, SLOs, quotas, certificates, change gates,
   incident path, and sensitive-data handling.
8. **Multi-cloud translation:** Azure and GCP equivalents plus at least five
   semantic differences that affect the design.
9. **Cost/risk register:** top five cost drivers and top ten risks with owners.

## Mandatory failure walkthroughs

Explain detection, customer impact, mitigation, verification, and prevention for:

- one Availability Zone loses egress;
- a DNS change returns mixed old/new answers;
- NAT ports are exhausted during a retry storm;
- the primary dedicated circuit fails and VPN backup lacks full capacity;
- a certificate is renewed without the expected intermediate chain;
- a route advertisement creates an asymmetric return path;
- the secondary Region is healthy but cannot accept production scale.

## Decision record template

| Field | Content |
| --- | --- |
| Decision | One precise architecture choice |
| Context | Requirement, constraint, and expected traffic |
| Options | At least two viable alternatives |
| Choice and why | Evidence-based selection |
| Trade-offs | Security, reliability, latency, operations, and cost |
| Failure behavior | Detection, blast radius, and recovery |
| Validation | Test and measurable acceptance criteria |
| Revisit trigger | Growth, incident, regulation, or platform change |

## Self-assessment

Score 0–4 for requirements, flow correctness, address/routing design, DNS,
security, resilience, operability, multi-cloud accuracy, cost, and executive
communication. A strong result scores at least 30/40 with no category below 2.
