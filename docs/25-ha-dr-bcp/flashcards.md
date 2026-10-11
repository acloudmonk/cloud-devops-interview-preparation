# Active-Recall Flashcards

[← Module overview](index.md) · [Rapid-fire revision](rapid-fire.md)

Use spaced repetition. Say the answer before expanding each card.

1. **HA / DR / BC?** Continue through routine failure / restore technology after disruption / sustain the business outcome.
2. **RTO / RPO?** Recovery duration target / tolerable data-loss interval.
3. **MTPD / WRT?** Maximum tolerable disruption / post-technology business recovery time.
4. **BIA output?** Impact over time, minimum service, dependencies, tiers, objectives, owners, and workarounds.
5. **Availability trap?** Redundant copies may share identity, DNS, data, configuration, deployment, or capacity failure.
6. **Multi-AZ purpose?** Regional HA against supported localized failures—not automatic regional disaster recovery.
7. **Backup-and-restore trade-off?** Low standby cost, longest provisioning and restoration path.
8. **Pilot-light trade-off?** Core state ready, but untested scale-up and integration remain on the critical path.
9. **Warm-standby trade-off?** Faster complete environment, with cost, drift, and capacity risk.
10. **Active-active trade-off?** Potential continuity, with hard data, conflict, routing, and operational problems.
11. **Replication plus backup?** Replication serves availability; historical isolated backups serve corruption and cyber recovery.
12. **Single writer plus fencing?** One mutation authority and a mechanism that blocks the former primary.
13. **Failover inputs?** Impact, confidence, scope, lag, target health, security state, capacity, and primary recovery prospect.
14. **Failback sequence?** Stabilize, choose truth, synchronize, reconcile, test, shift gradually, verify, restore protection.
15. **Cyber recovery difference?** Recover trusted identities and clean data in isolation; ordinary failover may propagate compromise.
16. **Control-plane risk?** Emergency creation, permission, quota, or configuration calls may be impaired or slow.
17. **Recovery dependency order?** Access/network/keys/data/platform/application/integration/observability/business validation.
18. **Runbook essentials?** Trigger, authority, roles, prerequisites, evidence, decisions, validation, communication, and failback.
19. **Exercise ladder?** Review, tabletop, component restore, technical simulation, integrated exercise, bounded interruption.
20. **Recovery metric?** End-to-end business result under a named scenario, not backup or server status alone.
21. **Manual workaround test?** Throughput, duration, staffing, access, security, data capture, and reconciliation.
22. **Third-party control?** Evidence and contract plus technical isolation, alternatives, contacts, data exit, and tests.
23. **Multi-cloud decision?** Compare concentration-risk reduction with duplicated data, identity, tooling, skills, and tests.
24. **Governance loop?** Inventory, objectives, owner, exercise, finding, risk decision, remediation, and retest.
25. **Architect answer shape?** Outcome → impact/objective → failure → design → operation → evidence → trade-off/residual risk.

Return to the [module overview](index.md) when ready to continue.
