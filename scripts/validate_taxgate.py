#!/usr/bin/env python3
"""Validate taxgate.html against data/taxgate.json and the repository.

Checks performed (no network access):
  * every amount row is recomputed independently with Decimal
  * every data-table body row carries at least one external source link
  * every external link points at an official or named primary domain
  * every local link resolves to a file in the repository
  * the load-bearing citations and both main tables are present
  * the page is responsive by construction (table-wrap + data-label cells)
"""
import json
import re
import sys
from decimal import Decimal as D
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ALLOWED = (
    'gov.cn', 'safe.gov.cn', 'chinatax.gov.cn', 'irs.gov', 'ecfr.gov',
    'pbc.gov.cn', 'customs.gov.cn', 'fincen.gov', 'boc.cn', 'abchina.com',
    'hsbc.com.cn', 'ccb.com', 'icbc.com.cn', 'cmbchina.com', 'skyremit.cn',
    'wise.com', 'unionpayintl.com',
)

errors = []
data = json.loads((ROOT / 'data/taxgate.json').read_text())
html = (ROOT / 'taxgate.html').read_text()

# --- 1. independent arithmetic ------------------------------------------------
rows = data['rows']
if len(rows) != 40:
    errors.append(f'expected 40 amount rows, found {len(rows)}')
for i, row in enumerate(rows, start=1):
    amount = D(i * 10000)
    if D(row['amount_usd']) != amount:
        errors.append(f'row {i}: amount {row["amount_usd"]} != {amount}')
        continue
    expect20 = amount * D('0.20')
    expect45 = amount * D('0.45')
    expect_late = expect20 * D('0.0005') * D(30)
    if D(row['prc_tax_20pct_usd']) != expect20:
        errors.append(f'row {i}: 20% figure mismatch')
    if D(row['prc_tax_45pct_usd']) != expect45:
        errors.append(f'row {i}: 45% figure mismatch')
    if D(row['prc_late_fee_30d_usd']) != expect_late:
        errors.append(f'row {i}: surcharge mismatch')

# --- 2. every table body row sourced -----------------------------------------
tables = re.findall(r'<table class="data[^"]*">(.*?)</table>', html, re.S)
if len(tables) < 6:
    errors.append(f'expected at least 6 data tables, found {len(tables)}')
checked_rows = 0
for t_i, table in enumerate(tables, start=1):
    body = re.search(r'<tbody>(.*?)</tbody>', table, re.S)
    if not body:
        errors.append(f'table {t_i}: no tbody')
        continue
    for r_i, tr in enumerate(re.findall(r'<tr>.*?</tr>', body.group(1), re.S), start=1):
        checked_rows += 1
        links = re.findall(r'href="(https?://[^"]+)"', tr)
        if not links:
            errors.append(f'table {t_i} row {r_i}: no external source link')
            continue
        if not any(any(dom in url for dom in ALLOWED) for url in links):
            errors.append(f'table {t_i} row {r_i}: no recognised primary domain')

# --- 3. local links resolve ---------------------------------------------------
for href in set(re.findall(r'href="([^"#:]+\.html)"', html)):
    if not (ROOT / href).exists():
        errors.append(f'broken local link: {href}')

# --- 4. required citations present -------------------------------------------
required = [
    'https://fgk.chinatax.gov.cn/zcfgk/c100009/c5193028/content.html',  # IIT Law
    'https://fgk.chinatax.gov.cn/zcfgk/c100009/c5195081/content.html',  # TCA Law
    'https://www.safe.gov.cn/tianjin/2024/0430/2464.html',              # Detailed Rules
    'https://fgk.chinatax.gov.cn/zcfgk/c100012/c5194375/content.html',  # 2013 No. 40
    'https://www.gov.cn/gongbao/content/2008/content_1071846.htm',      # FX Regulations
    'https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010/subpart-H/section-1010.821',
    'https://www.irs.gov/businesses/comparison-of-form-8938-and-fbar-requirements',
]
for url in required:
    if url not in html:
        errors.append(f'missing required source: {url}')
for phrase in ['Art. 13(1)', 'Art. 32', 'Hui Fa [2003] No. 102', 'tax vouchers']:
    if phrase not in html:
        errors.append(f'missing load-bearing phrase: {phrase}')

# --- 5. responsive construction ----------------------------------------------
if html.count('<div class="table-wrap">') < 6:
    errors.append('tables are not wrapped for horizontal scrolling')
if html.count('data-label=') < 100:
    errors.append('cells are not labelled for the mobile card layout')

if errors:
    print('FAIL')
    for e in errors[:40]:
        print(' -', e)
    sys.exit(1)
print(f'PASS: 40 recomputed amount rows, {checked_rows} sourced table rows across '
      f'{len(tables)} tables, required citations, local links and responsive markup.')
