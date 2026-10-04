# Observability Specification

## Business signals

- admitted and rejected journeys
- reservation attempts by outcome
- confirmed orders and purchase success rate
- unknown payment outcomes and reconciliation age
- expired holds and inventory invariant violations

## Platform signals

- CloudFront and WAF request/error/block rates
- ALB target response time and unhealthy targets
- ECS desired/running count, CPU, memory, and restarts
- DynamoDB latency, throttles, and conditional-check failures
- SQS depth, age of oldest message, receive count, and DLQ depth

## Correlation

Propagate a generated `correlation_id`; use an opaque `order_id`. Do not place
tokens, credentials, identity attributes, addresses, or payment details in
logs, metrics, or traces.

## Alert design

Every alert must identify user impact, threshold/window, severity, owner,
dashboard, runbook, and safe first action. Page on rapid SLO burn, invariant
risk, or inability to process work. Ticket slower cost and capacity trends.
