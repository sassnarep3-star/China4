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
| 2 | Research CNY→USD conversion methods (official sources: SAFE, PBOC, IRS, FinCEN, State Dept) | research/sources.md | in progress | agent-1 | pending | All claims need official-source links |
| 3 | Build conversion-penalty breakdown (taxes, fees, limits) | research/penalties.md | unclaimed | agent-1 | pending | Flag unverified values |
| 4 | Build data table of methods with pros/cons | site/data/methods.json (or .md) | unclaimed | agent-1 | pending | Every row needs official source link |
| 5 | Create GitHub Pages site (landing page + subpages, dashboard UI) | site/*.html, site/css, site/js | unclaimed | agent-1 | pending | No broken links |
| 6 | Verify all site content line by line against official sources | site/ | unclaimed | agent-1 | pending | Unverified → blank + flagged |
| 7 | Create "Flagged for Review" page with irregularities | site/flagged.html | unclaimed | agent-1 | pending | Published on site |
| 8 | Integration: merge branches, re-verify combined data, confirm site builds | main (via PR) | unclaimed | agent-1 | pending | Do not merge broken site |
| 9 | Create PR from integration branch to main, merge, confirm Pages deploys | GitHub | unclaimed | agent-1 | pending | Record PR link + merge result here |

## Rules
- Statuses: unclaimed, in progress, done, needs review
- "needs review" = published on Flagged for Review page, does not block other tasks
- Never mark verified without checking an official source; link the source
- Shared outputs (table data, index, navigation) changed only by final integration session
