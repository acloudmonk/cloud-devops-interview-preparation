# Security and Threat Modeling

[← Workload identity](workload-federation.md) · [Next: Operations →](operations-governance.md)

Threat-model discovery, login, redirect, token issue, browser/workload storage,
gateway, service hop, policy decision, data access, logs, and recovery. Identity
controls are themselves high-value attack paths.

## Material threats and controls

| Threat | Required reasoning |
| --- | --- |
| Broken object authorization | enforce every resource action from trusted context |
| Broken authentication | strong enrollment/recovery, MFA, session and bot controls |
| Token theft/replay | secure storage, short life, audience, sender constraint when needed |
| Redirect/mix-up/CSRF | exact redirects, PKCE, state/nonce, issuer validation |
| JWT confusion | algorithm allowlist, issuer/audience/type/key and claim validation |
| Tenant confusion | bind issuer, tenant, subject, resource, and provisioning authority |
| API abuse | schema/size/depth limits, quotas, cost controls, anomaly detection |
| Webhook forgery | raw-body signature, timestamp, replay cache, rotation |
| SSRF/injection | destination policy, parsing/encoding, allowlists, isolation |
| Key compromise | inventory, protected signing, rotation, revocation, blast-radius query |

Do not log access or refresh tokens, secrets, assertions, or sensitive claims.
Correlation should retain actor, client, tenant, action, resource, policy version,
result, reason, and request ID without turning logs into a credential store.

## Recovery as a security control

Protect administrator recovery, signing-key change, federation configuration,
client registration, redirect URI, and policy deployment more strongly than routine
login. Require separation of duties, change evidence, alerts, tested rollback, and
independent recovery for the identity control plane.

## Verification

Use contract and negative tests, authorization matrix and tenant-isolation tests,
fuzzing, dependency review, dynamic testing, abuse simulation, and incident drills.
Scanner findings are evidence inputs, not proof that the trust model is correct.
