#!/usr/bin/env python3
"""Build task 23 comparisons from documented tariffs, not executable quotes."""
from decimal import Decimal as D, ROUND_CEILING
from pathlib import Path
import json
from build_site import ROOT, layout, table, source

ABC='https://www.abchina.com/cn/PublicPlate/sfbz/fwjgbz/202109/t20210929_2047241.htm'
HSBC='https://www.hsbc.com.cn/content/dam/hsbc/cn/docs/document-download/tariff-of-accouts-and-services.pdf'
STA='https://tianjin.chinatax.gov.cn/11200000000/0300/030004/03000418/20191024101530609.shtml'
FIE='https://fgk.chinatax.gov.cn/zcfgk/c102416/c5252107/content.html'
TREATY='https://www.irs.gov/pub/irs-trty/china.pdf'
FTC='https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1/section-1.901-2'
F6166='https://www.irs.gov/individuals/international-taxpayers/form-6166-certification-of-us-tax-residency'
F8833='https://www.irs.gov/forms-pubs/about-form-8833'
SFOP='https://www.irs.gov/individuals/international-taxpayers/us-taxpayers-residing-outside-the-united-states'
SDOP='https://www.irs.gov/individuals/international-taxpayers/us-taxpayers-residing-in-the-united-states'
DIIRSP='https://www.irs.gov/individuals/international-taxpayers/delinquent-international-information-return-submission-procedures'
FBAR='https://www.taxpayeradvocate.irs.gov/wp-content/uploads/2023/01/ARC22_PurpleBook_04_ReformPenInts_34.pdf'
PRC='https://fgk.chinatax.gov.cn/zcfgk/c100012/c5194375/content.html'
SAFE='https://www.safe.gov.cn/safe/2021/0702/19306.html'
REFUND='https://guangdong.chinatax.gov.cn/gdsw/zjfg/2015-04/24/content_7585cb6a374c47cb92fafcdabc17e8de.shtml'

def link(url, text):
    return f'<a class="source" href="{url}" rel="noopener noreferrer">{text}</a>'
def ceil(x): return int(x.to_integral_value(rounding=ROUND_CEILING))
def cny(x): return f'¥{x:,.2f}'
def usd(x): return f'${x:,.2f}'
def commission(p, low, high): return min(D(high),max(D(low),p*D('.001')))

def main():
    rate=D('6.6929'); rows=[]
    for n in range(1,41):
        amount=D(n*10000); p=amount*rate
        rows.append({'usd':int(amount),'illustrative_cny_principal':str(p), 'abc_sha_cny':str(commission(p,20,200)+80), 'boc_sha_cny':str(commission(p,50,260)+150), 'hsbc_standard_sha_cny':str(commission(p,100,500)+120), 'cny_300000_min_transfers':ceil(p/D(300000)), 'wise_alipay_min_transfers':ceil(p/D(50000)), 'moneygram_min_transfers':ceil(amount/D(10000)), 'treaty_difference_usd':str(amount*D('.10')), 'sdop_illustrative_penalty_usd':str(amount*D('.05'))})
    data={'as_of':'2026-11-11','historical_cny_per_usd':str(rate),'rate_note':'Historical BOC selling-rate illustration, not a current quote or net-payout guarantee.', 'rows':rows}
    (ROOT/'data/method-treaty.json').write_text(json.dumps(data,indent=2)+'\n')
    bankref=link(ABC,'ABC')+' '+source('S4')+' '+link(HSBC,'HSBC')
    bankrows=[[usd(D(r['usd'])),cny(D(r['abc_sha_cny'])),cny(D(r['boc_sha_cny'])),cny(D(r['hsbc_standard_sha_cny'])),bankref] for r in rows]
    caprows=[[usd(D(r['usd'])),str(r['cny_300000_min_transfers']),str(r['wise_alipay_min_transfers']),str(r['moneygram_min_transfers']),'—',source('S11')+' '+link('https://www.skyremit.cn/news/blog-detail-119-SkyRemit-Salary-Remittance-Frequently-Asked-Questions.html','SkyRemit')+' '+link('https://www.icbc.com.cn/page/721854316817449008.html','ICBC') ] for r in rows]
    body='<p><a href="treaty-filings.html">Treaty and filing playbook →</a> · <a href="banks.html">Bank evidence</a> · <a href="evidence.html">Strict current-cost register</a></p>'
    body+='<div class="callout warning"><strong>Not an all-in quote.</strong> Illustrations use the historical 6.6929 CNY/USD BOC selling rate solely to size the principal. Compare identical net USD receipts using live FX and branch quotes. Sending commissions below exclude FX spread, taxes, intermediary and receiving charges and assume one transfer; other institutions may use a different FX rate. Eligibility and source-of-funds documentation still apply.</div>'
    body+='<h2>Illustrative sending-bank fees</h2><p>Standard SHA fees, using published tariff formulas only. Actual discounts, eligibility and fees must be confirmed. HSBC Premier Elite and Private Banking outward TT and cable are shown as zero in the cited tariff; standard Premier is not. Existing USD does not require this conversion but remains subject to wire fees.</p>'
    body+=table(['USD principal','ABC SHA','BOC SHA','HSBC Premier / Advance SHA','Tariff'],bankrows,'40 amounts · sending commission and cable only')
    body+='<p>For documented full-arrival services, ABC adds USD 25 and BOC adds USD 15 for BOC New York or USD 25 otherwise; HSBC USD full-amount service prepays ¥200 and a shortfall may be charged. These are not guarantees against all deductions. '+bankref+'</p>'
    body+='<p>HSBC Global Transfer to eligible own/family HSBC accounts and Study Abroad Transfer to eligible destinations are free for Premier per tariff; confirm entitlement, route, FX and other banks’ charges. An advertised zero commission is not a zero all-in cost. '+link(HSBC,'HSBC tariff sections 2.2.4, 2.2.6, 2.2.7')+'</p>'
    body+='<h2>Provider caps: arithmetic lower bounds, not a recommended splitting plan</h2><p>Wise bank funding and SkyRemit each have a CNY 300,000 per-transfer ceiling; Wise Alipay has CNY 50,000. ICBC MoneyGram has USD 10,000 per transfer and USD 20,000 per day. These counts ignore fees, minimums, daily and overall limits, provider verification, eligibility and timing. Never split to evade controls. Current prices and net receipts are unknown.</p>'
    body+=table(['USD equivalent','300k CNY cap','Wise Alipay 50k cap','MoneyGram 10k cap','Live cost','Source'],caprows,'Minimum transfers based on historical principal')
    body+='<p>For demand drafts, overseas ATM, emigration property transfers and other channels see <a href="playbooks.html">documented playbooks</a> and <a href="penalties.html">existing BOC models</a>. No comparative live quote or universal eligibility is asserted.</p>'
    (ROOT/'method-matrix.html').write_text(layout('method-matrix.html','Transfer method matrix','Compare documented tariffs and provider limits, not live prices.',body))
    rules=[
    ('Outbound filing scope','Announcement 2013 No. 40 Art. 1 applies to domestic institutions and individuals for specified external payments over USD 50,000; Art. 3 lists exemptions. Art. 4 directs foreign individuals’ own income/current transfers to personal FX rules. The 2021 notice addresses repeat payments under a single contract. Classify the payment before applying either route.',link(PRC,'2013 No. 40')+' '+link(SAFE,'2021 No. 19')+' '+source('S1')),
    ('Determine treaty eligibility','For a qualifying US treaty resident and beneficial owner, Treaty Art. 9 generally caps source-country dividend tax at 10% of gross; exceptions include effectively connected holdings. Residence, beneficial ownership, anti-abuse rules and facts matter; US citizenship alone does not establish eligibility.',link(TREATY,'Treaty Art. 9')+' '+link(STA,'2019 No. 35')),
    ('Certificate and China claim','Apply for IRS Form 6166 using Form 8802. Since Oct. 1, 2026, the individual user fee is $105. Pay.gov PDF upload does not replace mailing or faxing the signed application. Under 2019 No. 35, self-assess, submit the nonresident treaty-benefit information report to the withholding agent and retain supporting materials, including appropriate residency certificate and beneficial-ownership evidence.',link(F6166,'IRS 6166')+' '+link(STA,'2019 No. 35 Arts. 3–7')),
    ('Excess withholding and FTC','From Sept. 1, 2026 the cited PRC announcement taxes foreign individuals’ FIE dividends at 20%. If a 10% treaty limit applies, the difference may be refundable, but US creditability depends on the compulsory-payment rules and reasonable steps to reduce foreign tax. Do not assume the excess is creditable or that every dividend qualifies.',link(FIE,'2026 No. 27')+' '+link(FTC,'26 CFR 1.901-2')+' '+link(TREATY,'Treaty')),
    ('China refund','Announcement 2019 No. 35 Art. 10 provides a claim procedure and verification within 30 days; China Tax Collection and Administration Law Art. 51 addresses refunds of overpaid tax within three years. Confirm accrual date and applicable procedure with the authority.',link(STA,'Art. 10')+' '+link(REFUND,'Tax law Art. 51')),
    ('US treaty disclosure','Form 8833 may be required for a treaty-based return position or dual-resident tie-breaker; exceptions and penalties apply. Review the facts and instructions with a cross-border adviser.',link(F8833,'IRS Form 8833')+' '+link('https://www.ecfr.gov/current/title-26/part-301/section-301.6712-1','Disclosure penalty')),
    ('Streamlined foreign','Non-willful taxpayers meeting the foreign non-residency and other eligibility tests generally submit three years of returns and six years of FBARs. The streamlined foreign procedure waives the specified penalties, not tax and interest. Check the appropriate citizenship/residency test.',link(SFOP,'IRS SFOP')),
    ('Streamlined domestic','Non-willful eligible taxpayers failing the foreign non-residency test generally must have filed original returns for the three covered years, submit amended returns and six years of FBARs, and pay a 5% miscellaneous offshore penalty calculated on the specified highest aggregate year-end asset balance.',link(SDOP,'IRS SDOP')),
    ('Delinquent forms','Delinquent FBAR procedures are distinct from streamlined filings; the taxpayer advocate describes no penalty when income was reported and accurate delinquent FBARs are filed before IRS contact. IRS DIIRSP addresses late international information returns with reasonable cause; relief is not automatic. Form 3520 is generally filed separately.',link(FBAR,'Taxpayer Advocate')+' '+link(DIIRSP,'IRS DIIRSP')),
    ('Calendar','US return and FBAR deadlines, extensions and payment interest differ. Certain taxpayers abroad get an automatic two-month return extension, but interest generally runs from the original payment due date. A transfer does not itself cure earlier filing failures.',source('S25')+' '+link('https://www.irs.gov/individuals/international-taxpayers/us-citizens-and-resident-aliens-abroad-automatic-2-month-extension-of-time-to-file','IRS abroad extension'))]
    body='<p><a href="method-matrix.html">← Transfer method matrix</a> · <a href="taxes.html">Tax overview</a></p><div class="callout warning">These are conditional pathways, not individualized advice. Do not assume a treaty, refund, credit or remediation program applies. The dividend and penalty scenarios below use different hypothetical bases and are not added to transfer costs.</div>'
    body+=table(['Issue','Action and qualification','Primary source'],rules,'Treaty, payment and remediation checklist')
    treatyref=link(FIE,'PRC dividend rule')+' '+link(TREATY,'Treaty Art. 9')+' '+link(SDOP,'IRS SDOP')
    trows=[[usd(D(r['usd'])),usd(D(r['treaty_difference_usd'])),usd(D(r['sdop_illustrative_penalty_usd'])),treatyref] for r in rows]
    body+='<h2>Two independent illustrations</h2><p>Dividend column assumes the entire amount is a qualifying gross dividend, domestic 20% versus treaty 10%; it is not a promised refund or US credit. SDOP column assumes the same number instead represents the highest aggregate year-end penalty base, with all assets included; the actual base can differ substantially. Neither figure describes the tax on a transfer.</p>'
    body+=table(['Hypothetical base','20% vs 10% difference','SDOP 5% example','Sources'],trows,'Separate scenarios · $10,000 increments')
    (ROOT/'treaty-filings.html').write_text(layout('treaty-filings.html','Treaty claims and filings','Cross-border documentation and US remediation pathways.',body))
    print('Built method matrix, treaty filings and reproducible data.')
if __name__=='__main__': main()
