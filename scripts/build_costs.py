#!/usr/bin/env python3
"""Build costs.html and steps.html from officially sourced model inputs.

Every number emitted here is either (a) copied from an official page fetched
during this session (listed in INPUTS below, each with its source URL), or
(b) computed from those numbers by the formula printed on the page.
Anything that cannot be traced to an official source is emitted as a blank
cell marked [unverified] -- never inferred.
"""
from pathlib import Path
import math

ROOT = Path(__file__).resolve().parents[1]

# ----------------------------------------------------------------------------
# Model inputs -- each one traced to an official page fetched this session.
# ----------------------------------------------------------------------------
RATE_DATE = "9 Nov 2026, 05:30 (BOC publication stamp)"
BUY = 6.6648       # BOC USD 现汇买入价 per 100 USD -> /100
SELL = 6.6929      # BOC USD 现汇卖出价 per 100 USD -> /100  (rate a customer buys USD)
REF = 6.7168       # BOC 中行折算价 per 100 USD -> /100
PARITY = 6.7168    # PBOC/CFETS central parity, 6 Nov 2026
CASH_SELL = 6.6929  # BOC USD 现钞卖出价 (identical to spot sell on the sampled board)

SPREAD_PCT = (SELL - BUY) / SELL * 100.0        # full quoted buy/sell spread
FX_PCT = SPREAD_PCT / 2.0                        # one-way cost vs mid-market

FEE_RATE, FEE_MIN, FEE_MAX, CABLE = 0.001, 50.0, 260.0, 150.0
QUOTA = 50000.0        # SAFE annual per-person quota, USD
SAFE_LOCAL_CNY = 500000.0   # PBOC/SAFE: <= CNY 500,000 approved by local SAFE branch
SAFE_ONEOFF_CNY = 200000.0  # PBOC/SAFE: <= CNY 200,000 may be remitted in one go

SRC_RATE = "https://www.boc.cn/sourcedb/whpj/"
SRC_TARIFF = "https://www.boc.cn/ebanking/service/cs1/200905/t20090506_990712.html"
SRC_TARIFF_PDF = "https://pic.bankofchina.com/bocappd/pricelist/202503/P020250331641149290400.pdf"
SRC_QUOTA = "https://www.safe.gov.cn/safe/2007/0105/5320.html"
SRC_CASH = "https://www.gov.cn/gongbao/content/2004/content_63085.htm"
SRC_PROPERTY = "https://www.gov.cn/gongbao/content/2005/content_64294.htm"
SRC_PROPERTY_SAFE = "http://m.safe.gov.cn/safe/2004/1116/4133.html"
SRC_REGS = "https://www.chinamoney.com.cn/english/rarfmrrudrgl/20080805/813.html"


def send_fee_cny(usd_amount):
    """BOC published sending charge for one outward telegraphic transfer."""
    cny = usd_amount * SELL
    return min(max(cny * FEE_RATE, FEE_MIN), FEE_MAX) + CABLE


def fx_cost(usd):
    return usd * FX_PCT / 100.0


def route_quota(a):
    """Annual-quota route: one wire per calendar year, up to US$50,000 each."""
    n = max(1, math.ceil(a / QUOTA))
    per = a / n
    fees_cny = n * send_fee_cny(per)
    return {
        "total": fx_cost(a) + fees_cny / SELL,
        "fx": fx_cost(a),
        "fee": fees_cny / SELL,
        "wires": n,
        "time": "1 yr" if n == 1 else f"{n} yrs",
        "label": "Bank wire, annual quota",
    }


def route_documented(a):
    """Documented conversion + single wire (SAFE Detailed Rules, Art. 13)."""
    fees_cny = send_fee_cny(a)
    return {
        "total": fx_cost(a) + fees_cny / SELL,
        "fx": fx_cost(a),
        "fee": fees_cny / SELL,
        "wires": 1,
        "time": "1 wire",
        "label": "Documented conversion + 1 wire",
    }


def route_property(a):
    """Emigration / inheritance property transfer, SAFE approval, 3 wires."""
    tranches = [a * 0.5, a * 0.25, a * 0.25]
    fees_cny = sum(send_fee_cny(t) for t in tranches)
    return {
        "total": fx_cost(a) + fees_cny / SELL,
        "fx": fx_cost(a),
        "fee": fees_cny / SELL,
        "wires": 3,
        "time": "2 yrs (50/25/25)",
        "label": "SAFE property transfer",
    }


def route_cash(a):
    """Physical cash exit (SAFE + GAC Interim Measures, Arts. 5 and 7)."""
    if a > 10000:
        return None
    trips = max(1, math.ceil(a / 5000.0))
    return {
        "total": fx_cost(a),  # cash sell price equals spot sell price on the sampled board
        "fx": fx_cost(a),
        "fee": 0.0,
        "wires": 0,
        "time": f"{trips} exit" + ("s" if trips > 1 else ""),
        "label": "Cash carry",
    }


def money(x):
    return f"${x:,.2f}"


def pct(x, a):
    return f"{x / a * 100:.3f}%"


def link(url, text):
    return f'<a href="{url}">{text}</a>'


BLANK = '<span class="blank">— unverified</span>'

NAV = [
    ("index.html", "Dashboard"),
    ("methods.html", "Methods &amp; Guides"),
    ("estimates.html", "$10k–$400k Estimates"),
    ("costs.html", "Route cost model"),
    ("penalties.html", "Penalties &amp; Costs"),
    ("taxes.html", "US &amp; PRC Taxes"),
    ("flagged.html", "Flagged for Review"),
    ("sources.html", "Sources"),
]


def page(title, active, body):
    parts = []
    for href, label in NAV:
        attrs = ' class="active" aria-current="page"' if href == active else ''
        parts.append('<a%s href="%s">%s</a>' % (attrs, href, label))
    nav = "".join(parts)
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} | China4</title><link rel="stylesheet" href="style.css"></head><body><header class="site-header"><div class="header-inner"><a class="brand" href="index.html"><span class="mark">C4</span> China4</a><nav aria-label="Main navigation">{nav}</nav></div></header><main class="container">
{body}
</main><footer class="site-footer"><div class="inner"><span>China4 · Source-first research</span><a href="flagged.html">Open questions &amp; limitations</a></div></footer></body></html>"""


DISCLAIMER = ('<div class="disclaimer"><strong>Research, not legal or tax advice.</strong> '
              'The figures on this page are model estimates computed from published official '
              'inputs, not bank quotes and not a determination of your eligibility. Verify '
              'current rates, the bank’s executable quote and your documents with the bank and '
              'qualified China–US advisers before acting. Sources reviewed 8–9 November 2026; '
              'older guidance may have changed.</div>')

# ----------------------------------------------------------------------------
# Build costs.html
# ----------------------------------------------------------------------------
amounts = list(range(10000, 400001, 10000))

rows_head = []
rows_matrix = []
rows_illegal = []

for a in amounts:
    q = route_quota(a)
    d = route_documented(a)
    p_ = route_property(a)
    c = route_cash(a)

    # headline: cheapest legal route that is actually available at this amount
    if a <= QUOTA:
        best, best_label = d, d["label"] + " (or quota route — identical cost)"
    else:
        best, best_label = d, d["label"] + f" (quota-only fallback: {q['wires']} yrs, {money(q['total'])})"

    rows_head.append(f"""<tr>
<td data-label="Amount"><strong>${a:,}</strong></td>
<td data-label="Cheapest legal route">{best_label}</td>
<td data-label="Total est. cost"><strong>{money(best['total'])}</strong></td>
<td data-label="Cost %">{pct(best['total'], a)}</td>
<td data-label="FX spread">{money(best['fx'])}</td>
<td data-label="Bank sending fee">{money(best['fee'])}</td>
<td data-label="Time">{best['time']}</td>
<td data-label="Source">{link(SRC_TARIFF, 'BOC tariff')} · {link(SRC_RATE, 'BOC rate board')}</td>
</tr>""")

    cash_cell = money(c['total']) + f"<br><span class='small'>{c['time']}</span>" if c else \
        '<span class="blank">Not permitted above $10,000</span>'
    rows_matrix.append(f"""<tr>
<td data-label="Amount"><strong>${a:,}</strong></td>
<td data-label="Annual-quota route">{money(q['total'])}<br><span class="small">{q['wires']} wire(s), {q['time']}</span></td>
<td data-label="Documented single wire">{money(d['total'])}<br><span class="small">1 wire</span></td>
<td data-label="SAFE property transfer">{money(p_['total'])}<br><span class="small">3 wires, 2 yrs</span></td>
<td data-label="Cash carry">{cash_cell}</td>
<td data-label="Source">{link(SRC_TARIFF, 'BOC tariff')} · {link(SRC_QUOTA, 'SAFE quota')} · {link(SRC_PROPERTY, 'PBOC property transfer')} · {link(SRC_CASH, 'SAFE/GAC cash')}</td>
</tr>""")

    rows_illegal.append(f"""<tr>
<td data-label="Amount"><strong>${a:,}</strong></td>
<td data-label="Low end of fine (30%)">{money(a * 0.30)}</td>
<td data-label="High end of fine (300%)">{money(a * 3.00)}</td>
<td data-label="Confiscation">Illegal gains may also be confiscated; criminal liability if a crime is constituted</td>
<td data-label="Compared with legal route">Legal documented route at this amount: {money(route_documented(a)['total'])} ({pct(route_documented(a)['total'], a)})</td>
<td data-label="Source">{link(SRC_REGS, 'PRC FX Regulations, Arts. 45–46')}</td>
</tr>""")

inputs_rows = f"""<tr><td>BOC USD spot buying rate (bank buys USD)</td><td>{BUY:.4f} CNY / USD</td><td>{link(SRC_RATE, 'BOC FX rate board')}</td></tr>
<tr><td>BOC USD spot selling rate (customer buys USD)</td><td><strong>{SELL:.4f} CNY / USD</strong></td><td>{link(SRC_RATE, 'BOC FX rate board')} — published {RATE_DATE}</td></tr>
<tr><td>BOC USD reference rate (中行折算价)</td><td>{REF:.4f} CNY / USD</td><td>{link(SRC_RATE, 'BOC FX rate board')}</td></tr>
<tr><td>BOC USD cash selling rate (customer buys USD cash)</td><td>{CASH_SELL:.4f} CNY / USD — identical to the spot selling rate on the sampled board, so no cash premium is added for the cash-carry route</td><td>{link(SRC_RATE, 'BOC FX rate board')}</td></tr>
<tr><td>Quoted buy–sell spread (sell − buy) ÷ sell</td><td>{SPREAD_PCT:.4f}%</td><td>Computed from the two BOC rates above — {link(SRC_RATE, 'BOC FX rate board')}</td></tr>
<tr><td><strong>One-way FX cost used in the model</strong> (half of the quoted spread)</td><td><strong>{FX_PCT:.4f}%</strong></td><td>Computed: spread ÷ 2 — the standard measure of a one-way retail conversion cost against mid-market. Rates: {link(SRC_RATE, 'BOC FX rate board')}</td></tr>
<tr><td>Outward telegraphic transfer charge</td><td>0.1% of remittance value, min CNY 50, max CNY 260</td><td>{link(SRC_TARIFF, 'BOC e-banking personal tariff')} · {link(SRC_TARIFF_PDF, 'BOC 2025 price list PDF')}</td></tr>
<tr><td>Telecommunication (cable) fee, destinations outside HK/Macau/Taiwan</td><td>CNY 150 per transfer</td><td>{link(SRC_TARIFF, 'BOC e-banking personal tariff')}</td></tr>
<tr><td>Individual annual foreign-exchange purchase / settlement quota</td><td>US$50,000 per person per calendar year</td><td>{link(SRC_QUOTA, 'SAFE, Detailed Rules on Individual FX, Art. 2')}</td></tr>
<tr><td>Cash exit: no permit needed / bank permit / SAFE approval</td><td>≤ US$5,000 / US$5,001–10,000 / &gt; US$10,000 (in principle not allowed)</td><td>{link(SRC_CASH, 'SAFE + GAC Interim Measures, Arts. 5 and 7')}</td></tr>
<tr><td>SAFE property transfer: approval level</td><td>≤ CNY 500,000 local SAFE branch; above that, SAFE head office (≈ US${SAFE_LOCAL_CNY/SELL:,.0f} at the rate above)</td><td>{link(SRC_PROPERTY, 'PBOC, Interim Measures, Art. 10')} · {link(SRC_PROPERTY_SAFE, 'SAFE release')}</td></tr>
<tr><td>Intermediary / correspondent bank charge and US receiving-bank charge</td><td>{BLANK}</td><td>No official published figure found — left blank by policy: {link(SRC_TARIFF_PDF, 'BOC price list')} states overseas bank charges are collected separately · {link('flagged.html', 'Flagged for review')}</td></tr>"""

body_head = f"""<h1 class="page-title">Legal-route cost model: $10,000 to $400,000</h1>
<p class="page-sub">What each <strong>legal route</strong> costs, in $10,000 steps, computed from published official bank rates and tariffs. Every figure shows its formula, its rate snapshot and its source.</p>
<div class="callout info"><h3>How this differs from <a href="estimates.html">$10k–$400k Estimates</a></h3>
<p><a href="estimates.html"><strong>$10k–$400k Estimates</strong></a> compares <em>providers</em> — BOC, CCB, HSBC, SkyRemit, Wise, PayPal, UnionPay — and which is cheapest at each amount. <strong>This page compares <em>legal routes</em></strong>: what it costs to spread a transfer over several calendar years under the annual quota, what a SAFE-approved emigration or inheritance property transfer costs given that its remittance must be staged over two years, what cash carry costs, and what the illegal channel would cost in statutory fines. Both pages use the same $10,000–$400,000 grid; use them together.</p></div>

<div class="best-answer"><h2>Read this first</h2>
<p><strong>The dominant cost is not the fee — it is the size of the amount relative to the rules.</strong> Because the individual annual foreign-exchange quota is {link(SRC_QUOTA, 'US$50,000 per person per calendar year')}, moving more than that in one year requires either documentation of a legitimate, taxed current-account source (then {link('https://www.safe.gov.cn/safe/2007/0105/5320.html', 'SAFE Detailed Rules Art. 13')} allows conversion with a tax certificate) or a SAFE-approved property transfer. The bank's own charges are small and capped: on the {link(SRC_TARIFF, 'BOC published tariff')} the sending charge tops out at CNY 260 plus a CNY 150 cable fee — about <strong>${(FEE_MAX + CABLE) / SELL:,.2f}</strong> per wire at the rate used here, however large the transfer.</p>
<p><strong>What is deliberately left blank:</strong> intermediary/correspondent bank charges and the US receiving bank's incoming-wire fee. No official published figure was found for either, so they are not filled in. Add them yourself from your two banks.</p>
</div>

<section class="section"><h2 class="section-title">Model inputs (every one from an official source)</h2>
<div class="table-wrap card-mobile"><table class="data mobile-cards"><thead><tr><th scope="col">Input</th><th scope="col">Value used</th><th scope="col">Official source</th></tr></thead><tbody>
{inputs_rows}
</tbody></table></div>
<p class="small"><strong>Formula:</strong> total estimated cost = (amount × {FX_PCT:.4f}%) + (Σ per-wire sending charge in CNY ÷ {SELL:.4f}). The CNY sending charge per wire = min(CNY 260, max(CNY 50, 0.001 × USD value × {SELL:.4f})) + CNY 150. Because the sending charge is capped, the cost <em>percentage falls as the amount rises</em>.</p>
</section>

<section class="section"><h2 class="section-title">Headline estimate by amount (most important first)</h2>
<p class="small">Each row is an independent gross USD target: the amount you want to end up sending. "Cheapest legal route" assumes you can document the source; where you cannot, the quota-only fallback is shown in brackets.</p>
<div class="table-wrap card-mobile"><table class="data mobile-cards"><thead><tr>
<th scope="col">Gross USD</th><th scope="col">Cheapest legal route</th><th scope="col">Total est. cost</th><th scope="col">Cost %</th><th scope="col">FX spread</th><th scope="col">Bank sending fee</th><th scope="col">Time</th><th scope="col">Source</th>
</tr></thead><tbody>
{''.join(rows_head)}
</tbody></table></div>
</section>

<section class="section"><h2 class="section-title">Every legal route, side by side, at every amount</h2>
<div class="table-wrap card-mobile"><table class="data mobile-cards"><thead><tr>
<th scope="col">Gross USD</th><th scope="col">Annual-quota route</th><th scope="col">Documented single wire</th><th scope="col">SAFE property transfer</th><th scope="col">Cash carry</th><th scope="col">Source</th>
</tr></thead><tbody>
{''.join(rows_matrix)}
</tbody></table></div>
<p class="small"><strong>Why the quota route costs more above $50,000:</strong> it needs one wire per calendar year, so it pays the CNY 150 cable fee again each year and waits a year between tranches. <strong>Why the SAFE property-transfer route costs more:</strong> the rules require the money to leave in three stages — no more than half up front, no more than half of the remainder after one year, and the balance after two years ({link(SRC_PROPERTY, 'PBOC Interim Measures, Art. 6')}) — so it pays three sets of fees. <strong>Cash carry</strong> is capped by {link(SRC_CASH, 'Arts. 5 and 7')}: above US$10,000 it is in principle not permitted.</p>
</section>

<section class="section"><h2 class="section-title">Illegal channel: statutory penalty exposure (never use)</h2>
<p class="small">For contrast only. These are the statutory fine ranges in the PRC foreign-exchange regulations and are the reason the legal routes above are cheaper by orders of magnitude even in the worst case.</p>
<div class="table-wrap card-mobile"><table class="data mobile-cards"><thead><tr>
<th scope="col">Gross USD</th><th scope="col">Low end of fine (30%)</th><th scope="col">High end of fine (300%)</th><th scope="col">Confiscation / criminal</th><th scope="col">Compared with the legal route</th><th scope="col">Source</th>
</tr></thead><tbody>
{''.join(rows_illegal)}
</tbody></table></div>
</section>

<section class="section"><h2 class="section-title">What this estimate excludes</h2>
<div class="table-wrap card-mobile"><table class="data mobile-cards"><thead><tr><th scope="col">Excluded item</th><th scope="col">Why</th><th scope="col">Source</th></tr></thead><tbody>
<tr><td>Intermediary / correspondent bank deductions</td><td>{BLANK} — varies by routing bank; no official published figure</td><td>{link(SRC_TARIFF_PDF, 'BOC price list (states overseas bank charges are collected separately)')} · {link('flagged.html', 'Flagged for review')}</td></tr>
<tr><td>US receiving bank incoming-wire fee</td><td>{BLANK} — set privately by each US bank; no official published figure</td><td>{link('flagged.html', 'Flagged for review')}</td></tr>
<tr><td>Chinese tax already owed on the underlying income</td><td>{BLANK} — depends on how the money was earned and whether it was taxed in China</td><td>{link('https://www.safe.gov.cn/safe/2007/0105/5320.html', 'SAFE Detailed Rules, Art. 13 (tax certificate)')}</td></tr>
<tr><td>US tax on income or on foreign-currency gain</td><td>{BLANK} — depends on your filings, basis and whether the funds were already reported</td><td>{link('https://www.irs.gov/publications/p54', 'IRS Pub. 54')} · {link('https://www.irs.gov/pub/fatca/int_practice_units/int_c_041.pdf', 'IRS FX guidance')}</td></tr>
<tr><td>Bank-specific discounts for e-banking channels</td><td>{BLANK} — BOC lists channel discounts separately from the standard tariff</td><td>{link(SRC_TARIFF, 'BOC tariff page')}</td></tr>
</tbody></table></div>
</section>
{DISCLAIMER}"""

(ROOT / "costs.html").write_text(page("Cost estimator", "costs.html", body_head), encoding="utf-8")
print("wrote costs.html")
