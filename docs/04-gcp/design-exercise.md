# Enterprise GCP Design Exercise

[← Well-Architected review](well-architected.md) · [Next: Scenarios →](scenarios.md)

## Brief

A regulated commerce company serves North America, Europe, and India. It acquired teams
with standalone projects and service-account keys. Traffic spikes 12× during campaigns.
The platform processes orders and payments, distributes media, publishes events to
analytics, and must support RTO 60 minutes/RPO 5 minutes for ordering. Current incidents
include Shared VPC firewall mistakes, Cloud NAT port pressure, Cloud Run connection
storms, Pub/Sub backlog, untested restores, quota failure, and unattributed spend.

## Produce

1. Requirements, assumptions, SLOs, residency, RTO/RPO, and ownership.
2. Organization/folder/project and billing hierarchy.
3. Identity, federation, privileged access, policy, keys, perimeter, and audit design.
4. Global/regional network, DNS, ingress, egress, hybrid, and private service paths.
5. Runtime, transactional data, object, analytics, and integration selections.
6. Zone/region failure, degradation, backup, restore, and integrity verification.
7. Delivery, observability, incident, quota, cost, and sustainability controls.
8. Alternatives, evidence plan, risks, and exit triggers.

## Constraints to challenge

- EU customer data must remain in approved locations.
- A legacy payment component needs OS control and a partner private connection.
- Developers need safe self-service without broad organization access.
- Analytics may lag 15 minutes; order confirmation may not.
- Region failure capacity cannot depend on an unapproved quota increase.

## Evaluation

Score 0–2 for each: clarification, hierarchy/governance, identity/security, network,
compute, data, integration, reliability/recovery, operations/evidence, cost/capacity,
and communication/trade-offs. **18/22** is a strong result; any unaddressed data
integrity or identity risk requires remediation regardless of total.
