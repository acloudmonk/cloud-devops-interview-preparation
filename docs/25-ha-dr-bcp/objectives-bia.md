# Business Impact and Recovery Objectives

[← Module overview](index.md) · [Continuity decision model](concepts.md)

A business impact analysis (BIA) identifies important products and processes,
their time-dependent consequences, dependencies, workarounds, and recovery
priorities. It prevents every system from receiving an expensive “critical” label.

## Discovery sequence

1. Map customer journeys and business services, not only applications.
2. Identify owners, users, operating periods, regulatory duties, and suppliers.
3. Quantify impact at intervals such as 15 minutes, 1 hour, 4 hours, and 24 hours.
4. Define the minimum business continuity objective: what reduced service is viable?
5. Map applications, data, identity, network, people, facilities, vendors, and control planes.
6. Assign recovery tiers and sequence prerequisite services before dependants.
7. Obtain business and risk-owner approval for targets and exceptions.

## Objective vocabulary

- **RTO**: target elapsed time to restore an agreed service level after disruption.
- **RPO**: maximum tolerable data-loss interval measured backward from disruption.
- **MTPD/MAO**: longest disruption the business can tolerate before impact becomes unacceptable.
- **WRT**: work recovery time after technology restoration for validation, backlog, reconciliation, and business restart.
- **Availability target**: acceptable successful service over a measurement window; it is not an RTO.

A useful constraint is `RTO + WRT ≤ MTPD`. Document precisely when each clock
starts, which service level stops it, and whether the target covers detection,
decision, technical recovery, validation, and business resumption.

## Example recovery tiers

| Tier | Illustrative target | Typical strategy |
| --- | --- | --- |
| 0 | RTO minutes; RPO near zero | Multi-AZ plus engineered multi-Region or alternate channel |
| 1 | RTO under 1 hour; RPO minutes | Warm standby or carefully automated pilot light |
| 2 | RTO several hours; RPO hours | Pilot light or automated restore |
| 3 | RTO 24–72 hours; RPO daily | Backup and rebuild |

These are examples, not universal standards. Target the entire service chain;
the slowest critical dependency determines achievable recovery. Validate provider
quotas, data volume, DNS behavior, staff availability, and supplier commitments.

## Interview signal

Do not accept “zero RPO and zero RTO” without challenge. Ask what consequence
justifies the cost and complexity, which write conflicts are acceptable, whether
the application supports concurrent writers, and which residual risks remain.

Return to the [module overview](index.md) when ready to continue.
