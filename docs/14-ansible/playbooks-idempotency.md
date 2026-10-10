# Playbooks, Idempotency, and Failure Control

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

A playbook is a change program across distributed targets. Correct YAML is only
the beginning; the design must converge, bound concurrency, expose partial
failure, and verify the service outcome.

## Idempotency and convergence

An idempotent task reports no change when the target already satisfies intent.
A convergent playbook moves supported starting states toward the declared end
state. Idempotency can fail through timestamps, unordered templates, shell
commands, generated values, mutable package repositories, or inaccurate module
`changed` reporting.

Prefer modules with explicit state. When a command is unavoidable, use discovery
and guards, define `changed_when` and `failed_when`, validate output, and test a
second run.

## Playbook structure

Use plays to express target and orchestration boundaries. Give every task a
meaningful name, use fully qualified collection names, separate discovery from
mutation, and keep business data outside task flow. Handlers should run only when
notified and should model a real dependent action such as a service reload.

## Failure and recovery controls

- `serial` bounds the batch and failure radius.
- `max_fail_percentage` and `any_errors_fatal` define stop behavior.
- blocks with `rescue` and `always` express local recovery and cleanup.
- retries handle known transient conditions, not permanent errors.
- delegation coordinates load balancers, databases, or control APIs.
- assertions fail early when prerequisites or safety conditions are false.

Do not use `ignore_errors` as a recovery strategy. It can turn a known failure
into an apparently successful run.

## Rolling change pattern

For each batch:

1. verify capacity and drain the targets;
2. apply the smallest reversible configuration change;
3. restart or reload only when needed;
4. wait for technical readiness;
5. verify application behavior and telemetry;
6. restore traffic and observe;
7. continue only if stop criteria remain healthy.

Rollback may mean restoring a versioned template or package, not running the
playbook backward. Define the recovery artifact and data compatibility first.

## Check mode and diff mode

Check mode is a forecast whose quality depends on module support and external
state. Diff mode can expose sensitive content. Use both as evidence, not proof;
review unsupported tasks and perform a controlled canary before production.

## Result taxonomy

Distinguish `ok`, `changed`, `failed`, `unreachable`, `skipped`, and rescued or
ignored failures. A run can be green while the application is broken, and a
changed count can be noisy without representing useful work. Verify outcomes.

Return to the [module overview](index.md) when ready to continue.
