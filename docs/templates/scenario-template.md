# Scenario: Concise Problem Statement

## Prompt

Describe the ambiguous business and technical situation.

## What the interviewer is testing

Name the architecture judgment, distributed-systems concept, operational
skill, and communication behavior being assessed.

## Clarifying questions

- Business outcome?
- Scale and growth?
- Latency and availability?
- RTO and RPO?
- Security, compliance, and residency?
- Budget, timeline, and team constraints?

## Assumptions

State reasonable assumptions if the interviewer withholds information.

## Candidate options

Describe at least two feasible approaches.

## Recommended answer

Use the CLEAR-DOC framework from the interview playbook.

### Answer outline

1. Confirm the business outcome and the most important constraint.
2. State assumptions and measurable targets.
3. Compare at least two credible options.
4. Recommend one option and explain why it fits.
5. Walk through failure, recovery, security, observability, and cost.

## AWS anchor

Map the design to AWS capabilities by behavior, not by producing a service
catalog. Explain important limits and operational consequences.

## Multi-cloud translation

Identify the equivalent Azure and Google Cloud capabilities and call out any
meaningful semantic or operational differences. Avoid claiming that services
are identical merely because they occupy the same category.

## Failure modes

Explain how the design degrades and recovers.

## Trade-offs

State what the recommendation optimizes and what it sacrifices.

## Follow-up questions

- Requirement-change follow-up
- Failure or troubleshooting follow-up
- Cost, security, migration, or organizational follow-up

## Scoring rubric

Score requirements, option analysis, distributed-systems reasoning, failure
handling, security, operations, economics, and communication. Define observable
basic, strong, senior, and principal-level signals rather than relying on an
overall impression.
