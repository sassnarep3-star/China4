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

### Conflict resolution — agent-b10a7fc7 (2026-11-08 UTC)
- `git pull --rebase` hit a COORDINATION.md conflict because integration PRs #6/#7 landed on main during this session's claim. Resolved by **keeping all other sessions' entries intact** and appending this session's claim section; no other session's work was discarded.

---

## Session `agent-b10a7fc7` — claim log (branch `arena/b10a7fc7-china4`)

**Branch constraint note (irregularity, logged):** Arena binds this session to the single branch
`arena/b10a7fc7-china4` and forbids creating/pushing any other branch, so the
`session-<id>/<task>` branch convention in the project brief cannot be honored here.
All work below is committed and pushed to `arena/b10a7fc7-china4` only. Non-overlap is
maintained by **file scope** instead: this session owns root-level site pages and the
`scripts/`, `official-sources.json` and `VERIFICATION.md` files. Open PRs #4
(`arena/97c2d0a5-china4`) and #5 (`arena/6eb49625-china4`) belong to other sessions and
are NOT modified, closed, or merged by this session. `git pull --rebase` is run before each push.

This session acts as the **final integration session** for its own branch: tasks 1–9 were
already marked done by `agent-1`; the new tasks below close the gaps left by that work
(cost estimates in $10,000 increments to $400,000, step-by-step playbooks, and corrected
line-by-line verification).

| # | Task | Scope (files) | Status | Owner | Sources verified | Notes |
|---|------|---------------|--------|-------|------------------|-------|
| 10 | Re-verify every existing root page line by line against official sources; correct facts | index.html, methods.html, penalties.html, taxes.html, sources.html, flagged.html | in progress | agent-b10a7fc7 | (to be recorded) | High-severity finding so far: SAFE 2022 policy Q&A says USD 50,000 is a *facilitation* amount, not an annual cap; PRC FX Regulations Art. 39/40/45 fines are <=30% (serious 30%-100%), not 30%-500%/30%-300% |
| 11 | Build $10k-$400k (40 increments) cost estimates for EVERY method, mobile-friendly tables | costs.html, scripts/build_site.py | in progress | agent-b10a7fc7 | (to be recorded) | Explicit computed-estimate model from official bank rate board + official bank tariff + statutory rates |
| 12 | Step-by-step playbooks for every method | steps.html | in progress | agent-b10a7fc7 | (to be recorded) | No user input required |
| 13 | Site UI, dashboard navigation, responsive tables | style.css, all root *.html (nav generated by build script) | in progress | agent-b10a7fc7 | n/a | |
| 14 | Verification harness (official source link per table row, internal links, HTML validity) | scripts/verify_site.py, VERIFICATION.md, official-sources.json | in progress | agent-b10a7fc7 | (to be recorded) | |
| 15 | Integration: PR to main, merge, confirm GitHub Pages deploy, record result | COORDINATION.md, .github/workflows/gh-pages.yml | unclaimed -> in progress | agent-b10a7fc7 | n/a | Must not merge a broken site |

Claim timestamp: 2026-11-08 (UTC).
