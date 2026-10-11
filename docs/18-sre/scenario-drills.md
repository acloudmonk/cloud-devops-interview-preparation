# Advanced SRE Incident Drills

[← Module overview](index.md) ·
[Scenario answer framework](../interview-playbook/scenario-answer-framework.md)

For each drill, state user impact, incident roles, first stabilization, data and
evidence protection, communication, recovery proof, and prevention.

## 1. Retry storm during a dependency brownout

Reduce retry amplification, shed or queue noncritical work, constrain concurrency,
activate circuit/fallback behavior, and protect the recovering dependency. Track
user outcome and queue age, coordinate owner/vendor, then tune timeouts, bounded
retry budgets with jitter, idempotency, and load tests for partial failure.

## 2. Error-budget dashboard shows healthy during confirmed impact

Declare from credible customer evidence, do not wait for the SLI. Check measurement
point, valid/good classification, telemetry freshness, exclusions, route/version,
and client/dependency blind spots. Mitigate service, preserve the faulty evidence,
repair/backfill carefully, and govern SLI data quality and synthetic checks.

## 3. Database failover succeeds but application remains unavailable

Validate DNS/endpoint, connection pools, credentials, transaction state, replica
lag, caches, and client retry behavior; recycle connections in controlled waves
and protect data. Verify read/write correctness from the user path. Test the whole
application recovery, not only the managed database event.

## 4. Incident commander is also debugging and stops communicating

Transfer command or technical work explicitly, appoint communications and scribe,
restore update cadence, summarize impact/actions/risks, and reduce parallel work.
Afterward improve staffing, role triggers, exercises, and authority so critical
coordination does not depend on one expert.

## 5. Autoscaling reaches the cloud-service quota

Protect critical traffic, shed/degrade lower-priority work, redistribute within
tested capacity, request emergency quota help, and stop retry amplification.
Forecast quota/headroom including zone loss and deployments, pre-scale, diversify
bottlenecks where justified, and alert with provider lead time.

## 6. Canary looks healthy while full rollout fails

Stop/rollback exposure safely, compare traffic cohorts, data, dependencies,
capacity, cache state, flags, regions, and sample size. The canary may have missed
high-risk tenants or shared saturation. Add representative cohorting, minimum
evidence, dependency/capacity signals, and staged exposure constraints.

## 7. Automation deletes healthy capacity across regions

Disable the automation and credentials, halt propagation, restore minimum capacity
through separated emergency authority, preserve decisions/configuration/audit logs,
and verify user recovery. Add scope boundaries, canaries, rate limits, two-person
control for fleet-wide actions, dry run, invariants, and kill switch.

## 8. A chaos experiment causes unexpected customer impact

Abort and restore using the pre-agreed path, declare impact, preserve experiment
and system evidence, and communicate honestly. Review violated prerequisites,
blast-radius enforcement, steady-state metric, hidden dependency, and abort delay;
pause expansion until corrective actions and a smaller validation succeed.

## 9. Postmortem actions are repeatedly overdue

Escalate active residual risk to named owners, re-rank actions with product work,
remove weak or duplicate tasks, fund high-impact systemic controls, and verify
completed outcomes. Track aging/recurrence at leadership review and make deferral
an explicit risk decision instead of an invisible ticket state.

## 10. On-call exhaustion creates a second incident

Rotate responders, simplify command, bring trained backup, reduce nonessential
change/work, and protect decision quality. Communicate staffing risk. Review alert
load, shift duration, handover, escalation, staffing, recovery time, and chronic
toil; correct the service and human system rather than blaming the responder.

Return to the [module overview](index.md) when ready to continue.
