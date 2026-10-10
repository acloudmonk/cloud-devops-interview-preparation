# Workforce Identity and Federation

[← Module overview](index.md) · [Scenario answer framework](../interview-playbook/scenario-answer-framework.md)

Workforce Zero Trust begins with a governed identity lifecycle, not an MFA
purchase. An architect connects authoritative people records to accounts,
entitlements, sessions, privileged actions, evidence, and rapid revocation.

## Identity lifecycle

1. Establish an authoritative source for employees, partners, and service owners.
2. Provision through groups and governed attributes rather than one-off grants.
3. Separate identity proofing, authentication, federation, and authorization.
4. Reconcile joiner, mover, leaver, dormant-account, and contractor expiry events.
5. Review resource-level access with accountable owners and remove unused grants.

Use one enterprise identity provider where practical, federate to applications
and clouds with OIDC or SAML, and automate lifecycle exchange where supported.
Federation reduces password and key sprawl but concentrates dependency and blast
radius, so protect administration, signing keys, recovery, and audit paths.

## Authentication assurance

Prefer phishing-resistant authenticators such as FIDO2/WebAuthn security keys or
passkeys for privileged and high-risk access. SMS or one-time codes are weaker
against phishing and session interception. Match proofing and authentication
strength to resource risk, then define step-up conditions and recovery controls.

Authentication is not the end of the decision. Protect session cookies and tokens;
constrain audience, issuer, subject, scope, and lifetime; rotate signing material;
and revoke or re-evaluate sessions when identity, device, or risk changes.

## Privileged access

- Separate daily and administrative personas.
- Make elevation just-in-time, scoped, approved, recorded, and expiring.
- Protect cloud root/owner roles and IdP administration with stronger controls.
- Avoid standing human access to production where brokered operations suffice.
- Maintain independent, tested break-glass identities with monitored use.

## AWS-first pattern

Federate the workforce through IAM Identity Center into permission sets and
short-lived role sessions. Use AWS Organizations and SCPs as guardrails, not as
resource entitlements. Analyze external and unused access, record authentication
and API activity, and centralize security investigation. Azure maps to Microsoft
Entra ID, Conditional Access, Privileged Identity Management, and Azure RBAC;
Google Cloud maps to Cloud Identity, Workforce Identity Federation, IAM,
organization policy, and Privileged Access Manager.

## Failure questions

Plan for IdP outage, stolen session, malicious administrator, synchronization
delay, lost authenticator, federation-key compromise, and erroneous mass
deprovisioning. Recovery must not silently restore broad permanent access.

Return to the [module overview](index.md) when ready to continue.
