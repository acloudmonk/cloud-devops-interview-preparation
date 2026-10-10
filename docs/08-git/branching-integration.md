# Branching and Integration

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

## Read the graph first

Integration choices change either graph topology, commit identity, or both.

| Operation | Graph effect | Published-history risk |
| --- | --- | --- |
| Fast-forward | Moves a ref to an existing descendant | Low; no new commit |
| Merge commit | Creates a commit with multiple parents | Preserves branch topology |
| Squash merge | Creates one new commit with combined patch | Original branch commits are not ancestors of target |
| Rebase | Replays patches as new commits on a new base | Rewrites commit IDs |
| Cherry-pick | Applies selected change as a new commit | Duplicate logical changes can complicate later integration |
| Revert | Adds a commit that inverses an earlier patch | Safe for shared history; semantics may conflict later |
| Reset | Moves a reference; modes also change index/working tree | Dangerous on published branches |

## Merge or rebase

Use merge when preserving the exact shared topology is useful or rewriting is
not permitted. Use rebase to place unpublished work on a new base and produce a
linear review when team policy expects it. Neither makes conflicts disappear;
rebase may surface them commit by commit.

After rebasing, re-run tests because the commits now have different parents and
may interact differently with the base.

## Squash trade-offs

Squash merge produces a simple target history and makes one-PR reversion easy.
It loses individual commit ancestry and can confuse later attempts to merge the
same long-lived branch. Preserve intent in the PR and squash message.

## Revert complexities

Reverting a merge requires choosing which parent is the mainline. The resulting
commit says the merged changes should not be present; a later merge may not
reapply them automatically. Plan whether to revert the revert, create a corrected
change, or use another controlled recovery path.

## Conflict resolution

A conflict is a request for a human decision about competing histories.

1. understand both changes and the desired combined behavior;
2. inspect base and surrounding commits, not only conflict markers;
3. resolve generated files from their source where possible;
4. test the integrated behavior;
5. review the entire resulting diff and graph;
6. record non-obvious decisions for reviewers.

## Release and hotfix integration

If release branches exist, define source of truth, allowed changes, forward-port
or backport direction, version/tag rules, and retirement. A hotfix applied to
production but not reintegrated into the development line will regress later.

## Safe force update

Confirm branch ownership, fetch immediately before rewriting, communicate with
collaborators, protect important old tips with a temporary reference if needed,
and use a lease. Protected default/release branches should normally reject
force pushes entirely.
