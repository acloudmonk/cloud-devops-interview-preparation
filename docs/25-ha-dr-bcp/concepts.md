# Continuity Decision Model

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Continuity architecture begins with the business service, not a list of cloud
features. The design must preserve or recover a defined outcome under named
failure conditions, within agreed time and data-loss limits, using procedures
that real people can execute.

## Six-part mental model

1. **Outcome** — critical customer or business service and minimum acceptable level.
2. **Impact** — safety, financial, legal, operational, and reputational consequence over time.
3. **Objective** — availability target, RTO, RPO, maximum tolerable disruption, and recovery priority.
4. **Failure model** — component, zone, Region, provider, identity, data, cyber, facility, supplier, or people loss.
5. **Capability** — redundancy, isolation, backup, replication, alternate process, recovery automation, and communications.
6. **Evidence** — monitoring, restore tests, exercises, measured recovery, audit trail, and owned improvements.

```mermaid
flowchart LR
    B[Business service] --> I[Impact over time]
    I --> O[Recovery objectives]
    O --> F[Failure assumptions]
    F --> A[Architecture and continuity plan]
    A --> T[Test and measure]
    T --> G[Govern gaps and improve]
    G --> I
```

## Terms that should not be interchanged

| Term | Primary question |
| --- | --- |
| Resilience | Can the system absorb, adapt to, and recover from disruption? |
| High availability | Can it continue through expected localized failures? |
| Backup | Can a protected copy restore data or configuration? |
| Disaster recovery | Can the technology service be recovered after a declared disruption? |
| Business continuity | Can the organization keep critical outcomes operating? |
| Crisis management | Who directs enterprise decisions, safety, communication, and priorities? |

Replication is not backup: corruption or destructive credentials can propagate.
Backup is not recovery: stored copies do not prove infrastructure, applications,
keys, identities, dependencies, or people can restore service. Multi-Region is
not automatically DR: correlated configuration and control failures can affect
both Regions.

## Architecture test

A credible design can answer: Which business journey is protected? What is the
minimum acceptable service? Which disruptions are in scope? When does the clock
start and stop? How much data loss is tolerable? Who can declare and direct
recovery? What dependencies and control planes remain? How is recovery verified?
How is normal service restored without losing new data?

Return to the [module overview](index.md) when ready to continue.
