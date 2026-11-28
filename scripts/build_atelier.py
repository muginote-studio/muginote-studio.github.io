#!/usr/bin/env python3
"""Build a parallel Uff-inspired edition without rewriting existing store pages."""
from pathlib import Path
from html import escape
from urllib.parse import urlparse
from PIL import Image
import json,re,hashlib

ROOT=Path(__file__).resolve().parents[1]
DATA=json.loads((ROOT/'assets/atelier/content.json').read_text())
OUT=ROOT/'atelier'
LABELS={'tea':'お茶と喫茶','coffee':'コーヒーと喫茶','sweets':'お菓子と喫茶','meal':'ごはんとカフェ','bar':'カフェとバル','bakery':'パンとカフェ'}
ENGLISH={'tea':'TEA & A LITTLE REST','coffee':'COFFEE & A LITTLE REST','sweets':'SWEETS & LITTLE JOYS','meal':'FOOD & COFFEE','bar':'CAFE & BAR','bakery':'BREAD & COFFEE'}
PHOTO_SETS={
 'tea':['/assets/tea.webp','/assets/cookies.webp','/assets/batch-c/photos/bread.webp','/assets/latte.webp'],
 'coffee':['/assets/coffee.webp','/assets/latte.webp','/assets/cookies.webp','/assets/interior.webp'],
 'sweets':['/assets/icecream.webp','/assets/cookies.webp','/assets/tea.webp','/assets/latte.webp'],
 'meal':['/assets/sandwich.webp','/assets/toast.webp','/assets/latte.webp','/assets/interior.webp'],
 'bar':['/assets/wine.webp','/assets/table.webp','/assets/coffee.webp','/assets/sandwich.webp'],
 'bakery':['/uff/assets/hero.webp','/uff/assets/bread.webp','/uff/assets/croissant.webp','/uff/assets/latte.webp']}
MOMENTS={'tea':('お茶の時間に、','小さな余白を。'),'coffee':('一杯ぶんの、','ひと休みを。'),'sweets':('甘い寄り道を、','今日の楽しみに。'),'meal':('ごはんの時間を、','ゆっくりと。'),'bar':('今日の余韻を、','もう少し。'),'bakery':('パンのある日を、','少し好きになる。')}
def e(s):return escape(str(s),quote=True)
def rgb(color):
 color=color.lstrip('#');return tuple(int(color[i:i+2],16)for i in (0,2,4))
def hx(c):return '#'+''.join(f'{round(v):02x}'for v in c)
def mix(a,b,t):return tuple(x*(1-t)+y*t for x,y in zip(a,b))
def lum(c):
 vals=[v/255 for v in c];return sum((v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4)*w for v,w in zip(vals,[.2126,.7152,.0722]))
def contrast(a,b):return (max(lum(a),lum(b))+.05)/(min(lum(a),lum(b))+.05)
def theme(d):
 colors=[rgb(c)for c in d.get('palette',[])if re.fullmatch(r'#[0-9a-fA-F]{6}',c)]
 if not colors:
  css=(ROOT/'assets/site.css').read_text();match=re.search(r'\.theme-'+re.escape(d['slug'].split('-')[0])+r'\{([^}]+)',css)
  if match:colors=[rgb(x)for x in re.findall(r'#[0-9a-fA-F]{6}',match.group(1))]
 if not colors:colors=[rgb('#f7f6ef'),rgb('#344c3b'),rgb('#71816b')]
 ink=min(colors,key=lum);paper=max(colors,key=lum)
 if lum(paper)<.7:paper=mix(paper,(255,255,255),.86)
 if lum(ink)>.15:ink=mix(ink,(18,24,20),.6)
 while contrast(ink,paper)<7:ink=mix(ink,(15,18,16),.1)
 soft=mix(paper,ink,.075);line=mix(paper,ink,.22)
 return {'paper':hx(paper),'ink':hx(ink),'soft':hx(soft),'line':hx(line),'contrast':round(contrast(ink,paper),2)}
def photo(path,classes='',priority=False):
 f=ROOT/path.lstrip('/')
 with Image.open(f)as im:w,h=im.size
 src='../../'+path.lstrip('/')
 return f'<figure class="{classes}"><img src="{src}" width="{w}" height="{h}" alt="イメージ写真。実際の店舗・商品とは異なります。" '+('fetchpriority="high"'if priority else'loading="lazy"')+' decoding="async"><figcaption class="image-label">イメージ写真</figcaption></figure>'
FLOWER='<svg viewBox="0 0 32 32" width="32" height="32" aria-hidden="true" focusable="false"><path d="M16 3v26M3 16h26M7 7l18 18M7 25L25 7" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>'
CUP='<svg viewBox="0 0 80 60" width="80" height="60" aria-hidden="true" focusable="false"><g fill="none" stroke="currentColor" stroke-width="1.3"><path d="M19 19h35v13c0 20-35 20-35 0ZM54 22h6c13 0 11 16-6 16M12 51h53M29 13c-7-7 7-8 0-15M43 13c-7-7 7-8 0-15"/></g></svg>'
def ext(url,label,cls='text-link'):
 return f'<a class="{cls}" href="{e(url)}" target="_blank" rel="noopener noreferrer nofollow">{e(label)}</a>'
def heading(text):
 escaped=e(text)
 if '、'in text:return escaped.replace('、','、<br>',1)
 if '。'in text.rstrip('。'):return escaped.replace('。','。<br>',1)
 return escaped

manifest=[]
for index,d in enumerate(DATA):
 slug=d['slug'];name=e(d['name']);category=d['category'];t=theme(d)
 paths=PHOTO_SETS[category].copy()
 originals=d['existingPhotos']
 if originals:paths=[originals[0]]+[p for p in paths if p!=originals[0]]
 if slug=='uff':paths=['/uff/assets/hero.webp','/uff/assets/bread.webp','/uff/assets/croissant.webp','/uff/assets/latte.webp']
 # Keep every picture slot distinct, reusing attributed repository assets.
 unique=[];seen=set()
 for path in paths+PHOTO_SETS['coffee']:
  digest=hashlib.sha256((ROOT/path.lstrip('/')).read_bytes()).hexdigest()
  if digest not in seen:unique.append(path);seen.add(digest)
  if len(unique)==4:break
 paths=unique
 hero_photo=photo(paths[0],'hero-photo',True)
 signature=d['name']
 if len(signature)>24:signature=ENGLISH[category].title()
 p=d['place'];old='../../'+slug+'/'
 action=d['instagram'] or d['sourceUrls'][0]
 action_label='お店のInstagramを見る'if d['instagram']else'お店の紹介記事を見る'
 story=''.join(f'<p class="body-copy">{e(v)}</p>'for v in d['story'])
 features=d['features'][:2]
 if len(features)<2:features=features+[{'title':'訪れる前に','text':'営業日やメニューは、お店の最新の案内をご確認ください。'}]
 picks=''
 for i,f in enumerate(features):
  picks+=f'<article class="pick">{photo(paths[i+2],"pick-photo")}<p class="pick-category">{ENGLISH[category]}</p><h3>{e(f["title"])}</h3><p class="body-copy">{e(f["text"])}</p></article>'
 extra=''
 if len(d['features'])>2:
  f=d['features'][2];extra=f'<div class="extra-feature"><h3>{e(f["title"])}</h3><p>{e(f["text"])}</p></div>'
 fact_rows=''.join(f'<div><dt>{e(f["label"])}</dt><dd>{e(f["value"])}</dd></div>'for f in d['facts'])
 source_rows=''.join(f'<li>{ext(url,"店舗情報の出典 "+str(i+1),"")}<small>{e(urlparse(url).netloc)}</small></li>'for i,url in enumerate(d['sourceUrls']))
 moment=MOMENTS[category]
 style=';'.join('--'+k+':'+t[k]for k in ['paper','ink','soft','line'])
 html=f'''<!doctype html>
<html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><meta name="theme-color" content="{t['ink']}"><title>{name}｜{e(d['headline'])}｜デザイン案</title><meta name="description" content="{e(d['summary'])} 非公式のデザイン提案です。"><link rel="stylesheet" href="../../assets/atelier/site.css"><script src="../../assets/atelier/site.js" defer></script></head>
<body style="{style}"><a class="skip" href="#main">本文へスキップ</a><div class="concept-note"><span>自主制作の非公式デザイン案 / 店舗未承認</span><a href="{old}">前の版を見る</a></div>
<header class="site-header"><a class="brand" href="#top"><span class="brand-name">{name}</span><span class="brand-sub">{ENGLISH[category]}</span></a><button class="menu-toggle" type="button" aria-label="メニューを開く" aria-expanded="false" aria-controls="navigation"><span></span><span></span></button><nav class="site-nav" id="navigation" aria-label="メインナビゲーション"><a href="#about">お店のこと</a><a href="#discover">ひと息の楽しみ</a><a href="#visit">お店への道のり</a>{ext(action,'Instagram'if d['instagram']else'お店の案内','nav-social')}</nav></header>
<main id="main"><section class="hero" id="top" aria-labelledby="hero-title"><div class="hero-copy"><p class="eyebrow"><span class="flower">{FLOWER}</span>{e(p)} / {LABELS[category]}</p><h1 id="hero-title">{heading(d['headline'])}</h1><p class="hero-description">{e(d['heroIntro'])}</p><a class="text-link" href="#discover">ひと息の楽しみをのぞく</a><div class="hero-bottom"><span>{ENGLISH[category]}<br>A LITTLE MOMENT FOR YOU.</span><a href="#about">SCROLL</a></div></div><div class="hero-photo">{hero_photo.replace('class="hero-photo"','class="hero-photo-inner"')}<div class="hero-seal"><span>A LITTLE MOMENT</span>{CUP}<span>{'TEA & CAFE'if category=='tea'else'LOCAL CAFE'}</span></div><p class="hero-signature" aria-hidden="true">{e(signature)}</p></div></section>
<div class="opening-strip"><span class="strip-title">A little pause, a little joy.</span><p>{name}</p><span class="strip-note">{LABELS[category]}</span></div>
<section class="story wrap" id="about" aria-labelledby="about-title"><div class="story-visual">{photo(paths[1],'story-photo')}<p class="handwritten" aria-hidden="true">A small place,<br>a little happiness.</p></div><div class="story-copy"><p class="eyebrow">ABOUT THE PLACE</p><h2 id="about-title">{heading(d['aboutHeading'])}</h2>{story}{ext(action,action_label)}</div></section>
<section class="picks" id="discover" aria-labelledby="discover-title"><div class="wrap"><div class="section-heading"><div><p class="eyebrow">A LITTLE DISCOVERY</p><h2 id="discover-title">日々の途中の、<br>小さな楽しみ。</h2></div><p class="heading-note">公開記事で紹介されている、<br>お店を知るための小さな手がかり。</p></div><div class="picks-grid">{picks}</div>{extra}<div class="picks-note"><p>掲載内容は出典の掲載時点の情報です。写真はイメージで、現在の提供メニュー・商品を示すものではありません。</p>{ext(action,'最新の案内を見る')}</div></div></section>
<section class="moment wrap" aria-labelledby="moment-title"><span class="flower">{FLOWER}</span><p class="eyebrow">TAKE A LITTLE BREAK.</p><h2 id="moment-title">{e(moment[0])}<br>{e(moment[1])}</h2><p>ふと気になる一軒を、<br>今日の寄り道の候補に。</p><span class="moment-line" aria-hidden="true"></span><p class="moment-english" aria-hidden="true">Stay for a little while.</p></section>
<section class="visit" id="visit" aria-labelledby="visit-title"><div class="visit-inner wrap"><div class="visit-info"><p class="eyebrow">COME SAY HELLO</p><h2 id="visit-title">{e(p)}で、<br>ひと息の時間を。</h2><p class="visit-name">{name}</p><dl>{fact_rows}</dl><p class="visit-small">店舗情報は公開資料の掲載時点のものです。現在の営業日・営業時間・提供内容は、訪問前にお店の案内でご確認ください。</p><div class="visit-actions">{ext(d['maps'],'Google マップで場所を見る','solid-link')}{ext(action,action_label,'solid-link outline-link')}</div></div><div class="visit-visual">{photo(paths[1],'visit-image')}<p class="visit-signature" aria-hidden="true">A place to pause.</p><p class="eyebrow">{e(p)} / {LABELS[category]}</p></div></div></section></main>
<footer class="site-footer"><div class="footer-main"><a class="footer-name" href="#top">{name}</a><p class="footer-tagline">A little joy.<br>A little time for you.</p>{ext(action,'Instagram'if d['instagram']else'お店の紹介を見る')}</div><div class="footer-bottom"><span>{name} / Design proposal</span><a href="#top">ページ上部へ</a></div><div class="disclosure" id="sources"><p>muginote studioによる自主制作の非公式デザイン案です。店舗の依頼・承認を受けた公式サイトではありません。</p><p>写真はすべてイメージ素材です。実店舗・実商品・器とは異なります。価格の保証、予約・注文の受付は行っていません。</p><details><summary>店舗情報と写真の出典</summary><ul class="sources-list">{source_rows}<li>写真：既存提案に使用したUnsplashのイメージ素材。<a href="../../assets/atelier/photo-sources.json">写真の出典一覧</a> ／ <a href="https://unsplash.com/license" target="_blank" rel="noopener noreferrer">利用条件</a></li></ul><p>今回の制作では、以前の提案に記録した店舗情報と配色資料を引き継いでいます。Instagramの新しい投稿や最新の営業予定を確認したものではありません。</p></details><div class="version-links"><a href="../">今回のデザイン一覧</a><a href="{old}">このお店の前の版</a><a href="../../">これまでのデザイン一覧</a></div></div></footer></body></html>
'''
 dest=OUT/slug;dest.mkdir(parents=True,exist_ok=True);(dest/'index.html').write_text(html)
 manifest.append({**{k:d[k]for k in ['id','slug','name','region','place','category','sourceUrls']},'path':'/atelier/'+slug+'/','previousPath':'/'+slug+'/','thumbnail':paths[0],'palette':[t['paper'],t['ink'],t['soft']],'textContrast':t['contrast'],'templateReference':'/uff/','font':'Self-hosted Noto Serif JP and Cormorant Garamond; system sans-serif for body text.'})

options=''.join(f'<option value="{e(region)}">{e(region)}</option>'for region in dict.fromkeys(d['region']for d in DATA))
filters='<button type="button" data-filter="all" aria-pressed="true">すべて</button>'+''.join(f'<button type="button" data-filter="{k}" aria-pressed="false">{v}</button>'for k,v in LABELS.items())
cards=''
for d in manifest:
 path=ROOT/d['thumbnail'].lstrip('/')
 with Image.open(path)as im:w,h=im.size
 palette=''.join(f'<span style="background:{c}"></span>'for c in d['palette'])
 cards+=f'''<a class="gallery-card" href="{d['slug']}/" data-store-id="{d['id']}" data-region="{e(d['region'])}" data-category="{d['category']}" data-search="{e(d['name']+' '+d['place']+' '+d['region']+' '+LABELS[d['category']]+' '+d['slug'])}"><div class="gallery-image"><img src="../{d['thumbnail'].lstrip('/')}" width="{w}" height="{h}" loading="lazy" decoding="async" alt="{e(d['name'])}のデザインに使用したイメージ写真。実店舗の写真ではありません。"><span>イメージ写真</span></div><div class="card-info"><p>{e(d['place'])} / {LABELS[d['category']]}</p><h2>{e(d['name'])}</h2><span class="card-cta">デザインを見る</span><div class="card-palette" aria-hidden="true">{palette}</div></div></a>'''
gallery=f'''<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>Atelier Collection｜muginote studio カフェのデザイン提案</title><meta name="description" content="写真と余白、やわらかな文字で紹介する全国100店舗の非公式Webデザイン提案。以前のデザインと比較できます。"><link rel="stylesheet" href="../assets/atelier/site.css"><script src="../assets/collection.js" defer></script></head><body class="atelier-gallery"><a class="skip" href="#main">本文へスキップ</a><header class="gallery-header"><a class="studio" href="../">muginote studio</a><nav aria-label="コレクション"><a href="../">これまでのデザイン</a><a href="#gallery-results">今回の100店舗</a></nav></header><main class="gallery-main" id="main"><section class="gallery-intro"><p class="eyebrow">ATELIER COLLECTION / CAFE WEBSITES</p><h1>一杯の時間を、<br>美しく。</h1><p class="body-copy">写真と余白、やわらかな文字。<br>それぞれの街で見つけた、小さなお店のデザイン集です。<br>気になる一軒から、ゆっくりご覧ください。</p><span class="collection-count">100 DESIGN CONCEPTS / 47 PREFECTURES</span><span class="edition-word" aria-hidden="true">Atelier.</span></section><section class="gallery-controls" aria-label="デザインを探す" hidden><form id="collection-search" role="search"><div class="search-field"><label for="shop-search">店名・地域で探す</label><input id="shop-search" type="search" placeholder="例：京都、コーヒー、mico" autocomplete="off" aria-controls="gallery-results"></div><div class="region-field"><label for="region-filter">都道府県</label><select id="region-filter" aria-controls="gallery-results"><option value="all">すべての地域</option>{options}</select></div></form><div class="category-filters" role="group" aria-label="お店の種類">{filters}</div><div class="filter-summary"><p id="filter-status" aria-live="polite">100件 / 100件のデザイン</p><button type="button" id="clear-filters">条件をリセット</button></div></section><p id="gallery-empty" class="gallery-empty" hidden>一致するデザインがありません。条件を変えてみてください。</p><section class="gallery-grid" id="gallery-results" aria-label="店舗のデザイン一覧">{cards}</section><section class="gallery-note" aria-label="このコレクションについて"><p>すべてmuginote studioによる自主制作の非公式デザイン案です。店舗の承認・依頼を受けた公式サイトではありません。写真はイメージ素材で、実店舗・実商品とは異なります。</p><p><a href="../">これまでのデザイン一覧</a> ／ <a href="../archive/batch-a-v1/">担当Aの初版アーカイブ</a></p></section></main><footer class="gallery-footer"><span>muginote studio / Atelier Collection</span><a href="#main">ページ上部へ</a></footer></body></html>'''
(OUT/'index.html').write_text(gallery)
(ROOT/'collections/atelier.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(f'Built {len(manifest)} new store pages and their gallery. Minimum text contrast: {min(d["textContrast"]for d in manifest)}:1')
