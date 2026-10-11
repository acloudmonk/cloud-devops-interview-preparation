# Enterprise Continuity Design Exercise

[← Module overview](index.md) · [Cloud capability map](cloud-mapping.md)

## Brief

A regulated payments company serves customers from AWS. Its customer portal and
APIs run across three Availability Zones in one Region. Aurora PostgreSQL is the
transaction system of record; S3 stores statements; EKS hosts services; Route 53
and CloudFront provide public entry. Workforce identity is in Azure, analytics is
in Google Cloud, and two external payment networks are critical dependencies.

The board wants “zero downtime and zero data loss.” Current backups remain in the
production account, the secondary Region contains only a VPC, failover has never
been tested, and the contact list is nine months old. Design a defensible HA,
disaster-recovery, cyber-recovery, and business-continuity operating model.

## Required discovery

Clarify critical journeys and operating periods; safety, financial, contractual,
and regulatory impact; transaction consistency; settlement and reconciliation;
data residency; fraud controls; current incidents; dependency commitments; staff
and supplier availability; risk appetite; recovery budget; and decision authority.

## Produce these artifacts

1. **Business service map** — journeys, minimum service, owners, dependencies, and impact over time.
2. **Recovery tier table** — availability, RTO, RPO, MTPD, service level, and approver.
3. **Failure model** — component, zone, Region, corruption, cyber, identity, supplier, and people loss.
4. **Target architecture** — regional HA, DR pattern, data protection, traffic, identity, and degraded mode.
5. **Activation model** — signals, authority, roles, communications, recovery waves, and validation gates.
6. **Test plan** — restore, failover, cyber clean-room, supplier, workforce, and business exercises.
7. **Roadmap** — immediate controls, 90-day foundation, later maturity, cost, and residual risk.

## Constraints to address

- RPO differs for authorized transactions, statements, analytics, and configuration.
- Duplicate or split-brain payment writes are less acceptable than brief unavailability.
- Identity and key recovery cannot depend entirely on the affected production boundary.
- The secondary Region must have quotas, images, configuration, observability, and connectivity.
- External payment networks may require pre-registered addresses and certificates.
- A cyber event may make replicated production data and credentials untrustworthy.
- Manual payment processing has limited capacity and requires later reconciliation.

## Strong answer outline

Reject the universal zero target and run a BIA. Keep the transactional path
Multi-AZ, define safe degradation, and select warm standby or another measured
regional pattern for the highest tier. Use a clear single-writer/fencing model,
cross-Region data protection, independently secured immutable backups, replicated
artifacts and infrastructure definitions, pre-created emergency access, and
tested supplier connectivity. Sequence recovery foundations before applications.

Create separate technical, cyber, crisis, and business-continuity roles. Exercise
component restores first, then regional and clean-room recovery. Measure RTO/RPO
end to end and route gaps through owned risk governance. Present the residual risk
and cost of each target so the business can approve the design.

## Self-scoring rubric

| Dimension | 0 | 2 | 4 |
| --- | --- | --- | --- |
| Business alignment | service list only | targets stated | impact-based tiers and minimum service |
| Failure analysis | Region loss only | several failures | correlated technical, cyber, supplier, and people risks |
| Architecture | products listed | plausible topology | complete data, identity, dependency, capacity, and degraded-mode design |
| Recovery operation | generic runbook | sequence and roles | activation, fencing, validation, reconciliation, and failback |
| Continuity | omitted | communications included | viable people, supplier, workaround, and crisis model |
| Evidence | backups assumed | tests proposed | measured progressive exercises and governed remediation |

Maximum: **24**. Aim for at least **19** before moving to the mock interview.

Return to the [module overview](index.md) when ready to continue.
