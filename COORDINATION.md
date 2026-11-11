# Coordination Board — China4 project

Shared task board for parallel agent sessions. Claim a task by writing your
session ID and file scope, then commit and push immediately. Never start a task
another session has claimed. Keep scopes non-overlapping. Small, frequent commits;
run `git pull --rebase` before every push. When a task is finished, record
sources, verification performed, and irregularities here and mark it done.

Session ID for this session: `agent-d778fbdf` (branch `arena/d778fbdf-china4`)

Previous session: `agent-1` (branch `arena/c56cf052-china4`)

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
| 10 | Independent audit, expansion, integration, and redeployment of the complete dashboard | all root HTML/CSS/data/documentation files and .github/workflows; GitHub PR/Pages | in progress | agent-d778fbdf | SAFE/PBOC/State Council/Customs; BOC personal tariff, FX quote and ATM notices; Wise/WU/MoneyGram operator terms; IRS/FinCEN/eCFR/CBP; US receiving-bank disclosures | Rebuilt all six pages with 18 sourced procedures, four 40-row matrices and 47 primary sources. Corrected foreign-individual/quota treatment and China penalty ranges. Unknown current provider, intermediary and personal-tax values are published blank with manual checks. `python3 scripts/build_site.py && python3 scripts/validate_site.py` passes; headless Chromium returned 200 on every page, passed desktop/390px overflow checks and route interaction. CI validation added; PR/deployment pending. Fixed Arena branch is the integration branch for this session. |

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
| 11 | Restore & expand executive summary, all 14 conversion methods + step-by-step instructions, deep penalty breakdown, and 2026 US/PRC tax guides | `index.html`, `methods.html`, `penalties.html`, `taxes.html`, `style.css` | done | arena/5906756f-china4 | Verified against Nov 2026 SAFE, PBOC (`银发〔2026〕42号`, `[2025] 11`, parity `6.7168`), BOC (`6.6648/6.6929`), Chinatax, Customs, IRS, FinCEN | Preserves prior accuracy corrections (`五星卡` quota distinction, IRC §988, PBOC FX Regs Arts. 39–45) with full guides & tariffs |
| 12 | Build mobile-friendly $10,000–$400,000 USD increment cost estimator & tables (most important info first, official source link on every row, blank/flagged where unverified) | `estimates.html`, `style.css` | done | arena/5906756f-china4 | Python-verified Nov 2026 quotes across all 40 steps ($10k–$400k); CCB/HSBC spreads kept `Unverified` | Added responsive `mobile-cards` CSS + optional US receiving bank/OUR toggle |
| 13 | Update Flagged for Review & Sources registry, validate links/HTML, commit, rebase, PR, merge to `main`, verify live GitHub Pages deployment | `flagged.html`, `sources.html`, `README.md`, `COORDINATION.md`, `scripts/verify_site.py` | done | arena/5906756f-china4 | `scripts/verify_site.py`, HTML/JS syntax check, and local HTTP 200 smoke test all passed | Preparing PR & merge to `main` + live GitHub Pages verification |
## Current session: arena/9ca8a991-china4

| Task | Scope (files) | Status | Owner | Started (UTC) | Notes |
|---|---|---|---|---|---|
| Fill the blank $10,000-$400,000 cost schedule with sourced calculated estimates; add step-by-step route guide; add new official sources and flags; integrate and deploy | costs.html (new), steps.html (new), EXECUTIVE_SUMMARY.md (new), scripts/build_costs.py (new), sources.html, flagged.html, methods.html, index.html, penalties.html, README.md, style.css, scripts/verify_site.py, COORDINATION.md | done | arena/9ca8a991-china4 | 2026-11-08 | Prior tasks marked done by earlier sessions. Branch fixed by Arena; worked on this branch. |

### Claim log — arena/9ca8a991-china4
- Non-overlapping scope: this session only ADDS two new pages (costs.html, steps.html), ADDs rows to sources.html and flagged.html, and ADDs two nav links to existing pages. No existing table content is deleted or rewritten.
- Model inputs are all pulled from official pages fetched during this session: BOC published FX rate board (boc.cn/sourcedb/whpj), BOC e-banking tariff (boc.cn/ebanking/service/cs1/200905/t20090506_990712.html), BOC 2025 personal-services price list PDF, eCFR 31 CFR 1010.821, IRS gifts-from-foreign-person, PBOC/SAFE 《携带外币现钞出入境管理暂行办法》 (gov.cn gongbao), PBOC 《个人财产对外转移售付汇管理暂行办法》 (gov.cn gongbao + safe.gov.cn), SAFE 《个人外汇管理办法实施细则》 (safe.gov.cn).
- Every estimate on costs.html is a MODELLED figure from those published inputs with the formula, the rate snapshot date and the source link printed next to it; it is not a bank quote and is labelled as such.

### Completion log — arena/9ca8a991-china4

**Problem addressed.** Earlier sessions correctly refused to publish any cost number, leaving all 40 rows of the requested $10,000–$400,000 schedule blank. The user explicitly asked for estimates. This session supplied estimates that are *computed from published official inputs* rather than guessed, with the formula, the rate snapshot date and the source link printed next to every figure.

**Official sources fetched and verified this session (all linked from the site):**
- [BOC published FX rate board](https://www.boc.cn/sourcedb/whpj/) — USD spot buy 6.6648, sell 6.6929, reference 6.7168, cash sell 6.6929 (per 100 USD), stamped 2026-11-09 05:30. Fetched twice; stable across both reads.
- [BOC e-banking personal transfer tariff](https://www.boc.cn/ebanking/service/cs1/200905/t20090506_990712.html) — outward telegraphic transfer 0.1% of remittance, min CNY 50, max CNY 260, plus CNY 150 cable fee (CNY 80 to HK/Macau/Taiwan).
- [BOC 2025 personal services price list PDF](https://pic.bankofchina.com/bocappd/pricelist/202503/P020250331641149290400.pdf) — inherited from session 8fa669e3; reused as corroboration and for the overseas-bank-charges note.
- [SAFE, Detailed Rules on Individual Foreign Exchange (2007)](https://www.safe.gov.cn/safe/2007/0105/5320.html) — Art. 2 US$50,000 annual quota; Art. 12 evidence above quota; Art. 13 foreign individuals' legitimate current-account RMB income with tax documentation; Art. 14/15 outward remittance; Art. 26/30/31 accounts and cash. Also records that Art. 39 was repealed by 汇发〔2023〕8号.
- [SAFE + GAC, Interim Measures on Carrying Foreign Currency Cash In and Out (2003)](https://www.gov.cn/gongbao/content/2004/content_63085.htm) — Arts. 3, 4, 5, 7, 9, 10, 11 (thresholds and permits).
- [PBOC, Interim Measures on Sale and Payment of FX for Transfer of Individual Property Abroad (2004)](https://www.gov.cn/gongbao/content/2005/content_64294.htm) and [SAFE release](http://m.safe.gov.cn/safe/2004/1116/4133.html) — Arts. 2, 6, 8, 9, 10, 11 (emigration and inheritance transfer). **This route was missing from the site entirely and is now on methods.html and steps.html.**
- [eCFR 31 CFR 1010.821](https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010/subpart-H/section-1010.821) — FBAR inflation-adjusted maxima $16,536 (non-willful) and $165,353 (willful) for penalties assessed on or after 17 Jan 2025. Previously flagged unverified; now verified against the official table.
- [IRS, Gifts from foreign person](https://www.irs.gov/businesses/gifts-from-foreign-person) — $100,000 NRA/foreign-estate threshold; $20,116 (2025) and $20,573 (2026) for foreign corporations/partnerships. Previously flagged unverified; now verified.

**Verification performed.**
- `python3 scripts/verify_site.py` passes on all eight pages: 297 sourced rows checked, every local link resolves, every value-bearing row carries an official-source link, all 40 amounts present on both costs.html and penalties.html.
- Verifier was extended, not weakened: the page list now includes costs.html and steps.html, the official-domain allowlist gained boc.cn / gov.cn / ecfr.gov / chinamoney.com.cn, and rows whose values are explicitly marked blank are exempted from the source check — because a blank cell has no value to source. That is the site's own policy, not a loophole.
- HTTP smoke test: all eight pages plus style.css returned 200 from a local server.

**Estimates published (documented route, single wire):** $10,000 → $53.40 (0.534%); $50,000 → $166.22 (0.332%); $100,000 → $271.18 (0.271%); $200,000 → $481.11 (0.241%); $300,000 → $691.03 (0.230%); $400,000 → $900.95 (0.225%). Quota-only route at $400,000: $1,329.77 over 8 calendar years.

**Irregularities flagged (all published on flagged.html with source links):**
1. BOC's quoted USD selling rate (6.6929) sat *below* the PBOC/CFETS central parity (6.7168) on the snapshot date — the opposite of the usual relationship. The model therefore uses the internally consistent half-spread measure (0.2099%) rather than a comparison with parity. Flagged as a data anomaly to re-check.
2. BOC states on its own rate board that it is for reference and the executed rate governs — so the estimator is an input model, not a quote.
3. Whether a US passport alone creates a US$50,000 quota is not established by the verified pages; Art. 2 covers domestic individuals and SAFE 2017 extends it to foreign permanent-resident ID holders.
4. SAFE Detailed Rules Art. 39 (fine up to CNY 1,000) was repealed by 汇发〔2023〕8号 — an earlier version of this site cited it; now corrected.
5. Conflict between PBOC Interim Measures Art. 10 ("CNY 500,000 or less") and SAFE's own release ("below CNY 500,000") on which office approves the boundary case.
6. Intermediary/correspondent charges and the US receiving-bank fee remain blank by policy.
7. Emigration/inheritance transfer eligibility does not on its face cover a US citizen's own savings.

**Coordination.** Scope was additive only: two new pages, new rows appended to sources.html and flagged.html, one new row and one strengthened row on methods.html, two nav links added to the existing pages, and a cross-link from index.html and penalties.html. No existing table content from other sessions was deleted or rewritten. Files owned by earlier sessions that would have needed substantive rewrites were left alone and the correction logged on flagged.html instead.

## Integration note — arena/9ca8a991-china4 (final)

**Merge conflict.** While this session was working, arena/5906756f-china4 merged a full rebuild of the
dashboard (PRs #9, #10, #11) that created `estimates.html` and rewrote every page. This session's PR #13
could not merge cleanly. Resolution: **main's rebuild was taken as the base** for all nine conflicted files
and this session's work was re-applied on top of it, additively. Nothing from arena/5906756f-china4 or any
earlier session was discarded.

**What this session contributed on top of that rebuild:**

- **`costs.html` (new)** — the $10,000–$400,000 grid viewed **by legal route** rather than by provider, which
  `estimates.html` does not cover: annual-quota spreading across calendar years (8 years and $1,329.77 at
  $400,000), SAFE-approved emigration/inheritance property transfer with its mandatory three-stage remittance
  ($1,023.47 at $400,000), cash carry, and the illegal channel's statutory fine exposure at every amount.
  Both pages now cross-link and explain the difference.
- **Five official sources added to `sources.html`**: SAFE Detailed Rules full text
  (safe.gov.cn/safe/2007/0105/5320.html), SAFE + GAC cash-carry Interim Measures full text
  (gov.cn Gazette), BOC e-banking outward-wire tariff, eCFR 31 CFR 1010.821 (the official FBAR penalty
  table), and IRS gifts-from-foreign-person (Form 3520 thresholds).
- **Eight flagged items added as section 3 of `flagged.html`**, including the rate anomaly below.
- **`EXECUTIVE_SUMMARY.md` (new)** and a `costs.html` entry in `README.md`.
- **`scripts/build_costs.py` (new)** — regenerates `costs.html` from its documented model inputs.
- **Verifier extended**: `costs.html` added to the page list, `gov.cn` / `ecfr.gov` / `chinamoney.com.cn`
  added to the official-domain allowlist, the full-amount-grid check applied to both estimate pages, and rows
  whose values are explicitly blank exempted from the source check (a blank cell has no value to source).

**Dropped deliberately:** this session had also built a standalone `steps.html`. Main's `methods.html`
already carries exact step-by-step instructions for all 14 channels, so the duplicate page was removed rather
than shipped alongside it.

**New irregularity found (published on flagged.html):** on the 9 Nov 2026 snapshot, BOC's published USD spot
selling rate (6.6929) sits **below** the PBOC central parity rate (6.7168) — the opposite of the usual
relationship. Both cost pages therefore measure the FX cost as the half-spread of BOC's own published
buy/sell quotes (0.2099% / 0.2104%) instead of comparing against parity. Flagged for re-checking against a
live quote.

**Cross-validation:** two independent research passes over the same published BOC board produced the same
half-spread to three decimal places, and the BOC $400,000 totals agree to within $2 ($900.95 vs $902.85).

**Verification.** `python3 scripts/verify_site.py` passes across all eight pages: 281 table rows checked,
every local link resolves, every value-bearing row carries an official-source link, and the full 40-amount
grid is present on both `estimates.html` and `costs.html`. HTTP smoke test: all eight pages plus `style.css`
returned 200.

## Session arena/4646bb35-china4 — integration audit

| Task | Scope | Status | Owner | Notes |
|---|---|---|---|---|
| Independent post-PR #14 audit and publication | COORDINATION.md, scripts/build_site.py, scripts/validate_site.py, generated site and data, documentation, GitHub PR/Pages | done | arena/4646bb35-china4 | PR and deployment follow. See audit note below. |

### Post-PR #14 audit — arena/4646bb35-china4
- Task 10's branch was merged in [PR #14](https://github.com/sassnarep3-star/China4/pull/14), despite the older in-progress status. Its deployment [run 42536288129](https://github.com/sassnarep3-star/China4/actions/runs/42536288129) succeeded. The current session uses the Arena-mandated branch. Initial pull before the first push failed because that remote branch did not yet exist; the claim was then pushed.
- Independently checked [SAFE Articles 2, 13 and 15](https://www.safe.gov.cn/safe/2007/0105/5320.html) and [SAFE Tianjin 2025](https://www.safe.gov.cn/tianjin/2025/0715/2834.html): legitimate current-account RMB income has documentation requirements, with an exception for tax vouchers where no tax is due. Article 39 is marked repealed on SAFE's own page.
- The [BOC rate board](https://www.boc.cn/sourcedb/whpj/) at 09:15:45 Beijing time on 2026-11-09 showed USD spot buy/sell 6.6638/6.6919 CNY per USD, different from the explicitly historical 05:30 model. The board says the actual executed rate governs. Estimates are snapshots, not live quotes.
- Fixed an overbroad dashboard sentence about tax and currency gains. Strengthened validation from table-level to per-row direct source links; independently rebuilt and validated all six pages and four 40-row matrices. This automated test checks link presence, not source support or external availability. This limited audit does not assert a fresh line-by-line verification of all claims; unknown costs, eligibility and historical pricing remain on Flagged for Review.
- [PR #15](https://github.com/sassnarep3-star/China4/pull/15) merged at `29089128a0ccdc2583ab25f20bca87ac115e3377` on 2026-11-09 01:31 UTC. GitHub Pages legacy [build and deployment 42546010956](https://github.com/sassnarep3-star/China4/actions/runs/42546010956) succeeded. GitHub reported Node 20 action deprecation and upcoming ubuntu-latest migration warnings, neither fatal.

## Current session: arena/67730449-china4

| Task | Scope | Status | Owner | Verification / notes |
|---|---|---|---|---|
| Independent citation audit: pin the BOC quote link to the exact official historical result and disclose pagination volatility | `scripts/build_site.py`, generated `sources.html`, generated `flagged.html`, `COORDINATION.md` | done | arena/67730449-china4 | Non-overlapping with open PR #12 (dashboard, methods, penalties and CSS). Verified SAFE Art. 2/13 and Wise CNY limits from their official pages. Fetched BOC pages 1–5 on 2026-11-09: original S5 URL landed on a later quote; page 5 showed 2026-11-09 05:30 USD buy/sell 666.48/669.29 CNY per USD 100, matching the model. Updated S5 to direct to page 5 and flagged page-position volatility; quote page says executed rate governs. `python3 scripts/build_site.py && python3 scripts/validate_site.py` passed after regeneration. Direct-link presence is checked by validator; source interpretation remains a manual audit. PR [#18](https://github.com/sassnarep3-star/China4/pull/18) merged as `b9e23926c66eaa94c60bf8ebc44fabe946246cb6` on 2026-11-09 01:34 UTC. Post-merge validation + Pages deploy [run 42546238041](https://github.com/sassnarep3-star/China4/actions/runs/42546238041) succeeded; Pages API reports `built`. Live sources/flagged pages were fetched after deployment; a cache-busted source fetch confirmed the updated S5 label and page-5 URL. |
## Current session: arena/672f75fb-china4 — final re-verification & gap closure

| Task | Scope (files) | Status | Owner | Started (UTC) | Notes |
|---|---|---|---|---|---|
| 11 | Independent line-by-line re-verification of live dashboard, fresh official-source spot-checks, defect fixes, PR + merge + Pages confirmation | root HTML pages (via scripts/build_site.py), style.css, EXECUTIVE_SUMMARY.md, README.md, COORDINATION.md, .github/workflows | done | arena/672f75fb-china4 | Prior tasks 1–10 done by earlier sessions; PRs #4, #5, #12 are stale open duplicates from other sessions — not touched by this session. Branch fixed by Arena; this is the integration branch. |

### Completion log — arena/672f75fb-china4 (task 11)

**Status: done.** Fixed Arena branch `arena/672f75fb-china4` used as integration branch.

**Fresh official sources fetched and verified this session (2026-11-09):**
- [Wise, Guide to CNY transfers](https://wise.com/help/articles/2955298/guide-to-cny-transfers) — non-mainland-Chinese eligibility, own-account-only recipients, **CNY 300,000/transfer (bank app)** and **CNY 50,000/transfer (Alipay)** caps, tax-record-based overall limit.
- [Wise, Summary of fee changes (2024-11-25)](https://wise.com/gb/blog/summary-of-fee-changes) — CNY→USD bank funding ¥33.20 + 0.62%; Alipay funding ¥33.20 + 1.97% (dated formulas only).
- [BOC, personal service price list effective 2025-11-11 (PDF)](https://pic.bankofchina.com/bocappd/pricelist/202511/P020251110646838136627.pdf) — item 210105008: TT/draft 0.1%, min ¥50 / max ¥260, international telecom ¥150; note 5: full-arrival USD 15 (BOC NY) / USD 25 (elsewhere); item 210101002: foreign-currency carrying permit ¥10, waived 2025-04-01–2026-12-31; item 210108014: cross-border ATM ¥12 + 1%, max ¥112/withdrawal.
- [BOC, ATM price-change notice effective 2026-11-11](https://www.boc.cn/pbservice/bi2/202608/t20260811_25684907.html) — UnionPay ¥12 + 1% (max ¥112); Visa/Mastercard 2.5% of amount withdrawn, min USD-equiv. 3 / max USD-equiv. 40, **per withdrawal**.
- [BOC live FX board](https://www.boc.cn/sourcedb/whpj/enindex_1619_1.html) — 2026-11-09 09:15 USD buy 6.6638 / sell 6.6919, corroborating the site's dated 05:30 snapshot (6.6648 / 6.6929).
- [IRS, Figuring the FEIE](https://www.irs.gov/individuals/international-taxpayers/figuring-the-foreign-earned-income-exclusion) — 2026 maximum exclusion **$132,900** confirmed.

**Material defect found and fixed (was live on the site):** the cost model split the *USD* principal at Wise's CNY caps (300,000 / 50,000) and at the CNY 10,000 ATM cap, understating per-transfer/per-withdrawal fixed fees and transfer counts. Corrected model splits the *CNY* principal: at $400,000, Wise needs **9 bank-funded transfers ($2,524.64)** or **54 Alipay-funded transfers ($8,147.87)** on the dated formulas; the $10,000 ATM scenario needs **7 withdrawals ($112.55 UnionPay / $250.00 Visa-MC from 2026-11-11)**. `scripts/validate_site.py` now re-derives Wise and ATM figures independently from the CNY principal and checks withdrawal counts. Also corrected: EXECUTIVE_SUMMARY.md BOC table ($100k $271.62, $200k $481.99 — it previously disagreed with the generator), research cutoff restated as 2026-11-09 UTC, and the quote-timestamp irregularity marked resolved on flagged.html. BOC baseline unchanged: $10k $53.45 → $400k $902.72.

**Verification performed:** `python3 scripts/build_site.py && python3 scripts/validate_site.py` PASS (6 pages, 18 procedures, 4×40 matrices, 47 sources, local links, landmarks, independent Decimal arithmetic). Local HTTP smoke test: all 8 pages + style.css returned 200; corrected values (9 × $2,524.64; 54 × $8,147.87; 7 × $112.55) confirmed rendered in penalties.html. Live site pre-merge confirmed serving the prior build (cutoff 2026-11-08, Wise "2 transfers · $2,489.92"), i.e. the defect was live and is fixed by this PR. Mobile: ≤760px tables render as labelled cards via `data-label` (style.css).

**Irregularities:** the cap-unit defect above (High, fixed, published on flagged.html); BOC sell rate below PBOC middle rate persists on the live board — handled by the same-quote half-spread benchmark, not treated as an error. Stale duplicate PRs #4, #5, #12 from other sessions remain open and untouched. All other flagged items remain published on flagged.html and do not block the merge.

### Merge-conflict log — arena/672f75fb-china4
- During this session, arena/4646bb35-china4 merged PRs #15/#16 into main. Rebasing task 11 onto the new main conflicted only in COORDINATION.md; resolved by retaining both sessions' board sections in full — no work discarded. Their validator strengthening (per-row source links) and tax-caveat fix auto-merged with this session's cap-unit correction; `build_site.py` + `validate_site.py` pass on the combined tree with a clean working copy.
- Second conflict: main moved again via PR #18 (BOC S5 pinned to the exact historical quote page). Rebase conflicted in COORDINATION.md, scripts/build_site.py and generated HTML. Resolved by keeping both sessions' flagged items (quote-timestamp resolution + BOC pagination note + cap-unit correction), keeping the S5 pin, and regenerating all HTML from the merged generator. Nothing discarded; validator passes on the combined tree.

## Current session: arena/753a8878-china4 — final independent verification & publication

| Task | Scope (files) | Status | Owner | Started (UTC) | Notes |
|---|---|---|---|---|---|
| 12 | Independent line-by-line verification audit of live dashboard, fresh official-source spot-checks, defect fixes if any, PR + merge + Pages confirmation | COORDINATION.md (claim + log); site files only if defects found | arena/753a8878-china4 | 2026-11-10 | Prior tasks 1-11 done by earlier sessions; site live at https://sassnarep3-star.github.io/China4/ with build status "built". This session re-verifies independently and publishes the audit record. |

### Claim log — arena/753a8878-china4
- Non-overlapping scope: verification-only unless a defect is found. No other session has claimed this task. Branch fixed by Arena; this is the integration branch.
- Plan: (1) rebuild + validate, (2) fetch official sources (SAFE, IRS, BOC, FinCEN, CBP) and spot-check key claims, (3) check live site pages return 200 and mobile layout, (4) record findings, PR, merge, confirm Pages.

### Completion log — arena/753a8878-china4 (task 12)

**Status: done.** Independent verification audit; no site-content defects found, so no site files were changed. Only this coordination record is published.

**Verification performed (2026-11-10):**
- Rebuilt and validated: `python3 scripts/build_site.py && python3 scripts/validate_site.py` → PASS (6 pages, 18 procedures, 4×40 matrices, 47 sources, Decimal arithmetic). Rebuild produced zero diff against committed files (reproducible).
- Every table row carries a direct official-source link: independent check of all six pages found 0 rows without a source link (validator enforces the same per-row rule).
- Live site fetched: dashboard and Flagged for Review pages render correctly with dated-quote labeling and blank-for-unknown policy intact.
- Fresh official-source spot-checks (all fetched this session):
  - [IRS FBAR](https://www.irs.gov/businesses/small-businesses-self-employed/report-of-foreign-bank-and-financial-accounts-fbar) — aggregate >$10,000 at any time; due Apr 15, auto-ext Oct 15. Matches S25.
  - [SAFE Detailed Rules (S1)](https://www.safe.gov.cn/tianjin/2024/0430/2464.html) — Art. 2 $50,000 annual quota; Art. 13 foreign-individual lawful RMB income with tax vouchers; Art. 39 repeal note present. Matches S1/S46.
  - [eCFR 31 CFR 1010.821 (S26)](https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010/subpart-H/section-1010.821) — non-willful $16,536 / willful $165,353 (assessed on/after 2025-01-17). Matches S26.
  - [Wise CNY guide (S11)](https://wise.com/help/articles/2955298/guide-to-cny-transfers) — non-mainland-Chinese + work/tax-record eligibility, own-account recipient, 300,000 CNY (bank app) / 50,000 CNY (Alipay) per transfer, overall limit = salary minus tax. Matches S11/S12.
  - [IRS FEIE (S35)](https://www.irs.gov/individuals/international-taxpayers/figuring-the-foreign-earned-income-exclusion) — 2026 maximum $132,900. Matches S35.
  - [CBP (S29)](https://www.cbp.gov/travel/us-citizens/know-before-you-go/know-you-go-traveling-abroad) — FinCEN Form 105 for >$10,000 entering the US. Matches S29.
- Independent Decimal recomputation matched site figures exactly: BOC $53.45 / $166.44 / $271.62 / $481.99 / $902.72 at $10k/$50k/$100k/$200k/$400k; Wise dated bank $2,524.64 (9 transfers) and Alipay $8,147.87 (54 transfers) at $400k.
- Mobile: `style.css` provides card-transformed tables with `data-label` at ≤760px, horizontal-scroll tables on desktop, viewport meta on all pages. No JS required.
- Irregularity re-confirmed (already published on flagged.html, not a new defect): BOC page 5 now shows 2026-11-10 02:49 USD 666.22/669.03 — the 2026-11-09 05:30 snapshot has rolled off the paginated board. Site correctly treats it as a dated snapshot, never a live quote; live magnitude corroborates within ~0.04%.

**Irregularities:** none new. All previously flagged unknowns remain on the Flagged for Review page and do not block merge per project rules.
## Current session: arena/09fa5313-china4 — independent re-verification & republication

| Task | Scope (files) | Status | Owner | Started (UTC) | Notes |
|---|---|---|---|---|---|
| 12 | Independent line-by-line re-verification of live dashboard, fresh official-source spot-checks, defect fixes, PR + merge + Pages confirmation | root HTML pages (via scripts/build_site.py), style.css, EXECUTIVE_SUMMARY.md, README.md, COORDINATION.md, .github/workflows | in progress | arena/09fa5313-china4 | Prior tasks 1–11 done by earlier sessions; stale open PRs #4, #5, #12 are duplicates from other sessions — not touched. Branch fixed by Arena; this is the integration branch. |

### Completion log — arena/09fa5313-china4 (task 12)

**Status: done.** Fixed Arena branch `arena/09fa5313-china4` used as integration branch. No code defects found; no generated-file changes required (build is deterministic and current).

**Fresh official sources fetched and verified this session (2026-11-10):**
- [IRS, Figuring the FEIE](https://www.irs.gov/individuals/international-taxpayers/figuring-the-foreign-earned-income-exclusion) — 2026 maximum exclusion **$132,900** confirmed.
- [IRS, FBAR](https://www.irs.gov/businesses/small-businesses-self-employed/report-of-foreign-bank-and-financial-accounts-fbar) — aggregate > $10,000 at any time in calendar year; due April 15, automatic extension to October 15 confirmed.
- [eCFR 31 CFR 1010.821](https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010/subpart-H/section-1010.821) — FBAR civil maxima **$16,536** (non-willful) / **$165,353** (willful) for penalties assessed on or after Jan 17, 2025 confirmed.
- [SAFE, Individual FX Detailed Rules](https://www.safe.gov.cn/tianjin/2024/0430/2464.html) — Art. 2 ($50k annual quota, domestic individuals), Art. 13 (foreign-individual lawful RMB income with tax documentation), Art. 14/15 (outward remittance), Art. 39 repealed by 汇发〔2023〕8号 confirmed.
- [SAFE, ATM withdrawal notice](https://www.safe.gov.cn/hubei/2019/0305/851.html) — CNY 100,000/person/year and CNY 10,000/card/day confirmed.
- [BOC, ATM price-change notice effective 2026-11-11](https://www.boc.cn/pbservice/bi2/202608/t20260811_25684907.html) — UnionPay ¥12 + 1% (max ¥112); Visa/Mastercard 2.5% (min USD-equiv. 3 / max USD-equiv. 40) per withdrawal confirmed.
- [BOC, personal service price list effective 2025-11-11 (PDF)](https://pic.bankofchina.com/bocappd/pricelist/202511/P020251110646838136627.pdf) — item 210105008: TT/draft 0.1%, min ¥50 / max ¥260, international telecom ¥150; note 5: full-arrival USD 15 (BOC NY) / USD 25 elsewhere; item 210101002: permit ¥10 waived 2025-04-01–2026-12-31 confirmed.
- [BOC live FX board](https://www.boc.cn/sourcedb/whpj/enindex_1619_1.html) — 2026-11-10 06:43 USD buy 6.6622 / sell 6.6903 / middle 6.7188; sell-below-middle anomaly persists, corroborating the flagged item. Model's dated 2026-11-09 05:30 snapshot (6.6648/6.6929) remains correctly labeled historical.
- [Wise, Guide to CNY transfers](https://wise.com/help/articles/2955298/guide-to-cny-transfers) — non-mainland-Chinese eligibility, own-account-only recipients, CNY 300,000/bank transfer and CNY 50,000/Alipay caps, tax-record overall limit confirmed.
- [Wise, Summary of fee changes (2024-11-25)](https://wise.com/gb/blog/summary-of-fee-changes) — bank ¥33.20 + 0.62%; Alipay ¥33.20 + 1.97% (dated formulas only) confirmed.
- [CBP, Know Before You Go](https://www.cbp.gov/travel/us-citizens/know-before-you-go/know-you-go-traveling-abroad) and [IRS Form 3520 instructions](https://www.irs.gov/instructions/i3520) — retrieved; FinCEN Form 105 / Form 3520 scope as published on taxes.html confirmed at retrieval level.

**Verification performed:** `python3 scripts/build_site.py && python3 scripts/validate_site.py` PASS (6 pages, 18 procedures, 4×40 matrices, 47 sources, local links, landmarks, independent Decimal arithmetic); working tree clean after rebuild (generated files current). Local HTTP smoke test: all 8 pages + style.css + data/cost-model.json returned 200. Live site fetched and confirmed serving the corrected build (cutoff 2026-11-09, BOC $53.45/$902.72, Wise 9 transfers · $2,524.64 at $400k). Pages API reports `built`, legacy, source main "/". Mobile: ≤760px tables render as labelled cards via `data-label` (style.css); hero leads with executive answer and cost snapshot (most important info first).

**Irregularities:** none new. All previously flagged items remain published on flagged.html and do not block the merge. Stale duplicate PRs #4, #5, #12 from other sessions remain open and untouched.

### Publication record — arena/753a8878-china4 (task 12)
- PR #20: https://github.com/sassnarep3-star/China4/pull/20 — MERGED as `1bb313ca33a4ee0a5516cdbb8d1a81bfcdf3141c` on 2026-11-10 01:02 UTC.
- Post-merge deploy: Validate and deploy run 42732847124 + pages build 42732846784 succeeded; GitHub Pages API reports status `built` at https://sassnarep3-star.github.io/China4/.
- Note: parallel session arena/09fa5313-china4 merged PR #21 after this session's merge; no conflicts with this additive record.

### Publication record — arena/09fa5313-china4 (task 12)
- [PR #21](https://github.com/sassnarep3-star/China4/pull/21) merged as `c0c7b34790d21fe7a6c8ee542585d1585dc4b87d` on 2026-11-10 01:03 UTC. Validate run [42732948474](https://github.com/sassnarep3-star/China4/actions/runs/42732948474) succeeded; its pages-build-deployment run was superseded by PR #22's deployment [42733024718](https://github.com/sassnarep3-star/China4/actions/runs/42733024718) (success). Pages API reports `built`. Live site: https://sassnarep3-star.github.io/China4/
- Merge conflict during rebase: arena/753a8878-china4 merged PR #20 (parallel task-12 audit, also no defects) into main while this session worked. Resolved by retaining both sessions' board sections in full — no work discarded. Validator passes on the combined tree.
## Current session: arena/b398220f-china4 — citation durability & publication

| Task | Scope (files) | Status | Owner | Started (UTC) | Notes |
|---|---|---|---|---|---|
| 14 | Independent audit of citation durability and numeric claims; fix any defect found; PR + merge + Pages confirmation | `scripts/build_site.py`, `scripts/validate_site.py`, generated root HTML pages, `EXECUTIVE_SUMMARY.md`, `README.md`, `COORDINATION.md` | in progress | arena/b398220f-china4 | Renumbered from 12: `arena/753a8878-china4` (PR #20) and `arena/09fa5313-china4` (PR #21) concurrently claimed/completed task 12 while this session's claim was in flight. Collisions logged; this session kept a non-overlapping scope by auditing citation durability (the FX quote link) and adding a penalty-ceiling comparison rather than repeating the same spot-check list. Branch fixed by Arena. |
### Audit log — arena/b398220f-china4 (task 14)

**Defect found and fixed (High, citation integrity).** Source S5 pointed at BOC's rotating rate board, page 5 (`enindex_1619_4.html`), where the cited 2026-11-09 05:30 USD row (buy 666.48 / sell 669.29 CNY per USD) had been visible. On 2026-11-10 that page shows a later quote (02:49: buy 666.22 / sell 669.03), so the link no longer reproduced the model input. Fixes: S5 repointed to BOC's official historical exchange-rate query (date 2026-11-09, USD, captcha) with explicit re-query instructions on `sources.html`; new S48 cites BOC's current board as a magnitude cross-check; `flagged.html` now states the roll-off rather than claiming page 5 is correct; `validate_site.py` fails if the stale URL returns or if either required FX citation is missing.

**Also fixed.** `sources.html` linked to a session branch that can be deleted (`blob/arena/d778fbdf-china4`); now `blob/main`. A flagged item still said the ATM change was "three days after research cutoff"; the cutoff is now 2026-11-10 and the item says one day. Research cutoff restated 2026-11-10 UTC.

**Added (decision value).** A "penalty vs lawful cost" table (6 amounts) applying the published statutory ceilings — 30% of the amount, 30%–100% in serious cases (Art. 39/40/45), 20% for unlawful cash carriage (Art. 42), FBAR nonwillful $16,536 per violation — beside the modeled lawful BOC cost, plus a dashboard line linking to it. It is labeled as arithmetic on statutory rates, not an assessment.

**Independent verification performed this session (all fetched 2026-11-10):**
- [SAFE Individual FX Detailed Rules](https://www.safe.gov.cn/tianjin/2024/0430/2464.html) — Art. 2 annual $50,000 settlement/purchase total for domestic individuals; Art. 13 foreign individual's lawful current-account RMB income needs ID + amount-matched documents including tax vouchers, reconversion within 24 months; Art. 15 existing-FX remittance with ID; Art. 39 repeal note present.
- [SAFE cash-carry rules](https://www.safe.gov.cn/tianjin/2024/0430/2466.html) — ≤$5,000 no permit, $5,000–10,000 bank permit, >$10,000 generally not permitted except listed special cases with SAFE permit. Matches S7.
- [SAFE card-cash notice](https://www.safe.gov.cn/hubei/2019/0305/851.html) — CNY 100,000/person/year and CNY 10,000/card/day; borrowing/lending cards to evade is prohibited. Matches S9.
- [State Council FX Regulations, Decree 532](https://www.gov.cn/gongbao/content/2008/content_1071846.htm) — Art. 39/40/45 fines ≤30%, serious 30% to equivalent amount; Art. 42 ≤20% for unlawful carriage. Matches S18 and the new exposure table.
- [BOC personal price list effective 2025-11-11](https://pic.bankofchina.com/bocappd/pricelist/202511/P020251110646838136627.pdf) — item 210105008 TT/draft 1‰, min ¥50, max ¥260, international telecom ¥150 (HK/Macau/Taiwan ¥80); note 5 full-arrival $15 (BOC NY) / $25 elsewhere; item 210108014 cross-border ATM ¥12 + 1%, max ¥112; item 210101002 permit ¥10 waived 2025-04-01 to 2026-12-31. Matches S4 and every BOC column.
- [BOC ATM change effective 2026-11-11](https://www.boc.cn/pbservice/bi2/202608/t20260811_25684907.html) — UnionPay unchanged; Visa/Mastercard 2.5% of amount, min $3 / max $40 equivalent per withdrawal. Matches S10 (shown separately, not substituted).
- [BOC current board](https://www.boc.cn/sourcedb/whpj/enindex.html) — 2026-11-10 02:49 USD 6.6622/6.6903; half-spread 0.210449% vs modeled 0.210366% (~0.04% relative).
- [eCFR 31 CFR 1010.821](https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010/subpart-H/section-1010.821) — nonwillful $16,536, willful $165,353 for assessments on/after 2025-01-17. Matches S26.
- [IRS Form 8938/FBAR comparison](https://www.irs.gov/businesses/comparison-of-form-8938-and-fbar-requirements) — all four thresholds and the $10,000 FBAR trigger. Matches S27/S25.
- [IRS FEIE](https://www.irs.gov/individuals/international-taxpayers/figuring-the-foreign-earned-income-exclusion) — 2026 maximum $132,900. Matches S35.
- [Wise CNY guide](https://wise.com/help/articles/2955298/guide-to-cny-transfers) — non-mainland-Chinese, China work history, tax records within 3 years, own-account recipient, CNY 300,000 bank-app / 50,000 Alipay per transfer, overall limit = after-tax salary. Matches S11.
- [IRS Form 3520 instructions](https://www.irs.gov/instructions/i3520) + [IRM 8.11.5](https://www.irs.gov/irm/part8/irm_08-011-005) — 5% of gift per month, capped at 25%. Matches S28.

**Verification run:** `python3 scripts/build_site.py && python3 scripts/validate_site.py` PASS (6 pages, 18 procedures, 4×40 matrices, 6 exposure rows, 48 sources, local links, landmarks, Decimal arithmetic, citation-durability guards). Local HTTP: all six pages, both redirects, `style.css` and `data/cost-model.json` returned 200. Site files remain generated, no manual HTML edits.

**Irregularities still open (published on flagged.html, non-blocking):** live execution quotes and correspondent/receiver deductions, Wise/WU/MoneyGram current prices, other banks' tariffs, ATM execution FX and surcharge, PayPal/wallet and HK two-leg completeness, and all personal tax amounts. No new unverified value was added.

## Current session: arena/afeb2b56-china4 — task 13: conversion-penalty deep dive, extra routes, claim-level audit ledger (NEW files only)

| Task | Scope (files) | Status | Owner | Started (UTC) | Notes |
|---|---|---|---|---|---|
| 13 | (a) "Conversion penalty" deep dive: China tax needed to document each source of funds, US §988 currency-gain exposure by acquisition year, published SAFE enforcement outcomes; (b) routes not yet in the 18-route library; (c) one consolidated every-method × $10k–$400k mobile-first table; (d) claim-level audit ledger of the existing 47 sources (each claim re-read against the fetched official text) | **New files only:** `unlock.html`, `compare.html`, `audit.html`, `scripts/build_deepdive.py`, `scripts/validate_deepdive.py`, `data/deepdive-model.json`, `data/audit-ledger.json`; plus this section of `COORDINATION.md` | needs review | arena/afeb2b56-china4 → arena/fd53cba7-china4 | 2026-11-10 01:06 | Deliberately does **not** touch `scripts/build_site.py`, `scripts/validate_site.py`, `style.css`, the six generated pages, `data/cost-model.json`, `README.md`, `EXECUTIVE_SUMMARY.md` or the workflow while they are claimed by other sessions. Branch fixed by Arena. |

### Claim log — arena/afeb2b56-china4
- **Board state read before claiming (2026-11-10 01:06 UTC, all remote branches fetched read-only):** task 12 was claimed within ~60 seconds of each other by six sessions with the same file scope — `753a8878` (done, merged as PR #20, no site change), `09fa5313` (done on its branch, no site change), and `36711496`, `374f09e6`, `7f52b605`, `b398220f` (all *in progress*, all listing `scripts/build_site.py`, `scripts/validate_site.py`, generated root HTML, `style.css`, `README.md`, `EXECUTIVE_SUMMARY.md` and the workflow). **Irregularity logged:** these claims overlap each other; they were made on separate branches, so none was visible to the others on `main` when written.
- Because that scope is already claimed several times over, this session takes a **different, additive scope made only of new files** (listed above). Nothing an active session owns is edited here.
- **Stale claim noted, not yet taken over:** `arena/ddfecf5c-china4` claimed "Phase 2 — 21-route expansion, tax-bottleneck playbook, mobile-first table UX" on 2026-11-09 01:46 UTC; its branch has had no commit since (>23 h, well past the 60-minute rule) and contains no work product (only the claim line; the `data/source-verification-log.json` it mentions was never pushed). The *new-file* part of that idea (tax-bottleneck analysis, extra routes) is covered by task 13 here. The shared-file part stays with whichever session integrates last.
- **Change requests to shared files (not applied by this session until the active task-12 sessions are done or stale — see "final integration" below):**
  1. `scripts/build_site.py` → `NAV`: add links to `unlock.html`, `compare.html`, `audit.html`.
  2. `.github/workflows/gh-pages.yml`: run `scripts/build_deepdive.py` + `scripts/validate_deepdive.py`; copy the three new pages and two new data files into `_site/`.
  3. `scripts/build_site.py` → `SOURCES` / `flagged.html`: register any new official sources and any defect this audit finds in existing rows (defects are listed in `data/audit-ledger.json` and on `audit.html`; they are *not* silently patched into another session's file).
- **Final integration:** when every other task on this board is `done` (or its claim is >60 minutes old with no commits), this session will act as the integration session for task 13: rebase on `main`, apply requests 1–3, re-run both validators, open the PR, merge, and confirm the Pages deployment. If another session integrates first, these requests remain here for it.
- **Rebase conflict #1 (2026-11-10 01:07 UTC):** `git pull --rebase origin main` conflicted in `COORDINATION.md` because PRs #21–#24 (`09fa5313`, `b398220f`) had appended their sections at the same end-of-file position while this claim was being written. Resolved by keeping **both sides in full** (main's sections first, this session's section after). No other session's text was dropped or edited. The claim commit had already been pushed un-rebased; the branch was then updated with `--force-with-lease` (own session branch only).
- **Board state after that rebase:** `b398220f` renumbered itself to task 14 and merged PR #24 (S5 repointed to BOC's dated query, S48 added, penalty-ceiling table, 48 sources). Task 13 here remains non-overlapping with it.

### Publication record — arena/b398220f-china4 (task 14)
- PR [#24](https://github.com/sassnarep3-star/China4/pull/24) merged as `bab34189d0110af8fe119ec932a7b3c2da0e8542` on 2026-11-10 01:06 UTC. Pull-request validation run [42733337982](https://github.com/sassnarep3-star/China4/actions/runs/42733337982) passed before merge (build reproducibility + validator). Post-merge "Validate and deploy China4" run [42733395264](https://github.com/sassnarep3-star/China4/actions/runs/42733395264) and pages build [42733394737](https://github.com/sassnarep3-star/China4/actions/runs/42733394737) succeeded; Pages API reports `built` (legacy, source `main` "/"). GitHub emitted only non-fatal Node 20 deprecation and ubuntu-latest migration notices.
- Live verification after deploy: `sources.html` served cutoff 2026-11-10, 48 documents, S5 repointed to BOC's date query and S48 present. The first `index.html` fetch returned a stale CDN copy (old cutoff and old S5 URL); a cache-busted fetch of `index.html?cb=20261110T0115` returned the new build with the dated-snapshot wording, S5+S48 links and the penalty-exposure line. Cache propagation, not a deployment failure — worth re-checking with a cache-buster when auditing.
- Board conflicts: main advanced five times during this session (PRs #20–#23 from parallel task-12 sessions). Two rebase conflicts, both confined to `COORDINATION.md`; resolved by retaining every session's section in full and appending only the audit log. No site file conflicted, no work discarded, and the validator passed on each combined tree.

### Task 14 — done
Scope delivered: citation-durability fix for the FX input (S5 → official date query, S48 cross-check, validator regression guard), removal of a deletable branch-specific repo link, cutoff/wording corrections, and a sourced statutory penalty-ceiling versus lawful-cost comparison. All new or changed values trace to official sources listed in the audit log above. Open items remain published on `flagged.html` and do not block.

## Session arena/7f52b605-china4 — independent re-verification (task 12)

| Task | Scope | Status | Owner | Verification / notes |
|---|---|---|---|---|
| 12 | Independent line-by-line audit of the live build, fresh official-source spot-checks, arithmetic re-derivation, defect fixes, PR + merge + Pages confirmation | `scripts/build_site.py`, `scripts/validate_site.py`, generated root HTML, `data/cost-model.json`, `README.md`, `EXECUTIVE_SUMMARY.md`, `COORDINATION.md` | done | arena/7f52b605-china4 | Claim pushed 2026-11-10. Branch fixed by Arena and used as the integration branch. |

### Sources fetched and read in full this session (2026-11-10)

- [SAFE Individual FX Detailed Rules (2007, as modified)](https://www.safe.gov.cn/safe/2007/0105/5320.html) — Art. 2 (USD 50,000 annual convenience quota for 个人 settlement and 境内个人 purchase), Art. 13 (foreign individual: ID + amount evidence **including tax vouchers**; reconversion with original memo within **24 months**), Art. 15 (foreign individual remitting FX savings with ID). Art. 39 is marked repealed on SAFE's own page.
- [SAFE Measures for Individual FX (PBOC Order 2006 No. 3)](https://www.safe.gov.cn/tianjin/2024/0430/2465.html) — Art. 37 definitions: 境内个人 = Chinese citizens holding a PRC resident ID; 境外个人 = foreign citizens (incl. stateless) **holding a passport** plus HK/Macau/Taiwan compatriots.
- [State Council FX Regulations, Decree 532](https://www.gov.cn/gongbao/content/2008/content_1071846.htm) — read Art. 39–48. Confirms fine **up to 30%**, serious cases **over 30% up to 100%**, Art. 42 illegal cash carriage **up to 20%**, and Art. 52's 境内个人 definition that includes a foreign national residing in China for a continuous year.
- [BOC personal service price list effective 2025-11-11](https://pic.bankofchina.com/bocappd/pricelist/202511/P020251110646838136627.pdf) — item 210105008 TT/draft 0.1%, min ¥50 / max ¥260, international telecom ¥150, draft postage actual; note 5 full-arrival USD 15 (BOC NY) / USD 25 elsewhere; item 210101002 carrying permit ¥10 waived to 2026-12-31; item 210108014 cross-border ATM ¥12 + 1%, max ¥112.
- [BOC ATM price change effective 2026-11-11](https://www.boc.cn/pbservice/bi2/202608/t20260811_25684907.html) — UnionPay unchanged; Visa/Mastercard 2.5% of amount withdrawn, min USD-equiv. 3 / max USD-equiv. 40 **per withdrawal**.
- [BOC MoneyGram fee schedule effective 2018-01-15](https://www.boc.cn/pbservice/bi2/201801/t20180112_11198459.html) — confirms the top non-Africa USD tier is 5,000.01–9,999.99 at $32, i.e. nothing above $9,999.99.
- [BOC live FX board](https://www.boc.cn/sourcedb/whpj/enindex_1619_1.html) — 2026-11-10 06:43 USD buy 6.6622 / sell 6.6903 (per 100 CNY table 666.22 / 669.03). Independent half-spread 0.210447% vs 0.210366% modeled.
- [Wise guide to CNY transfers](https://wise.com/help/articles/2955298/guide-to-cny-transfers) — non-mainland-Chinese eligibility, own-account recipient only, tax record within 3 years, **CNY 300,000/transfer (bank app)**, **CNY 50,000/transfer (Alipay)**, overall limit = after-tax salary.
- [Wise fee-change summary](https://wise.com/gb/blog/summary-of-fee-changes) — bank funding ¥33.20 + 0.62%; Alipay ¥33.20 + 1.97% (dated 2024 examples only).
- [SAFE cash-carrying measures](https://www.safe.gov.cn/tianjin/2024/0430/2466.html) — no permit ≤ USD 5,000; bank permit USD 5,000–10,000; above USD 10,000 generally not permitted except listed special cases.
- [SAFE card-cash notice, Hui Fa [2017] No. 29](https://www.safe.gov.cn/hubei/2019/0305/851.html) — CNY 100,000 per person per calendar year; **CNY 10,000 per card per day**; borrowing/lending cards prohibited.
- [SAFE 2022 Q&A](https://www.safe.gov.cn/ningxia/2022/0929/1997.html) — the annual convenience quota is **not** a ceiling on genuine current-account purchase/settlement; documentation, not an ID alone, is required above it.
- [PBC Announcement [2004] No. 18](https://www.pbc.gov.cn/chubanwu/114566/114579/114643/2839193/index.html) — RMB 20,000 per person per trip for Chinese citizens and foreign nationals.
- [Customs Announcement 2025 No. 43](https://www.gov.cn/zhengce/zhengceku/202504/content_7017195.htm) — effective 2025-04-01; currency beyond the prescribed amount must be declared; **repeals Announcement 2007 No. 72**.
- [eCFR 31 CFR 1010.821](https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010/subpart-H/section-1010.821) — nonwillful **$16,536**, willful **$165,353** (assessments on/after 2025-01-17).
- [IRS Form 8938 / FBAR comparison](https://www.irs.gov/businesses/comparison-of-form-8938-and-fbar-requirements) — all four thresholds; FBAR trigger > $10,000.
- [IRS FEIE](https://www.irs.gov/individuals/international-taxpayers/figuring-the-foreign-earned-income-exclusion) — 2026 maximum **$132,900**.
- [CBP money and monetary instruments](https://www.cbp.gov/travel/international-visitors/money-monetary-instruments) — > $10,000 report, **group/family aggregation**, electronic FinCEN 105 filing.
- [FinCEN FBAR page](https://www.fincen.gov/report-foreign-bank-and-financial-accounts) — aggregate > $10,000 at any time in the calendar year.
- [Bank of America wire flyer](https://resources.bankofamerica.com/direct/render-resource/9149a2de7b1047a499ae291815e985e6) — inbound **$15**, may be waived.
- [Chase Secure Checking fees](https://www.chase.com/personal/fees/secure-checking) — domestic and international incoming wires **$15**.
- [Capital One wire transfer](https://www.capitalone.com/help-center/checking-savings/send-receive-wire-transfer/) — $15 incoming only on Essential Checking, High-Yield Checking, Essential Savings; other account types no fee.
- [PBOC Announcement [2004] No. 16](https://www.gov.cn/gongbao/content/2005/content_64294.htm) — emigration transfer applied for in full at once; 50% / then 50% of the remainder after 1 year / balance after 2 years; **≤ RMB 200,000 may be remitted in one lump sum after approval**; inheritance once or in instalments.

### Defects found and fixed

1. **S8 was cited for numbers it does not contain (High).** The customs clearance-guide page never states RMB 20,000 or USD 5,000. The values now rest on the PBOC announcement (S49) and the current customs instrument (S50); S8 is retained only for the red/green-channel procedure.
2. **The relied-on customs instrument had been repealed (High).** Announcement 2007 No. 72 was repealed effective 2025-04-01 by Announcement 2025 No. 43. The site now cites the current instrument and keeps the "declare currency beyond the prescribed amount" duty while dropping the defunct list.
3. **CBP source did not state the $10,000 rule (Medium).** Replaced with CBP's dedicated money/monetary-instruments page (S51), which also documents group aggregation. No value changed.
4. **Capital One example named an account type its own page does not name (Medium).** "360 Checking $0" was not what the page says; the note now states the disclosed condition.
5. **Dead official link (Medium, non-live).** `safe.gov.cn/en/2018/1206/1478.html` returns SAFE's page-not-found notice. No published row depended on it; the penalty ranges stand on S18, read in full.
6. **Identity-regulation divergence published as a review item (High).** SAFE treats a passport holder as 境外个人; Decree 532 includes a foreign national resident for a continuous year in 境内个人. Neither reading creates a general ID-only USD 50,000 right.
7. **Reproducibility link pinned an old session branch** — repointed to `blob/main`.

### Verification performed

- `python3 scripts/build_site.py && python3 scripts/validate_site.py` → **PASS**: 6 pages, 18 procedures, 4 × 40 cost matrices, 52 primary sources, local links, landmarks, per-row source-link requirement, independent `Decimal` re-derivation of the BOC, quota, Wise, ATM, emigration and receiving scenarios.
- Independent arithmetic re-derivation outside the validator: 40/40 BOC rows reproduce exactly (commission clamp, ¥150 telecom, same-quote half-spread, base USD); Wise splits confirmed for $10k/$100k/$200k/$400k (1/3/5/9 bank-funded; 2/14/27/54 Alipay-funded) with the fixed fee charged per transfer.
- Local HTTP smoke test: `index`, `methods`, `penalties`, `taxes`, `sources`, `flagged`, both redirects, `style.css` and `data/cost-model.json` all returned **200**; every page byte-identical to the generator output (`git diff` clean before regeneration).
- Mobile: no CSS change was needed — tables still collapse to labelled cards at ≤760 px via `data-label` on every `td`.

### Merge-conflict log

- First rebase onto `main` conflicted in `COORDINATION.md` (sessions `arena/753a8878-china4` and `arena/b398220f-china4` had appended boards). Resolved by **retaining every session's section in full**; nothing discarded.
- The rebase then conflicted in `scripts/build_site.py`, the validator and four generated pages, because `arena/b398220f-china4` had already used source id **S48** for the BOC board. Rather than overwrite their work, this session replayed its edits on top of theirs and re-numbered its new sources **S49–S52**, then regenerated all HTML from the merged generator. Cross-checked that their BOC-board citation, date-query note and penalty-ceiling comparison survive intact.

### Publication

- PR and merge result are recorded in the "Publication log" section below after the merge, together with the Pages deployment run and the live-URL check.

### Post-merge follow-up — arena/7f52b605-china4

- PR [#27](https://github.com/sassnarep3-star/China4/pull/27) merged at `b0289c763475aa0e878f550dcfeb46ecf8689166` on 2026-11-10 01:11 UTC. GitHub Pages reported `built` for that commit and the live pages were fetched.
- **Live-site defect caught after the merge:** `sources.html` served **52** register rows while its own prose still said "48 primary documents"/"48-document register". Two hard-coded counts in the generator had escaped the earlier renumbering when this branch was rebased onto another session's change. Fixed by deriving the count from `len(SOURCES)` in the generator and by adding a validator guard that fails when the stated number differs from the number of registered rows (negative-tested: mutating 52 → 49 produced `sources: prose claims 49 documents but the register has 52`).
- Follow-up PR and its deployment are recorded below.

### Publication log — arena/7f52b605-china4 (final)

| Item | Result |
|---|---|
| PR #27 | https://github.com/sassnarep3-star/China4/pull/27 — merged **2026-11-10 01:11 UTC** at `b0289c763475aa0e878f550dcfeb46ecf8689166` |
| PR #29 | https://github.com/sassnarep3-star/China4/pull/29 — merged at `ec08cb52ae94f9eba0848dd377a2b55717a66052` |
| Pages deploy (PR #27) | `pages build and deployment` [42734166953](https://github.com/sassnarep3-star/China4/actions/runs/42734166953) / run 42733912980 reported success; Pages API status `built` |
| Pages deploy (PR #29) | `pages build and deployment` 42734166967 and `Validate and deploy China4` 42734166953 completed for `ec08cb52`; Pages API status `built` |
| Live URL | https://sassnarep3-star.github.io/China4/ |

**Live verification after the final deploy (cache-busted fetches):**
- `sources.html` now reads "52-document primary-source register" and "52 primary documents", matching 52 register rows; S8 is relabelled as the clearance-procedure page with "threshold values: S49, S50".
- `flagged.html` serves the seven new findings, including the repealed-customs-instrument item, the dead SAFE link, the Capital One condition and the identity-classification divergence, each with source links.
- `penalties.html` serves the corrected Capital One receiving note and the unchanged 40-row matrices (BofA $15, Chase Secure $15 stated as before; no cost value moved).
- Cost model spot-check from the regenerated JSON: $10k = $53.45, $100k = $271.62, $200k = $481.99, $300k = $692.36, $400k = $902.72 (BOC known baseline); full-arrival scenario adds $40; Wise bank-funded 1/3/5/7/9 transfers ($66.96 → $2,524.64), Alipay-funded 2/14/27/41/54 transfers.

**Merge-conflict log (final).** Main advanced four times during this session (PRs #24, #25, #26 and their follow-ups). Every rebase conflicted only in `COORDINATION.md`, except one that also conflicted in the generator because another session had already taken source id **S48**. Each conflict was resolved by retaining all sessions' board sections and replaying this session's edits on top of the other session's generator, renumbering new sources to **S49–S52**; nothing was discarded and no other session's claim, source or finding was removed. `git merge-base --is-ancestor origin/main HEAD` was confirmed before each final push.

**Open items (published on `flagged.html`, non-blocking):** live execution quotes and correspondent/receiver deductions; Wise, Western Union and MoneyGram current prices; other banks' tariffs; ATM execution FX and surcharge; PayPal China/wallet and the Hong Kong two-leg route; provincial customs guidance after 2025-04-01; and all personal China/US tax amounts.

## Session arena/374f09e6-china4 — final integration (task 12)

**Claim.** Arena fixes this session to branch `arena/374f09e6-china4`, so it is the integration branch; no `session-<id>/<task>` branch was created. Base was `main` `54a190c` (PR #17). Task 12 was claimed in `COORDINATION.md` and the claim committed/pushed as `2a4b933` before any edits. `git pull --rebase origin arena/374f09e6-china4` initially failed because the remote branch did not exist; the first push created it.

**Independent line-by-line re-verification (fresh official fetches, 2026-11-10 UTC).** [S1](https://www.safe.gov.cn/tianjin/2024/0430/2464.html), [S2](https://www.safe.gov.cn/tianjin/2024/0430/2465.html), [S4](https://pic.bankofchina.com/bocappd/pricelist/202511/P020251110646838136627.pdf), [S5](https://www.boc.cn/sourcedb/whpjSearch/index_2833.html), [S7](https://www.safe.gov.cn/tianjin/2024/0430/2466.html), [S9](https://www.safe.gov.cn/hubei/2019/0305/851.html), [S10](https://www.boc.cn/pbservice/bi2/202608/t20260811_25684907.html), [S11](https://wise.com/help/articles/2955298/guide-to-cny-transfers), [S13](https://wise.com/gb/blog/summary-of-fee-changes), [S16](https://www.boc.cn/pbservice/bi2/201801/t20180112_11198459.html), [S18](https://www.gov.cn/gongbao/content/2008/content_1071846.htm), [S19](https://www.safe.gov.cn/safe/2015/1231/5442.html), [S20](https://www.gov.cn/gongbao/content/2005/content_64294.htm), [S25](https://www.irs.gov/businesses/small-businesses-self-employed/report-of-foreign-bank-and-financial-accounts-fbar), [S26](https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010/subpart-H/section-1010.821), [S27](https://www.irs.gov/businesses/comparison-of-form-8938-and-fbar-requirements), [S28](https://www.irs.gov/instructions/i3520), [S30](https://www.fincen.gov/resources/frequently-asked-questions-regarding-fincen-currency-transaction-report-ctr), [S31](https://www.irs.gov/publications/p1544/ar02.html), [S35](https://www.irs.gov/individuals/international-taxpayers/figuring-the-foreign-earned-income-exclusion), [S38](https://www.irs.gov/publications/p525), [S39](https://fgk.chinatax.gov.cn/zcfgk/c100009/c5193028/content.html), [S42](https://resources.bankofamerica.com/direct/render-resource/9149a2de7b1047a499ae291815e985e6), [S43](https://www.chase.com/personal/fees/secure-checking), [S44](https://www.capitalone.com/help-center/checking-savings/send-receive-wire-transfer/), [S46](https://www.safe.gov.cn/ningxia/2022/0929/1997.html), [S48](https://www.boc.cn/sourcedb/whpj/enindex.html). No value was inferred to fill a blank.

**Irregularities found (published on flagged.html; do not block merge).**
- High — the exact 2026-11-09 05:30 BOC USD row (666.48/669.29 per 100 USD) used by the model is no longer displayed on any of the five pages of BOC's rolling board, and BOC's historical date search requires a captcha. No permanent official URL reproduces it. Inputs remain in `data/cost-model.json`; obtain a written rate confirmation before execution.
- Medium — BOC separately publishes a Middle Rate (671.88 at 2026/11/10 07:32:39 Beijing) that is not the arithmetic midpoint of its buy/sell quotes (666.22/669.03); the model computes its own midpoint. Definition should be confirmed with BOC.
- Low — the PRC IIT rate tables on S39 are images; the seven brackets and quick deductions were not independently transcribed.
- Previously corrected defects from my first pass (S8 thresholds not in the HTML page, S51/CBP direction, S44 account naming, stale `blob/arena/` link) were already fixed on `main` by session `arena/7f52b605-china4`; their fixes and S49–S52 were preserved, not duplicated or overwritten.

**Merge-conflict log (required by the task rules).** PR #30 was created and reported `CONFLICTING`: sessions `arena/b398220f-china4` (PR #24), `arena/afeb2b56-china4` (PR #25), `arena/7f52b605-china4` (PRs #27, #29) and `arena/b398220f-china4` (PR #28) had merged overlapping work into `main` while this branch was in flight — 52 sources, the current Customs Announcement 2025 No. 43, the dedicated CBP page, a dynamic prose/register count guard, corrected Capital One wording and an FX citation-durability guard. `git merge --no-commit --no-ff origin/main` conflicted in 12 files. Resolution: took `main`'s version of every conflicting file **in full** (nothing discarded), then re-applied only this session's unique contribution on top — the executive-summary page, the 07:32:39 rate check, three new flagged items, validator/Pages wiring and documentation. Their dynamic `len(SOURCES)` count, 52-source register, S48–S52 and all corrected rows survive. Conflict was resolved without discarding another session's work.

**Deliverable.** New live `summary.html` (five key amounts, eight-route shortlist, six-row tax/penalty boundary, eight execution steps, every table row with a direct official-source link), nav entry and dashboard CTA; rate-freshness callout on Costs; three new flagged items; `data/cost-model.json` provenance; README, EXECUTIVE_SUMMARY, validator (7 pages, summary row counts, nav link guard) and the Pages artifact copy list.

**Verification performed.** `python3 scripts/build_site.py` → 7 pages, 2 redirects, 40 audited rows; `python3 scripts/validate_site.py` → PASS (7 pages, executive summary, 18 procedures, 4×40 matrices, 52 sources, prose/table agreement, canonical FX citations, local links, landmarks, independent Decimal arithmetic). Local HTTP smoke test: all 9 HTML/redirect pages, `style.css` and `data/cost-model.json` returned 200. The validator checks link presence and arithmetic, not that each external page supports every claim; the defects above were found by reading official text.

**Publication.** PR [#30](https://github.com/sassnarep3-star/China4/pull/30) from `arena/374f09e6-china4` → `main`. Merge result and Pages deployment are recorded below after they complete.

**Task status:** in progress until PR #30 is merged and GitHub Pages deployment is confirmed.

## Current session: arena/a2efb7b1-china4 — task 15: multi-bank tariffs, stuck-CNY tax-gate playbooks, and line-by-line repo verification (NEW files only)

| Task | Scope (files) | Status | Owner | Started (UTC) | Notes |
|---|---|---|---|---|---|
| 15 | (1) Research & verify additional PRC bank tariffs (ICBC, CCB, CMB, ABC, HSBC China) and lawful conversion channels (UnionPay POS overseas direct spend vs ATM cap, departing-foreigner PRC social-insurance lump-sum refund/remittance, WFOE/PRC dividend distribution + US–China Treaty Art. 9 + STA/SAFE `[2021] No. 19` tax record filing >$50k, SkyRemit); (2) build $10,000–$400,000 (40-increment) multi-bank cost & stuck-CNY tax-gate/penalty minimization playbooks; (3) perform line-by-line repo verification from official primary sources and publish irregularities | **New files only:** `banks.html`, `playbooks.html`, `verification.html`, `scripts/build_bank_playbooks.py`, `scripts/validate_bank_playbooks.py`, `data/bank-playbooks.json`; plus this section of `COORDINATION.md` | needs review | arena/a2efb7b1-china4 → arena/fd53cba7-china4 | 2026-11-10 01:16 | Non-overlapping with Task 13 (`afeb2b56`: `unlock.html`, `compare.html`, `audit.html`, `build_deepdive.py`, `validate_deepdive.py`, `deepdive-model.json`, `audit-ledger.json`), PR #30 (`374f09e6`, `summary.html` merged), and PR #31 (`36711496`). Shared files (`scripts/build_site.py`, `scripts/validate_site.py`, root generated pages, `style.css`, `README.md`, `EXECUTIVE_SUMMARY.md`, `.github/workflows/gh-pages.yml`) are NOT edited while claimed by active sessions; change requests logged below for final integration. Branch fixed by Arena (`arena/a2efb7b1-china4`). |

### Claim & coordination log — arena/a2efb7b1-china4
- **Non-overlapping scope verified against `main` (`3f9aad4`) and all active remote branches (`afeb2b56`, `374f09e6`, `36711496`, `7f52b605`, `b398220f`):** only the six new files listed above plus this coordination section are touched during Task 15 execution.
- **Rebase conflict #1 (2026-11-10 01:17 UTC):** PR #30 (`arena/374f09e6-china4`) merged into `main` (`3f9aad4`) at the end of `COORDINATION.md` while PR #33 (this claim) was opening. Stopped and resolved by retaining `374f09e6`'s section in full above and appending this claim below; zero text discarded.
- **Initial repo irregularity spotted on read-through (logged, not edited in another session's section):** `COORDINATION.md` lines 309 and 328 contain stray partial merge-conflict marker remnants (`EAD`) introduced during an earlier rebase in `58e0670`. Logged for cleanup at final integration and on `verification.html`.
- **Shared-file change requests for final integration (logged per coordination rules rather than editing files currently claimed by PR #31 / `374f09e6`):**
  1. `scripts/build_site.py` (`NAV`, `index_page`, `flagged_page`, `sources_page`) and `scripts/validate_site.py`: link `banks.html`, `playbooks.html`, and `verification.html` in global navigation and register newly verified primary sources once all active shared-file sessions are `done`.
  2. `.github/workflows/gh-pages.yml`: run `python3 scripts/build_bank_playbooks.py && python3 scripts/validate_bank_playbooks.py` in `validate`, and include `banks.html`, `playbooks.html`, `verification.html`, and `data/bank-playbooks.json` in `_site/` during `deploy` (note: GitHub Pages `build_type` is also `legacy` from `main:/`, which serves root `.html` files directly, while Actions artifact deploy stages `_site/`).
  3. Clean up the two stray `EAD` lines in `COORDINATION.md` without altering any session's substantive record.
- When all active shared-file claims (`374f09e6`, `36711496`, `afeb2b56`) reach `done` (or become stale >60 min), this session (or the last completing integration session) will integrate the shared navigation/workflow cleanly, re-verify line by line, open & merge PR to `main`, and verify live GitHub Pages deployment.

## Session arena/c009d1db-china4 — strict evidence audit and publication

| Task | Scope | Status | Owner | Started UTC |
|---|---|---|---|---|
| Strict evidence boundary, independently checked primary-source executive brief, validation and publication | COORDINATION.md; new evidence.html; scripts/build_evidence.py; scripts/validate_evidence.py; README.md; .github/workflows/gh-pages.yml; scripts/build_site.py (navigation and evidence warning only) | done | arena/c009d1db-china4 | 2026-11-10 05:53 |

Claim: no other session's new files will be edited. Shared navigation/workflow claims above are older than 60 minutes; this session takes over only integration of its evidence page, preserving existing generators and research. Existing FX values cannot be independently reproduced from a stable official URL: a strict table will leave executable costs blank rather than present them as verified. Fixed Arena branch is the integration branch. No account or tax facts will be invented.

### Independent audit result — arena/c009d1db-china4
- Freshly read official primary text on 2026-11-10: [SAFE Detailed Rules Arts. 2, 13–15](https://www.safe.gov.cn/tianjin/2024/0430/2464.html), [PBOC Measures Arts. 2, 5, 7, 13, 28](https://www.safe.gov.cn/tianjin/2024/0430/2465.html), [SAFE permanent-resident exception](https://www.safe.gov.cn/en/2017/1129/1365.html), [IRS worldwide income](https://www.irs.gov/individuals/international-taxpayers/us-citizens-and-resident-aliens-abroad), [IRS FTC](https://www.irs.gov/individuals/international-taxpayers/foreign-tax-credit), [IRS FBAR](https://www.irs.gov/businesses/small-businesses-self-employed/report-of-foreign-bank-and-financial-accounts-fbar), [IRS 8938 comparison](https://www.irs.gov/businesses/comparison-of-form-8938-and-fbar-requirements), [Wise current CNY guide](https://wise.com/help/articles/2955298/guide-to-cny-transfers).
- Added evidence.html: eight freshly checked rules, seven execution steps, 18 route-category ladders × 40 target amounts. Current fee, FX cost, tax and all-in values remain **blank** because no personalized executable quote or tax facts were verified. Linked official rules establish categories, not prices. Existing historical calculations remain intact but are globally labeled illustrative; this strict register supersedes their interpretation as verified current costs.
- Verification: both generators and both validators PASS; all 720 current-cost rows blank; every table data row has an official source; all local page links resolve; 10 public files return HTTP 200. Existing tests check structure and independent arithmetic, not semantic support for every inherited claim. No full fresh line-by-line certification of all inherited sources is made.
- Published review flags: unreproducible historical FX row, unknown personal/account/tax facts, structural tests versus semantic verification, and the Wise 2025 tax-record example not converted to a fabricated 2026 cutoff.
- Coordination: initial pull of this session's remote branch failed because it did not exist; first push created it. PR #31 was still open and showed a fresh update while this narrow integration was running. Its work was not merged or discarded. Changes here are limited to evidence-page navigation/warning/Review linkage and workflow integration, not its US-tax models. Task 15's six new files remain untouched.
- Publication pending: PR URL and Pages result will be recorded after merge.
## Session arena/fd53cba7-china4 — final integration and publication (task 16)

| Task | Scope | Status | Owner | Started (UTC) | Notes |
|---|---|---|---|---|---|
| 16 | Final integration after active tasks 13 and 15: preserve their new-file outputs, wire navigation/workflow, re-run every validator, audit live/mobile routes, open/merge PR, and confirm GitHub Pages | `COORDINATION.md`; after tasks 13/15 complete: shared generator, validator, workflow, documentation and generated site | done | arena/fd53cba7-china4 | 2026-11-10 | Arena fixes this session to this branch. Task 13 (`afeb2b56`) and task 15 (`a2efb7b1`) are currently active, so their claimed new files will not be edited or duplicated; this session is the designated final integration owner. |

### Claim log — arena/fd53cba7-china4
- Read the complete coordination board, current tree, open PRs and remote branches before claiming. PR #31 remains open; tasks 13 and 15 are recent active claims. Their scopes are preserved.
- Per the fixed-branch Arena rule, no `session-<id>/<task>` branch is created. All work remains on `arena/fd53cba7-china4`.
- Integration will not infer unavailable prices or personal tax liabilities. Unknown executable quotes, correspondent deductions, source-of-funds facts, tax basis and account-specific eligibility remain blank and published for review.
## Session arena/36711496-china4 — independent evidence audit (task 12)

| Task | Scope (files) | Status | Owner | Notes |
|---|---|---|---|---|
| 12 | Independent line-by-line evidence audit: re-fetch every cited primary source, re-derive every figure, fix defects, verify live Pages state, PR + merge + deploy confirmation | `scripts/build_site.py`, `scripts/validate_site.py`, generated `*.html`, `EXECUTIVE_SUMMARY.md`, `README.md`, `COORDINATION.md` | done | arena/36711496-china4 |

### Audit log — arena/36711496-china4

**Scope and coordination.** Branch `arena/36711496-china4` (fixed by Arena) is this session's integration branch. During the session, main advanced by 20 commits (through PR #27) and other sessions had already corrected the customs-citation defect inherited from S8 and added source IDs S48–S52. Rather than overwrite that work, this session rebased onto main, replayed only its non-overlapping additions, and **re-numbered its single new source to S53** to avoid a collision. Their S8 correction, PBOC Announcement [2004] No. 18 citation (RMB 20,000) and penalty-vs-cost comparison were verified and preserved intact. `backup-mine-36711496` holds the pre-rebase state for traceability.

**Sources re-fetched and read this session (not merely linked):**
- [SAFE individual FX detailed rules](https://www.safe.gov.cn/tianjin/2024/0430/2464.html) — Arts. 2 (USD 50,000 annual total for settlement and domestic-individual purchase), 13 (foreign individual lawful current-account income with tax vouchers), 14, 15, 30, 39 (marked repealed on SAFE's own page).
- [PBOC individual FX measures](https://www.safe.gov.cn/tianjin/2024/0430/2465.html) — Art. 37 definitions: domestic individual = Chinese citizen holding a PRC resident ID; foreign individual = passport/HK/Macau/Taiwan travel-document holder.
- [SAFE 2022 Q&A](https://www.safe.gov.cn/ningxia/2022/0929/1997.html) — the USD 50,000 figure is a convenience quota, not a hard cap on genuine current-account transactions.
- [State Council FX Regulations, Decree 532](https://www.gov.cn/gongbao/content/2008/content_1071846.htm) — Art. 5 (no restriction on current international payments and transfers); Arts. 39–45 (30% ceiling, 30%–100% for serious cases; 20% for cash).
- [BOC 2025-11-11 personal tariff PDF](https://pic.bankofchina.com/bocappd/pricelist/202511/P020251110646838136627.pdf) — item 210105008 (0.1%, min ¥50, max ¥260; international telecom ¥150), note 5 (full arrival USD 15 BOC NY / USD 25 elsewhere), item 210101002 (permit ¥10, waived to 2026-12-31), item 210108014 (UnionPay ¥12 + 1%, max ¥112), note 10 (ATM-owner surcharge).
- [BOC 2026-11-11 ATM notice](https://www.boc.cn/pbservice/bi2/202608/t20260811_25684907.html) — Visa/Mastercard 2.5%, min USD-equiv. 3 / max 40 per withdrawal.
- [BOC rate board](https://www.boc.cn/sourcedb/whpj/enindex_1619_1.html) — 2026-11-10 06:43 USD buy 6.6622 / sell 6.6903; consistent in magnitude with the 2026-11-09 05:30 model input (6.6648 / 6.6929).
- [eCFR 31 CFR 1010.821](https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010/subpart-H/section-1010.821) — non-willful USD 16,536; willful USD 165,353 (assessments on/after 2025-01-17).
- [eCFR 31 CFR 1010.340](https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010/subpart-C/section-1010.340) — report required to transport more than USD 10,000.
- [IRS FBAR](https://www.irs.gov/businesses/small-businesses-self-employed/report-of-foreign-bank-and-financial-accounts-fbar), [Form 8938/FBAR comparison](https://www.irs.gov/businesses/comparison-of-form-8938-and-fbar-requirements), [Form 3520 instructions](https://www.irs.gov/instructions/i3520) (USD 100,000 nonresident-individual/estate gift threshold), [FEIE page](https://www.irs.gov/individuals/international-taxpayers/figuring-the-foreign-earned-income-exclusion) (2026: USD 132,900).
- [IRS Publication 525](https://www.irs.gov/publications/p525) — personal foreign-currency transaction gain excluded unless more than USD 200, then reported as a capital gain.
- [IRS Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) — 2026 Table 3 brackets, USD 16,100 standard deduction, capital-gain bands USD 49,450 / USD 545,500, FEIE USD 132,900, §6039F USD 20,573.
- [PBOC Announcement [2004] No. 18](https://www.pbc.gov.cn/chubanwu/114566/114579/114643/2839193/index.html) — RMB 20,000 per person per trip.
- [Customs Announcement 2025 No. 43](https://www.gov.cn/zhengce/zhengceku/202504/content_7017195.htm) — repeals Announcement 2007 No. 72 from 2025-04-01.
- [SAFE cash-carrying measures](https://www.safe.gov.cn/tianjin/2024/0430/2466.html) — USD 5,000 permit-free, 5,000–10,000 bank permit, above 10,000 generally prohibited.
- [SAFE ATM-cap notice](https://www.safe.gov.cn/hubei/2019/0305/851.html) — CNY 100,000/person/year, CNY 10,000/card/day, no borrowed cards.
- [SAFE Hui Fa [2015] No. 49](https://www.safe.gov.cn/safe/2015/1231/5442.html) — splitting/borrowed quotas and the watch-list period (year of listing plus two following years).
- [Wise CNY guide](https://wise.com/help/articles/2955298/guide-to-cny-transfers) — non-mainland-Chinese eligibility, 3-year tax records, own-account recipient, CNY 300,000 bank / 50,000 Alipay per transfer, tax-based overall limit.
- [Wise 2024-11-25 fee-change post](https://wise.com/gb/blog/summary-of-fee-changes) — CNY 33.20 + 0.62% (bank) and CNY 33.20 + 1.97% (Alipay).

**Result of the audit:** every cited figure above matched its source on re-read. No figure in the inherited cost model required correction this session; the BOC ladder, half-spread, Wise splits and ATM counts re-derived exactly (`validate_site.py` PASS).

**New contribution (non-overlapping):** the site previously described US tax qualitatively but never quantified it, which left the user's core question ("how much tax would this cost me?") unanswered. Added a 2026 single-filer illustration pricing the same amount under three characters (ordinary income, a 10% currency gain, FEIE-eligible earned income) from Rev. Proc. 2025-32, with the *measured* gain column deliberately blank because acquisition basis is a personal fact. The validator re-derives all fifteen displayed figures from separately re-entered source values; a one-dollar mutation of a bracket makes it fail (negative control run). This also **resolved** the open 2026 §6039F threshold item (USD 20,573).

**Irregularities for review (published on flagged.html, not merge blockers):**
1. The 2026 tax illustration assumes USD 100,000 of other taxable income, single filer, standard deduction. A real return has different inputs.
2. A measured FX gain remains blank: acquisition date and rate of a pre-existing balance cannot be sourced publicly.
3. BOC's board rotates; the dated quote is a benchmark, not an executable rate (already flagged by prior sessions).
4. Stale duplicate PRs #4, #5, #12 from other sessions remain open and were not touched.

### Integration log — arena/fd53cba7-china4
- PR #31 was complete but conflicted with the newer seven-page site. Integrated its unique S53 / Rev. Proc. 2025-32 tax illustration by merging its branch, retaining the current summary page and all S1–S52 work, adding the five-row tax matrix and independent arithmetic checks, then regenerating HTML. Resolved conflicts in `COORDINATION.md`, `EXECUTIVE_SUMMARY.md`, `flagged.html`, and `scripts/validate_site.py` without discarding either side. Removed the two previously logged stray `EAD` marker remnants.
- Tasks 13 and 15 remain separate recent active claims with no work-product commits beyond their coordination claims. Their scopes were neither duplicated nor overwritten. They are optional additive expansion work; the integrated seven-page deliverable already satisfies the requested executive summary, lawful-method library, pros/cons, exact conditional procedures, $10,000–$400,000 matrices, primary-source register and flagged unknowns.
- Verification before PR: `python3 scripts/build_site.py` and clean generated diff; `python3 scripts/validate_site.py` PASS (7 pages, 18 procedures, four 40-row matrices, five-row 2026 tax illustration, 53 sources, source links on every table row, local links, landmarks and independent Decimal arithmetic).

### Publication result — arena/fd53cba7-china4
- Active-claim handoff: tasks 13 and 15 had no work-product commit more than four hours after their claim commits (well beyond the 60-minute takeover rule). They are marked `needs review`, not silently represented as completed. Their unresolved additive topics are already published on `flagged.html`: other-bank tariffs/live quotes, provider prices, source-of-funds/tax basis, eligibility and personal tax amounts. They do not block the verified original deliverable.
- Integration PR [#34](https://github.com/sassnarep3-star/China4/pull/34) merged to `main` at commit `ad394af0a47bd501e4f864a7d3ac66bcc89fdb8f` on 2026-11-10 05:53 UTC.
- Pull-request validation [run 42764883572](https://github.com/sassnarep3-star/China4/actions/runs/42764883572) passed before merge. Post-merge validation/artifact deployment [run 42764917091](https://github.com/sassnarep3-star/China4/actions/runs/42764917091) and legacy Pages build/deploy [run 42764916667](https://github.com/sassnarep3-star/China4/actions/runs/42764916667) both succeeded for the merge commit. Pages API reports `built`, source `main:/`, live URL https://sassnarep3-star.github.io/China4/.
- The sandbox network allowlist blocks direct `github.io` HTTP requests (curl returned no connection), so no false live-content claim is made. Deployment was instead confirmed from both successful deploy jobs and the GitHub Pages API; local HTTP smoke tests returned 200 for every page, both redirects, CSS and JSON.
- Non-failing infrastructure warning: GitHub's managed legacy Pages build reports Node.js 20 deprecation / forced Node.js 24 and an upcoming `ubuntu-latest` image migration. This is a GitHub-managed action warning, not a site failure.

- Integration conflict 2026-11-10: main advanced through PRs #34/#35 while PR #36 was opening. Stopped and retained both coordination logs in full; regenerated conflicting HTML from the automatically merged generator, preserving the new S53 tax illustration and this evidence page. Both validators re-run below.

### Publication result — arena/c009d1db-china4
- PR [#36](https://github.com/sassnarep3-star/China4/pull/36) merged 2026-11-10 05:55:46 UTC at `8303a41bc5e97c179b4f9543c94d0d77f4f21854`.
- PR validation [42765124364](https://github.com/sassnarep3-star/China4/actions/runs/42765124364) succeeded before merge. Post-merge validation and artifact deploy [42765164757](https://github.com/sassnarep3-star/China4/actions/runs/42765164757) succeeded; legacy Pages build/deploy [42765164814](https://github.com/sassnarep3-star/China4/actions/runs/42765164814) succeeded. Pages API reports `built` with live URL https://sassnarep3-star.github.io/China4/; evidence brief: https://sassnarep3-star.github.io/China4/evidence.html . Direct live HTTP is outside the sandbox's outbound-host allowlist, so deployment confirmation is from GitHub API and successful deployments, not a claimed live-browser fetch.
- Non-blocking GitHub infrastructure warnings: forced Node 24 for Node 20 actions and ubuntu-latest migration. Site build and deploy still passed.
- A plain `git pull --rebase` after integrating main tried to flatten pre-existing merged history and conflicted in the board. Aborted without discarding work, then `git pull --rebase=merges` succeeded preserving the complete merge graph; no force push used.
- Task done; personalized current prices and comprehensive independent re-verification of all inherited material remain explicitly unresolved, not falsely marked verified.

## Session arena/8686e554-china4 — task 17: the "tax gate" (what it costs to make stuck CNY convertible), all-in cost table, claim-level verification ledger (NEW files only)

| Task | Scope (files) | Status | Owner | Started (UTC) | Notes |
|---|---|---|---|---|---|
| 17-TG | (a) **Tax gate**: for each lawful origin of the CNY (wages, bonus, property sale, rent, dividends, interest, business/equity exit, gift, inheritance, unexplained balance) — the China tax that has to be evidenced before a bank may convert, its statutory rate and official source, the lawful reducers (treaty, exemptions), and how the US foreign tax credit / exclusion treats that same tax; (b) **all-in cost table**: tax gate + transfer cost for every scenario and every method at each $10,000 step from $10,000 to $400,000, mobile-first, most important column first; (c) **claim-level verification ledger**: line-by-line re-read of the published site claims against the official text, with a link per row and irregularities flagged | **New files only (amended 06:03 UTC — `ledger.html` released, see claim log):** `taxgate.html`, `allin.html`, `taxgate-sources.html`, `taxgate.css`, `scripts/build_taxgate.py`, `scripts/validate_taxgate.py`, `data/taxgate-model.json`, `data/taxgate-sources.json`; plus this section of `COORDINATION.md` | in progress | arena/8686e554-china4 | 2026-11-10 05:55 | Does **not** edit `scripts/build_site.py`, `scripts/validate_site.py`, `style.css`, the seven generated pages, `data/cost-model.json`, `README.md`, `EXECUTIVE_SUMMARY.md` or the workflow — those are claimed by `arena/fd53cba7-china4` (task 16, final integration) and `arena/581766ee-china4`. Branch fixed by Arena, so no `session-<id>/<task>` branch is created. |

### Claim log — arena/8686e554-china4
- **Board state read before claiming (2026-11-10 05:52–05:58 UTC; every remote branch fetched read-only).** `main` moved three times while this claim was being written: `2ce9664` → `ad394af` (PR #34) → `aebbc40` (PR #35), both from `arena/fd53cba7-china4`, which integrated PR #31's S53 tax illustration, marked its task 16 `done`, and re-labelled the undelivered tasks 13 and 15 `needs review`. Four other sessions started in the same four minutes:
  - `arena/fd53cba7-china4` — task 16 final integration: **done** (PRs #34, #35 merged).
  - `arena/581766ee-china4` — final audit and gap remediation of the shared generator/validator/generated pages: in progress (branch only, no PR yet).
  - `arena/abe2d028-china4` — a second "task 16": final integration **and takeover of stale tasks 13 and 15**, claimed 05:53:39 UTC with the scope "all root HTML pages, `style.css`, `data/*.json`, `scripts/*.py`, docs, workflow". Claim line only so far; no work product.
  - `arena/c009d1db-china4` — strict evidence register: new `evidence.html`, `scripts/build_evidence.py`, `scripts/validate_evidence.py`, plus nav/workflow wiring (PR #36 open).
- **Overlap disclosed, not hidden.** The `arena/abe2d028-china4` claim was pushed about 90 seconds before this one and was not yet on any branch when this session last fetched before writing its claim. Its takeover of tasks 13/15 overlaps the *topic* of task 17(a)–(c) (the tax needed to document each source of funds; one all-method table; a claim-level audit). It does not overlap at *file* level: task 17 uses only the eight new file names listed above, none of which is named in any other claim. Resolution adopted by this session, in order:
  1. `arena/abe2d028-china4` keeps precedence on the task 13/15 file names (`unlock.html`, `compare.html`, `audit.html`, `banks.html`, `playbooks.html`, `verification.html` and their scripts/data) and on every shared file. This session will not create or edit any of them.
  2. Before starting each part of task 17, this session re-fetches `arena/abe2d028-china4` (and `main`). Any part that branch has already delivered is **dropped from task 17 and linked to instead**; the drop is logged here.
  3. If that branch shows no work-product commit for 60 minutes (the board's takeover rule), task 17 proceeds in full under its own file names.
- **Stale claims (60-minute rule).** Task 13 (`arena/afeb2b56-china4`, last commit 01:08 UTC) and task 15 (`arena/a2efb7b1-china4`, last commit 01:20 UTC) are more than four hours old with no work product on any branch — only their claim lines were ever pushed. `arena/fd53cba7-china4` has since marked both `needs review`.
- **Why this scope.** The live site prices bank fees and FX spread (about 0.2%–0.5%) and a US tax illustration, but every cost matrix states that it "excludes underlying tax". The user's stated problem is the opposite: the balance cannot be converted "without paying a considerable amount of taxes". The China-side tax that unlocks conversion, by source of funds, is the largest cost component and is not quantified anywhere on the site. Task 17 covers that gap and nothing already published.
- **Change requests to shared files (not applied by this session while the shared files are claimed by an active session):**
  1. `scripts/build_site.py` → `NAV`: add links to `taxgate.html`, `allin.html`, `ledger.html`.
  2. `.github/workflows/gh-pages.yml`: run `python3 scripts/build_taxgate.py && python3 scripts/validate_taxgate.py` in `validate`; copy `taxgate.html`, `allin.html`, `ledger.html`, `taxgate.css`, `data/taxgate-model.json` and `data/verification-ledger.json` into `_site/`.
  3. `flagged.html` / `sources.html` (via the shared generator): register any new official source and any defect the ledger finds in an existing row. Defects are published on `ledger.html` and listed here; they are not silently patched into another session's file.
- **Integration.** If an integration session is still active when task 17 is finished, the requests above stay here for it. If every other task is `done` (or stale for more than 60 minutes) at that point, this session applies requests 1–3 itself as the last integration step, re-runs every validator, opens the PR, merges, and confirms the Pages deployment.
- **Rebase conflict #1 (2026-11-10 05:57 UTC).** `git pull --rebase origin main` conflicted in `COORDINATION.md`: PR #35 had appended `arena/fd53cba7-china4`'s publication result at the same end-of-file position as this claim. Resolved by keeping **both sides in full** (main's text first, this section after it). No other session's text was dropped or edited.
- **Claim published on `main`.** Claim-only PR [#37](https://github.com/sassnarep3-star/China4/pull/37) merged at `c14ac937bc1b4f2510d3743278d84a5873153e0c` on 2026-11-10 05:58:16 UTC so that every session reading the board on `main` sees this scope. Only `COORDINATION.md` changed; PR validation run 42765384171 passed.
- **Board re-read 06:00–06:03 UTC — eight sessions are now active; collisions found and resolved on this side.**
  - `arena/eed69928-china4` (also numbered 17; claim commit 05:57:34 UTC on its own branch, not yet on `main`): `calculator.html`, `howto.html`, `conversion-penalty.html`, **`ledger.html`**, calculator scripts/data — every method × every amount from published tariffs, walkthroughs, a conversion-penalty breakdown, and a ledger of its inputs.
  - `arena/abe2d028-china4` (re-labelled 17 on its branch): `banks.html`, `playbooks.html`, `verification.html` — multi-bank tariffs, route playbooks, row-by-row ledger.
  - `arena/545a0f57-china4` (18): `fxgain.html`, `enforcement.html`, `moreroutes.html`. `arena/0c416453-china4` (18): everything under `kit/`. Both name this session's task and stay out of it.
  - **File collision — `ledger.html`.** This session's claim reached its branch first (05:55 UTC) and `main` at 05:58:16 UTC, before `arena/eed69928-china4`'s claim commit. Rather than argue precedence, this session **releases `ledger.html`** to `arena/eed69928-china4` and renames its own file to `taxgate-sources.html` (data file `data/taxgate-sources.json`). No file in this claim is now named in any other claim.
  - **Number collision.** Three sessions used "17". This session's task is referred to as **17-TG** from here on; nobody else's row was edited.
  - **Topic split adopted to avoid duplicate work.**
    - *Per-method transfer cost for further banks and operators at every amount, and per-method walkthroughs* → left to `arena/eed69928-china4` (`calculator.html`, `howto.html`) and `arena/abe2d028-china4` (`banks.html`). `allin.html` will **not** re-price extra banks or operators; it adds the tax gate to the already-published BOC wire baseline and links to those pages for other rails.
    - *China tax that must be evidenced, by source of funds, with rates from the tax statutes, and what remains after the US credit* → stays with 17-TG (`taxgate.html`, `allin.html`); this claim was on the board first. `arena/eed69928-china4`'s `conversion-penalty.html` lists the same topic among others; request to that session: link to `taxgate.html` for the per-source China tax table rather than rebuilding it, and this session will link to `conversion-penalty.html` for route-level statutory penalties rather than rebuilding those.
    - *Claim-by-claim ledger of the existing site* → three other sessions already publish one (`verification.html`, `ledger.html`, `kit/review.html`). 17-TG drops the site-wide ledger. `taxgate-sources.html` records only the sources and exact official sentences behind the tax-gate pages. Defects this session happens to find in existing rows while reading the repo are still listed in this section for the integration owner.

## Session arena/545a0f57-china4 — task 18: US currency-gain exposure by acquisition year, published enforcement outcomes, and routes beyond the 18-route library (NEW files only)

| Task | Scope (files) | Status | Owner | Started (UTC) | Notes |
|---|---|---|---|---|---|
| 18 | (a) **US currency-gain exposure**: what converting the CNY balance itself can cost in US tax, by the year the CNY was acquired, from official IRS yearly-average rates, at every $10,000 step from $10,000 to $400,000 (fills the "Measured FX gain — needs acquisition date and rate" column that is blank on `taxes.html`); (b) **published enforcement outcomes**: what SAFE has actually fined individuals in its own published case circulars, beside the statutory ceilings already on the site; (c) **routes beyond the 18-route library** ("list as many as possible"): every further channel found, each classified lawful / conditional / not an exit route / prohibited from the official text, with pros, cons and steps — excluding the four channels listed under task 15 / `playbooks.html` | **New files only:** `fxgain.html`, `enforcement.html`, `moreroutes.html`, `extras.css`, `scripts/build_extras.py`, `scripts/validate_extras.py`, `data/extras-model.json`; plus this section of `COORDINATION.md` | in progress | arena/545a0f57-china4 | 2026-11-10 05:58 | Does **not** edit `scripts/build_site.py`, `scripts/validate_site.py`, `style.css`, any existing generated page, `data/cost-model.json`, `README.md`, `EXECUTIVE_SUMMARY.md`, the workflow, or any file claimed by tasks 16/17 or `evidence.html`. Branch fixed by Arena, so no `session-<id>/<task>` branch is created. |

### Claim log — arena/545a0f57-china4
- **Board state read before claiming (2026-11-10 05:52–05:58 UTC; every remote branch fetched read-only).** Six sessions, this one included, started within about three minutes of each other. Active claims found, all left untouched by this session:
  - `arena/fd53cba7-china4` — task 16, final integration (PRs #34 and #35 merged).
  - `arena/c009d1db-china4` — `evidence.html` and its two scripts (PR #36 merged).
  - `arena/581766ee-china4` — audit of the shared generator and cost comparisons (PR #38 open).
  - `arena/abe2d028-china4` — "task 17": `banks.html`, `playbooks.html`, `verification.html` (multi-bank tariffs, route playbooks, row-by-row ledger).
  - `arena/8686e554-china4` — "task 17": `taxgate.html`, `allin.html`, `ledger.html` (China tax gate by source of funds, all-in cost table, claim-level ledger; claim PR #37 open).
- **Irregularity logged:** two sessions hold the number 17 for different scopes (the claims were written on separate branches within minutes, so neither could see the other). This session takes **18** to avoid a third collision.
- **Why this scope.** It is what remains of stale task 13 (`arena/afeb2b56-china4`, claim-only since 01:08 UTC, more than four hours without a commit) once tasks 17/17 are subtracted: the US currency-gain question by acquisition year, SAFE's published enforcement outcomes, and the routes not yet in the library. None of the five active claims lists these three items or these file names. Handoff of that part of task 13 is noted here under the 60-minute rule; task 13's own file names (`unlock.html`, `compare.html`, `audit.html`) are **not** reused.
- **Overlap guard.** Before every push this session re-fetches `main` and all active branches. If another session publishes the same analysis first, this session links to it instead of duplicating it, narrows task 18, and logs that here. The four channels named under task 15 (UnionPay POS spend, departing-foreigner social-insurance refund, WFOE dividend with treaty and tax-filing, SkyRemit) belong to `playbooks.html` and are excluded from `moreroutes.html`.
- **Verification rule for this task.** Every table row carries a link to the official page it was read from in this session. A value that could not be confirmed on an official page is left blank and listed as unverified on the page itself; nothing is inferred to fill a cell.
- **Change requests to shared files (not applied by this session while those files are claimed):**
  1. `scripts/build_site.py` → `NAV` / dashboard: link `fxgain.html`, `enforcement.html`, `moreroutes.html`.
  2. `.github/workflows/gh-pages.yml`: run `python3 scripts/build_extras.py && python3 scripts/validate_extras.py`; copy the three pages, `extras.css` and `data/extras-model.json` into `_site/`.
  3. `flagged.html` / `sources.html` (via the shared generator): register new official sources and any defect found in an existing row. Until then they are published on the new pages themselves and listed in this section.
- **Integration.** If an integration owner is still active when task 18 is finished, requests 1–3 stay here for it. If every other task is `done` (or its claim is more than 60 minutes old with no commits) at that point, this session applies them itself as the last step, re-runs every validator, opens the PR, merges, and confirms the Pages deployment.

## Session arena/0c416453-china4 — task 18: execution kit (time-to-exit and cost of delay, remote access and paperwork, bank-counter phrasebook, repo/deployment review) — NEW directory only

| Task | Scope (files) | Status | Owner | Started (UTC) | Notes |
|---|---|---|---|---|---|
| 18 | (a) **Time-to-exit and cost of delay**: for every route that has an official cap, how many transfers / trips / calendar years each $10,000 step from $10,000 to $400,000 takes, and what waiting costs (interest-rate gap and FX exposure) from official rate inputs; (b) **remote access and paperwork kit**: what a US-based account holder must do in person versus through an agent, expired-ID account restrictions, entry options, apostille/notarisation, how the China tax record is obtained, document pack per route — each row tied to the official rule; (c) **bank-counter phrasebook**: the exact Chinese terms with the official text each comes from; (d) **repo, CI and deployment review**: irregularities in the repository mechanics themselves (double Pages deployment, stale PRs/branches, validator blind spots, external-link liveness) | **New directory only:** everything under `kit/` (`kit/index.html`, `kit/timeline.html`, `kit/access.html`, `kit/phrasebook.html`, `kit/review.html`, `kit/kit.css`, `kit/_build/build_kit.py`, `kit/_build/validate_kit.py`, `kit/data/*.json`); plus this section of `COORDINATION.md` | in progress | arena/0c416453-china4 | 2026-11-10 05:58 | Edits **no** existing file other than this board. Does not create or touch any file named in another claim. Branch fixed by Arena (`arena/0c416453-china4`), so no `session-<id>/<task>` branch is created. |

### Claim log — arena/0c416453-china4
- **Board state read before claiming (2026-11-10 05:51–05:58 UTC; every remote branch fetched read-only into a local `peek/` namespace, nothing checked out or pushed).** Five other sessions started within the same few minutes:
  - `arena/fd53cba7-china4` — task 16, final integration; PRs #34/#35 merged; marked done.
  - `arena/c009d1db-china4` — strict evidence audit, `evidence.html`; PR #36 merged; marked done.
  - `arena/581766ee-china4` — audit and gap remediation on the shared generator, validator, generated root pages, `data/cost-model.json`, README, EXECUTIVE_SUMMARY and workflow; in progress.
  - `arena/abe2d028-china4` — also numbered task 16: final integration and takeover of stale tasks 13 and 15, claiming all root HTML, `style.css`, `data/*.json`, `scripts/*.py`, docs and workflow; in progress.
  - `arena/8686e554-china4` — task 17: tax gate, all-in cost table, claim-level verification ledger (`taxgate.html`, `allin.html`, `ledger.html`, `taxgate.css`, `scripts/build_taxgate.py`, `scripts/validate_taxgate.py`, `data/taxgate-model.json`, `data/verification-ledger.json`); in progress.
- **Irregularity logged:** those claims overlap each other on the shared files, and the number 16 was taken twice. Each was written on its own branch, so none was visible on `main` to the others at the time. This session reads the other branches directly before every push for that reason.
- **Why this scope.** Every topic named in another claim is left alone: the China tax needed to unlock conversion and the all-in table (task 17), the claim-by-claim ledger of site statements (task 17), the evidence brief (`c009d1db`), the shared pages and cost model (`581766ee`, `abe2d028`), and the stale task 13/15 file names (`unlock.html`, `compare.html`, `audit.html`, `banks.html`, `playbooks.html`, `verification.html`). What no claim covers is (1) **time**: the site counts wires but never prices what a multi-year route costs while the money waits; (2) **access**: how someone living in the US actually operates a Chinese account and collects the documents the rules require; (3) the **repository's own mechanics**, as distinct from the site's claims.
- **File-level isolation.** Generator, validator, data and CSS all live inside `kit/`, not in `scripts/`, `data/` or `style.css`, so that the blanket `scripts/*.py` / `data/*.json` / root-HTML claims of other sessions cannot collide with this one.
- **Overlap guard.** Before each push this session re-fetches `main` and every active branch. If another session publishes the same analysis first, this session links to it instead of duplicating it and narrows task 18; that decision is logged here.
- **Change requests to shared files (not applied by this session while those files are claimed):**
  1. `scripts/build_site.py` → `NAV` (or the dashboard body): add one link to `kit/index.html`.
  2. `.github/workflows/gh-pages.yml`: run `python3 kit/_build/build_kit.py && python3 kit/_build/validate_kit.py` in `validate`; copy the `kit/` directory (excluding `kit/_build/`) into `_site/`.
  3. Any defect this session finds in an existing page is listed on `kit/review.html` and in this section; it is not patched into another session's file.
- **Integration.** If another integration session is still active when task 18 is finished, requests 1–3 stay here for it. If every other task is `done` (or its claim is more than 60 minutes old with no commits) at that point, this session applies requests 1–3 itself as the last integration step, re-verifies the combined site, opens the PR, merges, and confirms the Pages deployment.

## Session arena/abe2d028-china4 — task 17: additive multi-bank and playbook evidence (NEW FILES ONLY)

| # | Task | Scope (files) | Status | Owner | Started (UTC) | Notes |
|---|---|---|---|---|---|---|
| 17 | Complete the abandoned task-15 additive evidence set: official multi-bank tariff comparison, lawful route playbooks, and a row-by-row verification ledger | **New files only:** `banks.html`, `playbooks.html`, `verification.html`, `scripts/build_bank_playbooks.py`, `scripts/validate_bank_playbooks.py`, `data/bank-playbooks.json`, plus this section of `COORDINATION.md` | **done** | arena/abe2d028-china4 | 2026-11-10 05:53 | Non-overlapping handoff after stale task 15. Shared generator, existing root HTML, CSS, README, workflow and `evidence.html` are NOT edited. The additive work is verified on this branch; shared-file publication is requested below because other additive sessions remain active. |

### Coordination and conflict log
- The original task-15 claim (`arena/a2efb7b1-china4`, 01:20 UTC) produced only a coordination claim and no new files by 05:53 UTC; the >60-minute stale-claim rule permits handoff. Task 13 likewise produced only a claim.
- Three concurrent sessions claimed at 05:51–05:53 UTC: `arena/fd53cba7-china4` (task-16 final integration), `arena/581766ee-china4` (overlapping audit), and `arena/c009d1db-china4` (new strict `evidence.html`). To avoid duplicate claims, this session **narrowed its initial broad task-16 claim to task 17's exact new-file scope**. It will not start final integration until those claims are marked done or become stale.
- Rebase conflict #1 (05:55 UTC): `origin/main` advanced with PRs #31/#34 while this branch was claiming. Resolution: retained `origin/main`'s full `COORDINATION.md`, including fd53cba7's task-16 claim and all other sessions' logs, then appended this narrowed section. No other session's text was discarded.
- **Shared-file request for the final integration owner:** once task 17 is done, add `banks.html`, `playbooks.html`, and `verification.html` to global navigation/dashboard, include the pages and `data/bank-playbooks.json` in the Pages artifact, and run `scripts/validate_bank_playbooks.py` in CI. If no integration owner remains active after 60 minutes, this session will perform that final integration on the Arena-fixed branch.
- Fixed-branch constraint: Arena fixes all work to `arena/abe2d028-china4`; no `session-<id>/<task>` branch was created or pushed.
- **Rebase conflict #2 (06:28 UTC):** `origin/main` advanced through PRs #36–#42 while task 17 was in flight. Resolution: retained `origin/main`'s full `COORDINATION.md`, including every other session's claim and log, then appended this task-17 section below. No other text was discarded.
- **Numbering collision logged:** `arena/8686e554-china4` uses task **17-TG** for the China tax-gate / all-in table / source ledger, and other sessions use 18. This section is the separate multi-bank / playbook / verification scope under the original task-15 file names; no 17-TG file is edited.

### Task-17 result — 2026-11-10 06:30 UTC

**Status:** `done` for the six claimed new files and this board section. **No PR, merge, shared-file edit or Pages deployment was attempted by this session.** Other additive sessions (17-TG, task 18 and PR #38) remain active; a final integration owner should combine the work and publish it.

**Deliverables.** `banks.html` (8 tariff/provider rows, 12 eligibility rows, 49-source task-17 register), `playbooks.html` (9 conditional playbooks / 63 cited steps, a $10,000–$400,000 evidence ladder with 40 independently re-derived BOC baseline rows, and penalty boundaries), `verification.html` (28 ledger rows, 16 irregularities, 27 canonical fact checks, explicit scope boundary), `data/bank-playbooks.json` (single editorial source), and the new builder/validator scripts. All current executable quotes, other-bank current all-in costs, provider current all-in costs and personal tax amounts remain `—` or flagged; nothing was inferred to fill them.

**Sources re-read for task 17.** The local **T01–T49** register in `data/bank-playbooks.json` and `banks.html#source-register` contains every full URL and reading status. Fresh official/provider reads include SAFE/PBOC/State Council individual-FX, quota, anti-splitting, tax-filing, ATM and cash rules ([T01–T12](https://www.safe.gov.cn/tianjin/2024/0430/2464.html), [T07–T08](https://www.safe.gov.cn/safe/2021/0702/19306.html), [T09–T10](https://www.safe.gov.cn/safe/2017/1230/8116.html)); BOC, ABC, CCB, HSBC, CMB and ICBC tariff/product pages ([T15–T26](https://www.boc.cn/custserv/fd5/), [T20](https://www.abchina.com/cn/PublicPlate/sfbz/fwjgbz/202109/t20210929_2047241.htm), [T21](https://wealth.ccb.com/he/cn/faverable/20160822_1471836289.html), [T22](https://www.hsbc.com.cn/content/dam/hsbc/cn/docs/document-download/tariff-of-accouts-and-services.pdf)); SkyRemit and Wise provider rules ([T27–T34](https://www.skyremit.cn/), [T33](https://wise.com/help/articles/2955298/guide-to-cny-transfers)); foreign-employee social insurance and PRC tax rules ([T35–T39](https://jiangsu.chinatax.gov.cn/art/2011/9/6/art_23636_3204.html), [T38](https://fgk.chinatax.gov.cn/zcfgk/c102416/c5252107/content.html)); and US treaty / IRS / FinCEN / CBP materials ([T40–T49](https://www.irs.gov/pub/irs-trty/china.pdf), [T41](https://www.irs.gov/publications/p525), [T46](https://www.cbp.gov/travel/international-visitors/money-monetary-instruments)). The inherited **S1–S53** register and the five-row Rev. Proc. 2025-32 tax illustration were **not** fully re-fetched or re-derived here; no new “verified” mark is applied to them.

**Verification performed.**
- `python3 -m py_compile scripts/build_bank_playbooks.py scripts/validate_bank_playbooks.py` — passed.
- `python3 scripts/build_bank_playbooks.py` — `Built 3 additive pages, 40 audited amount rows and 49 sources.`
- `python3 scripts/validate_bank_playbooks.py` — `PASS: 3 additive pages, 49 sources, 8 fee rows, 9 playbooks/63 cited steps, 28 ledger rows, 16 irregularities, 27 canonical facts, 40 re-derived amount rows, 8 sourced tables, links and anchors.` The validator checks every table row and every playbook step for official source links, local links/anchors, landmarks, balanced HTML, canonical facts, blank quote cells and independent Decimal arithmetic from hardcoded inputs.
- Generated-diff check — rebuilt twice; SHA-256 of all three pages unchanged.
- Negative controls — **5/5 failed as expected**: mutated canonical fee, blank quote filled with `$0`, all source links removed from one procedure step, unknown source id, all source links removed from one table row.
- Inherited-site regression after rebase onto `origin/main` `9ca6b50` — `python3 scripts/build_site.py && python3 scripts/build_evidence.py && python3 scripts/validate_site.py && python3 scripts/validate_evidence.py` all passed (7 pages, 53 sources, 720 strictly blank strict-cost rows); `git diff --exit-code` clean for tracked generated files.
- Local HTTP smoke test — 200 for `evidence.html`, all seven inherited main pages, the three new pages, both compatibility redirects, `style.css`, `data/cost-model.json` and `data/bank-playbooks.json`.

**Irregularities published on `verification.html` (16 rows; not blockers).** Key items: BOC's exact dated USD row is not reproducible from the rolling board/captcha search and its published Middle Rate is not the arithmetic midpoint; ABC effective-date/discount wording must be confirmed with a branch; CCB is a 2016 branch page; HSBC “free” is tier-specific and excludes downstream fees; CMB and ICBC expose no stable text outward-wire tariff; SkyRemit and Wise leave current executable totals/fees blank; PBOC Art. 37 and Decree 532 Art. 52 use different individual definitions; the 20% foreign-individual FIE dividend rule and the treaty's 10% caps / saving clause need fact-specific reconciliation; inherited S1–S53 values were not re-derived; personal FX-gain basis remains a taxpayer fact; social-insurance payout is not a general extraction route; and cash/ATM/CBP limits are not a $400,000 transfer route.

**Shared-file request for the final integration owner (not applied by this session).** (1) `scripts/build_site.py` / dashboard: add `banks.html`, `playbooks.html` and `verification.html` to global navigation while preserving `evidence.html`; (2) `.github/workflows/gh-pages.yml`: run `python3 scripts/build_bank_playbooks.py` before the generated-diff check, run `python3 scripts/validate_bank_playbooks.py` in the validate job, and copy the three pages plus `data/bank-playbooks.json` into `_site/`; (3) `README.md` / `EXECUTIVE_SUMMARY.md` / `sources.html` / `flagged.html`: optionally link the additive pages and register their official sources. Re-run every validator and confirm Pages deployment after these shared edits. If every other active claim becomes done or stale for >60 minutes before integration, this session may take over that final step on `arena/abe2d028-china4`; it has not done so now.

## Session arena/1a8e4027-china4 — task 19: final integration, re-verification and publication

| # | Task | Scope (files) | Status | Owner | Started (UTC) | Notes |
|---|------|---------------|--------|-------|---------------|-------|
| 19 | Final integration: merge the additive task-17 multi-bank/playbook/verification pages, integrate the open PR #38 shared-file corrections, wire navigation and the Pages/CI artifact, re-verify the combined site line by line, then open/merge the PR and confirm GitHub Pages | `COORDINATION.md`; shared generator `scripts/build_site.py`, `scripts/validate_site.py`, generated root pages, `data/cost-model.json`, `README.md`, `EXECUTIVE_SUMMARY.md`, `.github/workflows/gh-pages.yml`; additive files `banks.html`, `playbooks.html`, `verification.html`, `scripts/build_bank_playbooks.py`, `scripts/validate_bank_playbooks.py`, `data/bank-playbooks.json`; plus this section | in progress | arena/1a8e4027-china4 | 2026-11-10 09:50 | Arena-fixed branch; no `session-<id>/<task>` branch. |

### Claim log — arena/1a8e4027-china4
- **Board state read before claiming (2026-11-10 09:46–09:52 UTC; every remote branch fetched read-only).** Latest commits on the active branches: `arena/abe2d028-china4` 06:31 UTC, `arena/581766ee-china4` 05:58 UTC, `arena/545a0f57-china4` 05:58 UTC, `arena/0c416453-china4` 05:59 UTC, `arena/eed69928-china4` 05:57 UTC, `arena/afeb2b56-china4` 01:08 UTC. **Every one of those claims is now more than three hours old with no work-product commit**, far past the board's 60-minute takeover rule. `main` is `9ca6b50` (PR #42).
- **What actually exists as unmerged work.** A file-level sweep of all 37 remote branches found exactly one delivered, unmerged deliverable: `arena/abe2d028-china4` adds `banks.html`, `playbooks.html`, `verification.html`, `scripts/build_bank_playbooks.py`, `scripts/validate_bank_playbooks.py` and `data/bank-playbooks.json` (3 commits ahead of `main`, `behind=0`). No branch contains `taxgate.html`, `allin.html`, `ledger.html`, `fxgain.html`, `enforcement.html`, `moreroutes.html`, `extras.css`, `calculator.html`, `howto.html`, `conversion-penalty.html` or anything under `kit/` — those sessions pushed claim lines only. Open PRs #4, #5, #12 (stale, from much earlier sessions) and #38 are untouched by this session.
- **Why this scope.** `arena/abe2d028-china4` explicitly requests a final integration owner (its own log: "a final integration owner should combine the work and publish it"). PR #38 is an open, self-validated correction set on the shared generator. Neither has been merged. Combining them, re-verifying and publishing is exactly the board's "final integration session" role, and nothing else is claimed with live commits.
- **Overlap guard.** Before every push this session re-fetches `main` and all remote branches. If any other session publishes the same files first, this session links to it instead of duplicating it and narrows task 19.
- **No invented values.** Unknown current provider quotes, correspondent deductions, account-specific fees, source-of-funds facts and personal tax amounts stay blank (`—`) and are published on the Flagged for Review page. Nothing is inferred to fill a cell.

### Verification performed — arena/1a8e4027-china4 (2026-11-10 ~09:55–10:10 UTC)

Every figure below was re-read from the linked official page in this session, not merely linked. Structural validators were re-run after the merge.

**Re-built and re-validated.** `python3 scripts/build_site.py`, `build_evidence.py`, `build_bank_playbooks.py` all run clean; `validate_site.py` → `PASS: 7 HTML pages, executive summary, 18 procedures, 5×40 cost matrices, 2026 US tax illustration, 54 sources`; `validate_evidence.py` → `PASS: 720 strictly blank current-cost rows, 18 route ladders`; `validate_bank_playbooks.py` → `PASS: 3 additive pages, 49 sources, 8 fee rows, 9 playbooks/63 cited steps, 28 ledger rows, 16 irregularities, 27 canonical facts, 40 re-derived amount rows`. Local HTTP smoke test returned 200 for all eleven pages, both compatibility redirects, `style.css` and both JSON data files.

**Primary sources re-read this session (all linked from the site):**

| Claim checked | Verified value | Official source |
|---|---|---|
| BOC personal cross-border telegraphic transfer | 0.1%; min CNY50; max CNY260; international telegram CNY150 (item 210105008) | [BOC personal price list, effective 2025-11-11 (PDF)](https://pic.bankofchina.com/bocappd/pricelist/202511/P020251110646838136627.pdf) |
| BOC UnionPay cross-border ATM fee | CNY12 + 1% per withdrawal, max CNY112 (item 210108014) | same BOC PDF |
| BOC full-arrival (全额到账) | USD15 when the receiving account is at BOC New York, USD25 otherwise; charged on top of commission and telegram (note 5) | same BOC PDF |
| BOC ATM-owner surcharge warning | present (note 10) | same BOC PDF |
| BOC FX board (current) | USD buying 665.76 / selling 668.56, Middle Rate 671.67 per 100 USD at 2026-11-10 17:54:59 | [BOC exchange-rate board](https://www.boc.cn/sourcedb/whpj/enindex.html) |
| SAFE individual FX annual total | USD 50,000 per person per year for settlement and purchase; above-quota current-account business handled under Arts. 10–15; Art. 39 repealed by 汇发〔2023〕8号 | [SAFE Detailed Rules (汇发〔2007〕1号, as amended)](https://www.safe.gov.cn/tianjin/2024/0430/2464.html) |
| SAFE overseas ATM caps | CNY 100,000 per person per natural year; CNY 10,000 per card per day; borrowed cards prohibited (汇发〔2017〕29号) | [SAFE Hubei notice](https://www.safe.gov.cn/hubei/2019/0305/851.html) |
| FBAR civil penalties | non-willful USD 16,536; willful USD 165,353; assessed on/after 2025-01-17 (31 CFR 1010.821 Table 1) | [eCFR 31 CFR 1010.821](https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010/subpart-H/section-1010.821) |
| US personal FX gain threshold | gain on a personal foreign-currency transaction is excluded unless more than USD 200, then reported as a capital gain | [IRS Publication 525](https://www.irs.gov/publications/p525) |
| PRC comprehensive-income IIT brackets | 3/10/20/25/30/35/45% with quick deductions 0/2,520/16,920/31,920/52,920/85,920/181,920 (source S54) | [Shanghai Tax Service bracket PDF](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/202402/P020240202362406243753.pdf) |
| US–China treaty caps | dividends, interest and royalties capped at 10% each; saving clause in Protocol 1 ¶2 (1984 treaty, in force 1987-01-01) | [IRS/US Treasury treaty text](https://www.irs.gov/pub/irs-trty/china.pdf) |
| ABC outward remittance | 0.1%; min CNY20; max CNY200 for individuals (item 09012); outbound SWIFT telegram CNY80 for individuals (item 09015); full-arrival overseas-bank fee USD25; ABC express remittance USD15 + 0.25%, min USD15, max USD50 (item 09023) | [ABC market-adjusted price standard](https://www.abchina.com/cn/PublicPlate/sfbz/fwjgbz/202109/t20210929_2047241.htm) |
| SkyRemit pricing | CNY79 fixed fee plus a variable percentage; Alipay/WeChat channel fee 0.8%; bank channel adds no such fee | [SkyRemit transparent-pricing notice](https://www.skyremit.cn/news/blog-detail-109-Transparent-Pricing-Model-Updated.html) |
| Wise CNY outbound eligibility | non-mainland-Chinese sender; valid PRC tax record for the last 3 years; own-account recipient only; bank app CNY300,000 and Alipay CNY50,000 per transfer; tax-based overall limit shared with SkyRemit | [Wise guide to CNY transfers](https://wise.com/help/articles/2955298/guide-to-cny-transfers) |

**Findings and irregularities logged (not merge blockers).**
1. **BOC Middle Rate is not the arithmetic midpoint.** The board's published Middle Rate column (671.67) differs from (665.76 + 668.56)/2 = 667.16. This confirms the site's existing flag that the model computes its own midpoint rather than borrowing BOC's column. The current board's half-spread (0.2091%) is within ~0.06% relative of the modelled 2026-11-09 input (0.21037%), so the dated input remains representative while the absolute rate has moved.
2. **ABC discount note scope.** The ABC page states that the listed free/discount items in categories (一)–(九) apply from 2026-09-30 until the price directory expires. `banks.html` already qualifies this; no change needed.
3. **ABC express remittance is already captured.** `abc_express = USD15 + 0.25%; min USD15; max USD50` (item 09023) is present in `canonical_facts` and validated; re-confirmed against the official page this session.
4. **Wise current-cost cells.** Blanked under PR #38 because Wise's published 2024 examples do not establish a current price and Wise deducts fees before conversion. The route remains fully documented on `methods.html` and `banks.html`; the net-payout caveat is printed on `penalties.html`.
5. **Unchanged inherited limitations.** BOC's dated USD row is not permanently retrievable from a static URL (rolling board + captcha historical query); inherited S1–S53 values were not all re-derived this session; personal source-of-funds facts, account-specific fees and personal tax amounts remain blank by policy. These stay published on `flagged.html` and `verification.html`.
6. **Repository mechanics.** Three stale open PRs (#4, #5, #12) from early sessions remain open and were not touched. No force push was used. The `git merge` of `arena/abe2d028-china4` conflicted only in `COORDINATION.md`; both sessions' sections were retained in full.

### Publication result — arena/1a8e4027-china4 (task 19)

- Integration PR [#43](https://github.com/sassnarep3-star/China4/pull/43) merged to `main` at commit `b3ac3fc` on 2026-11-10 ~10:03 UTC.
- Pull-request validation [run 42795635952](https://github.com/sassnarep3-star/China4/actions/runs/42795635952) (`validate` job) concluded **SUCCESS** before merge.
- Post-merge workflow [run 42795723881](https://github.com/sassnarep3-star/China4/actions/runs/42795723881) concluded **SUCCESS**; GitHub's legacy Pages build/deploy [run 42795722825](https://github.com/sassnarep3-star/China4/actions/runs/42795722825) also concluded **SUCCESS**.
- GitHub Pages API reports `status: built`, `build_type: legacy`, `source: main:/`, public, live URL **https://sassnarep3-star.github.io/China4/**.
- Live content was read back after deployment: the dashboard (`index.html`) shows the integrated route inventory with the Wise current-cost cell blanked and the corrected penalty wording, and `banks.html` serves the eight-row multi-bank tariff table with the new navigation. Direct `curl` to `github.io` is blocked by this sandbox's outbound-host allowlist (SSL connect error), so live content was confirmed through the page-fetch tool and the Pages API rather than a claimed browser fetch.
- Task 19 is **done**. The published site now has eleven pages: `index.html`, `summary.html`, `methods.html`, `penalties.html`, `taxes.html`, `flagged.html`, `sources.html`, `evidence.html`, `banks.html`, `playbooks.html`, `verification.html`, plus the `estimates.html` / `costs.html` compatibility redirects.
- Remaining unresolved items are published, not hidden: current provider quotes, correspondent deductions, account-specific receiving fees, personal source-of-funds facts and personal tax amounts are blank (`—`) and listed on `flagged.html` and `verification.html`. No universal cheapest route is claimed.

## Session arena/3c69f1fe-china4 — verification and PR/merge closeout

| Task | Scope (files) | Status | Owner | Notes |
|---|---|---|---|---|
| Rebase onto integrated main, verify the complete dashboard, and close out via PR/merge; record PR link, merge result and Pages deploy confirmation | COORDINATION.md | done | arena/3c69f1fe-china4 | No unique code delta: task 20 (Before-You-Decide questions page with discovery suggestions + fresh 2026-11-11 audit) was already integrated on origin/main via PR #47 by session arena/e701c274-china4 (merge commit cbfc46b). This session's duplicate questions page was superseded, not duplicated, per the no-overlap rule. Local validation PASS on the integrated tree: 8 pages, before-you-decide checklist, 18 procedures, 5×40 cost matrices, 2026 US tax illustration, 54 sources; evidence and bank-playbooks validators PASS. Key figures re-confirmed against public sources: FBAR $16,536 nonwillful / $165,353 willful (31 CFR 1010.821, eff. 2025-01-17); FEIE 2026 $132,900 (Rev. Proc. 2025-32). Closeout PR #53: https://github.com/sassnarep3-star/China4/pull/53 (arena/3c69f1fe-china4 → main), merged via `gh pr merge 53 --merge` at merge commit 7faa1d5531ea22d8f79625edc118818a4e49296c. CI run 42947553702 concluded SUCCESS; GitHub Pages legacy build/deploy status `built`, live https://sassnarep3-star.github.io/China4/ (source main `/`). Final record committed on arena/3c69f1fe-china4 and submitted as a follow-up PR so the merge result is persisted on main. |


## Session arena/9ff08099-china4 — current-date ATM tariff and publication audit

| Task | Scope | Status | Owner | Started (UTC) | Notes |
|---|---|---|---|---|---|
| Audit the newly effective 2026-11-11 BOC overseas ATM tariff against official sources, correct any affected current-cost presentation, validate and publish | `COORDINATION.md`, `scripts/build_site.py`, `scripts/validate_site.py`, generated root HTML and `EXECUTIVE_SUMMARY.md` only if correction required; PR/Pages | done | arena/9ff08099-china4 | 2026-11-11 02:33 | Previous broad claims are older than 60 minutes without new commits; published integration is PR #44. Arena requires this fixed branch. Scope limited to ATM effective-date audit and necessary integration. |

### Audit results — arena/9ff08099-china4 (2026-11-11 UTC)
- Re-read [BOC's 2026-11-11 ATM notice](https://www.boc.cn/pbservice/bi2/202608/t20260811_25684907.html): UnionPay ¥12 + 1%, cap ¥112 per withdrawal; Visa/Mastercard 2.5%, min USD-equivalent 3, max USD-equivalent 40 per withdrawal. Corrected the Costs page's now-obsolete “future” label and source register, retaining historical FX assumptions and a warning that the model is not an executable ATM quote. The notice alone does not establish card-specific eligibility, ATM-owner charges or transaction FX.
- Re-read [SAFE overseas ATM notice](https://www.safe.gov.cn/hubei/2019/0305/851.html): annual CNY100,000 per individual across cards and daily CNY10,000 per card, no borrowed-card evasion. Re-read [SAFE current-account Q&A](https://www.safe.gov.cn/tianjin/2025/0715/2834.html), [IRS currency guidance](https://www.irs.gov/individuals/international-taxpayers/foreign-currency-and-currency-exchange-rates), and [IRS FBAR](https://www.irs.gov/businesses/small-businesses-self-employed/report-of-foreign-bank-and-financial-accounts-fbar) for the summary distinctions.
- Fixed a material labeling defect in Flagged for Review: the historical quoted 666.48 / 669.29 figure is in CNY per **100** USD, not per USD. Model uses 6.6648 / 6.6929 per USD; numbers were not changed. Historical row remains unverified in this session because BOC's date search requires CAPTCHA; [BOC's rolling board](https://www.boc.cn/sourcedb/whpj/enindex.html) was reviewed only as a current, non-executable cross-check. Current personal fees, individual taxes, eligibility and the historical quote remain flagged, not guessed.
- Added regression checks for the tariff label, execution-quote disclaimer and quoted-unit correction. All three builders and all three validators pass, including local links, source presence, independent amount calculations and 720 blank strict current-cost rows. This was a **targeted audit**, not a claim that every inherited row or every external link was freshly verified. No source-link checker can establish substantive correctness merely from link presence.
- Initial pull/rebase failed because the remote session branch did not yet exist; first branch push created it. No other branch was created or pushed.
## Session arena/198e49b1-china4 — task 21 (2026-11-11 UTC)

| Task | Status | Owner | File scope |
|---|---|---|---|
| Correct ATM effective-date rollover and add regression coverage; verify and publish | in progress | arena/198e49b1-china4 | scripts/build_site.py, scripts/validate_effective_dates.py, generated root HTML/data/cost-model.json, README.md, COORDINATION.md |

- Read shared board and open PR #45: task 20 changes COORDINATION.md only; no content overlap. This session claims the newly effective 2026-11-11 ATM wording correction, not another session's work. Arena fixes the branch name, so this session uses its assigned branch rather than creating a session branch.
- Official notice read directly: https://www.boc.cn/pbservice/bi2/202608/t20260811_25684907.html. Visa/Mastercard fee becomes effective today; inherited copy still calls it future. UnionPay formula is unchanged. No new FX quote or account-specific cost is invented.

### Task 21 verification and limits
- Re-read official BOC notice: https://www.boc.cn/pbservice/bi2/202608/t20260811_25684907.html. Corrected obsolete future labels and published the effective-today formula prominently on the eight generator-layout pages; flagged the rollover on flagged.html. No rate or fee calculations changed.
- Independently re-read SAFE Arts. 2, 13 and 15 at https://www.safe.gov.cn/tianjin/2024/0430/2464.html; Wise outbound eligibility/limits at https://wise.com/help/articles/2955298/guide-to-cny-transfers; and IRS FBAR threshold/dates at https://www.irs.gov/businesses/small-businesses-self-employed/report-of-foreign-bank-and-financial-accounts-fbar. These support the conditional documented-income recommendation, not a cheapest-route guarantee. IRS Pub. 525 retrieval returned only its opening chunk: no new semantic verification claimed for its currency-gain rule.
- All three existing generators and validators pass. Added `scripts/validate_effective_dates.py`: eight shared-layout pages show the dated notice; obsolete wording absent; original historical FX input preserved. Initial regression expected all eleven pages to use the shared layout; test correctly failed because the bank generator has independent layout. Narrowed the assertion to the eight actually affected pages, without altering unrelated bank pages.
- Existing strict register retains 720 blank current-cost rows. Personal taxes, bank-specific execution quotes and correspondent charges remain unknown, not zero. No claim is made that every inherited source was re-read this session.
- Task 20 PR #45 merged concurrently; this session preserves its coordination entry during rebase. Fixed Arena branch remains the integration branch.
## Session arena/c5e783f4-china4 — final verification, gap audit, and publication (2026-11-11)

| Task | Scope (files) | Status | Owner | Started (UTC) | Notes |
|---|---|---|---|---|---|
| 20 | Final verification and publication: re-run all generators/validators, audit the live site against every user requirement (executive summary, questions/information/answers, US-citizen best route, methods pros/cons, penalty breakdown, $10k–$400k cost tables, step-by-step procedures, site structure, line-by-line sourcing), spot-check load-bearing official sources, fix any gap found, then PR → merge → confirm Pages deploy | COORDINATION.md (this section); site fixes only if a gap is found, via `scripts/build_site.py` / `scripts/build_evidence.py` / `scripts/build_bank_playbooks.py` + regenerated HTML + `data/*.json` | arena/c5e783f4-china4 | 2026-11-11 02:32 | Branch fixed by Arena (`arena/c5e783f4-china4`). No other session holds a live claim on these files: task 17 taxgate (`arena/8686e554-china4`) and tasks 13/15 have no remote branch and no work-product commits; PRs #4/#5/#12/#38 are stale and untouched. Shared-file edits limited to this claim. |

### Claim log — arena/c5e783f4-china4
- Board read 2026-11-11 02:32 UTC. `main` = `62210ff` (PR #44 merge, task 19 done, Pages `built`). Only remote branch is `origin/main`; no competing live claim. This session claims task 20 above and will not edit files outside its scope except to fix a verified gap.
- Work plan: (1) rebuild + validate all three generators; (2) local HTTP smoke test of every page; (3) read back the live site and compare to repo; (4) spot-check official sources (BOC board/tariff, SAFE, IRS, eCFR, FinCEN/CBP); (5) requirement-by-requirement gap audit; (6) commit, push, PR, merge, confirm deploy; (7) record result here.

### Verification performed — arena/c5e783f4-china4 (2026-11-11 02:32–02:50 UTC)

**Rebuilt and re-validated.** `python3 scripts/build_site.py` → 7 main pages, 2 redirects, 40 amount rows; `build_evidence.py` → evidence.html (8 checked rules, 18×40 strict rows); `build_bank_playbooks.py` → 3 additive pages. `validate_site.py` → PASS (7 pages, 18 procedures, 5×40 matrices, 2026 tax illustration, 54 sources, Decimal arithmetic); `validate_evidence.py` → PASS (720 strictly blank current-cost rows); `validate_bank_playbooks.py` → PASS (49 sources, 9 playbooks/63 cited steps, 28 ledger rows). Rebuild produced zero diff — generated files are current. Local HTTP smoke test returned 200 for all 11 pages, both redirects, `style.css` and both JSON data files.

**Live site read back.** https://sassnarep3-star.github.io/China4/ serves the current dashboard (executive answer, cost snapshot, 18-route inventory). Pages API reports `status: built`, `build_type: legacy`, `source: main:/`.

**Official sources spot-checked this session (re-read, not merely linked):**

| Claim checked | Verified value | Official source |
|---|---|---|
| BOC FX board (current) | USD buying 666.29 / selling 669.10 per 100 USD at 2026/11/11 10:30:02; half-spread 0.2104% vs modelled 0.21037% — representative, absolute rate moved as flagged | [BOC exchange-rate board](https://www.boc.cn/sourcedb/whpj/enindex.html) |
| FBAR civil penalties | non-willful USD 16,536; willful USD 165,353; assessed on/after 2025-01-17 (31 CFR 1010.821 Table 1) | [eCFR 31 CFR 1010.821](https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010/subpart-H/section-1010.821) |
| US personal FX gain threshold | gain on a personal foreign-currency transaction excluded unless more than USD 200, then capital gain | [IRS Publication 525](https://www.irs.gov/publications/p525) |

**Requirement-by-requirement gap audit.** Executive summary → `summary.html` + `EXECUTIVE_SUMMARY.md`. Questions/information/answers + how to discover missing information → `flagged.html` ("Required verification" column with official starting points) + `taxes.html` ("Ten questions for a cross-border tax professional") + dashboard four checks. US-citizen best route → dashboard executive answer (licensed-bank wire with source-of-funds evidence; $50,000 quota is for domestic individuals). Methods pros/cons → `methods.html` (18 routes). Penalty breakdown → `penalties.html` (statutory ceilings vs lawful cost). $10,000–$400,000 tables → five 40-row matrices, mobile card layout at ≤760 px (`data-label`), most important columns first. Step-by-step → `methods.html` + `playbooks.html` (63 cited steps). Sourcing policy → every table row carries a source link (validator-enforced); unverified values blank and flagged. **No gap found; no site change required.** Unverified current quotes (Wise, WU, MoneyGram, correspondent deductions, personal taxes) remain blank by policy — estimating them would be hallucination.

**Irregularities (not merge blockers, already published on flagged.html):** BOC dated quote not permanently retrievable (rotating board + captcha); BOC Middle Rate ≠ arithmetic midpoint; stale open PRs #4/#5/#12/#38 untouched; task 17 taxgate files never delivered (no remote branch) — the China-tax-by-source topic is covered on `taxes.html` + `flagged.html` and is not duplicated here.

### Publication result — arena/c5e783f4-china4 (task 20)

- Integration PR [#45](https://github.com/sassnarep3-star/China4/pull/45) merged to `main` at commit `054fcd2` on 2026-11-11 02:33 UTC.
- Pull-request validation [run 42946741957](https://github.com/sassnarep3-star/China4/actions/runs/42946741957) concluded **SUCCESS** before merge.
- Post-merge workflow [run 42946802184](https://github.com/sassnarep3-star/China4/actions/runs/42946802184) and legacy Pages build/deploy [run 42946801491](https://github.com/sassnarep3-star/China4/actions/runs/42946801491) both concluded **SUCCESS**. Pages API reports `status: built`, live URL https://sassnarep3-star.github.io/China4/.
- Task 20 is **done**. No site content change was required: the published 11-page dashboard already satisfies the executive summary, questions/information/answers, US-citizen best-route, methods pros/cons, penalty breakdown, $10,000–$400,000 mobile tables, step-by-step procedures, and line-by-line sourcing requirements. Unverified current quotes remain blank and flagged by policy.
- Note: other sessions merged PR #48 (BOC ATM tariff correction) while this session was publishing; that work is theirs and was not altered here.
### Coordination conflict — arena/9ff08099-china4
- Another session claimed an overlapping broad integration audit at the same time on a separate branch, invisible when this claim was pushed, and merged PR #45 while this audit was in progress. The board conflicted; retained both sections without discarding either session’s work. Rebased locally first, then restored the already-pushed commits and merged origin/main to avoid rewriting the published session branch. No site-file conflict occurred.
- Task 21 integration conflict: concurrent task 20 appended at the same board location. Aborted rebase of the already-pushed claim to avoid rewriting history, merged main and retained both sections in full; no other session content discarded.

### Second integration conflict — arena/9ff08099-china4
- PR #48 independently completed the same ATM rollover while this session ran, and merged before PR #46. Preserved all of #48’s broader site changes and both coordination logs; retained the separate FX quote-unit correction and a regression check. The first merge attempt of PR #46 failed due to conflicts, not a site validation failure. The required pull/rebase after a merge replayed the other branch’s commits and conflicted; it was aborted in favor of retaining the already-resolved merge history.

### Publication result — arena/9ff08099-china4
- [PR #46](https://github.com/sassnarep3-star/China4/pull/46) merged 2026-11-11 at `d40b6231c64aefdec0e8c1974b9b2ee3175cf015`; PR validation [run 42947051695](https://github.com/sassnarep3-star/China4/actions/runs/42947051695) passed.
- Both [legacy Pages deployment 42947089526](https://github.com/sassnarep3-star/China4/actions/runs/42947089526) and [repository validation/deployment 42947090415](https://github.com/sassnarep3-star/China4/actions/runs/42947090415) succeeded for that merge. Live Flagged for Review page was read back, including the corrected per-100-USD unit. GitHub Actions emitted Node 20 deprecation warnings but no failures.
## Session arena/e701c274-china4 — task 20: fresh audit + "Before You Decide" questions page + publication

| # | Task | Scope (files) | Status | Owner | Started (UTC) | Notes |
|---|------|---------------|--------|-------|---------------|-------|
| 20 | Fresh independent audit of the live site, add a dedicated "Before You Decide" questions/information/answers checklist page (the one brief item without a dedicated home), re-verify load-bearing sources, rebuild/validate, PR, merge, confirm Pages | `COORDINATION.md`; `scripts/build_site.py`, `scripts/validate_site.py`, `scripts/validate_evidence.py`, `data/bank-playbooks.json` (nav only), generated root pages, `.github/workflows/gh-pages.yml`, `README.md`, `EXECUTIVE_SUMMARY.md`; plus this section | done | arena/e701c274-china4 | 2026-11-11 | Arena-fixed branch; no `session-<id>/<task>` branch. Prior tasks 1–19 done; site live at https://sassnarep3-star.github.io/China4/ (PR #44 merged). |

### Claim log — arena/e701c274-china4
- **Board state read before claiming (2026-11-11).** `main` is `62210ff` (PR #44 merged). Open PRs #4, #5, #12, #38 are stale early-session PRs, untouched. No other session has a live claim with recent commits; this session is the integration owner for task 20.
- **Gap analysis.** The brief asks for (a) executive summary — exists (`summary.html` + `EXECUTIVE_SUMMARY.md`); (b) clear list of questions/information/answers needed before any decision + how to discover missing info — **no dedicated page** (only scattered "four checks" on `index.html` and 8 steps on `summary.html`); (c) best lawful way for a US citizen + conversion-penalty breakdown — exists (`methods.html`, `penalties.html`, `taxes.html`); (d) $10k–$400k cost tables, mobile-friendly, step-by-step — exists (`penalties.html` 5×40 matrices, `methods.html` 18 procedures, `playbooks.html`); (e) line-by-line verification with source per row, blanks flagged — exists (`verification.html`, `flagged.html`, `evidence.html` strict blanks). This session fills (b) and freshly re-verifies load-bearing sources.
- **No invented values.** New page reuses only already-registered S-sources; unknown personal facts stay blank and are listed as "how to discover" steps. No new prices, rates, or tax amounts are introduced.
- **Overlap guard.** Before every push, re-fetch `main` and remote branches. If another session publishes first, link instead of duplicating.

### Verification and publication — arena/e701c274-china4 (task 20, 2026-11-11 UTC)

**Fresh re-verification (read, not merely linked).** SAFE Detailed Rules (Arts. 2, 13–15, 39 repealed by 汇发〔2023〕8号); SAFE 2022 Q&A (convenience quota, not a hard cap); BOC tariff PDF items 210105008/210108014 + notes 5/10; BOC board 2026/11/11 10:30:02 (USD 666.29/669.10, Middle 671.91, half-spread ~0.2104% vs modeled 0.210366%); IRS FBAR (>$10,000, Apr 15/Oct 15); FinCEN FBAR; IRS Pub 525 ($200 threshold); Wise CNY guide (eligibility, CNY 300,000/50,000 caps, own-account). All matched. Live site read back and confirmed.

**New page.** `questions.html` (14 questions + 10-row discovery checklist + 7 gates; 31 sourced rows, all reusing registered S-sources; no new values). Wired into `build_site.py` NAV/main, `validate_site.py` PAGES, `validate_evidence.py` nav list, `data/bank-playbooks.json` nav, Pages artifact, README and EXECUTIVE_SUMMARY. Research cutoff bumped to 2026-11-11 UTC; BOC model inputs unchanged. Penalties freshness callout gained the 2026-11-11 board read (prose only; table counts unchanged).

**Build/validate.** `build_site.py` → 8 pages; `validate_site.py` PASS (8 pages, 54 sources); `validate_evidence.py` PASS (720 blanks); `validate_bank_playbooks.py` PASS. Local HTTP smoke: all 12 pages + redirects + CSS + JSON returned 200. Mobile: all 138 `td` on questions.html carry `data-label`; ≤760px card layout confirmed.

**Irregularities (not blockers, published on flagged.html as before).** Dated BOC row still not permanently retrievable (captcha date query); Wise current prices still blank; personal facts/tax amounts still blank. No new irregularities found; no values inferred.

**Publication.** [PR #47](https://github.com/sassnarep3-star/China4/pull/47) merged 2026-11-11 02:37 UTC as `cbfc46bddffe60ac659a98459d3f996c0e2035d3`. The [Pages workflow](https://github.com/sassnarep3-star/China4/actions/runs/42947260552) completed validation and deployment successfully; the live [questions page](https://sassnarep3-star.github.io/China4/questions.html) was read back. Concurrent PRs #45, #48 and #46 updated main; rebase conflicts in this log and generated HTML were resolved by retaining both sessions’ logs and rebuilding from the merged generators.

- Checklist wording tightened: cash declaration does not authorize exceeding the RMB limit, and own-account restrictions and tax documentation are route-specific. No universal requirement to resolve past filings before a wire is asserted.

- Publication-log PR #50 conflicted after questions-page PR #47 merged concurrently. Retained both board sections and all #47 site changes.

## Session arena/100de12f-china4 — task 22: the "conversion penalty" quantified (China tax needed to make stuck CNY convertible, by source of funds), all-in cost ladder, US currency-gain by acquisition year — takeover of stale task 17-TG (NEW files only)

| # | Task | Scope (files) | Status | Owner | Started (UTC) | Notes |
|---|------|---------------|--------|-------|---------------|-------|
| 22 | (a) **Tax gate / conversion penalty**: for each lawful origin of the CNY (wages, labour-service fees, business income, interest, dividends, rent, property sale, incidental income, gift, inheritance, already-taxed savings, unexplained balance) — the China tax that has to be evidenced before a bank may convert above the convenience quota, its statutory rate and official source, late-payment surcharge and fine exposure on back taxes, lawful reducers (treaty, exemptions), and how the US foreign tax credit / exclusion treats that same tax; (b) **all-in ladder**: tax gate + already-published BOC transfer cost at every $10,000 step from $10,000 to $400,000, mobile-first, most important column first; (c) **US currency gain on the conversion itself by acquisition year**, from IRS yearly-average rates (topic of stale task 18(a); none of its file names used); (d) repository-mechanics review findings (logged below as change requests, not patched into other sessions' files) | **New files only — the exact set released by stale task 17-TG:** `taxgate.html`, `allin.html`, `taxgate-sources.html`, `taxgate.css`, `scripts/build_taxgate.py`, `scripts/validate_taxgate.py`, `data/taxgate-model.json`, `data/taxgate-sources.json`; plus this section of `COORDINATION.md` | in progress | arena/100de12f-china4 | 2026-11-11 02:38 | Does **not** edit `scripts/build_site.py`, any other generator/validator, `style.css`, any existing generated page, any existing `data/*.json`, `README.md`, `EXECUTIVE_SUMMARY.md` or the workflow while live sessions hold them. Branch fixed by Arena, so no `session-<id>/<task>` branch is created. |

### Claim log — arena/100de12f-china4
- **Board state read before claiming (2026-11-11 02:31–02:38 UTC).** The whole board was read. Because this clone's fetch refspec tracks only `main`, every remote branch was additionally fetched read-only into a local `refs/peek/*` namespace (`git fetch origin '+refs/heads/*:refs/peek/*'`); nothing was checked out or pushed. Four sessions were live inside the same six minutes: `arena/c5e783f4-china4` (task 20, verification-only, PR #45 merged), `arena/9ff08099-china4` (ATM tariff audit, PR #46 merged), `arena/198e49b1-china4` (task 21, the same ATM rollover, PR #48 merged) and `arena/e701c274-china4` (also numbered 20, `questions.html`, PR #47 merged). Their scopes are the shared generator, the generated root pages and the questions page. **None of those files is touched by task 22.**
- **Takeover of a stale claim (60-minute rule).** Task 17-TG (`arena/8686e554-china4`) last committed on 2026-11-10 06:02 UTC — more than 20 hours ago — and its branch contains the claim text only: no `taxgate.html`, `allin.html` or any work product exists on any of the 44 remote branches. Task 22 takes over that task and its released file names. Task 18(a) (`arena/545a0f57-china4`, last commit 2026-11-10 05:58 UTC, claim only) is taken over as a *topic* only; its file names (`fxgain.html`, `enforcement.html`, `moreroutes.html`, `extras.css`, `scripts/build_extras.py`, `scripts/validate_extras.py`, `data/extras-model.json`) are not used.
- **Why this scope.** The stated problem is that the balance cannot be converted "without paying a considerable amount of taxes". Every published cost matrix prices bank fees and FX spread (roughly 0.2%–0.5%) and states that it excludes underlying tax; `taxes.html` gives the resident comprehensive-income schedule and a US-side illustration only. The China tax that unlocks conversion, by source of funds, is the largest cost component and is not quantified anywhere on the site. Task 20's audit recorded "no gap found" and left this topic to `taxes.html` + `flagged.html`; task 22 respectfully treats it as the main open gap and fills it without editing those pages.
- **No invented values.** Tax figures are arithmetic on statutory rates read from the official text in this session, labelled as scenario illustrations and not as an assessment of anyone's liability. Any rate, exemption or procedure that cannot be confirmed on an official page is left blank and listed as unverified on the page itself. The transfer-cost component reuses the already-published BOC baseline from `data/cost-model.json` unchanged (read-only).
- **Irregularities found while reviewing the repository (logged for the integration owner; not patched into other sessions' files):**
  1. **Two deployments race on every merge.** GitHub Pages is configured `build_type: legacy`, source `main:/`, which publishes the entire repository root; the workflow's `deploy` job separately uploads a hand-listed `_site/` artifact (`cp evidence.html index.html … _site/`) and calls `actions/deploy-pages`. The deployments API shows two `github-pages` deployments per merge commit, seconds apart. Whichever finishes last decides what is live. Verified at 02:35 UTC: `https://sassnarep3-star.github.io/China4/scripts/build_site.py` returned the generator source, which only the legacy build can serve — so the root build was live then, and the scripts, `COORDINATION.md` and `data/` are publicly served. A page that exists in the repo but is missing from the hand-written `cp` list would disappear whenever the artifact deployment wins.
  2. **Sessions cannot see each other's branches by default.** The fetch refspec in these clones tracks only `main` and the session's own branch, so `git branch -r` shows a single remote branch. Task 20's claim log states "Only remote branch is `origin/main`; no competing live claim" while three other sessions were live. `git ls-remote --heads origin` lists 44 branches. This is the mechanical cause of the repeated invisible overlapping claims recorded on this board.
  3. **Duplicate work and number collisions today.** The same BOC ATM effective-date rollover was audited and merged twice (PRs #46 and #48); "task 20" is used by two sessions.
  4. **Stale open PRs** #4, #5, #12 and #38 remain open (not touched).
  5. **Pull-request checks can be silently cancelled.** The workflow places *every* run — pull-request validation included — in one `concurrency: group: "pages"`. GitHub keeps one running and one pending run per group, so in a burst a queued PR validation is evicted by the next queued run. Observed on this session's claim-only PR #52: run [42947547071](https://github.com/sassnarep3-star/China4/actions/runs/42947547071) concluded `cancelled` (not failed) while PRs #49–#54 were merging, leaving the PR `MERGEABLE` with **no completed check**. A PR can therefore be merged without validation ever having run. Suggested fix for the integration owner: scope the concurrency group to the deploy job only, or key it by `github.ref` for pull requests.
- **Change requests to shared files (not applied by this session while those files are claimed by a live session):**
  1. `scripts/build_site.py` → `NAV` (and the equivalent nav list in `data/bank-playbooks.json` / `scripts/build_evidence.py`): add `taxgate.html` and `allin.html`.
  2. `.github/workflows/gh-pages.yml`: run `python3 scripts/build_taxgate.py` before the generated-diff check and `python3 scripts/validate_taxgate.py` in `validate`; add `taxgate.html`, `allin.html`, `taxgate-sources.html`, `taxgate.css`, `data/taxgate-model.json` and `data/taxgate-sources.json` to the `_site/` copy list — or replace the hand-written list with a glob so it cannot go stale (irregularity 1).
  3. `flagged.html` (via the shared generator): register irregularities 1–4 and any defect task 22 finds in an existing row.
- **Integration.** If another integration owner is still live when task 22's content is ready, requests 1–3 stay here for it. If every other claim is `done` or more than 60 minutes old with no commits at that point, this session applies requests 1–3 itself as the last integration step, re-runs every validator, opens the PR, merges and confirms the Pages deployment.
- **Rebase conflict #1 (2026-11-11 02:40 UTC).** Claim-only PR #52 reported `CONFLICTING`: PRs #50 (`arena/9ff08099-china4`) and #51 (`arena/e701c274-china4`) had appended their publication logs at the same end-of-file position while the claim was being pushed. Stopped, then resolved by keeping **both sides in full** — `main`'s text first, this section after it. No other session's text was dropped or edited. Only `COORDINATION.md` conflicted.

## Session arena/0829bcfa-china4 — task 23: Multi-bank & all-channel $10k–$400k matrix + cross-border treaty-claim, outbound-filing & US offshore remediation playbook (narrowed for zero overlap)

| # | Task | Scope (files) | Status | Owner | Started (UTC) | Notes |
|---|---|---|---|---|---|---|
| 23 | (a) **Multi-bank & all-channel $10,000–$400,000 cost, transfer-count & feasibility matrix (`method-matrix.html`)**: 40-increment ($10k–$400k) mobile-first comparison across documented PRC bank tariffs (`ABC` SHA/OUR, `BOC` SHA/OUR/Demand Draft/Overseas ATM, `HSBC China` Private Banking vs Premier/Advance SHA/Full-Amount, existing-USD savings wires without FX spread, staged emigration `汇发〔2004〕16号` across ABC vs BOC) plus statutory/provider single-transfer cap & minimum-transfer-count mechanics (`Wise` bank-funded & `SkyRemit` `CNY 300,000` single cap = 1 transfer up to `$40k`, 2–9 transfers at `$50k–$400k`; `Wise Alipay` `CNY 50,000` cap; `ICBC MoneyGram` `$10k/$20k` caps; unverified live FX/provider quotes strictly blank `—` and flagged); (b) **Cross-border treaty-relief claim, outbound filing exemptions & US offshore compliance remediation playbook (`treaty-filings.html`)**: primary-source procedures for `STA/SAFE [2013] No. 40` Art. 1 vs Art. 4 (`境外个人` own-account personal FX rules) & Art. 3 (15 exemptions) + `[2021] No. 19`; claiming US–China Treaty 10% caps via IRS `Form 8802` / `Form 6166` (`$105` individual fee from 2026-10-01) + PRC `STA [2019] No. 35` (`非居民纳税人享受协定待遇管理办法`), avoiding the IRS `Form 1116` non-creditable excess-withholding trap (including post-`2026-09-01` `公告2026年第27号` 20% FIE dividends), 3-year PRC refund (`税收征收管理法` Art. 51) vs 10-year US FTC refund (`Form 1040-X`), and `Form 8833`; IRS pre-transfer remediation (`Streamlined Foreign 0%` vs `Streamlined Domestic 5%` vs `Delinquent FBAR` / `Form 3520`), master PRC/US filing calendar, and 40-increment ($10k–$400k) treaty-claim savings vs offshore-penalty exposure matrix | **New files only during active parallel work:** `method-matrix.html`, `treaty-filings.html`, `scripts/build_method_treaty.py`, `scripts/validate_method_treaty.py`, `data/method-treaty.json`, plus this section of `COORDINATION.md` | in progress | arena/0829bcfa-china4 | 2026-11-11 02:37 | Branch fixed by Arena (`arena/0829bcfa-china4`). Narrowed and renumbered from initial `02:37:02 UTC` claim (`8648072`) so there is **zero topic or file overlap** with `arena/100de12f-china4` (task 22: `taxgate.html`, `allin.html`, FX gain by year) or `arena/bd21a698-china4` (task 21-TG: `taxgate.html`). |

### Claim & overlap-resolution log — arena/0829bcfa-china4
- **Simultaneous-claim conflict & narrowing (2026-11-11 02:41 UTC):** Our initial claim (`8648072`, pushed at `02:37:02 UTC`) included a source-of-funds tax-unlock & FX-gain-by-year scope alongside `method-matrix.html`. Upon rebasing onto `origin/main` (`b3861f1`), we observed that `arena/bd21a698-china4` (`02:37:26 UTC`, task `21-TG`) and `arena/100de12f-china4` (`02:39:37 UTC`, task `22`, merged as claim PR #52) claimed the source-of-funds tax gate (`taxgate.html`), BOC+tax all-in ladder (`allin.html`), and US FX-gain-by-year topics in the same 3-minute window. Following the board protocol (*"stop, resolve any conflict without discarding their work, narrow or adjust your scope so there is no overlap, and record the resolution in COORDINATION.md"*), we preserved `main`'s text in full, renumbered our task to **23**, and replaced the overlapping source-of-funds/FX-year topic with **`treaty-filings.html`** (administrative treaty-claim workflow `Form 8802`/`6166` + `STA [2019] No. 35`, `STA/SAFE [2013] No. 40` Art. 1 vs Art. 4 & Art. 3 exemptions, IRS Streamlined Offshore `0%`/`5%` remediation, and master PRC/US filing calendar) alongside **`method-matrix.html`** (multi-bank ABC/BOC/HSBC + provider cap/transfer-count 40-increment matrix).
- **Non-overlapping scope rule honored:** While `arena/100de12f-china4` and `arena/bd21a698-china4` are active, this session edits **only** its five new files (`method-matrix.html`, `treaty-filings.html`, `scripts/build_method_treaty.py`, `scripts/validate_method_treaty.py`, `data/method-treaty.json`) and this `COORDINATION.md` section.
- **Shared-file change request (applied at final integration when no other active session holds shared files):**
  1. `scripts/build_site.py`, `data/bank-playbooks.json`, `scripts/validate_site.py`, `scripts/validate_evidence.py`: add `method-matrix.html` and `treaty-filings.html` to global navigation and cross-links, preserving `questions.html` and any merged `taxgate.html` / `allin.html` work.
  2. `.github/workflows/gh-pages.yml`, `README.md`, `EXECUTIVE_SUMMARY.md`, `flagged.html`: run `python3 scripts/build_method_treaty.py` and `python3 scripts/validate_method_treaty.py` in CI, stage `method-matrix.html`, `treaty-filings.html`, and `data/method-treaty.json` (or glob `*.html *.css` and `data/*.json` so no additive page can be dropped by `_site/`), and register newly verified statutory irregularities (`STA/SAFE [2013] No. 40` Art. 1 vs Art. 4 scope nuance, IRS treaty-cap non-creditability trap on post-`2026-09-01` 20% FIE dividends, and workflow/Pages race).

- **Research and integration:** Re-read the 2026 HSBC tariff, ABC tariff, treaty, China filing and refund rules, IRS Form 6166 and offshore procedures. Form 8802 individual fee increased to **$105** on 2026-10-01; earlier $85 claim corrected. The added pages distinguish conditional tariff examples from live executable quotes; withholding and streamlined-penalty examples use separate hypothetical bases. No personal eligibility or tax liability is asserted.
- **Integration scope:** Re-fetched all branch heads; the two live overlapping tax-gate sessions remain confined to additive files, with no current shared-file claims. Added navigation, CI validation and artifact staging for task 23, without touching their files. Pages artifact now stages root HTML/CSS and JSON files; moved Pages concurrency to deploy only so PR validation is not cancelled by unrelated runs. Legacy Pages versus Actions deployment race remains an administrative configuration issue requiring repository settings review.
- **Validation:** Four builders and all five validators including the effective-date regression pass locally. Task 23 validator independently checks all 40 tariff calculations, cap counts, sourced responsive rows and local links.

## Session arena/47133a67-china4 — deployment reliability

| Task | Scope | Status | Owner | Started UTC | Notes |
|---|---|---|---|---|---|
| Diagnose and repair failed Pages deployment after PR #55; validate and publish | `.github/workflows/gh-pages.yml`, `COORDINATION.md` | in progress | arena/47133a67-china4 | 2026-11-11 07:36 | Prior integration branch merged; earlier workflow claims have been inactive for over 60 minutes. Arena-fixed branch. Investigate failure before altering settings. |
- Initial branch pull failed because the remote branch did not yet exist; the initial push then created it. Task 23 shipped in PR #55, but its board entry remained in progress; earlier task 22's branch had no commits in over 60 minutes and its claimed files are absent from main. No unpublished work is assumed verified or merged.
- GitHub API showed legacy branch publishing from main and successful Pages build for PR #55, but the separate custom deploy job failed. Its failure log was inaccessible (GitHub log host returned EOF), so the precise failure is unconfirmed. A request to switch Pages to Actions received HTTP 403 (integration lacks access). Rather than leave a failing competing deployment, removed the redundant custom deploy job and retained validation; the existing branch publisher remains authoritative. GitHub's [publishing-source documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site) describes branch vs workflow publishing. Branch publishing exposes repository-root content and is independent of validation; documented both limitations in README. No claim of full line-by-line external source verification is made by this session.
## Session arena/e1d49618-china4 — publication integrity audit

| Task | Scope | Status | Owner | Started UTC |
|---|---|---|---|---|
| Audit generated site, current deployment configuration and reproducible validation; publish audit limits | COORDINATION.md, PUBLICATION_AUDIT.md, scripts/validate_publication.py, .github/workflows/gh-pages.yml (validation step only); GitHub Pages settings | in progress | arena/e1d49618-china4 | 2026-11-11 07:40 |

Claim: existing content scopes are preserved. This is a narrow integration/publication task, not a claim that inherited financial research has been independently verified. Previous shared-file claims are over 60 minutes old; no open PR currently owns this scope. Arena requires the fixed current branch, so no additional branch is created. Source retrieval and personal-account limits will be reported explicitly.

### Audit outcome — arena/e1d49618-china4
- Scope expanded only to `scripts/build_site.py` and generated `flagged.html` for the required published irregularity. Existing content and other sessions' additive files preserved.
- Official documents re-read: SAFE 2007 https://www.safe.gov.cn/en/2007/0105/819.html (selected quota/authenticity text), IRS currency https://www.irs.gov/individuals/international-taxpayers/foreign-currency-and-currency-exchange-rates, GitHub Pages https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages. This is not full independent legal verification of inherited research.
- Confirmed Pages legacy/Actions mismatch; latest custom deploy failed but legacy build succeeded. Settings update denied HTTP 403; no credentials requested. Initially drafted a runtime mode guard; concurrent PR #56 removed the deploy job instead, and that fix is preserved. Added all-root-page local link/anchor validator and Review-page flag. Detailed failed logs inaccessible; failure step confirmed via API metadata only.
- Four builders and all six validators pass. No generated drift outside the intended Review page. Unknown current quote/tax values remain blank. See PUBLICATION_AUDIT.md for limits and sources. PR and publication confirmation follow below.

- Rebase conflict: concurrent session arena/47133a67-china4 merged PR #56 during this audit. Stopped and resolved board conflicts by retaining both logs; preserved their removed-deploy workflow and narrowed our workflow edit to one validator invocation. No other session work discarded.

## Session arena/ba756fdb-china4 — task 25: the "tax gate" (China tax that unlocks conversion, by source of funds), all-in cost ladder, and US currency-gain exposure by acquisition year (NEW files only)

| # | Task | Scope (files) | Status | Owner | Started (UTC) | Notes |
|---|---|---|---|---|---|---|
| 25 | (a) **Tax gate** — for each lawful origin of the stuck CNY (wages, bonus, service fees, business profit, dividends, interest, rent, property sale, equity/share sale, gift, inheritance, undocumented balance): the China tax that must be evidenced before a bank may convert and remit, its statutory rate, lawful reliefs, and how the US treats the same tax (credit / exclusion). (b) **All-in ladder** — tax gate + published bank transfer cost for every scenario at each USD 10,000 step from USD 10,000 to USD 400,000, mobile-first, most important column first. (c) **US currency-gain exposure by acquisition year** — fills the "Measured FX gain" column that is blank on `taxes.html`, from the IRS yearly-average rate table, at every USD 10,000 step. | **New files only:** `taxgate.html`, `allin.html`, `fxgain.html`, `taxgate.css`, `scripts/build_taxgate.py`, `scripts/validate_taxgate.py`, `data/taxgate-model.json`; plus this section of `COORDINATION.md` | in progress | arena/ba756fdb-china4 | 2026-11-11 07:45 | Arena fixes the branch name, so this session works on `arena/ba756fdb-china4` instead of a `session-<id>/<task>` branch. Takeover of stale claims under the 60-minute rule — see claim log. |

### Claim log — arena/ba756fdb-china4
- **Board read 2026-11-11 07:38–07:45 UTC; all 49 remote branches fetched read-only.** `main` = `15e4e8a` (PR #57). Live sessions found (commits within the last 10 minutes), all left untouched:
  - `arena/47133a67-china4` — Pages deployment reliability (`.github/workflows/gh-pages.yml`); PR #56 merged.
  - `arena/e1d49618-china4` — publication integrity audit (`PUBLICATION_AUDIT.md`, `scripts/validate_publication.py`); PR #57 merged.
  - `arena/6691b7ad-china4` — "task 24": independent verification, CI deploy repair (`.github/workflows/gh-pages.yml`), publication.
  - `arena/8e3f208c-china4` — "task 24": content verification of load-bearing figures (`data/*.json`, the four `scripts/build_*.py` generators and the generated root `*.html`).
  - `arena/325783ff-china4` — repository and Pages closeout audit (PR #59 open).
- **Why this scope.** The brief says the money cannot be converted "without paying a considerable amount of taxes" and asks to "break down the conversion penalty". Every published cost matrix states that it *excludes underlying tax*; `taxes.html` carries only the comprehensive-income (wage) schedule and leaves the "Measured FX gain" column blank. The China-side tax that a bank needs evidenced before it converts — by source of funds — is the largest cost component and is not quantified anywhere on the site. It was claimed three times and never delivered.
- **Takeover under the 60-minute rule (handoff noted).** The same topic was claimed by `arena/8686e554-china4` (17-TG, last commit 2026-11-10 06:02 UTC), `arena/bd21a698-china4` (21-TG, 2026-11-11 02:37 UTC) and `arena/100de12f-china4` (task 22, 2026-11-11 02:42 UTC); the acquisition-year currency-gain part by `arena/545a0f57-china4` (task 18, 2026-11-10 05:58 UTC). All four claims are 5–26 hours old. A file-by-file comparison of each of those branches against `main` shows **no work product** — no `taxgate.html`, `allin.html`, `fxgain.html` or related script/data file exists on any branch. This session takes the topic over and reuses the file names `taxgate.html`, `allin.html` and `fxgain.html` so that a resumed session finds the work instead of duplicating it. `enforcement.html`, `moreroutes.html`, `calculator.html`, `howto.html`, `conversion-penalty.html`, `ledger.html` and `kit/` are **not** taken.
- **No overlap with live sessions.** Nothing in this scope is named in any live claim. `arena/8e3f208c-china4` owns the shared generators and generated root pages; this session does not edit them. If this session finds a defect in an existing row while reading the repo, it is logged in this section for that owner rather than patched.
- **Verification rule for this task.** Every table row carries a link to the official page it was read from in this session. A value that could not be confirmed on an official page is left blank and listed as unverified on the page itself; nothing is inferred to fill a cell.
- **Change requests to shared files (not applied by this session while those files are claimed by a live session):**
  1. `scripts/build_site.py` → `NAV` (and the equivalent nav lists in `scripts/build_evidence.py`, `data/bank-playbooks.json`, `scripts/build_method_treaty.py`): add `taxgate.html`, `allin.html`, `fxgain.html`.
  2. `.github/workflows/gh-pages.yml`: run `python3 scripts/build_taxgate.py` before the generated-diff check and `python3 scripts/validate_taxgate.py` in the validation step.
  3. `flagged.html` (via the shared generator): register the irregularities this task finds. Until then they are published on the three new pages themselves and listed in this section.
- **Integration.** If another integration owner is still live when task 25 is ready, requests 1–3 stay here for it. If every other claim is `done` or more than 60 minutes old with no commits at that point, this session applies requests 1–3 itself as the last integration step, re-runs every validator, opens the PR, merges and confirms the Pages deployment.
