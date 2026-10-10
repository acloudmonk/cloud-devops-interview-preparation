# Terraform and OpenTofu Scenario Questions

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Answer each aloud before reading the model response. Use: clarify, inspect, protect,
diagnose, recover, prevent, measure.

## 1. A plan unexpectedly replaces a production database

**Model answer:** Stop approval and identify the exact attribute and provider schema that
requires replacement. Compare code, inputs, lock-file/provider change, state binding, and
refreshed remote value. Confirm whether address/key changes caused identity loss. Preserve
the plan and state version. Redesign the change using a supported in-place path, moved
address, staged resource, or migration; retain cloud deletion protection and backup. Add
a replacement policy gate and an upgrade test using representative state.

## 2. Two pipelines report the same state lock

**Model answer:** Freeze retries and identify the lock owner, run, PID/runner, and backend
logs. Determine whether an apply is active or orphaned. Recover or terminate the original
run before force-unlocking with the exact identifier and approval. Generate a fresh plan.
Prevent recurrence with one apply queue per state, cancellation semantics, observable
lock age, and no blind force-unlock automation.

## 3. An apply failed halfway through

**Model answer:** Assume some cloud calls succeeded. Preserve logs, plan, state version,
revision, identity, and cloud audit events. Protect customer service, stop conflicting
runs, refresh state, and inventory completed graph nodes and external side effects. Choose
roll-forward or explicit recovery based on risk; do not simply rerun. Verify outcomes and
add failure testing or provider timeout guidance.

## 4. A console emergency change appears as drift

**Model answer:** Confirm incident authorization and current customer need before reverting
anything. Record the owner and expiry, then update desired configuration or intentionally
remove the mitigation when safe. Generate a fresh reviewed plan. Improve the break-glass
workflow so emergency evidence, source reconciliation, and drift alerts are connected.

## 5. A team wants one state for all AWS accounts

**Model answer:** Reject convenience as the primary boundary. Compare owners, credentials,
change cadence, SLOs, regions, and failure radius. Split roots by durable operating and
security boundaries, while avoiding per-resource fragmentation. Publish small contracts
for dependencies. Use separate apply roles and queues so a networking change cannot lock
or mutate every workload account.

## 6. A reusable module exposes 80 variables

**Model answer:** Identify supported outcomes and real variants. Remove pass-through inputs,
encode safe invariants, split materially different lifecycles, and expose intentional
extension points. Version the smaller contract and migrate consumers with deprecation
guidance. Measure adoption, exceptions, upgrade time, and support load rather than reuse
count alone.

## 7. A provider upgrade changes hundreds of plans

**Model answer:** Separate the provider update from functional changes. Read release and
schema notes, inspect lock changes, run representative plans, and classify normalization,
real updates, and replacements. Canary low-risk roots, define pause criteria, and roll
out by failure domain. Retain the previous executable/lock and state backups, but do not
assume binary downgrade can read newly written state safely.

## 8. A secret was marked sensitive but appeared in state

**Model answer:** Explain that sensitivity controls presentation, not storage. Restrict and
rotate the secret, inspect state versions, plans, logs, caches, and support artifacts, and
review access/audit history. Prefer runtime retrieval or reference-based integrations
where possible. Encrypt and restrict state, minimize secret-returning data/resources, and
test redaction across the full pipeline.

## 9. A root needs resources in three AWS accounts and two regions

**Model answer:** First challenge whether one lifecycle truly requires all five targets.
If yes, configure explicit provider aliases and narrowly scoped assumed roles, pass aliases
to modules, make targets visible in plan evidence, and assess partial-failure recovery.
Otherwise split roots by owner/failure domain and exchange stable contracts. Never rely on
an ambiguous default provider that could point to production.

## 10. The team routinely uses targeted applies

**Model answer:** Treat this as a design or recovery smell. Targeting can omit relevant
graph changes and leave configuration partially reconciled. Identify why full plans are
too slow or risky—oversized state, poor ownership, or broken dependencies—then redesign
boundaries. Reserve targeting for documented exceptional recovery, followed by a full
fresh plan and outcome verification.

## 11. Brownfield resources must be adopted without downtime

**Model answer:** Inventory identity, dependencies, owner, and safeguards. Write matching
configuration, use declarative import or a controlled import, and iterate on read-only
plans until differences are understood. Adopt small groups, separate import from behavior
change, protect deletion, and verify cloud outcomes. Import binds identity; it does not
prove the configuration is safe.

## 12. `count` must become `for_each`

**Model answer:** Map every numeric address to a stable semantic key. Use moved declarations
or supported state moves, test with a state copy, and require a zero-replacement plan.
Separate the address refactor from any resource change and retain backup/recovery evidence.
Without address mapping, Terraform/OpenTofu interprets identical infrastructure as old
objects removed and new objects created.

## 13. Policy service is unavailable during a production change

**Model answer:** Apply the predefined failure policy by risk tier. High-risk production
changes normally fail closed; an emergency path requires bounded approvers, compensating
review, recorded evidence, expiry, and retrospective evaluation. Restore policy service,
re-evaluate the exact revision/plan if still valid, and measure availability. Do not invent
an unreviewed bypass during the outage.

## 14. Leadership asks whether to standardize on OpenTofu

**Model answer:** Inventory current Terraform versions, HCP/Enterprise dependencies,
providers, modules, automation, policy, state graphs, support, and licensing requirements.
Compare required features, governance, commercial support, registry, compatibility, and
exit cost. Pilot representative low-risk roots, back up state, prove no-change plans and
rollback constraints, then migrate in dependency order. Avoid ideological or all-at-once
selection.

## 15. A plan was approved yesterday and is ready to apply

**Model answer:** Treat approval as tied to code, inputs, tool/provider versions, state,
identity, target, and a validity window. Check whether any changed; production state can
drift even if Git did not. Expire the stale plan and generate a new one. The pipeline must
apply the exact approved saved plan once, not regenerate silently at apply time.
