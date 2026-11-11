#!/usr/bin/env python3
"""Regression audit for the 2026-11-11 ATM notice rollover.

Checks publication wording, not live availability or source authenticity.
The notice was manually read on 2026-11-11; numerical model stays historical.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
NOTICE = 'https://www.boc.cn/pbservice/bi2/202608/t20260811_25684907.html'
pages = ['index', 'summary', 'methods', 'penalties', 'taxes', 'sources',
         'flagged', 'evidence']
for page in pages:
    text = (ROOT / f'{page}.html').read_text()
    assert 'ATM update · 2026-11-11' in text, page
    assert NOTICE in text, page
    assert 'Future Visa/Mastercard' not in text, page
    assert 'one day after the research cutoff' not in text, page
    assert 'This does not refresh the historical FX quote' in text, page
assert 'now in force' in (ROOT / 'sources.html').read_text()
assert 'Issuer fees are not all-in ATM costs' in (ROOT / 'flagged.html').read_text()
# Rollover must not fabricate a newer FX snapshot.
model = (ROOT / 'data/cost-model.json').read_text()
json.loads(model)
assert '6.6929' in model
print('PASS: 8 pages show the sourced tariff rollover, no obsolete future wording; historical FX preserved.')
