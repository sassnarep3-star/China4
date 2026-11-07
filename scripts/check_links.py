#!/usr/bin/env python3
"""Check static local references and presence of sources in JS records; not legal verification."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import re, sys
root = Path(__file__).resolve().parents[1]
errors = []
class Links(HTMLParser):
    def __init__(self, path): super().__init__(); self.path = path
    def handle_starttag(self, tag, attrs):
        for key, val in attrs:
            if key not in ('href', 'src') or not val: continue
            parsed = urlsplit(val)
            if parsed.scheme or parsed.netloc or not parsed.path: continue
            target = (self.path.parent / unquote(parsed.path)).resolve()
            if not target.exists(): errors.append(f'{self.path.relative_to(root)}: missing {val}')
for f in root.rglob('*.html'):
    parser = Links(f); parser.feed(f.read_text())
# Data rows without a source are a failure. Method entries use a sources array;
# bracket rows get their common official source directly in the renderer.
for filename in ('rules.js', 'us.js', 'costs.js'):
    text = (root/'site/data'/filename).read_text()
    for record in re.findall(r'\{\s*(?:area|regime|item):.*?\n  \}', text, re.S):
        if 'source:' not in record: errors.append(f'{filename}: record missing source')
        if 'status: "verified"' in record and not re.search(r'https?://[^" ]*(?:gov\.cn|irs\.gov|fincen\.gov|cbp\.gov|govinfo\.gov)', record): errors.append(f'{filename}: verified row missing official domain')
for filename, pattern in [('methods.js', r'\{\s*name:.*?\n      \}'), ('flagged.js', r'\{\s*id:.*?\n  \}')]:
    for record in re.findall(pattern, (root/'site/data'/filename).read_text(), re.S):
        if not re.search(r'https?://', record): errors.append(f'{filename}: record missing external source')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print('PASS: local HTML references and data source presence (external links not tested).')
