# Runbook: Order Processing Degradation

## Trigger

Purchase success or latency SLO burn, rising SQS message age, non-empty DLQ, or
growing unknown-payment count.

## Safety

- Assign incident lead and record the deployment version.
- Do not purge a queue or replay payments without business-owner approval.
- Reduce admission before scaling stateful dependencies beyond known limits.
- Preserve evidence and never copy sensitive payloads into the incident record.

## Triage

1. Confirm customer impact and whether browsing, reservation, or payment fails.
2. Check recent deployments and configuration changes.
3. Compare admitted rate with API capacity and queue-drain rate.
4. Inspect oldest-message age, receive counts, DLQ, and worker health.
5. Separate known payment failures from unknown outcomes.
6. Check DynamoDB latency, throttling, conditional failures, and quotas.
7. Check the payment stub/provider latency, error class, and rate limits.

## Stabilize

- Tighten admission or shed non-critical features.
- Roll back a correlated application release.
- Restore worker count within a tested ceiling.
- Stop unsafe retries and move ambiguous payments to reconciliation.
- Isolate poison messages through the configured redrive policy.

## Recover and verify

Confirm new requests meet objectives, backlog age returns to normal, DLQ work is
accounted for, reservations expire correctly, payments reconcile, and no seat
or charge was duplicated. Record recovery time and follow-up owner.
