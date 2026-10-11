# Case 4: Hybrid Modernization Program

[← Platform transformation](platform-transformation.md) · [Next: Cyber-recovery crisis →](cyber-recovery.md)

## Brief

A manufacturer has 140 applications in two data centers. Hardware support ends in
eighteen months. ERP, plant systems, and identity dependencies are poorly mapped;
some factories tolerate only 100 ms latency and intermittent WAN service. The board
wants “80% in cloud” while regulators require selected records to remain in-country.

## Discovery prompts

- What business events, contracts, and support deadlines drive the program?
- Which applications depend on local equipment, shared databases, identity, or batch?
- What are latency, availability, RTO/RPO, residency, and data-transfer constraints?
- Which workloads should retire, retain, rehost, replatform, refactor, or replace?
- What landing-zone, network, security, skills, funding, and vendor constraints exist?

## Candidate tasks

1. Build a portfolio evidence model and migration-wave selection method.
2. Design cloud foundations, identity, connectivity, DNS, security, and operations.
3. Compare rehost, replatform, refactor, replace, retire, and retain decisions.
4. Plan data movement, coexistence, cutover, rollback, and data-center exit evidence.
5. Define business outcomes, wave gates, cost controls, and capability uplift.

## Failure injects

- Network dependency mapping missed a licensing server used by 25 applications.
- Replication lag exceeds the agreed RPO during cutover rehearsal.
- Cloud spend doubles while both estates run in parallel.
- A factory loses WAN connectivity for six hours.
- The first migration wave meets schedule but creates more operational tickets.

## Model direction

Challenge the percentage target; success is reduced business risk and improved
outcomes, not resource count. Establish an AWS landing zone with federated identity,
account boundaries, policy, logging, networking, keys, budgets, and operational
ownership before production waves. Use discovery telemetry and business interviews
to build dependency confidence, then group waves by business capability and shared
dependencies rather than application convenience.

Keep latency- or outage-sensitive plant control local and design store-and-forward
integration. Rehearse data migration and rollback using measured change rates and
validation, not only tool completion. Set parallel-run budgets and explicit exit
criteria. Begin with representative low/medium-risk workloads, improve the factory,
then move higher-risk systems. Track incident load, lead time, recovery evidence,
unit cost, and retired assets; a migrated VM is not modernization by itself.

## Strong close

Recommend a portfolio governance model and first two waves. State which workloads
should remain hybrid, how that decision is revisited, and the evidence required to
close each data-center dependency safely.
