# Rapid-Fire Revision

[← Ten-minute architecture review](presentation-template.md) · [Next: Active-recall flashcards →](flashcards.md)

Answer each aloud in one or two sentences, then add a failure mode or trade-off.

1. **What does messaging decouple?** Time, availability, endpoint, scale, and deployment to varying degrees.
2. **What coupling remains?** Semantic, contract, ordering, volume, privacy, and operational coupling.
3. **What is a command?** A request for a named capability to perform an action.
4. **What is an event?** An immutable statement that something happened.
5. **What is a notification?** A signal that may require the consumer to fetch authoritative state.
6. **What is a work queue?** A destination where one competing worker handles each task attempt.
7. **What is publish/subscribe?** Independent subscriptions receive the same published fact.
8. **What is a retained log?** An ordered partitioned history read by consumer groups at their positions.
9. **What is an event bus?** A router that matches discrete events to configured targets.
10. **When prefer a workflow?** When multi-step state, timeout, compensation, and visibility must be explicit.
11. **What is choreography?** Capabilities react to facts without one central process coordinator.
12. **What is orchestration?** A coordinator explicitly tracks and directs workflow progress.
13. **What is at-most-once delivery?** Loss may occur but deliberate redelivery does not.
14. **What is at-least-once delivery?** Accepted messages can be redelivered, so effects need idempotency.
15. **Why qualify exactly once?** It applies only within a defined transactional or deduplication boundary.
16. **What is acknowledgment?** Evidence to the broker that a delivery can be settled or position advanced.
17. **Why acknowledge after processing?** Early acknowledgment can lose uncompleted work.
18. **What does late acknowledgment risk?** A crash can cause redelivery after the effect occurred.
19. **What is idempotency?** Reapplying an operation produces no additional incorrect business effect.
20. **Event ID versus business key?** Event ID finds delivery duplicates; business key/version protects domain effects.
21. **What is an outbox?** Publication intent committed atomically with domain state.
22. **What is an inbox?** Processing evidence committed with consumer-owned state.
23. **What is a partition?** An ordered shard that bounds parallelism, storage, and consumer assignment.
24. **What is a partition key?** The value mapping related records to an ordering and state-locality scope.
25. **Is ordering normally global?** No; it is typically guaranteed only within a group or partition.
26. **What is a consumer group?** Consumers sharing work and a logical stream position.
27. **Why can extra consumers be idle?** Parallelism cannot exceed usable partitions or broker assignment units.
28. **What is a hot partition?** A shard receiving disproportionate traffic or expensive work.
29. **What is backpressure?** Controlling upstream rate or concurrency to match sustainable downstream capacity.
30. **Why is a queue not infinite capacity?** A sustained deficit eventually exceeds retention, storage, or freshness.
31. **What is queue age?** Time the oldest unprocessed message has waited.
32. **Why is depth insufficient?** It hides age, skew, poison groups, and processing duration.
33. **What is a poison message?** A record that repeatedly fails for a persistent reason.
34. **What is a DLQ?** Quarantine for failed messages requiring diagnosis and repair.
35. **Why is DLQ arrival not success?** The intended business outcome remains incomplete.
36. **What is re-drive?** Controlled delivery of quarantined records after correction.
37. **What is replay?** Reprocessing a retained historical range from an earlier position.
38. **Why is replay risky?** It can duplicate irreversible effects and overload live systems.
39. **What is event time?** Time the business fact occurred.
40. **What is processing time?** Time a processor observes or handles the event.
41. **What is a watermark?** A processor's estimate of event-time completeness for a window.
42. **What is schema compatibility?** Whether old/new producers and consumers can exchange changed records safely.
43. **What is semantic compatibility?** Whether unchanged-looking fields retain the same business meaning.
44. **What does a schema registry do?** Stores schemas and can enforce configured structural compatibility.
45. **What is CloudEvents?** A common specification for event metadata and transport bindings.
46. **What is AsyncAPI?** A specification for describing asynchronous APIs, channels, and messages.
47. **What is claim check?** Store a large payload separately and send a protected reference.
48. **What is event sourcing?** Persist domain state as an ordered event history.
49. **Is a broker log an event store?** Not automatically; domain invariants, versions, privacy, and reconstruction differ.
50. **What is a projection?** Derived read state built from an event sequence.
51. **What is correlation?** Grouping work belonging to one journey or conversation.
52. **What is causation?** Recording which command or event caused another event.
53. **How should retries behave?** Classified, bounded, exponentially backed off, jittered, and budgeted.
54. **What proves event-system health?** Commit-to-business-effect freshness and correctness, not broker uptime alone.
55. **What is a strong event architecture answer?** It defines meaning, guarantees, scale, failure, repair, security, and ownership precisely.
