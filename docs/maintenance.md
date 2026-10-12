# Content Maintenance and Review

[← Documentation home](index.md) · [Reference standards](reference-catalog/index.md)

This repository changes only when a maintainer explicitly requests a review or an
approved issue identifies a focused correction. There is no recurring, scheduled,
or event-triggered content-maintenance process.

## Start a review manually

Begin maintenance only after a maintainer chooses a specific page, module, reference,
or reported problem. Record that scope in a feature branch or issue so the work is
visible and bounded. Normal pull-request checks remain automatic quality gates for an
already requested change; they do not create or modify documentation.

A passing link check proves reachability, not technical currency. A human reviewer must
still confirm service lifecycle, terminology, behavior, quotas, regional availability,
pricing assumptions, framework pillars, and recommended replacements.

## Manual review procedure

1. Select one or more owner modules; do not update all dates mechanically.
2. Check official lifecycle and release notices before secondary commentary.
3. Revalidate version-sensitive service names, limits, pricing models, Regions,
   identity behavior, failure semantics, and framework guidance.
4. Confirm each reference still supports the stated learning outcome.
5. Replace obsolete sources and record meaningful semantic changes in the PR.
6. Run the complete local validation suite and obtain manual approval.
7. Update `Last reviewed` or `Last verified` only for pages actually examined.

## Manual validation commands

Run these commands from the repository root after making an approved change:

```powershell
python scripts/check_module_quality.py
python -m mkdocs build --strict
npx --yes markdownlint-cli2 "**/*.md" "#site/**" "#.venv/**"
git diff --check
```

To request the complete GitHub documentation workflow manually on `main`, including
external-link validation, use:

```powershell
gh workflow run docs.yml --ref main
gh run list --workflow docs.yml --limit 1
```

The same checks run automatically only as safeguards on a pull request or a push to
`main`; no scheduled workflow starts a review.

## Feedback triage

Classify incoming evidence before editing:

| Evidence | Action |
| --- | --- |
| Personal knowledge gap | Use the study tracker and repeat the relevant mock |
| Unclear explanation | Improve the owning page and add a clarifying example if useful |
| Incorrect or outdated claim | Verify against authoritative sources and correct promptly |
| Broken, moved, or deprecated reference | Replace or archive it and preserve the learning purpose |
| Missing scenario or follow-up | Add it only when it tests a distinct decision or failure mode |
| Request for a new module | Prefer the existing owner module unless scope is genuinely separate |

Use the
[GitHub issue chooser](https://github.com/acloudmonk/cloud-devops-interview-preparation/issues/new/choose)
for content and reference reports. Never include credentials, account identifiers,
customer details, proprietary interview questions, or confidential incident data.

## Definition of done

A maintenance change is complete when its evidence is cited, affected navigation and
cross-references remain correct, dates reflect real review, local validation passes,
GitHub checks pass, and a maintainer manually approves the pull request.
