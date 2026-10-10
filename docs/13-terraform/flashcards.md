# Terraform and OpenTofu Active-Recall Flashcards

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Use each prompt without viewing the cue. Explain an ownership boundary, failure mode, and
one condition that changes the choice.

| Prompt | Answer cue |
| --- | --- |
| Five-state model | intent → configuration → recorded state → observed remote state → customer outcome |
| Plan context | code + inputs + state + provider reads + tool/provider versions + identity/target |
| Saved-plan invariant | approve and apply same artifact once; expire when context changes |
| Graph limitation | orders API operations; does not prove application readiness or business outcome |
| Resource identity | address and stable key bind desired object to state/remote identity |
| State protection | encryption + least privilege + audit + versioning + locking + tested recovery |
| Lock safety | prove writer inactive before force unlock; create a fresh plan afterward |
| Root boundary | owner/credential/account/region/environment/cadence/SLO/failure radius |
| Module contract | typed inputs, safe invariants, stable outputs, tests, version, owner, deprecation |
| Module smell | pass-through fields, many booleans, unrelated lifecycles, deep nesting, no upgrade test |
| Environment promotion | promote versioned source/dependencies; separately plan against each target |
| Provider trust | executable dependency with credentials, schema, API behavior, and supply-chain risk |
| CI identity | protected trusted runner federates to short-lived scoped role; no static cloud keys |
| Policy lifecycle | advisory → remediate paved path → enforce by risk; owner/tests/exception/failure mode |
| Secret reality | sensitive marking is presentation control; state/plan/log/artifact protection still required |
| Drift classification | emergency, external ownership, unauthorized, normalization, or brownfield mismatch |
| Brownfield adoption | inventory → matching config → import binding → no-surprise plan → staged ownership |
| Address refactor | moved/state mapping plus representative-state test and zero replacement |
| Partial apply | preserve evidence → inventory completed calls → refresh → roll forward/recover → verify |
| Upgrade safety | dedicated change, release/schema review, representative plan, canary, waves, pause criteria |
| Terraform value | broad recognition/ecosystem plus HCP Terraform/Enterprise and Stacks options |
| OpenTofu value | open governance plus compatible foundation and independently developed features |
| Compatibility boundary | exact versions/features tested; OpenTofu may read state Terraform cannot later read |
| Multi-cloud principle | share operating controls and intent; keep cloud semantics and modules explicit |
| Executive recommendation | minimum supported contract, bounded trust/state, recovery, adoption, measures, decision |

Review missed cards after one day, three days, and seven days.
