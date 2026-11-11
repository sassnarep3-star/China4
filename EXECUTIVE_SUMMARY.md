# Executive summary — China4 evidence desk

- **Research cutoff:** 2026-11-10 UTC (independent re-verification; FX citation made durable, Wise current-cost cells blanked, ATM cap-unit correction retained)
- **BOC retail quote timestamp:** 2026-11-09 05:30 Beijing time

**Current deliverable:** [executive summary](summary.html) · [`index.html`](index.html) · [cost matrices](penalties.html) · [procedures](methods.html) · [taxes](taxes.html) · [bank tariffs](banks.html) · [route playbooks](playbooks.html) · [verification ledger](verification.html) · [sources](sources.html) · [open items](flagged.html)

This summary supersedes earlier draft summaries and cost pages. Earlier provider figures that were not supported by current primary evidence are no longer presented as executable prices.

## Bottom line

For a US passport holder classified by SAFE as a **foreign individual**, the most verifiable default is conversion and an own-account international wire through a licensed bank, supported by lawful source-of-funds and tax evidence. The **USD 50,000 annual convenience purchase quota applies to domestic individuals**; it is not blanket ID-only permission for every US citizen. Genuine documented current-account transactions are not subject to a blanket USD 50,000 hard cap.

Moving existing own-account principal is not itself a new wage or gift. It is not proof of zero tax: underlying income, gains, interest, tax residence, personal FX rules and information returns require separate analysis.

## Audited BOC planning model

Inputs:

- USD retail buy/sell: **6.6648 / 6.6929 CNY per USD**; internally calculated midpoint **6.67885**.
- Personal TT/draft commission: **0.1%, minimum CNY 50, maximum CNY 260**.
- US-bound international TT telecom charge: **CNY 150**.
- One-way half-spread benchmark: **0.2103656%**, calculated from the same-timestamp retail buy/sell pair. It is an arithmetic benchmark, not a guaranteed markup or accessible mid-market quote.
- Quote durability: BOC's rate board rotates, and by 2026-11-10 the cited 2026-11-09 05:30 row had rolled off the page where it was first captured. The citation now points to BOC's official historical query (date 2026-11-09, USD) rather than a page number. BOC's live board at 2026-11-10 02:49 showed **6.6622 / 6.6903**, a **0.210449%** half-spread — about 0.04% relative difference from the modeled input, so the dated input remains representative even though the absolute rate moved.

| USD-equivalent principal | BOC TT known modeled cost | Wire-only component | FX benchmark component |
|---:|---:|---:|---:|
| $10,000 | **$53.45** | $32.41 | $21.04 |
| $50,000 | **$166.44** | $61.26 | $105.18 |
| $100,000 | **$271.62** | $61.26 | $210.36 |
| $200,000 | **$481.99** | $61.26 | $420.73 |
| $400,000 | **$902.72** | $61.26 | $841.46 |

Known modeled cost excludes correspondent deductions, account-specific recipient fees, underlying taxes, travel and professional costs. Optional BOC full-arrival pricing is **USD 15 to BOC New York / USD 25 elsewhere**. Receiving examples are BofA USD 15 and Chase Secure USD 15; [Capital One](https://www.capitalone.com/help-center/checking-savings/send-receive-wire-transfer/) charges USD 15 only on Essential Checking, High-Yield Checking and Essential Savings and no fee on other account types, so confirm your own account schedule.

**Penalty versus lawful cost (the decisive comparison):** at USD 400,000 the modeled lawful BOC cost is **USD 902.72**, while the published statutory ceiling for an FX offence is 30% of the amount (USD 120,000), rising to the equivalent amount (USD 400,000) in serious cases — before criminal exposure. These ceilings are statutory rates applied to the principal, not an assessment or prediction; enforcement is discretionary and fact-specific. See the [comparison table](penalties.html#penalty-vs-cost).

## Conditional comparisons

- **Wise from CNY:** available only to eligible non-mainland-Chinese users with qualifying work/tax records; recipient must be the sender’s own account. Bank-app funding cap CNY 300,000 per transfer; Alipay funding cap CNY 50,000. Current price and equal-net-payout transfer count remain unverified and blank. The 2024 examples do not establish current fees. Wise deducts fees before conversion; compare live offers for the same net USD payout.
- **Domestic-individual annual schedule:** if that identity classification genuinely applies, the illustrative USD 400,000 / eight annual USD 50,000 wires model costs **USD 1,331.53** at constant inputs. This is arithmetic, not advice to split or evade review.
- **Emigration property:** qualifying property must be applied for together. At or below CNY 200,000, one approved remittance may be possible. Larger scenarios model 50% initially, 25% after one year and 25% after two years; USD 400,000 modeled known BOC cost is **USD 1,025.24**, excluding professional/tax costs.
- **Inheritance:** one or multiple remittances may be used after the single application; the mandatory emigration timetable is not incorrectly imposed on inheritance.
- **Property sale:** a foreign individual’s registered sale proceeds require title/transfer and tax evidence; remittance is limited to the seller’s after-tax share.
- **Cash/ATM:** cash above USD 10,000 is generally prohibited except specified SAFE-approved special cases. Customs declaration is a separate layer: inbound/outbound travellers are limited to **RMB 20,000 each per trip** (PBOC Announcement [2004] No. 18) and must declare currency beyond the prescribed amount under **Customs Announcement 2025 No. 43**, which replaced the repealed 2007 No. 72 on 2025-04-01. Domestic-card overseas ATM withdrawals are capped at CNY 100,000 per person/year and CNY 10,000 per card/day. Only the USD 10,000 matrix row fits the ATM annual cap at the planning rate; it needs **7 withdrawals** at the daily cap, with modeled issuer fees of **$112.55** (UnionPay, current) or **$250.00** (Visa/Mastercard formula effective since 2026-11-11), excluding ATM-owner surcharges and execution FX.
- **Unproven/prohibited:** no direct generic PayPal China, standalone Alipay/WeChat or Hong Kong detour is represented as verified. Private swaps, borrowed quotas, false documents and crypto/stablecoin workarounds are not recommended.

## US reporting and lawful tax relief

- **FBAR:** aggregate foreign financial accounts exceeded USD 10,000 at any time in the calendar year; due April 15 with automatic extension to October 15.
- **Form 8938:** separate thresholds based on US/abroad residence and filing status; both FBAR and Form 8938 can apply.
- **Form 3520:** specified foreign gifts/bequests and trusts, not moving your own savings.
- **Cash:** FinCEN Form 105 applies to physically transporting more than USD 10,000; bank CTR aggregation and trade/business Form 8300 are distinct rules.
- **Underlying income:** compare FEIE (2026 maximum USD 132,900 for a qualifying person) with the foreign tax credit, without claiming a credit on excluded income. Treaty saving-clause rules matter for US citizens.
- **Past omissions:** eligible nonwillful taxpayers should evaluate the IRS streamlined offshore or US-resident procedures rather than silently back-filing.

## Reproduce and verify

```sh
python3 scripts/build_site.py
python3 scripts/validate_site.py
```

The build regenerates seven main pages, two compatibility redirects and `data/cost-model.json`. The independent validator checks 18 procedures, four 40-row matrices, 52 primary sources, local links, HTML structure, citation durability for the dated FX quote, and Decimal arithmetic. GitHub Actions repeats the build/validation before deploying the public artifact.


## Final integration — arena/374f09e6-china4 (2026-11-10 UTC)

This session re-read the load-bearing official sources, then added the **live executive-summary page** (`summary.html`), which previously existed only as this Markdown file in the repository. The page carries a five-amount key-cost table, an eight-route shortlist, a six-row tax/penalty boundary and eight ordered execution steps; every table row links to a primary source. The dashboard CTA, navigation, validator, Pages artifact and documentation were updated with it.

**Merge-conflict resolution.** While this session was working, other sessions merged PRs #24–#29 into `main` (including a 52-source register with S48–S52, current Customs Announcement 2025 No. 43, the dedicated CBP monetary-instruments page and the corrected Capital One wording). PR #30 therefore reported `CONFLICTING`. Rather than overwrite that work, `main`'s tree was taken in full and this session re-applied only its genuinely new contribution on top: the summary page, a second same-day rate-freshness check, three additional flagged items and the validator/Pages wiring. All 52 source IDs, S48–S52, the prose/register count guard and every other session's corrections were preserved.

**Additional verification.** A 2026/11/10 07:32:39 Beijing read of [BOC's official board](https://www.boc.cn/sourcedb/whpj/enindex.html) showed USD 666.22 / 669.03 CNY per 100 USD and a separately published Middle Rate of 671.88; the Costs page now discloses that the Middle Rate is a distinct column, not the arithmetic midpoint of the buy/sell quotes. [IRS Publication 525](https://www.irs.gov/publications/p525) (personal FX gain over $200 is capital gain), [Instructions for Form 3520](https://www.irs.gov/instructions/i3520) (>$100,000 foreign gifts, 5%/month capped at 25%), [FinCEN's CTR FAQ](https://www.fincen.gov/resources/frequently-asked-questions-regarding-fincen-currency-transaction-report-ctr) and [IRS Publication 1544](https://www.irs.gov/publications/p1544) were also re-read. New flagged items: no permanent official URL for the exact dated BOC row, the undefined Middle Rate column, and the PRC IIT rate tables being published as images. Nothing was inferred to fill a blank.

`python3 scripts/build_site.py` → 7 pages, 2 redirects, 40 audited rows; `python3 scripts/validate_site.py` → **PASS** (7 pages, executive summary, 18 procedures, 4×40 matrices, 52 sources, prose/table agreement, canonical FX citations, local links, independent Decimal arithmetic). Local HTTP smoke test: all 9 HTML/redirect pages, `style.css` and `data/cost-model.json` returned **200**. Mobile tables still collapse to labelled cards at ≤760 px via `data-label` on every `td`.

## What the tax exposure looks like, quantified (2026)

Illustration for a **single filer under 65 with USD 100,000 of other taxable income**, using the brackets, standard deduction, capital-gain bands and FEIE amount published in IRS Rev. Proc. 2025-32. Same dollar amount, three different characters:

| Amount | If ordinary income: added US tax | If a 10% currency gain: US capital-gain tax | If FEIE-eligible earned income: US tax |
|---:|---:|---:|---:|
| $10,000 | **$2,286.00** | $150.00 | **$0.00** |
| $50,000 | **$11,886.00** | $750.00 | $1,804.00 |
| $100,000 | **$23,886.00** | $1,500.00 | $9,474.00 |
| $200,000 | **$57,057.25** | $3,000.00 | $32,702.00 |
| $400,000 | **$127,057.25** | $6,000.00 | $97,254.25 |

Read this as a scale, not a forecast. Two consequences drive the decision:

- **A currency gain is not a percentage levy on the principal.** Publication 525 excludes a personal foreign-currency transaction gain unless it is more than USD 200 and reports it as a capital gain above that amount, so a held-for-personal-use balance converted once is a small separate line. A *measured* gain stays blank on the site because the acquisition date and rate of a pre-existing balance are personal facts.
- **The large numbers appear only if the money is untaxed income.** That is a reporting-history question answered by the FBAR, FEIE/FTC and streamlined-procedure material — not by choosing a different payment rail. No rail converts taxable income into exempt principal.

## Re-verification performed 2026-11-10

Primary documents re-fetched and read, not merely linked: SAFE individual FX rules (Arts. 2, 13, 14, 15, 30, 39) and the PBOC individual FX measures (Art. 37 identity definitions); the SAFE 2022 Q&A confirming a convenience quota rather than a hard cap; the State Council FX Regulations (Dec. 532, Arts. 5 and 39–45); the BOC tariff PDF (items 210101002, 210105008, 210108014, notes 5 and 10) and the 2026-11-11 ATM notice; eCFR 31 CFR 1010.821 and 1010.340; IRS FBAR guidance, the Form 8938/FBAR comparison, Form 3520 instructions, the FEIE page and Publication 525; IRS Rev. Proc. 2025-32; PBOC Announcement [2004] No. 18; Customs Announcement 2025 No. 43; SAFE's cash-carrying and ATM-cap notices; and Wise's CNY guide with its dated 2024-11-25 fee-change post.

All cited figures matched the sources on re-read. The 2026 US tax illustration is arithmetic on published brackets: a mutation test (changing one bracket's tax-at-floor by one dollar) makes the validator fail, which confirms the check is live rather than tautological.
