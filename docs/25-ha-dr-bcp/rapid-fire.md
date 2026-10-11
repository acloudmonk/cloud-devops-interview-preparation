# Rapid-Fire Revision

[← Module overview](index.md) · [Active-recall flashcards](flashcards.md)

Answer each in one or two sentences. Expand only when challenged.

1. **What is high availability?** Maintaining an acceptable service through expected failures using redundancy, isolation, detection, and recovery.
2. **What is disaster recovery?** Restoring an agreed technology service after a declared disruption within recovery objectives.
3. **What is business continuity?** Sustaining critical business outcomes across people, process, supplier, facility, communications, and technology disruption.
4. **What is RTO?** The target elapsed time to restore the defined service level.
5. **What is RPO?** The maximum tolerable data-loss interval measured backward from disruption.
6. **What is MTPD?** The maximum tolerable period before disruption impact becomes unacceptable.
7. **What is work recovery time?** Time after technical restoration to validate, reconcile, clear backlog, and resume business operation.
8. **How should RTO relate to MTPD?** RTO plus work recovery time should not exceed MTPD.
9. **Is availability equivalent to RTO?** No; availability measures service success over time, while RTO targets recovery after disruption.
10. **Is replication a backup?** No; replication can copy corruption or malicious deletion and may not retain historical recovery points.
11. **Does a successful backup prove recovery?** No; only a validated restore and business-service test prove useful recovery.
12. **What is a failure domain?** A boundary within which a single fault can affect resources together.
13. **What is common-mode failure?** One cause defeats supposedly redundant paths through a shared dependency or design.
14. **What does Multi-AZ usually protect?** Localized infrastructure failure within a Region, subject to the service and workload design.
15. **Does Multi-AZ provide regional DR?** Not by itself.
16. **What is backup and restore?** Rebuilding service and restoring protected data after disruption.
17. **What is pilot light?** Critical data and core components remain ready while most capacity is provisioned during recovery.
18. **What is warm standby?** A complete but reduced-capacity environment that scales during recovery.
19. **What is multi-site active-active?** Multiple sites concurrently serve production traffic, often requiring coordinated state ownership.
20. **Which DR strategy is best?** The least complex strategy proven to meet business objectives and failure assumptions.
21. **What is a single-writer model?** Only one site owns mutation for a data set at a time.
22. **What is fencing?** Preventing an old or isolated primary from continuing unsafe writes after promotion.
23. **What is split brain?** Multiple nodes or sites believe they are authoritative and accept conflicting changes.
24. **Why is failover not only DNS?** Data, capacity, identity, dependencies, clients, and validation must also be ready.
25. **Why can DNS recovery be slow?** Resolver and client caching, TTL behavior, negative caching, and pinned connections vary.
26. **What is a degraded mode?** A deliberately reduced but safe service used while dependencies or capacity are impaired.
27. **What is recovery sequencing?** Restoring prerequisites before dependent business services in planned waves.
28. **Why pre-create recovery resources?** Emergency control-plane operations, quota requests, and new permissions can fail or extend RTO.
29. **Why protect keys separately?** Encrypted backups are unusable if key material or authorization cannot be recovered.
30. **What is an immutable backup?** A recovery copy whose retention or deletion cannot be altered during its protected period.
31. **What is logical air gap?** Isolation that limits production identities and control paths from modifying protected recovery data.
32. **What is clean-room recovery?** Restoring into a trusted isolated environment after compromise or corruption.
33. **What should stop the RTO clock?** The explicitly agreed, validated business-service level—not infrastructure startup alone.
34. **Who declares a disaster?** A named role with delegated authority using documented thresholds and evidence.
35. **Why separate incident and crisis command?** Technical stabilization and enterprise safety, priority, and communication require different focus.
36. **What is a BIA?** Analysis of business-service impact over time, dependencies, continuity needs, and recovery priority.
37. **Why tier services?** To align scarce recovery investment and sequence with actual business consequence.
38. **What makes a manual workaround credible?** Known capacity, staffing, security, data capture, duration, and reconciliation.
39. **What is a tabletop exercise?** A discussion-based rehearsal of decisions, roles, dependencies, and communication.
40. **What does a restore test prove?** That selected protected data can be recovered under tested conditions; scope must be stated.
41. **What should a DR exercise measure?** Actual RTO/RPO, business validation, failed assumptions, manual work, communications, and recovery capacity.
42. **Why test failback?** Recovery-mode writes and state must return safely without divergence or another outage.
43. **What is recovery drift?** Difference between primary and recovery environments that makes recovery unreliable.
44. **How does IaC support DR?** It creates repeatable infrastructure, but artifacts, state, credentials, quotas, and tests remain necessary.
45. **Why can active-active reduce reliability?** Added coordination, conflicts, latency, and operational paths create new failure modes.
46. **When is multi-cloud DR justified?** When provider concentration risk warrants the complexity and both provider paths can be operated and tested.
47. **What is residual risk?** Risk remaining after controls, explicitly understood and accepted by the accountable owner.
48. **What is recovery evidence?** Dated, scoped measurements and records showing a target was achieved under a named scenario.
49. **What invalidates recovery evidence?** Material changes to architecture, data scale, dependencies, people, objectives, or procedures.
50. **Best closing interview point?** State objective, chosen strategy, proof, trade-off, owner, and residual risk.

Return to the [module overview](index.md) when ready to continue.
