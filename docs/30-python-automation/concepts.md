# Automation Decision Model

[← Module overview](index.md) · [Next: Language and data →](language-data.md)

Use **outcome → authority → inventory/state → plan → bounded change → verify →
evidence → reconcile**. Code syntax comes after the operating contract.

## Choose the right mechanism

| Need | Prefer | Warning |
| --- | --- | --- |
| repeatable infrastructure state | Terraform/OpenTofu or provider declarative system | Python can hide unmanaged state |
| host/application configuration | Ansible or image/config system | ad hoc SSH loops drift |
| event orchestration | managed workflow, queue, or event service | long scripts lose durable progress |
| custom API/data transformation | Python library, CLI, job, or service | define ownership and lifecycle |
| tiny local composition | shell may be enough | quoting, portability, and error handling degrade quickly |

## Automation contract

Define inputs and validation; target inventory and ownership; identity and allowed
actions; source of truth; idempotency key; concurrency and rate limits; dry-run
meaning; checkpoint/restart; partial-success output; verification; rollback or
compensation; audit evidence; and accountable operator.

## Control loop

One-shot mutation assumes the world stayed unchanged. Safer automation observes,
computes a desired delta, applies bounded work, verifies outcome, and reconciles.
Every list operation must handle pagination; every retry must understand ambiguity;
every destructive operation needs scope proof and a stop condition.

## Interview answer shape

State business outcome and invariant, justify mechanism, define inputs/state and
authority, explain idempotency/failure/concurrency, then cover testing, rollout,
evidence, cost, owner, and residual risk.
