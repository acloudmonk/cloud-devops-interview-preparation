# Security and Integrity

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

## Identity and authorization

Use centralized identity, strong authentication, short-lived credentials,
least-privilege roles, reviewable team membership, and rapid offboarding. Human,
bot, CI, deploy, and integration identities need different permissions and
lifecycle owners.

Repository read access can expose source, history, issues, actions logs,
artifacts, and metadata. Treat it as a data-access decision, not a harmless
developer convenience.

## Secret prevention and response

Prevention layers include secure secret delivery, ignore rules, editor/pre-commit
feedback, push protection, server scanning, review, and CI policy. None removes
the need for rotation.

If a secret enters Git:

1. treat it as compromised and rotate/revoke it immediately;
2. determine repositories, forks, clones, logs, caches, artifacts, and users exposed;
3. preserve incident evidence and notify security/data owners;
4. remove it from current content and rewrite history only when the exposure,
   policy, and disruption justify it;
5. coordinate rewritten refs with every consumer and prevent reintroduction;
6. fix the secret-delivery and detection control.

History rewriting reduces future discovery; it cannot make a disclosed secret
trusted again.

## Commit and tag signing

Signing verifies that a holder of an accepted key created an object. Design key
issuance, identity binding, expiration, revocation, hardware protection,
automation signing, allowed algorithms, verification enforcement, and response
to compromised keys. Protect release tags more strongly than ordinary local
development if they authorize downstream publication.

## Branch and tag immutability

Protect default, release, and deployment-significant refs from deletion,
unreviewed updates, and force pushes. Restrict who can modify policy/workflow/
ownership files. Audit bypasses and ensure administrators do not silently evade
controls.

## Untrusted code and CI

Pull-request code can modify tests, build scripts, and workflow-consumed files.
Do not expose write tokens or secrets to untrusted forks. Separate evaluation
of untrusted code from privileged publication, use ephemeral isolated runners,
and minimize network and repository permissions.

## Dependency and provenance boundary

Git integrity does not prove dependencies, actions, containers, compilers, or
artifacts are trustworthy. Pin and review automation dependencies, generate
provenance where required, protect artifact promotion, and keep source review
separate from release authorization.

## Audit and retention

Retain repository, membership, policy, merge, bypass, token, workflow, and
release events according to investigation and regulatory needs. Export critical
audit evidence if provider retention is insufficient and test restoration.
