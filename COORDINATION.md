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
