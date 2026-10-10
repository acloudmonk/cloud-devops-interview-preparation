# Traces and Profiles

[← Module overview](index.md) · [Scenario answer framework](../interview-playbook/scenario-answer-framework.md)

A distributed trace models the causal path of a request or transaction. Spans
represent timed operations with parent/child or link relationships. Continuous
profiles aggregate code-level resource use over time. Together they connect user
latency and errors to dependency and code behavior.

## Span design

Name spans by stable operation, not raw URL or unique value. Record service and
resource identity, span kind, start/end, status, bounded attributes, relevant
events, and links. Avoid duplicating payloads or sensitive data. Instrument
meaningful boundaries—server entry, client call, queue publish/consume, datastore,
and important internal work—without creating a span for every function.

## Context propagation

Trace context must cross HTTP/gRPC headers, queues, asynchronous jobs, scheduled
work, retries, and fan-out/fan-in boundaries. Validate accepted propagators and
strip untrusted baggage. Baggage carries application context across services but
is not automatically recorded and can create security, privacy, and size risks.

For asynchronous work, model producer and consumer causality using the semantic
conventions and span links where a strict parent is misleading. Keep message and
trace identity distinct; retries and redelivery are separate attempts.

## Sampling decisions

- **Head sampling** decides near trace start: simple and cheap, but cannot know final outcome.
- **Tail sampling** decides after observing more/all spans: keeps errors or slow
  traces intelligently, but requires state, delay, affinity, memory, and failure handling.
- **Adaptive/dynamic sampling** changes rate by service, route, tenant class,
  rarity, or load and needs safeguards against bias and cost surprises.

Always preserve the probability or sampling information needed for valid analysis.
Sampling should retain rare failures and representative normal traffic while
respecting privacy. A trace backend is not an audit system.

## Trace quality failure modes

Missing propagation creates disconnected traces; incorrect clocks produce
impossible timing; retries inflate apparent dependency time; async work may look
orphaned; inconsistent service names fragment topology; and partial export can
make the blamed service merely the last visible hop.

## Profiles

CPU, allocation, heap, lock, and wall-time profiles reveal where resources are
consumed inside code. Continuous profiling can compare versions, hosts, and time
windows and can link exemplars or profiles to traces where tooling supports it.
Control symbol access, source-path leakage, tenant isolation, sampling overhead,
and retention. Use profiles to explain resource cost, not as a substitute for
request or business context.

## Investigation flow

Start from affected journey and time, segment metrics by stable dimensions, use
an exemplar or trace search to inspect request paths, pivot to correlated logs and
changes, then use profiles when the bottleneck is inside a process. Confirm with
multiple signals before declaring cause.

Return to the [module overview](index.md) when ready to continue.
