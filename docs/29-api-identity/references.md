# APIs and Enterprise Identity References

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Verify protocol status, provider feature, quota, pricing, Region, SLA, token claim,
and support behavior in current documentation before production decisions.

## Core reading order

1. [HTTP Semantics — RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html)
2. [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
3. [OAuth 2.0 Security Best Current Practice — RFC 9700](https://www.rfc-editor.org/rfc/rfc9700.html)
4. [OpenID Connect Core](https://openid.net/specs/openid-connect-core-1_0.html)
5. [OWASP API Security Top 10](https://owasp.org/API-Security/)

## API styles and contracts

- [gRPC documentation](https://grpc.io/docs/)
- [GraphQL specification](https://spec.graphql.org/)
- [AsyncAPI specification](https://www.asyncapi.com/docs/reference/specification/latest)
- [CloudEvents specification](https://cloudevents.io/)
- [JSON:API specification](https://jsonapi.org/format/)

## Identity and security standards

- [OAuth 2.0 — RFC 6749](https://www.rfc-editor.org/rfc/rfc6749.html)
- [Bearer Token Usage — RFC 6750](https://www.rfc-editor.org/rfc/rfc6750.html)
- [Proof Key for Code Exchange — RFC 7636](https://www.rfc-editor.org/rfc/rfc7636.html)
- [JSON Web Token — RFC 7519](https://www.rfc-editor.org/rfc/rfc7519.html)
- [OAuth Token Exchange — RFC 8693](https://www.rfc-editor.org/rfc/rfc8693.html)
- [SCIM Protocol — RFC 7644](https://www.rfc-editor.org/rfc/rfc7644.html)
- [SAML 2.0 technical overview](https://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0.html)
- [SPIFFE specifications](https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/)

## AWS anchor

- [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html)
- [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html)
- [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)
- [IAM OIDC federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html)
- [IAM Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html)
- [Amazon Verified Permissions](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/what-is-avp.html)

## Azure translation

- [Azure API Management](https://learn.microsoft.com/azure/api-management/api-management-key-concepts)
- [Microsoft identity platform protocols](https://learn.microsoft.com/entra/identity-platform/v2-protocols)
- [Microsoft Entra workload identity federation](https://learn.microsoft.com/entra/workload-id/workload-identity-federation)
- [Azure role-based access control](https://learn.microsoft.com/azure/role-based-access-control/overview)

## Google Cloud translation

- [Google Cloud API Gateway](https://cloud.google.com/api-gateway/docs)
- [Apigee documentation](https://cloud.google.com/apigee/docs)
- [Workload Identity Federation](https://cloud.google.com/iam/docs/workload-identity-federation)
- [Cloud Identity and Access Management](https://cloud.google.com/iam/docs/overview)

## Targeted video and discovery channels

- [Google Cloud: API security in Apigee](https://www.youtube.com/watch?v=O_xCDsFysgY)
- [AWS Events](https://www.youtube.com/@AWSEventsChannel)
- [Microsoft Developer](https://www.youtube.com/@MicrosoftDeveloper)
- [Google Cloud Tech](https://www.youtube.com/@googlecloudtech)

## Books for deeper study

- *API Design Patterns* by JJ Geewax
- *OAuth 2 in Action* by Justin Richer and Antonio Sanso
- *Identity-Native Infrastructure Access* by Ev Kontsevoy, Sakshyam Shah, and Peter Conrad
- *Enterprise Integration Patterns* by Gregor Hohpe and Bobby Woolf

Use books for durable mental models and official specifications/provider documents
for current protocol and service behavior.

## Suggested review loop

1. Learn HTTP, API contract, and OAuth/OIDC boundaries from the core sources.
2. Trace one browser, partner, and workload flow with issuer, audience, policy, and data.
3. Study the AWS anchor, then translate intent—not product names—to Azure and Google.
4. Use OWASP and the protocol security guidance to attack your design assumptions.
5. Use video only for a weak concept and verify details in the written primary source.
6. Return to scenarios and explain failure, recovery, evidence, owner, and trade-off.

Return to the [module overview](index.md) when ready to continue.
