#!/usr/bin/env python3
"""Build the tax-gate page: what actually creates a tax or a documentation
block when CNY becomes USD.

Every figure below is either (a) quoted from an official page fetched in this
session, or (b) arithmetic on a quoted statutory rate, labelled as a
hypothetical. Nothing personal is assessed.
"""
from decimal import Decimal as D
from pathlib import Path
import json
from build_site import ROOT, layout, table, source

# --- Official sources read in this session (2026-11-11 UTC) -----------------
IIT = 'https://fgk.chinatax.gov.cn/zcfgk/c100009/c5193028/content.html'
TCA = 'https://fgk.chinatax.gov.cn/zcfgk/c100009/c5195081/content.html'
RULES = 'https://www.safe.gov.cn/tianjin/2024/0430/2464.html'
FILING40 = 'https://fgk.chinatax.gov.cn/zcfgk/c100012/c5194375/content.html'
FILING19 = 'https://www.safe.gov.cn/safe/2021/0702/19306.html'
FXREG = 'https://www.gov.cn/gongbao/content/2008/content_1071846.htm'
CASH = 'https://www.safe.gov.cn/tianjin/2024/0430/2466.html'
ECFR821 = 'https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010/subpart-H/section-1010.821'
FBARCMP = 'https://www.irs.gov/businesses/comparison-of-form-8938-and-fbar-requirements'
FTC = 'https://www.irs.gov/individuals/international-taxpayers/foreign-tax-credit'
PUB54 = 'https://www.irs.gov/publications/p54'
F8802 = 'https://www.irs.gov/individuals/international-taxpayers/form-8802-application-for-united-states-residency-certification-user-fee-fact-sheet'
TREATY = 'https://www.irs.gov/pub/irs-trty/china.pdf'
PROPERTY = 'https://www.gov.cn/gongbao/content/2005/content_64294.htm'
SPLIT = 'https://www.safe.gov.cn/safe/2015/1231/5442.html'

RATE = D('6.6929')          # historical BOC selling rate, same basis as the published models
AMOUNTS = [D(n * 10000) for n in range(1, 41)]


def link(url, text):
    return f'<a class="source" href="{url}" target="_blank" rel="noopener noreferrer">{text}</a>'


def usd(x):
    return f'${x:,.0f}'


def pct(x):
    return f'${x:,.0f}'


def build_rows():
    rows = []
    for amount in AMOUNTS:
        tax20 = amount * D('0.20')
        tax45 = amount * D('0.45')
        late30 = tax20 * D('0.0005') * D('30')
        rows.append({
            'amount_usd': str(amount),
            'prc_tax_20pct_usd': str(tax20),
            'prc_tax_45pct_usd': str(tax45),
            'prc_late_fee_30d_usd': str(late30),
        })
    return rows


def main():
    rows = build_rows()
    data = {
        'as_of': '2026-11-11',
        'historical_cny_per_usd': str(RATE),
        'rate_note': ('The PRC rates are applied to the USD amount after converting at the '
                      'historical 6.6929 CNY/USD BOC selling rate, so a 20% rate on CNY income '
                      'equals 20% of the USD equivalent at that rate. Not a current quote.'),
        'statutory_rates': {
            'comprehensive_3_45': '0.03-0.45',
            'business_5_35': '0.05-0.35',
            'flat_20': '0.20',
            'late_fee_per_day': '0.0005',
            'evasion_fine_range': '0.50-5.00',
        },
        'rows': rows,
    }
    (ROOT / 'data/taxgate.json').write_text(json.dumps(data, indent=2) + '\n')

    # --- 1. Framing ---------------------------------------------------------
    body = ('<p><a href="taxes.html">Tax overview →</a> · <a href="treaty-filings.html">Treaty and '
            'filing playbook</a> · <a href="questions.html">Before-you-decide checklist</a> · '
            '<a href="penalties.html">Cost matrices</a></p>')
    body += ('<div class="callout warning"><strong>Read this before any cost table.</strong> '
             'No provision imposing a tax on the act of exchanging CNY for USD was found in the '
             'texts reviewed here (Individual Income Tax Law Art. 2 lists nine taxable income '
             'categories and none is a currency exchange; the FX regulations govern permission '
             'and documentation, not a conversion levy). The money that hurts is (1) PRC income '
             'tax that was never paid on the income behind the balance, (2) PRC late-payment '
             'surcharge and fines on that unpaid tax, (3) US income tax on the same income, and '
             '(4) US information-return penalties. A limited negative finding is not a legal '
             'opinion — see the review limits below. ' + link(IIT, 'IIT Law Art. 2') + ' ' +
             link(FXREG, 'FX Regulations') + '</div>')

    # --- 2. Where the cost actually sits ------------------------------------
    body += '<h2>The four costs that get called “tax on the conversion”</h2>'
    layers = [
        ['PRC income tax on the source of the balance',
         'Charged when the income arises, not when it is converted. Rates depend on the income '
         'category; see the table below.',
         'Paid or unpaid', link(IIT, 'IIT Law Arts. 2–3, 6')],
        ['PRC documentation / tax-clearance gate at the bank',
         'The bank checks identity and purpose. For a foreign individual purchasing FX from '
         'lawful current-account RMB income, the required supporting documents expressly include '
         'tax vouchers. This is an evidence requirement; it does not by itself create a new tax.',
         'Blocks the purchase, not the tax', link(RULES, 'Detailed Rules Art. 13(1)')],
        ['US income tax on the same income',
         'A US citizen is taxed on worldwide income whether or not the money enters the US. '
         'Foreign tax paid may be creditable, subject to limits; a credit is not an exemption.',
         'Applies regardless of transfer', link(PUB54, 'IRS Pub. 54') + ' ' + link(FTC, 'IRS FTC')],
        ['US information returns and their penalties',
         'FBAR is required when foreign accounts exceed USD 10,000 in aggregate at any time in '
         'the calendar year; Form 8938 thresholds are separate. The current non-willful FBAR '
         'maximum is USD 16,536 per violation for assessments on or after 2025-01-17.',
         'Punishes non-disclosure, not conversion',
         link(FBARCMP, 'IRS 8938/FBAR comparison') + ' ' + link(ECFR821, '31 CFR 1010.821')],
    ]
    body += table(['Layer', 'When it is charged', 'Effect on a transfer', 'Primary source'],
                  layers, 'The four costs commonly bundled as a “conversion tax”')

    # --- 3. China tax by source of funds ------------------------------------
    body += ('<h2>China individual income tax by source of the balance</h2>'
             '<p>Statutory rates as written in the IIT Law. Which category a balance falls into is '
             'a factual question about how it was earned, and can change the answer by tens of '
             'percentage points. No value is assigned to your balance here.</p>')
    bysource = [
        ['Salary / wages from a PRC employer (comprehensive income)',
         'Annual progressive rate after the CNY 60,000 basic deduction and allowed deductions; '
         'normally withheld monthly by the employer as withholding agent.',
         '3% – 45%', link(IIT, 'Art. 3(1), Art. 6(1), Art. 9')],
        ['Interest, dividends, bonuses',
         'Flat proportional rate on the amount received, no expense deduction.',
         '20%', link(IIT, 'Art. 3(3), Art. 6(6)')],
        ['Gain on sale of property',
         'Flat rate on proceeds minus original cost and reasonable expenses.',
         '20%', link(IIT, 'Art. 3(3), Art. 6(5)')],
        ['Rental income from property',
         'Flat rate after a fixed deduction (CNY 800 if rent is CNY 4,000 or less, otherwise 20%).',
         '20%', link(IIT, 'Art. 3(3), Art. 6(4)')],
        ['Business / self-employment income',
         'Annual progressive rate on revenue less costs, expenses and losses.',
         '5% – 35%', link(IIT, 'Art. 3(2), Art. 6(3)')],
        ['Contingent income (for example certain windfalls)',
         'Flat proportional rate on the amount received. Whether a gift or inheritance falls in '
         'this category depends on the facts; confirm before relying on it.',
         '20%', link(IIT, 'Art. 3(3), Art. 2(9)')],
        ['Appreciation of the CNY against the USD while the balance is held',
         'No currency-exchange category appears among the nine taxable categories. A PRC rule '
         'taxing an individual’s FX gain was not located in this review. The US treats such a '
         'gain separately — see taxes.html and flagged.html.',
         '— (PRC, not located)', link(IIT, 'IIT Law Art. 2 (scope of review)')],
        ['Tax already withheld and paid by an employer',
         'Withholding by the payer is the statutory mechanism; a taxpayer without a withholding '
         'agent must self-file, and residents must settle annually.',
         'Already paid', link(IIT, 'Art. 9, Art. 10, Art. 13')],
    ]
    body += table(['What the balance is', 'PRC treatment', 'Statutory rate', 'Source'],
                  bysource, 'China IIT rates by income character')

    # --- 4. Documentation gate ---------------------------------------------
    body += ('<h2>What the bank will actually demand</h2>'
             '<p>The annual USD 50,000 convenience total covers settlement by all individuals and '
             'purchase by <em>domestic</em> individuals. A foreign individual is not inside that '
             'purchase quota; the route is the documented current-account purchase, which '
             'requires amount-linked documents including tax vouchers.</p>')
    gates = [
        ['Domestic individual · purchase within the annual total',
         'Valid identity document at the bank; entry into the individual FX system.',
         'No tax voucher stated', link(RULES, 'Detailed Rules Art. 2')],
        ['Domestic individual · purchase above the annual total',
         'Valid identity document plus documents evidencing the transaction amount.',
         'Amount-linked documents', link(RULES, 'Detailed Rules Art. 12')],
        ['Foreign individual · purchase from lawful PRC current-account income',
         'Valid identity document plus amount-linked supporting documents “including tax '
         'vouchers” (含税务凭证). This is the gate that blocks an untaxed balance.',
         'Tax vouchers expressly required', link(RULES, 'Detailed Rules Art. 13(1)')],
        ['Either identity · remitting existing FX abroad for current-account use',
         'Domestic individual: up to USD 50,000 equivalent per day from an FX savings account on '
         'ID; above that, authenticity documents. Foreign individual: ID for remittance from an '
         'FX savings account.',
         'Documentation, not a new tax', link(RULES, 'Detailed Rules Arts. 14–15')],
        ['Single outbound payment of USD 50,000 or more for service trade, income or current '
         'transfers',
         'Tax filing record (备案) with the tax authority before the bank processes payment, '
         'subject to the listed exemptions, which include an individual’s private use such as '
         'study, travel and visiting relatives.',
         'Filing record', link(FILING40, '2013 No. 40 Art. 1, Art. 3(13)') + ' ' +
         link(FILING19, '2021 No. 19')],
        ['Emigrating domestic individual moving pre-emigration property abroad',
         'Governed by the personal-property transfer rules, with identity, settlement, source and '
         'title documents and tax-payment evidence; the bank remits directly to the applicant’s '
         'own overseas account.',
         'Tax evidence + approval', link(PROPERTY, 'PBOC property-transfer rules') + ' ' +
         link(RULES, 'Detailed Rules Art. 20')],
        ['Foreign-currency cash out of China',
         'Up to USD 5,000 equivalent needs no carrying permit; USD 5,000–10,000 needs a bank '
         'permit; above USD 10,000 is not permitted in principle except for listed special cases '
         'with a SAFE permit. Withdrawing FX cash above USD 10,000 domestically requires prior '
         'SAFE registration.',
         'Permit regime', link(CASH, 'Hui Fa [2003] No. 102') + ' ' +
         link(RULES, 'Detailed Rules Art. 30')],
    ]
    body += table(['Identity and channel', 'Documentation', 'Tax evidence', 'Source'],
                  gates, 'Documentation gate by identity and channel')

    # --- 5. Penalty arithmetic ---------------------------------------------
    body += ('<h2>If the PRC tax was never paid: surcharge and fine</h2>'
             '<p>Unpaid tax carries a daily surcharge of 0.05% of the overdue tax from the day it '
             'became overdue. A failure to file can also attract a fine of 50% to five times the '
             'unpaid tax where the conduct is treated as evasion or non-filing; administrative '
             'penalties are barred if the conduct was not discovered within five years. These are '
             'statutory maxima and ranges, not predictions. ' + link(TCA, 'Tax Collection and '
             'Administration Law Arts. 32, 62–64, 86') + '</p>')
    prows = [[usd(D(r['amount_usd'])), pct(D(r['prc_tax_20pct_usd'])),
              pct(D(r['prc_tax_45pct_usd'])), pct(D(r['prc_late_fee_30d_usd'])),
              link(IIT, 'Art. 3') + ' ' + link(TCA, 'Art. 32')] for r in rows]
    body += table(['USD equivalent of the balance', 'PRC tax if the whole balance were untaxed '
                   'income at 20%', 'Same at the top 45% marginal rate', 'Surcharge on the 20% '
                   'figure after 30 days (0.05%/day)', 'Sources'],
                  prows, 'Hypothetical PRC tax at statutory rates · $10,000 increments')

    body += ('<div class="callout info"><strong>How to read that table.</strong> Both columns '
             'assume the entire balance is untaxed income of a single character, which is almost '
             'never true; salary is taxed progressively and the first CNY 60,000 is deducted, and '
             'property tax is charged on the gain, not the price. The columns exist to show the '
             'size of the exposure and why establishing that tax was already paid is worth more '
             'than any bank-fee optimisation on this site.</div>')

    # --- 6. US side ---------------------------------------------------------
    body += ('<h2>The US side does not go away by leaving the money in China</h2>')
    us = [
        ['Worldwide income', 'A US citizen reports worldwide income whether or not funds are '
         'transferred. The transfer is not the taxable event; earning the income was.',
         link(PUB54, 'IRS Pub. 54')],
        ['Foreign tax credit', 'PRC tax paid on the same income can be credited against US tax on '
         'that income, subject to the limitation and to the requirement that the foreign charge '
         'be a compulsory payment. Excess PRC withholding is not automatically creditable.',
         link(FTC, 'IRS FTC')],
        ['Treaty relief', 'The US–China treaty can reduce PRC withholding on specified income, '
         'claimed with Form 6166 obtained through Form 8802 (individual user fee USD 105 for '
         'applications postmarked on or after 2026-10-01), plus PRC procedures.',
         link(TREATY, 'Treaty') + ' ' + link(F8802, 'IRS fee fact sheet')],
        ['FBAR', 'Aggregate foreign accounts above USD 10,000 at any time in the calendar year '
         'must be reported; the current non-willful maximum is USD 16,536 per violation for '
         'assessments on or after 2025-01-17.',
         link(FBARCMP, 'IRS comparison') + ' ' + link(ECFR821, '31 CFR 1010.821')],
        ['Form 8938', 'Separate thresholds apply and differ by filing status and residence; the '
         'figures on the IRS comparison page are the published base amounts.',
         link(FBARCMP, 'IRS comparison')],
    ]
    body += table(['US obligation', 'As published', 'Source'], us, 'US reporting and credit map')

    # --- 7. Order of operations --------------------------------------------
    body += ('<h2>The order that minimises total cost</h2>'
             '<p>Sequence matters more than route choice: paying PRC tax late adds 0.05% a day, '
             'and an information-return penalty can exceed every bank fee on this site combined.'
             '</p>')
    steps = [
        ['1', 'Fix the identity first',
         'The bank will treat you as a domestic or foreign individual. The two follow different '
         'purchase rules, and the foreign-individual route is the one that requires tax vouchers. '
         'Get the classification in writing before pricing anything.',
         link(RULES, 'Art. 2, Art. 13')],
        ['2', 'Label every tranche of the balance',
         'Salary, bonus, property proceeds, interest, gifts and company money have different '
         'rates and different documents. Do not relabel one as another.',
         link(IIT, 'Art. 2')],
        ['3', 'Prove the PRC tax position, or settle it',
         'Pull withholding records or the individual income tax app history. If tax is owed, '
         'paying it stops the 0.05% daily surcharge and is the document the bank will ask for.',
         link(TCA, 'Art. 32') + ' ' + link(RULES, 'Art. 13(1)')],
        ['4', 'Check the treaty position before withholding',
         'If PRC withholding will exceed the treaty cap, the certificate route can reduce it at '
         'source; recovering it afterwards is slower and may not be creditable in the US.',
         link(F8802, 'Form 8802 / 6166') + ' ' + link(TREATY, 'Treaty')],
        ['5', 'Come current on US information returns first',
         'FBAR and Form 8938 history should be reviewed before moving a large balance, because '
         'the transfer itself can draw attention to an unfiled history.',
         link(FBARCMP, 'FBAR / 8938')],
        ['6', 'Then choose the transfer channel',
         'With clean documents, the cheapest channel is a normal bank wire or a documented '
         'provider route. See the 40-row matrices; no current live quote is verified there.',
         link('penalties.html', 'Cost matrices') + ' ' + link('method-matrix.html', 'Tariff matrix') +
         ' ' + link(RULES, 'Detailed Rules Art. 14')],
        ['7', 'Do not split to dodge the quota',
         'Splitting, borrowed quotas and “underground banks” are named enforcement targets, and '
         'the FX Regulations allow a fine of up to 30% of the amount, rising to 30%–100% in '
         'serious cases. That is larger than any tax saving described here.',
         link(SPLIT, 'Hui Fa [2015] No. 49') + ' ' + link(FXREG, 'Art. 39, Art. 45')],
        ['8', 'Keep the file',
         'Retain tax receipts, bank approvals, rate confirmations and US filings; both the PRC '
         'bank and the IRS can ask for them later.',
         link(RULES, 'Art. 36') + ' ' +
         link('verification.html', 'Verification ledger')],
    ]
    body += table(['#', 'Step', 'Why', 'Source'], steps, 'Sequential order of operations')

    # --- 8. Review limits ---------------------------------------------------
    body += ('<h2>What this page does not establish</h2><ul>'
             '<li>The absence of a PRC conversion tax is a <strong>limited negative finding</strong> '
             'across the IIT Law, the FX Regulations and the individual FX rules reviewed here. It '
             'is not a legal opinion and it does not cover local practice, provincial guidance or '
             'rules outside those texts. ' + link(IIT, 'IIT Law') + ' ' + link(FXREG, 'FX Regulations') +
             '</li>'
             '<li>No personal tax rate, residency status, deduction or treaty eligibility is '
             'assumed. Whether you are a PRC resident individual (domicile or 183 days) changes '
             'the answer. ' + link(IIT, 'Art. 1') + '</li>'
             '<li>Current bank and provider prices are not verified anywhere on this site; the '
             'tables use a historical FX snapshot to size amounts only. See '
             '<a href="flagged.html">Flagged for Review</a>.</li>'
             '<li>US state tax, exit tax, gift and estate consequences and PRC social insurance are '
             'outside this page.</li>'
             '<li>The 20% and 45% columns are hypothetical arithmetic on statutory rates, not an '
             'estimate of your liability.</li></ul>')
    body += ('<p>Row-by-row verification for this page is recorded on '
             '<a href="verification.html">Verification</a>; the build is reproducible with '
             '<code>python3 scripts/build_taxgate.py</code> from <code>data/taxgate.json</code>.</p>')

    (ROOT / 'taxgate.html').write_text(
        layout('taxgate.html', 'Tax gate',
               'What actually costs tax when CNY becomes USD — and in what order to fix it.',
               body))
    print('Built taxgate.html and data/taxgate.json')


if __name__ == '__main__':
    main()
