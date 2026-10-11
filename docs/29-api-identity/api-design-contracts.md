# API Contracts and Lifecycle

[← Decision model](concepts.md) · [Next: Interaction styles →](api-styles-integration.md)

An API contract includes semantics, failure behavior, authorization, limits, and
lifecycle—not only an OpenAPI schema.

## HTTP contract choices

- Model stable business resources and actions; do not expose storage tables.
- Use methods and status codes consistently; document conditional and partial outcomes.
- Make retryable writes idempotent with a scoped key, request fingerprint, retained
  outcome, expiry policy, and concurrency rule.
- Define deterministic pagination, stable cursors, filters, sorting, maximum sizes,
  and behavior when the dataset changes.
- Use structured errors with safe code, message, correlation ID, retryability, and
  field detail; never leak credentials or internals.
- State concurrency control, such as entity tags or versions, when lost updates matter.

## Compatibility and versioning

Prefer additive compatible change, tolerant readers, consumer contract tests, and
observed usage. Version only when semantics cannot remain compatible. A version can
appear in a path, header, media type, schema, or product; consistency matters more
than fashion. Define support window, deprecation signal, migration evidence, and
retirement authority before launching the first version.

## Contract governance

Use design review, linting, generated documentation, examples, security schemes,
compatibility checks, and ownership metadata in delivery. Code generation speeds
adoption but can spread a flawed contract. SDKs require versioning, telemetry,
security updates, and language-specific support.

## AWS-first translation

Amazon API Gateway can expose HTTP, REST, and WebSocket APIs; use CloudFront or
AWS WAF where edge caching and abuse controls are required. Keep business semantics
in services and contract repositories, not in gateway-specific configuration.

## Review questions

Can a consumer safely retry? Can old and new producers coexist? What does deletion
mean? Which changes break authorization or tenant isolation? How is real usage
measured before retirement?
