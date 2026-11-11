#!/usr/bin/env python3
"""Check all root HTML local targets and publishing-mode safeguards, offline."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.ids, self.links = set(), []
        self.feed(path.read_text())
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            self.ids.add(a['id'])
        for key in ('href', 'src'):
            if a.get(key):
                self.links.append(a[key])

pages = {p.resolve(): Page(p) for p in ROOT.glob('*.html')}
errors = []
for path, page in pages.items():
    for link in page.links:
        u = urlsplit(link)
        if u.scheme or u.netloc:
            continue
        target = (path.parent / unquote(u.path)).resolve() if u.path else path
        if target.is_dir():
            target /= 'index.html'
        if not target.is_file():
            errors.append(f'{path.name}: missing {link}')
        elif u.fragment and target in pages and unquote(u.fragment) not in pages[target].ids:
            errors.append(f'{path.name}: missing anchor {link}')
w = (ROOT / '.github/workflows/gh-pages.yml').read_text()
if 'actions/deploy-pages' in w:
    errors.append('Competing Actions deploy reintroduced while branch publishing is authoritative')
if 'scripts/validate_publication.py' not in w:
    errors.append('Publication validator must run in CI')
assert not errors, '\n'.join(errors)
print(f'PASS: all {len(pages)} root HTML pages local links/anchors; branch-publisher-only workflow; CI publication check.')
