# Advanced Git Incident Drills

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

These ten drills bring the module total to 25 scenarios. Give a five-minute
answer before reading the coaching cues.

## 1. Accidental force push during release

**Coaching cues:** Freeze pushes, preserve both remote and clone tips, locate the
expected ref through audit/reflogs/CI, choose restoration versus integration,
update under incident authority, notify consumers, and prevent recurrence.

## 2. History rewrite reintroduces a revoked secret

**Coaching cues:** Keep the credential revoked, stop pushes, identify the clone
or branch that restored old objects, coordinate every ref/fork/cache, add server
blocking, and verify exposure—not only the default branch.

## 3. Merge queue starves urgent fixes

**Coaching cues:** Measure queue and test time, flakiness, batch behavior, and
priority policy. Define an audited emergency lane with minimum evidence and
post-merge reconciliation; do not normalize bypassing all checks.

## 4. Repository administrator bypasses protections

**Coaching cues:** Treat admin as a governed privileged role. Preserve audit,
validate intent/impact, rotate compromised access if relevant, require bounded
break glass and independent review, and configure rules to include administrators.

## 5. Cherry-pick is clean but release fails

**Coaching cues:** Textual applicability is not semantic compatibility. Compare
dependencies, configuration, migrations, tests, and surrounding commits; revert
the release-line change and implement/version an appropriate backport.

## 6. Signed tag points to the wrong commit

**Coaching cues:** Stop publication, preserve tag/artifact/provenance evidence,
assess whether tags are mutable, revoke affected release authorization, create a
new unambiguous version under policy, and notify consumers. Never silently retag.

## 7. CI bot can approve its own workflow change

**Coaching cues:** This is a trust-cycle flaw. Restrict bot permissions, require
independent ownership for workflow/policy paths, separate untrusted evaluation
from privileged actions, rotate tokens, and review prior changes made under it.

## 8. Large binary deleted but repository stays large

**Coaching cues:** The object remains in history. Identify all references and
consumers; choose retention versus coordinated filtering/LFS migration; freeze,
back up, rehearse, rewrite, verify, and block reintroduction.

## 9. Rebase changed tested commit IDs before release

**Coaching cues:** Evidence may bind to old objects. Re-run required checks on
the exact new head, require fresh approval if material, and design the process
so release authorization refers to immutable reviewed commits/artifacts.

## 10. Ownership team is unavailable during incident

**Coaching cues:** Use documented alternates and bounded emergency authority,
record risk and changes, preserve least privilege, monitor/rollback, and require
owner review afterward. Fix ownership coverage rather than making bypass permanent.
