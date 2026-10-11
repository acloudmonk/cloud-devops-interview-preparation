# Active-Recall Flashcards

[← Rapid-fire revision](rapid-fire.md) · [Next: References and videos →](references.md)

Cover the answer column and recall both the definition and design consequence.

| # | Prompt | Recall answer |
| ---: | --- | --- |
| 1 | Command | Request to a named capability; acceptance or rejection is meaningful. |
| 2 | Integration event | Stable external fact owned by the producing domain. |
| 3 | Queue | Load-levelled work with competing consumers. |
| 4 | Pub/sub | Independent subscriptions receive a published fact. |
| 5 | Retained log | Partitioned ordered history supporting independent positions and replay. |
| 6 | Workflow | Explicit state, timeout, compensation, and operator visibility. |
| 7 | At-least-once | Redelivery is possible; design idempotent effects. |
| 8 | Exactly-once boundary | Name the transactional reads/writes covered; external effects remain separate. |
| 9 | Acknowledgment timing | After effect avoids loss but permits duplicate after crash. |
| 10 | Idempotency key | Stable business identity used to prevent repeated effects. |
| 11 | Outbox | Domain change and publish intent share one local transaction. |
| 12 | Inbox | Consumer evidence and local effect share one transaction. |
| 13 | Partition key | Defines entity order, locality, distribution, and parallelism. |
| 14 | Consumer group | Logical consumers share partitions/work and position. |
| 15 | Hot partition | Skewed traffic or work limits total throughput despite spare capacity. |
| 16 | Backpressure | Bound input or concurrency to sustainable downstream rate. |
| 17 | Oldest-message age | Stronger freshness signal than depth alone. |
| 18 | DLQ | Quarantine requiring owned diagnosis, repair, re-drive, and verification. |
| 19 | Replay | Controlled historical reprocessing with isolated side-effect and capacity plan. |
| 20 | Event time | When the fact occurred, used for business-time windows. |
| 21 | Watermark | Estimate of completeness used to handle late event-time data. |
| 22 | Structural compatibility | Schema readers/writers can exchange old and new shapes. |
| 23 | Semantic compatibility | Business meaning remains safe for existing consumers. |
| 24 | CloudEvents | Standard event metadata; it does not define domain semantics. |
| 25 | AsyncAPI | Description format for asynchronous channels, operations, and messages. |
| 26 | Claim check | Protected reference replaces a large or sensitive broker payload. |
| 27 | Projection | Derived state rebuilt from source events and checkpoints. |
| 28 | Event sourcing | Domain state is an event history, requiring invariant and evolution discipline. |
| 29 | Reconciliation | Compare authorities and effects, then repair drift with evidence. |
| 30 | Freshness SLO | Time from authoritative commit to required consumer-visible effect. |
