# Credentials, Secrets, Keys, and PKI

[← Module overview](index.md) · [Module 15: DevSecOps](../15-devsecops/index.md)

Zero Trust reduces reusable bearer credentials, but cannot eliminate all secrets
or cryptographic trust. The architecture must cover issuance, distribution,
storage, use, rotation, revocation, recovery, and evidence.

## Credential preference

Prefer, in order: platform-provided workload identity; federation and token
exchange; short-lived automatically issued certificates or tokens; dynamically
generated secrets; and finally managed static secrets when legacy systems require
them. A secret manager protects storage and delivery—it does not make a static,
overprivileged password short-lived.

## Token and session controls

- Validate issuer, signature, audience, subject, time, nonce, and intended use.
- Keep access tokens brief and constrain refresh tokens and session cookies.
- Never place sensitive bearer tokens in URLs, logs, source, or images.
- Bind tokens to sender or client where the ecosystem supports it.
- Plan signing-key overlap, verifier refresh, replay defense, and emergency revoke.

## PKI design questions

Define trust domains, certificate profiles, subject naming, issuance authority,
private-key protection, maximum lifetime, renewal, revocation behavior, audit, and
root/intermediate recovery. Short-lived certificates reduce dependence on
revocation lists but require highly available issuance and reliable time.

## AWS-first controls

Use STS role sessions instead of IAM user access keys; Secrets Manager or Systems
Manager Parameter Store where secrets remain; KMS for controlled key use; ACM for
supported public/private certificate lifecycle; and AWS Private CA where a managed
private hierarchy fits. Apply resource policies, separation of duties, encryption
context, rotation, and centralized evidence. Equivalent Azure services include
managed identities, Key Vault, and Managed HSM; Google Cloud offers Workload
Identity Federation, Secret Manager, Cloud KMS, and Certificate Authority Service.

## Rotation and compromise

Rotation is complete only when producers issue new material, consumers adopt it,
old material is disabled, failures are visible, and rollback is controlled. During
compromise, preserve evidence, contain the issuer or credential, identify every
consumer and use, replace trust, verify recovery, and address the issuance path—not
just the exposed secret.

Return to the [module overview](index.md) when ready to continue.
