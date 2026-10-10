# Pull-Request Governance

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

## A pull request is a decision record

A strong PR connects intent, implementation, evidence, operational risk, and
approval. It is not proof that the change is safe merely because it exists.

Require enough information to answer:

- what outcome and scope are intended;
- what changed and what deliberately did not;
- how it was tested and what remains unverified;
- security, data, compatibility, migration, and operational risks;
- rollout, rollback/revert, monitoring, and ownership;
- which experts and change authorities must approve.

## Review design

| Control | Purpose | Failure mode to avoid |
| --- | --- | --- |
| Required reviewers | Independent technical judgment | Rubber-stamp or self-approval |
| CODEOWNERS | Route sensitive paths to accountable teams | Treating ownership files as access control by themselves |
| Required checks | Repeatable evidence | Untrusted or stale checks satisfying policy |
| Conversation resolution | Make objections explicit | Resolving without addressing risk |
| Signed commits/tags | Verify cryptographic identity under policy | Assuming a green badge proves correctness |
| Merge queue | Test changes against an up-to-date integration state | Merging individually green but mutually incompatible PRs |
| Rulesets/protection | Enforce branch/tag invariants | Broad admin bypass with no audit |

Ownership should be narrow enough to find knowledgeable reviewers and broad
enough to avoid one-person bottlenecks. Define alternates and absence coverage.

## Approval quality

Approval should be invalidated when material changes occur. Separate author,
reviewer, and deployment authority where risk or regulation requires it. Bots
can verify policy and syntax; accountable humans own judgment that automation
cannot encode.

## Merge methods

Standardize permitted merge methods so history is predictable. Record how issue
linking, release notes, authorship, commit signatures, and reversion work under
merge-commit, squash, or rebase-merge policies.

## Emergency changes

An emergency path must be faster, not uncontrolled. Define incident authority,
minimum approver, bounded bypass, audit evidence, monitoring, rollback,
post-incident review, and expiry/reconciliation. Test access before an incident.

## Automation trust

Checks run with code, tokens, runners, actions/plugins, and network access.
Protect workflow definitions and runner configuration; pin/approve dependencies;
limit token permissions; isolate untrusted fork code; and prevent a check from
approving changes to its own trust configuration without stronger review.

## Useful governance metrics

Measure review latency, change size, stale approvals, bypass usage, queue time,
failed-change/revert rate, ownership coverage, and unresolved-risk recurrence.
Metrics should reveal system constraints, not incentivize shallow review.
