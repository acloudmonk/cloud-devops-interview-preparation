# Python Automation Mock Interview

[← Mock interview index](index.md) · [Module 30 overview](../30-python-automation/index.md)

Duration: **50 minutes**
Primary context: **AWS multi-account automation with multi-cloud follow-ups**

## Candidate brief

Design Python automation that discovers and remediates public storage exposure across
300 AWS accounts and later Azure subscriptions and Google Cloud projects. It runs on
events and schedules, respects approved exceptions, survives partial failure, and
must not turn a code or configuration defect into an organization-wide incident.

## Interview structure

### 0–6 minutes — Discovery and mechanism

Clarify outcome, policy, authoritative inventory, targets, scale, latency, exception,
ownership, compliance, current tooling, and why Python rather than IaC/workflow/service.

### 6–17 minutes — Design and SDK behavior

Cover package structure, data models, configuration, identity, Boto3 sessions,
pagination, retries, waiters, idempotency, checkpoints, and result contract.

### 17–28 minutes — Safety and verification

Explain selection, plan/dry run, revalidation, approvals, max changes, canary,
concurrency/quota, tests, isolated integration, rollback/compensation, reconciliation.

### 28–38 minutes — Failure branches

Handle three: timeout-after-success, missing page, throttling storm, process crash,
bad dependency, corrupted checkpoint, leaked log secret, or concurrent runs.

### 38–46 minutes — Delivery and operation

Cover artifact and dependency supply chain, deployment, structured evidence, SLO,
alerts, kill switch, incident command, multi-cloud adapters, cost, and retirement.

### 46–50 minutes — Executive close

State recommendation, alternative, trade-off, highest residual risk, owner, next
proof, and candidate questions.

## Scoring rubric

| Dimension | Strong evidence |
| --- | --- |
| Discovery | outcome, state, authority, scope, constraints, owners, unknowns |
| Python design | typed models, pure decisions, adapters, explicit errors/results |
| SDK/API | identity, pagination, retry, quota, async readiness, request evidence |
| Safety | idempotency, plan, bounds, canary, checkpoint, reconcile, kill switch |
| Testing | unit/contract/integration/failure/permission/destructive-path proof |
| Delivery | reproducible artifact, dependency controls, promotion, rollback |
| Operation | structured evidence, SLO, partial status, incident, ownership, cost |
| Multi-cloud | shared intent/results with accurate native adapters and trust |
| Communication | structured decision, trade-off, residual risk, next validation |

Score each 0–4. Maximum **36**; 31–36 is strong architect signal, 24–30 is credible
with targeted gaps, and below 24 requires another practice cycle.
