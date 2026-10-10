# Inventory, Variables, and Facts

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Inventory is an execution boundary, not merely a host list. A safe design makes
target discovery, grouping, variable ownership, and the final resolved host set
explainable before a task runs.

## Static and dynamic inventory

- **Static inventory** suits small, stable, deliberately curated targets.
- **Inventory plugins** query cloud or source-of-truth APIs and suit elastic fleets.
- **Constructed groups** derive operational groups from trusted metadata.
- **Multiple sources** can be combined, but load order and duplicate identities
  must be understood.

Prefer supported inventory plugins over custom scripts. Filter at the source by
account, region, lifecycle state, and managed tag; then require an explicit host
limit for higher-risk runs. Preview the inventory graph and selected host count.

## Grouping is policy

Useful dimensions include environment, service, role, operating system, region,
patch ring, owner, and criticality. Do not overload one group hierarchy with all
dimensions. Treat tags and labels used for targeting as governed production data.

Never let an application team assign a tag that silently grants privileged
automation if the tag is also the authorization boundary.

## Variable model

Variables can originate from inventory, group and host files, roles, plays,
facts, registered results, environment lookups, controller surveys, or extra
variables. High precedence is not the same as good ownership.

Design rules:

- define one owner and intended override points for each variable;
- namespace role variables to prevent collisions;
- keep defaults safe and validate required inputs;
- use structured dictionaries for related settings;
- keep secrets out of ordinary inventory and debug output;
- inspect resolved values when behavior is surprising.

Extra variables have very high precedence. Restrict free-form overrides for
production jobs; expose validated parameters rather than arbitrary input.

## Facts and registered data

Facts describe observed target properties. Registered results describe a task
outcome during the current run. Both can become stale or unavailable. Gather only
the facts required at scale, cache them with an explicit freshness model, and do
not treat a cached fact as authorization evidence.

## Precedence troubleshooting

When a value is unexpected:

1. identify the affected host and exact variable;
2. inspect inventory sources and group membership;
3. list every definition and its load order;
4. distinguish configuration, keyword, command option, and variable precedence;
5. inspect controller survey or extra-variable injection;
6. reduce duplicate definitions instead of adding a stronger override.

## Inventory safety review

Record the inventory source, filters, credential, refresh time, resolved count,
excluded populations, and sample hosts. Alert on large count changes, empty
critical groups, duplicate host identities, or targets outside approved accounts.

Return to the [module overview](index.md) when ready to continue.
