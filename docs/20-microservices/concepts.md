# Microservices Decision Model

[← Module overview](index.md) · [Next: Domain and service boundaries →](domain-boundaries.md)

## Begin with forces, not fashion

Evaluate **business change → domain boundary → team ownership → independent lifecycle
→ distributed cost → evidence**. Microservices are an organizational and operational
architecture, not simply small deployable processes.

| Option | Strong fit | Principal cost |
| --- | --- | --- |
| Modular monolith | one product/team, strong transactions, evolving domain | module discipline and shared release |
| Microservices | distinct domains/teams need independent change or scale | network, data, delivery, and operations complexity |
| Serverless functions | event-driven bounded tasks with variable demand | fragmentation, limits, observability, provider coupling |
| Macroservices | a few stable business capabilities | coarser scaling and release units |

Start with a modular monolith when boundaries and operating maturity are uncertain.
Extraction is easier from explicit modules than from a distributed monolith.

## Expected benefits

Potential benefits are independent deployability, fault isolation, domain autonomy,
targeted scaling, and technology choice. Each must be proven. If teams coordinate
every release, share tables, or fail together, the architecture pays distribution
cost without receiving independence.

## Readiness questions

1. Are business capabilities and owners distinguishable?
2. Is independent change constrained by current architecture?
3. Can teams own build, data, SLO, on-call, and lifecycle?
4. Do delivery, identity, observability, and platform capabilities scale?
5. Can contracts, consistency, partial failure, and recovery be tested?
6. Does expected value exceed added people, latency, infrastructure, and risk cost?

## Granularity test

A service should be cohesive enough to enforce meaningful invariants and autonomous
enough to evolve without coordinated internal knowledge. Line count, endpoint count,
and “one noun per service” are poor boundaries. Merge services that are chatty,
transactionally inseparable, jointly released, and owned by one team without a
clear external contract.
