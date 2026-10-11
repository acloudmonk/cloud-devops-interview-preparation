# API and Identity Decision Model

[← Module overview](index.md) · [Next: API contracts →](api-design-contracts.md)

Use one reasoning chain: **capability → consumer → interaction → contract → actor →
trust → policy → operation → evidence**. Product names come after these decisions.

## Core distinctions

| Concern | Question | Common failure |
| --- | --- | --- |
| Capability | What business action or information is exposed? | API mirrors an internal database |
| Consumer | Human, browser, mobile app, partner, service, or operator? | One trust model for every actor |
| Interaction | Sync, async, streaming, callback, or batch? | REST chosen by habit |
| Contract | What semantics remain stable? | Schema-only compatibility |
| Authentication | Who or what presented this credential? | Treated as permission |
| Authorization | May this actor perform this action here and now? | UI hiding replaces enforcement |
| Delegation | Is an app acting for a user? | User password shared with client |
| Federation | Which external assertion is trusted and mapped? | Mutable email treated as identity |
| Evidence | What proves issue, decision, use, and change? | Tokens logged without decisions |

## Four planes

1. **Consumer plane** — applications, users, partners, SDKs, and credentials.
2. **API data plane** — gateways, services, policies, traffic, and business data.
3. **Identity/policy plane** — issuer, directory, keys, consent, and authorization.
4. **Management plane** — definitions, onboarding, deployment, audit, and recovery.

Separating the planes exposes common-mode failure. A healthy API cannot authorize
new requests if its only policy service is unavailable; a healthy identity provider
cannot fix an incompatible contract.

## Decision record

Record capability owner, consumers, data classification, protocol/style, contract
and compatibility promise, identity issuer, token audience, authorization owner,
tenant boundary, availability target, abuse controls, evidence, cost, lifecycle,
and emergency/recovery authority.

## Interview answer shape

State the consumer journey and invariant, select interaction and contract, trace
identity and authorization end to end, protect the boundary, describe failure and
recovery, then close with trade-offs, evidence, owner, and migration path.
