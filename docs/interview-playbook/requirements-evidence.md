# Requirements, Constraints, and Evidence

[← Stakeholders](stakeholder-mapping.md) · [Next: Workshop facilitation →](workshop-facilitation.md)

Separate:

- **outcome:** desired measurable change;
- **requirement:** capability or quality needed for the outcome;
- **constraint:** boundary the solution must respect;
- **preference:** desirable but negotiable choice;
- **assumption:** unverified belief used temporarily;
- **invariant:** condition that must never be violated;
- **acceptance criterion:** observable proof of completion.

Turn “fast, secure, scalable, highly available, low cost” into thresholds, measurement
points, workload conditions, time windows, failure scopes, and accountable owners.

## Evidence hierarchy

Prefer observed production data and controlled tests, then system records, documented
policy/contracts, corroborated interviews, individual recollection, and unsupported
assertion. Lower-quality evidence can guide a hypothesis but should not be presented as
fact.

## Quality-attribute scenario

Write **source → stimulus → environment → artifact → response → measure**. Example:
“During a zone loss at campaign peak, order submission degrades optional recommendations
and restores full service within five minutes while duplicate charges remain zero.”

Trace each requirement to source, rationale, priority, owner, validation method, and
affected option. Resolve contradictions explicitly; a MoSCoW label does not settle
competing stakeholder incentives.
