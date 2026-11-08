# Executive summary — China4 evidence desk

- **Research cutoff:** 2026-11-08 UTC
- **BOC retail quote timestamp:** 2026-11-09 05:30 Beijing time

**Current deliverable:** [`index.html`](index.html) · [cost matrices](penalties.html) · [procedures](methods.html) · [open items](flagged.html)

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
| $100,000 | **$271.29** | $61.26 | $210.04 |
| $200,000 | **$481.40** | $61.26 | $420.14 |
| $400,000 | **$902.72** | $61.26 | $841.46 |

Known modeled cost excludes correspondent deductions, account-specific recipient fees, underlying taxes, travel and professional costs. Optional BOC full-arrival pricing is **USD 15 to BOC New York / USD 25 elsewhere**. Receiving examples are BofA USD 15, Chase Secure USD 15 and Capital One 360 Checking USD 0, subject to account terms and waivers.

## Conditional comparisons

- **Wise from CNY:** available only to eligible non-mainland-Chinese users with qualifying work/tax records; recipient must be the sender’s own account. Bank-app funding cap CNY 300,000 per transfer; Alipay funding cap CNY 50,000. Current price requires a live quote. The site separately models Wise’s **dated 2024-11-25** formulas, never as current prices.
- **Domestic-individual annual schedule:** if that identity classification genuinely applies, the illustrative USD 400,000 / eight annual USD 50,000 wires model costs **USD 1,331.53** at constant inputs. This is arithmetic, not advice to split or evade review.
- **Emigration property:** qualifying property must be applied for together. At or below CNY 200,000, one approved remittance may be possible. Larger scenarios model 50% initially, 25% after one year and 25% after two years; USD 400,000 modeled known BOC cost is **USD 1,025.24**, excluding professional/tax costs.
- **Inheritance:** one or multiple remittances may be used after the single application; the mandatory emigration timetable is not incorrectly imposed on inheritance.
- **Property sale:** a foreign individual’s registered sale proceeds require title/transfer and tax evidence; remittance is limited to the seller’s after-tax share.
- **Cash/ATM:** cash above USD 10,000 is generally prohibited except specified SAFE-approved special cases. Domestic-card overseas ATM withdrawals are capped at CNY 100,000 per person/year and CNY 10,000 per card/day. Only the USD 10,000 matrix row fits the ATM annual cap at the planning rate.
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

The build regenerates six main pages, two compatibility redirects and `data/cost-model.json`. The independent validator checks 18 procedures, four 40-row matrices, 47 primary sources, local links, HTML structure and Decimal arithmetic. GitHub Actions repeats the build/validation before deploying the public artifact.
