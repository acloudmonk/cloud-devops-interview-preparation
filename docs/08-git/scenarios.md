# Git and Source-Control Scenarios

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

Answer aloud before reading the model answer. Draw the graph, identify published
state and consumers, preserve evidence, choose a reversible action, and verify.

## 1. Commit disappeared after rebase

**Model answer:** Stop rewriting and inspect local reflogs and old branch tips.
Create a temporary branch at the wanted object before integrating it. Verify
the patch and parent context; then determine whether it was intentionally
dropped, duplicated upstream, or needs cherry-pick/rebase.

## 2. Bad commit is already on main

**Model answer:** Assess impact and deployment state, then use a reviewed revert
on shared history rather than resetting main. Test the inverse against current
code, deploy/verify customer recovery, and create a corrected forward change.

## 3. Developer wants to force-push a shared branch

**Model answer:** Fetch and draw divergence, identify collaborators and policy,
and preserve both tips. Prefer merge or a new branch. If rewriting is agreed and
permitted, communicate, use `--force-with-lease`, and help consumers reconcile.

## 4. Secret committed to a private repository

**Model answer:** Treat it as compromised regardless of repository visibility.
Rotate/revoke first, investigate clones/logs/artifacts, remove current exposure,
and coordinate history rewrite only if required. Fix delivery and scanning.

## 5. Merge conflict in generated lock/output files

**Model answer:** Resolve source manifests/configuration and regenerate using
the approved deterministic tool version. Do not splice generated conflict
markers mechanically. Review dependency changes and run integrity/tests.

## 6. Hotfix exists only on a release branch

**Model answer:** Identify source-of-truth policy and forward-port the logical
fix to trunk, not blindly the hash if code diverged. Test both supported lines,
record backport relationships, and automate detection of unpropagated fixes.

## 7. PR checks were green but main broke after merge

**Model answer:** Determine whether main advanced, checks used stale base, or two
changes interacted. Revert/disable the smallest change, protect customers, and
use merge queues or up-to-date integration testing with trustworthy required checks.

## 8. CODEOWNERS approval did not occur

**Model answer:** Check path patterns, file location/case, team visibility and
permissions, ruleset requirement, draft/base branch, and whether later changes
dismissed approval. CODEOWNERS requests review; enforcement requires branch rules.

## 9. Repository clone becomes extremely slow

**Model answer:** Measure pack transfer, largest objects/history, refs, LFS,
working-tree file count, filesystem, hooks, and CI patterns. Apply partial/sparse
clone or maintenance where suitable; rewrite/split only after coordinated analysis.

## 10. Team proposes a monorepo

**Model answer:** Evaluate atomic-change need, ownership/access compatibility,
build graph, CI selection, release independence, scale, and migration. Choose a
boundary model with success metrics rather than assuming monorepo fixes coordination.

## 11. Reverting a merge does not allow remerge

**Model answer:** A merge revert records that the merged tree change is unwanted
while ancestry remains. Decide whether to revert the revert, add a corrected
change, or merge new commits; test carefully and explain mainline-parent choice.

## 12. External fork needs CI

**Model answer:** Run untrusted code without secrets/write tokens on isolated
ephemeral capacity. Require trusted review before privileged publication, protect
workflow changes, and avoid checkout/execution patterns that combine fork code
with base-repository credentials.

## 13. Commit shows “verified” but author denies it

**Model answer:** Preserve the object and audit evidence; inspect signature key,
identity binding, key compromise, automation/delegation, and platform policy.
Revoke/rotate as appropriate and do not equate cryptographic validity with intent.

## 14. Teams use environment branches

**Model answer:** Map how code moves, drift, emergency changes, and artifact
identity. Migrate toward one source history plus immutable artifact promotion,
using a pilot, compatibility controls, freeze/synchronization, and rollback.

## 15. Source-hosting provider is unavailable

**Model answer:** Activate continuity objectives: verified mirrors/backups,
critical ref and release metadata, read-only clones, controlled emergency change,
and later reconciliation. Avoid creating two writable sources of truth without
an explicit conflict and audit plan.
