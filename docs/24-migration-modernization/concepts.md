# Migration and Modernization Decision Model

[← Module overview](index.md) · [Next: Discovery, portfolio, and business case →](discovery-portfolio.md)

## Begin with the business change

State why the organization is moving: exit a data center, reduce risk, improve release
speed, enter a market, satisfy regulation, integrate an acquisition, or change unit
economics. Define outcome metrics, deadline, scope, constraints, owners, funding, and
the consequence of doing nothing. “Move to cloud” is a destination, not an outcome.

## Treat migration as a controlled transition

Model current state, target state, and the temporary coexistence between them. The
transition introduces duplicate paths, synchronization, identity and network changes,
support ambiguity, and rollback decisions. Architecture must cover this temporary
system—not only the final diagram.

## Make decisions at the right granularity

An application is rarely one indivisible unit. Assess user journeys, services, data,
integrations, infrastructure, licenses, operational processes, and teams. Components
may receive different dispositions, but excessive fragmentation creates coordination
cost. Record assumptions and the evidence that would change each decision.

## Use explicit decision rights

Business owners own outcomes and acceptable disruption; application owners own
behavior and validation; platform teams own destination readiness; security and risk
owners define control evidence; migration teams coordinate execution; service owners
accept operations. One accountable cutover authority makes go/no-go decisions.

## Measure end-to-end completion

Track discovery confidence, decision coverage, landing-zone readiness, wave flow,
defect escape, cutover success, performance, incidents, control evidence, cloud cost,
benefits, legacy shutdown, contract exit, and team capability. Server counts migrated
can hide business failure and stranded cost.

## Migration decision record

Capture outcome, workload boundary, dependencies, disposition, target, assumptions,
data path, coexistence, security, tests, RTO/RPO, cutover, rollback threshold, support,
cost, benefits, decommissioning, owner, approvals, risks, and re-evaluation triggers.
