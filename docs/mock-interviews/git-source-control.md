# Mock Interview: Git and Source-Control Strategy

[← Git module overview](../08-git/index.md) ·
[Master competency map](../master-competency-map.md)

Use this 50-minute interview after completing Module 08. Reveal follow-ups only
when their section begins.

## Candidate brief

A 180-engineer organization uses long-lived development, staging, and production
branches across 40 repositories. Releases are slow, hotfixes are lost, checks
are flaky, administrators frequently bypass policy, and a credential was
recently committed. Design a safer operating model and lead recovery.

## Schedule

| Time | Candidate task | Interviewer observes |
| --- | --- | --- |
| 0–5 min | Clarify delivery, support, ownership, regulatory, and incident needs | Discovery before workflow preference |
| 5–13 min | Explain the object/ref/commit graph and shared-history risks | Git mental model |
| 13–23 min | Design branch, integration, release, and backport model | Flow and traceability trade-offs |
| 23–32 min | Design reviews, rules, checks, ownership, and emergency access | Governance quality |
| 32–39 min | Respond to leaked secret and accidental force push | Security and recovery |
| 39–45 min | Choose repository boundaries and migration | Architecture and adoption |
| 45–50 min | Give an executive recommendation | Concision, risk, and ownership |

## Required follow-ups

1. A commit disappeared after an interactive rebase. What do you preserve and inspect?
2. Why might reverting a merge not allow the same branch to reapply its changes?
3. The checks were green before merge but main broke. What trust/integration state was missed?
4. The secret was deleted in the next commit. Why is the incident not resolved?
5. The source-control provider is unavailable during an urgent production fix. What is allowed?

## Branching follow-ups

| Candidate choice | Ask |
| --- | --- |
| Adopt trunk-based development | Which automation, flags, and migration prerequisites exist? |
| Use squash merge | Which ancestry/audit information moves to PR metadata? |
| Require signing | How are keys issued, revoked, and handled for bots? |
| Rewrite leaked-secret history | Which refs, forks, caches, signatures, and consumers break? |
| Use a monorepo | How do permissions, CI selection, ownership, and releases remain independent? |
| Permit emergency bypass | Who authorizes it, how is it bounded, and when is it reconciled? |

## Scorecard

Score each dimension from 0 to 4.

| Dimension | 0–1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- |
| Discovery | Chooses favorite workflow | Basic team/release questions | Delivery, risk, support, trust, recovery | Finds constraints that change the model |
| Git model | Command trivia | Basic commits/branches | Correct objects, refs, graph, published state | Predicts subtle identity/ancestry effects |
| Workflow | Generic GitFlow/trunk | Plausible branches | Constraint-based lifecycle/backports | Migration and measurable flow design |
| Governance | “Require PRs” | Reviews and checks | Ownership, trusted checks, queue, exceptions | Separates judgment, automation, and authority |
| Security | Delete leaked file | Rotation mentioned | Exposure, identity, workflow, signing lifecycle | Integrates incident, audit, and supply-chain trust |
| Recovery | Fresh clone/reset | Plausible commands | Preserve graph/evidence and recover safely | Coordinates every consumer and prevents recurrence |
| Architecture | Mono/multi preference | Lists trade-offs | Boundaries from access/coupling/release | Migration, scale, continuity, and ownership |
| Communication | Tool dump | Understandable | Structured and decision-oriented | Controls time and executive risk discussion |

Maximum score: **32**. A score of 25 or more with no dimension below 2 is a
strong senior-level practice result.

## Reflection

Record one missed constraint, one incorrect graph assumption, one unsafe command,
one weak control, and one answer to shorten. Repeat within seven days.
