#!/usr/bin/env python3
"""Build the China4 static research dashboard and its reproducible cost audit.

All monetary scenarios are illustrative planning models, not executable quotes.
The static HTML is the deliverable; this script documents every calculation.
"""
from __future__ import annotations

from decimal import Decimal, ROUND_CEILING, getcontext
from pathlib import Path
from html import escape
import json

getcontext().prec = 34
ROOT = Path(__file__).resolve().parents[1]
D = Decimal
ZERO = D("0")
AMOUNTS = [D(i * 10000) for i in range(1, 41)]
BUY = D("6.6648")
SELL = D("6.6929")
MID = (BUY + SELL) / 2
QUOTE_TIME = "2026-11-09 05:30 Beijing time (BOC page timestamp)"
RESEARCH_DATE = "2026-11-10 UTC"

SOURCES = {
    "S1": ("SAFE", "Individual FX Detailed Rules (modified), especially Arts. 2, 12–15", "https://www.safe.gov.cn/tianjin/2024/0430/2464.html"),
    "S2": ("SAFE / PBOC", "Measures for the Administration of Individual Foreign Exchange", "https://www.safe.gov.cn/tianjin/2024/0430/2465.html"),
    "S3": ("SAFE", "Current Account FX Business Guide (2020 edition)", "https://www.safe.gov.cn/safe/file/file/20200831/f0127756271c43ef9b3908d5d157bd91.pdf"),
    "S4": ("Bank of China", "Personal Financial Services Price List, effective 2025-11-11 (PDF)", "https://pic.bankofchina.com/bocappd/pricelist/202511/P020251110646838136627.pdf"),
    "S5": ("Bank of China", "Official historical exchange-rate query — select 2026-11-09 and USD (captcha required)", "https://www.boc.cn/sourcedb/whpjSearch/index_2833.html"),
    "S6": ("Bank of China", "Personal outward remittance product and channel instructions", "https://www.boc.cn/pbservice/pb4/200806/t20080626_760.html"),
    "S7": ("SAFE", "Foreign-currency cash carrying limits and permit rules", "https://www.safe.gov.cn/tianjin/2024/0430/2466.html"),
    "S8": ("China Customs", "Official cash declaration guide (red/green channel clearance procedure)", "https://online.customs.gov.cn/static/pages/guides/000629014002/000629014002.html"),
    "S9": ("SAFE", "Domestic-bank-card overseas ATM withdrawal limits", "https://www.safe.gov.cn/hubei/2019/0305/851.html"),
    "S10": ("Bank of China", "ATM price change effective 2026-11-11", "https://www.boc.cn/pbservice/bi2/202608/t20260811_25684907.html"),
    "S11": ("Wise", "Official guide to sending from CNY", "https://wise.com/help/articles/2955298/guide-to-cny-transfers"),
    "S12": ("Wise", "Official verification requirements for sending from CNY", "https://wise.com/help/articles/6UiSPdtzZzYuwQqI4HHtNX/getting-verified-when-sending-from-cny"),
    "S13": ("Wise", "Published 2024-11-25 CNY fee-change examples and formulas", "https://wise.com/gb/blog/summary-of-fee-changes"),
    "S14": ("Western Union", "Official send-money-from-China instructions and partner banks", "https://www.westernunion.com/cn/en/send-money.html"),
    "S15": ("Western Union", "Official China fee/FX variability disclosure", "https://www.westernunion.com/cn/en/wu-services-in-china.html"),
    "S16": ("Bank of China / MoneyGram", "MoneyGram China outbound fee schedule effective 2018-01-15 (dated)", "https://www.boc.cn/pbservice/bi2/201801/t20180112_11198459.html"),
    "S17": ("PBOC and nine other regulators", "2021 virtual-currency notice, Yin Fa [2021] No. 237", "https://www.pbc.gov.cn/tiaofasi/144941/3581332/4348658/index.html"),
    "S18": ("State Council, PRC", "Regulations on Foreign Exchange Administration, Decree 532", "https://www.gov.cn/gongbao/content/2008/content_1071846.htm"),
    "S19": ("SAFE", "Notice on splitting, borrowed quotas, and the watch list, Hui Fa [2015] No. 49", "https://www.safe.gov.cn/safe/2015/1231/5442.html"),
    "S20": ("PBOC / SAFE", "Interim Measures for Personal Property Transfers Abroad, PBOC Announcement [2004] No. 16", "https://www.gov.cn/gongbao/content/2005/content_64294.htm"),
    "S21": ("SAFE", "2025 cross-border investment/financing guide, section 8 (property)", "https://www.safe.gov.cn/safe/file/file/20250915/16a1dd8e54f94d26969b0a9b781106a8.pdf"),
    "S22": ("SAFE", "Capital Account FX Business Guide (2020 edition), including direct investment", "https://www.safe.gov.cn/yunnan/file/file/20210303/26c1c63b5ced4c639e22d63df04afbef.pdf"),
    "S23": ("Bank of China / PBOC / HKMA", "Cross-boundary Payment Connect launch and supported directions/currencies", "https://www.boc.cn/aboutboc/bi1/202506/t20250620_25390382.html"),
    "S24": ("SAFE", "Official notice on lawful online FX channels; private changers are unlawful", "https://www.safe.gov.cn/guangdong/2020/0304/1668.html"),
    "S25": ("IRS", "FBAR threshold, deadlines, and filing guidance", "https://www.irs.gov/businesses/small-businesses-self-employed/report-of-foreign-bank-and-financial-accounts-fbar"),
    "S26": ("eCFR", "31 CFR 1010.821, current FBAR civil-penalty maxima", "https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010/subpart-H/section-1010.821"),
    "S27": ("IRS", "Form 8938 and FBAR comparison, including all residence/filing-status thresholds", "https://www.irs.gov/businesses/comparison-of-form-8938-and-fbar-requirements"),
    "S28": ("IRS", "Current Instructions for Form 3520", "https://www.irs.gov/instructions/i3520"),
    "S29": ("US Customs and Border Protection", "FinCEN Form 105 for more than USD 10,000 entering/leaving the US", "https://www.cbp.gov/travel/us-citizens/know-before-you-go/know-you-go-traveling-abroad"),
    "S30": ("FinCEN", "CTR FAQ: same-day cash aggregation above USD 10,000", "https://www.fincen.gov/resources/frequently-asked-questions-regarding-fincen-currency-transaction-report-ctr"),
    "S31": ("IRS", "Form 8300 applies to trade/business cash receipts, not an ordinary own-account transfer", "https://www.irs.gov/publications/p1544/ar02.html"),
    "S32": ("IRS", "Publication 54 (2025): worldwide income, FEIE, FTC, and filing rules", "https://www.irs.gov/publications/p54"),
    "S33": ("IRS", "Foreign tax credit and Form 1116 guidance", "https://www.irs.gov/individuals/international-taxpayers/foreign-tax-credit"),
    "S34": ("IRS", "Foreign earned income exclusion eligibility", "https://www.irs.gov/individuals/international-taxpayers/foreign-earned-income-exclusion"),
    "S35": ("IRS", "2026 maximum foreign earned income exclusion", "https://www.irs.gov/individuals/international-taxpayers/figuring-the-foreign-earned-income-exclusion"),
    "S36": ("IRS", "Streamlined procedures for qualifying US taxpayers residing outside the US", "https://www.irs.gov/individuals/international-taxpayers/us-taxpayers-residing-outside-the-united-states"),
    "S37": ("IRS", "Streamlined procedures for qualifying US taxpayers residing in the US", "https://www.irs.gov/individuals/international-taxpayers/us-taxpayers-residing-in-the-united-states"),
    "S38": ("IRS", "Publication 525: personal foreign-currency transaction gain over USD 200", "https://www.irs.gov/publications/p525"),
    "S39": ("State Taxation Administration, PRC", "PRC Individual Income Tax Law and rate schedules", "https://fgk.chinatax.gov.cn/zcfgk/c100009/c5193028/content.html"),
    "S40": ("MOF / STA", "2019 Announcement 35: nonresidents and residents without domicile", "https://fgk.chinatax.gov.cn/zcfgk/c102416/c5202332/content.html"),
    "S41": ("IRS / US Treasury", "US–China income tax treaty documents and saving-clause material", "https://www.irs.gov/businesses/international-businesses/china-tax-treaty-documents"),
    "S42": ("Bank of America", "2026 wire-transfer flyer: inbound fee and possible waivers", "https://resources.bankofamerica.com/direct/render-resource/9149a2de7b1047a499ae291815e985e6"),
    "S43": ("Chase", "Chase Secure Checking incoming-wire fee disclosure", "https://www.chase.com/personal/fees/secure-checking"),
    "S44": ("Capital One", "Incoming-wire fee: USD 15 only on Essential Checking, High-Yield Checking and Essential Savings; other account types no fee", "https://www.capitalone.com/help-center/checking-savings/send-receive-wire-transfer/"),
    "S45": ("Bank of China", "Consolidated service-price index and effective date", "https://www.boc.cn/custserv/fd5/"),
    "S46": ("SAFE", "2022 clarification: USD 50,000 is a convenience quota, not a hard current-account cap", "https://www.safe.gov.cn/ningxia/2022/0929/1997.html"),
    "S47": ("IRS", "Yearly-average FX rates and spot-rate translation principle", "https://www.irs.gov/individuals/international-taxpayers/yearly-average-currency-exchange-rates"),
    "S48": ("Bank of China", "Current retail exchange-rate board (rotating snapshots; re-checked 2026-11-10 02:49 Beijing)", "https://www.boc.cn/sourcedb/whpj/enindex.html"),
    "S49": ("PBOC", "Announcement [2004] No. 18: RMB 20,000 per-trip limit for inbound/outbound travellers", "https://www.pbc.gov.cn/chubanwu/114566/114579/114643/2839193/index.html"),
    "S50": ("China Customs", "Announcement 2025 No. 43 (effective 2025-04-01), which repealed Announcement 2007 No. 72", "https://www.gov.cn/zhengce/zhengceku/202504/content_7017195.htm"),
    "S51": ("CBP", "Money and monetary instruments: FinCEN Form 105 above USD 10,000 and group aggregation", "https://www.cbp.gov/travel/international-visitors/money-monetary-instruments"),
    "S52": ("FinCEN", "FBAR trigger: aggregate foreign accounts above USD 10,000 at any time in the calendar year", "https://www.fincen.gov/report-foreign-bank-and-financial-accounts"),
    "S53": ("IRS", "Rev. Proc. 2025-32: 2026 rate tables, standard deduction, capital-gain thresholds, FEIE and the §6039F gift threshold", "https://www.irs.gov/pub/irs-drop/rp-25-32.pdf"),
    "S54": ("Shanghai Tax Service", "Comprehensive income annual rate table and quick deductions (official PDF)", "https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/202402/P020240202362406243753.pdf"),
}


def source(*ids: str) -> str:
    return " ".join(
        f'<a class="source" href="{SOURCES[i][2]}" target="_blank" rel="noopener noreferrer" aria-label="{escape(SOURCES[i][0])}: {escape(SOURCES[i][1])}">[{i}]</a>'
        for i in ids
    )


def table(headers, rows, caption="", cls="") -> str:
    head = "".join(f"<th scope=\"col\">{h}</th>" for h in headers)
    body = []
    for row in rows:
        cells = "".join(f'<td data-label="{escape(headers[i])}">{cell}</td>' for i, cell in enumerate(row))
        body.append(f"<tr>{cells}</tr>")
    cap = f"<caption>{caption}</caption>" if caption else ""
    return f'<div class="table-wrap"><table class="data {cls}">{cap}<thead><tr>{head}</tr></thead><tbody>{"".join(body)}</tbody></table></div>'


NAV = [
    ("evidence.html", "Evidence", "Fresh audit and strict costs"),
    ("index.html", "Dashboard", "Decision dashboard"),
    ("summary.html", "Summary", "Executive brief"),
    ("methods.html", "Methods", "18 routes and procedures"),
    ("penalties.html", "Costs", "40-row cost matrices"),
    ("taxes.html", "Taxes", "China and US tax/reporting"),
    ("flagged.html", "Review", "Unknowns and irregularities"),
    ("sources.html", "Sources", "Primary-source register"),
    ("banks.html", "Banks", "Multi-bank tariff evidence"),
    ("playbooks.html", "Playbooks", "Documented route procedures"),
    ("verification.html", "Verification", "Row-by-row ledger"),
]


def layout(filename: str, title: str, subtitle: str, body: str) -> str:
    links = "".join(
        '<a href="{}"{}><span>{}</span><small>{}</small></a>'.format(
            href,
            ' class="active" aria-current="page"' if href == filename else "",
            short,
            desc,
        )
        for href, short, desc in NAV
    )
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{escape(subtitle)}">
<meta name="theme-color" content="#102a43">
<title>{escape(title)} — China4 Research</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<a class="skip-link" href="#main">Skip to research</a>
<header class="site-header"><div class="header-inner">
<a class="brand" href="index.html" aria-label="China4 home"><span class="mark">C4</span><span>China4 <small>evidence desk</small></span></a>
<nav aria-label="Primary navigation">{links}</nav>
</div></header>
<main class="container" id="main">
<div class="page-heading"><div><p class="eyebrow">CNY → USD · US-citizen research</p><h1>{escape(title)}</h1><p class="page-sub">{subtitle}</p></div><div class="as-of"><span>Research cutoff</span><strong>{RESEARCH_DATE}</strong><small>BOC quote: 2026-11-09 Beijing</small></div></div>
<aside class="callout info"><strong>Evidence boundary:</strong> <a href="evidence.html">Read the fresh evidence brief and strict current-cost register first.</a> Older dollar calculations use a historical FX snapshot that cannot currently be reproduced from a permanent official row. They are illustrative, not verified executable costs. Unconfirmed current costs are blank in the strict register.</aside>
{body}
<div class="disclaimer"><strong>Research, not individualized legal, tax, or investment advice.</strong> Eligibility follows the source and character of funds, identity used at the bank, tax residence, and transaction purpose. Obtain a written all-in bank/provider quote and qualified cross-border tax review before execution. “—” means unknown or unavailable, never zero.</div>
</main>
<footer class="site-footer"><div class="inner"><div><strong>China4 evidence desk</strong><p>Independent primary-source audit · calculations reproducible in <code>scripts/build_site.py</code> and <code>data/cost-model.json</code>.</p></div><div><p>Reviewed {RESEARCH_DATE}. FX and fees change.</p><p><a href="flagged.html">Read unresolved items before acting</a> · <a href="https://github.com/sassnarep3-star/China4">Repository</a></p></div></div></footer>
</body></html>'''


def usd(x: D) -> str:
    return f"${x:,.2f}"


def cny(x: D) -> str:
    return f"¥{x:,.2f}"


def integer_ceil(x: D) -> int:
    return int(x.to_integral_value(rounding=ROUND_CEILING))


def split_principal(amount: D, cap: D):
    out = []
    left = amount
    while left > 0:
        piece = min(left, cap)
        out.append(piece)
        left -= piece
    return out


def wire_cny(amount: D) -> D:
    principal = amount * SELL
    return min(D(260), max(D(50), principal * D("0.001")))


def spread_cny(amount: D) -> D:
    return amount * SELL * (SELL - MID) / MID


def boc_parts(amount: D):
    principal = amount * SELL
    commission = wire_cny(amount)
    telecom = D(150)
    spread = spread_cny(amount)
    base = commission + telecom + spread
    return {
        "amount_usd": amount,
        "principal_cny": principal,
        "commission_cny": commission,
        "telecom_cny": telecom,
        "spread_cny": spread,
        "base_cny": base,
        "base_usd": base / SELL,
        "existing_usd_wire_usd": (commission + telecom) / SELL,
        "draft_known_usd": (commission + spread) / SELL,
    }


def quota_model(amount: D):
    pieces = split_principal(amount, D(50000))
    total = sum((boc_parts(p)["base_cny"] for p in pieces), ZERO)
    return len(pieces), total / SELL


def atm_unionpay(amount: D):
    # SAFE caps overseas ATM withdrawals at CNY 10,000 per card/day [S9];
    # the BOC UnionPay fee applies per withdrawal [S4/S10].
    pieces = split_principal(amount * SELL, D(10000))
    fee = sum((min(D(112), D(12) + D("0.01") * p) for p in pieces), ZERO)
    return len(pieces), fee / SELL


def atm_card_future(amount: D):
    # Same CNY 10,000/day withdrawal split; Visa/MC fee is 2.5% of the amount
    # withdrawn, min USD-equivalent 3 / max USD-equivalent 40 per withdrawal [S10].
    pieces = split_principal(amount * SELL, D(10000))
    fee = sum((min(D(40), max(D(3), D("0.025") * p / SELL)) for p in pieces), ZERO)
    return len(pieces), fee


def cost_rows():
    rows = []
    for amount in AMOUNTS:
        item = boc_parts(amount)
        qn, qcost = quota_model(amount)
        emigration_pieces = [amount] if item["principal_cny"] <= D(200000) else [amount / 2, amount / 4, amount / 4]
        emigration_total = sum((boc_parts(piece)["base_cny"] for piece in emigration_pieces), ZERO) / SELL
        item.update({
            "quota_wires": qn, "quota_total_usd": qcost,
            "full_arrival_other_us_plus_bofa_usd": item["base_usd"] + D(40),
            "emigration_wires": len(emigration_pieces),
            "emigration_staged_total_usd": emigration_total,
            "inheritance_one_wire_total_usd": item["base_usd"],
            "property_sale_one_wire_total_usd": item["base_usd"],
        })
        if amount <= D("14941.21"):
            un, ucost = atm_unionpay(amount)
            vn, vcost = atm_card_future(amount)
            item.update({"atm_unionpay_withdrawals": un, "atm_unionpay_fee_usd": ucost, "atm_future_card_withdrawals": vn, "atm_future_card_fee_usd": vcost})
        rows.append(item)
    return rows



# --- 2026 US federal tax arithmetic (Rev. Proc. 2025-32, source S53) ---------
# Single filer, under 65, not blind. Floors, rates and tax-at-floor are quoted
# exactly from Table 3 (ordinary) and section 4.03 (capital gain) of S53.
US_ORDINARY_2026 = [
    (D("0"), D("0.10"), D("0")),
    (D("12400"), D("0.12"), D("1240")),
    (D("50400"), D("0.22"), D("5800")),
    (D("105700"), D("0.24"), D("17966")),
    (D("201775"), D("0.32"), D("41024")),
    (D("256225"), D("0.35"), D("58448")),
    (D("640600"), D("0.37"), D("192979.25")),
]
US_STANDARD_DEDUCTION_2026 = D("16100")
US_LTCG_ZERO_MAX_2026 = D("49450")
US_LTCG_FIFTEEN_MAX_2026 = D("545500")
US_OTHER_TAXABLE_2026 = D("100000")
FEIE_2026 = D("132900")


def us_ordinary_tax(taxable: D) -> D:
    """2026 single-filer ordinary income tax from the published S53 table."""
    if taxable <= 0:
        return ZERO
    floor, rate, base = US_ORDINARY_2026[0]
    for candidate_floor, candidate_rate, candidate_base in US_ORDINARY_2026:
        if taxable > candidate_floor:
            floor, rate, base = candidate_floor, candidate_rate, candidate_base
    return base + rate * (taxable - floor)


def us_ltcg_tax(other_taxable: D, gain: D) -> D:
    """2026 single-filer long-term capital gain tax, stacked on other income."""
    if gain <= 0:
        return ZERO
    start = max(other_taxable, ZERO)
    end = start + gain
    fifteen_part = max(ZERO, min(end, US_LTCG_FIFTEEN_MAX_2026) - max(start, US_LTCG_ZERO_MAX_2026))
    twenty_part = max(ZERO, end - max(start, US_LTCG_FIFTEEN_MAX_2026))
    return D("0.15") * fifteen_part + D("0.20") * twenty_part


def us_tax_scenarios():
    """Illustrative 2026 US tax on the same amount under different characters."""
    rows = []
    for amount in (D(10000), D(50000), D(100000), D(200000), D(400000)):
        baseline = us_ordinary_tax(US_OTHER_TAXABLE_2026)
        rows.append({
            "amount": amount,
            "other_taxable": US_OTHER_TAXABLE_2026,
            "ordinary_delta": us_ordinary_tax(US_OTHER_TAXABLE_2026 + amount) - baseline,
            "fx_gain": amount * D("0.10"),
            "fx_gain_tax": us_ltcg_tax(US_OTHER_TAXABLE_2026, amount * D("0.10")),
            "feie_tax": us_ordinary_tax(max(ZERO, US_OTHER_TAXABLE_2026 + amount - FEIE_2026)),
        })
    return rows


US_TAX = us_tax_scenarios()


COSTS = cost_rows()


def callout(kind, title, text):
    return f'<div class="callout {kind}"><h2>{title}</h2><p>{text}</p></div>'


def index_page():
    comparison = [
        ("Documented current-account income → BOC telegraphic transfer", "US passport holder with lawful after-tax Chinese income", "Amount supported by evidence; bank review", f"10k {usd(COSTS[0]['base_usd'])} · 400k {usd(COSTS[-1]['base_usd'])} known model", '<span class="tag good">Primary baseline</span>', source("S1", "S4")),
        ("Existing foreign-currency savings → international wire", "Funds already in USD, not CNY needing conversion", "ID for foreign-individual FX savings; bank review", f"10k {usd(COSTS[0]['existing_usd_wire_usd'])} · 400k {usd(COSTS[-1]['existing_usd_wire_usd'])} before receiving charges", '<span class="tag good">Conditional</span>', source("S1", "S4")),
        ("Original-currency reconversion → remit", "Unused RMB from an earlier FX conversion", "Original exchange memo, generally 24 months", "Same BOC conversion/wire model; memo amount controls", '<span class="tag good">Conditional</span>', source("S1", "S2")),
        ("Wise from CNY (bank app or Alipay funding)", "Non-mainland-Chinese person with qualifying work/tax history; own-name recipient", "300k CNY/bank transfer; 50k CNY/Alipay; overall tax-based limit", "Current fee/FX —; live quote required", '<span class="tag mixed">Compare live quote</span>', source("S11", "S12", "S13")),
        ("BOC demand draft → US foreign-item deposit", "US bank accepts the draft; slower collection acceptable", "Same source-of-funds review; postage/collection terms", f"Known subtotal 10k {usd(COSTS[0]['draft_known_usd'])} + postage/collection", '<span class="tag mixed">Niche</span>', source("S4", "S44")),
        ("Western Union through a China partner bank", "Speed/cash payout matters more than verified price", "Provider, agent, SAFE and receiving limits", "Current fee and FX margin —", '<span class="tag mixed">Quote required</span>', source("S14", "S15")),
        ("MoneyGram through BOC", "Small legacy schedule comparison only", "Current availability/limits require confirmation", "— ($32 historical top tier ends at $9,999.99; current terms unverified)", '<span class="tag mixed">Dated evidence</span>', source("S16")),
        ("Carry USD cash", "Only a small, documented amount", "≤$5k no permit; >$5k–$10k bank permit; >$10k special SAFE permit", "Travel/withdrawal/security costs —; BOC permit fee waived through 2026-12-31", '<span class="tag mixed">Not scalable</span>', source("S7", "S4", "S29")),
        ("Chinese card → overseas ATM", "Emergency cash only, not a USD account transfer", "CNY 100k/person/year and CNY 10k/card/day", "At the modeled rate only $10k fits an unused annual cap; other amounts exceed that cap", '<span class="tag mixed">Very limited</span>', source("S9", "S4", "S10")),
        ("Emigration property transfer", "Qualifying emigrant liquidating pre-emigration lawful property", "SAFE approval; full amount applied for together; staged remittance can apply", "BOC baseline if BOC is used + tax/legal costs —", '<span class="tag good">Special legal route</span>', source("S20", "S4")),
        ("Inherited PRC property transfer", "Foreign citizen inheriting lawful PRC estate", "Notarized inheritance/title/tax documents; SAFE process", "BOC baseline if BOC is used + professional costs —", '<span class="tag good">Special legal route</span>', source("S20", "S4")),
        ("Sale of PRC residential property", "Foreign individual selling lawfully owned property", "Registered sale, completed title transfer, tax evidence", "After-tax net proceeds; BOC baseline if used", '<span class="tag good">Special legal route</span>', source("S21", "S4")),
        ("Foreign-invested business exit/equity proceeds", "Documented direct-investment liquidation or equity sale", "Registration information, authentic transaction and tax review", "Institution-specific —", '<span class="tag mixed">Fact-specific</span>', source("S22")),
        ("Domestic-individual genuine current-account purchase", "Only if bank classifies applicant as domestic individual", "$50k is convenience quota, not a cap on documented genuine current-account use", f"Illustrative $50k/year schedule: 400k {usd(COSTS[-1]['quota_total_usd'])} over 8 years", '<span class="tag mixed">Not default for US passport</span>', source("S1", "S46")),
        ("Hong Kong Payment Connect", "Qualifying mainland↔HK CNY/HKD payments", "Not a documented direct CNY→USD-to-US route", "Second-leg legality/fees —", '<span class="tag mixed">Not a complete route</span>', source("S23")),
        ("PayPal China / standalone Alipay / WeChat", "No primary evidence found for this exact own-account CNY→USD flow", "Do not infer availability from wallet branding", "—", '<span class="tag bad">Unproven</span>', source("S11", "S24")),
        ("Private swap / borrowed quotas / fake invoices", "No lawful implementation for evasion", "Watch-list and penalty exposure", "Do not use", '<span class="tag bad">Avoid</span>', source("S18", "S19", "S24")),
        ("Crypto / stablecoin P2P", "Not offered as a lawful workaround", "PBOC notice prohibits related business activities", "Do not use", '<span class="tag bad">Avoid</span>', source("S17")),
    ]
    comp_table = table(["Route", "When it fits", "Controlling limit / evidence", "Cost treatment", "Assessment", "Official sources"], comparison,
                       "Every row links to primary evidence. “Conditional” means the source of funds must fit the rule; it does not mean pre-approved.")
    snapshots = []
    for i in [0, 4, 9, 39]:
        r = COSTS[i]
        snapshots.append((f"<strong>{usd(r['amount_usd'])}</strong>", cny(r['principal_cny']), usd(r['base_usd']), usd(r['full_arrival_other_us_plus_bofa_usd']), "— (current quote unverified)", source("S4", "S5", "S13", "S42")))
    snapshot_table = table(["USD-equivalent principal", "CNY at 6.6929", "BOC known baseline", "+ $25 full-arrival + $15 BofA example", "Wise bank current quote", "Sources"], snapshots,
                           "Known BOC model = published fee + CNY 150 telecom + same-quote half-spread. Correspondent/recipient charges, taxes and unknowns excluded unless shown.")
    body = f'''
<div class="hero"><div class="hero-copy"><p class="eyebrow light">Executive answer · independently corrected</p><h2>Use the route your documents support—not a quota workaround.</h2><p>For a US passport holder, the most verifiable default is a licensed-bank conversion and own-account international wire supported by lawful source-of-funds and tax evidence. The $50,000 convenience purchase rule is written for <strong>domestic individuals</strong>; it is not blanket “ID-only” permission for a foreign individual.</p><div class="hero-actions"><a class="cta" href="summary.html">Read the executive summary</a><a class="cta secondary" href="methods.html">Choose a documented route</a><a class="cta secondary" href="penalties.html">Compare all 40 amounts</a></div></div><div class="hero-panel"><span>BOC modeled known cost</span><strong>{usd(COSTS[0]['base_usd'])}</strong><small>per USD 10,000 equivalent</small><hr><strong>{usd(COSTS[-1]['base_usd'])}</strong><small>per USD 400,000 equivalent</small><p>Published wire tariff + same-quote FX benchmark. Not an all-in quote.</p></div></div>
{callout("info", "Bottom line", "No single route is always cheapest or tax-free. Start with BOC’s documented wire as the auditable baseline; if Wise confirms your eligibility, compare its live CNY debit, fee, execution rate and final USD received against the bank’s written quote. Assess taxes on the underlying income and any taxable currency gain separately; the payment rail alone does not determine tax. " + source("S1", "S11", "S32"))}
<div class="metric-grid"><div class="metric"><span>BOC USD selling rate</span><strong>6.6929</strong><small>CNY per USD · {QUOTE_TIME}. Dated snapshot; BOC’s board rotates, so re-query by date.</small><p>{source("S5", "S48")}</p></div><div class="metric"><span>Retail half-spread benchmark</span><strong>0.210366%</strong><small>From same-timestamp buy 6.6648 / sell 6.6929; arithmetic, not a guaranteed markup</small><p>{source("S5", "S48")}</p></div><div class="metric"><span>FBAR aggregate trigger</span><strong>&gt; $10,000</strong><small>Foreign accounts at any time in the calendar year</small><p>{source("S25", "S52")}</p></div><div class="metric"><span>Convenience purchase quota</span><strong>$50,000</strong><small>Domestic individuals; genuine documented current-account needs can exceed it</small><p>{source("S1", "S46")}</p></div></div>
<section class="section"><div class="section-heading"><p class="eyebrow">01 · Eligibility first</p><h2>Four checks before comparing prices</h2></div><div class="steps four"><div><span>1</span><h3>Classify identity</h3><p>SAFE’s implementation measures define a passport-holding foreign citizen as a foreign individual. Confirm which identity the bank has on file. {source("S2")}</p></div><div><span>2</span><h3>Classify money</h3><p>After-tax current-account income, old foreign-currency savings, original-currency reconversion, inheritance and property proceeds follow different rules. {source("S1", "S20", "S21")}</p></div><div><span>3</span><h3>Build evidence</h3><p>Passport, contracts/payslips, amount-matched records and Chinese tax evidence; keep the complete chain from income to bank balance. {source("S1")}</p></div><div><span>4</span><h3>Compare net USD</h3><p>Record CNY principal, execution rate, every sender/intermediary/receiver fee, and final USD credited. Never treat “no fee” as “no spread.” {source("S4", "S15")}</p></div></div></section>
<section class="section"><div class="section-heading"><p class="eyebrow">02 · Cost snapshot</p><h2>What the official inputs actually show</h2><a href="penalties.html">Full formulas and 40-row matrices →</a></div>{snapshot_table}<p class="note">Wise costs are blank because the historical examples do not establish current pricing or a same-net-payout quote. Wise deducts fees before conversion; compare live quotes for the same net amount. Full-arrival is optional; the BofA charge is an example that may be waived by account. {source("S4", "S13", "S42")}</p><p class="note"><strong>Penalty exposure at $400,000:</strong> the modeled lawful BOC cost is {usd(COSTS[-1]['base_usd'])}, while the published statutory ceiling for an FX offence is 30% of the amount, rising to 100% in serious cases — a ceiling of $120,000 to $400,000, before criminal or tax consequences. <a href="penalties.html#penalty-vs-cost">See the side-by-side comparison →</a> {source("S18", "S4")}</p></section>
<section class="section"><div class="section-heading"><p class="eyebrow">03 · Route inventory</p><h2>18 channels, special cases, and rejected shortcuts</h2><a href="methods.html">Exact procedures →</a></div>{comp_table}</section>
<section class="section"><div class="section-heading"><p class="eyebrow">04 · Compliance</p><h2>The reporting layer does not disappear after conversion</h2></div><div class="steps three"><div><span>A</span><h3>FBAR</h3><p>Aggregate maximum foreign-account values, not just the amount transferred. Due April 15 with automatic extension to October 15. {source("S25")}</p></div><div><span>B</span><h3>Income and asset forms</h3><p>Form 8938 has separate residence/status thresholds. Form 3520 is for specified foreign gifts/bequests and trusts—not moving your own savings. {source("S27", "S28")}</p></div><div><span>C</span><h3>Relief, not concealment</h3><p>Review FEIE versus foreign tax credit for underlying income and correct qualifying past nonwillful filings through IRS procedures. {source("S33", "S34", "S36", "S37")}</p></div></div></section>'''
    return layout("index.html", "Move CNY to USD, lawfully and verifiably", "Executive route selection, official-input cost models, and US–China compliance for a US citizen with CNY in a Chinese bank account.", body)


def route_details(rid, title, verdict, summary, pros, cons, steps, cost, sources):
    pro_items = "".join(f"<li>{x}</li>" for x in pros)
    con_items = "".join(f"<li>{x}</li>" for x in cons)
    step_items = "".join(f"<li>{x}</li>" for x in steps)
    return f'''<details class="route" id="{rid}"><summary><span class="route-title">{title}</span><span class="tag {"good" if verdict in ("Primary", "Conditional", "Special") else "mixed" if verdict not in ("Avoid", "Unproven") else "bad"}">{verdict}</span></summary><div class="route-body"><p>{summary}</p><div class="pros-cons"><div><h3>Advantages</h3><ul>{pro_items}</ul></div><div><h3>Constraints</h3><ul>{con_items}</ul></div></div><h3>Procedure</h3><ol class="procedure">{step_items}</ol><div class="route-cost"><strong>Cost treatment</strong><p>{cost}</p></div><p class="source-line"><strong>Primary evidence</strong> {sources}</p></div></details>'''


def methods_page():
    routes = []
    routes.append(route_details("wire", "1. Lawful current-account CNY income → BOC USD telegraphic transfer", "Primary",
        "For a foreign individual, SAFE Article 13 supports purchasing FX from lawful current-account RMB income with ID, amount-based evidence and tax records. This is not the domestic-individual ID-only convenience route.",
        ["Clear regulatory basis and complete paper trail", "One transfer can exceed $50,000 when evidence supports it", "Published BOC tariff caps the percentage commission at CNY 260"],
        ["Bank decides whether documents are sufficient", "Execution FX, correspondent and recipient charges can change net proceeds", "Underlying income tax must be addressed separately"],
        ["Confirm the bank records you as a foreign individual and ask its cross-border desk to pre-review the exact source-of-funds category.", "Assemble passport, employment/service contract, payslips or transaction documents, bank statements and amount-matched Chinese tax evidence.", "Obtain your US account’s legal name, account number, receiving SWIFT/BIC, bank address and incoming-wire instructions; do not guess an intermediary.", "Ask BOC for a written CNY principal, USD selling rate, commission, CNY 150 telecom charge, full-arrival option and expected recipient deductions.", "Submit the purchase/remittance application through BOC’s cross-border-remittance channel or branch and answer authenticity review consistently.", "Save the application, FX memo, SWIFT receipt, fee receipts and final US credit; reconcile them to FBAR and tax workpapers."],
        f"Known model: clamp(0.1% × CNY principal, ¥50, ¥260) + ¥150 + same-quote half-spread. Results: $10k {usd(COSTS[0]['base_usd'])}; $400k {usd(COSTS[-1]['base_usd'])}. Add optional full-arrival and receiving charges as applicable.", source("S1", "S4", "S5", "S6")))
    routes.append(route_details("savings", "2. Existing USD savings → international wire (no CNY conversion)", "Conditional",
        "SAFE Article 15 permits a foreign individual to remit existing FX savings abroad with ID. This route applies only if the balance is already USD (or another currency accepted for the remittance), not to CNY merely described as savings.",
        ["No new CNY→USD purchase or retail conversion spread", "Simple evidence chain if the FX balance origin is clear"],
        ["Does not itself convert the CNY balance", "Bank can still request authenticity/source documents", "Wire and receiving charges remain"],
        ["Verify the account currency and whether it is an FX savings account.", "Present ID and the bank’s requested evidence for the existing balance.", "Follow steps 3–6 of the telegraphic-transfer route, selecting remittance of existing FX rather than a new CNY purchase.", "Retain the original deposit/conversion history so the no-new-conversion treatment is auditable."],
        f"BOC wire-only known subtotal: $10k {usd(COSTS[0]['existing_usd_wire_usd'])}; $400k {usd(COSTS[-1]['existing_usd_wire_usd'])}. No half-spread is modeled because no new conversion occurs; correspondent/receiver charges are extra.", source("S1", "S4")))
    routes.append(route_details("reconversion", "3. Unused RMB from an earlier FX conversion → original-currency reconversion", "Conditional",
        "A foreign individual may reconvert unused RMB using ID and the original exchange memo, generally within 24 months. Small ID-only exceptions exist, but they do not make the whole bank balance eligible.",
        ["Direct statutory category for genuinely unused converted funds", "Can avoid trying to relabel the balance as salary"],
        ["Original memo and 24-month timing constrain the amount", "Not available for unrelated CNY income", "Bank must match the reconversion to the original transaction"],
        ["Locate each original exchange memo and its date/amount.", "Calculate the still-unused portion; exclude unrelated deposits.", "Ask the original bank to verify the 24-month window and any small ID-only exception rather than assuming it.", "Purchase the original currency within the eligible amount and either hold it as FX or remit using the wire procedure.", "Keep the original and new memos linked in your records."],
        "Use the BOC conversion/wire model only for the eligible amount. The matrix does not imply the entire requested row qualifies.", source("S1", "S2")))
    routes.append(route_details("wise", "4. Wise from CNY → own USD account (bank-app or Alipay funding)", "Compare quote",
        "Wise’s current official guide says eligible non-mainland-Chinese users who work or worked in China and have qualifying Chinese tax records can send from CNY to an account they own. A PBOC-regulated partner handles the China leg.",
        ["Documented non-bank alternative", "Own-name requirement reduces third-party misuse", "Published caps and transparent quote flow"],
        ["Not for mainland-Chinese senders", "Tax records within Wise’s accepted period and overall limit control eligibility", "Current fees/rates are quote-dependent; historical matrix is not an offer"],
        ["Create a personal Wise account and select CNY→USD to your own USD bank account or Wise account.", "Upload passport, an accepted current/former work-eligibility document and Chinese personal-income-tax records meeting Wise’s recency rules.", "Let Wise calculate your overall sending limit; cancel unfunded transfers you do not intend to complete so their reserved limit is released.", "Choose Chinese bank-app funding (up to CNY 300,000 per transfer) or Alipay funding (up to CNY 50,000 per transfer) and record the live fee/rate before paying.", "For bank funding, send CNY only from your same-name account to the unique partner safeguarding-account details shown by Wise; for Alipay, complete the displayed payment flow.", "Track verification/payout and save the quote, local debit, tax records and final USD receipt."],
        "Current fee, rate and net USD payout —. Wise’s published 2024 price-change examples do not establish today’s prices at the amounts in the matrix. Fees are deducted before conversion; compare quotes for the same net USD received.", source("S11", "S12", "S13")))
    routes.append(route_details("draft", "5. BOC cross-border demand draft → US bank collection/deposit", "Niche",
        "BOC’s current personal price list covers both telegraphic transfers and drafts. A draft avoids the CNY 150 telecom charge but adds actual postage and US foreign-item acceptance/collection considerations.",
        ["Same CNY 50–260 commission scale as BOC wire", "No BOC international telecom charge"],
        ["Physical loss/delay and stop-payment risk", "US bank may treat it as a foreign collection item with delays/fees", "Postage and receiving terms are not uniform"],
        ["Complete the same eligibility and document pre-review as a BOC wire.", "Before ordering, give your US bank the draft’s currency, issuer and amount; obtain written acceptance, endorsement, collection and fee instructions.", "Ask BOC for the draft fee and actual postage; make it payable exactly as the US bank instructs.", "Purchase/issue the USD draft and record its number, FX memo and receipt.", "Use a delivery method you consider adequately trackable/insured, then deposit under the US bank’s foreign-item procedure.", "Reconcile final credit and retain collection/fee records."],
        f"Known subtotal excluding postage and US collection: $10k {usd(COSTS[0]['draft_known_usd'])}; $400k {usd(COSTS[-1]['draft_known_usd'])}. A dash in the matrix means those charges are unknown.", source("S4", "S44")))
    routes.append(route_details("wu", "6. Western Union through an official China partner bank", "Quote needed",
        "Western Union lists online/mobile and in-person sending from China through partner banks. Its official disclosure says it also makes money from FX and that fees/rates vary by brand, channel and location.",
        ["Official China outbound process", "Cash pickup can avoid a recipient bank account", "MTCN tracking and broad agent network"],
        ["No current static China→US fee/FX schedule verified", "Agent, payment, delivery and receiving limits vary", "SAFE source-of-funds review still applies"],
        ["Use only a partner/channel listed by Western Union and confirm that your US passport and own-name US payout are accepted.", "Present ID and the source/tax evidence required for the underlying purchase/remittance.", "Request the complete quote: CNY debit, transfer fee, CNY→USD rate, USD payout, agent limit and any cash-payout restriction.", "Compare final USD with the BOC and Wise quotes; pay only after the quote is shown.", "Keep the receipt/MTCN; the receiver presents required ID and payout details.", "Retain the FX and fee evidence for account and tax records."],
        "Current fee and FX margin are blank in all 40 rows. Expired promotional schedules are not used as current prices.", source("S14", "S15", "S1")))
    routes.append(route_details("mg", "7. MoneyGram through Bank of China", "Dated",
        "BOC published a MoneyGram outbound fee schedule effective 2018-01-15. It documents a route and historical tiers but is not represented as a current 2026 quote.",
        ["Bank-agent process and historical fee evidence", "Potential cash-pickup alternative"],
        ["Current availability, price, FX and limits need fresh confirmation", "Published non-Africa schedule ends at $9,999.99", "No basis to extrapolate larger rows"],
        ["Ask BOC whether MoneyGram outbound service is currently available at your branch/channel.", "Complete the same eligibility review and provide recipient/payout details.", "Obtain a current fee, FX, destination and per-transaction limit quote in writing.", "Compare final USD and pay only under the displayed terms.", "Save the reference number and supporting documents."],
        "The dated schedule’s $32 top tier ends at $9,999.99. Every $10,000-increment matrix cell is therefore blank; no current fee or higher tier is inferred.", source("S16", "S1")))
    routes.append(route_details("other-bank", "8. Another licensed Chinese bank → USD wire", "Unpriced",
        "SAFE’s foreign-individual rules are not BOC-specific. Another licensed bank may offer a better execution rate or document process, but no institution-wide current tariff was verified for ICBC, CCB or others.",
        ["Potential competitive FX or service", "Same licensed-bank evidence framework"],
        ["Do not reuse BOC’s fees as another bank’s fees", "Channel availability and document practice vary"],
        ["Ask the bank to classify your identity/source and pre-check the documents.", "Request its current personal cross-border USD tariff, execution rate, correspondent terms and receiving instructions.", "Compare total CNY debit and net USD against BOC/Wise.", "Execute and preserve the same evidence chain."],
        "All non-BOC institution-specific values remain blank; use the BOC matrix only as a benchmark, not a proxy.", source("S1", "S24")))
    routes.append(route_details("domestic", "9. Domestic-individual genuine current-account purchase/remittance", "Conditional",
        "The $50,000 annual convenience purchase quota applies to domestic individuals. Genuine documented current-account purchases above it are possible; the quota is not a hard annual cap. A US passport holder should not assume this classification.",
        ["Documented current-account needs are not artificially capped at $50,000", "Electronic bank channels may be available"],
        ["Identity classification is decisive", "Purpose must be genuine and documented", "Annual-repeat modeling is not permission to split or disguise a transaction"],
        ["Ask the bank which SAFE identity applies to the account; do not select domestic-individual treatment merely to obtain ID-only processing.", "For convenience-quota purchases, provide ID and truthful purpose information.", "Above the quota, provide amount-matched current-account purpose evidence; for outward FX-savings remittances, follow the applicable daily documentation rule.", "Keep purchase and payment purposes consistent and never borrow another person’s quota.", "Use the illustrative annual schedule only if each year’s request independently satisfies the rules."],
        f"Illustrative $50k/year, one-wire-per-year model at constant rates: $400k over 8 years = {usd(COSTS[-1]['quota_total_usd'])}. This is arithmetic, not a recommendation or evasion strategy.", source("S1", "S3", "S19", "S46")))
    routes.append(route_details("emigration", "10. Emigration property transfer", "Special",
        "SAFE provides a formal route for a qualifying emigrant to liquidate lawful property owned before obtaining the relevant emigration status and transfer it abroad. It is not a generic route for any savings.",
        ["Designed for capital/property transfers", "Can address amounts outside ordinary current-account income"],
        ["Strict applicant/property/tax eligibility", "Full intended property amount must be addressed in the application", "Staged-remittance rules and professional costs can apply"],
        ["Confirm you meet the emigration/status and property-timing requirements in SAFE’s current service guide.", "Prepare the application, identity/settlement evidence, source and title documents, tax certificate/payment evidence and any agent documents.", "Apply to the SAFE office specified for the former household-registration location; disclose the full intended transfer.", "After approval, take the approval/registration documents to the designated bank for purchase/remittance.", "For staged transfers, follow the approved timing and present prior-remittance evidence at later stages.", "Retain approval, tax, FX and remittance records."],
        "If BOC executes the final wire, its published baseline applies. Matrix D models one approved remittance at or below CNY 200,000 and 50%/25%/25% above that threshold; taxes, legal/notary/agent and other professional costs remain blank.", source("S20", "S4")))
    routes.append(route_details("inheritance", "11. Inherited PRC property → outward transfer", "Special",
        "A foreign citizen may use SAFE’s inheritance property-transfer process for lawfully inherited PRC assets after realization and required documentation.",
        ["Explicit legal channel for inherited capital", "Can cover financial assets as well as realized property"],
        ["Notarization, title, tax and deceased-person records", "Different decedents and disputes can complicate review", "Not a substitute for documenting ordinary savings"],
        ["Confirm the assets form a lawful, undisputed inheritance and identify the correct SAFE jurisdiction.", "Prepare application and passport plus notarized inheritance evidence, decedent title documents, financial-asset records and tax evidence.", "Submit through the available SAFE service channel or with a properly documented agent.", "After approval, liquidate where required and have the bank execute purchase/remittance under the approval.", "Keep notarized, tax, sale/liquidation and final wire evidence."],
        "BOC baseline only if BOC is used. Legal, notary, liquidation, tax and professional fees —.", source("S20", "S4")))
    routes.append(route_details("property", "12. Foreign individual sells lawfully owned PRC home → remit after-tax proceeds", "Special",
        "SAFE’s 2025 operating guide provides bank handling for a foreign individual’s registered sale of PRC residential property. Remittance cannot exceed the seller’s share of sale proceeds after included taxes/fees.",
        ["Specific bank-based path for property capital", "No artificial $50,000 convenience-quota ceiling stated for eligible proceeds"],
        ["Requires genuine registered sale and completed title transfer", "Tax evidence must match the requested remittance", "Property ownership and local eligibility facts matter"],
        ["Verify original ownership and the seller’s foreign-individual status/share.", "Complete the genuine sale, registered contract and title transfer.", "Obtain the competent tax authority’s evidence for the transaction.", "Give the bank passport, registered sale/title documents and tax evidence; request remittance no greater than the after-tax seller share.", "Have the bank check consistency, execute purchase/remittance and complete balance-of-payments reporting.", "Keep the full ownership-to-remittance chain."],
        "BOC baseline if selected; property taxes, sale costs and adviser fees are excluded/blank.", source("S21", "S4")))
    routes.append(route_details("property-refund", "13. Uncompleted foreign-buyer property purchase → refund/reconversion", "Special",
        "The same SAFE guide covers returning unused RMB purchase funds when the property transaction fails. This is a reconversion/refund route, not a way to cycle unrelated CNY.",
        ["Specific failed-purchase mechanism", "Original path and interest treatment are addressed by the guide"],
        ["Original payment/conversion evidence required", "Transaction-failure and regulatory records required", "Cannot exceed the refundable amount"],
        ["Collect the original payment and FX-conversion records.", "Obtain evidence that the purchase/registration failed or was lawfully cancelled, plus any required written explanation.", "Present passport and the regulator/escrow documents requested by the bank.", "Request reconversion and return along the original path or eligible same-name FX account as instructed.", "Document any permitted interest separately and retain all bank records."],
        "Only the documented refundable amount is eligible. Execution and receiving fees follow the chosen bank; current non-BOC values —.", source("S21")))
    routes.append(route_details("investment-exit", "14. Foreign direct-investment exit, equity sale or liquidation proceeds", "Fact-specific",
        "SAFE’s capital-account guide addresses repatriation of foreign-invested enterprise proceeds, including equity transfers and liquidation. This applies to genuine investment capital, not relabeling a personal bank balance.",
        ["Formal channel for business capital", "Bank and registration framework supports large documented transactions"],
        ["Corporate, registration, valuation and tax facts are decisive", "May require transaction-control information and tax documents", "Professional implementation is normally necessary"],
        ["Map the entity, investor, registration and exact exit event.", "Obtain the relevant equity/liquidation documents and bank/SAFE registration-control information.", "Complete required corporate approvals and tax filing/payment evidence.", "Ask the handling bank to verify transaction authenticity, amount and registration data before purchase/remittance.", "Remit to the documented foreign investor and retain corporate, tax and bank records."],
        "Institution-specific costs and tax are blank. Do not apply the personal-income model to business proceeds.", source("S22")))
    routes.append(route_details("cash", "15. Convert to USD cash → carry to the United States", "Small only",
        "China’s rules distinguish cash from account FX. Up to $5,000 equivalent needs no carrying permit; above $5,000 through $10,000 needs a bank permit. Above $10,000 is generally prohibited except specified special cases requiring SAFE permission. Customs declaration is a separate layer: inbound and outbound travellers are limited to RMB 20,000 each per trip and must declare currency beyond the prescribed amount under the 2025 instrument that replaced the 2007 announcement.",
        ["No international wire", "BOC’s published carrying-permit fee is waived through 2026-12-31"],
        ["Loss/theft and travel risk", "Not scalable beyond $10,000", "China permit and US monetary-instrument declaration are separate"],
        ["Establish lawful CNY source and complete the bank’s purchase/withdrawal review.", "For more than $5,000 through $10,000, obtain the bank carrying permit before departure; for a special case above $10,000, obtain SAFE permission rather than assuming it will be granted.", "Keep purchase, withdrawal and permit documents with the cash.", "At US entry, file FinCEN Form 105 when transporting more than $10,000 in currency/monetary instruments; exactly $10,000 is not ‘more than.’", "For a US bank cash deposit, respond to source questions and remember banks aggregate same-day cash over $10,000 for CTR purposes.", "Do not divide cash among people or days to evade China or US reporting."],
        "FX purchase spread can be modeled, but cash-withdrawal, travel, insurance, US deposit and security costs are blank. Amounts above $10,000 are marked generally infeasible, not priced as routine travel.", source("S7", "S49", "S50", "S4", "S51", "S30")))
    routes.append(route_details("atm", "16. Chinese bank card → overseas ATM cash", "Emergency",
        "SAFE caps domestic-card overseas ATM withdrawals at CNY 100,000 per person per year and CNY 10,000 per card per day. This produces cash, not a USD bank-account transfer, and borrowed-card evasion is prohibited.",
        ["Immediate access to local currency abroad", "Published BOC UnionPay fee cap per withdrawal"],
        ["Only the $10,000 scenario fits the annual cap at this FX rate", "ATM owner surcharge and execution FX can add cost", "Cash deposit/reporting and physical-security issues remain"],
        ["Check your annual person-level withdrawal total and card-level daily total before traveling.", "Ask BOC which network/fee applies and request the ATM’s displayed surcharge and conversion terms before confirming.", "Withdraw within both limits using only your own card; do not borrow cards.", "Keep ATM and FX receipts; deposit cash transparently and answer bank source questions.", "Do not split deposits or use additional people/cards to bypass limits or reports."],
        f"At $10k: {COSTS[0]['atm_unionpay_withdrawals']} withdrawals at the CNY 10,000/card/day cap; current BOC UnionPay modeled fee {usd(COSTS[0]['atm_unionpay_fee_usd'])}; Visa/Mastercard formula effective 2026-11-11 {usd(COSTS[0]['atm_future_card_fee_usd'])}. Other matrix rows exceed the annual cap. FX and ATM-owner costs —.", source("S9", "S4", "S10")))
    routes.append(route_details("hk", "17. Hong Kong Payment Connect / offshore-CN H detour", "Incomplete",
        "BOC describes mainland–Hong Kong Payment Connect for specified CNY/HKD scenarios. That is not evidence of an unrestricted CNY→USD transfer to the US, and routing through Hong Kong does not erase mainland source rules.",
        ["May be useful for a genuine qualifying mainland–HK payment", "Participating-bank channel"],
        ["Not a complete documented CNY→USD route", "Southbound direction/residence and currency constraints", "Second-leg FX/fees and US receipt unverified"],
        ["Do not initiate a detour until both banks confirm the complete lawful path in writing.", "Verify your eligibility, direction, currency and purpose for the mainland–HK leg.", "Separately verify the HK account’s CNY/HKD→USD conversion and US remittance terms.", "Compare all legs and retain evidence; otherwise use the direct bank route."],
        "Every price cell remains blank because no complete official two-leg CNY→USD cost schedule was established.", source("S23", "S1")))
    routes.append(route_details("unsupported", "18. PayPal China, standalone wallets, private swaps, crypto and false-trade workarounds", "Avoid",
        "No primary evidence was found for direct PayPal China or standalone Alipay/WeChat own-account CNY→USD repatriation. Wise’s use of Alipay as a funding rail is not proof of a standalone wallet service. Private swaps, borrowed quotas, false invoices and crypto P2P are not lawful substitutes.",
        ["No verified advantage to recommend"],
        ["Unsupported product availability can strand funds", "Private FX and evasion expose users to enforcement", "PBOC prohibits virtual-currency-related business activities covered by its notice"],
        ["Do not fund an unverified route.", "For a genuine wallet product, obtain operator terms explicitly supporting your passport, China funding, USD conversion and own US payout; otherwise leave it unused.", "Never borrow quotas, split to evade review, fabricate trade documents or use underground changers.", "Do not use crypto/stablecoins as a quota workaround; use a documented licensed route instead."],
        "No cost matrix is offered for prohibited or unproven workarounds. Unknown is not zero and technical feasibility is not legality.", source("S17", "S18", "S19", "S24", "S11")))
    body = f'''
{callout("info", "How to use these procedures", "Complete the identity/source check before paying any fee. The procedures deliberately separate lawful routes from unproven products and prohibited shortcuts. Cost values link to the full matrices; unknown institution-specific values stay blank.")}
<section class="section"><div class="section-heading"><p class="eyebrow">Route library</p><h2>18 routes with pros, cons, and exact procedures</h2><a href="penalties.html">Jump to $10k–$400k costs →</a></div><div class="route-list">{''.join(routes)}</div></section>
<section class="section"><h2>Documents to keep for every lawful route</h2>{table(["Record", "Purpose", "Official basis"], [
    ("Passport and bank identity classification", "Distinguish foreign-individual from domestic-individual treatment", source("S2")),
    ("Source contracts, payslips, transaction/title records", "Match the money to a lawful current-account or capital-account category", source("S1", "S20", "S21", "S22")),
    ("Chinese tax records and prior US returns", "Substantiate after-tax source and analyze FEIE/FTC without double counting", source("S1", "S33")),
    ("Execution quote, FX memo, fee and SWIFT/provider receipts", "Prove actual cost and amount sent; replace planning assumptions with actuals", source("S4", "S5")),
    ("Historical maximum balances and final US credits", "FBAR/Form 8938 analysis and reconciliation", source("S25", "S27")),
], "A single evidence folder should follow the money from origin through final USD credit.")}</section>'''
    return layout("methods.html", "Conversion routes and exact procedures", "Eighteen bank, provider, property, cash, conditional, unproven and prohibited paths—with implementation steps and primary evidence.", body)


def summary_page():
    """Executive brief: the decision, the numbers, the routes, the tax boundary."""
    number_rows = []
    for i in [0, 4, 9, 19, 39]:
        r = COSTS[i]
        pct = r["base_usd"] / r["amount_usd"] * D(100)
        number_rows.append((
            f"<strong>{usd(r['amount_usd'])}</strong>",
            cny(r["principal_cny"]),
            f"<strong>{usd(r['base_usd'])}</strong>",
            f"{pct:.3f}%",
            source("S4", "S5", "S48"),
        ))
    number_table = table(
        ["USD principal", "CNY principal", "BOC known modeled cost", "Cost as % of principal", "Official sources"],
        number_rows,
        "Published 2025-11-11 personal tariff plus a same-quote half-spread benchmark at the dated 6.6648 / 6.6929 retail pair. Excludes correspondent deductions, recipient fees, taxes and unknown costs. Full 40-row grid: <a href=\"penalties.html\">Costs</a>.",
        "numeric matrix",
    )
    shortlist = [
        ("Documented after-tax Chinese income → licensed-bank wire", "Default for a US passport holder", f"{usd(COSTS[0]['base_usd'])} at $10k · {usd(COSTS[-1]['base_usd'])} at $400k known model", "Bank must accept the identity, source-of-funds and tax evidence", '<span class="tag good">Primary</span>', source("S1", "S2", "S4", "S5", "S48")),
        ("Existing foreign-currency savings → own-account wire", "Funds already held in USD", f"{usd(COSTS[0]['existing_usd_wire_usd'])} at $10k · {usd(COSTS[-1]['existing_usd_wire_usd'])} at $400k before receiving charges", "No CNY conversion needed; receiving deductions remain unknown", '<span class="tag good">Conditional</span>', source("S1", "S4")),
        ("Wise from CNY (bank app / Alipay funding)", "Eligible non-mainland-Chinese user with Chinese tax records", "Current fee and execution rate —; live quote required", "Own-name recipient only; CNY 300,000 / 50,000 per-transfer caps; overall limit based on tax records", '<span class="tag mixed">Compare live quote</span>', source("S11", "S12", "S13")),
        ("Domestic-individual annual convenience quota schedule", "Only if the bank classifies you as a domestic individual", f"Illustrative $400k over 8 annual $50k wires: {usd(COSTS[-1]['quota_total_usd'])}", "Constant-rate arithmetic, not advice to split or borrow quotas", '<span class="tag mixed">Not default</span>', source("S1", "S46", "S19")),
        ("Emigration / inheritance property transfer", "Qualifying emigrant or foreign heir of PRC property", f"Staged $400k BOC model: {usd(COSTS[-1]['emigration_staged_total_usd'])}", "SAFE application for the full amount; staged remittance; professional and tax costs unknown", '<span class="tag good">Special route</span>', source("S20", "S4")),
        ("USD cash carry", "Small, fully documented amount only", "Travel, insurance and security costs —", "≤ $5k no permit; > $5k–$10k bank permit; > $10k generally prohibited except special SAFE cases; RMB 20,000 per-trip cash limit", '<span class="tag mixed">Not scalable</span>', source("S7", "S8", "S49", "S50", "S4")),
        ("Chinese card → overseas ATM", "Emergency cash, not a USD account transfer", f"$10k scenario: {usd(COSTS[0]['atm_unionpay_fee_usd'])} UnionPay modeled issuer fee", "At the modeled rate only $10k fits an unused CNY 100,000/year cap; CNY 10,000/card/day", '<span class="tag mixed">Very limited</span>', source("S9", "S4", "S10")),
        ("Private swaps, borrowed quotas, fake invoices, crypto workarounds", "No lawful implementation", "Not priced; statutory penalty exposure", "Watch-list treatment and fines under the current FX regulations", '<span class="tag bad">Avoid</span>', source("S18", "S19", "S17", "S24")),
    ]
    shortlist_table = table(
        ["Route", "Best fit", "Cost position", "Controlling constraint", "Assessment", "Official sources"],
        shortlist,
        "Ranked by evidential strength, not by a claim of a universal cheapest price. Every row links primary evidence; see <a href=\"methods.html\">Methods</a> for the 18 step-by-step procedures.",
    )
    tax_rows = [
        ("Moving your own existing balance", "Not itself a new wage or gift — but not proof of zero tax", "Underlying income, interest, gains, residence and information returns still require analysis", source("S32", "S38", "S39")),
        ("FBAR / FinCEN 114", "Aggregate foreign accounts exceeded $10,000 at any time in the calendar year", "Due April 15 with automatic extension to October 15", source("S25", "S26", "S52")),
        ("Form 8938", "Separate thresholds by residence and filing status; both FBAR and 8938 can apply", "Filed with the annual return; specified foreign financial assets", source("S27")),
        ("Form 3520", "Specified foreign gifts/bequests and trusts, not moving your own savings", "Gifts/bequests over $100,000 from a foreign individual or estate; 5%/month late penalty capped at 25% for covered cases", source("S28")),
        ("Lawful US tax relief", "FEIE 2026 maximum $132,900 per qualifying person; foreign tax credit for qualifying foreign income tax", "No credit on income excluded under FEIE; treaty saving clause preserves broad US taxation of citizens", source("S34", "S35", "S33", "S41")),
        ("China noncompliance exposure", "Up to 30% of the amount; serious cases 30% up to 100% for covered FX violations; cash violations up to 20%", "Maximums are statutory ranges, not a prediction of an assessment", source("S18", "S19")),
    ]
    tax_table = table(
        ["Topic", "Verified rule", "Decision constraint", "Official sources"],
        tax_rows,
        "No personalized tax amount can be computed from the principal alone. Full analysis: <a href=\"taxes.html\">Taxes</a>.",
    )
    steps = [
        "Classify your identity with the bank: SAFE defines a passport-holding foreign citizen as a foreign individual, which is not the same as a domestic individual for the annual convenience quota. " + source("S2", "S1"),
        "Classify the money: after-tax salary, existing foreign currency, unused RMB from an earlier conversion, inheritance and property proceeds each follow different rules. " + source("S1", "S20", "S21"),
        "Assemble the evidence chain: passport, contracts/payslips, amount-matched records, Chinese tax receipts and prior US returns. " + source("S1", "S32"),
        "Resolve US reporting first: FBAR, Form 8938, Form 3520 and any past-due filings are independent of the transfer rail. " + source("S25", "S27", "S28", "S36"),
        "Ask the Chinese bank for a written all-in quote: CNY debit, FX rate, commission, telecom, correspondent deduction and final USD credit. " + source("S4", "S6"),
        "If eligible, obtain Wise's live CNY quote and compare the final USD received — not just the headline fee. " + source("S11", "S13"),
        "Execute the documented route to your own US account; never split to evade review or borrow another person's quota. " + source("S1", "S19"),
        "Keep the FX memo, all fee receipts and the final credit; reconcile against the model and update FBAR maximum balances. " + source("S4", "S25"),
    ]
    body = f'''
{callout("info", "Executive answer", "For a US citizen holding CNY in a Chinese bank account, the best-evidenced route is a licensed-bank conversion and an own-account international wire supported by lawful source-of-funds and Chinese tax evidence. The USD 50,000 annual convenience purchase quota is written for domestic individuals; it is not blanket ID-only permission for a foreign individual. Moving your own principal is not itself new taxable income, but it is not proof of zero tax: underlying income, interest, currency gains, tax residence and US information returns must be analyzed separately. " + source("S1", "S2", "S32"))}
{callout("warn", "Read before acting", "Every figure below is a planning model from published official inputs, not an executable bank quote. The BOC retail rate used here is a dated 2026-11-09 05:30 snapshot; the official board is a rolling window and no longer displays that exact row; BOC's historical date search requires a captcha. The exact historical row was not independently re-retrieved in this session. Obtain a written same-time rate and all-in fee quote before execution. Blank or “—” means unknown, never zero. " + source("S5", "S4"))}
<section class="section"><div class="section-heading"><p class="eyebrow">01 · Most important numbers</p><h2>Known modeled cost at five amounts</h2><a href="penalties.html">All 40 amounts →</a></div>{number_table}</section>
<section class="section"><div class="section-heading"><p class="eyebrow">02 · Route shortlist</p><h2>Which method fits which facts</h2><a href="methods.html">18 procedures →</a></div>{shortlist_table}</section>
<section class="section"><div class="section-heading"><p class="eyebrow">03 · Tax and penalty boundary</p><h2>What the transfer does and does not change</h2><a href="taxes.html">Full tax analysis →</a></div>{tax_table}</section>
<section class="section"><div class="section-heading"><p class="eyebrow">04 · Execution</p><h2>Eight steps, in order</h2></div><ol class="procedure">{''.join(f"<li>{s}</li>" for s in steps)}</ol></section>
<section class="section"><div class="section-heading"><p class="eyebrow">05 · Verification boundary</p><h2>What remains unverified</h2></div><p>Current provider quotes, correspondent and recipient deductions, personal tax amounts, eligibility, cash/travel costs and a permanent official URL for the dated BOC quote are deliberately left blank. They are published with their required manual checks on the <a href="flagged.html">Flagged for Review</a> page. The complete primary-source register is on <a href="sources.html">Sources</a>. {source("S5", "S48", "S4", "S32")}</p></section>'''
    return layout("summary.html", "Executive summary", "The decision, the modeled costs, the route shortlist, the tax boundary and the eight execution steps — each linked to primary evidence.", body)


def penalties_page():
    bank_rows = []
    compare_rows = []
    physical_rows = []
    special_rows = []
    for r in COSTS:
        a = r["amount_usd"]
        bank_rows.append((
            f"<strong>{usd(a)}</strong>", cny(r["principal_cny"]), cny(r["commission_cny"]), cny(r["telecom_cny"]), cny(r["spread_cny"]),
            f"<strong>{usd(r['base_usd'])}</strong>", usd(r["existing_usd_wire_usd"]), usd(r["draft_known_usd"]) + " + —", source("S4", "S5")
        ))
        compare_rows.append((
            f"<strong>{usd(a)}</strong>", usd(r["full_arrival_other_us_plus_bofa_usd"]),
            f"{r['quota_wires']} annual wire(s) · {usd(r['quota_total_usd'])}",
            "— (current quote unverified)",
            "— (current quote unverified)",
            "— (current quote)", source("S4", "S42", "S1", "S11", "S13", "S15")
        ))
        if "atm_unionpay_fee_usd" in r:
            union = f"{r['atm_unionpay_withdrawals']} withdrawal(s) · {usd(r['atm_unionpay_fee_usd'])}"
            future = f"{r['atm_future_card_withdrawals']} withdrawal(s) · {usd(r['atm_future_card_fee_usd'])}"
        else:
            union = "Above annual cap at modeled rate · —"
            future = "Above annual cap at modeled rate · —"
        mg = "— (dated $32 tier ends at $9,999.99)" if a == D(10000) else "— (outside dated schedule)"
        cash = "Bank permit · cost —" if a == D(10000) else "Generally prohibited; special SAFE permit · —"
        physical_rows.append((f"<strong>{usd(a)}</strong>", "— (current fee/FX)", mg, union, future, cash, source("S15", "S16", "S9", "S4", "S10", "S7")))
        emigration_time = "one approved remittance" if r["emigration_wires"] == 1 else "50% now / 25% after 1 year / 25% after 2 years"
        special_rows.append((
            f"<strong>{usd(a)}</strong>",
            f"{r['emigration_wires']} wire(s) · {emigration_time}<br>{usd(r['emigration_staged_total_usd'])}",
            f"1 wire modeled (splitting optional)<br>{usd(r['inheritance_one_wire_total_usd'])}",
            f"1 wire modeled<br>{usd(r['property_sale_one_wire_total_usd'])}",
            "— (institution-specific)", source("S20", "S21", "S22", "S4", "S5")
        ))
    bank_table = table(
        ["USD principal", "CNY principal", "BOC commission", "Telecom", "FX half-spread", "BOC TT known total (USD)", "Existing-USD wire subtotal", "BOC draft subtotal + postage/collection", "Sources"],
        bank_rows,
        "Matrix A · All 40 amounts. BOC TT and draft models include CNY conversion; existing-USD wire does not. Draft subtotal excludes actual postage and US collection. All exclude underlying tax and unknown charges.",
        "numeric matrix"
    )
    compare_table = table(
        ["USD principal", "BOC TT + $25 full-arrival + $15 BofA example", "Conditional domestic $50k/year model", "Wise bank: current total", "Wise Alipay: current total", "Western Union current total", "Sources"],
        compare_rows,
        "Matrix B · Route variants. Wise current totals are unverified and blank. Wise fees are deducted from the CNY sent before conversion, so fee examples do not establish the same net USD received. Do not rank these costs without live same-net-receipt quotes. BOC full-arrival uses the non-BOC-NY $25 tier; BofA’s $15 inbound charge can be waived by account. Domestic schedule is conditional arithmetic, not advice to split.",
        "numeric matrix"
    )
    physical_table = table(
        ["USD principal", "Western Union", "MoneyGram dated fee", "BOC UnionPay ATM (current)", "BOC Visa/MC ATM from 2026-11-11", "USD cash carry", "Sources"],
        physical_rows,
        "Matrix C · Every amount for transmitters and physical routes. Only the $10,000 ATM scenario fits SAFE’s CNY 100,000/person/year cap at this quote, assuming the entire annual allowance remains; eligibility changes with the rate and prior withdrawals. No current WU price or MG tier above $9,999.99 is inferred.",
        "numeric matrix"
    )
    special_table = table(
        ["USD principal", "Qualifying emigration property transfer", "Qualifying inheritance transfer", "Foreign seller’s after-tax property proceeds", "Direct-investment exit", "Sources"],
        special_rows,
        "Matrix D · Conditional legal-property routes, assuming BOC executes at the same dated inputs. Emigration amounts up to CNY 200,000 may be remitted once after approval; larger scenarios model the maximum 50%/25%/25% schedule. Inheritance can be one or several remittances. None is a generic savings workaround.",
        "numeric matrix"
    )
    # These methods are covered separately so every requested amount has an
    # explicit blank rather than silently borrowing BOC's tariff or inventing a quote.
    unpriced_rows = [
        (f"<strong>{usd(a)}</strong>", "—", "—", "—", "—", "—", "—",
         source("S1", "S21", "S24", "S23", "S17", "S11"))
        for a in AMOUNTS
    ]
    unpriced_table = table(
        ["USD principal", "Unused RMB reconversion", "Other licensed bank wire", "Property purchase refund", "HK detour", "Standalone wallet / PayPal", "Private swap / crypto workaround", "Sources"],
        unpriced_rows,
        "Matrix E · Unverified costs or routes, all 40 amounts. Dashes are unknown, not zero. Reconversion or property refunds may qualify only with applicable evidence; another bank must quote its own prices. The HK and standalone wallet paths are unverified; private swaps and crypto workarounds should not be used. These blanks do not constitute a finding that a route is available.",
        "numeric matrix",
    )
    exposure_rows = []
    for key in (0, 4, 9, 19, 29, 39):
        r = COSTS[key]
        amount = r["amount_usd"]
        exposure_rows.append((
            f"<strong>{usd(amount)}</strong>",
            usd(amount * D("0.30")),
            usd(amount),
            usd(amount * D("0.20")),
            "$16,536",
            usd(r["base_usd"]),
            source("S18", "S26", "S4", "S5"),
        ))
    exposure_table = table(
        ["USD principal", "FX-offence fine at 30% ceiling", "Serious FX-offence ceiling (100% of amount)", "Unlawful cash-carry fine at 20% ceiling", "FBAR nonwillful max (per violation)", "Lawful BOC modeled cost (same amount)", "Sources"],
        exposure_rows,
        "Illustrative arithmetic on statutory maximum rates, not an assessment, prediction, or quote. [S18] Art. 39/40/45 allow a fine up to 30% of the amount and, in serious cases, from 30% up to the equivalent amount (100%). Art. 42 allows up to 20% for unlawful currency carriage. FBAR nonwillful maximum is $16,536 per violation [S26]. The lawful column is the modeled BOC cost at the same principal [S4][S5], excluding underlying tax and unknown fees.",
        "numeric matrix",
    )
    penalty_rows = [
        ("Unlawful removal of domestic FX / deceptive capital transfer", "Order to repatriate; fine up to 30%; serious cases 30% up to 100%; criminal liability if constituted", source("S18")),
        ("Fraudulent documents / illegal FX arbitrage", "Reconversion plus fine up to 30%; serious cases 30% up to 100%; criminal liability if constituted", source("S18")),
        ("Private, disguised, speculative or introduced FX dealing at covered scale", "Warning, confiscation of illegal gains, fine up to 30%; serious cases 30% up to 100%; criminal liability if constituted", source("S18")),
        ("Noncompliant FX cash carried across border", "Warning and possible fine up to 20%; customs rules may govern", source("S18")),
        ("Borrowed quotas / splitting to evade authenticity or quota review", "Watch-list process; current and following two years, with document-based review during that period", source("S19")),
        ("FBAR nonwillful maximum", "Up to $16,536 per violation under current 31 CFR 1010.821 (assessments on/after 2025-01-17); not an automatic assessment", source("S26")),
        ("FBAR willful maximum", "Greater of $165,353 or 50% of the statutory balance amount per violation under the cited regulation; criminal exposure is separate", source("S26", "S25")),
        ("Form 3520 specified foreign gift reporting", "5% of gift per month, capped at 25%, for covered late reporting; see instructions for facts/defenses", source("S28")),
    ]
    body = f'''
{callout("info", "Rate freshness check — " + RESEARCH_DATE, "A second read of " + source("S48") + " at 2026/11/10 07:32:39 Beijing showed USD buying 666.22 and selling 669.03 CNY per 100 USD, with a separately published Middle Rate column of 671.88. The matrices use the earlier 2026-11-09 05:30 row (666.48 / 669.29 per 100 USD). BOC's Middle Rate is a distinct published column, not the arithmetic midpoint of its buy/sell quotes, so the model computes its own midpoint. Both are dated snapshots, not executable quotes: obtain a written same-time rate before execution. See <a href='flagged.html'>Flagged for Review</a>.")}
{callout("warn", "Read the model boundary", "These are planning models from official published inputs—not executable all-in quotes. CNY principal means the USD-equivalent principal multiplied by 6.6929; final USD received requires a live execution rate and every intermediary/receiver fee. A blank means unknown, not zero.")}
<section class="section"><div class="section-heading"><p class="eyebrow">Model inputs</p><h2>Formula and source hierarchy</h2></div><div class="formula-grid"><div><h3>BOC personal US-bound TT</h3><code>fee CNY = clamp(0.001 × USD principal × 6.6929, 50, 260) + 150</code><p>Current 2025-11-11 personal tariff. Electronic channels share counter pricing; agreements/promotions and actual foreign-bank charges may differ. {source("S4", "S45")}</p></div><div><h3>Same-quote retail benchmark</h3><code>midpoint = (6.6648 + 6.6929) / 2 = 6.67885</code><code>half-spread = principal × (6.6929 − midpoint) / midpoint</code><p>0.2103656% of USD-equivalent principal. This is an arithmetic benchmark, not a guaranteed markup or accessible mid-market execution. {source("S5")}</p></div><div><h3>Wise examples, not quotes</h3><p>Wise published examples for a CNY 10,000 transfer in 2024, including bank-app and Alipay funding. Those examples do not establish current prices at these matrix amounts. Current totals and execution rate remain blank. {source("S11", "S13")}</p></div></div><p class="note">BOC quote timestamp: {QUOTE_TIME}. The research cutoff is {RESEARCH_DATE}. Cross-check: BOC’s board on 2026-11-10 02:49 Beijing showed USD buy 6.6622 / sell 6.6903, a half-spread of 0.210449% versus the modeled 0.210366% (about 0.04% relative difference), so the dated input remains representative while the absolute rate has moved. The exact 2026-11-09 05:30 row has rolled off BOC’s paginated board; re-query that date through BOC’s official historical search. The quote is labeled, never treated as synchronous with another market rate. {source("S48")}</p></section>
<section class="section"><div class="section-heading"><p class="eyebrow">40 amounts · Bank rails</p><h2>BOC conversion, remittance, and draft costs</h2></div>{bank_table}</section>
<section class="section"><div class="section-heading"><p class="eyebrow">40 amounts · Alternatives</p><h2>Full-arrival, conditional annual, Wise and WU comparisons</h2></div>{compare_table}<p class="note">Other published BOC full-arrival tier: $15 when the receiving account is at BOC New York. Receiving examples: BofA $15 (some waivers), Chase Secure $15, Capital One $0 on account types other than Essential Checking, High-Yield Checking and Essential Savings, which pay $15; correspondent charges can be separate. {source("S4", "S42", "S43", "S44")}</p></section>
<section class="section"><div class="section-heading"><p class="eyebrow">40 amounts · Cash/transmitters</p><h2>Availability-limited routes and dated fee evidence</h2></div>{physical_table}<p class="note">ATM models exclude ATM-owner surcharge and unverified execution FX. Withdrawals are split at SAFE’s CNY 10,000 per card/day cap, so $10,000 (¥66,929) needs 7 withdrawals. Current UnionPay formula: min(¥112, ¥12 + 1% × CNY withdrawal) per withdrawal. Future Visa/Mastercard formula: 2.5% of the amount withdrawn, min $3/max $40 equivalent per withdrawal, effective 2026-11-11. {source("S4", "S9", "S10")}</p></section>
<section class="section"><div class="section-heading"><p class="eyebrow">40 amounts · Special property</p><h2>Emigration, inheritance, property sale, and investment exit</h2></div>{special_table}<p class="note">The emigration route requires one application for the full intended property amount. The schedule is a maximum-tranche planning model, not permission to defer documented current-account income. Inheritance and property-sale rows assume one wire for comparability; professional, tax, title, liquidation and receiving costs remain excluded. {source("S20", "S21")}</p></section>
<section class="section"><div class="section-heading"><p class="eyebrow">40 amounts · Remaining routes</p><h2>Unverified or unpriced methods</h2></div>{unpriced_table}</section>
<section class="section" id="penalty-vs-cost"><div class="section-heading"><p class="eyebrow">Penalty vs lawful cost</p><h2>Why the route choice dominates the cost</h2></div><p>At every amount the published statutory ceiling for an FX offence is a multiple of the modeled lawful conversion cost. The comparison below applies the statutory <em>rates</em> to the principal; it is not an estimate of what a regulator would assess, and enforcement is discretionary and fact-specific.</p>{exposure_table}</section>
<section class="section"><div class="section-heading"><p class="eyebrow">Noncompliance exposure</p><h2>Corrected penalties—no invented ranges</h2></div>{table(["Rule / violation", "Published consequence", "Official sources"], penalty_rows, "Maximums and ranges are not predictions of an assessment. Criminal, tax, accuracy, fraud and other consequences depend on the facts and are not comprehensively priced.")}</section>'''
    return layout("penalties.html", "Cost matrices and penalty exposure", "Reproducible $10,000–$400,000 scenarios at $10,000 increments, statutory penalty ceilings versus lawful cost, and corrected China/US reporting penalties.", body)


def taxes_page():
    reporting = [
        ("US worldwide income", "Report taxable worldwide income even when living abroad; filing can still be required when FEIE/FTC reduces liability", "Every route; underlying wages, interest, gains and other income", source("S32")),
        ("FBAR / FinCEN 114", "Aggregate foreign financial accounts exceeded $10,000 at any time in the calendar year", "Due April 15; automatic extension to October 15; maximum balances, not transfer size", source("S25", "S52")),
        ("Form 8938 — living in the US, unmarried/MFS", "More than $50,000 on last day or more than $75,000 at any time", "Specified foreign financial assets; filed with annual return when required", source("S27")),
        ("Form 8938 — living in the US, MFJ", "More than $100,000 on last day or more than $150,000 at any time", "Separate from FBAR; both can apply", source("S27")),
        ("Form 8938 — living abroad, unmarried/MFS", "More than $200,000 on last day or more than $300,000 at any time", "Must also satisfy IRS ‘living abroad’ criteria; read the comparison", source("S27")),
        ("Form 8938 — living abroad, MFJ", "More than $400,000 on last day or more than $600,000 at any time", "Specified assets are broader than just bank accounts", source("S27")),
        ("Form 3520", "Gifts/bequests over $100,000 from a foreign individual or foreign estate, with related/nominee aggregation; separate trust rules", "Not a form for moving your own savings; 5% per month late penalty capped at 25% for covered gifts", source("S28")),
        ("FinCEN Form 105", "Bringing, sending or receiving more than $10,000 in currency/monetary instruments at one time into or out of the US; the threshold applies to a family or group total, not per person", "This is not FBAR and not an income tax", source("S51")),
        ("Bank CTR", "Financial institution reports same-day physical-cash transactions over $10,000, including known aggregation", "A report is not a tax or evidence of wrongdoing; never structure to avoid it", source("S30")),
        ("Form 8300", "Trade/business receipt of more than $10,000 cash in one or related transactions", "Not generally an individual’s own-account cash deposit; business facts can differ", source("S31")),
    ]
    china_rates = [
        ("≤ ¥36,000", "3%", "¥0", source("S39", "S54")),
        ("> ¥36,000–144,000", "10%", "¥2,520", source("S39", "S54")),
        ("> ¥144,000–300,000", "20%", "¥16,920", source("S39", "S54")),
        ("> ¥300,000–420,000", "25%", "¥31,920", source("S39", "S54")),
        ("> ¥420,000–660,000", "30%", "¥52,920", source("S39", "S54")),
        ("> ¥660,000–960,000", "35%", "¥85,920", source("S39", "S54")),
        ("> ¥960,000", "45%", "¥181,920", source("S39", "S54")),
    ]
    relief = [
        ("Foreign earned income exclusion", "2026 maximum $132,900 per qualifying person; requires eligible foreign earned income, foreign tax home and bona fide-residence or physical-presence test", "Does not exempt a bank transfer, interest, property gain or all prior income; file Form 2555 with the return", source("S34", "S35")),
        ("Foreign tax credit", "Credit qualifying foreign income taxes on income also subject to US tax, subject to category and limitation rules", "Often central when Chinese tax was paid; no FTC on income excluded under FEIE", source("S33")),
        ("US–China treaty", "Allocates taxing rights and provides relief mechanisms, but saving-clause rules preserve broad US taxation of citizens/residents", "Do not assume a treaty makes a US citizen’s transfer or Chinese salary tax-free", source("S41")),
        ("Personal FX gain", "Publication 525 says personal foreign-currency transaction gain need not be included unless over $200; if over $200, report as capital gain", "Different business/investment rules may apply; preserve acquisition/disposition rates and basis", source("S38", "S47")),
        ("Past nonwillful filings", "Streamlined offshore/US-resident procedures can apply to eligible taxpayers; generally three tax years and six FBAR years", "Eligibility and penalties differ; do not quietly back-file if a formal procedure is appropriate", source("S36", "S37")),
    ]
    tax_rows = []
    for r in US_TAX:
        tax_rows.append((
            f"<strong>{usd(r['amount'])}</strong>",
            usd(r['other_taxable']),
            usd(r['ordinary_delta']),
            f"10% = {usd(r['fx_gain'])} → {usd(r['fx_gain_tax'])}",
            usd(r['feie_tax']),
            "— (needs acquisition date and rate)",
            source("S53"),
        ))
    tax_table = table(
        ["Amount in question", "Assumed other taxable income (single)", "If ordinary income: added US tax", "If a 10% currency gain: US capital-gain tax", "If FEIE-eligible earned income: US tax", "Measured FX gain", "Sources"],
        tax_rows,
        "Illustrative 2026 single-filer arithmetic from published brackets. The character of the money decides which column applies; column 6 stays blank because basis is unknown.",
        "numeric matrix",
    )
    body = f'''
{callout("info", "Tax conclusion", "Moving your own existing bank balance is not, by itself, a new wage or gift. That does not establish ‘zero tax’: underlying income/gains, interest, personal FX gain, tax residence and information returns still require analysis. No personalized tax amount can be calculated from principal alone.")}
<section class="section"><div class="section-heading"><p class="eyebrow">US compliance</p><h2>Reporting thresholds that can apply alongside the transfer</h2></div>{table(["Rule", "Trigger / requirement", "How to apply it", "Official sources"], reporting, "FBAR and Form 8938 are independent. Form 3520 is not triggered merely because you move your own funds.")}</section>
<section class="section"><div class="section-heading"><p class="eyebrow">China underlying tax</p><h2>Resident comprehensive-income schedule</h2></div><p>China’s IIT law makes a person domiciled in China, or without domicile but present at least 183 days in a tax year, a resident individual. Residents are taxed on China and foreign-source income; nonresidents on China-source income. The table applies to annual <strong>taxable</strong> comprehensive income after statutory deductions—not gross remittance principal. Nonresidents generally calculate wages monthly using the monthly-converted schedule and a ¥5,000 monthly expense deduction. Non-domicile 90-day, 183-day, six-year and treaty rules can change the income included. {source("S39", "S40")}</p>{table(["Annual taxable comprehensive income", "Rate", "Quick deduction", "Official source"], china_rates, "Tax = taxable income × rate − quick deduction, subject to the complete law, deductions, residence and special rules. Nonresident monthly brackets are 1/12 of these thresholds with quick deductions 1/12 of these values.")}<p class="note">Source of money and tax records are also required for the foreign-individual FX purchase route. Paying bank fees is not paying income tax. {source("S1")}</p></section>
<section class="section"><div class="section-heading"><p class="eyebrow">Lawful tax minimization</p><h2>Compare relief mechanisms without double counting</h2></div>{table(["Mechanism", "Verified rule", "Decision constraint", "Official sources"], relief, "The lowest legal tax outcome is fact-specific. Do not choose a transfer rail based on an assumed exemption.")}</section>
<section class="section"><div class="section-heading"><p class="eyebrow">The penalty, quantified</p><h2>What a tax bill on the balance would look like in 2026</h2></div><p>The feared “conversion penalty” is two separate questions. Mechanically, converting CNY to USD is a bank-fee event, not a tax event. The tax question is what the money <em>is</em>: already-taxed principal, wage income, a capital gain, or a gift. The table prices the same amount under each character so the scale of the risk is visible rather than assumed.</p>{tax_table}<div class="callout warn"><h2>Why the measured-gain column is blank</h2><p>A currency gain is measured between the rate when the CNY was acquired and the rate when it is converted. Acquisition dates and rates for a pre-existing balance are personal facts no public source can supply, so none is inferred. Publication 525 excludes a personal foreign-currency transaction gain unless it is more than $200 and reports it as a capital gain above that amount, so a held-for-personal-use balance converted once is a small separate line — not a percentage levy on the principal. {source("S38", "S47")}</p></div><p class="note">Assumptions: single filer, under 65, not blind, 2026 standard deduction of {usd(US_STANDARD_DEDUCTION_2026)} and {usd(US_OTHER_TAXABLE_2026)} of other taxable income. Brackets, capital-gain bands, the standard deduction and the {usd(FEIE_2026)} exclusion are quoted from IRS Rev. Proc. 2025-32. Change the assumed inputs and every figure moves. {source("S53", "S35")}</p></section>
<section class="section"><div class="section-heading"><p class="eyebrow">Execution worksheet</p><h2>Ten questions for a cross-border tax professional</h2></div><ol class="checklist"><li>Which years did the CNY income arise, and what were your China/US tax-residence positions in each?</li><li>How much is principal, interest, capital gain, gift, inheritance or business equity?</li><li>Which Chinese taxes were withheld or paid, and do you have amount-matched official records?</li><li>Which income was already reported on US returns, and at what translated USD basis?</li><li>Does FEIE qualify, and would FTC produce a better result across current and carryover years?</li><li>Are you claiming any treaty position requiring specific disclosure or residency analysis?</li><li>Does personal FX gain exceed $200, or do business/investment FX rules apply instead?</li><li>What were each foreign account’s maximum values for every open FBAR year?</li><li>Do Form 8938, 3520, trust/entity, state or other information returns apply independently?</li><li>If past filings were incomplete, are you eligible for streamlined or another formal correction procedure?</li></ol><p class="note">Personal tax due, China exit-related professional costs and US tax on the transfer are intentionally <strong>blank</strong> until these facts are known. See <a href="flagged.html">Flagged for Review</a>.</p></section>'''
    return layout("taxes.html", "China and US tax obligations", "Separate underlying tax from transfer mechanics: FBAR, FATCA, Form 3520, cash reporting, China IIT, FEIE, FTC, treaty and correction paths.", body)


def flagged_page():
    unresolved = [
        ("Independent line-by-line verification of the entire inherited research", "The current session rechecked selected high-impact primary sources and calculations, not every inherited claim or all external links; previous audit assertions are not independently certified by this session.", "Review remaining claims and legal updates against their linked primary documents before relying on them.", source("S1", "S4", "S18", "S32")),
        ("Strict evidence audit and current-cost blanks", "Historical scenario arithmetic is not verification of an executable current quote; unknown live fees and personal taxes remain blank in the strict register", 'Read <a href="evidence.html#audit-flags">the fresh evidence audit and its review flags</a> before relying on inherited estimates', source("S1", "S5", "S11")),
        ("Permanent official record of the 2026-11-09 05:30 BOC USD quote", "BOC's five-quote board has rotated and its historical date query requires a captcha; the exact row was not present on any of the five board pages at the 2026-11-10 re-check", "Request a written BOC rate confirmation or an archived official statement; re-run the model from verified current inputs before relying on the figures", source("S5", "S48")),
        ("Official definition of BOC's Middle Rate column", "The board publishes a Middle Rate that is a separate figure, not the arithmetic midpoint of its own buy/sell quotes; the model deliberately computes its own midpoint instead", "Ask BOC for the column definition and confirm which published rate applies to a personal FX purchase", source("S48")),
        ("Live BOC execution quote and actual foreign-bank deductions", "Dated quote is only a benchmark; route/correspondent/recipient can change net USD", "Obtain written same-time quote and final-credit confirmation", source("S4", "S5", "S6")),
        ("Current Wise CNY→USD fee and execution rate", "2024 examples are historical, and eligibility and overall limit are account-specific", "Start but do not fund a Wise transfer; record the displayed live quote", source("S11", "S12", "S13")),
        ("Western Union current China→US fee, FX and limits", "Official pages confirm route and variability, not a static current schedule", "Request agent/channel quote and payout limit", source("S14", "S15")),
        ("MoneyGram current service and amounts above $9,999.99", "Verified BOC schedule is dated 2018 and stops below $10,000", "Ask BOC for current MoneyGram terms; do not extrapolate", source("S16")),
        ("Other Chinese banks’ tariffs", "No current ICBC/CCB/other personal tariff was verified", "Obtain institution’s current personal price list and quote", source("S24")),
        ("Draft postage and US foreign-item collection terms", "BOC charges actual postage; US acceptance/fees/timing vary", "Get both banks’ written draft/collection instructions", source("S4", "S44")),
        ("US correspondent and recipient charge for your account", "Published examples do not establish your waiver or route", "Ask US bank for incoming international-wire and FX terms", source("S42", "S43", "S44")),
        ("ATM execution FX and owner surcharge", "Published issuer fee is not the total cash cost", "Read ATM screen and keep final CNY debit/USD cash receipts", source("S4", "S9", "S10")),
        ("Cash withdrawal, travel and deposit costs", "No uniform official total", "Budget actual transport/security and ask US bank about cash deposit", source("S7", "S29", "S30")),
        ("PayPal China / standalone Alipay / WeChat direct route", "No primary proof of exact passport-funded CNY→USD own-US-account service", "Do not use without explicit operator terms; Wise’s Alipay rail is different", source("S11", "S24")),
        ("Hong Kong second leg to USD/US", "Payment Connect evidence covers specified CNY/HKD mainland–HK flows only", "Obtain written two-bank complete-route confirmation or do not use", source("S23")),
        ("Personal China and US tax amounts", "Source, basis, residence, filing history, deductions and credits are unknown", "Provide year-by-year records to a cross-border tax professional", source("S32", "S33", "S39", "S40")),
        ("2026 §6039F threshold for gifts from foreign corporations/partnerships", "Resolved 2026-11-10: Rev. Proc. 2025-32 sets the 2026 §6039F aggregate threshold at USD 20,573, separate from the USD 100,000 nonresident-individual/estate gift threshold", "Applies only if such a gift exists; not to moving your own savings", source("S53", "S28")),
        ("Whether a provincial customs office has issued local guidance since 2025-04-01", "Only the national instrument (S50) and the PBOC limit (S49) were verified; branch-level implementation notes were not reviewed", "Ask the departure-port customs office (12360 hotline) for the operative threshold on your travel date", source("S50", "S49")),
        ("Current BOC promotional waiver", "The verified 2025 wire promotion expired 2025-12-31; none is assumed for 2026", "Ask branch/app for a current dated promotion and preserve terms", source("S45")),
    ]
    irregular = [
        ("PRC IIT rate schedules were not independently transcribed from law-page images", "Resolved 2026-11-10: all seven annual bracket thresholds, rates and deductions were checked against the Shanghai tax authority’s official text PDF; individual tax still depends on eligibility, deductions and source.", "Low", source("S39", "S54")),
        ("Wise comparison is not a same-net-payout quote", "Corrected the labels: Wise deducts fees from funded CNY before conversion; its historical fees and transfer counts do not demonstrate delivery of the USD principal. No current execution rate or total for an equal net payout was verified.", "High", source("S11", "S13")),
        ("MoneyGram historical top tier mislabeled as a $10,000 tier", "Corrected the dashboard: the $32 tier ends at $9,999.99; no fee for $10,000 or higher was verified.", "High", source("S16")),
        ("Customs cash-declaration source was cited for thresholds it does not contain (corrected 2026-11-10)", "The customs clearance-guide page used as S8 documents red/green channel procedure but not the RMB 20,000 / USD 5,000 figures it was labelled with. Those figures now rest on the PBOC announcement (S49) and the current customs instrument (S50); S8 is retained only for the channel procedure", "High", source("S49", "S50", "S8")),
        ("Relied-on customs announcement was repealed (corrected 2026-11-10)", "Customs Announcement 2007 No. 72 — the historical basis for the RMB 20,000 / USD-equivalent 5,000 declaration list — was repealed with effect from 2025-04-01 by Announcement 2025 No. 43, whose text was fetched from gov.cn. The duty to declare currency beyond the prescribed amount survives, but the older instrument must not be presented as current law", "High", source("S50")),
        ("CBP page cited for the $10,000 rule was not the page that states it (corrected 2026-11-10)", "The general “know before you go” travel page was replaced for this purpose by CBP’s dedicated money/monetary-instruments page (S51), which states the more-than-$10,000 report, the group-aggregation rule and the electronic FinCEN 105 filing route. No numeric value changed", "Medium", source("S51")),
        ("Receiving-bank example named an account type its source does not name (corrected 2026-11-10)", "Capital One charges $15 only on Essential Checking, High-Yield Checking and Essential Savings and no fee on its other account types; the earlier shorthand “360 Checking $0” is not what the page says. The note now states the disclosed condition", "Medium", source("S44")),
        ("Dead official link found during the 2026-11-10 re-verification", "A SAFE enforcement page previously used as a general citation (safe.gov.cn/en/2018/1206/1478.html) returns SAFE’s “page not found” notice. It was already absent from the published pages, so no live row depended on it; the penalty ranges rest on the State Council regulation (S18), which was fetched and read in full, including the separate 20% ceiling for illegally carried FX cash", "Medium", source("S18")),
        ("Identity classification can differ between the two Chinese rulebooks", "SAFE’s personal-FX measures treat a passport holder as 境外个人 (foreign individual) whatever the residence, while the State Council FX regulation defines 境内个人 to include a foreign national residing in China continuously for a year. Which regime a bank applies depends on account identity and residence facts; neither reading turns the USD 50,000 convenience quota into a general ID-only right", "High", source("S2", "S18", "S1")),
        ("Prior advice: every user gets $50,000 with ID only", "Corrected: annual convenience purchase quota applies to domestic individuals; foreign individuals follow lawful current-account income, reconversion or special routes", "High", source("S1", "S2", "S46")),
        ("Prior China private-FX fine: 30%–300%", "Corrected under current 2008 regulation: up to 30%; serious cases 30% up to 100%, plus other consequences", "High", source("S18")),
        ("Prior blanket ‘no US tax’ statement", "Corrected: moving own principal is not itself new income, but underlying income/gains, interest and personal FX rules remain", "High", source("S32", "S38")),
        ("BOC quote timestamp vs research cutoff", "Resolved: the quote is stamped 2026-11-09 05:30 Beijing time (= 2026-11-08 21:30 UTC) and is explicitly dated, never compared as though simultaneous with a different market quote. Re-verified 2026-11-10 against BOC’s live board (02:49: buy 6.6622 / sell 6.6903), which corroborates the magnitude and the ~0.21% half-spread benchmark", "Medium", source("S5", "S48")),
        ("BOC’s paginated board no longer displays the exact cited FX row", "The 2026-11-09 05:30 USD row (buy 666.48 / sell 669.29 CNY per USD) had rolled off page 5 by 2026-11-10, so the original page link could not reproduce the input. S5 was repointed to BOC’s official historical search (query 2026-11-09 + USD); the values remain reproducible only by that date query, not from a permanent archived page. Live-board magnitude is corroborated at 6.6622 / 6.6903", "Medium", source("S5", "S48")),
        ("Cost model treated Wise/ATM CNY caps as USD amounts (corrected 2026-11-09)", "The inherited model split the USD principal at 300,000/50,000/10,000 as if those caps were USD. Wise caps are CNY 300,000 (bank app) and CNY 50,000 (Alipay) per transfer, and the ATM cap is CNY 10,000 per card/day. The previous model corrected the currency units, but the Wise fee examples were later removed from the matrix because current prices and equal-payout counts are unverified. The ATM model uses CNY units and remains a dated illustrative scenario.", "High", source("S11", "S9", "S10")),
        ("ATM tariff changes one day after the research cutoff", "The 2025-11-11 price list is current on the cutoff date; the separate Visa/Mastercard formula is labeled from its 2026-11-11 effective date and shown alongside, never substituted silently", "Medium", source("S4", "S10")),
        ("Wise matrix extrapolated historical examples", "Corrected: all current Wise cost cells are blank; the 2024 examples do not establish current prices or equal net payout at the requested amounts.", "High", source("S11", "S13")),
        ("MoneyGram $10,000 falls outside top published tier", "Schedule ends at $9,999.99; all rows at $10,000 and above are blank, and the dashboard no longer labels this a $10,000 tier", "Medium", source("S16")),
        ("Foreign-individual status may differ from intuition", "US citizenship, PRC documentation, account identity and residence facts must be reconciled by the bank", "High", source("S1", "S2")),
        ("Property-transfer rules changed in presentation over time", "Latest 2025 operating guide used for property sale; older general measures still cited for framework", "Medium", source("S21", "S2")),
        ("FX spread is an analytical benchmark", "Half-spread uses BOC’s own same-timestamp buy/sell midpoint; it is not proof of the bank’s profit or an executable mid-market rate", "Medium", source("S5", "S48")),
        ("DOMESTIC $50k/year model could be misused", "Shown solely as constant-rate arithmetic for independently lawful annual transactions; never borrow quotas or split to evade review", "High", source("S19", "S46")),
        ("US tax was described qualitatively but never quantified", "Added a 2026 single-filer illustration that prices the same amount by character (ordinary income, a 10% currency gain, FEIE-eligible earned income) from Rev. Proc. 2025-32; a measured FX gain stays blank because acquisition basis is a personal fact", "Medium", source("S53", "S38")),
        ("Crypto description was overbroad on old site", "Corrected to the PBOC notice’s actual prohibited business activities and legal-risk language; no blanket claim about every individual act is added", "Medium", source("S17")),
    ]
    body = f'''
{callout("warn", "Review before execution", "This page is part of the deliverable, not a merge blocker. Values below remain blank because they are not verified. Historical values are labeled and never silently promoted to current prices.")}
<section class="section"><div class="section-heading"><p class="eyebrow">A · Open items</p><h2>Unknown values and the exact manual check required</h2></div>{table(["Item", "Why it is unresolved", "Required verification", "Official starting point"], unresolved, "Institution- and person-specific unknowns. “—” elsewhere on the site refers to these items.")}</section>
<section class="section"><div class="section-heading"><p class="eyebrow">B · Audit findings</p><h2>Corrections and irregularities</h2></div>{table(["Finding", "Resolution / treatment", "Severity", "Primary evidence"], irregular, "Material errors found in the inherited pages were corrected rather than preserved for the sake of consistency.")}</section>
<section class="section"><h2>Verification policy</h2><div class="steps three"><div><span>1</span><h3>Primary evidence</h3><p>Regulator, statute, court/regulatory text, issuing bank or operator. Secondary travel/expat estimates are not used as facts.</p></div><div><span>2</span><h3>Date and scope</h3><p>Old tariffs remain only when labeled historical; future changes show their effective date; product availability is not inferred from branding.</p></div><div><span>3</span><h3>Blank means unknown</h3><p>No unconfirmed fee, tax, limit or route is backfilled. Conditional scenarios use disclosed inputs and reproducible formulas.</p></div></div></section>'''
    return layout("flagged.html", "Flagged for Review", "Unresolved institution-specific values, corrected legacy errors, timestamp conflicts, and the manual checks required before moving money.", body)


def sources_page():
    rows = []
    used = {
        "S1": "Foreign-individual lawful income, existing FX, reconversion and domestic quota",
        "S2": "Identity definitions, current/capital account framework and anti-evasion",
        "S3": "Current-account guide and outward-remittance evidence",
        "S4": "Wire/draft/ATM/permit prices, full-arrival and foreign-bank charges",
        "S5": "Dated USD buy/sell quotes used for every CNY/FX calculation (date query)",
        "S6": "BOC remittance channels and SWIFT instructions",
        "S7": "China foreign-currency cash permits and special-case ceiling",
        "S8": "Customs red/green channel clearance procedure (threshold values: S49, S50)",
        "S9": "ATM CNY 100,000/year and CNY 10,000/card/day caps",
        "S10": "Future Visa/Mastercard ATM fee effective 2026-11-11",
        "S11": "Wise eligibility, own-name recipient, funding routes and caps",
        "S12": "Wise passport, work eligibility and tax-record verification",
        "S13": "Dated bank 0.62% and Alipay 1.97% formulas plus CNY 33.20 fixed fee",
        "S14": "Western Union China outbound steps and partner channels",
        "S15": "Western Union fee/FX variability",
        "S16": "Historical MoneyGram fee tiers",
        "S17": "Virtual-currency restrictions",
        "S18": "Current State Council FX offenses and corrected penalty ranges",
        "S19": "Anti-splitting and watch-list consequences",
        "S20": "Emigration/inheritance eligibility, documents, approval and remittance staging",
        "S21": "2025 property sale/refund documentation and after-tax cap",
        "S22": "Foreign direct-investment exit route",
        "S23": "Hong Kong Payment Connect scope and currencies",
        "S24": "Licensed FX channels and private-changer warning",
        "S25": "FBAR trigger and due dates",
        "S26": "Current adjusted FBAR civil maxima",
        "S27": "All Form 8938 thresholds and FBAR distinction",
        "S28": "Foreign gift/bequest threshold and Form 3520 penalty",
        "S29": "US travel declaration guidance (the $10,000 rule itself is cited to S51)",
        "S30": "US bank physical-cash aggregation",
        "S31": "Trade/business Form 8300 scope",
        "S32": "Worldwide income and citizen-abroad framework",
        "S33": "FTC eligibility and no credit on excluded income",
        "S34": "FEIE eligibility tests",
        "S35": "2026 FEIE $132,900 maximum",
        "S36": "Streamlined offshore correction procedure",
        "S37": "Streamlined US-resident correction procedure",
        "S38": "Personal FX gain threshold and character",
        "S39": "China IIT residence, taxable income and rates",
        "S40": "China non-domicile and treaty calculation rules",
        "S41": "Treaty text and technical explanation",
        "S42": "BofA inbound wire example and waivers",
        "S43": "Chase Secure inbound wire example",
        "S44": "Capital One incoming fees and foreign-check context",
        "S45": "BOC consolidated price-list effective date and amendments",
        "S46": "Convenience quota is not a genuine current-account hard cap",
        "S47": "US tax FX translation principle and annual rates",
        "S48": "Live-board corroboration of the dated quote and half-spread",
        "S49": "RMB 20,000 per-trip cash limit",
        "S50": "Current customs declaration instrument (2025 No. 43)",
        "S51": "FinCEN Form 105 threshold and group aggregation",
        "S52": "FBAR aggregate-account threshold",
        "S53": "2026 brackets, standard deduction, capital-gain bands, FEIE and the §6039F threshold",
        "S54": "Seven annual comprehensive-income brackets and quick deductions",
    }
    for sid, (authority, title, url) in SOURCES.items():
        rows.append((f"<strong>{sid}</strong>", authority, f'<a href="{url}" target="_blank" rel="noopener noreferrer">{escape(title)}</a>', used[sid], f'<a class="source" href="{url}" target="_blank" rel="noopener noreferrer">Open primary ↗</a>'))
    body = f'''
{callout("info", "Evidence standard", "The register contains the primary pages used in the audit. Chinese-language rules are summarized conservatively in English. Bank/operator pages establish their own products and prices—not another institution’s terms. All external links open in a new tab for side-by-side manual review.")}
<section class="section"><div class="section-heading"><p class="eyebrow">{len(SOURCES)} primary documents</p><h2>Source register and exact use</h2></div>{table(["ID", "Issuer", "Document", "Used to verify", "Manual review"], rows, "Source IDs are stable across the generated pages. Retrieval/review cutoff: " + RESEARCH_DATE + ".")}</section>
<section class="section"><div class="section-heading"><p class="eyebrow">Reproducibility</p><h2>How to audit the calculations</h2></div><ol class="procedure"><li>Open <a href="https://github.com/sassnarep3-star/China4/blob/main/scripts/build_site.py"><code>scripts/build_site.py</code></a> and confirm the Decimal inputs BUY=6.6648, SELL=6.6929 and amount ladder $10,000…$400,000.</li><li>Run <code>python3 scripts/build_site.py</code>. It rebuilds the HTML and <code>data/cost-model.json</code> without network calls.</li><li>Compare BOC commission against the CNY 50 minimum and CNY 260 maximum; add CNY 150 telecom only to TT, not draft.</li><li>Verify the half-spread from BOC’s same-timestamp buy/sell midpoint. Do not substitute the PBOC fixing or a later mid-market quote.</li><li>Because BOC’s board rotates, re-query the dated quote through its official historical search (date 2026-11-09, currency USD, captcha) rather than expecting the row to remain on a page number.</li><li>Check current Wise quotes directly; no current price is inferred from its 2024 examples.</li><li>Confirm that ATM amounts above $10,000 are marked infeasible under the annual cap and that unknown values remain blank.</li></ol><p class="note">The dashboard intentionally does not fetch live prices during a visit. This prevents a stale static page from presenting new values without an audit trail.</p></section>'''
    return layout("sources.html", "Official sources and calculation audit", f"{len(SOURCES)}-document primary-source register with direct manual-review links and exact instructions for rebuilding every cost row.", body)


def main():
    pages = {
        "index.html": index_page(),
        "summary.html": summary_page(),
        "methods.html": methods_page(),
        "penalties.html": penalties_page(),
        "taxes.html": taxes_page(),
        "sources.html": sources_page(),
        "flagged.html": flagged_page(),
    }
    for filename, content in pages.items():
        (ROOT / filename).write_text(content, encoding="utf-8")
    for alias in ("estimates.html", "costs.html"):
        (ROOT / alias).write_text(f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="refresh" content="0; url=penalties.html"><link rel="canonical" href="penalties.html"><title>Consolidated cost matrices — China4</title></head>
<body><main><h1>Cost matrices have moved</h1><p>The provider and legal-route models are now consolidated in the <a href="penalties.html">audited cost matrices</a>.</p></main></body></html>''', encoding="utf-8")
    audit = {
        "research_cutoff_utc": RESEARCH_DATE,
        "summary_page_introduced_utc": "2026-11-10 UTC",
        "boc_quote_provenance": "USD 666.48 / 669.29 CNY per 100 USD captured from the official BOC board on 2026-11-09; the row has rolled off the five-quote board and BOC's date search requires a captcha. See flagged.html.",
        "boc_quote_timestamp_beijing": QUOTE_TIME,
        "inputs": {
            "boc_usd_cash_spot_buy_cny_per_usd": str(BUY),
            "boc_usd_cash_spot_sell_cny_per_usd": str(SELL),
            "internal_same_quote_midpoint": str(MID),
            "half_spread_fraction": str((SELL - MID) / MID),
            "wire_commission_fraction": "0.001",
            "wire_commission_min_cny": "50",
            "wire_commission_max_cny": "260",
            "telecom_us_cny": "150"
        },
        "wise_net_payout_caveat": "Current Wise price is unverified and omitted; Wise deducts fees before conversion, so quotes must be compared for the same net USD payout.",
        "exclusions": ["underlying tax", "unverified correspondent deductions", "recipient fees unless explicitly shown", "travel/professional costs", "live provider fees/rates", "unknown institution-specific values"],
        "rows": [{k: (str(v) if isinstance(v, D) else v) for k, v in row.items()} for row in COSTS],
    }
    (ROOT / "data").mkdir(exist_ok=True)
    (ROOT / "data" / "cost-model.json").write_text(json.dumps(audit, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Built {len(pages)} main pages, 2 compatibility redirects and {len(COSTS)} audited amount rows.")


if __name__ == "__main__":
    main()
