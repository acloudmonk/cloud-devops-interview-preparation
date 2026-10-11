# Rapid-Fire Revision

[← Presentation template](presentation-template.md) · [Next: Flashcards →](flashcards.md)

Answer each in one or two sentences before expanding with an example.

1. **Why is “move to cloud” not a business outcome?** It names a destination, not measurable value, risk reduction, or user change.
2. **What is transition architecture?** The identities, paths, data authority, synchronization, controls, and operations required while current and target states coexist.
3. **Why record discovery confidence?** Inventory facts differ in freshness and reliability; confidence focuses validation and informs risk.
4. **What makes an application boundary useful?** It groups behavior, data, dependencies, ownership, and change that can be decided and validated coherently.
5. **What is portfolio rationalization?** Selecting an evidence-based disposition for each workload or meaningful component.
6. **Name the seven common dispositions.** Rehost, replatform, refactor/re-architect, repurchase, relocate, retire, and retain.
7. **When is rehost reasonable?** When deadline and compatibility dominate and moved debt has an owned treatment or acceptable risk.
8. **What is the danger of rehost?** It can preserve fragility, licensing, manual operations, and inefficient cost.
9. **What distinguishes replatform from refactor?** Replatform makes bounded platform changes; refactor materially changes application architecture or code.
10. **When is retain a good decision?** When movement cost/risk exceeds value and there is a support, integration, and review plan.
11. **What must be proven before retirement?** Actual usage, dependency, records, regulatory, contractual, and business-owner acceptance.
12. **Why can repurchase be difficult?** SaaS replacement changes process, identity, integration, data migration, configuration, vendor risk, and exit.
13. **What belongs in a migration business case?** Delivery, dual run, cloud, network, people, license, support, risk, decommissioning, contingency, and benefits.
14. **Why use sensitivity analysis?** Demand, schedule, exchange rate, savings, and shutdown assumptions are uncertain.
15. **What is a landing zone?** A governed, operable cloud foundation and delivery capability, not merely accounts and networks.
16. **What proves landing-zone readiness?** A representative workload successfully traverses delivery, control, operation, recovery, and cost paths.
17. **Why check service quotas before a wave?** Quota lead time or exhaustion can block deployment or fail under load.
18. **What is a wave?** A planned group of workloads and dependencies moving through shared readiness, cutover, acceptance, and closure.
19. **How should waves be grouped?** By business capability, dependency, calendar, risk, data, platform, and team capacity.
20. **What makes a good first wave?** Valuable, representative, recoverable, testable, owned, and capable of improving later patterns.
21. **Why avoid a trivial pilot?** It fails to exercise difficult production capabilities and creates false confidence.
22. **What is a migration factory?** Repeatable cross-functional flow and automation from intake through decommissioning.
23. **Which factory metrics matter?** Wait time, blocker age, work in progress, rework, defect escape, gate pass, stability, and closure.
24. **What is a wave entry gate?** Evidence that scope, ownership, dependencies, disposition, target, funding, and platform prerequisites are ready.
25. **What is cutover readiness?** Rehearsed runbook, synchronized data, acceptance evidence, monitoring, support, communications, and viable abort plan.
26. **What is data authority?** The system and path permitted to accept authoritative writes at a given transition phase.
27. **Why is dual write dangerous?** Independent writes can partially fail, reorder, duplicate, or conflict across systems.
28. **What does fencing achieve?** It prevents multiple systems or actors from simultaneously acting as authority.
29. **What is CDC?** Change data capture transfers committed source changes after or alongside a baseline copy.
30. **What limits a rollback?** Time, irreversible schema/state changes, new target writes, external actions, and loss of source compatibility.
31. **What is the last safe rollback point?** The latest moment rollback can restore coherent service and data within approved loss and time.
32. **Why is backup not a complete rollback plan?** Restore duration, lost writes, routing, dependencies, validation, and reconciliation remain unresolved.
33. **What should reconciliation test?** Counts, keys, aggregates, business invariants, deletes, history, permissions, and downstream outputs.
34. **Why continue reconciliation after cutover?** Delayed jobs, rare paths, and asynchronous consumers can reveal later divergence.
35. **What is a go/no-go criterion?** A pre-agreed measurable condition used by an accountable authority to proceed, hold, or abort.
36. **What is operational acceptance?** Evidence that an owned service can be observed, supported, secured, recovered, changed, and paid for.
37. **What is hypercare?** Temporary enhanced observation and response after cutover with explicit exit criteria.
38. **Why test failures before migration?** Nominal success does not prove alerts, recovery, access, data integrity, or operator response.
39. **How should control mapping work?** Preserve control objectives while mapping current, transition, and target implementations and evidence.
40. **How should migration exceptions be governed?** Scope, owner, risk acceptance, compensating control, expiry, and remediation.
41. **Which temporary identities are easy to miss?** Vendor users, agents, pipelines, transfer services, migration operators, and break-glass access.
42. **Why are temporary data copies risky?** They can bypass residency, encryption, retention, access, masking, and deletion controls.
43. **What is modernization?** A change to technology and ways of working intended to improve a measurable business or engineering constraint.
44. **Why separate migration from later modernization?** It reduces simultaneous change and lets operational evidence guide deeper investment.
45. **What may require pre-move modernization?** Unsupported runtime, hard-coded identity, incompatible licensing, or an unmovable dependency.
46. **What is the strangler pattern?** Incrementally route bounded capabilities to a replacement while legacy behavior remains available.
47. **Why can containerization fail to add value?** Packaging alone may preserve architecture, manual operations, fragility, and cost.
48. **What is value realization?** Measuring whether owned benefits occur after delivery and correcting or stopping when they do not.
49. **Why track unit economics?** Total spend without business volume can hide whether efficiency improved or demand merely changed.
50. **Why delay long-term commitments?** Post-migration demand and sizing often differ from estimates; premature commitments lock in waste.
51. **What creates stranded cost?** Migrated workloads whose hardware, licenses, facilities, people processes, or contracts remain active.
52. **What proves decommissioning?** Approved records handling, dependency removal, shutdown, sanitization, inventory updates, contract closure, and cost removal.
53. **How should multi-cloud services be compared?** By required semantics, limits, control evidence, operations, recovery, skills, cost, and exit—not names.
54. **When is provider-specific capability justified?** When its measurable value exceeds portability and switching risk for that workload.
55. **When is migration truly complete?** When business, technical, operational, security, legacy, financial, and benefit closure all have evidence.
