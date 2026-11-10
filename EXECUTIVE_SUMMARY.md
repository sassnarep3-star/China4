# Executive summary — China4 evidence desk

- **Research cutoff:** 2026-11-09 UTC · **links re-verified:** 2026-11-10 UTC (Wise/ATM cap-unit correction retained; new BOC citation audit below)
- **BOC retail quote timestamp:** 2026-11-09 05:30 Beijing time

**Current deliverable:** [executive summary](summary.html) · [`index.html`](index.html) · [cost matrices](penalties.html) · [procedures](methods.html) · [taxes](taxes.html) · [sources](sources.html) · [open items](flagged.html)

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

| USD-equivalent principal | BOC TT known modeled cost | Wire-only component | FX benchmark component |
|---:|---:|---:|---:|
| $10,000 | **$53.45** | $32.41 | $21.04 |
| $50,000 | **$166.44** | $61.26 | $105.18 |
| $100,000 | **$271.62** | $61.26 | $210.36 |
| $200,000 | **$481.99** | $61.26 | $420.73 |
| $400,000 | **$902.72** | $61.26 | $841.46 |

Known modeled cost excludes correspondent deductions, account-specific recipient fees, underlying taxes, travel and professional costs. Optional BOC full-arrival pricing is **USD 15 to BOC New York / USD 25 elsewhere**. Receiving examples are BofA USD 15 and Chase Secure USD 15; [Capital One](https://www.capitalone.com/help-center/checking-savings/send-receive-wire-transfer/) publishes USD 15 for three named account types and no fee for all others, so the USD 0 example is an inference that must be confirmed against your own account schedule.

## Conditional comparisons

- **Wise from CNY:** available only to eligible non-mainland-Chinese users with qualifying work/tax records; recipient must be the sender’s own account. Bank-app funding cap CNY 300,000 per transfer; Alipay funding cap CNY 50,000. Current price requires a live quote. The site separately models Wise’s **dated 2024-11-25** formulas, never as current prices. At those CNY caps, USD 400,000 requires **9 bank-funded or 54 Alipay-funded transfers** (dated-formula fees $2,524.64 / $8,147.87); an earlier model that treated the CNY caps as USD understated the fixed per-transfer fees and was corrected on 2026-11-09.
- **Domestic-individual annual schedule:** if that identity classification genuinely applies, the illustrative USD 400,000 / eight annual USD 50,000 wires model costs **USD 1,331.53** at constant inputs. This is arithmetic, not advice to split or evade review.
- **Emigration property:** qualifying property must be applied for together. At or below CNY 200,000, one approved remittance may be possible. Larger scenarios model 50% initially, 25% after one year and 25% after two years; USD 400,000 modeled known BOC cost is **USD 1,025.24**, excluding professional/tax costs.
- **Inheritance:** one or multiple remittances may be used after the single application; the mandatory emigration timetable is not incorrectly imposed on inheritance.
- **Property sale:** a foreign individual’s registered sale proceeds require title/transfer and tax evidence; remittance is limited to the seller’s after-tax share.
- **Cash/ATM:** cash above USD 10,000 is generally prohibited except specified SAFE-approved special cases. Domestic-card overseas ATM withdrawals are capped at CNY 100,000 per person/year and CNY 10,000 per card/day. Only the USD 10,000 matrix row fits the ATM annual cap at the planning rate; it needs **7 withdrawals** at the daily cap, with modeled issuer fees of **$112.55** (UnionPay, current) or **$250.00** (Visa/Mastercard formula from 2026-11-11), excluding ATM-owner surcharges and execution FX.
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

The build regenerates seven main pages, two compatibility redirects and `data/cost-model.json`. The independent validator checks 18 procedures, four 40-row matrices, 47 primary sources, canonical citation URLs, local links, HTML structure and Decimal arithmetic. GitHub Actions repeats the build/validation before deploying the public artifact.


## Independent re-audit — 2026-11-10 UTC

All prior tasks were already marked done; this session re-fetched the load-bearing official documents, added the executive-summary page to the live site, corrected citation defects, and re-verified the combined build. New findings (all published on [flagged.html](flagged.html) with source links):

1. **High — BOC rate citation no longer reproduces the model's quote.** All five pages of [BOC's official exchange-rate board](https://www.boc.cn/sourcedb/whpj/enindex.html) now show 2026/11/10 quotes; the exact 2026-11-09 05:30 USD row (666.48 / 669.29 CNY per 100 USD) used by the model is not displayed, and BOC's historical date search requires a captcha. A fresh official read at 2026/11/10 07:32:39 Beijing shows USD 666.22 / 669.03 with a separate Middle Rate column of 671.88. S5 was repointed to the canonical board and the dated inputs remain in `data/cost-model.json`; they are historical model inputs, not currently re-verifiable from a permanent official URL. Obtain a written rate confirmation before executing.
2. **Medium — Customs thresholds were cited to a page whose HTML hides the numbers.** The official [passenger-baggage service guide PDF](https://online.customs.gov.cn/static/pages/guides/000629014002/5.%E8%BF%9B%E5%87%BA%E5%A2%83%E8%A1%8C%E6%9D%8E%E7%89%A9%E5%93%81%E7%9B%91%E7%AE%A1%EF%BC%88%E7%89%B9%E6%AE%8A%E9%A1%B9%E7%9B%AE%E9%99%A4%E5%A4%96%EF%BC%89%E6%94%BF%E5%8A%A1%E6%9C%8D%E5%8A%A1%E4%BA%8B%E9%A1%B9%E5%8A%9E%E4%BA%8B%E6%8C%87%E5%8D%97%EF%BC%88%E4%BF%AE%E6%94%B9%E7%A8%BF%EF%BC%89.pdf) states RMB 20,000 / USD-equivalent 5,000 verbatim (reproducing GACC Announcement 2007 No. 72); S8 now points there. The currently effective announcement should still be confirmed with Customs.
3. **Medium — Form 105 wording narrowed.** [CBP](https://www.cbp.gov/travel/us-citizens/know-before-you-go/know-you-go-traveling-abroad) states the over-USD-10,000 reporting duty for travelers *entering* the US; the site no longer asserts "into or out of" on that source.
4. **Medium — receiving-bank example was an inference.** [Capital One](https://www.capitalone.com/help-center/checking-savings/send-receive-wire-transfer/) names three account types charged USD 15 and says all others are not charged, but never names "360 Checking"; the example now says to confirm your account schedule.
5. **Low — PRC IIT rate table is published as images** on the [State Taxation Administration law page](https://fgk.chinatax.gov.cn/zcfgk/c100009/c5193028/content.html); the seven brackets and quick deductions should be re-checked against those images.
6. **Stale reproducibility link fixed** from a retired session branch to `blob/main/scripts/build_site.py`; the "ATM tariff changes three days after cutoff" note was corrected after the cutoff moved.

**Sources re-fetched and confirmed this session:** [S1](https://www.safe.gov.cn/tianjin/2024/0430/2464.html) SAFE Detailed Rules (Arts. 2, 10–15, 30; Art. 39 repealed), [S2](https://www.safe.gov.cn/tianjin/2024/0430/2465.html) identity definitions (Art. 37: foreign individual = passport holder), [S4](https://pic.bankofchina.com/bocappd/pricelist/202511/P020251110646838136627.pdf) BOC 2025-11-11 tariff (0.1% min ¥50 max ¥260, ¥150 telecom, $15/$25 full arrival, ¥10 permit waived to 2026-12-31, ¥12+1% max ¥112 ATM), [S5](https://www.boc.cn/sourcedb/whpj/enindex.html), [S7](https://www.safe.gov.cn/tianjin/2024/0430/2466.html) cash permits, [S9](https://www.safe.gov.cn/hubei/2019/0305/851.html) ATM caps, [S10](https://www.boc.cn/pbservice/bi2/202608/t20260811_25684907.html) 2026-11-11 ATM change, [S11](https://wise.com/help/articles/2955298/guide-to-cny-transfers) / [S13](https://wise.com/gb/blog/summary-of-fee-changes) Wise caps and dated formulas, [S16](https://www.boc.cn/pbservice/bi2/201801/t20180112_11198459.html) MoneyGram schedule, [S18](https://www.gov.cn/gongbao/content/2008/content_1071846.htm) Decree 532 Arts. 39–45, [S19](https://www.safe.gov.cn/safe/2015/1231/5442.html) watch list, [S20](https://www.gov.cn/gongbao/content/2005/content_64294.htm) property transfer Art. 6, [S25](https://www.irs.gov/businesses/small-businesses-self-employed/report-of-foreign-bank-and-financial-accounts-fbar) FBAR, [S26](https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010/subpart-H/section-1010.821) $16,536 / $165,353, [S27](https://www.irs.gov/businesses/comparison-of-form-8938-and-fbar-requirements) Form 8938 thresholds, [S29](https://www.cbp.gov/travel/us-citizens/know-before-you-go/know-you-go-traveling-abroad) Form 105, [S35](https://www.irs.gov/individuals/international-taxpayers/figuring-the-foreign-earned-income-exclusion) 2026 FEIE $132,900, [S39](https://fgk.chinatax.gov.cn/zcfgk/c100009/c5193028/content.html) IIT law, [S42](https://resources.bankofamerica.com/direct/render-resource/9149a2de7b1047a499ae291815e985e6), [S43](https://www.chase.com/personal/fees/secure-checking), [S44](https://www.capitalone.com/help-center/checking-savings/send-receive-wire-transfer/), [S46](https://www.safe.gov.cn/ningxia/2022/0929/1997.html).

**Verification performed:** clean rebuild (`python3 scripts/build_site.py`), `python3 scripts/validate_site.py` PASS, and a local HTTP smoke test returning 200 for all 9 HTML/redirect pages, `style.css` and `data/cost-model.json`. The validator checks a direct official-source link in every table body row, but link presence does not prove that an external page supports every claim; the defects above were found by fetching and reading the official text, not by the automated check.
