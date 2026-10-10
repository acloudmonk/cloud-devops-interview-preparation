# Git Rapid-Fire Revision

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

Answer each in 30–60 seconds with a definition, graph consequence, and one
condition that changes the answer.

## Objects and state

1. **Blob?** Content object without a filename; trees associate names/modes with objects.
2. **Tree?** Snapshot of directory entries pointing to blobs and subtrees.
3. **Commit?** Tree, parent(s), author/committer metadata, and message forming graph history.
4. **Branch?** Mutable reference to a commit, not a container of commits.
5. **HEAD?** Current symbolic branch reference or direct detached commit position.
6. **Index?** Proposed next tree and staging area for normal and conflicted entries.
7. **Working tree?** Editable materialization; uncommitted content may never exist in Git objects.
8. **Detached HEAD risk?** New commits lack a durable branch name unless one is created.
9. **`main` versus `origin/main`?** Local branch versus last fetched observation of remote branch.
10. **Object ID proves?** Content/metadata identity and integrity, not author trust or correctness.

## Integration and history

1. **Fast-forward?** Move a ref to an existing descendant without a new merge commit.
2. **Merge commit?** New commit with multiple parents preserving topology.
3. **Rebase?** Replay patches on a new base, creating new commit IDs.
4. **Squash merge?** Create one target commit for combined branch changes without preserving ancestry.
5. **Cherry-pick?** Apply selected commit change as a new commit on current history.
6. **Revert?** Add a new commit that inverses an earlier change.
7. **Reset?** Move a ref and optionally change index/working tree; unsafe on shared history.
8. **Merge-revert trap?** Ancestry remains, so later merging the same branch may not restore reverted content.
9. **`--force-with-lease`?** Rewrite only if remote ref equals the expected value; still disruptive.
10. **Conflict meaning?** Git cannot determine intended combined history; a semantic decision is required.

## Collaboration and governance

1. **Trunk-based development?** Frequent small integration to one primary branch, with runtime/release decoupling.
2. **Long-lived branch cost?** Drift, delayed feedback, semantic conflict, and unclear source of truth.
3. **Release branch purpose?** Stabilize/support a version with explicit backport and retirement rules.
4. **Environment-branch concern?** Source history becomes deployment state and drifts from immutable promotion.
5. **Feature-flag obligation?** Owner, observability, default, rollback, security review, and expiry.
6. **CODEOWNERS guarantees approval?** No; it routes requests, while branch/ruleset policy enforces requirements.
7. **Stale approval?** Approval predates material new changes and may need dismissal/re-review.
8. **Merge queue value?** Tests queued changes against current target and preceding queued changes.
9. **Emergency change?** Faster bounded authority with audit, evidence, rollback, and post-review.
10. **Useful flow metric?** Branch/PR age and queue time interpreted with quality and risk, not individual ranking.

## Architecture and security

1. **Monorepo strength?** Atomic cross-project change and shared discovery/tooling.
2. **Multirepo strength?** Independent access, ownership, lifecycle, tooling, and release boundaries.
3. **Submodule?** Repository records a commit pointer to another repository with separate access/history.
4. **Git LFS?** Git stores pointers while large content uses separate storage and lifecycle.
5. **Why deletion does not shrink history?** Earlier reachable commits still reference the object.
6. **Signed commit proves?** Accepted key signed the object; trust depends on identity and key policy.
7. **First secret-leak action?** Revoke or rotate the credential, not merely delete the file.
8. **Fork CI risk?** Untrusted code can attempt to read secrets/tokens or alter privileged workflows.
9. **Protected branch goal?** Enforce update, review, check, signing, force/deletion, and bypass invariants.
10. **Git backup scope?** Objects/refs plus provider configuration, PR/issues, audit, releases, and restore tests.

## Recovery and judgment

1. **Reflog?** Local record of reference movements; valuable recovery aid but not a permanent backup.
2. **Lost commit first move?** Stop destructive operations, inspect reflog, and create a protective reference.
3. **Push rejected?** Fetch and inspect divergence/policy before choosing integration.
4. **`bisect` requirement?** Reliable reproducible good/bad classification across candidate commits.
5. **Generated-file conflict?** Resolve source inputs and regenerate deterministically.
6. **Accidental force push response?** Freeze, preserve all tips, find authoritative commit, restore/integrate under review.
7. **History rewrite concern?** Every commit ID/ref/signature/fork/consumer can be affected.
8. **Green check limit?** It proves one configured execution, not test relevance or trustworthiness.
9. **Recovery verification?** Expected refs/graph, builds/releases, consumers, audit, and customer outcome.
10. **Principal-level close?** Impact, graph/evidence, recovery, remaining divergence/risk, owner, and next decision.
