# Advanced Distributed-Estate Drills

[← Module overview](index.md) · [Scenario questions](scenarios.md)

Use five minutes per drill. Cover impact, facts, command, containment, data/trust,
recovery, communication, reconciliation, and prevention.

1. **Route leak:** on-premises advertises a default route into two clouds; contain propagation and restore deterministic paths.
2. **DNS forwarding loop:** hybrid private names intermittently fail; isolate resolvers, caches, ownership, and cycle prevention.
3. **Certificate expiry:** one cross-cloud gateway expires during peak demand; restore trust without bypassing authentication.
4. **Replication backlog:** link loss fills queues and threatens storage; prioritize, shed, preserve order, and reconcile.
5. **Compromised CI:** signed artifacts across three environments are suspect; halt delivery, establish trust, rebuild, and attest.
6. **Edge clock drift:** offline factories generate conflicting event times; use sequence/domain rules and repair time synchronization.
7. **Carrier common mode:** “diverse” links share one metro; sustain critical service and redesign physical independence.
8. **Provider API outage:** workloads run but autoscaling/configuration cannot change; use pre-provisioned data-plane operation and capacity policy.
9. **Acquisition identity collision:** duplicate user identifiers grant wrong access; stop federation, map immutable identities, and review authorization.
10. **Exit rehearsal fails:** data exports are incomplete and target performance is poor; quantify gap, fix format/capacity, and reset risk expectation.

## Self-review

- Did I protect customer/safety outcome before restoring architecture symmetry?
- Did I identify common-mode identity, DNS, carrier, CI/CD, and operator dependencies?
- Did I state authoritative data and reconciliation behavior?
- Did I preserve native evidence while using one incident command?
- Did I turn a recurring gap into a platform, contract, or governance improvement?

Return to the [module overview](index.md) when ready to continue.
