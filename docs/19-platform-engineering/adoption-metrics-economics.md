# Adoption, Metrics, and Economics

[← Reliability and platform operations](reliability-operations.md) · [Next: Enterprise design exercise →](design-exercise.md)

## Adoption is an outcome signal

Pilot with teams whose problems match the first path. Pair during migration, collect
qualitative and behavioral feedback, and improve before expansion. Mandates can
create nominal adoption while teams bypass controls or keep parallel workflows.

## Balanced measures

| Dimension | Examples |
| --- | --- |
| Flow | environment lead time, deployment wait, onboarding time |
| Quality/reliability | change failure, recovery time, policy escapes, SLO attainment |
| Experience | task success, cognitive load, satisfaction, support effort |
| Adoption | active teams, repeat use, path completion, supported-version coverage |
| Economics | platform cost/team, successful deployment cost, duplicated tooling retired |

Use DORA-style measures at the correct service/team boundary and combine them with
developer experience and business outcomes. Lines of platform code, portal logins,
templates created, and infrastructure count are activity—not proof of value.

## Migration strategy

Segment consumers by readiness and risk. Provide automated assessment, migration
guides, office hours, compatibility bridges, and deadlines tied to supported
versions. Track time-to-value and failure demand. Retire old paths only after users
can succeed and critical exceptions have owners.

## Economics and capacity

Model people, licenses, shared cloud services, support, upgrades, and migration—not
just infrastructure. Compare platform investment with reduced duplicated work,
wait time, incidents, audit effort, and time to business value. Track unit cost per
active team or successful workflow while guarding against perverse cost shifting.

## Continuous discovery

Review journey telemetry, interviews, support themes, exceptions, incidents, and
roadmap outcomes. Stop or simplify capabilities with weak value. The platform is
never “finished”; its purpose is sustained customer outcomes under changing risk
and technology.
