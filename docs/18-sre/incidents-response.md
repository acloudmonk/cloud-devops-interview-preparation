# Incident Response and Communication

[← Module overview](index.md) · [Scenario answer framework](../interview-playbook/scenario-answer-framework.md)

Incident response restores acceptable service safely while managing uncertainty,
coordination, and communication. Root-cause analysis is secondary during active
impact unless understanding cause is necessary for safe mitigation.

## Incident lifecycle

1. **Detect and declare:** confirm credible impact, set severity, open records and communication.
2. **Command and scope:** assign roles, identify affected users/journeys, establish priorities.
3. **Stabilize:** stop unsafe change, shed load, fail over, degrade, scale, isolate, or roll back.
4. **Investigate:** form and test hypotheses using timelines, changes, signals, and experiments.
5. **Recover:** restore service and data, verify from user perspective, watch for recurrence.
6. **Handover/close:** record residual risk, owners, monitoring period, communication, and follow-up.

## Roles and authority

- **Incident commander:** sets priorities, assigns work, manages risk, and keeps the shared picture.
- **Operations/technical leads:** investigate and execute scoped mitigation.
- **Communications lead:** provides accurate internal/customer/stakeholder updates.
- **Scribe:** maintains timeline, hypotheses, decisions, actions, and evidence.
- **Subject experts and liaison roles:** join as needed without creating parallel command.

One person may initially hold several roles, but separate them as severity and
duration grow. Define authority for rollback, traffic shift, emergency access,
vendor escalation, customer communication, and business continuity before crisis.

## Technical response discipline

Create a timestamped fact/hypothesis/decision log. Change one important variable
at a time where possible, state expected result and rollback, use peer confirmation
for dangerous actions, and preserve evidence. Prefer reversible mitigation and
known runbooks, but do not let a stale procedure override observed reality.

## Communication

State impact, scope, start time, current status, mitigation, uncertainty, next
update time, and workarounds without unsupported cause or recovery estimates.
Use consistent severity and channels. Internal detail may differ from customer
communication, but facts must not conflict. Communicate material recovery risk
and data-integrity uncertainty explicitly.

## Handover and long incidents

Track roles, system state, actions completed/in progress, hypotheses, risks,
dependencies, access, next decisions, and communication commitments. Rotate
responders before cognitive exhaustion. A warm verbal handover plus written state
is safer than a transcript dump.

## Measures

Measure detection, declaration, engagement, mitigation, recovery, communication,
recurrence, and user impact with context. Avoid turning response-time measures
into incentives to declare prematurely, hide incidents, or choose unsafe shortcuts.

Return to the [module overview](index.md) when ready to continue.
