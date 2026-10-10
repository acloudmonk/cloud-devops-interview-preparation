# Repository Architecture

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

## Repository boundary is an architecture decision

Repository structure affects ownership, atomic change, visibility, tooling,
dependency management, release independence, and blast radius.

| Model | Strengths | Costs/risks |
| --- | --- | --- |
| Monorepo | Atomic cross-project changes, shared tooling, discoverability | Scale, permissions, CI selection, ownership, broad coupling |
| Multirepo | Independent access, lifecycle, tooling, and release | Cross-repo coordination, duplicated policy, dependency drift |
| Hybrid | Boundaries chosen by domain/risk with shared foundations | Requires explicit rules to avoid arbitrary fragmentation |

A monorepo does not require one deployable or release cadence. A multirepo does
not guarantee service independence.

## Boundary questions

- Must changes across components be atomic?
- Are access/classification requirements compatible?
- Do components share release, support, and ownership lifecycles?
- Can interfaces and dependencies be versioned independently?
- How will discovery, refactoring, CI selection, and policy enforcement scale?
- What happens when the hosting platform or repository is unavailable?

## Shared code

Prefer explicit packages and versioned interfaces when consumers can evolve
independently. Source copying hides provenance; live source sharing can couple
every consumer. Define compatibility, ownership, deprecation, vulnerability
response, and release automation.

## Submodules and subtrees

Submodules record a commit pointer to another repository and require recursive
checkout, access, and deliberate pointer updates. They preserve repository
identity but add tooling and usability complexity. Subtrees copy another history
into a path and simplify checkout while complicating bidirectional synchronization.

Choose neither merely to avoid deciding ownership and release boundaries.

## Large and generated files

Git history retains every committed version, so deleting a large file in a
later commit does not shrink existing history. Use artifact/package/object
storage for build outputs and large binaries. Git LFS stores pointer files in
Git and content separately; availability, quotas, authorization, backup, and
archive still require design.

Generated sources belong in Git only when consumers cannot reproduce them,
review/audit requires them, or release constraints justify the noise. Document
the generator, version, deterministic process, and ownership.

## Scale and performance

Use path-aware CI, sparse checkout, partial clone, caching, and repository
maintenance where supported. Diagnose object count/size, refs, working-tree
scale, network transfer, filesystem behavior, hooks, and CI checkout patterns
before splitting a repository as a performance workaround.

## Migration

Preserve authorship, timestamps, tags, important branches, review/audit links,
LFS objects, release assets, and legal requirements. Freeze or synchronize
writes, validate object/ref counts, test consumers, retain rollback, and publish
new source-of-truth ownership.
