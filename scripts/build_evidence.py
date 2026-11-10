#!/usr/bin/env python3
"""Strict evidence brief: never manufacture a quote from historical FX inputs."""
from build_site import ROOT, layout, table, source, callout

SAFE='https://www.safe.gov.cn/tianjin/2024/0430/2464.html'
PBOC='https://www.safe.gov.cn/tianjin/2024/0430/2465.html'
FTC='https://www.irs.gov/individuals/international-taxpayers/foreign-tax-credit'
WORLD='https://www.irs.gov/individuals/international-taxpayers/us-citizens-and-resident-aliens-abroad'
PR='https://www.safe.gov.cn/en/2017/1129/1365.html'
def link(url, label):
    return f'<a class="source" href="{url}" rel="noopener noreferrer">{label}</a>'

# These eight statements were independently read against the linked official text
# on 2026-11-10. Provider terms are not legislation or personalized approval.
rules=[
('First route to investigate', 'For a passport-classified foreign individual with lawful current-account CNY income: documented bank FX purchase and remittance. This is a conditional recommendation, not proof it is cheapest for this account.', 'SAFE Detailed Rules Art. 13(1); Measures Art. 13', link(SAFE,'SAFE Art. 13')),
('Not a universal $50,000 ceiling', 'The annual $50,000 rule applies to settlement and domestic-individual purchases; foreign-national lawful current-account income has the document-based pathway. Permanent resident ID holders have a separately stated $50,000 convenience quota.', 'Detailed Rules Art. 2 and 13; 2017 permanent-resident circular', link(SAFE,'SAFE rules')+' '+link(PR,'Permanent-resident exception')),
('Tax evidence versus a new tax', 'SAFE requires amount-based supporting documents including tax evidence for the foreign-individual income purchase. This requirement alone does not establish that the conversion itself incurs a tax or a penalty.', 'Art. 13(1): 含税务凭证 (including tax vouchers)', link(SAFE,'Exact text')),
('US taxes follow income, not the dashboard amount', 'US citizens are generally subject to US tax on worldwide income. The transfer amount alone cannot establish taxable income, gain, deductions, credits, or the tax owed. No zero-tax assurance is made.', 'IRS worldwide-income guidance', link(WORLD,'IRS worldwide income')),
('Reduce double taxation lawfully', 'A qualifying foreign income tax may support a foreign tax credit. Form 1116 is generally used by individuals; taxes on excluded income cannot also be credited. Eligibility and limits must be evaluated.', 'IRS foreign-tax-credit guidance', link(FTC,'IRS credit rules')),
('FBAR is separate from transfer fees', 'A US person generally must report foreign accounts if their aggregate value exceeded $10,000 at any time in the calendar year. An exact $10,000 transfer does not by itself decide the filing requirement.', 'Account balances, not wire increments; exceptions apply', source('S25')),
('Form 8938 is separate from FBAR', 'For specified individuals living in the US: unmarried or married separate, over $50,000 at year-end or $75,000 anytime; joint, over $100,000 or $150,000. Living-abroad thresholds differ. Both forms can apply.', 'Use residence, filing status and all relevant assets, not just this balance', source('S27')),
('Wise is conditional, not a tax bypass', 'From-CNY requires non-mainland-Chinese status, current or former China work, qualifying tax records within its stated three-year period, and payment to an account you own. Bank-app cap: CNY 300,000/transfer; Alipay: CNY 50,000. Overall limit is document-based.', 'Provider terms checked 2026-11-10; live fee not published as one universal amount', source('S11')),
]
# Inherited catalog: source links are provided for review, not represented as a
# fresh independent verification of each route in this narrow audit.
routes=[('Documented current-account bank wire','S1'),('Existing USD savings wire (does not convert CNY)','S1'),('Unused prior-conversion CNY reconversion','S1'),('Wise bank-app funding','S11'),('Bank demand draft','S4'),('Western Union','S14'),('MoneyGram (dated tariff)','S16'),('Eligible own annual convenience quota','S46'),('Emigration property transfer','S20'),('Foreign-national inheritance transfer','S20'),('Foreign-national property-sale proceeds','S2'),('Overseas ATM cash withdrawal','S9'),('Cross-boundary Payment Connect (not a general USD exit)','S23'),('Genuine business/direct-investment proceeds','S22'),('Direct overseas card spending (not USD deposit)','S9'),('Other licensed bank/exchange channels','S24'),('Informal/private FX (not recommended)','S24'),('Crypto route (not recommended)','S17')]

def main():
    body=callout('info','Executive answer: document the money before choosing the rail','Start with the source-of-funds category and the bank’s recorded identity. For eligible foreign-national lawful income, compare a documented bank remittance with Wise if its work/tax-record conditions fit. No source establishes a cheapest route for this unidentified bank account. Avoid borrowed quotas, false purposes, or unlicensed private exchange. '+link(PBOC,'PBOC Measures Arts. 5, 7, 13'))
    body+='<p><strong>Independent narrow audit: 2026-11-10 UTC.</strong> Eight rules below were freshly checked against seven official government/provider pages plus the permanent-resident circular. This is not a fresh line-by-line verification of every inherited document. Links identify evidence, not personal tax advice.</p>'
    body+=table(['Priority','Finding','Evidence boundary','Official source'],rules,'Freshly checked executive findings')
    body+='<section class="section"><h2>Execution playbook</h2><ol class="procedure">'
    steps=[('Have the bank identify its recorded account-holder category and the exact lawful source of each CNY deposit. Do not relabel salary, a gift, property proceeds or company funds as one another.',link(PBOC,'Measures Arts. 2, 5, 28')),
    ('For lawful current-account income, assemble passport, amount-linked source documents and Chinese tax evidence; request review under Detailed Rules Art. 13 rather than assuming an annual quota is the only option.',link(SAFE,'Detailed Rules Art. 13')),
    ('If work and tax history qualify, request a Wise CNY-to-own-USD-account quote; verification establishes the overall permitted amount. Provider transaction caps do not authorize quota evasion.',source('S11')+' '+link(PBOC,'Art. 7')),
    ('For a bank quote, obtain CNY total debit, USD net receipt, the selling rate, each sending/intermediary/receiving charge, and quote expiry. The existing tariff/model page is a checklist, not an executable offer.',source('S4','S5')),
    ('If someone calls a charge a tax, obtain the taxing authority, tax base, tax year and assessment. Evaluate US worldwide income and eligible foreign tax credits separately from provider charges.',link(WORLD,'IRS income')+' '+link(FTC,'IRS credit')),
    ('Review prior and current FBAR and Form 8938 obligations independently of the wire amount. Moving funds does not establish that earlier reporting was complete.',source('S25','S27')),
    ('Submit only authentic, consistent documents through the approved bank/provider flow; retain the FX purchase record, wire receipt and final account credit. Do not split to evade review.',link(PBOC,'Measures Arts. 5–8'))]
    body+=''.join(f'<li>{text} {src}</li>' for text,src in steps)+'</ol></section>'
    body+='<section class="section"><h2>Strict current-cost register: $10,000 to $400,000</h2><p><strong>Blank is unverified, not free.</strong> No current executable fee, execution FX rate, personal tax liability or all-in total has been verified for this account. Accordingly every such value is intentionally blank. The historical arithmetic scenarios on <a href="penalties.html">Costs</a> are not filled into this register. In each table, the USD figure is the requested comparison target, not proof of eligibility or a promised net credit. An official rule or provider source accompanies every row; it does not supply the missing price.</p><p>The inherited catalog has 18 route categories; some are unsuitable, do not produce a US USD deposit, or are expressly not recommended. Its complete pros, cons and procedural detail remains on <a href="methods.html">Methods</a>. Fresh independent verification here is limited to the rules above.</p>'
    for n,(name,sid) in enumerate(routes,1):
        rows=[(f'${i*10000:,}','','','','','Unverified; eligibility and quote required',source(sid)) for i in range(1,41)]
        body+=f'<details class="strict-route"><summary>{n}. {name} — 40 amounts</summary>'+table(['USD target','Current fee USD','FX cost USD','Tax USD','All-in cost USD','Status','Official source'],rows,f'{name}: current costs intentionally blank')+'</details>'
    body+='</section><section class="section" id="audit-flags"><h2>Flagged for Review — this audit</h2>'
    flags=[('High','Inherited FX snapshot cannot be reproduced from a permanent static official row. Derived dollar figures remain historical illustrations, not verified current costs. Do not use their apparent precision to select a route.',source('S5','S48')),
    ('High','Unknown bank, ownership, source of funds, Chinese tax history, US basis and reporting history prevent an actual cheapest-route or tax calculation.',link(SAFE,'Required evidence')+' '+link(WORLD,'US income rules')),
    ('Medium','A structural test requiring a source link per row is not semantic verification that the source proves every statement. Inherited procedures beyond this brief need claim-by-claim review.',source('S1','S11')),
    ('Medium','The Wise guide describes the last-three-years tax record requirement with a 2025 example. This audit does not turn that example into an independently confirmed fixed 2026 start date.',source('S11'))]
    body+=table(['Priority','Irregularity and handling','Official source'],flags,'Unresolved matters; do not block publication')+'</section>'
    (ROOT/'evidence.html').write_text(layout('evidence.html','Verified evidence brief','Fresh primary-source checks · strict current-cost blanks · executable quotes not invented',body),encoding='utf-8')
    print('Built evidence.html: 8 checked rules, 18 × 40 strict cost rows, 4 review flags.')
if __name__=='__main__': main()
