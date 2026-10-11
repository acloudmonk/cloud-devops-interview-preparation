# Google Cloud Well-Architected Review

[← Cost and capacity](cost-capacity.md) · [Next: Design exercise →](design-exercise.md)

The current Google Cloud Well-Architected Framework has six pillars:

1. operational excellence;
2. security, privacy, and compliance;
3. reliability;
4. cost optimization;
5. performance optimization;
6. sustainability.

It also has cross-pillar perspectives. Use it as a review method, not a certification
checklist or substitute for workload context.

## Review workflow

1. Define scope, journeys, stakeholders, data, SLOs, and constraints.
2. Gather diagrams, inventories, policy, telemetry, incidents, costs, and restore tests.
3. Review every pillar with platform and workload owners.
4. State risk as condition → failure → impact → evidence.
5. Rank likelihood, impact, urgency, dependency, and effort.
6. Assign owner, date, acceptance criteria, and evidence.
7. Revisit after material change or on a defined cadence.

Ask whether teams can operate safely; identities and data are layered; recovery is
proved; spend is attributable; peak performance is measured; and avoidable resource
consumption is minimized. “Regional recovery depends on an untested KMS and DNS path”
is actionable; “improve DR” is not.
