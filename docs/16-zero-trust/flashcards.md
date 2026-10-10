# Zero Trust Active-Recall Flashcards

[← Module overview](index.md) · [Rapid-fire revision](rapid-fire.md)

Use these cards without looking at the answer. Mark a card weak if you cannot add
one failure mode and one trade-off.

| Front | Back |
| --- | --- |
| Zero Trust in one precise sentence | Explicit, least-privilege access decisions around resources using current evidence, enforcement, and feedback instead of implicit location trust. |
| Seven-part decision model | Resource, subject, signals, policy, decision, enforcement, feedback. |
| Four questions for a protect surface | What resource/transaction, which subjects, which required flows, and which business impact? |
| MFA versus authorization | MFA strengthens subject authentication; authorization still constrains resource, action, condition, and duration. |
| Federation's hidden concentration risk | IdP administration, signing keys, session issuance, availability, and recovery become high-blast-radius dependencies. |
| Phishing-resistant examples | FIDO2/WebAuthn security keys and passkeys with appropriate identity proofing and recovery. |
| RBAC plus ABAC | Roles provide understandable baseline; authoritative attributes narrow access by resource and context. |
| Safe adaptive policy rule | Deterministic grant boundary first; current risk may constrain, challenge, or deny inside it. |
| Managed-device misconception | Management and posture add evidence; they do not prove the device is uncompromised. |
| Workload identity chain | Platform identity → scoped token/certificate → destination authorization → attributable log → revocation. |
| mTLS limitation | Authenticates accepted certificate possession and protects transport; does not establish application/business authorization. |
| Private endpoint limitation | Reduces exposure and supplies context; does not replace identity or least-privilege resource policy. |
| Data-perimeter triad on AWS | Trusted identities, trusted resources, and expected networks/service paths. |
| Token validation essentials | Issuer, signature, audience, subject, time, intended use, and replay controls. |
| Complete secret rotation | Issue new, update consumers, disable old, observe failures, and preserve controlled rollback. |
| Policy deployment controls | Version, review, positive/negative tests, simulation, canary, telemetry, rollback, recovery separation. |
| Resource-specific dependency failure | Choose deny, reduced capability, bounded cache, or emergency access from risk and recovery needs. |
| Break-glass qualities | Independent, narrow, strongly authenticated, short, monitored, reviewed, and regularly tested. |
| Five adoption phases | Discover/stabilize, pilot, expand, enforce, optimize. |
| Three outcome measures | Example: standing privilege, time to revoke, lateral paths—balanced with successful user tasks. |
| AWS workforce anchor | External IdP/IAM Identity Center, permission sets and short role sessions, Organizations guardrails, CloudTrail evidence. |
| AWS workload anchor | Platform-specific IAM roles and STS; avoid shared access keys and node-role leakage. |
| Azure translation anchors | Entra ID, Conditional Access, PIM, managed identities, Azure Policy, Key Vault, Defender/Monitor. |
| Google Cloud translation anchors | Cloud Identity/federation, Context-Aware Access, IAM, workload federation, organization policy, SCC/Audit Logs. |
| Strong architecture test | Name removed implicit trust, replacement evidence, non-bypassable enforcement, expiry/revocation, and safe failure behavior. |

Return to the [module overview](index.md) when ready to continue.
