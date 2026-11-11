#!/usr/bin/env python3
"""Independently check the amount ladder, tariff arithmetic and table citations."""
import json
from decimal import Decimal as D, ROUND_CEILING
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
ROOT=Path(__file__).resolve().parents[1]
class Audit(HTMLParser):
    def __init__(self):
        super().__init__(); self.inbody=False; self.row=None; self.rows=[]
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if tag=='tbody': self.inbody=True
        if tag=='tr' and self.inbody: self.row={'sources':[], 'cells':0}
        if tag=='td' and self.row is not None:
            assert a.get('data-label'); self.row['cells']+=1
        if tag=='a':
            href=a.get('href',''); u=urlsplit(href)
            if not u.scheme and u.path: assert (ROOT/u.path).exists(), href
            if self.row is not None and 'source' in a.get('class','').split():
                assert u.scheme=='https' and u.netloc; self.row['sources'].append(href)
    def handle_endtag(self, tag):
        if tag=='tr' and self.row is not None:
            assert self.row['cells'] and self.row['sources']; self.rows.append(self.row); self.row=None
        if tag=='tbody': self.inbody=False

data=json.loads((ROOT/'data/method-treaty.json').read_text()); rows=data['rows']; assert len(rows)==40
assert data['historical_cny_per_usd']=='6.6929'
for i,r in enumerate(rows,1):
    a=D(i*10000); p=a*D('6.6929'); assert r['usd']==a and D(r['illustrative_cny_principal'])==p
    for key,lo,hi,cable in [('abc_sha_cny',20,200,80),('boc_sha_cny',50,260,150),('hsbc_standard_sha_cny',100,500,120)]:
        assert D(r[key])==min(D(hi),max(D(lo),p/D(1000)))+D(cable)
    for key,base,value in [('cny_300000_min_transfers',p,300000),('wise_alipay_min_transfers',p,50000),('moneygram_min_transfers',a,10000)]:
        assert r[key]==int((base/D(value)).to_integral_value(rounding=ROUND_CEILING))
    assert D(r['treaty_difference_usd'])==a/D(10) and D(r['sdop_illustrative_penalty_usd'])==a/D(20)
for name,count in [('method-matrix.html',80),('treaty-filings.html',50)]:
    p=Audit(); p.feed((ROOT/name).read_text()); assert len(p.rows)==count,(name,len(p.rows))
print('PASS: 40 scenarios, tariff arithmetic, cap counts, sourced responsive rows and local links.')
