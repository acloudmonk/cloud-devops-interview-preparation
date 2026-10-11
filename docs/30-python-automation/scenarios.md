# Scenario Questions and Model Answers

[← Module overview](index.md) · [Scenario answer framework](../interview-playbook/scenario-answer-framework.md)

## 1. A cleanup script deletes production resources

**Model answer:** Stop new work, revoke execution authority, preserve run/plan/API
evidence, enumerate targets, and restore or compensate by business priority. Replace
implicit discovery with explicit account/Region scope, protected-resource policy,
plan/revalidation, maximum changes, canary, approval, and independent reconciliation.

## 2. An SDK call times out after creating a resource

**Model answer:** Treat outcome as unknown, not failure. Query using idempotency token,
request ID, stable name, or tags before retry. Bound backoff/jitter and record final
uncertainty. Prefer native client tokens or durable operation state for creation.

## 3. Only the first thousand resources are processed

**Model answer:** Suspect missing pagination. Confirm service token and filter semantics,
then use the SDK paginator or explicit continuation loop. Test multiple/empty pages,
changing inventory, duplicate identifiers, interruption, and completeness metrics.

## 4. Automation works locally but is denied in CI

**Model answer:** Compare effective identities, account/Region, trust policy, permission
boundary, session conditions, and resource policy. Do not copy developer credentials.
Use CI workload federation and least privilege, test denied and allowed paths, and log
identity/account without exposing tokens.

## 5. Security asks for retry on every exception

**Model answer:** Classify errors. Retry only known transient and repeatable operations;
fail validation/auth/permission errors, resolve conflicts deliberately, and query
ambiguous outcomes. Bound attempts/elapsed time, add jitter, honor service guidance,
and report exhausted/uncertain items for reconciliation.

## 6. Twenty threads trigger severe throttling

**Model answer:** Reduce concurrency, centralize rate budgets, honor retry hints, and
measure per-service/account quotas. Use bounded workers and backpressure, not per-item
unbounded submission. Batch where semantics preserve item outcomes and negotiate quota
only after algorithm/API-call reduction.

## 7. Dry run says 20 changes but apply makes 200

**Model answer:** Stop the run and compare selection/config/version/time. Dry run and
apply must share planning logic and persist an immutable plan. Revalidate each target,
reject scope growth, expire stale plans, require maximum-change guards, and test drift
between plan and apply.

## 8. A Lambda batch retries successful messages

**Model answer:** Identify event-source retry semantics and return item-level partial
failures where supported. Make each record idempotent, isolate poison messages, control
visibility/timeouts and concurrency, checkpoint business outcome, and monitor oldest
age, duplicate effect, and dead-letter backlog.

## 9. A library upgrade changes response shape

**Model answer:** Pin/lock deployed applications, inspect changelog and transitive diff,
and run adapter contract/integration tests. Encapsulate SDK responses behind owned
models, canary the new artifact, preserve rollback, and automate dependency updates
rather than freezing indefinitely.

## 10. Logs contain access tokens and customer records

**Model answer:** Restrict access, stop further emission, revoke reusable credentials,
follow data-incident retention/removal procedure, and assess exposure. Redact at source,
allowlist fields, classify data, test logging, and retain identifiers/request IDs rather
than payloads or credentials.

## 11. A job crashes after half its changes

**Model answer:** Do not restart blindly. Read the manifest/checkpoint, query actual
state, classify changed/unchanged/failed/unknown, and resume only revalidated items.
Persist item outcome atomically, version checkpoints, support bounded retry, and
independently reconcile completion.

## 12. Multi-cloud teams request one generic SDK wrapper

**Model answer:** Standardize outcome, policy, identity, evidence, and error categories,
but retain native paging, operations, retries, permissions, and resource semantics in
adapters. A lowest-common-denominator wrapper can hide unsafe differences. Add provider
contract tests and explicit unsupported capabilities.

## 13. A Python process consumes all memory

**Model answer:** Measure object growth and input volume. Stream paginated records,
avoid accumulating tasks/results, bound queues/concurrency, release large references,
and profile representative data. Add memory limit, progress/checkpoint, and graceful
shutdown rather than merely increasing instance size.

## 14. Operators parse human CLI output in pipelines

**Model answer:** Introduce a versioned JSON output contract with stable fields, exit
codes, partial-status semantics, and diagnostics on stderr. Deprecate parsing with
migration time and tests. Keep human tables free to evolve without breaking automation.

## 15. A scheduled remediation has no owner

**Model answer:** Pause high-risk unattended change until ownership and authority are
clear. Inventory trigger, artifact, identity, permissions, targets, policy, evidence,
SLO, alert route, exception and kill switch. Assign product/platform/security duties,
test an incident, and define retirement.
