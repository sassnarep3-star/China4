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

## Current session: arena/8fa669e3-china4

| Task | Scope | Status | Owner | Notes |
|---|---|---|---|---|
| Independent integration audit, corrections, and publication | root HTML pages, style.css, README.md, .github/workflows, COORDINATION.md | done | arena/8fa669e3-china4 | Audit and corrections completed; publication outcome recorded below. Session branch fixed by Arena. |

### Integration audit log — arena/8fa669e3-china4
- Corrected inherited universal $50,000 quota claim: [SAFE 2017](https://www.safe.gov.cn/en/2017/1129/1365.html) explicitly covers foreign permanent resident ID holders; [SAFE 2007](https://www.safe.gov.cn/en/2007/0105/819.html) differentiates purchase and settlement. Removed universal tax-free conversion claim: [IRS currency guidance](https://www.irs.gov/pub/fatca/int_practice_units/int_c_041.pdf) identifies section 988 FX transactions.
- Verified documented current-account income pathway against [SAFE Tianjin 2025](https://www.safe.gov.cn/tianjin/2025/0715/2834.html), reporting against [IRS FBAR](https://www.irs.gov/businesses/small-businesses-self-employed/report-of-foreign-bank-and-financial-accounts-fbar), [IRS 8938](https://www.irs.gov/businesses/corporations/fatca-information-for-individuals), and [IRS 3520 instructions](https://www.irs.gov/instructions/i3520). Checked [SAFE enforcement](https://www.safe.gov.cn/en/2018/1206/1478.html) and [PBOC notice](https://www.pbc.gov.cn/en/3688253/3689012/2025080817521950275/index.html). All rows audited for official source links and claims scoped to source; account-specific values remain unverified.
- Irregularities published on flagged.html: historical applicability, Chinese cash exit rules, costs, provider availability, unknown source/status and tax basis. Initial `git pull --rebase` before branch creation failed because the remote branch did not yet exist; initial branch push then succeeded.
- Static HTML: validated local links, stylesheets and official links in every data row; no build step. All 16 distinct official source URLs were fetched through the research tool; this verifies retrieval at review time, not future availability or geographic accessibility. Open PRs #4 and #5 are separate sessions and were not altered.
- Integration PR [#6](https://github.com/sassnarep3-star/China4/pull/6) merged on 2026-11-08 at commit `503de098355e8b7ac4378a08a59513c2f139610b`. GitHub Pages legacy build and deploy [run 42533583018](https://github.com/sassnarep3-star/China4/actions/runs/42533583018) succeeded for that merge. Live site: https://sassnarep3-star.github.io/China4/. A Node.js deprecation warning was emitted by GitHub's managed Pages build; it did not fail deployment.

## Current session

| Task | Scope (files) | Status | Owner | Started (UTC) | Notes |
|---|---|---|---|---|---|
| Final integration audit, corrections, cost schedule, and deployment verification | root HTML pages, style.css, README.md, .github/workflows, COORDINATION.md | done | agent-3aacec32 | 2026-11-08 | Prior tasks are marked done; auditing existing integration. Session branch fixed by Arena. |

- Conflict during rebase: another integration session merged overlapping changes after this claim. Preserved both board entries and the already-published site; this session will integrate only supplemental tariff research.

### Supplemental audit — agent-3aacec32
- The other integration PRs #6/#7 landed during this session. A coordination-board rebase conflict was resolved by retaining both sessions' entries; the already-published site was preserved, and only supplemental content was applied.
- Reviewed the [2025 Bank of China tariff](https://pic.bankofchina.com/bocappd/pricelist/202503/P020250331641149290400.pdf) item 210105008 and notes, [SAFE cash rules](https://www.safe.gov.cn/tianjin/2024/0430/2466.html), [Shanghai property FAQ](https://english.shanghai.gov.cn/en-FAQHome/20240204/b4426264395b4fa3adfde73778c94ad4.html), [Shanghai salary FAQ](https://english.shanghai.gov.cn/en-FAQHome/20231211/74deb6f12c5e4e1686020bd042819690.html), and [IRS currency unit](https://www.irs.gov/pub/fatca/int_practice_units/fcu_t_018_02_01_08.pdf). Historical source status and applicability remain flagged.
- Added an amount-by-amount $10,000–$400,000 schedule; total transaction costs and taxes remain blank because no current executable quotes, source history or personal tax data are verified. Added conditional route steps. The tariff formula is a historical published component, not a verified actual quote.
- Static verification: `python scripts/verify_site.py` checks local links, required official links on each table row, and all requested amounts. It does not establish that every linked page remains available or that each claim is legally current.
- Supplemental PR: https://github.com/sassnarep3-star/China4/pull/8. Static verifier passed; all six pages and CSS returned HTTP 200 from a local server. The first HTTP smoke-test attempt raced server startup and failed; retry against a running server passed. No PR checks were configured. Merged as commit `d028e12b5fbdcaca0778b0c668e5340c835838b0`; GitHub Pages build and deploy [run 42533800234](https://github.com/sassnarep3-star/China4/actions/runs/42533800234) succeeded. Live cost schedule and dashboard were fetched successfully at https://sassnarep3-star.github.io/China4/. GitHub’s managed build emitted a non-failing Node.js deprecation warning.

## Current session: arena/d9dc8047-china4 — independent supplemental verification

| Task | Scope | Status | Owner | Verification / notes |
|---|---|---|---|---|
| Check current integrated research against official source text and preserve non-overlapping integration work | COORDINATION.md only | done | arena/d9dc8047-china4 | Confirmed current main had already integrated the requested dashboard, route steps, tariff component, $10,000–$400,000 schedule, flags and deployment while this branch was based on an older commit. Re-ran `scripts/verify_site.py` against origin/main snapshot; all table rows and local links passed. Independently fetched SAFE (2016 purchase evidence; 2015 quota-splitting statement), PBOC FX Regulations Arts. 39–45, GACC passenger cash guidance and virtual-currency notice, FinCEN and IRS pages. The PBOC-hosted text specifies separate administrative ranges (Arts. 39/40/45: generally up to 30%, serious cases above 30% and below 100%; Art. 42 carrying violation up to 20%); these are not personalized costs. An earlier proposed full-page rewrite overlapped newer integration work and was stashed, not applied, to preserve current main’s BOC tariff and IRS §988 analysis. No site content was overwritten. |

### Coordination/rebase note
- `origin/main` advanced to `667b5ba` with integration PRs #6–#9 while this session was auditing a checkout at `e7e12b1`. `git pull --rebase origin main` conflicted in this shared board. Resolved by retaining all existing integration/session entries and appending this audit record. No other session’s files or work were discarded.
- The authoritative GitHub Pages site had status `built` at `https://sassnarep3-star.github.io/China4/` before this audit; the latest main history records successful deploy run `42533800234` and follow-up run `42533888250`.

## Current session: arena/5906756f-china4

| # | Task | Scope (files) | Status | Owner | Sources verified | Notes |
|---|------|---------------|--------|-------|------------------|-------|
| 10 | Claim & verify comprehensive primary-source data (BOC, CCB, HSBC CN, Wise, SkyRemit, PayPal C2, SAFE, PBOC 2026-42, Chinatax, Customs, IRS 2026, FinCEN, CBP, US banks) | `COORDINATION.md` | done | arena/5906756f-china4 | All official primary agencies & tariffs fetched 2026-11-08 | Rebased onto `origin/main` (`3854ba8`) |
| 11 | Restore & expand executive summary, all 14 conversion methods + step-by-step instructions, deep penalty breakdown, and 2026 US/PRC tax guides | `index.html`, `methods.html`, `penalties.html`, `taxes.html`, `style.css` | in progress | arena/5906756f-china4 | Verified against Nov 2026 SAFE, PBOC, BOC, Chinatax, IRS, FinCEN | Preserves prior accuracy corrections while delivering complete guides & tariffs |
| 12 | Build mobile-friendly $10,000–$400,000 USD increment cost estimator & tables (most important info first, official source link on every row, blank/flagged where unverified) | `estimates.html`, `style.css` | in progress | arena/5906756f-china4 | Python-verified Nov 2026 quotes; CCB/HSBC spreads left unverified | Covers all 40 steps ($10k to $400k) |
| 13 | Update Flagged for Review & Sources registry, validate links/HTML, commit, rebase, PR, merge to `main`, verify live GitHub Pages deployment | `flagged.html`, `sources.html`, `README.md`, `COORDINATION.md`, `scripts/verify_site.py` | in progress | arena/5906756f-china4 | Pending final merge & live curl verification | — |
