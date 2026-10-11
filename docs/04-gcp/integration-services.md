# APIs, Messaging, Events, and Workflows

[← Data platforms](data-platforms.md) · [Next: Service selection →](service-selection.md)

| Need | Candidate | Questions |
| --- | --- | --- |
| API management | Apigee, API Gateway | lifecycle, policy, analytics, hybrid need |
| Event distribution | Pub/Sub | delivery, ordering, duplication, retention, replay |
| Event routing | Eventarc | source, filter, destination |
| Deferred work | Cloud Tasks | schedule, rate, retry, target |
| Orchestration | Workflows | state, compensation, duration |
| Time trigger | Cloud Scheduler | duplicate execution and idempotency |

Define ownership, schema compatibility, ordering key, delivery guarantee, idempotency,
retry/backoff, dead letters, retention, replay, poison messages, backpressure, and
observability. Pub/Sub is at-least-once by default; evaluate any exactly-once feature
against its current scope and limits.

Bound retries with jitter, preserve correlation, quarantine poison messages, and alert
on oldest unprocessed age and business completion. Replays must be authorized,
rate-limited, observable, and safe for side effects. For money or inventory, combine
an authoritative transition with outbox, deduplication, reconciliation, or compensation.
