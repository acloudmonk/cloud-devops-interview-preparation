# v1 Curriculum Readiness Report

[← Documentation home](index.md) · [Master competency map](master-competency-map.md)

Audit date: **2026-10-11**

## Outcome

The repository is ready to serve as a **v1 curriculum baseline** after this audit
passes pull-request CI. All original plan points have destinations, all 31 numbered
modules are initial releases, and the remaining work is study execution, periodic
source review, and evidence-driven improvement—not additional breadth by default.

## Inventory

| Asset | Verified inventory |
| --- | ---: |
| Original preparation points traced | 36 |
| Numbered modules in canonical learner order | 31 |
| Numbered modules with complete minimum practice path | 31 |
| Module mock interviews | 31 |
| Consultant discovery mock interviews | 1 |
| Cross-domain case studies | 8 |
| Consultant playbook steps | 15 |

## Two indexes, two purposes

| Page | Primary question | Numbering |
| --- | --- | --- |
| [Current learning path](index.md#current-learning-path) | What should I study next? | Study steps 1–31 in dependency order |
| [Master competency map](master-competency-map.md) | Where is each original requirement covered? | Original plan points 1–36 and Module ID order |

They must contain the same 31 module destinations, but they should not use the same
row order. The learning path follows prerequisites; the competency map preserves
traceability and Module IDs. Original point 1 defines the master map; points 33–36
define the interview framework, case studies, roadmap, and collaboration system
rather than additional numbered modules. CI now rejects missing, duplicated, or
incorrectly ordered study modules.

## Automated evidence

The module-quality validation command verifies:

- all released modules referenced by the competency map;
- the contiguous 1–31 study steps, exact dependency sequence, and the same module
  set as the competency map;
- required module pages, starting metadata, ordered paths, scenarios and answers;
- at least 10 substantive drills, 50 rapid-fire questions, and 25 flashcards;
- at least 15 references, three video sources, books, and review guidance;
- an existing timed, scored mock interview for every module;
- the eight-case cross-domain practice track;
- the 15-step Consultant Discovery Playbook and its practice minimums;
- absence of any module or map row still marked Planned.

Pull-request workflows also run strict MkDocs, repository-wide Markdown lint,
external/internal link validation, and secret scanning.

## Manual consistency review

- Repository README, documentation home, curriculum overview, competency map, roadmap,
  case studies, consultant playbook, and mock-interview index have explicit entry points.
- The last stale “planned” cross-references in Modules 16–18 were corrected.
- Module boundaries link to specialist material rather than duplicating all depth.
- Detailed deployment labs and hosted documentation remain intentionally outside the
  required learning path.
- Ordinary terms such as pilot-light recovery, pilot adoption, and planned maintenance
  remain because they describe architecture practices, not incomplete content.

## Ongoing maintenance

1. Follow the 24-week roadmap and use the
   [study progress log](study-progress.md) to record weak concepts and repeat scores.
2. Improve pages when learner evidence, incidents, interviews, or source changes justify it.
3. When explicitly requested, follow the [manual maintenance process](maintenance.md)
   to recheck provider service names, limits, prices, Regions, references, and
   framework guidance.
4. Preserve feature-branch, pull-request, manual-approval, and secret-scan practices.
5. Treat new modules as exceptional; prefer deepening an existing owner module.

## Release decision

After this audit PR is merged and all checks pass, maintainers may tag a v1 release.
Tagging and publishing release notes remain an explicit maintainer decision and are
not performed automatically by this audit.
