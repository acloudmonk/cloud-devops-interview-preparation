# Gateways and API Management

[← Interaction styles](api-styles-integration.md) · [Next: Identity protocols →](identity-protocols.md)

A gateway is an enforcement and routing point, not the owner of every business rule.

## Gateway responsibilities

- TLS termination or pass-through, routing, protocol translation, and safe transforms;
- token or request validation, coarse policy, WAF integration, and threat limits;
- per-consumer quotas, rate/concurrency limits, payload limits, and timeouts;
- correlation, access logs, latency/error metrics, and trace propagation;
- version routing, canary release, developer onboarding, keys, and API products.

Keep object-level authorization and business invariants close to authoritative data.
A gateway-only check can be bypassed by internal paths and usually lacks resource
context. Avoid large transformation logic that creates an untestable shared monolith.

## Traffic economics and fairness

Distinguish spike protection, sustained quota, concurrency, and downstream capacity.
Key limits by authenticated consumer and business tier, not only source IP. Return
clear retry guidance without revealing sensitive capacity. Protect expensive
operations separately and measure cost per successful business unit.

## AWS anchor and translations

Use Amazon API Gateway for managed REST, HTTP, or WebSocket entry, AWS WAF for
applicable edge threats, Cognito/JWT/IAM/Lambda authorizers for identity integration,
and CloudWatch/X-Ray for evidence. Azure API Management and Google Cloud API Gateway
or Apigee provide related capabilities, but policy and identity semantics differ.

## Failure design

Decide behavior when identity, policy, quota storage, developer portal, certificate,
or gateway control plane fails. Prefer cached verified keys and bounded policy data
where safe; never silently fail open for sensitive authorization. Preserve a tested
break-glass path with narrow scope, expiry, approval, and audit.
