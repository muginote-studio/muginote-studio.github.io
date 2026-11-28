#!/usr/bin/env python3
"""Verify the parallel collection retains the original store facts and pages."""
from pathlib import Path
from html import unescape
from html.parser import HTMLParser
import hashlib,json,re
ROOT=Path(__file__).resolve().parents[1]
def flat(html):return re.sub(r'\s+',' ',unescape(re.sub(r'<[^>]+>',' ',html))).strip()
data=json.loads((ROOT/'assets/atelier/content.json').read_text())
manifest=json.loads((ROOT/'collections/atelier.json').read_text())
credits={p['file']:p for p in json.loads((ROOT/'assets/atelier/photo-sources.json').read_text())}
assert len(data)==len(manifest)==100
assert len({r['path']for r in manifest})==100
class Page(HTMLParser):
 def __init__(self):super().__init__();self.hrefs=[];self.images=[];self.h1=0;self.noindex=False
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='a':self.hrefs.append(a.get('href',''))
  if tag=='img':self.images.append(a)
  if tag=='h1':self.h1+=1
  if tag=='meta'and a.get('name')=='robots':self.noindex='noindex'in a.get('content','')
for d,m in zip(data,manifest):
 original=(ROOT/d['slug']/'index.html').read_bytes()
 assert hashlib.sha256(original).hexdigest()==d['sourceHtmlSha256'],('Existing store page changed',d['slug'])
 source_text=flat(original.decode())
 target=ROOT/m['path'].strip('/')/'index.html';html=target.read_text();p=Page();p.feed(html)
 assert p.h1==1 and p.noindex,d['slug']
 assert d['name']in unescape(html),('Wrong store name',d['slug'])
 assert '../../'+d['slug']+'/'in p.hrefs,('Missing previous design link',d['slug'])
 for f in d['facts']:
  assert f['value']in source_text,('Imported fact is absent from source',d['slug'],f)
  assert f['value']in flat(html),('Fact was lost in new page',d['slug'],f)
 for url in d['sourceUrls']+[d['maps']]+([d['instagram']]if d['instagram']else[]):
  assert url in p.hrefs,('Lost source or contact link',d['slug'],url)
 assert '非公式'in html and '店舗未承認'in html and '実店舗・実商品'in html
 assert all(int(i['width'])>0 and int(i['height'])>0 and 'イメージ'in i['alt']for i in p.images)
 assert len(p.images)==5,(d['slug'],len(p.images))
 for img in p.images:
  path=(target.parent/img['src']).resolve();rel='/'+str(path.relative_to(ROOT))
  assert rel in credits,('Unattributed photo',rel)
  assert hashlib.sha256(path.read_bytes()).hexdigest()==credits[rel]['sha256'],('Photo source hash mismatch',rel)
 assert m['textContrast']>=7
font=json.loads((ROOT/'assets/atelier/font-sources.json').read_text())
assert hashlib.sha256((ROOT/'assets/atelier'/font['file']).read_bytes()).hexdigest()==font['sha256']
assert 'SIL OPEN FONT LICENSE'in(ROOT/'assets/atelier'/font['licenseFile']).read_text()
gallery=(ROOT/'atelier/index.html').read_text()
assert gallery.count('class="gallery-card"')==100
for m in manifest:assert 'href="'+m['slug']+'/"'in gallery
print('PASS: 100 new routes, original page hashes, copied store facts, contact/source links, photo provenance, licensed font and gallery')
