# Threat Model

## Scope and assets

List ticket inventory, order state, admission tokens, identity data, payment
references, audit records, deployment identity, and operational access.

## Actors and trust boundaries

Document customers, bots, administrators, CI/CD, third parties, AWS services,
internet boundaries, account boundaries, Regions, VPCs, and data stores.

## Threats and controls

|Threat or abuse case|Asset/impact|Prevent|Detect|Respond|Remaining risk|
|---|---|---|---|---|---|
|Bot exhausts inventory|Fair access and availability|Waiting room, WAF, rate limit|Admission and WAF metrics|Tighten admission|To complete|
|Replay creates duplicate order|Money and inventory|Idempotency record, conditional write|Duplicate-key metric|Reconcile|To complete|
|Leaked deployment credential|AWS account|OIDC, short sessions, least privilege|CloudTrail alert|Revoke trust/session|To complete|
|Sensitive data enters logs|Privacy and compliance|Structured logging and redaction|Log scan|Restrict, purge, notify|To complete|
|Origin bypasses edge controls|Availability|Origin protection and security groups|Direct-origin telemetry|Block and rotate|To complete|

## Data handling

For each data class, record collection purpose, Region, encryption, access,
retention, deletion, logging prohibition, backup, and recovery behavior.

## Review evidence

Record reviewer, date, open risks, accountable owner, and next review trigger.
