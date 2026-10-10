# Git References and Videos

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last verified: **2026-10-10**

Prefer Git project and hosting-provider documentation for behavior and controls
that can change. Verify commands against the installed Git version.

## Git project sources

- [Git reference manual](https://git-scm.com/docs)
  — authoritative command and concept documentation.
- [Pro Git](https://git-scm.com/book/en/v2)
  — free book covering basics, collaboration, internals, and administration.
- [Git objects](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects)
  — blobs, trees, commits, and content-addressed storage.
- [Git revisions](https://git-scm.com/docs/revisions)
  — names, ancestry, ranges, and special references.
- [gitrevisions and reflog](https://git-scm.com/docs/git-reflog)
  — local reference-movement records and management.
- [git-merge](https://git-scm.com/docs/git-merge),
  [git-rebase](https://git-scm.com/docs/git-rebase), and
  [git-revert](https://git-scm.com/docs/git-revert)
  — integration and reversal semantics.
- [git-bisect](https://git-scm.com/docs/git-bisect)
  — binary search for behavior-changing commits.
- [Git protocol v2](https://git-scm.com/docs/protocol-v2)
  — transport capability negotiation and fetch protocol.

## GitHub governance and security

- [About protected branches](https://docs.github.com/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)
  — reviews, checks, signing, queue, force/deletion, and bypass controls.
- [About rulesets](https://docs.github.com/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets)
  — layered repository/organization ref governance and enforcement states.
- [About code owners](https://docs.github.com/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)
  — ownership patterns and review requests.
- [About merge methods](https://docs.github.com/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/about-merge-methods-on-github)
  — merge commit, squash, and rebase behavior.
- [About commit signature verification](https://docs.github.com/authentication/managing-commit-signature-verification/about-commit-signature-verification)
  — GPG, SSH, S/MIME, persistent verification, and vigilant mode.
- [Secret scanning](https://docs.github.com/code-security/secret-scanning/introduction/about-secret-scanning)
  — detection, push protection, validity, and response concepts.
- [Secure use reference for GitHub Actions](https://docs.github.com/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions)
  — untrusted input, tokens, third-party actions, runners, and environments.

## GitLab and Azure DevOps translation

- [GitLab protected branches](https://docs.gitlab.com/user/project/repository/branches/protected/)
  — push/merge permissions, approvals, and protection semantics.
- [GitLab merge request approvals](https://docs.gitlab.com/user/project/merge_requests/approvals/)
  — approval rules, code owners, and policy behavior.
- [Azure Repos branch policies](https://learn.microsoft.com/azure/devops/repos/git/branch-policies)
  — reviewer, build, status, comment, merge, and bypass policies.
- [Secure Azure repositories and pull requests](https://learn.microsoft.com/azure/devops/repos/git/secure-repositories-pull-requests)
  — access, review, traceability, validation, and rollout guidance.

## Workflow references

- [Trunk Based Development](https://trunkbaseddevelopment.com/)
  — patterns for small, frequent integration and release branches.
- [GitHub flow](https://docs.github.com/get-started/using-github/github-flow)
  — branch, commit, PR, review, merge, and deletion workflow.

## Video

- [So You Think You Know Git? — Scott Chacon, FOSDEM 2024](https://www.youtube.com/watch?v=aolI_Rz0ZqY)
  — advanced Git behavior and useful modern features. Verify commands against
  current Git documentation before applying them to shared history.

Official channels for newer material:

- [GitHub](https://www.youtube.com/@GitHub)
- [GitLab](https://www.youtube.com/@GitLab)
- [Microsoft Developer](https://www.youtube.com/@MicrosoftDeveloper)
- [FOSDEM](https://www.youtube.com/@fosdemtalks)

## Books

- Scott Chacon and Ben Straub, *Pro Git* (also free online)
- Julia Evans, *How Git Works*
- Emma Jane Hogbin Westby, *Git for Teams*
- Jon Loeliger and Matthew McCullough, *Version Control with Git*

Check edition and supported platform/Git versions before purchasing.

## Suggested reading order

1. Pro Git basics, branching, and Git objects
2. Revision, merge, rebase, revert, reflog, and bisect manuals
3. GitHub protection, ruleset, ownership, signing, and Actions security docs
4. GitLab/Azure policy translations and workflow references
5. Advanced video and selected book chapters
