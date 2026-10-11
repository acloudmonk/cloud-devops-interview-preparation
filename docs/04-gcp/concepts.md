# GCP Architecture Decision Model

[← Module overview](index.md) · [Next: Global infrastructure →](global-infrastructure.md)

## Start with the workload

Capture users, critical journeys, data classification, compliance, demand shape,
latency, availability, RTO/RPO, portability, skills, budget, and change rate. Turn
"highly available" into a measurable service objective and failure model.

## Make decisions in order

1. Define outcomes, SLOs, constraints, and ownership.
2. Draw organization, folder, project, billing, and trust boundaries.
3. Place components by service scope and failure independence.
4. Choose identity, network, runtime, data, and integration semantics.
5. Design deployment, observability, degradation, backup, and recovery.
6. Test quotas, cost, security, operability, and exit triggers.

## Separate four concerns

The **resource hierarchy** supplies governance inheritance. The **control plane**
configures resources. The **data plane** serves workload traffic. The **management
plane** of the enterprise platform vends projects and common capabilities. A healthy
design makes dependencies and emergency procedures for each explicit.

## Interview answer loop

Use **clarify → decide → justify → fail → operate → verify**. Name an alternative,
why it loses under current constraints, evidence that validates the choice, and a
trigger that would cause redesign.

## Common weak answers

- treating a project as only a billing label;
- assuming a multi-zone product makes the whole journey resilient;
- using service-account keys where federation is possible;
- confusing IAM authorization with Organization Policy constraints;
- ignoring quotas, regional availability, downstream limits, or recovery tests.
