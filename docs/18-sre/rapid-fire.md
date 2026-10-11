# SRE Rapid-Fire Revision

[← Module overview](index.md) · [Active-recall flashcards](flashcards.md)

Answer each in one or two sentences, then add a business or failure trade-off.

1. **SRE?** Applying software-engineering methods to operations to meet explicit reliability objectives sustainably.
2. **Reliability?** Ability to perform the intended function correctly and consistently when expected and recover from disruption.
3. **Is SRE renamed operations?** No; it adds objective-based risk governance, engineering, automation, and learning while operations remains essential.
4. **Reliability versus availability?** Availability is one dimension; reliability can also include correctness, latency, durability, and recovery.
5. **SLI?** Quantitative measure of service behavior that matters to users.
6. **SLO?** Internal target for an SLI over a defined window.
7. **SLA?** Business/legal commitment defining scope, measurement, and consequences.
8. **Error budget?** Tolerable unreliability implied by an SLO, used as a risk signal.
9. **Error-budget formula?** Allowed bad fraction equals one minus the SLO target.
10. **Should a budget be consumed?** No; it is a limit and decision input, not an outage quota.
11. **Budget exhausted response?** Apply pre-agreed risk controls and reliability priorities, not a universal change freeze.
12. **Why journey-specific SLOs?** Averaging critical and low-value behavior can hide unacceptable user impact.
13. **Serial dependency availability?** Approximate by multiplying independent required component availabilities.
14. **Why independence matters?** Shared zones, control planes, identity, data, configuration, and operators create correlated failure.
15. **RTO?** Target duration to restore a capability after disruption.
16. **RPO?** Maximum tolerable data-loss period measured backward from disruption.
17. **MTTR limitation?** An average hides impact distribution, severe outliers, and differing definitions.
18. **Bulkhead?** Isolation boundary limiting one workload/failure from consuming all shared capacity.
19. **Circuit breaker?** Stops or limits calls to a failing dependency to prevent amplification and allow recovery.
20. **Retry requirement?** Bounded attempts, timeout budget, backoff/jitter, idempotency, and overload awareness.
21. **Graceful degradation?** Preserve critical user value by disabling or reducing noncritical behavior safely.
22. **Incident commander?** Owns priorities, coordination, risk, and shared state—not every technical command.
23. **First incident priority?** Stabilize user impact and protect data/safety before proving root cause.
24. **Useful incident update?** Impact, scope, start/status, mitigation, uncertainty, workaround, and next update time.
25. **Blameless?** Analyze decisions in context without punishment while preserving accountability for system improvement.
26. **Root-cause limitation?** Complex incidents often require multiple conditions and failed defenses; one root oversimplifies learning.
27. **Strong corrective action?** Owned, prioritized, time-bound, risk-linked, and verified to change system behavior.
28. **Near-miss value?** Reveals a hazard when impact was avoided by defense or luck.
29. **Toil?** Repetitive, manual, automatable, tactical service work that scales with service growth and has low enduring value.
30. **Is all manual work toil?** No; judgment, design, learning, and rare high-risk operations can be valuable.
31. **Best first toil action?** Eliminate unnecessary demand before automating it.
32. **Safe automation?** Scoped, idempotent, observable, least privileged, bounded, stoppable, and recoverable.
33. **Automation paradox?** Humans handle fewer routine cases but more novel severe failures, so skills can decay.
34. **Capacity planning inputs?** Business demand, resource translation, peak/failure shape, bottlenecks, quotas, lead time, and uncertainty.
35. **Little's Law?** In steady conditions, concurrency equals throughput times average time in system.
36. **Why tail latency?** User and dependency experience is often dominated by slow outliers hidden by averages.
37. **Autoscaling limitation?** It cannot overcome slow startup, fixed quotas, state bottlenecks, or dependency saturation.
38. **Headroom purpose?** Absorb demand error, zone loss, deployment, replay, debugging, and scaling delay.
39. **Load versus stress test?** Load validates expected demand; stress discovers limits and failure behavior beyond it.
40. **Soak test?** Sustained load test exposing leaks, queue growth, compaction, or degradation over time.
41. **Progressive delivery?** Increase exposure in controlled stages using health evidence and abort/rollback criteria.
42. **Why rollback may fail?** Data, schema, messages, configuration, caches, or dependencies may be incompatible with old code.
43. **Game day?** Planned exercise of people, process, communication, and technology against a scenario.
44. **Chaos engineering?** Controlled experimentation that tests a reliability hypothesis under injected fault.
45. **Chaos prerequisite?** Stable baseline, bounded scope, owner, observers, abort, recovery, and business safety.
46. **Operational readiness?** Evidence that ownership, SLOs, alerts, runbooks, capacity, change, recovery, access, and on-call are ready.
47. **Healthy on-call?** Actionable volume, trained staffing, clear authority, fair rotation, handover, escalation, and recovery time.
48. **SRE engagement risk?** Becoming an unbounded operations/ticket queue that removes product ownership.
49. **Provider SLA limitation?** It is a provider commitment, not the application's end-to-end user SLO or recovery capability.
50. **Best reliability question?** What user promise are we making, which risk dominates, and how have we proved recovery?

Return to the [module overview](index.md) when ready to continue.
