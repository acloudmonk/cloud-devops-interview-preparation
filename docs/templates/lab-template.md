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

For the current interview curriculum, default to a no-cost paper/design lab.
Mark executable or cloud-deployment work as an optional future extension.

Include a sandbox requirement, budget alert, required tags, short-lived
authentication, service quotas, regional availability, and resources that may
continue to incur cost after compute stops.

## Scenario

Provide business context, constraints, and non-functional requirements.

## Tasks

For every phase include the question being answered, assumptions, expected
evidence, decision criteria, and interview follow-ups.

1. Quantify requirements, invariants, capacity, SLOs, RTO, and RPO.
2. Explain how correctness would be validated under concurrency and retries.
3. Produce an AWS reference design unless another cloud is topic-specific.
4. Add identity, network, data protection, and trust boundaries.
5. Explain delivery, observability, rollback, and ownership.
6. Design load, failure, and recovery experiments with bounded blast radius.
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
- Proposed load and fault experiment evidence
- Defensible RTO/RPO and cost model

## Teardown

List every resource that must be removed and how removal is verified by tag and
service. Include retained logs, images, backups, snapshots, IP addresses,
replicas, secrets, keys, and state infrastructure.

## Reflection

Ask what would change at 10× scale, under a stricter RTO/RPO, or with a lower
budget.
