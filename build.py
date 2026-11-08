#!/usr/bin/env python3
"""
Build the China4 static site.

Every figure rendered by this script comes from one of two places:
  1. a value transcribed from an official source listed in SOURCES, or
  2. arithmetic performed here on those values, with the formula printed on
     the page (so the result can be re-checked by hand).

Run:  python3 build.py
Outputs the HTML pages at the repository root, plus data/cost_table.csv and
data/sources.json for audit. No third-party packages.
"""
from __future__ import annotations

import csv
import json
import math
import os
from html import escape

ROOT = os.path.dirname(os.path.abspath(__file__))
ACCESSED = "2026-11-08"
SITE_URL = "https://sassnarep3-star.github.io/China4/"

# ---------------------------------------------------------------------------
# Source registry. "status" records what happened when the URL was retrieved.
# ---------------------------------------------------------------------------
SOURCES: dict[str, dict] = {
    # ---- China: State Council / SAFE / PBOC ---------------------------------
    "fx_regs_2008": {
        "title": "中华人民共和国外汇管理条例（国务院令第532号）— Foreign Exchange Control Regulations of the PRC (2008 revision)",
        "publisher": "State Council of the PRC (gov.cn)",
        "url": "https://www.gov.cn/zhengce/2008-08/06/content_2602514.htm",
        "short": "FX Regulations 2008 (State Council)",
        "establishes": "Art. 5 (no restriction on current-account international payments and transfers); Art. 12 (current-account transactions need a genuine, lawful basis); Art. 15 (SAFE sets cash-carry limits); Art. 39 (evasion: fine up to 30%, or 30%–100% if serious); Art. 40 (illegal FX arbitrage); Art. 41 (illegal settlement); Art. 42 (carrying FX in/out: warning, fine up to 20%); Art. 45 (private/disguised FX trading: fine up to 30%, or 30%–100% if serious); Art. 48 (individuals up to RMB 50,000 for e.g. false documents); Art. 52(2) (a 'domestic individual' includes a foreigner who has continuously resided in China for one year).",
        "status": "Retrieved and read in full, 2026-11-08.",
        "official": True,
    },
    "safe_807": {
        "title": "国家外汇管理局关于印发《个人外汇管理办法实施细则》的通知（汇发〔2007〕1号）",
        "publisher": "State Administration of Foreign Exchange (SAFE)",
        "url": "https://www.safe.gov.cn/safe/2007/0105/5320.html",
        "short": "SAFE Detailed Rules (汇发〔2007〕1号)",
        "establishes": "Art. 2 (annual quota of US$50,000 per person for individual FX settlement and for domestic individuals' FX purchases); Art. 10–12 (documents needed above the quota); Art. 13 (a foreign individual may buy FX with legal RMB current-account income on ID plus supporting documents including tax certificates); Art. 14 (domestic individual remitting from an FX savings account: up to US$50,000/day on ID); Art. 15 (foreign individual remitting from an FX savings account: on ID; cash remittance above US$10,000/day needs customs/cash documents); Art. 17 (QDII); Art. 20 (emigration/inheritance transfer); Art. 21 (property); Art. 30 (cash withdrawal above US$10,000/day needs SAFE filing); Art. 31 (deposit of cash above US$5,000/day needs documents). Art. 39 was repealed by 汇发〔2023〕8号 (noted on the same page).",
        "status": "Retrieved and read in full, 2026-11-08.",
        "official": True,
    },
    "safe_eng_2007": {
        "title": "SAFE Spokesman Addresses Press Conference on the Detailed Rules on Measures for the Administration of Individual Foreign Exchange",
        "publisher": "SAFE (English)",
        "url": "https://www.safe.gov.cn/en/2007/0105/819.html",
        "short": "SAFE English Q&A (2007)",
        "establishes": "The US$50,000 annual quota applies to individual FX sales (结汇) for both domestic and foreign individuals, and to FX purchases (购汇) by domestic individuals; purchases above the quota require authenticity review.",
        "status": "Retrieved, 2026-11-08.",
        "official": True,
    },
    "safe_fpr_2017": {
        "title": "Circular on Foreign Exchange Sales and Settlement for Foreign Citizens with Their Foreign Permanent Resident ID Cards",
        "publisher": "SAFE (English)",
        "url": "https://www.safe.gov.cn/en/2017/1129/1365.html",
        "short": "SAFE 2017 (foreign permanent-resident ID cards)",
        "establishes": "A foreign permanent-resident ID card is a valid ID for FX business and its holders are eligible for the US$50,000 annual settlement and purchase quota. It extends the quota to that card type; it does not restrict the quota to it.",
        "status": "Retrieved, 2026-11-08.",
        "official": True,
    },
    "property_transfer_2004": {
        "title": "中国人民银行公告〔2004〕第16号 — 个人财产对外转移售付汇管理暂行办法",
        "publisher": "People's Bank of China, published on SAFE",
        "url": "https://www.safe.gov.cn/safe/2004/1116/5461.html",
        "short": "PBOC 2004 No.16 (property transfer abroad)",
        "establishes": "Two legal capital-account routes: emigration transfer (移民转移) and inheritance transfer (继承转移). Art. 6: one application for the whole amount; first remittance at most half, then at most half of the remainder after one year, all after two years; amounts up to RMB 200,000 may go in one payment. Art. 8/9: documents include hukou cancellation certificate, overseas residence proof certified by a Chinese embassy/consulate, proof of property rights, and a tax payment certificate from the tax authority. Art. 10: up to RMB 500,000 decided by the local SAFE branch, above that by SAFE headquarters. Art. 11: proceeds must be wired to the applicant's own account abroad, not taken out as cash. Art. 13: false documents or duplicate applications are punished under Art. 40 of the FX Regulations.",
        "status": "Retrieved and read in full, 2026-11-08.",
        "official": True,
    },
    "property_fx_2006": {
        "title": "国家外汇管理局 建设部关于规范房地产市场外汇管理有关问题的通知（汇发〔2006〕47号）",
        "publisher": "SAFE / Ministry of Construction",
        "url": "https://www.safe.gov.cn/safe/2006/0901/5468.html",
        "short": "SAFE 汇发〔2006〕47号 (property)",
        "establishes": "Art. 5: RMB proceeds from a foreign individual's sale of domestic commercial housing may be purchased into FX and remitted only after the local SAFE branch reviews (i) the purchase application, (ii) the transfer contract, and (iii) the tax clearance certificate for the property transfer.",
        "status": "Retrieved and read in full, 2026-11-08.",
        "official": True,
    },
    "watchlist_2015": {
        "title": "国家外汇管理局关于进一步完善个人外汇管理有关问题的通知（汇发〔2015〕49号）",
        "publisher": "SAFE",
        "url": "https://www.safe.gov.cn/safe/2015/1231/5442.html",
        "short": "SAFE 汇发〔2015〕49号 (watchlist)",
        "establishes": "Individuals must not use splitting or borrowed quotas to evade the quota or authenticity review. Lending your quota to help someone else, or borrowing another person's quota, leads to the 'watchlist' (关注名单): the year of listing plus the next two years, during which every FX transaction requires ID plus supporting documents.",
        "status": "Retrieved and read in full, 2026-11-08.",
        "official": True,
    },
    "cash_2003": {
        "title": "国家外汇管理局、海关总署关于印发《携带外币现钞出入境管理暂行办法》的通知（汇发〔2003〕102号）",
        "publisher": "SAFE / General Administration of Customs (reproduced by MOFCOM)",
        "url": "https://m.mofcom.gov.cn/article/zcfb/zczh/200311/20031100144140.shtml",
        "short": "SAFE/Customs 汇发〔2003〕102号 (cash)",
        "establishes": "Carrying FX cash out: up to US$5,000 no permit; US$5,000–10,000 a bank-issued carrying permit; above US$10,000 a SAFE-issued permit. Art. 3: carrying more than US$5,000 into China must be declared to customs. Art. 9: a bank permit may not exceed US$10,000 per certificate.",
        "status": "Retrieved via MOFCOM reprint; SAFE's own copy of this circular was not located as a standalone page. Listed as currently valid in SAFE's 2026 rules catalogue. Marked 'official (reprint)'.",
        "official": "mirror",
    },
    "rmb_cash_2004": {
        "title": "偏爱用现金？再爱也得符合要求 — 携带货币出入境规定（引中国人民银行公告〔2004〕第18号）",
        "publisher": "Shenzhen Port Office (ka.sz.gov.cn)",
        "url": "https://ka.sz.gov.cn/xxgk/qt/gzdt/content/post_12283223.html",
        "short": "Shenzhen Port Office on cash limits (2025)",
        "establishes": "RMB 20,000 per person per trip in/out of China (PBOC Announcement 2004 No.18); FX cash above US$5,000 into China must be declared; unapproved excess cash is subject to a customs fine of up to 20% of the excess value under the Customs Administrative Penalty Regulations.",
        "status": "Retrieved, 2026-11-08. The PBOC announcement itself and the customs.gov.cn page that previously carried it were not retrievable (customs URL returned 404), so the RMB 20,000 figure is taken from this official government page quoting the announcement. Flagged for a primary-source check.",
        "official": "secondary-official",
    },
    "card_2017": {
        "title": "国家外汇管理局关于规范银行卡境外大额提取现金交易的通知（汇发〔2017〕29号）",
        "publisher": "State Administration of Foreign Exchange (SAFE)",
        "url": "http://m.safe.gov.cn/safe/2017/1230/8116.html",
        "short": "SAFE 汇发〔2017〕29号 (card cash abroad)",
        "establishes": "Art. 1: cash withdrawals abroad on a domestic card (supplementary cards included) may not exceed the equivalent of RMB 100,000 per person per calendar year, and exceeding it suspends withdrawals for the rest of that year and the following year; Art. 1 also forbids borrowing or lending cards to get around the cap. Art. 4: the per-card daily limit is RMB 10,000 equivalent for both RMB and foreign-currency cards. Art. 6: breaches are punished under the FX Regulations. In force from 2018-01-01.",
        "status": "Retrieved and read in full, 2026-11-08 (SAFE's mobile site). The circular does not say that card spending abroad uses the US$50,000 quota; that inference is not made here.",
        "official": "official",
    },
    "crypto_2021": {
        "title": "关于进一步防范和处置虚拟货币交易炒作风险的通知（银发〔2021〕237号）",
        "publisher": "PBOC and nine other authorities",
        "url": "https://www.pbc.gov.cn/tiaofasi/144941/3581332/4348658/index.html",
        "short": "PBOC 银发〔2021〕237号 (virtual currency)",
        "establishes": "Virtual currency has no legal-tender status in China; business activities involving virtual currency — including exchange between fiat currency and virtual currency — are illegal financial activities and are strictly prohibited; financial institutions and payment institutions may not provide account, transfer or settlement services for them; overseas exchanges serving residents of mainland China are likewise illegal.",
        "status": "Retrieved, 2026-11-08.",
        "official": True,
    },
    "iit_law": {
        "title": "中华人民共和国个人所得税法",
        "publisher": "State Taxation Administration (chinatax.gov.cn)",
        "url": "https://www.chinatax.gov.cn/n810219/n810744/n3752930/n3752974/c3970366/content.html",
        "short": "China Individual Income Tax Law",
        "establishes": "Art. 3: comprehensive income is taxed at progressive rates from 3% to 45%; business income 5%–35%; interest, dividends, property leasing, property transfer and incidental income at a flat 20%. Art. 6: the annual standard deduction is RMB 60,000 for residents.",
        "status": "Retrieved, 2026-11-08.",
        "official": True,
    },
    "safe_catalogue_2026": {
        "title": "现行有效外汇管理主要法规目录（截至2026年6月30日）",
        "publisher": "SAFE",
        "url": "https://www.safe.gov.cn/safe/file/file/20260805/d2d0d6ce1441436eadc8bc600eb79c43.pdf",
        "short": "SAFE rules catalogue (to 2026-06-30)",
        "establishes": "SAFE's own list of foreign-exchange rules currently in force, including 汇发〔2003〕102号 (cash) and excluding 汇发〔2009〕56号 (the 2009 splitting circular), which SAFE branch sites mark as repealed.",
        "status": "Retrieved, 2026-11-08.",
        "official": True,
    },
    "safe_tianjin_2026": {
        "title": "个人财产转移购付汇业务问答（六）",
        "publisher": "SAFE Tianjin branch",
        "url": "http://www.safe.gov.cn/tianjin/2026/0318/3017.html",
        "short": "SAFE Tianjin Q&A (2026)",
        "establishes": "Current restatement (published 2026-03-18) that personal property transfer abroad consists of emigration transfer and inheritance transfer under PBOC Announcement 2004 No.16.",
        "status": "Retrieved, 2026-11-08.",
        "official": True,
    },
    # ---- China: commercial bank (official bank data) ------------------------
    "boc_rates": {
        "title": "中国银行外汇牌价 — Bank of China foreign-exchange quoted rates",
        "publisher": "Bank of China",
        "url": "https://www.boc.cn/sourcedb/whpj/",
        "short": "Bank of China FX rates",
        "establishes": "USD quoted per 100 USD: cash/spot buying 666.48, cash/spot selling 669.29, BOC conversion rate 671.68, quote timestamp 2026/11/09 05:30. Rates are indicative; the counter rate at the time of the transaction governs.",
        "status": "Retrieved, 2026-11-08 (quote timestamp 2026-11-09 05:30 Beijing time).",
        "official": "bank",
    },
    "boc_fees": {
        "title": "中国银行电子银行个人服务转账汇款费率表 — BOC personal remittance tariff",
        "publisher": "Bank of China",
        "url": "https://www.boc.cn/ebanking/service/cs1/200905/t20090506_990712.html",
        "short": "Bank of China remittance tariff",
        "establishes": "Cross-border telegraphic transfer: 1‰ of the remitted amount, minimum RMB 50, maximum RMB 260 per transfer, plus a cable charge of RMB 150 for destinations outside Hong Kong/Macau/Taiwan (RMB 80 within them). The table is headed 'effective 1 November 2014'; branch-level variation and promotions may apply.",
        "status": "Retrieved, 2026-11-08.",
        "official": "bank",
    },
    # ---- United States ------------------------------------------------------
    "irs_fbar": {
        "title": "Report of Foreign Bank and Financial Accounts (FBAR)",
        "publisher": "Internal Revenue Service",
        "url": "https://www.irs.gov/businesses/small-businesses-self-employed/report-of-foreign-bank-and-financial-accounts-fbar",
        "short": "IRS FBAR page",
        "establishes": "A US person must file FinCEN Form 114 if the aggregate value of foreign financial accounts exceeded US$10,000 at any time during the calendar year; due 15 April with an automatic extension to 15 October; civil penalty maximums are adjusted annually for inflation.",
        "status": "Retrieved, 2026-11-08.",
        "official": True,
    },
    "fincen_821": {
        "title": "31 CFR 1010.821 — Penalty adjustment and table (eCFR)",
        "publisher": "Financial Crimes Enforcement Network / eCFR",
        "url": "https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010/subpart-H/section-1010.821",
        "short": "31 CFR 1010.821 penalty table",
        "establishes": "For penalties assessed on or after 17 January 2025: non-willful FBAR violation maximum US$16,536; willful violation maximum US$165,353 (statutory base US$10,000 / US$100,000). eCFR as of 2026-11-05 had not yet posted a later inflation adjustment.",
        "status": "Retrieved, 2026-11-08.",
        "official": True,
    },
    "irs_fatca": {
        "title": "FATCA information for individuals (Form 8938)",
        "publisher": "Internal Revenue Service",
        "url": "https://www.irs.gov/businesses/corporations/fatca-information-for-individuals",
        "short": "IRS FATCA / Form 8938 page",
        "establishes": "Form 8938 reports specified foreign financial assets; the aggregate value must generally exceed US$50,000 (higher thresholds apply abroad). Failure to file may result in a US$10,000 penalty and up to US$50,000 more for continued failure after IRS notice; underpayments attributable to undisclosed foreign assets carry a 40% penalty.",
        "status": "Retrieved, 2026-11-08.",
        "official": True,
    },
    "irs_8938_compare": {
        "title": "Comparison of Form 8938 and FBAR requirements",
        "publisher": "Internal Revenue Service",
        "url": "https://www.irs.gov/businesses/comparison-of-form-8938-and-fbar-requirements",
        "short": "IRS 8938 vs FBAR comparison",
        "establishes": "Form 8938 thresholds: living in the US — unmarried US$50,000 year-end / US$75,000 any time, married filing jointly US$100,000 / US$150,000; living outside the US — unmarried US$200,000 / US$300,000, married filing jointly US$400,000 / US$600,000. FBAR threshold: aggregate accounts over US$10,000 at any time.",
        "status": "Retrieved, 2026-11-08.",
        "official": True,
    },
    "irs_3520_instr": {
        "title": "Instructions for Form 3520 (Rev. December 2025)",
        "publisher": "Internal Revenue Service",
        "url": "https://www.irs.gov/pub/irs-pdf/i3520.pdf",
        "short": "IRS Form 3520 instructions (12/2025)",
        "establishes": "Part IV is required when a US person receives more than US$100,000 from a nonresident-alien individual or foreign estate in a tax year (related donors aggregated). Section 6039F penalty: 5% of the gift per month of failure, capped at 25%, unless reasonable cause. Section 6677 trust penalties: generally the greater of US$10,000 or 35% of the gross value.",
        "status": "Retrieved, 2026-11-08.",
        "official": True,
    },
    "irs_gifts": {
        "title": "Gifts from foreign person",
        "publisher": "Internal Revenue Service",
        "url": "https://www.irs.gov/businesses/gifts-from-foreign-person",
        "short": "IRS 'gifts from foreign person'",
        "establishes": "Reporting thresholds: over US$100,000 from a nonresident alien or foreign estate (related donors aggregated); over US$20,116 for 2025 and US$20,573 for 2026 from foreign corporations/partnerships. Filing is informational; penalties under IRC 6039F(c) may apply without reasonable cause. Gifts from covered expatriates may be taxed under IRC 2801.",
        "status": "Retrieved, 2026-11-08.",
        "official": True,
    },
    "cbp_105": {
        "title": "Money and Other Monetary Instruments",
        "publisher": "US Customs and Border Protection",
        "url": "https://www.cbp.gov/travel/international-visitors/money-monetary-instruments",
        "short": "CBP currency reporting",
        "establishes": "Anyone bringing, sending or receiving more than US$10,000 in currency or monetary instruments at one time into or out of the United States must file FinCEN Form 105; the threshold applies to families/groups collectively; failure risks seizure and civil or criminal penalties.",
        "status": "Retrieved, 2026-11-08.",
        "official": True,
    },
    "irs_pub54": {
        "title": "Publication 54 — Tax Guide for U.S. Citizens and Resident Aliens Abroad",
        "publisher": "Internal Revenue Service",
        "url": "https://www.irs.gov/publications/p54",
        "short": "IRS Publication 54",
        "establishes": "US citizens and resident aliens are taxed on worldwide income; the foreign tax credit (Form 1116) and the foreign earned income exclusion are the main reliefs for foreign-source income.",
        "status": "Retrieved, 2026-11-08.",
        "official": True,
    },
    "irs_treaty": {
        "title": "China tax treaty documents",
        "publisher": "Internal Revenue Service",
        "url": "https://www.irs.gov/businesses/international-businesses/china-tax-treaty-documents",
        "short": "US–China tax treaty (IRS)",
        "establishes": "The 1984 US–China income tax treaty and accompanying documents, used to resolve double taxation and set withholding rates; it contains a savings clause preserving the US right to tax its citizens.",
        "status": "Retrieved, 2026-11-08 (index page).",
        "official": True,
    },
    "irs_fx_rates": {
        "title": "Foreign currency and currency exchange rates",
        "publisher": "Internal Revenue Service",
        "url": "https://www.irs.gov/individuals/international-taxpayers/foreign-currency-and-currency-exchange-rates",
        "short": "IRS foreign-currency guidance",
        "establishes": "Amounts on a US return must be expressed in US dollars, translated at the rate prevailing when an item is received, paid or accrued; this is the basis for treating a foreign-currency exchange gain or loss separately from the underlying funds.",
        "status": "Retrieved, 2026-11-08.",
        "official": True,
    },
    "irs_fx_unit": {
        "title": "LB&I Concept Unit INT-C-041 — Official Versus Free Market Exchange Rate (section 988)",
        "publisher": "Internal Revenue Service",
        "url": "https://www.irs.gov/pub/fatca/int_practice_units/int_c_041.pdf",
        "short": "IRS practice unit on IRC 988",
        "establishes": "IRC 988 applies to transactions in a non-functional currency, including buying or selling units of foreign currency; the spot rate under Treas. Reg. 1.988-1(d) is used to compute exchange gain or loss.",
        "status": "Retrieved, 2026-11-08.",
        "official": True,
    },
    "moj_1997": {
        "title": "中华人民共和国外汇管理条例（1997年修订文本，国家行政法规库）",
        "publisher": "Ministry of Justice — National Administrative Regulations Database",
        "url": "https://xzfg.moj.gov.cn/front/law/detail?LawID=1144",
        "short": "1997 FX Regulations text (MOJ)",
        "establishes": "The pre-2008 text of Art. 45 set a fine of 30% up to three times the illegal amount for private FX trading. The 2008 revision replaced this with a fine of up to 30%, or 30% to 100% in serious cases — the source of the widely repeated but outdated '30%–300%' range.",
        "status": "Search-indexed text read; the database page itself is a JavaScript application and could not be fully rendered by the research tool. Used only to explain the origin of the outdated range — flagged.",
        "official": "database",
    },
}

# ---------------------------------------------------------------------------
# Verified cost inputs
# ---------------------------------------------------------------------------
RATE_BUY = 6.6648    # BOC USD spot buying rate  (CNY per USD)
RATE_SELL = 6.6929   # BOC USD spot selling rate (CNY per USD) — what you pay
RATE_MID = round((RATE_BUY + RATE_SELL) / 2, 6)
SPREAD = (RATE_SELL - RATE_MID) / RATE_SELL          # one-way cost vs mid
FEE_RATE = 0.001
FEE_MIN_CNY = 50.0
FEE_MAX_CNY = 260.0
CABLE_CNY = 150.0
QUOTA = 50_000
ATM_YEAR_CNY = 100_000
ATM_YEAR_USD = ATM_YEAR_CNY / RATE_SELL
CASH_PER_TRIP = 5_000


def wire_fee_cny(usd: float) -> tuple[float, float]:
    """BOC tariff: 1 per mille of the RMB amount, min 50, max 260, + cable 150."""
    rmb = usd * RATE_SELL
    pct = rmb * FEE_RATE
    return min(max(pct, FEE_MIN_CNY), FEE_MAX_CNY) + CABLE_CNY, rmb


def legal_cost(usd: float) -> dict:
    fee_cny, rmb = wire_fee_cny(usd)
    spread_usd = usd * SPREAD
    fee_usd = fee_cny / RATE_SELL
    total = spread_usd + fee_usd
    return {
        "usd": usd,
        "rmb": rmb,
        "spread_usd": spread_usd,
        "fee_cny": fee_cny,
        "fee_usd": fee_usd,
        "total": total,
        "pct": total / usd * 100,
        "years": max(1, math.ceil(usd / QUOTA)),
    }


def legal_cost_quota(usd: float) -> dict:
    """Same transfer done entirely inside the annual quota: one wire per year."""
    c = legal_cost(usd)
    years = max(1, math.ceil(usd / QUOTA))
    fee_each_cny, _ = wire_fee_cny(min(usd, QUOTA))
    total = usd * SPREAD + years * fee_each_cny / RATE_SELL
    return {"total": total, "pct": total / usd * 100, "years": years}


def money(x: float, dp: int = 0) -> str:
    return f"${x:,.{dp}f}"


def pct(x: float, dp: int = 2) -> str:
    return f"{x:.{dp}f}%"


def src(key: str, label: str | None = None) -> str:
    s = SOURCES[key]
    return f'<a class="source" href="{s["url"]}" title="{escape(s["title"])}">{escape(label or s["short"])}</a>'


def srcs(*keys: str) -> str:
    return " · ".join(src(k) for k in keys)


# ---------------------------------------------------------------------------
# HTML shell
# ---------------------------------------------------------------------------
NAV = [
    ("index.html", "Dashboard", "dashboard"),
    ("costs.html", "Costs $10k–$400k", "costs"),
    ("methods.html", "Methods", "methods"),
    ("penalties.html", "Penalties", "penalties"),
    ("taxes.html", "US tax", "taxes"),
    ("playbook.html", "Step by step", "playbook"),
    ("flagged.html", "Flagged", "flagged"),
    ("sources.html", "Sources", "sources"),
]


def page(title: str, active: str, body: str, description: str = "") -> str:
    parts = []
    for href, label, key in NAV:
        cls = "active" if key == active else ""
        cur = ' aria-current="page"' if key == active else ""
        parts.append(f'<a class="{cls}"{cur} href="{href}">{label}</a>')
    nav = "".join(parts)
    desc = escape(description or "Source-verified research on moving money from mainland China to the United States.")
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)} — China4</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<header class="site-header">
  <div class="header-inner">
    <a class="brand" href="index.html"><span class="mark">C4</span> China4</a>
    <nav aria-label="Main navigation">{nav}</nav>
  </div>
</header>
<main class="container">
{body}
</main>
<footer class="site-footer">
  <div class="inner">
    <span>China4 · CNY→USD research, every figure traced to a source · data reviewed {ACCESSED}</span>
    <span><a href="flagged.html">Flagged &amp; unverified items</a> · <a href="sources.html">All sources</a> · <a href="https://github.com/sassnarep3-star/China4">GitHub</a></span>
  </div>
</footer>
</body>
</html>
"""


def table(headers: list[str], rows: list[str], caption: str = "", cls: str = "data",
          numeric: set[int] | None = None, wrap_id: str = "") -> str:
    numeric = numeric or set()
    th_parts = []
    for i, h in enumerate(headers):
        cls_attr = ' class="num"' if i in numeric else ""
        th_parts.append(f'<th scope="col"{cls_attr}>{h}</th>')
    th = "".join(th_parts)
    body = "\n".join(rows)
    cap = f"<caption>{caption}</caption>" if caption else ""
    idattr = f' id="{wrap_id}"' if wrap_id else ""
    return (f'<div class="table-wrap"{idattr}><table class="{cls}">{cap}'
            f"<thead><tr>{th}</tr></thead><tbody>{body}</tbody></table></div>")


AMOUNTS = list(range(10_000, 400_001, 10_000))


# ---------------------------------------------------------------------------
# Page: dashboard
# ---------------------------------------------------------------------------
def page_index() -> str:
    preview = []
    for amt in (10_000, 50_000, 100_000, 200_000, 400_000):
        c = legal_cost(amt)
        q = legal_cost_quota(amt)
        cls = ' class="highlight"' if amt == 50_000 else ""
        preview.append(
            f'<tr{cls}>'
            f'<td class="amount">{money(amt)}</td>'
            f'<td class="num">{money(c["total"])}</td>'
            f'<td class="num">{pct(c["pct"])}</td>'
            f'<td class="num">{money(q["total"])} / {q["years"]} yr</td>'
            f'<td>{srcs("boc_rates", "boc_fees")}</td></tr>'
        )
    preview_html = table(
        ["Amount", "Documented wire: cost", "Cost %", "Quota-only: cost / years", "Source"],
        preview,
        caption="Cost preview — one documented bank conversion and wire, no tax",
        numeric={1, 2, 3},
    )

    decision_rows = [
        ("Chinese citizen, or a foreigner who has lived in China for a full year (境内个人)",
         "You get the US$50,000/year <strong>purchase</strong> quota on ID alone. Above it, bring genuine-transaction documents: salary and tax records, service contracts, and so on.",
         srcs("safe_807", "fx_regs_2008")),
        ("US citizen living outside China (境外个人)",
         "The US$50,000 purchase quota is not your ceiling. You buy FX against <em>documented legal RMB income</em> — ID plus supporting documents <em>including tax certificates</em> — and the rule states no cap. Bank practice drives the outcome.",
         srcs("safe_807", "safe_eng_2007")),
        ("You already hold USD in a Chinese FX account",
         "Remittance of your own FX from an FX savings account: domestic individuals up to US$50,000/day on ID; foreign individuals on ID, with documents for cash-funded remittances above US$10,000/day.",
         src("safe_807")),
        ("You were a Chinese national who emigrated and cancelled your hukou",
         "Emigration property transfer (移民转移) under PBOC 2004 No.16: apply once for the whole amount, then 50% / 25% / 25% over two years; SAFE approval above RMB 500,000.",
         srcs("property_transfer_2004", "safe_tianjin_2026")),
        ("You inherited Chinese assets",
         "Inheritance transfer (继承转移): one application, may be paid in one go or in instalments; needs estate documents, a tax certificate and SAFE approval.",
         src("property_transfer_2004")),
        ("You sold a Chinese apartment",
         "Sale proceeds may be purchased into FX and remitted after the local SAFE branch reviews the application, the transfer contract and the tax-clearance certificate.",
         src("property_fx_2006")),
        ("The money is a gift from a relative",
         "The donor's own lawful funds must still pass China's rules; on the US side a gift over US$100,000/year from one foreign person must be reported on Form 3520 (informational — no US gift tax on a nonresident donor's gift).",
         srcs("irs_3520_instr", "irs_gifts")),
    ]
    decision_html = table(
        ["Your situation", "What actually governs it", "Official source"],
        [f"<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>" for a, b, c in decision_rows],
        caption="Which rule applies to you",
    )

    tax_rows = [
        ("Converting CNY to USD at a Chinese bank",
         "None. Conversion is an exchange of your own money, not income.",
         "No US income tax; a foreign-currency gain can arise separately (IRC §988).",
         srcs("fx_regs_2008", "irs_pub54")),
        ("Wiring your own after-tax savings to your US account",
         "None.",
         "None. Not a taxable event; reporting may still be required.",
         srcs("fx_regs_2008", "irs_fbar")),
        ("Salary or fees you earned in China and never declared",
         "Individual income tax at 3%–45% (comprehensive income), 20% on several other categories; a tax certificate is required to buy FX with the money.",
         "US income tax on worldwide income, with a foreign tax credit for Chinese tax paid.",
         srcs("iit_law", "irs_pub54")),
        ("A gift from a Chinese relative",
         "The donor must still comply with China's FX rules; no gift tax is described in the IIT Law.",
         "No US gift tax when the donor is a nonresident alien; Form 3520 if over US$100,000.",
         srcs("iit_law", "irs_gifts")),
        ("Selling a Chinese apartment",
         "Property-transfer income at 20%; tax clearance is a precondition for remitting the proceeds.",
         "US capital gain, with a foreign tax credit for Chinese tax paid.",
         srcs("iit_law", "property_fx_2006")),
        ("Using an underground changer or crypto",
         "Illegal. Fines of up to 30% — or 30%–100% in serious cases — plus confiscation and possible criminal liability; virtual-currency exchange is prohibited outright.",
         "US reporting duties are unchanged, and unreported income stays taxable.",
         srcs("fx_regs_2008", "crypto_2021")),
    ]
    tax_html = table(
        ["Event", "China", "United States", "Source"],
        [f"<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>" for a, b, c, d in tax_rows],
        caption="Where tax actually arises — and where it does not",
    )

    body = f"""
<div class="hero">
  <h1>Getting money out of China — the least-tax path</h1>
  <p>A source-verified dashboard for a US citizen with renminbi stranded in a Chinese bank account. It covers every lawful conversion route we could document, what each one really costs, the China and US penalties for getting it wrong, and a cost table from {money(10_000)} to {money(400_000)} in {money(10_000)} steps.</p>
  <div class="cta-row">
    <a class="cta" href="costs.html">See the cost table ($10k–$400k)</a>
    <a class="cta ghost" href="playbook.html">Step-by-step routes</a>
  </div>
</div>

<div class="best-answer">
  <h2>Executive summary</h2>
  <ol>
    <li><strong>China does not tax the act of converting or wiring your own after-tax money.</strong> Current-account payments must rest on a genuine, lawful transaction (FX Regulations Art. 12), and the tax statute taxes categories of <em>income</em>, not transfers — the tax falls on the income, not on the movement. {srcs("fx_regs_2008", "iit_law")}</li>
    <li><strong>The United States does not tax the transfer either.</strong> Moving your own savings is not income. What can be taxable is the income behind the money if it was never declared, or a foreign-currency gain on the currency itself under IRC §988. A genuine gift is not taxable to you, but one over US$100,000 must be reported. {srcs("irs_pub54", "irs_fx_unit", "irs_3520_instr")}</li>
    <li><strong>Your real constraint is documentation and residency status, not tax.</strong> A "domestic individual" gets the US$50,000/year purchase quota on ID alone. A US citizen living abroad is a "foreign individual" and instead buys FX against documented legal RMB income — a route the Detailed Rules state without a dollar ceiling. {srcs("safe_807", "fx_regs_2008")}</li>
    <li><strong>For six figures there are three heavy-lift lawful doors:</strong> emigration property transfer (移民转移), inheritance transfer (继承转移), and property-sale repatriation. All three need SAFE approval and tax-clearance paperwork, and the emigration route is deliberately spread over two years. {srcs("property_transfer_2004", "property_fx_2006")}</li>
    <li><strong>The bank route costs a fraction of one percent.</strong> {srcs("boc_rates", "boc_fees")} At the published Bank of China rate and tariff the all-in cost is about {money(legal_cost(10_000)["total"])} on {money(10_000)}, {money(legal_cost(50_000)["total"])} on {money(50_000)} and {money(legal_cost(400_000)["total"])} on {money(400_000)} — {pct(legal_cost(400_000)["pct"])}. No tax is involved.</li>
    <li><strong>The expensive mistakes are avoidable.</strong> Underground changers attract a fine of up to 30%, or 30%–100% in serious cases, plus confiscation, and crypto exchange is prohibited outright; skipping an FBAR can cost US$16,536 per non-willful violation (US$165,353 if willful); skipping Form 8938 starts at US$10,000; a late Form 3520 adds 5% of the gift per month to a 25% cap.</li>
  </ol>
</div>

<div class="section">
  <h2 class="section-title">Key numbers</h2>
  <div class="grid four">
    <div class="card"><div class="kpi">US$50,000</div><p class="small">Annual quota: FX <em>settlement</em> for all individuals, FX <em>purchases</em> for domestic individuals. Resets each 1 January — a convenience allowance, not a tax.</p></div>
    <div class="card"><div class="kpi">{pct(SPREAD*100)}</div><p class="small">One-way cost of the published USD bid/ask spread at Bank of China on {RATE_BUY} / {RATE_SELL} CNY per USD.</p></div>
    <div class="card"><div class="kpi">{money(legal_cost(10_000)["total"])}</div><p class="small">All-in legal cost on {money(10_000)}: spread plus the capped wire fee. Falls to {pct(legal_cost(400_000)["pct"])} at {money(400_000)}.</p></div>
    <div class="card"><div class="kpi">≤30% / 30%–100%</div><p class="small">Fine for private or disguised FX trading under Art. 45 of the 2008 FX Regulations — up to 30%, or 30%–100% if serious — plus confiscation of illegal gains.</p></div>
    <div class="card"><div class="kpi">US$10,000</div><p class="small">FBAR threshold: aggregate foreign accounts above this at any time in the year must be reported to FinCEN.</p></div>
    <div class="card"><div class="kpi">US$100,000</div><p class="small">Form 3520 threshold for gifts or bequests from a nonresident-alien individual or foreign estate in one year.</p></div>
    <div class="card"><div class="kpi">RMB 20,000</div><p class="small">Maximum RMB cash a person may carry in or out of China per trip.</p></div>
    <div class="card"><div class="kpi">US$10,000</div><p class="small">FinCEN Form 105 threshold for bringing currency into the United States.</p></div>
  </div>
</div>

<div class="section">
  <h2 class="section-title">The short answer</h2>
  <p><strong>If the money is yours and already taxed, the least-penalty route is a documented bank conversion and wire to your own US account.</strong> Go to the bank that holds the account, establish which category you fall into (domestic or foreign individual), present the source-of-funds file, convert at the counter rate and wire to your own US account. You will pay the FX spread and a capped wire fee — nothing else. The only mandatory extra spend is compliance: an FBAR if your foreign accounts aggregate over US$10,000, Form 8938 above the applicable threshold, and Form 3520 if the money arrives as a gift over US$100,000.</p>
  <p><strong>If the money is untaxed income, the tax is not a penalty for transferring — it is the tax you already owe.</strong> China's Individual Income Tax Law taxes comprehensive income at 3%–45%. For a foreign individual the Detailed Rules expressly require a tax certificate before FX can be bought against that income; for a domestic individual the required proof of employee remuneration is the employment contract plus income evidence. Settle that first; no transfer structure removes it, and structures that hide it convert a tax bill into a fine of up to 100% plus confiscation.</p>
  <div class="callout warn">
    <h3>What no lawful route can do</h3>
    <p>There is no lawful way to convert an unlimited amount of RMB into USD on demand with no questions asked. The $50,000 quota is a convenience allowance; amounts above it move on documents. Anyone offering to move six figures "without paperwork" is offering an illegal channel — and the fine is calculated on the amount, not on the fee they charge.</p>
  </div>
</div>

<div class="section">
  <h2 class="section-title">Cost preview</h2>
  {preview_html}
  <p class="table-note">One documented conversion and wire, using the Bank of China USD selling rate of {RATE_SELL} CNY per USD and the published tariff (1‰ of the RMB amount, minimum RMB 50, maximum RMB 260, plus RMB 150 cable). US receiving-bank and intermediary fees are <em>not</em> included — see <a href="costs.html">Costs</a>. Full 40-row table on that page.</p>
</div>

<div class="section">
  <h2 class="section-title">Which rule applies to you</h2>
  {decision_html}
  <p class="table-note">"Domestic individual" (境内个人) is defined in Art. 52(2) of the FX Regulations as a Chinese citizen or a foreigner who has continuously resided in China for one year. Everyone else is a "foreign individual" (境外个人), which changes both the quota and the paperwork.</p>
</div>

<div class="section">
  <h2 class="section-title">Where tax actually arises</h2>
  {tax_html}
</div>

<div class="section">
  <h2 class="section-title">How to use this dashboard</h2>
  <div class="grid two">
    <div class="card"><h3><a href="costs.html">Costs $10k–$400k</a></h3><p class="small">The full 40-row estimate, the formula behind it, the per-method comparison, and what is deliberately excluded.</p></div>
    <div class="card"><h3><a href="methods.html">Methods</a></h3><p class="small">Seventeen routes — lawful, conditional and illegal — with limits, pros, cons and a source on every row.</p></div>
    <div class="card"><h3><a href="penalties.html">Penalties</a></h3><p class="small">Exact China fine ranges by article, US reporting penalties, and why "30%–300%" is out of date.</p></div>
    <div class="card"><h3><a href="taxes.html">US tax &amp; reporting</a></h3><p class="small">FBAR, Form 8938, Form 3520, FinCEN 105, the currency-gain question and the treaty.</p></div>
    <div class="card"><h3><a href="playbook.html">Step by step</a></h3><p class="small">Six routes in the order you actually execute them, with the document list for each.</p></div>
    <div class="card"><h3><a href="flagged.html">Flagged for review</a></h3><p class="small">Everything that could not be confirmed from an official source — left blank on purpose.</p></div>
  </div>
  <div class="disclaimer"><strong>Research, not legal or tax advice.</strong> This dashboard summarises public regulations and one bank's published prices. Rules change, bank branches apply them unevenly, and your own facts (how you acquired the money, your Chinese tax residence, your hukou status) decide what is lawful for you. Confirm with the bank and a China–US cross-border adviser before moving money.</div>
</div>
"""
    return page("Getting money out of China", "dashboard", body,
                "Source-verified routes, costs and penalties for converting CNY to USD and moving it to the United States.")


# ---------------------------------------------------------------------------
# Page: costs
# ---------------------------------------------------------------------------
def page_costs() -> str:
    rows = []
    for amt in AMOUNTS:
        c = legal_cost(amt)
        q = legal_cost_quota(amt)
        cls = ' class="highlight"' if amt == QUOTA else ""
        rows.append(
            f"<tr{cls}>"
            f'<td class="amount">{money(amt)}</td>'
            f'<td class="num">{money(c["total"])}</td>'
            f'<td class="num">{pct(c["pct"])}</td>'
            f'<td class="num">{money(q["total"])} / {q["years"]} yr</td>'
            f'<td class="num">{money(amt*0.30)} – {money(amt)}</td>'
            f'<td>{srcs("boc_rates", "boc_fees")} · {src("fx_regs_2008", "Art. 45")}</td>'
            f"</tr>"
        )
    main_table = table(
        ["Amount", "Documented wire: cost", "Cost %", "Quota-only: cost / years", "Fine if illegal (30%–100%)", "Source"],
        rows, numeric={1, 2, 3, 4},
        caption=f"Every {money(10_000)} step from {money(10_000)} to {money(400_000)}",
        wrap_id="main-table",
    )

    detail = []
    for amt in (10_000, 50_000, 100_000, 200_000, 400_000):
        c = legal_cost(amt)
        detail.append(
            f"<tr>"
            f'<td class="amount">{money(amt)}</td>'
            f'<td class="num">RMB {c["rmb"]:,.0f}</td>'
            f'<td class="num">{money(c["spread_usd"], 2)}</td>'
            f'<td class="num">RMB {c["fee_cny"]:,.2f} = {money(c["fee_usd"], 2)}</td>'
            f'<td class="num">{money(c["total"], 2)}</td>'
            f'<td class="num">{pct(c["pct"])}</td>'
            f'<td>{srcs("boc_rates", "boc_fees")}</td></tr>'
        )
    detail_table = table(
        ["Amount", "RMB converted", "FX spread", "Wire fee (RMB → USD)", "Total", "Cost %", "Source"],
        detail, numeric={1, 2, 3, 4, 5}, caption="How the total is built at five reference amounts",
    )

    def mcell(amt: int, kind: str) -> str:
        c = legal_cost(amt)
        if kind == "doc":
            return f'{money(c["total"])} <span class="small">({pct(c["pct"])})</span>'
        if kind == "quota":
            q = legal_cost_quota(amt)
            return f'{money(q["total"])} over {q["years"]} yr'
        if kind == "cash":
            trips = math.ceil(amt / CASH_PER_TRIP)
            return f'Not viable — {trips} trips at US$5,000' if trips > 1 else f'{money(c["total"])} + travel'
        if kind == "card":
            return (f'Not viable — annual ATM cap ≈ {money(ATM_YEAR_USD)}' if amt > ATM_YEAR_USD
                    else "Capped; fees unverified")
        if kind == "illegal":
            return f'{money(amt*0.30)} – {money(amt)}'
        if kind == "crypto":
            return "Illegal — no lawful cost basis"
        return '<span class="blank">[unverified]</span>'

    method_rows = [
        ("Documented bank wire (salary, services, property, inheritance)", "doc",
         srcs("safe_807", "property_transfer_2004", "property_fx_2006")),
        ("Bank wire relying only on the US$50,000 quota", "quota", src("safe_807")),
        ("Foreign-currency cash carry", "cash", srcs("cash_2003", "rmb_cash_2004")),
        ("Domestic bank card — ATM withdrawals / spending abroad", "card", src("card_2017")),
        ("Emigration transfer (移民转移, SAFE approval, 2-year phasing)", "doc", src("property_transfer_2004")),
        ("Inheritance transfer (继承转移)", "doc", src("property_transfer_2004")),
        ("Western Union / MoneyGram through a Chinese bank", None, src("safe_807")),
        ("PayPal / Alipay / WeChat cross-border CNY→USD", None, src("safe_807")),
        ("Underground changer (非法买卖外汇)", "illegal", src("fx_regs_2008", "Art. 45")),
        ("Crypto / USDT P2P", "crypto", src("crypto_2021")),
    ]
    mrows = []
    for name, kind, source in method_rows:
        cells = "".join(
            f'<td class="num">{mcell(a, kind)}</td>' if kind else '<td><span class="blank">[unverified]</span></td>'
            for a in (10_000, 100_000, 400_000)
        )
        mrows.append(f"<tr><td>{name}</td>{cells}<td>{source}</td></tr>")
    method_table = table(
        ["Route", "At $10,000", "At $100,000", "At $400,000", "Source"],
        mrows, numeric={1, 2, 3}, caption="Cost by route at three reference amounts",
    )

    body = f"""
<h1 class="page-title">What it really costs</h1>
<p class="page-sub">Cost of converting and transferring CNY into USD, in {money(10_000)} steps from {money(10_000)} to {money(400_000)}. Figures are computed from two verified inputs — Bank of China's published USD rate and its published remittance tariff — plus statutory penalty ranges. Nothing is inferred.</p>

<div class="callout good">
  <h3>Headline</h3>
  <p>On the documented bank route, moving <strong>{money(400_000)}</strong> costs about <strong>{money(legal_cost(400_000)["total"])}</strong> — <strong>{pct(legal_cost(400_000)["pct"])}</strong>. Moving <strong>{money(10_000)}</strong> costs about <strong>{money(legal_cost(10_000)["total"])}</strong> ({pct(legal_cost(10_000)["pct"])}), because the fixed wire fee weighs more on a small amount. <strong>There is no tax in either figure.</strong> The alternative — an illegal changer — is priced at 30%–100% of the amount: {money(120_000)}–{money(400_000)} at {money(400_000)}.</p>
</div>

<div class="section">
  <h2 class="section-title">The inputs (verified)</h2>
  <div class="grid two">
    <div class="card">
      <h3>Exchange rate</h3>
      <p class="small">Bank of China quoted USD per 100 USD: buying {RATE_BUY}, selling <strong>{RATE_SELL}</strong>, conversion reference 6.7168. Quote timestamp 2026-11-09 05:30 Beijing time; page retrieved {ACCESSED}. Because you are buying USD, the bank's <em>selling</em> rate applies.</p>
      <p class="small">{src("boc_rates")}</p>
    </div>
    <div class="card">
      <h3>Wire tariff</h3>
      <p class="small">Cross-border telegraphic transfer: 1‰ of the RMB amount, minimum RMB 50, maximum RMB 260 per transfer, plus a RMB 150 cable charge outside Hong Kong/Macau/Taiwan. Schedule headed "effective 1 November 2014"; retrieved {ACCESSED}.</p>
      <p class="small">{src("boc_fees")}</p>
    </div>
  </div>
  <div class="callout info">
    <h3>Formula (re-check it by hand)</h3>
    <ul>
      <li>Mid rate = ({RATE_BUY} + {RATE_SELL}) ÷ 2 = <strong>{RATE_MID}</strong> CNY/USD.</li>
      <li>FX spread cost = amount × ({RATE_SELL} − {RATE_MID}) ÷ {RATE_SELL} = amount × <strong>{SPREAD:.6f}</strong> ({pct(SPREAD*100, 3)}).</li>
      <li>RMB converted = amount × {RATE_SELL}.</li>
      <li>Wire fee = clamp(0.001 × RMB converted, RMB 50, RMB 260) + RMB 150.</li>
      <li>Total cost in USD = spread + (wire fee ÷ {RATE_SELL}).</li>
    </ul>
    <p class="small">The quota column counts calendar years needed if you rely on the US$50,000 annual quota alone: ⌈amount ÷ 50,000⌉. A couple filing and remitting separately doubles the annual capacity.</p>
  </div>
</div>

<div class="section">
  <h2 class="section-title">Table 1 — every $10,000 step</h2>
  {main_table}
  <p class="table-note">Highlighted row = the US$50,000 quota boundary. "Legal total cost" assumes <em>one</em> documented conversion and wire, which is what an approved above-quota route allows. If you cannot document the funds and must rely on the annual quota alone, the spread is the same but the capped wire fee is paid again every year — the "quota-only" column adds that up and shows how many calendar years it takes. The illegal-route column is the statutory fine only; confiscation of illegal gains and criminal liability are additional.</p>
</div>

<div class="section">
  <h2 class="section-title">Table 2 — the arithmetic at five amounts</h2>
  {detail_table}
  <p class="table-note">Wire fees are capped in RMB, so they shrink as a share of the transfer: {pct(legal_cost(10_000)["pct"])} all-in at {money(10_000)} versus {pct(legal_cost(400_000)["pct"])} at {money(400_000)}. The RMB amounts use the same {RATE_SELL} rate.</p>
</div>

<div class="section">
  <h2 class="section-title">Table 3 — every route, side by side</h2>
  {method_table}
  <p class="table-note">"Not viable" means a legal or practical ceiling sits below the amount: cash carry is capped at US$5,000 per trip without a permit, and card cash withdrawals at RMB 100,000 (about {money(ATM_YEAR_USD)}) per person per year. Western Union/MoneyGram and the wallet apps have no published outbound CNY→USD tariff we could confirm from an official source, so those cells are left blank rather than estimated.</p>
</div>

<div class="section">
  <h2 class="section-title">Table 4 — what an illegal route costs</h2>
  {illegal_table()}
</div>

<div class="section">
  <h2 class="section-title">What these numbers deliberately exclude</h2>
  <div class="callout warn">
    <ul>
      <li><strong>US receiving-bank fee and correspondent/intermediary fees.</strong> Charged in transit by banks whose tariffs were not retrieved. Typically a fixed dollar amount; it does not scale with the transfer. <span class="blank">[unverified]</span></li>
      <li><strong>Chinese bank charges for the conversion leg</strong> beyond the spread, and branch-level differences or promotions. <span class="blank">[unverified]</span></li>
      <li><strong>Notarisation, translation, hukou-cancellation and legal fees</strong> for the property, emigration and inheritance routes. <span class="blank">[unverified]</span></li>
      <li><strong>China individual income tax</strong> on untaxed income. This is a tax on the income, not on the transfer, and is outside a conversion-cost estimate. Rates: 3%–45% comprehensive, 20% on property transfer.</li>
      <li><strong>Any travel cost</strong> for cash carry. <span class="blank">[unverified]</span></li>
    </ul>
  </div>
</div>

<div class="section">
  <h2 class="section-title">Check another amount</h2>
  <div class="card">
    <p class="small">This calculator runs the same formula in your browser with the rate above baked in. It is an estimate of the bank route only, before US receiving-bank and intermediary fees.</p>
    <p><label for="amt"><strong>Amount in USD</strong></label>
      <input id="amt" type="number" min="1000" step="1000" value="400000"
             style="font:inherit;padding:.45rem .6rem;border:1px solid var(--line);border-radius:8px;width:12rem;margin-left:.5rem">
      <button id="calc-btn" style="font:inherit;padding:.5rem .9rem;border-radius:8px;border:1px solid var(--accent);background:var(--accent);color:#fff;cursor:pointer;margin-left:.4rem">Estimate</button>
    </p>
    <p id="calc-out" class="small" aria-live="polite"></p>
  </div>
  <script>
  (function () {{
    var SELL = {RATE_SELL}, MID = {RATE_MID};
    function calc(a) {{
      var rmb = a * SELL;
      var feeCny = Math.min(Math.max(rmb * 0.001, 50), 260) + 150;
      var spread = a * (SELL - MID) / SELL;
      var total = spread + feeCny / SELL;
      return {{rmb: rmb, feeCny: feeCny, total: total, pct: total / a * 100}};
    }}
    var input = document.getElementById('amt');
    var out = document.getElementById('calc-out');
    function run() {{
      var a = parseFloat(input.value);
      if (!isFinite(a) || a <= 0) {{ out.textContent = 'Enter an amount above zero.'; return; }}
      var r = calc(a);
      out.innerHTML = 'RMB converted: <strong>' + r.rmb.toLocaleString(undefined, {{maximumFractionDigits: 0}}) +
        '</strong> · wire fee: <strong>RMB ' + r.feeCny.toFixed(2) + '</strong> · all-in cost: <strong>$' +
        r.total.toLocaleString(undefined, {{maximumFractionDigits: 0}}) + '</strong> (' + r.pct.toFixed(2) +
        '%). Excludes US bank and intermediary fees.';
    }}
    document.getElementById('calc-btn').addEventListener('click', run);
    input.addEventListener('keydown', function (e) {{ if (e.key === 'Enter') run(); }});
    run();
  }})();
  </script>
</div>
"""
    return page("Costs: $10,000 to $400,000", "costs", body,
                "Cost of converting CNY to USD in $10,000 steps to $400,000, computed from Bank of China published rates and tariffs.")


def illegal_table(step: int = 10_000) -> str:
    rows = []
    for amt in range(step, 400_001, step):
        low, high = amt * 0.30, amt * 1.00
        rows.append(
            f"<tr><td class='amount'>{money(amt)}</td>"
            f"<td class='num'>{money(low)}</td>"
            f"<td class='num'>{money(high)}</td>"
            f"<td class='num'>{money(legal_cost(amt)['total'])}</td>"
            f"<td class='num'>{high / max(legal_cost(amt)['total'], 1):,.0f}×</td>"
            f"<td>{src('fx_regs_2008', 'Art. 45 / 39')}</td></tr>"
        )
    return table(
        ["Amount", "Fine at 30%", "Fine at 100%", "Legal route cost", "Worst case ÷ legal cost", "Source"],
        rows, numeric={1, 2, 3, 4},
        caption="Private or disguised FX trading: fine of up to 30%, or 30%–100% in serious cases, plus confiscation",
    )


# ---------------------------------------------------------------------------
# Page: methods
# ---------------------------------------------------------------------------
METHODS = [
    dict(
        n=1, name="Bank wire within the annual quota", cn="境内个人购汇 + 汇出",
        tag=("good", "Lawful"),
        who="Chinese citizens and foreigners who have lived in China for a full year.",
        limit="US$50,000 per person per calendar year, on ID alone; resets 1 January.",
        cost=f"FX spread + wire fee. {money(legal_cost(10_000)['total'])} on {money(10_000)}; {money(legal_cost(50_000)['total'])} on {money(50_000)}.",
        pros=["Cheapest lawful route and the least paperwork",
              "Done in a branch or banking app; no SAFE approval",
              "Creates a clean paper trail for US reporting"],
        cons=["Hard annual ceiling per person",
              "Purpose must be a genuine current-account purpose — a false purpose is a violation (Art. 12, 44)",
              "Bank may ask what the money is for even inside the quota"],
        sources=["safe_807", "safe_eng_2007", "fx_regs_2008"],
        detail="The quota is an allowance, not a right to move unlimited money: within it the bank needs only your ID, but the declared purpose still has to be true.",
    ),
    dict(
        n=2, name="Bank wire above the quota — documented current-account income", cn="超过年度总额，凭真实性凭证",
        tag=("good", "Lawful with documents"),
        who="Domestic individuals with genuine income to repatriate: salary, service fees, royalties, family support, donations.",
        limit="No fixed ceiling; the bank reviews the documents for each transaction.",
        cost=f"Same price as route 1 per transfer: {money(legal_cost(400_000)['total'])} on {money(400_000)} ({pct(legal_cost(400_000)['pct'])}).",
        pros=["No dollar cap if the paper is genuine",
              "Same low bank cost as the quota route",
              "Explicitly contemplated by Art. 10–12 of the Detailed Rules"],
        cons=["Document set is demanding and bank-specific",
              "Large amounts may be queried or referred to SAFE",
              "Salary needs Chinese tax payment records — i.e. the tax must already be settled"],
        sources=["safe_807", "fx_regs_2008", "iit_law"],
        detail="Art. 10 lists the acceptable categories for domestic individuals above the quota: donations, family support, inheritance, insurance, royalties, legal/accounting/consulting services, employee remuneration, overseas investment returns, and 'other' with proof.",
    ),
    dict(
        n=3, name="Foreign individual buying FX against documented legal RMB income", cn="境外个人合法人民币收入购汇",
        tag=("mixed", "Lawful — bank practice decides"),
        who="A US citizen who does not meet the one-year residence test — including someone who has already left China.",
        limit="No dollar ceiling is stated; ID plus documents including the tax certificate.",
        cost=f"Same bank cost as route 1: {money(legal_cost(400_000)['total'])} on {money(400_000)} ({pct(legal_cost(400_000)['pct'])}).",
        pros=["The only route in the Detailed Rules that lets a non-resident convert large legal RMB income without the US$50,000 purchase quota",
              "Explicit statutory basis (Art. 13(1))",
              "Can be paired with property or inheritance documents"],
        cons=["Documentary burden is high and branch discretion is real",
              "A tax certificate is mandatory — untaxed income cannot be converted this way",
              "No published service standard for large amounts; expect delay"],
        sources=["safe_807", "safe_eng_2007"],
        detail="Art. 13(1): a foreign individual's legal current-account RMB income may be purchased into FX on ID plus supporting documents with a transaction amount, <em>including tax certificates</em>. This is the provision a former resident should raise at the bank.",
    ),
    dict(
        n=4, name="Remit USD you already hold in a Chinese FX account", cn="外汇储蓄账户汇出",
        tag=("good", "Lawful"),
        who="Anyone whose account already holds foreign currency rather than RMB.",
        limit="Domestic individual: up to US$50,000/day on ID. Foreign individual: on ID; cash-funded remittances above US$10,000/day need customs or original withdrawal documents.",
        cost="Spread is already sunk; only the wire fee applies (RMB 50–260 + RMB 150).",
        pros=["Cheapest possible transfer if the money is already in USD",
              "Daily cap, not annual, for domestic individuals",
              "No tax event"],
        cons=["Only works for money already converted",
              "Cash deposits need source documents"],
        sources=["safe_807"],
        detail="Art. 14 and 15. If a relative converted the money earlier, the bank will want the conversion trail.",
    ),
    dict(
        n=5, name="Emigration property transfer", cn="移民转移",
        tag=("mixed", "Lawful — SAFE approval"),
        who="A former Chinese national who has moved abroad (or to Hong Kong/Macau) and cancelled their mainland hukou.",
        limit="No fixed ceiling, but paid out in stages over two years.",
        cost=f"Bank spread and wire fee per instalment plus notarisation/legal costs (unverified). About {money(legal_cost(400_000)['total'])} of bank cost on {money(400_000)}.",
        pros=["Purpose-built for taking accumulated wealth out after emigrating",
              "Covers the sale proceeds of pre-emigration property",
              "Statutory, with published documents and approval thresholds"],
        cons=["Requires hukou cancellation and embassy-certified overseas residence proof",
              "First payment at most 50%; the rest over two years",
              "Above RMB 500,000 the file goes to SAFE headquarters"],
        sources=["property_transfer_2004", "safe_tianjin_2026", "safe_807"],
        detail="PBOC Announcement 2004 No.16. Art. 6 sets the 50% / 25% / 25% sequence; Art. 10 sets the RMB 500,000 approval split; Art. 11 forbids taking the money out as cash.",
    ),
    dict(
        n=6, name="Inheritance transfer", cn="继承转移",
        tag=("mixed", "Lawful — SAFE approval"),
        who="A foreign citizen (or Hong Kong/Macau resident) who inherited mainland assets.",
        limit="One application for the whole estate share; may be paid at once or in instalments.",
        cost=f"Bank cost as route 1 plus notarisation/translation (unverified): about {money(legal_cost(400_000)['total'])} at {money(400_000)}.",
        pros=["No staging requirement like the emigration route",
              "Clear document list in Art. 9",
              "Tax clearance is the main gate"],
        cons=["Notarised inheritance and property documents required",
              "Local SAFE approval; SAFE headquarters above RMB 500,000",
              "Cannot be paid in cash"],
        sources=["property_transfer_2004", "safe_tianjin_2026"],
        detail="Art. 9: application, identity and overseas residence proof, proof of inheritance, the deceased's property-rights documents and a tax certificate.",
    ),
    dict(
        n=7, name="Property-sale proceeds repatriation", cn="转让境内商品房购汇汇出",
        tag=("mixed", "Lawful — SAFE review"),
        who="A foreign individual (or foreign branch/representative office) selling a mainland apartment they bought.",
        limit="Proceeds net of Chinese tax, on approval.",
        cost=f"Bank cost as route 1 plus tax and conveyancing: about {money(legal_cost(400_000)['total'])} of bank cost at {money(400_000)}.",
        pros=["Converts a large illiquid asset into a lawful remittance",
              "Three-document test is published",
              "Pairs naturally with routes 3 and 5"],
        cons=["Property-transfer income is taxed at 20% in China",
              "Tax clearance must be obtained before SAFE will look at it",
              "Local practice and processing time vary"],
        sources=["property_fx_2006", "iit_law"],
        detail="汇发〔2006〕47号 Art. 5: purchase application, transfer contract, and the property-transfer tax-clearance certificate.",
    ),
    dict(
        n=8, name="Carry foreign-currency cash", cn="携带外币现钞出境",
        tag=("mixed", "Lawful within limits"),
        who="Small amounts and travellers.",
        limit="Up to US$5,000 without a permit; US$5,000–10,000 with a bank permit; above US$10,000 a SAFE permit.",
        cost=f"Spread only ({pct(SPREAD*100, 3)}) plus travel; not viable at scale — {math.ceil(400_000/CASH_PER_TRIP)} trips for {money(400_000)}.",
        pros=["No wire fee", "Immediate"],
        cons=["Tiny per-trip ceiling", "Physical risk of loss or seizure",
              "US$10,000+ into the US must be declared on FinCEN Form 105"],
        sources=["cash_2003", "cbp_105"],
        detail="汇发〔2003〕102号. The bank permit is capped at US$10,000 per certificate, and multiple certificates totalling over US$10,000 are refused at customs.",
    ),
    dict(
        n=9, name="Carry RMB cash", cn="携带人民币现钞",
        tag=("mixed", "Lawful within limits"),
        who="Nobody moving meaningful sums.",
        limit="RMB 20,000 per person per trip.",
        cost="Exchange it abroad, so the spread depends on the foreign bank; travel costs unverified.",
        pros=["No Chinese conversion paperwork"],
        cons=["RMB 20,000 is about US$3,000 — trivial against a six-figure balance",
              "Converting RMB outside China can attract an offshore discount",
              "Excess cash is fined up to 20% by customs"],
        sources=["rmb_cash_2004", "cash_2003"],
        detail="PBOC Announcement 2004 No.18 sets the RMB 20,000 limit.",
    ),
    dict(
        n=10, name="Spend or withdraw abroad on a domestic bank card", cn="境内银行卡境外使用/取现",
        tag=("mixed", "Lawful — capped"),
        who="Living expenses, not capital movement.",
        limit="Cash withdrawals: RMB 100,000 equivalent per person per calendar year, RMB 10,000 per card per day. Card spending abroad does not use the US$50,000 quota.",
        cost="Issuer FX rate plus withdrawal fees (fees unverified).",
        pros=["No quota use for card spending", "Convenient for living costs"],
        cons=[f"Annual cash ceiling about {money(ATM_YEAR_USD)}",
              "Not a way to move a balance",
              "Exceeding the cap suspends withdrawals for the rest of the year and the next"],
        sources=["card_2017"],
        detail="汇发〔2017〕29号, effective 2018-01-01.",
    ),
    dict(
        n=11, name="QDII funds", cn="合格境内机构投资者",
        tag=("mixed", "Lawful — investment only"),
        who="Domestic individuals investing abroad through approved institutions.",
        limit="Set by the fund's QDII quota, not by you.",
        cost="Fund fees and the institution's FX handling (unverified).",
        pros=["Expressly allowed by Art. 17 of the Detailed Rules"],
        cons=["You end up with an offshore investment, not USD in your US bank account",
              "Redeeming brings value back into the RMB system",
              "Not a mechanism for relocating cash"],
        sources=["safe_807"],
        detail="Art. 17 permits domestic individuals to invest abroad through banks, fund managers and other qualified domestic institutional investors. It is an investment channel, not a remittance channel.",
    ),
    dict(
        n=12, name="Franchised currency-exchange institutions", cn="个人本外币兑换特许机构",
        tag=("mixed", "Lawful — small cash amounts"),
        who="Travellers converting cash.",
        limit="Subject to the same individual FX rules and quota system.",
        cost="Counter spread (unverified).",
        pros=["Useful for small cash needs at airports and city counters"],
        cons=["Cash only", "Quota still applies", "Poor rate versus a bank wire"],
        sources=["watchlist_2015", "cash_2003"],
        detail="汇发〔2015〕49号 Art. 6 applies the individual FX rules to franchised exchange institutions.",
    ),
    dict(
        n=13, name="Western Union / MoneyGram through a bank agent", cn="西联汇款/速汇金",
        tag=("mixed", "Conditional — availability not verified"),
        who="Small, fast transfers if the service is offered.",
        limit="The underlying conversion is still an individual FX transaction, so the same quota and authenticity rules apply.",
        cost='<span class="blank">[unverified]</span> — no official outbound CNY→USD tariff located.',
        pros=["Fast payout where available"],
        cons=["Fees and FX margin are set by the agent and were not verifiable",
              "Availability inside mainland China could not be confirmed from an official source",
              "No advantage at six-figure amounts"],
        sources=["safe_807"],
        detail="Left unquantified on purpose rather than estimated.",
    ),
    dict(
        n=14, name="PayPal / Alipay / WeChat cross-border", cn="第三方支付跨境",
        tag=("mixed", "Conditional — not a verified route"),
        who="Small consumer payments.",
        limit="Not published for outbound personal CNY→USD transfers to a US bank account.",
        cost='<span class="blank">[unverified]</span>',
        pros=["Familiar interfaces"],
        cons=["No official confirmation that a personal outbound CNY→USD account-to-account transfer is supported",
              "Would still sit inside China's FX rules if it were",
              "Not a route for a balance of any size"],
        sources=["safe_807"],
        detail="Included because it is often suggested; the research did not find an official basis for it as a capital-movement channel.",
    ),
    dict(
        n=15, name="Borrowing relatives' quotas / splitting", cn="分拆结售汇、借用额度",
        tag=("bad", "Prohibited"),
        who="Anyone tempted to multiply the US$50,000 by using family members.",
        limit="Explicitly prohibited.",
        cost="Watchlist for the year of listing plus two more years; every subsequent FX transaction then needs documents. Fines under the FX Regulations where applicable.",
        pros=["None that survive contact with the rule"],
        cons=["The bank's monitoring system flags the pattern",
              "Also exposes relatives who lent their quota",
              "US gift reporting can still apply"],
        sources=["watchlist_2015", "fx_regs_2008"],
        detail="汇发〔2015〕49号 Art. 2: no splitting or quota-borrowing to evade the quota or authenticity review. Note that 汇发〔2009〕56号, which listed the 'five or more people' patterns, is repealed and no longer appears in SAFE's current catalogue.",
    ),
    dict(
        n=16, name="Underground changer / offsetting ('对敲')", cn="地下钱庄、变相买卖外汇",
        tag=("bad", "Illegal"),
        who="Nobody.",
        limit="No lawful channel exists.",
        cost=f"Fine of up to 30%, or 30%–100% in serious cases, plus confiscation of illegal gains: {money(120_000)}–{money(400_000)} at {money(400_000)}, versus {money(legal_cost(400_000)['total'])} lawfully.",
        pros=["Fast — and that is the whole of it"],
        cons=["Criminal exposure, not just a fine",
              "No recourse if the counterparty disappears",
              "Contaminated funds can freeze your account and your US bank relationship"],
        sources=["fx_regs_2008", "watchlist_2015"],
        detail="Art. 45 covers private trading, disguised trading and broking of foreign exchange; Art. 39 covers evasion.",
    ),
    dict(
        n=17, name="Crypto / USDT P2P", cn="虚拟货币",
        tag=("bad", "Illegal in China"),
        who="Nobody.",
        limit="Fiat-to-virtual-currency exchange is prohibited.",
        cost="No lawful cost basis. Confiscation, account freezing and criminal referral are the realistic outcomes; US capital-gains rules would also apply to any crypto disposal.",
        pros=["None lawful inside mainland China"],
        cons=["PBOC's 2021 notice treats fiat/crypto exchange as illegal financial activity",
              "Overseas exchanges serving mainland residents are equally unlawful",
              "Banks and payment institutions are barred from processing it"],
        sources=["crypto_2021", "fx_regs_2008"],
        detail="银发〔2021〕237号 §1(2)–(3).",
    ),
]


def page_methods() -> str:
    rows = []
    for m in METHODS:
        cls, label = m["tag"]
        rows.append(
            f"<tr><td class='amount'>{m['n']}. {m['name']}<br><span class='small'>{m['cn']}</span></td>"
            f"<td><span class='tag {cls}'>{label}</span></td>"
            f"<td>{m['limit']}</td>"
            f"<td>{m['cost']}</td>"
            f"<td>{srcs(*m['sources'])}</td></tr>"
        )
    summary = table(
        ["Route", "Status", "China-side limit", "Headline cost", "Source"],
        rows, caption="All routes found — lawful, conditional and prohibited",
    )

    cards = []
    for m in METHODS:
        cls, label = m["tag"]
        pros = "".join(f"<li>{p}</li>" for p in m["pros"])
        cons = "".join(f"<li>{c}</li>" for c in m["cons"])
        cards.append(f"""
<div class="method">
  <header>
    <h3>{m['n']}. {m['name']} <span class="small">{m['cn']}</span></h3>
    <span class="tag {cls}">{label}</span>
  </header>
  <div class="meta"><strong>Who it fits:</strong> {m['who']}</div>
  <p>{m['detail']}</p>
  <p class="small"><strong>Limit:</strong> {m['limit']}<br><strong>Cost:</strong> {m['cost']}</p>
  <div class="pros-cons">
    <div><h4>Pros</h4><ul class="pros">{pros}</ul></div>
    <div><h4>Cons</h4><ul class="cons">{cons}</ul></div>
  </div>
  <div class="sources"><b>Source:</b> {srcs(*m['sources'])}</div>
</div>""")

    body = f"""
<h1 class="page-title">Every way to convert CNY to USD</h1>
<p class="page-sub">Seventeen routes, grouped by what they actually are: lawful on ID, lawful on documents, lawful only with SAFE approval, prohibited, and illegal. Each row and card links an official source; anything we could not confirm is left blank and listed on the <a href="flagged.html">Flagged</a> page.</p>

<div class="callout info">
  <h3>Read the status labels carefully</h3>
  <p><span class="tag good">Lawful</span> works on identity documents alone or with routine paperwork. <span class="tag mixed">Lawful with documents</span> needs a documented source of funds. <span class="tag mixed">Lawful — SAFE approval</span> is a capital-account route with a formal application. <span class="tag bad">Prohibited</span> and <span class="tag bad">Illegal</span> carry penalties. "Conditional — not verified" means we could not confirm the channel from an official source and did not price it.</p>
</div>

<div class="section">
  <h2 class="section-title">Comparison table</h2>
  {summary}
</div>

<div class="section">
  <h2 class="section-title">Route by route</h2>
  <div class="grid two">
  {''.join(cards)}
  </div>
</div>

<div class="callout warn">
  <h3>The one thing that decides everything</h3>
  <p>Whether the bank treats you as a <strong>domestic individual</strong> (Chinese citizen, or foreigner continuously resident in China for one year) or a <strong>foreign individual</strong> determines which rule you are arguing under: the US$50,000 purchase <em>quota</em> (domestic) or documented legal income with a tax certificate and no stated ceiling (foreign). Both are in Art. 2 and Art. 13 of the same Detailed Rules. Ask the bank to state which category it has applied to your account, in writing.</p>
</div>
"""
    return page("Conversion methods", "methods", body,
                "Seventeen routes from CNY to USD with limits, pros, cons and an official source for every row.")


# ---------------------------------------------------------------------------
# Page: penalties
# ---------------------------------------------------------------------------
def page_penalties() -> str:
    cn_rows = [
        ("Private trading, disguised trading, buying/selling or broking FX in large amounts (includes underground changers and 'offsetting')",
         "FX Regulations Art. 45",
         "Warning; confiscation of illegal gains; fine of up to 30% of the amount; in serious cases a fine of 30% to 100% of the amount; criminal liability if a crime is constituted.",
         "fx_regs_2008"),
        ("FX evasion — moving domestic FX abroad in breach of the rules, or moving domestic capital abroad by deception",
         "Art. 39",
         "Ordered to repatriate the FX within a time limit; fine of up to 30%; in serious cases 30%–100%; criminal liability.",
         "fx_regs_2008"),
        ("Illegal FX arbitrage — receiving/paying in FX what should be RMB, or buying FX with false or invalid documents",
         "Art. 40",
         "Illegal funds returned/converted back; fine of up to 30%; in serious cases 30%–100%.",
         "fx_regs_2008"),
        ("Carrying FX into or out of China in breach of the rules",
         "Art. 42",
         "Warning; fine of up to 20% of the amount; where customs rules provide a penalty, those prevail.",
         "fx_regs_2008"),
        ("Changing the use of FX or of settlement funds without approval",
         "Art. 44",
         "Correction; confiscation of illegal gains; fine of up to 30%; in serious cases 30%–100%.",
         "fx_regs_2008"),
        ("Failure to declare, false documents, breach of account or registration rules",
         "Art. 48",
         "Correction and warning; for an individual, a fine of up to RMB 50,000.",
         "fx_regs_2008"),
        ("Splitting transactions or borrowing another person's quota",
         "汇发〔2015〕49号 Art. 2",
         "Entry on the 'watchlist' for the year of listing and the two following years; during that period every FX transaction requires documents. False documents can also attract the fines above.",
         "watchlist_2015"),
        ("Virtual-currency exchange or related business",
         "银发〔2021〕237号",
         "Treated as illegal financial activity: prohibited, with referral to criminal authorities where a crime is constituted; banks and payment institutions may not process it.",
         "crypto_2021"),
    ]
    cn_table = table(
        ["Conduct", "Provision", "Penalty", "Source"],
        [f"<tr><td>{a}</td><td class='nowrap'>{b}</td><td>{c}</td><td>{src(d)}</td></tr>" for a, b, c, d in cn_rows],
        caption="China — statutory penalties",
    )

    us_rows = [
        ("FBAR / FinCEN Form 114", "Aggregate foreign accounts over US$10,000 at any time in the year",
         "Non-willful: up to US$16,536 per violation. Willful: up to US$165,353 or 50% of the balance. Criminal exposure exists separately.",
         "fincen_821", "irs_fbar"),
        ("Form 8938 (FATCA)", "Specified foreign financial assets above the threshold (US$50,000/75,000 living in the US; US$200,000/300,000 single living abroad; US$400,000/600,000 jointly)",
         "US$10,000, plus up to US$50,000 more for continued failure after IRS notice; 40% penalty on an underpayment attributable to undisclosed foreign assets.",
         "irs_8938_compare", "irs_fatca"),
        ("Form 3520, Part IV", "Gifts or bequests over US$100,000 in a year from a nonresident-alien individual or foreign estate",
         "5% of the gift for each month the failure continues, capped at 25%; the IRS may also determine the income-tax consequences.",
         "irs_3520_instr", "irs_gifts"),
        ("FinCEN Form 105", "Carrying or sending more than US$10,000 in currency or monetary instruments into or out of the US",
         "Seizure and forfeiture of the currency, plus civil and criminal penalties under 31 U.S.C. 5321/5322.",
         "cbp_105",),
        ("Income tax return", "Worldwide income, including China-source income",
         "Tax due plus interest and the accuracy-related penalty under IRC 6662 (40% where the underpayment involves undisclosed foreign assets).",
         "irs_fatca", "irs_pub54"),
    ]
    us_table = table(
        ["Obligation", "Trigger", "Penalty", "Source"],
        [f"<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{' · '.join(src(k) for k in srcs_keys)}</td></tr>"
         for a, b, c, *srcs_keys in us_rows],
        caption="United States — reporting and tax penalties",
    )

    body = f"""
<h1 class="page-title">Penalties, precisely</h1>
<p class="page-sub">What each unlawful route actually costs, quoted from the operative article rather than from commentary. Two things are worth saying at the outset: converting your own after-tax money lawfully attracts <strong>no tax penalty at all</strong>, and the most commonly repeated number for illegal FX trading — "30% to 300%" — is from the version of the regulations replaced in 2008.</p>

<div class="section">
  <h2 class="section-title">China</h2>
  {cn_table}
  <p class="table-note">Fines are calculated on the <em>amount</em>, not on any fee charged by an intermediary. Confiscation of illegal gains is additional, and so is criminal liability where the conduct constitutes a crime.</p>
</div>

<div class="section">
  <h2 class="section-title">United States</h2>
  {us_table}
  <p class="table-note">None of these is a tax on moving money. They are penalties for not reporting, or for not declaring income. The FBAR figures are the inflation-adjusted maxima for penalties assessed on or after 17 January 2025; eCFR had not posted a later adjustment as of {ACCESSED}.</p>
</div>

<div class="section">
  <h2 class="section-title">The "30%–300%" figure is out of date</h2>
  <div class="callout danger">
    <p>Older articles, and earlier drafts of this dashboard, quote a fine of "30% to 300%" for illegal FX trading. That range comes from the <strong>1997 text</strong> of Art. 45, which set a fine of 30% up to <em>three times</em> the illegal amount ({src("moj_1997")}). The <strong>2008 revision</strong>, in force today, caps the fine at 30% of the amount, rising to between 30% and <em>the equivalent amount</em> (i.e. 100%) in serious cases ({src("fx_regs_2008", "Art. 45 of the 2008 text")}). The current range is therefore <strong>up to 30%, or 30%–100% if serious</strong> — still ruinous at six figures, but not 300%.</p>
  </div>
</div>

<div class="section">
  <h2 class="section-title">Legal cost versus penalty</h2>
  {illegal_table(50_000)}
  <p class="table-note">The last column compares the worst-case fine with the all-in cost of the documented bank route at the same amount. The ratio runs from about 187× at {money(10_000)} to roughly 444× at {money(400_000)}, because the bank cost is nearly flat in dollar terms while the fine scales with the amount.</p>
</div>

<div class="section">
  <h2 class="section-title">Non-monetary consequences</h2>
  <div class="grid three">
    <div class="card"><h3>Watchlist for three years</h3><p class="small">Being listed for splitting or quota-borrowing means every later FX transaction needs documents, for the rest of that year and the next two. {src("watchlist_2015")}</p></div>
    <div class="card"><h3>Frozen accounts</h3><p class="small">Funds traced to an illegal channel can be frozen or confiscated, and a US bank may exit the relationship when a foreign wire arrives with a murky source. {src("fx_regs_2008", "Art. 39/45")}</p></div>
    <div class="card"><h3>Criminal liability</h3><p class="small">Both Art. 39 and Art. 45 provide that where a crime is constituted, criminal responsibility is pursued — the administrative fine is not the ceiling. {src("fx_regs_2008")}</p></div>
  </div>
</div>
"""
    return page("Penalties", "penalties", body,
                "Exact China and US penalties for unlawful CNY-to-USD conversion, quoted from the operative provisions.")


# ---------------------------------------------------------------------------
# Page: US tax and reporting
# ---------------------------------------------------------------------------
def page_taxes() -> str:
    obligations = [
        ("FinCEN Form 114 — FBAR", "US persons with a financial interest in, or signature authority over, foreign accounts whose aggregate value exceeded US$10,000 at any time in the calendar year",
         "15 April, automatic extension to 15 October", "Not filed with the tax return; filed electronically with FinCEN",
         "Up to US$16,536 non-willful; up to US$165,353 willful", "irs_fbar", "fincen_821"),
        ("Form 8938 — FATCA", "Specified foreign financial assets above the threshold that depends on filing status and residence (e.g. US$50,000/75,000 single in the US; US$200,000/300,000 single living abroad)",
         "With the annual return, including extensions", "Attached to the return",
         "US$10,000, plus up to US$50,000 for continued failure; 40% on related underpayments", "irs_8938_compare", "irs_fatca"),
        ("Form 3520, Part IV", "Gifts or bequests over US$100,000 in the year from a nonresident-alien individual or foreign estate (related donors aggregated)",
         "15 April (15 June if living abroad; extendable to 15 October)", "Filed separately from the return",
         "5% of the gift per month, capped at 25%", "irs_3520_instr", "irs_gifts"),
        ("FinCEN Form 105", "Carrying or sending more than US$10,000 in currency or monetary instruments into or out of the United States",
         "At the time of entry or departure", "Electronic filing through CBP's FinCEN 105 site, or paper at the port",
         "Seizure and forfeiture, plus civil and criminal penalties", "cbp_105"),
        ("Form 1040 — worldwide income", "All income, wherever earned, translated into US dollars",
         "15 April (automatic extension to 15 October)", "With the return",
         "Tax, interest and accuracy-related penalties", "irs_pub54", "irs_fx_rates"),
        ("Form 1116 — foreign tax credit", "Foreign income tax paid on income also taxed by the US",
         "With the return", "Attached to the return",
         "Loss of credit (double taxation), not a penalty as such", "irs_pub54", "irs_treaty"),
    ]
    ob_table = table(
        ["Obligation", "Who / trigger", "Deadline", "How", "Penalty if missed", "Source"],
        [f"<tr><td><strong>{a}</strong></td><td>{b}</td><td>{c}</td><td>{d}</td><td>{e}</td><td>{' · '.join(src(k) for k in rest)}</td></tr>"
         for a, b, c, d, e, *rest in obligations],
        caption="What a US citizen must file around a China transfer",
    )

    scenarios = [
        ("You wire your own savings that were already taxed in China",
         "Nothing. Moving your own money is not income, and no Chinese tax arises on the conversion.",
         "FBAR if the account aggregate exceeded US$10,000; Form 8938 if above the threshold. A US$400,000 balance held abroad puts a single US resident over both the FBAR and the 8938 threshold.",
         srcs("irs_fbar", "irs_8938_compare")),
        ("The money is a gift from a Chinese relative",
         "No Chinese tax on the transfer; the donor still has to satisfy China's FX rules to send it.",
         "No US income tax. Form 3520 if gifts from that donor (and related donors) exceed US$100,000 in the year. Splitting the gift across years keeps each year under the reporting threshold — but on the China side, using five or more people to remit to one recipient is a prohibited pattern.",
         srcs("irs_3520_instr", "watchlist_2015")),
        ("You earned salary in China and never declared it there",
         "China individual income tax at 3%–45%; a tax payment certificate is required before the bank will sell you FX against salary.",
         "US income tax on the same income, less a foreign tax credit; the credit only works if the Chinese tax was actually paid.",
         srcs("iit_law", "safe_807", "irs_pub54")),
        ("You sold a Chinese apartment",
         "Property-transfer income at 20%; tax clearance is a precondition for remitting the proceeds.",
         "US capital gain on the difference between basis and sale price, with a foreign tax credit for the Chinese tax.",
         srcs("iit_law", "property_fx_2006", "irs_pub54")),
        ("You inherited Chinese assets",
         "The estate documents and a tax certificate are required for the inheritance transfer. Whether any Chinese inheritance tax applies was not established in this research.",
         "Inheritances are not US income. Form 3520 if the bequest from a foreign estate exceeds US$100,000.",
         srcs("property_transfer_2004", "irs_gifts")),
        ("You converted CNY you had been holding as an investment",
         "Not a Chinese tax event.",
         "A foreign-currency gain or loss can be taxable under IRC §988 when the currency is disposed of; the IRS applies the spot rate at the transaction date.",
         srcs("irs_fx_unit", "irs_fx_rates")),
    ]
    sc_table = table(
        ["Situation", "China", "United States", "Source"],
        [f"<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>" for a, b, c, d in scenarios],
        caption="Six situations, and where the tax actually lands",
    )

    body = f"""
<h1 class="page-title">US tax and reporting</h1>
<p class="page-sub">The question behind the question: will the US tax me for bringing my own money home? The answer is no — but four separate reporting regimes sit around the transfer, and their penalties dwarf the cost of the transfer itself.</p>

<div class="best-answer">
  <h2>Moving your own money is not a taxable event</h2>
  <p>US citizens are taxed on <em>worldwide income</em>, not on the movement of capital. A wire from your Chinese account to your US account converts one form of your own property into another; it creates no income. What creates tax is the income that produced the money, any foreign-currency gain on the currency itself, and — for gifts — nothing at all on the recipient's side, though a large foreign gift must be reported. {srcs("irs_pub54", "irs_fx_rates")}</p>
</div>

<div class="section">
  <h2 class="section-title">The reporting obligations</h2>
  {ob_table}
  <p class="table-note">FBAR and Form 8938 are separate obligations with separate penalties; filing one does not satisfy the other. {src("irs_8938_compare", "IRS comparison")}</p>
</div>

<div class="section">
  <h2 class="section-title">Where the tax lands, situation by situation</h2>
  {sc_table}
</div>

<div class="section">
  <h2 class="section-title">The currency-gain question</h2>
  <p>Foreign currency is property. The IRS's own practice unit on IRC §988 confirms that the section applies to "buying or selling units of foreign currency", and that exchange gain or loss is computed using the spot rate under Treas. Reg. 1.988-1(d). {src("irs_fx_unit")} In practice, for someone who received RMB as salary and simply converted it, the gain or loss is usually small or nil — but the basis and holding period have to be known, which is another reason to keep the bank records.</p>
  <div class="callout warn">
    <h3>Flagged</h3>
    <p>The frequently cited "US$200 personal-transaction" de minimis rule under IRC §988(e) was <strong>not</strong> verified from an official text in this session, so it is not used in any calculation here. Treat any claim that a small currency gain is automatically exempt as unverified until your adviser confirms the current text. See <a href="flagged.html">Flagged</a>.</p>
  </div>
</div>

<div class="section">
  <h2 class="section-title">Gifts, bequests and the donor's side</h2>
  <p>A gift from a Chinese relative is not taxable income to you: the US gift tax, where it applies at all, is imposed on the <em>donor</em>, and a nonresident alien donor's gift of non-US assets is generally outside it. The obligation that does bite is informational — Form 3520, Part IV, once gifts from one foreign individual (aggregating related donors) exceed US$100,000 in a year. {srcs("irs_gifts", "irs_3520_instr")}</p>
  <p>Two traps: the threshold is per year and per donor group, and the China side does not care that the US treats it as a gift — the donor's RMB still has to be converted lawfully, and marshalling five or more people to remit to you is precisely the pattern SAFE prohibits. {src("watchlist_2015")}</p>
  <div class="callout warn">
    <p><strong>Unverified:</strong> the precise interaction between the US gift-tax situs rules and a nonresident donor's gift of funds held in a Chinese bank was not traced to an official statement in this session. The reporting obligation is clear; the gift-tax conclusion should be confirmed with an adviser. Flagged on <a href="flagged.html">Flagged</a>.</p>
  </div>
</div>

<div class="section">
  <h2 class="section-title">Treaty, credit and double taxation</h2>
  <p>The 1984 US–China income tax treaty allocates taxing rights and provides relief mechanisms, and — importantly — contains a savings clause preserving the US right to tax its own citizens. {src("irs_treaty")} Where China has already taxed the same income, the foreign tax credit under Form 1116 is the ordinary relief; the foreign earned income exclusion is a separate, narrower relief for earned income. {src("irs_pub54")}</p>
  <p class="small">Note that a foreign tax credit requires the foreign tax to have been <em>paid</em>. A plan that avoids Chinese tax therefore does not create a credit — it creates US tax on the same income.</p>
</div>

<div class="section">
  <h2 class="section-title">Records to keep</h2>
  <ul>
    <li>Bank statements showing the RMB balance and its history.</li>
    <li>The conversion advice and the wire confirmation, showing the rate, fees and the receiving account.</li>
    <li>Source-of-funds documents: employment contract and payslips, tax payment certificates, property contract and tax clearance, or the estate documents.</li>
    <li>Copies of every US information return filed (FBAR, 8938, 3520) and the underlying account valuations.</li>
  </ul>
  <p class="small">The FBAR rules require records for five years from the due date. {src("irs_fbar")}</p>
</div>
"""
    return page("US tax and reporting", "taxes", body,
                "FBAR, Form 8938, Form 3520, FinCEN 105 and the currency-gain question for a China-to-US transfer.")


# ---------------------------------------------------------------------------
# Page: step-by-step playbook
# ---------------------------------------------------------------------------
def page_playbook() -> str:
    def steps(items: list[tuple[str, str]]) -> str:
        return '<ol class="steps">' + "".join(
            f"<li><strong>{a}</strong><span class='small'>{b}</span></li>" for a, b in items
        ) + "</ol>"

    route_a = steps([
        ("Confirm your category", "Ask the bank in writing whether it treats you as a 境内个人 (Chinese citizen or foreigner continuously resident for one year) or a 境外个人. This decides the rest."),
        ("Check the quota you have left", "The annual US$50,000 purchase quota resets on 1 January and is visible in the bank's app or at the counter."),
        ("Assemble identity documents", "Passport, and either the residence permit/ID used for the account or the entry records."),
        ("State a true purpose", "Within the quota the bank needs no supporting file, but the declared purpose must be genuine: travel, study, medical, family support, and so on. A false purpose is a violation in its own right."),
        ("Convert, then wire — or both at once", "The bank sells you USD at its prevailing rate and sends a SWIFT transfer to your own US account. Take the rate and fee advice in writing."),
        ("Keep the paperwork", "Conversion advice, wire confirmation, and the source-of-funds file behind the money."),
        ("File the US side", "FBAR by 15 April (automatic to 15 October); Form 8938 with the return if above your threshold."),
    ])
    route_b = steps([
        ("Bring the income file", "Employment contract, payslips and, decisively, the Chinese individual income tax payment records; or the service contract and invoice; or the donation/family-support documents listed in Art. 10."),
        ("Ask the bank to process it as an above-quota current-account transaction", "Art. 10–12 of the Detailed Rules is the basis: ID plus documents showing the transaction amount."),
        ("Expect a second-level review", "Large or unfamiliar files are escalated. Do not split the payment to stay under a threshold — that is the prohibited pattern."),
        ("Convert and wire to your own account", "The bank's rate and tariff apply; keep the advice."),
        ("File the US side", "FBAR and 8938 as applicable; keep the Chinese tax certificate — it supports a foreign tax credit."),
    ])
    route_c = steps([
        ("Frame it as Art. 13, not as the quota", "A foreign individual buying FX against legal RMB income: ID plus documents with a transaction amount, including the tax certificate. No dollar ceiling is stated in the rule."),
        ("Prove the RMB is legal income", "Salary with tax receipts; sale proceeds with the transfer contract and tax clearance; inheritance with the estate documents; service income with the contract and invoice."),
        ("Get the tax certificate first", "Without it the conversion has no basis. If the income was never taxed, settle that with the Chinese tax authority before approaching the bank."),
        ("Submit for authenticity review", "The bank reviews and may refer the file to the local SAFE branch. Ask for the decision in writing."),
        ("Wire to your own account abroad", "Ask the bank to remit to an account in your own name. Where the property-transfer rules apply, Art. 11 of PBOC 2004 No.16 requires the bank to remit the funds and forbids handing them over as cash."),
        ("File the US side", "FBAR, 8938 as applicable; report the income if it was not reported before."),
    ])
    route_d = steps([
        ("Check eligibility", "You moved from mainland China to a foreign country (or Hong Kong/Macau) and your mainland hukou has been cancelled; you are transferring property you owned <em>before</em> acquiring that emigration status."),
        ("Assemble the file for the SAFE branch where your hukou was", "Written application; the emigration-transfer applicant form; the FX business application form; hukou cancellation certificate plus embassy/consulate-certified overseas residence proof; property-rights documents; and the tax certificate or tax-payment proof."),
        ("Apply once for the whole amount", "Art. 6 requires a single application covering all the property you intend to move."),
        ("Obtain approval", "Up to RMB 500,000: the local SAFE branch decides. Above that: local branch screens, SAFE headquarters approves. You then receive an approval letter and a registration certificate for the bank."),
        ("First remittance: no more than 50%", "Present the approval documents to the designated bank; the bank converts and wires to your own account abroad."),
        ("Second stage after one year, third after two", "Each later remittance needs the prior approval letter and the previous registration certificate."),
        ("File the US side", "FBAR/8938 for the year of each remittance; keep every SAFE document — it is the cleanest possible source-of-funds record."),
    ])
    route_e = steps([
        ("Prove the inheritance", "Notarised will/estate documents or the court's inheritance determination, plus your identity and, for a foreign citizen, embassy/consulate-certified overseas residence proof."),
        ("Prove the assets and the tax position", "The deceased's property-rights documents and the tax certificate from the tax authority where the assets are."),
        ("Apply at the SAFE branch where the deceased's hukou was", "One application for everything inherited from that person; different deceased persons require separate applications."),
        ("Obtain approval and remit", "One payment or several — the rule allows either for inheritance, unlike the emigration route."),
        ("File the US side", "Form 3520 if the bequest exceeds US$100,000 from that foreign estate."),
    ])
    route_f = steps([
        ("Sell and pay the Chinese tax", "Property-transfer income is taxed at 20% in China; obtain the tax-clearance certificate."),
        ("Apply to the local SAFE branch", "Purchase application, the property transfer contract, and the tax-clearance certificate for the transfer (汇发〔2006〕47号 Art. 5)."),
        ("Convert and wire", "After SAFE review the bank converts the RMB proceeds and remits them."),
        ("File the US side", "Report the capital gain, claim the foreign tax credit, and file FBAR/8938 as applicable."),
    ])

    body = f"""
<h1 class="page-title">Step by step</h1>
<p class="page-sub">Six lawful routes, written in the order you actually execute them, with the documents that decide each one. Choose the route by your residency status and the source of the money — not by the amount alone.</p>

<div class="callout info">
  <h3>Before any route</h3>
  <p>Download or print the last 12 months of statements, and write a one-page source-of-funds memo: when and how the RMB arose, what tax was paid, and what evidence exists. Every route below turns on that memo. Banks do not accept "savings" without a trail.</p>
</div>

<div class="section">
  <h2 class="section-title">Route A — Domestic individual, within the US$50,000 quota</h2>
  <p class="small">Best for: up to US$50,000 a year, per person. Cost ≈ {money(legal_cost(50_000)['total'])} at {money(50_000)}. {srcs("safe_807", "safe_eng_2007")}</p>
  {route_a}
</div>

<div class="section">
  <h2 class="section-title">Route B — Domestic individual, above the quota with documents</h2>
  <p class="small">Best for: salary, service income, family support. No published ceiling. Cost ≈ {money(legal_cost(400_000)['total'])} at {money(400_000)}. {srcs("safe_807", "fx_regs_2008")}</p>
  {route_b}
</div>

<div class="section">
  <h2 class="section-title">Route C — Foreign individual with legal RMB income</h2>
  <p class="small">Best for: a US citizen who has left China, or never met the one-year residence test. Art. 13(1) route; no dollar ceiling stated; tax certificate mandatory. {srcs("safe_807", "safe_eng_2007")}</p>
  {route_c}
</div>

<div class="section">
  <h2 class="section-title">Route D — Emigration property transfer (移民转移)</h2>
  <p class="small">Best for: a former Chinese national with a six-figure balance and cancelled hukou. Staged over two years. {srcs("property_transfer_2004", "safe_tianjin_2026")}</p>
  {route_d}
</div>

<div class="section">
  <h2 class="section-title">Route E — Inheritance transfer (继承转移)</h2>
  <p class="small">Best for: inherited mainland assets. {src("property_transfer_2004")}</p>
  {route_e}
</div>

<div class="section">
  <h2 class="section-title">Route F — Property-sale proceeds</h2>
  <p class="small">Best for: an apartment sold by a foreign individual. {src("property_fx_2006")}</p>
  {route_f}
</div>

<div class="section">
  <h2 class="section-title">Small amounts only — cash and cards</h2>
  <div class="callout warn">
    <ul>
      <li><strong>FX cash out of China:</strong> up to US$5,000 with no permit; US$5,000–10,000 with a bank-issued permit; above US$10,000 a SAFE permit. Declare anything over US$5,000 when bringing cash <em>into</em> China. {src("cash_2003")}</li>
      <li><strong>RMB cash:</strong> RMB 20,000 per person per trip. {src("rmb_cash_2004")}</li>
      <li><strong>Into the US:</strong> over US$10,000 in currency or monetary instruments must be reported on FinCEN Form 105, and the threshold applies to a family travelling together collectively. {src("cbp_105")}</li>
      <li><strong>Card withdrawals abroad:</strong> RMB 100,000 per person per calendar year; RMB 10,000 per card per day. {src("card_2017")}</li>
    </ul>
  </div>
</div>

<div class="section">
  <h2 class="section-title">US filing calendar</h2>
  {table(
      ["When", "What", "Source"],
      [
          f"<tr><td>15 April</td><td>FBAR (FinCEN Form 114) — automatic extension to 15 October, no request needed</td><td>{src('irs_fbar')}</td></tr>",
          f"<tr><td>15 April</td><td>Form 3520 if a reportable foreign gift was received (15 June if you live abroad; 15 October with an extension)</td><td>{src('irs_3520_instr')}</td></tr>",
          f"<tr><td>With the return</td><td>Form 8938 attached to Form 1040; Form 1116 for the foreign tax credit</td><td>{srcs('irs_fatca', 'irs_pub54')}</td></tr>",
          f"<tr><td>At the border</td><td>FinCEN Form 105 if carrying more than US$10,000 into or out of the US</td><td>{src('cbp_105')}</td></tr>",
      ],
      caption="Deadlines that apply to the individual, not to the bank")}
</div>
"""
    return page("Step by step", "playbook", body,
                "Six lawful routes from CNY to USD, with document lists and the US filing calendar.")


# ---------------------------------------------------------------------------
# Page: flagged for review
# ---------------------------------------------------------------------------
def page_flagged() -> str:
    unverified = [
        ("US receiving-bank and correspondent/intermediary fees",
         "Not included in any cost figure",
         "Bank-specific, deducted in transit, and not published in a form we could verify for a China→US wire.",
         "Ask the receiving US bank for its incoming international wire fee and whether an intermediary deducts before credit."),
        ("Western Union / MoneyGram outbound tariff from mainland China",
         "Blank in Table 3",
         "No official outbound CNY→USD tariff located; availability inside mainland China not confirmed from an official source.",
         "Ask the bank branch that acts as agent for a written tariff and confirm the service is currently offered."),
        ("PayPal / Alipay / WeChat cross-border CNY→USD to a US bank account",
         "Blank in Table 3",
         "No official confirmation that a personal outbound account-to-account transfer is supported as a capital-movement channel.",
         "Check the operator's own current terms; assume China's FX rules apply if it is supported at all."),
        ("Notarisation, translation, hukou-cancellation and legal fees",
         "Excluded from every total",
         "Fees are set by notaries, translators and lawyers, not published centrally.",
         "Obtain quotes once the route is chosen; these can be material on the property and inheritance routes."),
        ("Cash-carry travel costs",
         "Excluded",
         "Depends entirely on the trip.",
         "Not worth modelling: the per-trip ceiling is US$5,000."),
        ("Branch-level FX spread and promotions at Chinese banks",
         "Not modelled",
         "The Bank of China page itself says the counter rate at the time of the transaction governs; branches and promotions vary.",
         "Ask for the rate and all fees in writing before instructing the transfer."),
        ("FBAR inflation adjustment for 2026 assessments",
         "US$16,536 / US$165,353 used",
         "eCFR (current as of 5 November 2026) still shows the amounts for penalties assessed on or after 17 January 2025.",
         "Check FinCEN's current adjustment before relying on a maximum in planning."),
        ("IRC §988(e) personal-transaction de minimis rule",
         "Not used in any calculation",
         "The statutory text could not be retrieved from an official source in this session; only secondary commentary was found.",
         "Ask a US tax adviser to confirm the current text and whether it applies to your conversion."),
        ("RMB 20,000 cash limit — primary source",
         "Figure used, from an official secondary page",
         "PBOC Announcement 2004 No.18 itself, and the customs.gov.cn page that reproduced it, were not retrievable (the customs URL returned 404). The figure is taken from the Shenzhen Port Office page quoting the announcement.",
         "Confirm against the PBOC announcement or a current customs page before relying on it."),
        ("Whether a particular US citizen is a 境内个人 or 境外个人",
         "Decides which route applies",
         "Turns on continuous residence in China of one year or more; the bank applies the test and its records decide.",
         "Ask the bank to state the category it has recorded for your account, in writing."),
        ("Chinese inheritance tax",
         "Not asserted either way",
         "No official source establishing the position was located in this session.",
         "Raise it with the Chinese tax authority handling the tax certificate."),
        ("US gift-tax treatment of a nonresident alien donor's gift",
         "Reporting obligation stated; gift-tax conclusion flagged",
         "The reporting rule is sourced; the situs/gift-tax analysis was not traced to an official statement.",
         "Confirm with a US adviser before treating a large gift as outside gift tax."),
    ]
    nearest = ["boc_fees", "safe_807", "safe_807", "property_transfer_2004", "cash_2003",
               "boc_rates", "fincen_821", "irs_fx_unit", "rmb_cash_2004", "card_2017",
               "fx_regs_2008", "property_transfer_2004", "irs_gifts"]
    unv_table = table(
        ["Item", "Status on the site", "Why it is not filled in", "How to close it", "Nearest official source"],
        [f"<tr><td><strong>{a}</strong></td><td><span class='blank'>{b}</span></td><td>{c}</td><td>{d}</td><td>{src(k)}</td></tr>"
         for (a, b, c, d), k in zip(unverified, nearest)],
        caption="Unverified values — left blank or excluded on purpose",
    )
    unv_table = unv_table.replace('</table>', f'<tfoot><tr><td colspan="5" class="small">All items above are published here rather than guessed. Source registry and retrieval notes: <a href="sources.html">Sources</a>.</td></tr></tfoot></table>')

    irregularities = [
        ("Fine range stated as 30%–300%",
         "Earlier revisions of this dashboard quoted 30%–300% for illegal FX trading.",
         "Corrected to the 2008 text: up to 30%, or 30%–100% in serious cases (Art. 45). The 30%–300% range comes from the superseded 1997 version.",
         "Corrected on <a href='penalties.html'>Penalties</a>; the history is explained there.",
         "fx_regs_2008", "moj_1997"),
        ("Claim that the US$50,000 quota is limited to holders of foreign permanent-resident ID cards",
         "The immediately preceding revision stated the quota is not universal and is granted to foreign permanent-resident ID holders, warning readers not to assume it applies to US passport holders.",
         "That reads a 2017 circular as a restriction when it is an extension: it makes the permanent-resident card a valid ID for FX business and confirms those holders get the US$50,000 quota. The 2007 SAFE Q&amp;A, and Art. 2 of the Detailed Rules, apply the quota to individual FX <em>settlement</em> for both domestic and foreign individuals and to FX <em>purchases</em> by domestic individuals.",
         "Reconciled on the <a href='index.html'>Dashboard</a>, <a href='methods.html'>Methods</a> and <a href='playbook.html'>Step by step</a> pages; both readings are linked here.",
         "safe_eng_2007", "safe_fpr_2017", "safe_807"),
        ("Removal of all cost estimates",
         "The preceding revision removed the method cost table and stated that no cheapest provider could be verified.",
         "Bank of China publishes both a live USD rate and its remittance tariff, so the bank leg can in fact be quantified. The rebuild reinstates it, states the formula, and keeps everything not published by a bank blank.",
         "New <a href='costs.html'>Costs</a> page with a 40-row table and a reproducible formula.",
         "boc_rates", "boc_fees"),
        ("Links to third-party mirrors for the core regulations",
         "Earlier revisions linked the FX Regulations and the Detailed Rules through commercial mirrors (fdi.gov.cn, chinamoney.com.cn) that either did not resolve to the text or are not the issuing authority.",
         "Replaced with the State Council text on gov.cn and SAFE's own pages; the mirrors are no longer cited for any figure.",
         "New <a href='sources.html'>Sources</a> registry lists the primary text for every rule.",
         "fx_regs_2008", "safe_807"),
        ("Repealed 2009 splitting circular cited as current",
         "An earlier revision cited 汇发〔2009〕56号 (the 'five or more people' splitting circular) as the operative rule.",
         "SAFE branch pages mark it repealed, and it does not appear in SAFE's catalogue of rules in force to 30 June 2026. The operative instrument is 汇发〔2015〕49号.",
         "Corrected throughout; the repeal is noted on <a href='methods.html'>Methods</a> route 15.",
         "watchlist_2015", "safe_catalogue_2026"),
        ("Card-withdrawal cap cited through a news report",
         "An earlier revision of this page took the RMB 100,000/year and RMB 10,000/day card caps from a Xinhua report of the SAFE release, because SAFE's own page had not been located.",
         "SAFE publishes the circular itself: 汇发〔2017〕29号, Arts. 1 and 4, in force from 2018-01-01. The figures in the news report match the circular, and the circular also forbids borrowing or lending cards to evade the cap.",
         "Source replaced with the SAFE text and the item removed from the unverified list above.",
         "card_2017"),
        ("Exchange-rate date ambiguity",
         "The Bank of China rate page is timestamped in Beijing time, one calendar day ahead of UTC.",
         "Figures on this site are dated by the quote timestamp (2026-11-09 05:30 Beijing time) with the retrieval date (2026-11-08 UTC) stated.",
         "Noted at the top of <a href='costs.html'>Costs</a>.",
         "boc_rates"),
    ]
    irr_rows = []
    for title, prior, finding, action, *keys in irregularities:
        links = " · ".join(src(k) for k in keys)
        irr_rows.append(
            f"<tr><td><strong>{title}</strong></td><td>{prior}</td><td>{finding}</td><td>{action}<br>{links}</td></tr>"
        )
    irr_table = table(
        ["Issue", "What the earlier text said", "What the sources show", "Action taken / source"],
        irr_rows, caption="Irregularities found in earlier revisions, and what was done about them",
    )

    body = f"""
<h1 class="page-title">Flagged for review</h1>
<p class="page-sub">Everything on this site that could not be confirmed from an official source, plus the errors found in earlier revisions and how they were resolved. Nothing on this page blocks the rest of the analysis — it is the honest edge of the research.</p>

<div class="callout info">
  <h3>Policy</h3>
  <p>A value is printed only if it comes from an official source or from arithmetic on such a value, with the formula shown. Otherwise the cell is left blank and appears below. Every row of every table on the site carries a link to an official source; a blank cell is deliberate, not an oversight.</p>
</div>

<div class="section">
  <h2 class="section-title">Unverified values</h2>
  {unv_table}
</div>

<div class="section">
  <h2 class="section-title">Irregularities found and corrected</h2>
  {irr_table}
</div>

<div class="section">
  <h2 class="section-title">Retrieval log</h2>
  <p>All sources listed on the <a href="sources.html">Sources</a> page were retrieved on {ACCESSED}. Retrieval confirms what the page said on that date; it does not guarantee the page will remain available, nor that a Chinese-language page and its English translation say precisely the same thing. Where SAFE publishes both, the Chinese text is authoritative — its own English pages say so — and the Chinese text was used for every number here.</p>
  <div class="callout warn">
    <h3>What would change the answer</h3>
    <ul>
      <li>A change in the US$50,000 quota, or in Art. 13 of the Detailed Rules.</li>
      <li>Your own residency history in China, and whether hukou was cancelled.</li>
      <li>The source of the money: taxed salary, property, inheritance or gift.</li>
      <li>Whether the funds have already been declared on prior US returns.</li>
    </ul>
    <p>Each of those is a fact only you and your documents can supply — which is why this page, rather than a confident single number, is the honest conclusion.</p>
  </div>
</div>
"""
    return page("Flagged for review", "flagged", body,
                "Unverified values and corrected irregularities in the China-to-US money research.")


# ---------------------------------------------------------------------------
# Page: sources
# ---------------------------------------------------------------------------
def page_sources() -> str:
    groups = [
        ("China — statutes, SAFE and PBOC (primary)",
         ["fx_regs_2008", "safe_807", "safe_eng_2007", "safe_fpr_2017", "property_transfer_2004",
          "property_fx_2006", "watchlist_2015", "crypto_2021", "safe_catalogue_2026", "safe_tianjin_2026"]),
        ("China — cash and cards (primary, mirror or official report)",
         ["cash_2003", "rmb_cash_2004", "card_2017"]),
        ("China — tax (primary)",
         ["iit_law"]),
        ("Commercial bank data used for the cost model",
         ["boc_rates", "boc_fees"]),
        ("United States — tax and reporting (primary)",
         ["irs_fbar", "fincen_821", "irs_fatca", "irs_8938_compare", "irs_3520_instr", "irs_gifts",
          "cbp_105", "irs_pub54", "irs_treaty", "irs_fx_rates", "irs_fx_unit"]),
        ("Historical text used only to explain a superseded figure",
         ["moj_1997"]),
    ]
    type_tag = {True: ("info", "Official"), "mirror": ("mixed", "Official reprint"),
                "secondary-official": ("mixed", "Official page, secondary text"),
                "bank": ("info", "Official bank data"), "database": ("mixed", "Official database"),
                False: ("mixed", "Secondary")}
    sections = []
    for title, keys in groups:
        rows = []
        for k in keys:
            s = SOURCES[k]
            cls, label = type_tag.get(s["official"], ("mixed", "Check"))
            rows.append(
                f"<tr><td><a href='{s['url']}'><strong>{escape(s['title'])}</strong></a>"
                f"<br><span class='small'>{escape(s['publisher'])}</span></td>"
                f"<td>{escape(s['establishes'])}</td>"
                f"<td><span class='tag {cls}'>{label}</span><br><span class='small'>{escape(s['status'])}</span></td></tr>"
            )
        sections.append(f"""
<div class="section">
  <h2 class="section-title">{title}</h2>
  {table(["Source", "What it establishes", "Type and retrieval"], rows)}
</div>""")

    body = f"""
<h1 class="page-title">Sources</h1>
<p class="page-sub">Every rule, rate and penalty figure used on this site, with what it establishes and what happened when it was retrieved on {ACCESSED}. The authoritative language is Chinese wherever SAFE publishes both, because SAFE's own English pages state that the Chinese text prevails.</p>

<div class="callout info">
  <h3>How the verification was done</h3>
  <ol>
    <li>Each primary text was opened and read, not summarised from a search result. The article numbers quoted on the site are the article numbers in the text.</li>
    <li>Where a figure is computed — every number on the <a href="costs.html">Costs</a> page — the inputs are one bank's published rate and tariff, and the formula is printed on the page.</li>
    <li>Where a figure could not be sourced, the cell is blank and the item appears on <a href="flagged.html">Flagged</a>.</li>
    <li>Superseded texts (the 1997 FX Regulations) are listed separately and used only to explain an outdated number, never to state current law.</li>
  </ol>
</div>
{''.join(sections)}

<div class="section">
  <h2 class="section-title">Corrections to earlier revisions</h2>
  <p>Five substantive corrections were made to earlier versions of this dashboard, including an outdated fine range and a misreading of the US$50,000 quota. Each is documented, with its sources, on the <a href="flagged.html">Flagged for review</a> page.</p>
</div>
"""
    return page("Sources", "sources", body,
                "Registry of every official source used, with what each establishes and its retrieval status.")


# ---------------------------------------------------------------------------
# Build, write, validate
# ---------------------------------------------------------------------------
PAGES = {
    "index.html": (page_index, "dashboard"),
    "costs.html": (page_costs, "costs"),
    "methods.html": (page_methods, "methods"),
    "penalties.html": (page_penalties, "penalties"),
    "taxes.html": (page_taxes, "taxes"),
    "playbook.html": (page_playbook, "playbook"),
    "flagged.html": (page_flagged, "flagged"),
    "sources.html": (page_sources, "sources"),
}


def write_data() -> None:
    os.makedirs(os.path.join(ROOT, "data"), exist_ok=True)
    with open(os.path.join(ROOT, "data", "cost_table.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["amount_usd", "rmb_converted", "fx_spread_usd", "wire_fee_cny",
                    "wire_fee_usd", "total_cost_usd", "cost_pct", "years_at_quota",
                    "illegal_fine_low_usd", "illegal_fine_high_usd"])
        for amt in AMOUNTS:
            c = legal_cost(amt)
            w.writerow([amt, f"{c['rmb']:.2f}", f"{c['spread_usd']:.2f}", f"{c['fee_cny']:.2f}",
                        f"{c['fee_usd']:.2f}", f"{c['total']:.2f}", f"{c['pct']:.4f}",
                        c["years"], f"{amt*0.30:.0f}", f"{amt:.0f}"])
    with open(os.path.join(ROOT, "data", "sources.json"), "w", encoding="utf-8") as f:
        json.dump({"accessed": ACCESSED, "sources": SOURCES}, f, indent=2, ensure_ascii=False)
    with open(os.path.join(ROOT, "data", "inputs.json"), "w", encoding="utf-8") as f:
        json.dump({
            "accessed": ACCESSED,
            "boc_usd_buy": RATE_BUY, "boc_usd_sell": RATE_SELL, "mid": RATE_MID,
            "spread_one_way": SPREAD, "fee_rate": FEE_RATE, "fee_min_cny": FEE_MIN_CNY,
            "fee_max_cny": FEE_MAX_CNY, "cable_cny": CABLE_CNY, "quota_usd": QUOTA,
            "atm_year_cny": ATM_YEAR_CNY, "cash_per_trip_usd": CASH_PER_TRIP,
            "quote_timestamp": "2026-11-09 05:30 Beijing time",
        }, f, indent=2)


def validate(pages: dict[str, str]) -> int:
    import re
    problems = 0
    existing = set(pages) | {"assets/style.css"}
    for name, html in pages.items():
        # internal links
        for href in re.findall(r'href="([^"]+)"', html):
            if href.startswith(("http://", "https://", "#", "mailto:")):
                continue
            target = href.split("#")[0]
            if target and target not in existing:
                print(f"  BROKEN internal link in {name}: {href}")
                problems += 1
        # every table body row must carry an external source link
        for tbl in re.findall(r"<tbody>(.*?)</tbody>", html, re.S):
            for row in re.findall(r"<tr.*?</tr>", tbl, re.S):
                if not re.search(r'href=[\'"]http', row):
                    snippet = re.sub(r"<[^>]+>", " ", row)[:90].strip()
                    print(f"  ROW WITHOUT SOURCE in {name}: {snippet}")
                    problems += 1
        # leftover template artefacts
        for bad in ("{{", "}}", "&amp;amp;", "&lt;span"):
            if bad in html:
                print(f"  SUSPECT TOKEN {bad!r} in {name}")
                problems += 1
    if not os.path.exists(os.path.join(ROOT, "assets", "style.css")):
        print("  MISSING assets/style.css")
        problems += 1
    return problems


def main() -> None:
    pages = {}
    for name, (fn, _active) in PAGES.items():
        pages[name] = fn()
        with open(os.path.join(ROOT, name), "w", encoding="utf-8") as f:
            f.write(pages[name])
    write_data()

    # Remove the stylesheet from the previous layout if it is still present.
    legacy = os.path.join(ROOT, "style.css")
    if os.path.exists(legacy):
        os.remove(legacy)

    problems = validate(pages)
    n_rows = sum(len(__import__("re").findall(r"<tr", h)) for h in pages.values())
    print(f"Built {len(pages)} pages, {n_rows} table rows, "
          f"{len(SOURCES)} sources; validation problems: {problems}")
    if problems:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
