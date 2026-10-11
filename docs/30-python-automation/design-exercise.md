# Enterprise Automation Design Exercise

[← Module overview](index.md) · [Scenario questions →](scenarios.md)

## Brief

Design Python automation that discovers and remediates public object-storage exposure
across 300 AWS accounts and 20 Regions. It runs daily and on security events, must not
change approved exceptions, and must produce evidence. Azure subscriptions and Google
Cloud projects will join later. A bad run must not alter thousands of resources.

## Constraints

- Assume roles through AWS Organizations; no stored cloud access keys.
- Inventory is eventually consistent and APIs throttle; jobs may restart mid-run.
- Security wants automatic containment; product owners require preview and exceptions.
- Remediation must meet 30-minute critical exposure and four-hour standard objectives.
- Some controls require multiple API calls and cannot be transactionally rolled back.

## Deliverable

Present: selection/inventory contract; desired policy and exception authority; Python
structure and data model; Boto3 sessions, pagination, retries, wait/verification;
idempotency and checkpointing; bounded concurrency/quota; plan/approval/apply modes;
testing and isolated accounts; artifact/identity supply chain; observability, incident,
rollback/compensation; multi-cloud extension; cost, rollout, owners, and residual risk.

## Strong direction

Use organization/account inventory and per-account roles, stream paginated resources,
normalize to a provider-neutral finding while retaining native evidence, calculate an
immutable plan, and apply small canary batches. Revalidate immediately before change,
use conditional/native controls, checkpoint per item, and independently reconcile.
Separate detection, policy, approval, execution, and audit authority.

## Scoring rubric

| Dimension | 0 | 2 | 4 |
| --- | --- | --- | --- |
| Contract | loop over accounts | basic inputs | authoritative inventory, policy, exceptions, outcomes |
| Safety | confirmation flag | dry run | same plan path, revalidation, bounds, canary, kill switch |
| Reliability | catch exception | retries | classification, idempotency, checkpoint, uncertainty, reconcile |
| Cloud SDK | calls listed | pagination | identity, Region, pagination, quota, request evidence |
| Verification | unit tests | mocked SDK | isolated integration, failure, permission, canary, independent proof |
| Operation | logs | metrics | SLO, incident, ownership, cost, retirement, multi-cloud semantics |

Maximum **24**; aim for **19** before the mock interview.
