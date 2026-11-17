#!/usr/bin/env python3
"""Offline publication checks, no network or game dependencies."""
from pathlib import Path
import json,re,hashlib
R=Path(__file__).resolve().parent.parent
html=(R/'index.html').read_text(encoding='utf-8')
chapters=json.loads((R/'source/data/chapters.json').read_text(encoding='utf-8'))
assert html.startswith('<!doctype html>')
assert len(chapters)==16
assert len(set(x['id'] for x in chapters))==16
for c in chapters:
 assert 'id="'+c['id']+'"' in html, c['id']
assert 'id="search"' in html
assert 'Geoplanetical' in html
assert 'community' in html.lower()
assert not any(term in html for term in ('file:///','C:\\Users\\','.env', 'YOUR-GITHUB-USERNAME')), 'Private path or placeholder'
assert '<script' in html and 'input' in html
assert (R/'.nojekyll').is_file()
print('PASS: index present, 16 chapters, search, source identity, no obvious local URLs')
