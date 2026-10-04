# Lab: Title

## Objective

Describe the skill or decision the learner will demonstrate.

## Prerequisites

- Tools
- Accounts
- Background knowledge

## Cost and safety

State expected cloud cost, credential requirements, data sensitivity, and hard
limits. Never assume free-tier eligibility.

Include a sandbox requirement, budget alert, required tags, short-lived
authentication, service quotas, regional availability, and resources that may
continue to incur cost after compute stops.

## Scenario

Provide business context, constraints, and non-functional requirements.

## Tasks

For every phase include the goal, exact command or configuration direction,
expected result, objective checkpoint, troubleshooting notes, and cleanup.

1. Quantify requirements, invariants, capacity, SLOs, RTO, and RPO.
2. Prove correctness locally before creating cloud resources.
3. Provision the AWS reference with IaC unless another cloud is topic-specific.
4. Add identity, network, data protection, and secret controls.
5. Add delivery, observability, and rollback.
6. Run load, failure, and recovery tests with bounded blast radius.
7. Translate relevant capabilities to Azure and GCP by semantics.

## Deliverables

- Architecture diagram
- Decision record
- Code or configuration
- Test evidence
- Cost estimate

## Validation

List objective checks and expected results. Validate business invariants,
duplicate delivery, partial failure, overload behavior, rollback, and measured
recovery—not only resource health.

## Evidence

- Tool and configuration versions
- Sanitized command/test output
- Dashboard or trace references
- Architecture Decision Records
- Load and fault experiment reports
- Measured RTO/RPO and cost

## Teardown

List every resource that must be removed and how removal is verified by tag and
service. Include retained logs, images, backups, snapshots, IP addresses,
replicas, secrets, keys, and state infrastructure.

## Reflection

Ask what would change at 10× scale, under a stricter RTO/RPO, or with a lower
budget.
