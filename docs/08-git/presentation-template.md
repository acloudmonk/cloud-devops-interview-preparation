# Ten-Minute Source-Control Review

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

Use one repository/flow diagram and one control matrix. Do not present a list of
Git commands.

| Time | Content |
| --- | --- |
| 0:00–1:00 | Business, delivery, security, regulatory, and recovery requirements |
| 1:00–2:15 | Repository boundaries, ownership, and source-of-truth model |
| 2:15–3:30 | Commit, branch, integration, release, and backport lifecycle |
| 3:30–5:00 | PR reviews, CODEOWNERS, rules, checks, queue, and merge method |
| 5:00–6:15 | Human/bot identity, signing, secrets, workflow trust, and audit |
| 6:15–7:30 | Emergency, provider-outage, force-push, and recovery procedures |
| 7:30–8:30 | Migration/adoption plan and developer experience |
| 8:30–9:15 | Flow, quality, bypass, and recovery metrics |
| 9:15–10:00 | Top risks, decision required, owner, and next measurable step |

## Quality checklist

- The commit graph and source of truth are unambiguous.
- Branch policy follows real delivery/support constraints.
- Required checks are bound to trusted identities and current commits.
- External code cannot access privileged secrets or write tokens.
- Emergency access is bounded, audited, tested, and reconciled.
- Backup covers refs, metadata, releases, policy, and restore testing.
- The close identifies one decision, evidence, owner, and deadline.
