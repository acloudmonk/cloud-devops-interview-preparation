# Toil, Automation, and Operational Engineering

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Toil is repetitive, manual, automatable, tactical work tied to running a service
that scales roughly with service growth and creates little enduring value. Not all
operations or manual work is toil: incident judgment, design, learning, and a
rare high-risk migration may be valuable human work.

## Identify and measure toil

Record task, trigger, frequency, duration, interruption cost, error/risk, required
judgment, growth driver, owner, and candidate control. Include ticket queues,
access requests, deployments, certificate/secret rotation, capacity adjustment,
alert cleanup, data repair, restart, failover, and evidence collection.

Measure enough to prioritize without making engineers account for every minute.
High-volume low-risk work may suit self-service; rare high-impact work may need
better procedure, simulation, or product redesign before automation.

## Response ladder

1. **Eliminate** unnecessary task or failure source.
2. **Simplify/standardize** input, ownership, and procedure.
3. **Expose safe self-service** with policy and evidence.
4. **Automate** deterministic decisions and actions.
5. **Redesign** architecture when the task is a symptom of a poor boundary.

Automation should reduce total risk and cognitive load, not merely move toil to
another team or create a fragile script only one person understands.

## Safe automation contract

Define preconditions, validated inputs, idempotency, scope, permissions, concurrency,
timeouts, retries, rate limits, approval, dry run, observability, rollback or
compensation, audit, owner, support, and decommissioning. Test partial completion,
stale state, duplicate execution, dependency failure, and emergency stop.

## Automation paradox

As normal work becomes automated, humans see fewer routine cases but handle more
novel and severe failures. Preserve operational competence with game days,
explainable state, manual recovery paths, training, and rotation. Avoid automation
that hides system state or allows one control-plane error to affect the whole fleet.

## Prioritization

Compare annual time/risk avoided with implementation, maintenance, platform,
security, and migration cost. Prioritize work that removes recurring incident
classes, reduces dangerous privilege, shortens recovery, or unlocks team capacity.
Time-box low-value automation and retire it when the underlying service disappears.

## Outcome measures

Track task frequency and duration, interruption, manual error, queue age, automation
success/rollback, support load, recurrence, engineering time returned, and whether
demand was eliminated. A growing automation repository can coexist with growing toil.

Return to the [module overview](index.md) when ready to continue.
