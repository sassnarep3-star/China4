# Coordination Board — China4 project

Shared task board for parallel agent sessions. Claim a task by writing your
session ID and file scope, then commit and push immediately. Never start a task
another session has claimed. Keep scopes non-overlapping. Small, frequent commits;
run `git pull --rebase` before every push. When a task is finished, record
sources, verification performed, and irregularities here and mark it done.

Session ID for this session: `agent-1` (branch `arena/c56cf052-china4`)

## Tasks

| # | Task | Scope (files) | Status | Owner | Sources verified | Notes |
|---|------|---------------|--------|-------|------------------|-------|
| 1 | Create COORDINATION.md (shared task board) | COORDINATION.md | done | agent-1 | n/a | Created at project start |
| 2 | Research CNY→USD conversion methods (official sources: SAFE, PBOC, IRS, FinCEN, State Dept) | site/sources.html, site/ pages | done | agent-1 | SAFE Detailed Rules ($50k quota), SAFE Regulations (fines), FinCEN FBAR, IRS FATCA/8938/Pub54/Form3520, US-China treaty (IRS), customs cash limits | Research complete; sources compiled |
| 3 | Build conversion-penalty breakdown | site/penalties.html | done | agent-1 | SAFE Regulations fines, FinCEN/IRS penalty figures | Built; unverified items flagged |
| 4 | Build data table of methods with pros/cons | site/methods.html | done | agent-1 | SAFE Detailed Rules, FinCEN, IRS, SAFE enforcement release | Every row has source link |
| 5 | Create GitHub Pages site (landing page + subpages, dashboard UI) | site/*.html, site/css, .github/workflows | done | agent-1 | n/a | 6 pages + CSS + workflow; HTML validated |
| 6 | Verify all site content line by line against official sources | root pages | done | agent-1 | SAFE Detailed Rules, SAFE Regulations, SAFE enforcement release, FinCEN FBAR, IRS FATCA/Pub 54/Form 3520/FAQ, IRS China treaty documents (1984), PBOC | Every table row carries an official-source link; values not confirmed from an official source left blank and flagged on flagged.html |
| 7 | Create "Flagged for Review" page with irregularities | flagged.html | done | agent-1 | n/a | Published on site: 8 unverified values + 5 irregularities with suggested manual checks |
| 8 | Integration: merge branches, re-verify combined data, confirm site builds | main (via PR) | done | agent-1 | PR #1 and PR #2 merged into main; live build commit e1491ef status "built" | All six pages + CSS return 200; no broken links |
| 9 | Create PR from integration branch to main, merge, confirm Pages deploys | GitHub | done | agent-1 | PR #1: https://github.com/sassnarep3-star/China4/pull/1 (merged); PR #2: https://github.com/sassnarep3-star/China4/pull/2 (merged); GitHub Pages live at https://sassnarep3-star.github.io/China4/ | Pages build_type legacy, source branch main path "/", html_url confirmed; flagged items do not block merge and are published on the Flagged for Review page |

## Rules
- Statuses: unclaimed, in progress, done, needs review
- "needs review" = published on Flagged for Review page, does not block other tasks
- Never mark verified without checking an official source; link the source
- Shared outputs (table data, index, navigation) changed only by final integration session

## Session agent-06824257 — full re-audit and cost-model extension (2026-11-08)

Arena fixes this session's branch to `arena/06824257-china4`; all work stays on
that branch rather than creating a `session-*` branch. The previous tasks are
recorded as done. This session independently reopens verification through the
new tasks below; no other active claim was present when inspected. Research and
implementation files below have a separate scope from the legacy site. Shared
site files and navigation are reserved for task 15 (final integration), after
the research, calculations, and checks are complete.

| # | Task | Scope (files) | Status | Owner | Sources / verification | Notes |
|---|------|---------------|--------|-------|------------------------|-------|
| 10 | Independent line-by-line audit of existing content | research/audit/* | done | agent-06824257 | 1,344 baseline lines classified; 24 issues mapped to official sources | Do not trust prior verification labels |
| 11 | Official-source legal-route and tax research | research/sources/*, research/findings.json | done | agent-06824257 | 53 registry entries; SAFE/PBOC/STA/IRS/FinCEN/eCFR/Supreme Court/operator primary pages | Cover individual, salary, property, business, cards, cash, and prohibited routes |
| 12 | Reproducible $10k–$400k cost tables, all 40 increments | research/costs.json, scripts/build_data.py | done | agent-06824257 | 28 methods x 40 amounts = 1,120 rows; BOC/Sky/ATM published components only | No invented fees, FX spreads, or tax rates; unknown total stays blank |
| 13 | Executive summary and step-by-step procedures | EXECUTIVE_SUMMARY.md, research/procedures.json | done | agent-06824257 | 28 source-matched procedures; executive summary links primary sources | Distinguish bank friction from tax; no evasion instructions |
| 14 | Automated data, link, accessibility and build checks | scripts/check_site.py, tests/*, .github/workflows/* | in progress | agent-06824257 | Pending | Validate all rows, calculations, local links and source citations |
| 15 | Final integration, accessible dashboard, PR, merge and Pages | index.html, methods.html, costs.html, procedures.html, taxes.html, penalties.html, sources.html, flagged.html, style.css, README.md, VERIFICATION.md, COORDINATION.md | unclaimed | agent-06824257 | Pending tasks 10–14 | Only integration edits shared outputs; verify before merging |

### Handoff / integration log
- 2026-11-08: Read the existing board and legacy site before claiming. Initial
  review already found unsupported fee estimates and potentially misleading
  tax/eligibility claims; they will be recorded in the audit, not copied forward.

- 2026-11-08: Tasks 10–13 completed independently. Additional primary checks closed
  the IRC 988 personal-transaction gap, Form 3520 penalty gap, Bittner FBAR unit,
  Alipay/WeChat/PayPal product scope, current-account RMB policy and Shanghai property
  tax guide. Remaining unverified items are published as flags, not guessed.
