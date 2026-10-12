# Contributing

Contributions should improve practical architect-level judgment, not simply add
lists of products or commands.

## Branch and pull-request workflow

The protected integration branch is **`main`**. Do not perform milestone work
directly on `main` after the initial repository bootstrap.

1. Synchronize your local `main` branch with the remote.
2. Create a dedicated branch for one bounded milestone or change.
3. Use a descriptive name such as `feature/milestone-02-linux-networking`.
   Codex-created branches use the `codex/feature/` prefix.
4. Keep commits reviewable and use imperative commit subjects.
5. Push the feature branch and open a pull request targeting `main`.
6. Wait for documentation, Markdown, link, and secret-scanning checks.
7. Require manual review and approval before merging.
8. Delete the feature branch after the merge.

Milestones must not be merged directly or automatically. Repository settings
should protect `main`, require a pull request, require passing status checks,
require at least one approval, dismiss stale approvals after new commits, and
block force pushes and deletion.

## Authoring principles

1. Start with the business problem and non-functional requirements.
2. Explain at least one viable alternative and the trade-off behind the choice.
3. Cover security, reliability, operability, and cost where relevant.
4. Prefer primary sources: specifications, official documentation, standards,
   and first-party engineering material.
5. Summarize sources in original language. Do not copy documentation or video
   transcripts.
6. Date-sensitive material must include a `Last reviewed` date.
7. Commands and examples must be safe, minimal, and reproducible.
8. Any separately approved future cloud implementation lab must include
   prerequisites, estimated cost, security constraints, validation, and teardown.

## Pull-request checklist

- [ ] The page has a clear learning objective and intended audience.
- [ ] Acronyms are expanded on first use.
- [ ] Architecture choices include constraints and trade-offs.
- [ ] External references are authoritative and reachable.
- [ ] Examples do not contain credentials, account identifiers, or secrets.
- [ ] The local documentation build passes with `--strict`.
- [ ] The competency map is updated if module status changed.
- [ ] Generated output, virtual environments, caches, state, and local tool
      configuration are not included.
- [ ] Secret scanning passes and no exception suppresses a real credential.
- [ ] The pull request targets `main` and has manual approval before merge.

## Released-module quality gate

A module can be marked **Initial release** only when it provides a complete,
ordered interview-preparation path rather than a collection of disconnected pages.
Topic-specific depth can vary, but every released module must include:

- a numbered path of at least 15 steps, `Last reviewed` metadata, a clear starting
  point, learning objectives, scope or adjacent-module boundaries, and a completion
  checklist;
- architect-level theory covering decisions, alternatives, trade-offs, security,
  reliability, operations, cost, and cross-cloud translation where relevant;
- a scored design exercise or equivalent architecture walkthrough;
- at least 15 scenario questions with model answers;
- at least 10 separately headed advanced drills, each with substantive response
  guidance rather than a one-line prompt;
- at least 50 rapid-fire questions and 25 active-recall flashcards;
- a timed, scored mock interview linked from the module path;
- at least 15 authoritative references, three relevant video sources, durable
  book recommendations, and a reading order or source-review loop; and
- working navigation plus passing strict build, Markdown, link, secret, and
  released-module quality checks.

All numeric requirements above are **minimum floors, not maximums**. Add more
material when it contributes distinct interview value and remains well structured;
do not add repetition merely to increase a count.

Run `python scripts/check_module_quality.py` before requesting review. This check
is a minimum structural gate; reviewers must still assess technical accuracy,
clarity, currency, originality, and the quality of engineering judgment.

## Templates

Use the files in `docs/templates/` for chapters, scenarios, architecture design
exercises, and reference entries. Consistent structure makes the repository easier
to review and study.
