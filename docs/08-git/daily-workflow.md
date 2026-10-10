# Daily Change Workflow

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

## Three-state discipline

Before committing, distinguish working-tree changes, staged index changes, and
the current commit. Review each relevant diff; a clean-looking editor does not
prove the index contains what you intend.

| Question | Evidence concept |
| --- | --- |
| What changed since the current commit? | Working tree plus index compared with HEAD |
| What will the next commit contain? | Index compared with HEAD |
| What is modified but not staged? | Working tree compared with index |
| Which files are untracked/ignored? | Status plus ignore-rule explanation |

Partial staging can create a coherent commit from a mixed working tree, but
review context carefully so a selected hunk does not depend on an unstaged hunk.

## Reviewable commits

A strong commit has one purpose, passes relevant checks, avoids generated noise
and secrets, and explains why the change exists. Commit messages should help a
future investigator distinguish intent from implementation detail.

Avoid using one commit as an arbitrary daily checkpoint in a shared review.
Local checkpoints are useful; organize them before publication when policy and
collaborator expectations permit.

## Ignore behavior

Ignore rules affect untracked paths, not files already tracked. Repository rules
belong in `.gitignore`; personal/editor rules should normally remain in local or
global excludes. Do not hide sensitive files after committing them—remove the
secret from history where required and rotate it immediately.

## Synchronizing safely

1. Fetch to obtain current remote state.
2. Inspect divergence and upstream changes.
3. Integrate with merge or rebase according to team policy.
4. Resolve conflicts by reconstructing intended behavior, not choosing “ours”
   or “theirs” mechanically.
5. Run tests and review the resulting diff/graph.
6. Push without bypassing protected-branch policy.

Use `--force-with-lease` only when rewriting a permitted branch: it refuses the
push when the remote reference differs from the value you expect. It is safer
than unconditional force but still rewrites published history.

## Commit quality checklist

- correct base and branch;
- no credentials, personal data, build artifacts, or unrelated files;
- staged diff reviewed, including renames and file modes;
- tests/checks proportional to risk;
- dependencies and generated files follow repository policy;
- message and PR explain purpose, risk, rollout, and rollback;
- issue/change record linked where required.

## Hooks are assistance, not enforcement

Client hooks can format, lint, or detect mistakes, but users can bypass or lack
them. Enforce mandatory controls on trusted server/CI paths and version hook
configuration so local feedback remains consistent.
