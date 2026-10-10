# Roles, Collections, and Content Contracts

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Reusable automation is a product contract. A role or collection should reduce
consumer decisions while preserving ownership, testability, versioning, and a
safe upgrade path.

## Role contract

A mature role defines:

- purpose, supported platforms, owner, and support window;
- namespaced inputs, types, safe defaults, and validation;
- observable postconditions and meaningful handlers;
- privilege and connection assumptions;
- dependencies and collection versions;
- tags, check-mode behavior, examples, and known limitations;
- deprecation and migration policy.

Keep defaults overridable and low precedence. Put internal constants in role
variables sparingly. Avoid roles with dozens of pass-through values, unrelated
lifecycles, or hidden global-variable dependencies.

## Collections

Collections package roles, modules, plugins, playbooks, and documentation under
a namespace. Pin collection versions in a reviewed requirements file and test
the complete dependency set in the same execution environment used for runs.

Fully qualified collection names make origin explicit and reduce collisions.
Treat third-party collections as executable supply-chain dependencies: verify
source, maintainer, release, integrity, permissions, and upgrade evidence.

## Composition choices

- Use a **role** for one coherent configuration capability.
- Use a **collection** for a governed domain or shared plugin ecosystem.
- Use a **playbook** to orchestrate roles and systems for an outcome.
- Use `include_*` when runtime conditions require dynamic inclusion.
- Use `import_*` when static parsing and predictable graph visibility matter.

Avoid deep include chains that conceal execution order. Prefer small, explicit
contracts composed by a readable orchestration playbook.

## Versioning and compatibility

Pin `ansible-core`, Python, system libraries, collections, and role releases.
Use semantic intent for interfaces, but do not assume every dependency follows
semantic versioning perfectly. Test representative operating systems and target
states before promotion.

For a breaking change, publish the reason, replacement, migration steps,
compatibility window, and removal date. Measure adoption rather than retaining
every legacy path indefinitely.

## Content ownership model

Platform teams can publish supported building blocks and paved workflows.
Application teams should own service-specific data and outcome verification.
Security teams define controls and exceptions without becoming the only content
maintainer. Every shared artifact needs an accountable owner and support signal.

Return to the [module overview](index.md) when ready to continue.
