#!/usr/bin/env python3
"""Mark a previously flagged chapter reviewed after the human has checked/edited it."""
from pathlib import Path
import argparse,datetime,json
R=Path(__file__).resolve().parent

def main():
 ap=argparse.ArgumentParser(description=__doc__)
 for field in ['chapter','build','game-version','note']:ap.add_argument('--'+field,required=True)
 ap.add_argument('--keep-historical-caveat',action='store_true',help='Keep historical rule warning even after reviewing the patch.')
 a=ap.parse_args();p=R/'data'/'chapters.json';chapters=json.loads(p.read_text(encoding='utf8'))
 chosen=next((c for c in chapters if c['id']==a.chapter),None)
 if not chosen:ap.error('Unknown chapter ID')
 if a.build not in chosen.get('pending_builds',[]):ap.error('Build was not queued for this chapter; cannot certify it')
 if len(a.note.strip())<12:ap.error('Explain what was actually checked in --note (at least 12 chars)')
 chosen['pending_builds'].remove(a.build)
 chosen['last_reviewed_build']=a.build;chosen['last_reviewed_game_version']=a.game_version;chosen['last_reviewed_on']=datetime.date.today().isoformat()
 chosen['verification_note']=a.note.strip()
 chosen['review_state']='needs-review' if chosen['pending_builds'] else ('historical-details-unverified' if a.keep_historical_caveat else 'current-with-caveats')
 p.write_text(json.dumps(chapters,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
 with (R/'CHANGELOG.md').open('a',encoding='utf8') as f:
  f.write(f'\n- {datetime.date.today().isoformat()}: Reviewed `{a.chapter}` for {a.game_version} / {a.build}: {a.note.strip()}\n')
 print('Review recorded for',a.chapter,'; remaining pending:',chosen['pending_builds'])
if __name__=='__main__':main()
