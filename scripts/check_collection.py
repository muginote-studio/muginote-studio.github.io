#!/usr/bin/env python3
"""Keep the static gallery, route manifest and assets in agreement."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse
import json,re
ROOT=Path(__file__).resolve().parents[1]
rows=json.loads((ROOT/'collections/index.json').read_text())
class Gallery(HTMLParser):
 def __init__(self):super().__init__();self.cards=[];self.options=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='a' and 'gallery-card'in a.get('class','').split():self.cards.append(a)
  if tag=='option':self.options.append(a.get('value'))
g=Gallery();html=(ROOT/'index.html').read_text();g.feed(html)
assert rows and len(rows)==len(g.cards),'gallery entry count'
assert len({r['id']for r in rows})==len(rows),'duplicate ID'
assert len({r['path']for r in rows})==len(rows),'duplicate route'
for r,c in zip(rows,g.cards):
 assert c['data-store-id']==r['id'],'card ID'
 assert c['href']=='/'+r['slug']+'/'or c['href']==r['slug']+'/','card route'
 assert c['data-category']==r['category'],'card category'
 assert c['data-region']==r['region'],'card region'
 assert r['region']in g.options,'region filter option'
 assert r['name']in c['data-search'],'search includes store name'
 assert (ROOT/r['slug']/'index.html').is_file(),'route has no index'
 assert(ROOT/r['thumbnail'].lstrip('/')).is_file(),'missing thumbnail'
 assert 'hidden'not in c,'static gallery must work without JavaScript'
 assert r['category']in {'tea','sweets','coffee','meal','bar','bakery'},'category'
 assert r['thumbnailType']in {'illustration','image-photo'},'image label type'
 for url in r['sourceUrls']:assert urlparse(url).scheme=='https','source URL'
assert f'{len(rows)} DESIGN CONCEPTS'in html,'stale count'
for p in ROOT.glob('*/index.html'):
 assert not re.search(r'Online fetch throttled|the gaas-browser|relay could not open',p.read_text()),'internal tool error in page'
print(f'PASS: {len(rows)} gallery entries, unique routes, region filters and available thumbnails')
