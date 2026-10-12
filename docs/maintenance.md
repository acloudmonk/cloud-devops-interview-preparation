# Content Maintenance and Review

[← Documentation home](index.md) · [Reference standards](reference-catalog/index.md)

This repository changes when evidence justifies an improvement. Maintenance should
preserve a focused interview curriculum rather than continuously adding breadth.

## Review cadence

| Cadence | Review | Evidence |
| --- | --- | --- |
| Every pull request | Build, Markdown, links, secrets, module structure | Passing required checks |
| Monthly | Scheduled documentation and external-link validation | GitHub Actions result and owned failures |
| Quarterly | Version-sensitive cloud, platform, framework, and reference review | Updated verification date plus source-backed PR |
| Event-driven | Deprecation, security advisory, major release, broken source, or learner evidence | Focused issue and bounded PR |

A passing link check proves reachability, not technical currency. A human reviewer must
still confirm service lifecycle, terminology, behavior, quotas, regional availability,
pricing assumptions, framework pillars, and recommended replacements.

## Quarterly review procedure

1. Select one or more owner modules; do not update all dates mechanically.
2. Check official lifecycle and release notices before secondary commentary.
3. Revalidate version-sensitive service names, limits, pricing models, Regions,
   identity behavior, failure semantics, and framework guidance.
4. Confirm each reference still supports the stated learning outcome.
5. Replace obsolete sources and record meaningful semantic changes in the PR.
6. Run the complete local validation suite and obtain manual approval.
7. Update `Last reviewed` or `Last verified` only for pages actually examined.

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
