# Product and Operating Model

[← Platform decision model](concepts.md) · [Next: Platform architecture →](platform-architecture.md)

## Product discovery

Interview developers, security, operations, finance, architecture, and product
leaders. Observe real journeys and measure wait time, handoffs, failure demand,
rework, cognitive load, and incident contribution. Segment personas: application,
data, ML, mobile, regulated, and legacy teams may need different paths.

Prioritize by customer pain, frequency, risk reduction, reuse, business impact,
effort, and platform readiness. A roadmap should describe outcomes such as reducing
environment lead time, not “install portal plugin.”

## Responsibility model

| Actor | Owns |
| --- | --- |
| Platform product | Discovery, roadmap, experience, contracts, adoption, value |
| Platform engineering | APIs, automation, reliability, security, lifecycle |
| Product team | Application behavior, data, SLO, on-call, business outcome |
| Enabling specialists | Coaching, patterns, policy intent, complex adoption |
| Governance functions | Risk objectives, evidence needs, exceptions, assurance |

Use “you build it, you run it” carefully: teams need appropriate capabilities,
skills, staffing, and escalation. The platform removes undifferentiated complexity;
it does not silently transfer every operational responsibility to developers.

## Funding and capacity

Treat platform work as product investment, not leftover project capacity. Fund a
stable multidisciplinary team and reserve capacity for reliability, upgrades,
security, adoption, and discovery. Showback may encourage informed consumption;
arbitrary chargeback can discourage beneficial shared controls.

## Governance and lifecycle

Publish support tiers, service ownership, decision rights, roadmap, release notes,
compatibility, deprecation, exception, and escalation processes. Product councils
provide feedback but should not become design-by-committee. Platform consumers need
a clear route for influence and a predictable contract.
