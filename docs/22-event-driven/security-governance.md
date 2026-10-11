# Security and Governance

[← Resilience and operations](resilience-operations.md) · [Next: AWS-first multi-cloud map →](cloud-mapping.md)

## Identity and least privilege

Use short-lived workload identity for producers, consumers, connectors, administrators,
and replay tools. Grant send, receive, acknowledge, seek, create destination, change
policy, inspect payload, and manage keys separately. Restrict consumer groups and
subscriptions as well as topics; network reachability is not authorization.

## Payload protection

Classify fields before publication, minimize payload, encrypt in transit and at rest,
and use field or application encryption when broker operators must not see sensitive
values. Manage key rotation, replay of old ciphertext, and consumer authorization.
Never place secrets in payloads, headers, dead-letter metadata, logs, or traces.

## Tenant isolation

Carry verified tenant context and enforce it in producer policy, destination or
partition strategy, consumer authorization, data writes, observability, replay, and
support tooling. Topic-per-tenant can strengthen some boundaries but creates scale and
fleet cost; shared topics demand rigorous application and policy isolation.

## Supply chain and connectors

Connectors and schema plugins often receive broad data and credentials. Pin and scan
artifacts, isolate execution, scope credentials, control outbound networks, audit
configuration, and stage upgrades. A compromised connector can exfiltrate entire
streams even when application services are least privileged.

## Privacy, retention, and deletion

Immutable logs complicate correction and erasure. Minimize personal data, tokenize
identifiers, use claim check with lifecycle controls, choose retention deliberately,
and document legal basis. Cryptographic erasure can help only when key boundaries and
copies are correct. Propagate deletion to projections, indexes, archives, and replays.

## Governance without central bottlenecks

Platform guardrails should automate destination templates, identity, encryption,
schema compatibility, metadata, retention limits, quotas, telemetry, and ownership.
Domain teams own meaning and consumers. Review high-risk changes such as public
routes, long retention, sensitive fields, cross-region replication, and replay into
irreversible effects.

## Threat scenarios

Test unauthorized publish, cross-tenant consume, forged event type, schema downgrade,
payload bomb, replay attack, poisoned connector, leaked DLQ, and privileged offset
rewind. Preserve tamper-evident administrative audit and require stronger controls for
bulk export, purge, re-drive, and policy changes.
