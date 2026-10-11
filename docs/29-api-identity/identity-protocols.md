# Identity and Federation Protocols

[← Gateways](gateway-management.md) · [Next: Authorization →](authorization-policy.md)

Protocols solve different problems. Do not use “OAuth login” as a substitute for
an explicit authentication and delegation design.

| Mechanism | Primary purpose | Critical boundary |
| --- | --- | --- |
| OAuth 2.0 | delegated authorization to an API | client, authorization server, resource server |
| OpenID Connect | authentication layer using OAuth flows | ID token audience, nonce, issuer, session |
| SAML 2.0 | browser enterprise federation assertions | service provider, IdP, audience, recipient |
| SCIM | user/group provisioning lifecycle | source authority, mapping, disable/delete semantics |
| JWT | compact claims format | signature does not make claims appropriate or current |
| Session cookie | application session handle/state | browser origin, CSRF, expiry, server revocation |

## Token discipline

An ID token tells a client about authentication; it is not an API access token.
An access token is for its resource audience and scopes; do not forward it to an
unrelated service. A refresh token obtains new access and needs stronger storage,
rotation, reuse detection, and revocation. Validate issuer, audience, signature,
algorithm policy, time, token type, required claims, and tenant before use.

Use authorization code with Proof Key for Code Exchange (PKCE) for browser/mobile
public clients. Avoid implicit flow and resource-owner password sharing. Use exact
redirect matching, state/nonce as applicable, issuer checks, secure browser storage,
and back-channel patterns when risk justifies them.

## Enterprise federation lifecycle

Define immutable external identity key, tenant routing, attribute authority,
just-in-time versus pre-provisioning, group/role mapping, step-up authentication,
account linking, disable/delete latency, and recovery. SCIM provisioning and single
sign-on are complementary; login success does not prove lifecycle governance.

## AWS anchor

Use IAM Identity Center for workforce access, Amazon Cognito for applicable customer
identity use cases, IAM roles for AWS authorization, and explicit federation trust.
Keep workforce, customer, partner, and workload identity populations separate.
