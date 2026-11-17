#!/usr/bin/env python3
"""Build readable HTML and Markdown from separately editable chapters."""
from pathlib import Path
import html,json,sys,re
try:
 import mistune
except ImportError:
 print('Missing dependency: run python -m pip install -r requirements.txt',file=sys.stderr);sys.exit(2)
R=Path(__file__).resolve().parent
C=json.loads((R/'data'/'chapters.json').read_text(encoding='utf8'))
P=json.loads((R/'data'/'patches.json').read_text(encoding='utf8'))
assert C and P
keys=[c['id'] for c in C]
assert len(keys)==len(set(keys)), 'Duplicate chapter IDs'
C.sort(key=lambda c:c['order'])
patch=P[-1]
md=['# Geoplanetical: The Living Player’s Field Guide', '',
    f'> Guide edition: 0.1 · Latest **recorded** game version: {patch["game_version"]} / build {patch["build"]} · {patch["recorded_on"]}',
    '', 'Community-informed, independent player handbook. **Not official.** Chapters marked NEEDS REVIEW may be outdated following a patch.',
    '','## Contents','']
for c in C:md.append(f'- [{c["title"]}](#{c["id"]})')
md.append('')
html_sections=[]
renderer=mistune.create_markdown(plugins=['table','strikethrough','url'])
for c in C:
 path=R/c['path']
 assert path.is_file(),f'Missing chapter {path}'
 s=path.read_text(encoding='utf8')
 assert s.startswith('# '),f'Chapter missing title: {path}'
 md.extend([f'<a id="{c["id"]}"></a>','',s,'','---',''])
 pending=c.get('pending_builds',[])
 if pending: label='NEEDS REVIEW • '+', '.join(pending);cl='danger'
 elif c['review_state']=='historical-details-unverified':label='Older numbers unverified';cl='amber'
 else:label='Checked against '+c['last_reviewed_game_version'];cl='ok'
 rendered=renderer(s)
 rendered=re.sub(r'<(/?)h([1-5])',lambda m:'<'+m[1]+'h'+str(int(m[2])+1),rendered)
 html_sections.append(f'<section class="chapter" id="{html.escape(c["id"])}" data-title="{html.escape(c["title"])}">'
                      f'<div class="section-top"><span class="status {cl}">{html.escape(label)}</span>'
                      f'<span class="review">Last editorial review: {html.escape(c["last_reviewed_on"])} · {html.escape(c["last_reviewed_build"])}</span></div>'
                      f'{rendered}</section>')
(R/'Geoplanetical_Living_Field_Guide.md').write_text('\n'.join(md)+'\n',encoding='utf8')
nav='\n'.join(f'<a class="navlink" href="#{html.escape(c["id"])}"><span>{c["order"]+1:02d}</span> {html.escape(c["title"])}</a>' for c in C)
pending_count=sum(bool(c['pending_builds']) for c in C)
source_link='https://steamcommunity.com/app/940230/allnews/'
title='Geoplanetical | Living Field Guide'
page=f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="color-scheme" content="light">
<title>{title}</title>
<style>
:root{{--ink:#1d2c37;--muted:#526475;--bg:#edf2f3;--panel:#fff;--border:#d5e0e4;--navy:#112b40;--teal:#007b79;--gold:#ffcf70;}}
[hidden]{{display:none!important}}
.skip{{position:absolute;left:12px;top:-80px;background:white;padding:10px;z-index:5}} .skip:focus{{top:12px}} :focus-visible{{outline:3px solid #ac6600;outline-offset:3px}}
*{{box-sizing:border-box}} html{{scroll-behavior:smooth}} body{{margin:0;background:var(--bg);color:var(--ink);font:16px/1.68 system-ui,-apple-system,Segoe UI,Arial,sans-serif}} a{{color:#046c75}} a:hover{{text-decoration-color:#d7a44a}} 
.hero{{background:linear-gradient(130deg,#0e2637 0%,#16465c 70%,#2b5f66 100%);color:#fff;padding:38px max(22px,calc((100vw - 1310px)/2));}}
.eyebrow{{font-size:12px;font-weight:800;letter-spacing:.15em;color:#bce5df;text-transform:uppercase}} h1,h2,h3{{line-height:1.22;letter-spacing:-.02em}} .hero h1{{font-size:clamp(29px,4.6vw,52px);margin:12px 0}} .hero p{{max-width:760px;color:#dbebec;margin:5px 0 17px}}
.hero .pill{{display:inline-block;padding:4px 11px;margin:0 8px 8px 0;border:1px solid #6b9aa7;border-radius:50px;font-size:12px;color:#e3f2f4}}
.shell{{display:grid;grid-template-columns:275px minmax(0,850px);gap:24px;max-width:1300px;margin:26px auto;padding:0 20px;align-items:start}}
.sidebar{{position:sticky;top:18px;background:var(--panel);border:1px solid var(--border);border-radius:14px;padding:18px;max-height:calc(100vh - 36px);overflow:auto;box-shadow:0 4px 20px #1837490c}}
.sidebar h2{{font-size:15px;margin:2px 0 10px}} input{{width:100%;padding:10px 12px;border:1px solid #a4bcc4;border-radius:8px;font-size:14px;margin-bottom:9px;outline-offset:2px}}
.navlink{{display:flex;gap:10px;color:#2c4352;text-decoration:none;padding:6px 8px;border-radius:8px;font-size:14px;line-height:1.4}} .navlink span{{color:#738e9e;font-variant-numeric:tabular-nums}} .navlink:hover,.navlink:focus{{background:#edf5f5}}
.hint{{font-size:12px;color:var(--muted)}} .content{{min-width:0}} .notice{{padding:14px 17px;border:1px solid #c8d9df;border-left:4px solid #258585;border-radius:9px;background:#faffff;margin-bottom:22px}}
.chapter{{background:#fff;border:1px solid var(--border);border-radius:14px;box-shadow:0 4px 20px #1837490b;padding:27px clamp(19px,4vw,42px);margin-bottom:24px;scroll-margin-top:20px}}
.chapter h2{{font-size:clamp(23px,2.4vw,31px);margin:16px 0 20px;color:#13384c}} .chapter h3{{font-size:21px;color:#16485b;margin-top:30px}}.chapter h4{{font-size:17px;margin-top:23px}} .chapter p{{margin:13px 0}}.chapter li{{padding:2px 0}}.chapter blockquote{{margin:20px 0;padding:3px 18px;border-left:4px solid #e5ad55;background:#fff8ea;border-radius:4px}} .chapter blockquote p{{margin:12px 0}}
.section-top{{display:flex;gap:10px;flex-wrap:wrap;align-items:center;justify-content:space-between;border-bottom:1px solid #e4ebee;padding-bottom:14px}}
.status{{padding:3px 10px;font-size:11px;font-weight:800;letter-spacing:.04em;border-radius:50px}} .ok{{background:#e2f4eb;color:#216241}} .danger{{background:#ffe2e2;color:#8f2626}} .amber{{background:#fff0cd;color:#85500d}} .review{{font-size:12px;color:var(--muted)}}
.chapter table{{display:block;overflow-x:auto;border-collapse:collapse;max-width:100%;font-size:14px}}.chapter th,.chapter td{{border:1px solid #dbe5e9;padding:9px 11px;text-align:left;vertical-align:top}}.chapter th{{background:#eaf2f4}}
.empty{{background:#fff;padding:20px;border-radius:12px;display:none}} footer{{color:var(--muted);font-size:12px;padding:14px 4px 40px}} code{{background:#eaf1f3;border-radius:3px;padding:2px 4px}} 
@media(max-width:890px){{.shell{{grid-template-columns:1fr}}.sidebar{{position:static;max-height:none}}.navlist{{display:grid;grid-template-columns:repeat(auto-fit,minmax(155px,1fr))}}.hero{{padding:30px 20px}}}}
@media(prefers-reduced-motion:reduce){{html{{scroll-behavior:auto}}}}
</style></head><body>
<a class="skip" href="#guide">Skip to guide</a>
<header class="hero"><div class="eyebrow">Independent community handbook · Edition 0.1</div><h1>Geoplanetical<br> The Living Field Guide</h1>
<p>Run a country. Fix the actual problem. Avoid accidentally financing three disasters at once. Friendly explanations for a complicated world.</p>
<span class="pill">Recorded game version: {html.escape(patch['game_version'])}</span><span class="pill">Steam build: {html.escape(patch['build'])}</span><span class="pill">{pending_count} chapters awaiting review</span>
</header>
<div class="shell"><aside class="sidebar"><h2>Find what you need</h2><label for="search" class="hint">Filter chapters by a word or topic</label><input id="search" type="search" placeholder="Try: inflation, war, electricity" autocomplete="off" aria-label="Search guide chapters"><div id="count" class="hint" role="status" aria-live="polite"></div><nav class="navlist" aria-label="Guide contents">{nav}</nav><p class="hint">This guide was reviewed against the recorded patch notes. Older mechanics may still need in-game testing.</p></aside>
<main id="guide" class="content" tabindex="-1"><div class="notice"><strong>A living guide, not a crystal ball.</strong> Chapter badges show when they were last checked. A red <strong>Needs review</strong> badge means a newer patch may have changed that advice. View <a href="{source_link}">official Steam news</a> for new announcements.</div>
<div id="empty" class="empty">No chapters match that search. Try fewer words or a different topic.</div>
{''.join(html_sections)}
<footer>Community-informed and not affiliated with Polytale Games. Original guidance credited to Balee_92, warmaninger, grayassembly and Traslo. Source and update method documented in <a href="source/SOURCES.md">Sources and credits</a> and <a href="source/MAINTAINERS.md">Maintainer workflow</a>. No automatic background updates.</footer></main></div>
<script>
(function(){{const box=document.getElementById('search'),sections=[...document.querySelectorAll('.chapter')],links=[...document.querySelectorAll('.navlink')],counter=document.getElementById('count');
const clean=s=>s.toLocaleLowerCase().normalize('NFKC');
function update(){{const words=clean(box.value).trim().split(/\\s+/).filter(Boolean);let shown=0;sections.forEach(s=>{{let hay=clean(s.textContent);let ok=words.every(w=>hay.includes(w));s.hidden=!ok;if(ok)shown++;}});links.forEach(a=>{{let sec=document.getElementById(a.getAttribute('href').slice(1));a.hidden=!!sec.hidden;}});counter.textContent=shown+' of '+sections.length+' chapters shown';document.getElementById('empty').style.display=shown?'none':'block';}}
box.addEventListener('input',update);box.addEventListener('keydown',e=>{{if(e.key==='Escape'){{box.value='';update();}}}});function revealHash(){{const target=document.getElementById(location.hash.slice(1));if(target&&target.classList.contains('chapter')&&target.hidden){{box.value='';update();target.scrollIntoView();}}}}window.addEventListener('hashchange',revealHash);update();revealHash();}})();
</script></body></html>'''
(R/'Geoplanetical_Living_Field_Guide.html').write_text(page,encoding='utf8')
print('Built Markdown', (R/'Geoplanetical_Living_Field_Guide.md').stat().st_size,'and HTML', (R/'Geoplanetical_Living_Field_Guide.html').stat().st_size,'bytes')
