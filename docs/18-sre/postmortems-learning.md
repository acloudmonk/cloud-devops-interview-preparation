# Postmortems and Organizational Learning

[← Module overview](index.md) · [Incident response](incidents-response.md)

A postmortem reconstructs how system conditions, design, change, signals,
procedures, incentives, and human decisions combined to create impact. Blameless
means decisions are examined in context without punishment; it does not mean
weak analysis or absence of accountability for improvement.

## When to review

Use defined triggers such as significant user impact, data/security risk, SLO burn,
failed recovery, repeated incident, dangerous near miss, or surprising dependency
behavior. Scale review depth to learning value and risk. Review near misses because
the absence of impact may have been luck.

## Postmortem structure

1. Executive summary and user/business impact.
2. Detection, response, mitigation, recovery, and communication assessment.
3. Evidence-based timeline with relevant changes and decisions.
4. Technical and organizational contributing conditions.
5. What worked, what failed, and where understanding differed from reality.
6. Corrective actions with owner, priority, due date, verification, and status.
7. Lessons for other services, standards, training, architecture, and SLOs.

Avoid a single "root cause" when several defenses and conditions mattered. Ask
why the action made sense with information available, how the system permitted
it, why detection/containment failed, and which counterfactual controls would
actually have changed impact.

## Corrective-action quality

Prefer eliminating a hazard or adding systemic prevention, containment,
detection, recovery, and validation over reminders and retraining alone. Include
short-term risk reduction and durable work. Assign risk owners for deferred or
rejected actions and record why the residual risk is accepted.

Actions are not complete when a ticket closes. Define evidence: a test passes,
recovery meets objective, unsafe permission is gone, alert detects the condition,
capacity margin exists, or recurrence class is prevented. Track aging and repeat
incidents across teams.

## Learning system

Share concise lessons, patterns, and reusable controls without exposing sensitive
data. Aggregate themes across incidents: change, capacity, dependency, access,
observability, automation, procedure, or organization. Feed them into platform
roadmaps, architecture reviews, training, vendor decisions, and investment.

## Facilitation safeguards

Separate disciplinary or legal processes from technical learning when necessary;
do not promise confidentiality the organization cannot provide. Include responders
and affected owners, challenge hindsight bias, distinguish fact from inference,
and review whether workload and on-call pressure contributed.

Return to the [module overview](index.md) when ready to continue.
