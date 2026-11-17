#!/usr/bin/env python3
"""Record a game patch, flag only matching guide chapters, never rewrite content."""
from pathlib import Path
import argparse,json,datetime
ROOT=Path(__file__).resolve().parent

def load(path):return json.loads(path.read_text(encoding='utf-8'))
def dump(path,obj):path.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

def main():
 ap=argparse.ArgumentParser(description=__doc__)
 for f in ['game-version','build','released','url','summary','topics']:ap.add_argument('--'+f,required=True)
 a=ap.parse_args();cpath=ROOT/'data'/'chapters.json';ppath=ROOT/'data'/'patches.json';chapters=load(cpath);patches=load(ppath)
 if not a.build.isdigit():ap.error('--build must contain digits')
 if a.build in [p['build'] for p in patches]:ap.error('Build already recorded: '+a.build)
 topics={s.strip().lower() for s in a.topics.split(',') if s.strip()}
 known=set(t for c in chapters for t in c['topics'])
 if topics=={'all'}: impacted=list(chapters);topics={'all'}
 else:
  unknown=topics-known
  if unknown:ap.error('Unrecognised topics: '+','.join(sorted(unknown)))
  if not topics:ap.error('No topics provided')
  impacted=[c for c in chapters if topics.intersection(c['topics'])]
 for c in impacted:
  c.setdefault('pending_builds',[]).append(a.build)
  c['review_state']='needs-review'
 patches.append({'game_version':a.game_version,'build':a.build,'released_utc':a.released,'recorded_on':datetime.date.today().isoformat(),'source_url':a.url,'summary':a.summary,'topics':sorted(topics),'state':'review-pending'})
 dump(cpath,chapters);dump(ppath,patches)
 with (ROOT/'CHANGELOG.md').open('a',encoding='utf8') as f:
  f.write(f'\n## {datetime.date.today().isoformat()} · Patch {a.game_version} / build {a.build} queued\n\n- Source: {a.url}\n- Affected chapters: '+', '.join(c['id'] for c in impacted)+'\n- Pending verification; no content automatically changed.\n')
 print('Queued patch',a.game_version,a.build,'; flagged',len(impacted),'of',len(chapters),'chapters')
if __name__=='__main__':main()
