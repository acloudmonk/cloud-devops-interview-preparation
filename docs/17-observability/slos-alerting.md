# SLIs, SLOs, Alerting, and Response

[← Module overview](index.md) · [Scenario answer framework](../interview-playbook/scenario-answer-framework.md)

An SLI measures a user-relevant behavior; an SLO sets its acceptable target over
a window; an error budget expresses permitted unreliability. Observability provides
evidence, but service owners must choose the promise and response.

## SLI design

Define the population, good event, valid event, measurement point, exclusions,
window, source, delay, and owner. Prefer request-based ratios where each valid
event can be classified. Time-based availability may suit continuously available
resources. Align latency thresholds to user and business behavior, not averages.

Measurements from a load balancer reveal edge experience but may miss client-side
failure; application measurements carry domain correctness but may disappear in
catastrophic failure; synthetic tests cover selected journeys but are not all users.
Use the most representative point and state blind spots.

## Error-budget reasoning

For a target `SLO`, the budget fraction is `1 - SLO`. Budget consumption connects
incidents, release risk, engineering investment, and product trade-offs. Do not
turn the budget into permission to cause outages or a performance score for teams.
Low-traffic services need careful windows and absolute-event context.

## Burn-rate alerts

Burn rate compares observed bad-event rate with the allowed error rate. A burn
rate of 1 consumes budget exactly at the planned rate; higher values consume it
faster. Combine a fast/high-burn window for severe incidents with a slower/lower-
burn window for sustained degradation. Requiring both short and long windows can
reduce noise while retaining urgency.

## Alert quality

Page only for urgent, actionable user or system risk requiring immediate human
judgment. Create tickets for non-urgent owned work and dashboards for exploration.
Every alert needs service, environment, impact, owner, severity, current evidence,
runbook, safe first actions, and escalation. Test firing, routing, inhibition,
silence expiry, no-data/error states, and recovery notification.

## Symptom and cause

Page primarily on symptoms such as SLO burn, failed critical journey, exhausted
capacity, or loss of safe redundancy. Attach probable-cause evidence rather than
paging separately for every CPU, pod, dependency, and log symptom. Cause alerts
remain appropriate when imminent failure can be prevented before user impact.

## Alert lifecycle

Treat alerts as versioned products: define expected behavior, test with historical
and synthetic data, deploy gradually, review after incidents, and remove those
without an owner or action. Track pages per shift, duplicates, acknowledgment,
false positives/negatives, auto-resolution, runbook success, and repeated causes.

Return to the [module overview](index.md) when ready to continue.
