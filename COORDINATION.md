# Coordination Board — China4 project

Shared task board for parallel agent sessions. Claim a task by writing your
session ID and file scope, then commit and push immediately. Never start a task
another session has claimed. Keep scopes non-overlapping. Small, frequent commits;
run `git pull --rebase` before every push. When a task is finished, record
sources, verification performed, and irregularities here and mark it done.

## Active sessions

| Session ID | Branch (as required by Agent Mode) | Status | Started |
|---|---|---|---|
| `agent-2` | `arena/a978a0c6-china4` | working | 2026-11-08 |

> Branch-name note: the original rules asked for `session-<id>/<task>` branches.
> Agent Mode sessions cannot switch branches, so each session works on the single
> branch it was started on. `agent-1` used `arena/c56cf052-china4`; `agent-2` uses
> `arena/a978a0c6-china4`. Scopes below stay disjoint by file.

## Tasks

| # | Task | Scope (files) | Status | Owner | Notes |
|---|------|---------------|--------|-------|-------|
| 1 | Create COORDINATION.md (shared task board) | COORDINATION.md | done | agent-1 | Project start |
| 2 | Research CNY→USD conversion methods | methods.html | done (pre-existing) | agent-1 | 9 methods |
| 3 | Conversion-penalty breakdown | penalties.html | done (pre-existing) | agent-1 | Unverified items flagged |
| 4 | Dashboard / landing page | index.html | done (pre-existing) | agent-1 | |
| 5 | US tax obligations page | taxes.html | done (pre-existing) | agent-1 | |
| 6 | Sources registry | sources.html | done (pre-existing) | agent-1 | |
| 7 | Flagged for Review page | flagged.html | done (pre-existing) | agent-1 | |
| 8 | PR #1–#3 merged, Pages live | main | done | agent-1 | https://sassnarep3-star.github.io/China4/ |
| **A2-1** | **Audit all pre-existing claims line by line vs official sources; repair/annotate** | all `*.html`, `COORDINATION.md` | in progress | **agent-2** | Link-rot found: `fdi.gov.cn` SAFE mirror unreachable; several secondary sources used as if official |
| **A2-2** | **New page: cost matrix for $10,000 steps up to $400,000 per method** | `costs.html` | in progress | **agent-2** | Needs sourced inputs only; blanks + flags where no official tariff exists |
| **A2-3** | **New page: step-by-step playbooks per method** | `playbook.html` | in progress | **agent-2** | Numbered steps, per-step source |
| **A2-4** | **Executive summary rewrite (top-of-dashboard, mobile-first)** | `index.html` | in progress | **agent-2** | Most important info first |
| **A2-5** | **Add missing legal channels (emigration asset transfer, UnionPay card, QDII, family remittance, etc.)** | `methods.html` | in progress | **agent-2** | Official source required per row |
| **A2-6** | **Integration, verification pass, PR to main, Pages deploy check** | `*.html`, `main` | unclaimed | — | Blocked until A2-1..A2-5 done |

## Rules
- Statuses: unclaimed, in progress, done, needs review
- "needs review" = published on Flagged for Review page, does not block other tasks
- Never mark verified without checking an official source; link the source
- Shared outputs (table data, index, navigation) changed only by the integration session
- If a claim is >60 min old with no commits, another session may take it over and must note the handoff below

## Log

- 2026-11-07 `agent-1`: bootstrapped site, 6 pages, PRs #1–#3 merged, Pages live.
- 2026-11-08 `agent-2`: claimed A2-1…A2-5. Scope = all root `*.html` + new `costs.html`, `playbook.html`.
  Reason: user requested per-$10,000 cost tables (to $400k), step-by-step instructions, deeper
  research, and a line-by-line verification pass. No other session active; scopes do not overlap.
