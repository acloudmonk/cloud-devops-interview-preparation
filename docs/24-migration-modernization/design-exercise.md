# Enterprise Migration Design Exercise

[← Multi-cloud capability map](cloud-mapping.md) · [Next: Scenarios →](scenarios.md)

## Brief

A regulated global enterprise must exit two data centers within 18 months. Its 600
applications span VMware, physical servers, a mainframe, commercial packages, custom
Java/.NET services, file transfer, databases, and end-of-life systems. Inventory and
ownership are incomplete. Acquisitions use Azure; analytics teams consume Google
Cloud; AWS is the primary target. PCI, PII, residency, quarter-end freezes, strict
RTO/RPO, expiring licenses, and limited modernization skills apply.

## Candidate tasks

1. Define business outcomes, constraints, success measures, governance, and discovery.
2. Segment the portfolio and explain disposition criteria and decision records.
3. Describe AWS landing-zone readiness and cross-cloud integration boundaries.
4. Form a learning wave and later dependency-aware waves with entry/exit gates.
5. Design data transition, coexistence, cutover, rollback, and reconciliation.
6. Define validation, operational acceptance, hypercare, and decommissioning.
7. Prioritize modernization and demonstrate value without promising generic savings.

## Required artifacts

- outcome tree and assumptions;
- portfolio data model and dependency view;
- disposition scorecard and three example decisions;
- target/transition architecture and control boundaries;
- wave plan, readiness gates, and migration-factory flow;
- cutover runbook outline and evidence matrix;
- benefits, cost, risk, decision, and decommissioning dashboard.

## Failure injects

- network telemetry reveals a hidden licensing server three days before cutover;
- a database replication lag exceeds the rollback window;
- security rejects a temporary vendor administrator account;
- performance tests pass, but month-end batch misses its deadline;
- migrated workloads run successfully while data-center cost remains unchanged;
- a provider service quota blocks wave deployment;
- leadership demands a simultaneous rewrite to meet the exit date.

## Evaluation rubric

| Dimension | Points |
| --- | ---: |
| Outcomes, discovery, portfolio evidence, and business case | 9 |
| Disposition, target state, landing zone, and multi-cloud judgment | 9 |
| Waves, factory flow, dependencies, and governance | 8 |
| Data, cutover, rollback, integrity, and recovery | 9 |
| Security, validation, operations, and decommissioning | 8 |
| Modernization, economics, risks, and communication | 7 |
| **Total** | **50** |

A strong answer separates target and transition states, states uncertainty, assigns
decision rights, uses measurable gates, protects data authority, and closes legacy
cost. A tool list without business, cutover, and operating evidence is incomplete.
