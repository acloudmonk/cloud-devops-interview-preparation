# CLI and Configuration Design

[← Language and data](language-data.md) · [Next: SDK engineering →](sdk-api-engineering.md)

A command-line interface is an API for humans and pipelines. Compatibility, exit
codes, output schema, safety, and documentation are contract decisions.

## Interface design

Use verb/noun commands, descriptive help, validated arguments, explicit target scope,
and stable exit codes. Send machine-readable results to standard output and diagnostics
to standard error. Offer JSON for automation and concise tables for humans. Include
correlation/run ID, plan summary, changed/failed counts, and partial-result location.

## Configuration precedence

Document one order such as command flag → environment → config file → safe default.
Show effective non-secret configuration and source. Reject contradictory settings.
Do not let environment discovery silently target a production account or Region.

## Destructive changes

Require explicit selection, inventory preview, plan, authorized confirmation, maximum
targets, and revalidation immediately before change. `--dry-run` must use the same
selection and decision logic, disclose what it cannot predict, and make no mutation.
Non-interactive mode requires explicit approval input, not a hanging prompt.

## Secrets and files

Prefer runtime identity and secret-manager references. Never accept secrets on a
command line where process listings/history expose them. Use restricted temporary
files, deterministic encoding, atomic replacement, and cleanup that preserves useful
failure evidence without retaining credentials.

## Compatibility

Version output schemas and deprecate flags with warnings, telemetry where appropriate,
migration instructions, deadline, and tests. Human prose is not a stable parser API.
