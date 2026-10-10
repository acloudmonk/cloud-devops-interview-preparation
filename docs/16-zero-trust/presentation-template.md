# Ten-Minute Zero Trust Architecture Review

[← Module overview](index.md) · [Design exercise](design-exercise.md)

Use this structure to present a Zero Trust recommendation to technical and
executive interviewers. Lead with risk reduction and business access, not products.

## 0:00–1:00 — Outcome and current risk

State the protected business transactions, users/workloads, most important
implicit trust, recent failure, constraints, and success measures.

## 1:00–2:00 — Principles and scope

Define explicit verification, least privilege, assume breach, resource focus, and
the bounded first protect surface. Correct the "trust nothing" misconception.

## 2:00–4:00 — Decision architecture

Draw subject/request, identity and posture signals, policy decision, enforcement,
protected resource, telemetry, revocation, and ownership. Trace one human and one
workload transaction end to end.

## 4:00–5:30 — Defense and failure containment

Cover phishing-resistant authentication, short-lived identity, authorization,
segmentation, data policy, credential lifecycle, alternate-path prevention, and
how these limit lateral movement.

## 5:30–6:30 — Availability and recovery

Explain IdP, proxy, policy, posture, DNS, and certificate failures; bounded cached
decisions; fail-open/fail-closed choices; rollback; and monitored break-glass.

## 6:30–7:30 — AWS and multi-cloud

Anchor the design in AWS Organizations, IAM Identity Center, STS roles,
resource/data perimeters, identity-aware access, and centralized evidence. Map
outcomes—not product names—to Azure and Google Cloud.

## 7:30–9:00 — Migration and ownership

Show discovery, foundational hygiene, a valuable pilot, reusable paved paths,
observe/warn/enforce waves, legacy coexistence, exception expiry, and retirement.
Name identity, endpoint, platform, resource, security, and risk owners.

## 9:00–10:00 — Measures and decision

Report exposure, standing privilege, credential lifetime, revocation, denied and
false-denied access, exceptions, containment, availability, and successful user
tasks. Close with the first decision, trade-off, and validation needed.

Return to the [module overview](index.md) when ready to continue.
