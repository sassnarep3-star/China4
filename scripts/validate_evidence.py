#!/usr/bin/env python3
"""Guard the strict blank-cost contract separately from historical arithmetic."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

ROOT=Path(__file__).resolve().parents[1]
class Audit(HTMLParser):
    def __init__(self):
        super().__init__(); self.rows=[]; self.row=None; self.cell=None; self.links=[]; self.body=False; self.route_count=0
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='tbody': self.body=True
        if tag=='details' and a.get('class')=='strict-route': self.route_count+=1
        if tag=='tr' and self.body: self.row={'cells':[],'sources':[]}
        if tag=='td' and self.row is not None: self.cell=''
        if tag=='a':
            self.links.append(a.get('href',''))
            if self.row is not None and a.get('class')=='source': self.row['sources'].append(a['href'])
    def handle_data(self,data):
        if self.cell is not None: self.cell+=data
    def handle_endtag(self,tag):
        if tag=='td' and self.cell is not None: self.row['cells'].append(self.cell); self.cell=None
        if tag=='tr' and self.row is not None: self.rows.append(self.row); self.row=None
        if tag=='tbody': self.body=False
p=Audit(); p.feed((ROOT/'evidence.html').read_text())
assert p.route_count==18
costs=[r for r in p.rows if len(r['cells'])==7]
assert len(costs)==720
for idx,r in enumerate(costs):
    assert r['cells'][0]==f'${(idx%40+1)*10000:,}'
    assert r['cells'][1:5]==['','','',''], 'Unverified executable cost filled in'
for r in p.rows:
    assert r['sources'], 'Row lacks an official source'
for href in p.links:
    u=urlsplit(href)
    if not u.scheme and u.path: assert (ROOT/u.path).exists(), href
for filename in ['index.html','summary.html','methods.html','penalties.html','taxes.html','flagged.html','sources.html']:
    assert 'href="evidence.html"' in (ROOT/filename).read_text()
print('PASS: 720 strictly blank current-cost rows; 18 route ladders; every data row sourced; local links and evidence navigation.')
