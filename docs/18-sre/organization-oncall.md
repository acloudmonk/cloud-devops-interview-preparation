# On-Call and SRE Organization

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Reliable services require clear ownership and a sustainable human system. On-call
is not free capacity; fatigue, excessive interruption, unsafe escalation, and weak
authority become technical reliability risks.

## On-call design

Define owned services, hours/time zones, primary/secondary and escalation, shift
length, staffing, handover, access, training, compensation/time recovery, and
backup for illness or major incidents. A rotation must receive actionable pages
at a volume that leaves responders able to think.

Give responders safe authority, current runbooks, tested access, service context,
and engineering support. Track pages per shift, after-hours load, repeated alerts,
engagement/mitigation time, escalations, interruptions, and responder health.
Numbers require qualitative review; fewer pages can mean broken detection.

## Readiness and certification

Use shadow shifts, simulations, architecture walkthroughs, common-failure drills,
access validation, and supervised response before independent duty. Re-certify
after major architecture/process change. Service onboarding must meet readiness
standards or carry explicit risk, rather than silently transferring an unready
system to a central SRE team.

## SRE engagement models

| Model | Fit | Risk |
| --- | --- | --- |
| Embedded SRE | sustained deep partnership with a critical product | local optimization and staffing cost |
| Central service SRE | direct operation of a bounded shared/critical estate | ticket-queue absorption and lost product ownership |
| Consulting/enabling SRE | temporary assessment, coaching, and reliability projects | recommendations without adoption authority |
| Platform SRE | builds shared reliability capabilities and paved paths | platform output mistaken for service outcome |
| Product team owns reliability | strong end-to-end ownership with enablement | inconsistent maturity and duplicated tooling |

Use entry and exit criteria for engagements: business importance, SLO and owner,
architecture/readiness, staffing, engineering roadmap, improvement objective, and
what happens when prerequisites or partnership fail.

## Responsibility boundary

Product teams own user behavior, code, domain correctness, and product trade-offs.
Platform teams own shared capability and its reliability. SRE owns agreed reliability
engineering and operation, not every support ticket. Security, compliance, vendors,
and business owners retain their responsibilities. Document who accepts residual risk.

## Healthy incentives

Reward accurate incident declaration, durable engineering, risk reduction, shared
learning, and sustainable operation. Avoid targets that encourage hiding outages,
rejecting onboarding help, inflating SLOs, closing weak actions, or automating merely
to meet a toil percentage. Reliability is a shared product outcome.

Return to the [module overview](index.md) when ready to continue.
