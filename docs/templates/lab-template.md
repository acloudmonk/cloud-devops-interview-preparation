# Architecture Design Exercise: Title

## Objective

Describe the skill or decision the learner will demonstrate.

## Prerequisites

- Prior module pages
- Background knowledge
- Optional diagramming or note-taking tool

## Scope and cost

The default exercise is completed on paper or a whiteboard and has no cloud
cost. It must not require credentials, application code, infrastructure
deployment, or a cloud account. Any practical implementation belongs in a
separately approved future milestone.

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

- Requirements and assumptions table
- Capacity and service-objective model
- Architecture diagram
- Option comparison and decision record
- Failure-mode and recovery table
- Security and trust-boundary notes
- Observability and validation plan
- Cost drivers and delivery phases
- Timed verbal presentation

## Validation

List the questions, calculations, review criteria, and proposed experiments that
would validate business invariants, duplicate delivery, partial failure,
overload behavior, rollback, and recovery. The learner designs the evidence;
running an implementation is not required.

## Evidence

- Explicit assumptions and sensitivity analysis
- Architecture Decision Records
- Proposed customer and system signals
- Proposed load, fault, rollback, and recovery experiments
- Defensible RTO/RPO and cost model

## Scoring

Define observable weak, acceptable, strong, and architect-level signals for
requirements, trade-offs, correctness, failure handling, security, operations,
economics, delivery, and communication.

## Reflection

Ask what would change at 10× scale, under a stricter RTO/RPO, or with a lower
budget.
