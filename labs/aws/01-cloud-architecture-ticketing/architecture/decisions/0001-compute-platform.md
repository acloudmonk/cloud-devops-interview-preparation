# ADR 0001: Compute platform

- Status: Proposed
- Date: YYYY-MM-DD
- Owners: Team or role
- Review trigger: Material change in workload shape, platform skills, or cost

## Context

Describe synchronous and background workloads, traffic shape, latency,
portability, operating model, delivery deadline, and constraints.

## Decision

Use ECS on Fargate for the AWS reference implementation. Explain the task and
service boundaries, scaling signal, deployment strategy, and failure domains.

## Alternatives considered

|Option|Benefits|Costs/risks|Evidence needed|
|---|---|---|---|
|AWS Lambda|To complete|To complete|To complete|
|Amazon EKS|To complete|To complete|To complete|
|EC2 Auto Scaling|To complete|To complete|To complete|

## Consequences

Record positive, negative, migration, cost, security, and operational effects.

## Validation

State the load, deployment, rollback, task-loss, and recovery tests that prove
the decision is fit for purpose.
