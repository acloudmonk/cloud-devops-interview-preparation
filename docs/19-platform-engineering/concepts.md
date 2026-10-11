# Platform Engineering Decision Model

[← Module overview](index.md) · [Next: Product and operating model →](product-operating-model.md)

## Start with a repeated user problem

A platform is justified when many teams repeatedly solve the same difficult,
high-risk problem and a shared capability can improve outcomes without erasing
needed autonomy. Describe the loop as **customer journey → friction → reusable
capability → interface → control → feedback → outcome**.

| Concept | Meaning | Common mistake |
| --- | --- | --- |
| Platform team | Product team serving internal engineering customers | Renamed operations queue |
| Internal developer platform | Integrated capabilities and workflows for software delivery | A single purchased tool |
| Developer portal | Discovery and interaction surface | Confusing the dashboard with the platform |
| Golden path | Supported, opinionated path for a common workload | Mandatory template for every workload |
| Control plane | Reconciliation and policy system for desired state | Privileged script collection |

## Decision questions

1. Who is the customer, and which journey is slow, unsafe, or cognitively costly?
2. Is the problem common enough to standardize and stable enough to productize?
3. Which responsibility shifts to the platform, and which remains with the team?
4. What interface and abstraction reduce effort without hiding critical semantics?
5. Which policies must prevent, detect, or explain unsafe states?
6. How will adoption, flow, quality, reliability, satisfaction, and cost improve?
7. How can consumers migrate, escape, recover, and leave the capability?

## Platform versus related practices

DevOps is a collaboration and delivery operating model; SRE manages reliability;
cloud foundations provide governed accounts, identity, networks, and controls;
platform engineering packages repeatable capabilities into an owned product. These
practices reinforce one another and should not become new organizational silos.

## Thin viable platform

Start with the smallest end-to-end capability that solves one important journey,
such as creating and safely deploying a service with ownership and telemetry. A
portal that links incomplete manual processes is not self-service. A huge foundation
that users cannot yet consume is not a viable product.

## Interview signal

Strong answers identify customers, current baseline, responsibility boundaries,
platform contract, adoption plan, failure behavior, and measurable value before
naming Backstage, Kubernetes, or a cloud service.
