# Mock Interview: Linux Production Operations

[← Linux module overview](../06-linux/index.md) ·
[Master competency map](../master-competency-map.md)

Use this 50-minute interview after completing the Linux module. Reveal each
follow-up only when its section begins.

## Candidate brief

A document-conversion service runs on 60 Linux EC2 instances across three
Availability Zones. At peak, latency rises, some workers are OOM-killed, and
temporary files occasionally fill the root filesystem. A recent security patch
made part of the fleet fail readiness. Design the operating and troubleshooting
model without deploying infrastructure.

## Schedule

| Time | Candidate task | Interviewer observes |
| --- | --- | --- |
| 0–5 min | Clarify workload, accepted-work invariant, objectives, and scope | Discovery before commands |
| 5–15 min | Explain process, resource, storage, and service lifecycle | OS mental model and limits |
| 15–27 min | Diagnose peak OOM and latency symptoms | Hypothesis-led evidence and safe mitigation |
| 27–36 min | Handle full disk, failed readiness, and lost access | Recovery and failure boundaries |
| 36–43 min | Design patching, identity, fleet replacement, and telemetry | Security/reliability trade-offs |
| 43–47 min | Compare repair-in-place with immutable replacement | Operating-model judgment |
| 47–50 min | Give an executive summary | Concision, ownership, and next decision |

## Required follow-ups

1. Load average is high while aggregate CPU is moderate. What do you inspect and why?
2. A worker OOMs while the host still has available memory. Explain the boundary.
3. Deleting the largest log does not release disk space. What is your hypothesis?
4. EC2 reports running and healthy, but requests fail. What does each signal prove?
5. Both SSH and the managed-session agent are unavailable. What is the recovery path?

## Branching follow-ups

| Candidate choice | Ask |
| --- | --- |
| Restart service | Which evidence is lost, which work is interrupted, and how is it reconciled? |
| Add memory | What distinguishes leak, limit, workload growth, and reclaim pressure? |
| Repair host | Why not replace it, and how will drift be reconciled? |
| Replace host | Could the image or configuration recreate the failure fleet-wide? |
| Disable security control | Who accepts the risk and what bounded alternative exists? |
| Collect a dump | What data exposure, overhead, approval, and retention controls apply? |

## Scorecard

Score each dimension from 0 to 4.

| Dimension | 0–1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- |
| Discovery | Starts with commands | Basic symptom questions | Customer, time, scope, change, invariant | Finds ambiguity that changes recovery |
| OS model | Component trivia | Plausible concepts | Correct layer/resource reasoning | Explains subtle limits and interactions |
| Diagnosis | Random checklist | Several useful checks | Falsifiable hypotheses and comparisons | Minimal safe evidence with sensitivity controls |
| Mitigation | Restart/reboot | Plausible action | Reversible and verifies customer recovery | Preserves evidence, capacity, and invariants |
| Recovery | Process starts | Checks service | Reconciles work and measures objective | Handles failback, drift, and systemic recurrence |
| Security | Generic controls | Mentions least privilege | Identity, access fallback, audit, data handling | Risk-based decision integrated with operations |
| Fleet design | Pets/manual repair | Some automation | Image, canary, drain, replace, inventory | Clear decision triggers and organizational ownership |
| Communication | Tool dump | Understandable | Structured and concise | Controls time and converts evidence into decisions |

Maximum score: **32**. A score of 25 or more with no dimension below 2 is a
strong senior-level practice result.

## Reflection

Record one missed scoping question, one weak mechanism explanation, one unsafe
or irreversible action, one missing verification signal, and one answer to
shorten. Repeat the same prompt within seven days.
