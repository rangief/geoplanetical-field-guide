#!/usr/bin/env python3
"""Rebuild HTML and Markdown from the modular source, then publish the root index."""
from pathlib import Path
import subprocess,sys,shutil
R=Path(__file__).resolve().parent.parent
S=R/'source'
subprocess.run([sys.executable,str(S/'build_guide.py')],check=True)
page=(S/'Geoplanetical_Living_Field_Guide.html').read_bytes()
assert page.startswith(b'<!doctype html>'), 'Expected HTML document'
assert b'class="chapter"' in page and b'id="search"' in page, 'Missing guide features'
(R/'index.html').write_bytes(page)
print('Updated root index.html from 16 source chapters')
