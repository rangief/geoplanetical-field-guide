#!/usr/bin/env python3
"""Non-destructive tests: simulate a future patch on a disposable copy."""
from pathlib import Path
import tempfile, shutil, subprocess,json,sys
R=Path(__file__).resolve().parent
with tempfile.TemporaryDirectory(prefix='geo-guide-qa-') as tmp:
 d=Path(tmp)
 for fn in ['patch_intake.py','review_chapter.py','build_guide.py','requirements.txt','CHANGELOG.md']:
  shutil.copy2(R/fn,d/fn)
 shutil.copytree(R/'data',d/'data'); shutil.copytree(R/'chapters',d/'chapters')
 original=json.loads((d/'data'/'chapters.json').read_text()); unrelated=next(c for c in original if c['id']=='10-warfare')
 def call(*args):
  p=subprocess.run([sys.executable,*args],cwd=d,text=True,capture_output=True)
  if p.returncode:raise AssertionError(f'Command failed: {args}: {p.stderr}')
  return p.stdout
 call('patch_intake.py','--game-version','1.1.TEST','--build','99999999','--released','2026-11-19','--url','https://example.org/patch-notes','--summary','Test inflation change','--topics','inflation')
 updated=json.loads((d/'data'/'chapters.json').read_text())
 assert next(c for c in updated if c['id']=='10-warfare')==unrelated,'Unrelated warfare chapter changed'
 impacted=[c for c in updated if c['pending_builds']==['99999999']]
 assert impacted and all('inflation' in c['topics'] for c in impacted)
 assert len(impacted)<len(updated)
 assert next(c for c in updated if c['id']=='07-inflation-and-currency')['review_state']=='needs-review'
 call('review_chapter.py','--chapter','07-inflation-and-currency','--build','99999999','--game-version','1.1.TEST','--note','Reviewed fictional test patch only; no gameplay evidence')
 final=json.loads((d/'data'/'chapters.json').read_text())
 assert '99999999' not in next(c for c in final if c['id']=='07-inflation-and-currency')['pending_builds']
 assert next(c for c in final if c['id']=='10-warfare')==unrelated
 try:
  call('build_guide.py')
  assert (d/'Geoplanetical_Living_Field_Guide.html').is_file()
  assert 'NEEDS REVIEW' in (d/'Geoplanetical_Living_Field_Guide.html').read_text()
 except AssertionError:raise
print('PASS: future patch marks only relevant chapters; reviewed chapter clears its own flag; unrelated chapters untouched; outputs rebuilt. No original files changed.')
