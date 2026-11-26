#!/usr/bin/env python3
"""Validate the isolated Batch A deliverable using only the standard library."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote
import json, re, hashlib, subprocess
ROOT = Path(__file__).resolve().parents[2]
BATCH = ROOT / 'assets/batch-a'
rows = json.loads((ROOT / 'collections/batch-a.json').read_text())
research = json.loads((BATCH / 'research.json').read_text())
errors = []
def check(ok, message):
    if not ok: errors.append(message)
class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.tags=[]; self.ids=[]; self.refs=[]; self.h1=0; self.images=[]
    def handle_starttag(self, tag, attrs):
        a=dict(attrs); self.tags.append((tag,a))
        if tag=='h1': self.h1+=1
        if a.get('id'): self.ids.append(a['id'])
        if tag=='img': self.images.append(a)
        if tag=='a' and a.get('target')=='_blank':
            check({'noopener','noreferrer','nofollow'} <= set(a.get('rel','').split()), 'external link rel')
        if tag=='svg':
            check(a.get('aria-hidden')=='true' and a.get('focusable')=='false','SVG accessibility')
            check(all(a.get(x) for x in ['viewbox','width','height']), 'SVG dimensions')
            check(a.get('stroke')=='currentColor','SVG currentColor')
        for key in ('href','src'):
            if key in a:self.refs.append(a[key])
check(len(rows)==30,'30 manifest entries')
check([x['id'] for x in rows]==[f'CAFE-{i:03d}' for i in range(11,41)],'ID coverage/order')
check(len({x['path'] for x in rows})==30,'unique paths')
check(len(research)==30,'30 research entries')
check(len({x['layout'] for x in research})>=10,'layout diversity')
required={'id','slug','path','name','region','category','thumbnail','summary','palette','sourceUrls','designReferenceUrls','referenceNotes'}
urls=set()
for row in rows:
    slug=row['slug'];path=ROOT/slug/'index.html';t=path.read_text();p=Page();p.feed(t)
    check(required<=row.keys(),slug+': manifest schema')
    check(row['path']=='/'+slug+'/',slug+': route')
    check(row['category'] in ['tea','sweets','coffee','meal','bar','bakery'],slug+': category')
    check((ROOT/row['thumbnail'].lstrip('/')).is_file(),slug+': thumbnail')
    check(p.h1==1,slug+': one h1')
    check(any(tag=='h1' and a.get('aria-label')==row['name'] for tag,a in p.tags),slug+': accessible store name')
    check(len(p.ids)==len(set(p.ids)),slug+': unique IDs')
    check(any(tag=='meta' and a.get('name')=='robots' and a.get('content')=='noindex,nofollow' for tag,a in p.tags),slug+': robots')
    check('自主制作の非公式デザイン案 / 店舗未承認' in t,slug+': disclosure')
    check('実店舗・実商品とは異なります' in t,slug+': illustrative label')
    check(len(p.images)==2,slug+': two photographs')
    check('メニュー' in t and 'aria-controls="site-nav"' in t,slug+': mobile menu contract')
    check(not re.search(r'\b(?:mailto|tel):',t),slug+': no speculative contact CTA')
    check(not re.search(r'<(?:form|iframe)\b',t),slug+': no fake form or third-party embed')
    check(not re.search(r'docs\.google\.com/spreadsheets|link_6a|github_pat_|ghp_|@gmail\.com',t),slug+': no internal data')
    for ref in p.refs:
        u=urlparse(ref)
        if u.scheme:
            check(u.scheme=='https',slug+': HTTPS link');urls.add(ref);continue
        if ref.startswith('#'):check(ref[1:] in p.ids,slug+': anchor '+ref);continue
        local=(path.parent/unquote(u.path)).resolve()
        check(local.is_relative_to(ROOT) and local.exists(),slug+': resource '+ref)
        if local.suffix=='.webp':check(local.read_bytes()[:4]==b'RIFF' and local.read_bytes()[8:12]==b'WEBP',slug+': WebP header')
    for im in p.images:
        check(bool(im.get('alt')),slug+': alt')
        check(int(im['width'])>0 and int(im['height'])>0,slug+': dimensions')
for photo in json.loads((BATCH/'image-sources.json').read_text()):
    check(hashlib.sha256((BATCH/photo['file']).read_bytes()).hexdigest()==photo['sha256'],'photo integrity '+photo['file'])
    check(photo['license']=='Unsplash License' and photo['licenseUrl']=='https://unsplash.com/license','photo license')
css=(BATCH/'site.css').read_text()
check('@media(max-width:680px)' in css and 'overflow-wrap:anywhere' in css,'narrow layout guards')
# CSS references are not covered by the repository HTML link checker.
for raw in re.findall(r"url\(\s*['\"]?([^'\")\s]+)",css):
    if urlparse(raw).scheme: continue
    target=(BATCH/unquote(raw)).resolve()
    check(target.is_relative_to(ROOT) and target.is_file(),'CSS resource '+raw)
font_records=json.loads((BATCH/'font-sources.json').read_text())
check(len(font_records)==5,'five self-hosted fonts')
for font in font_records:
    file=BATCH/font['file']
    check(file.is_file() and file.read_bytes()[:4]==b'wOF2','WOFF2 header '+font['file'])
    check(hashlib.sha256(file.read_bytes()).hexdigest()==font['sha256'],'font integrity '+font['file'])
    check(font['license']=='SIL Open Font License 1.1','font license '+font['file'])
    check((file.parent/(file.stem+'-OFL.txt')).is_file(),'bundled OFL '+font['file'])

check('prefers-reduced-motion:reduce' in css,'reduced motion')
check('.enhanced .site-header nav[hidden]' in css,'menu hidden state')
# WCAG relative luminance; all normal content colors must remain readable.
def luminance(h):
    c=[int(h[i:i+2],16)/255 for i in (1,3,5)]
    c=[x/12.92 if x<=.04045 else ((x+.055)/1.055)**2.4 for x in c]
    return sum(v*w for v,w in zip(c,[.2126,.7152,.0722]))
def contrast(a,b):
    x,y=sorted([luminance(a),luminance(b)]);return (y+.05)/(x+.05)
contrasts=[]
for row in rows:
    bg,ink,accent,soft=row['palette']
    values={k:round(contrast(a,b),2) for k,a,b in [('ink/paper',ink,bg),('ink/soft',ink,soft),('accent/paper',accent,bg)]}
    check(min(values.values())>=4.5,row['slug']+': text contrast '+str(values))
    contrasts.append({'id':row['id'],**values})
if errors:
    print('\n'.join(errors));raise SystemExit(1)
print(json.dumps({'result':'PASS','pages':len(rows),'layouts':len({x['layout'] for x in research}),'localPhotos':len(list((BATCH/'images').glob('*.webp'))),'localFonts':len(font_records),'uniqueExternalUrls':len(urls),'contrastMinimum':min(min(v for k,v in r.items() if k!='id') for r in contrasts),'contrast':contrasts},ensure_ascii=False,indent=2))
