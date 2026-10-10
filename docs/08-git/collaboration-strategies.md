# Collaboration Strategies

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

## Choose from constraints

A branching model is an operating policy, not a maturity badge. Choose it from
deployment frequency, test confidence, coupling, release support, compliance,
team topology, and recovery requirements.

| Model | Works well when | Main risks |
| --- | --- | --- |
| Trunk-based development | Small changes, strong automation, feature flags, frequent integration | Weak tests or oversized changes destabilize trunk |
| Short-lived feature branches | PR review is required and branches integrate within hours/days | Queues and drift grow when branches live too long |
| Release branches | Multiple supported releases need stabilization/backports | Fix propagation, divergence, and branch ownership complexity |
| GitFlow-style long-lived branches | Scheduled releases and organizational constraints require stages | Merge debt, unclear source of truth, slow feedback |
| Fork-based contribution | External/untrusted contributors need isolation | Secret exposure in CI, maintenance overhead, delayed synchronization |

## Trunk-based design

Trunk-based development means integrating small changes frequently into one
primary branch. Incomplete behavior is separated from deployment/release using
feature flags, branch by abstraction, backward-compatible migrations, and
progressive delivery—not long-lived source branches.

It requires fast deterministic checks, ownership, rapid rollback/revert, and a
healthy default branch. Direct unreviewed commits are not a requirement.

## Branch lifetime and batch size

Long-lived branches accumulate semantic conflicts even when textual merges are
clean. Measure time to first review, time to merge, change size, stale branches,
conflict rate, queue time, and revert rate. Use metrics to improve flow, not to
rank developers or reward unsafe smallness.

## Environment branches

Branches named development, test, staging, and production often make source
history represent deployment state. This encourages merge drift and emergency
commits that never return to the source of truth. Prefer immutable artifacts
promoted through environments; document exceptions when legacy constraints
require environment branches.

## Feature flags

Flags reduce branch lifetime but create runtime states. Define owner, default,
targeting, observability, security implications, rollback behavior, and expiry.
Remove stale flags and test important combinations.

## Multi-version support

For supported releases, define:

- which branch accepts the original fix;
- selection and ordering of backports;
- conflict and test ownership;
- version/tag creation and signing;
- security disclosure handling;
- end-of-support and branch deletion policy.

Automating backport proposals helps, but a clean cherry-pick does not prove the
change is semantically correct for an older version.

## Decision signals

Prefer the simplest model that satisfies real constraints. Revisit when branch
age, merge conflict, emergency bypass, release lead time, failed-change rate, or
unsupported-version burden crosses an agreed threshold.
