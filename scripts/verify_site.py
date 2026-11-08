#!/usr/bin/env python3
"""Check local navigation, source links on table rows and cost schedule coverage."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
PAGES = ['index.html','methods.html','penalties.html','taxes.html','flagged.html','sources.html']
OFFICIAL = ('safe.gov.cn', 'english.shanghai.gov.cn', 'bankofchina.com', 'irs.gov', 'fincen.gov', 'pbc.gov.cn', 'cbp.gov')

class Audit(HTMLParser):
    def __init__(self):
        super().__init__(); self.links=[]; self.in_body=False; self.row=None; self.rows=[]
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if tag == 'tbody': self.in_body=True
        if tag == 'tr' and self.in_body: self.row=[]
        if tag in ('a','link'):
            href=attrs.get('href',''); self.links.append(href)
            if self.row is not None: self.row.append(href)
    def handle_endtag(self, tag):
        if tag == 'tr' and self.row is not None: self.rows.append(self.row); self.row=None
        if tag == 'tbody': self.in_body=False

for name in PAGES:
    text=(ROOT/name).read_text(encoding='utf-8')
    p=Audit(); p.feed(text)
    for href in p.links:
        url=urlparse(href)
        if not url.scheme and url.path and not (ROOT/url.path).is_file():
            raise SystemExit(f'{name}: missing local link {href}')
    for i, row in enumerate(p.rows,1):
        if not any(any((urlparse(u).hostname or '') == d or (urlparse(u).hostname or '').endswith('.'+d) for d in OFFICIAL) for u in row):
            raise SystemExit(f'{name}: table row {i} lacks official source')
    if name == 'penalties.html':
        for amount in range(10000,400001,10000):
            if f'${amount:,.0f}' not in text: raise SystemExit(f'Missing ${amount:,}')
    print(f'{name}: {len(p.rows)} sourced rows; local links OK')
print('Static checks passed; source relevance/currentness and external availability require separate review.')
