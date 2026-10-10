# Recovery and Troubleshooting

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

## Preserve before changing

Record status, current branch/HEAD, recent graph, remotes, upstream, reflog, and
the exact command/error. If state matters, create a temporary branch/tag or copy
the patch before reset, rebase, clean, or garbage collection.

## Recovery map

| Symptom | First safe reasoning |
| --- | --- |
| Commit “lost” after reset/rebase | Inspect reflog and create a reference to the wanted object |
| Work on detached HEAD | Create a branch at the current commit before switching |
| Published bad change | Revert with review; avoid rewriting shared default history |
| Local uncommitted change overwritten | Check editor/local backups and stashes; Git may never have stored it |
| Push rejected | Fetch and inspect divergence/policy; do not force reflexively |
| Rebase conflict explosion | Abort if needed, reassess base/order, and integrate deliberately |
| Regression with unknown commit | Use reproducible test and binary search with `bisect` |
| Repository suddenly huge | Find largest objects/history and identify source before rewriting |

## Reflog limits

Reflogs record local reference movements and are often the fastest recovery
path. They are local, expire, and are not a backup. Server retention and
garbage-collection policies differ.

## Revert versus reset

Revert adds history that negates a change and is normally appropriate for a
shared branch. Reset moves a reference and may also update index/working tree;
it is suitable for controlled unpublished recovery. State exactly which state
must be preserved before choosing.

## Regression isolation

`git bisect` narrows a first-bad commit only when good/bad classification is
reliable. Automate a deterministic test where possible, mark untestable commits
appropriately, and consider build/environment/data changes outside Git history.

## Conflict and corruption response

For conflicts, reconstruct intended behavior and test. For suspected object
corruption, stop destructive maintenance, preserve copies, verify filesystem and
repository objects, compare another trusted clone/remote, and restore missing
objects from a verified source. A fresh clone may restore work but can erase
unique local evidence.

## Accidental force push

1. pause further pushes and identify the authoritative expected tip;
2. preserve current remote and affected local tips with references;
3. use server audit, reflogs, clones, PR commits, and CI checkouts to locate objects;
4. agree whether to restore the old tip or retain new work by merge/rebase;
5. update the protected ref through an authorized, reviewed operation;
6. notify consumers to reconcile safely and add prevention controls.

## Large-history rewrite

History filtering changes commit IDs and disrupts branches, tags, forks, open
PRs, caches, release references, and signatures. Inventory all refs and owners,
freeze writes, back up, rehearse, publish mapping/instructions, coordinate
cutover, verify, and prevent reintroduction.

## Incident close

Document impact, affected refs/consumers, timeline, preserved evidence, recovery,
verification, remaining divergence, owner, and policy/tooling improvements.
