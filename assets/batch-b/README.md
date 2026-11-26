# Batch B: 30 café design studies

CAFE-041〜CAFE-070の非公式トップページ。自主制作・店舗未承認。全ページに `noindex,nofollow` を設定。店舗写真・ロゴは転載していません。

30ページは10種類の構成を基に、店別の配色・文字組み・原稿・自主制作SVGを設定しています。店舗情報は2026年11月26日に公開ページへアクセスして照合しました。Instagramは28店で公開プロフィール名とプロフィール画像を確認できましたが、投稿一覧・本文・最新営業カレンダーは確認できていません。カフェ花とCampanellaは公式Instagramを特定できていません。

## ファイル

- `collections/batch-b.json`: 一覧統合用配列。共通一覧は未変更。
- 各店舗ルートの `index.html` と `design.css`。
- `assets/batch-b/design-system.css` と `navigation.js`: 担当B専用。
- 同ディレクトリの30個のSVG: 自主制作図形。実店舗・実商品の再現ではありません。
- 8個のWebP: 既存リポジトリのUnsplash素材を担当専用ディレクトリに複製。
- `photo-credits.json`: 写真の正確な取得元URL・ライセンスURL。
- `provenance.json`: 30店の配色根拠・出典・確認できなかった点。
- `routes.txt`: ID、指定ルート、店舗名。

## 写真の扱い

参考の店舗写真は配色・質感の観察だけに使用し、ページ・納品ZIPに転載していません。掲載写真は実店舗・実商品と異なるイメージ写真で、各写真の近くとフッターに表示しています。[Unsplash License](https://unsplash.com/license)の利用条件を2026年11月26日に確認しました。写真家名は未確認のため推測せず、正確な画像URLを `photo-credits.json` と各ページに記録しています。SVGはこのデザイン案のための自主制作です。

## 検証

- `python3 scripts/check_presentation.py`: 既存を含む41ページがPASS。
- `node --check assets/batch-b/navigation.js`: PASS。
- 全30ID・指定ルート・画像デコード・ローカル参照・アンカー・h1・SVGアクセシビリティ・JSON項目・非公式表示・noindexを静的検証。
- 使用する文字色のコントラスト比は最低4.62:1。
- JavaScriptに依存せず本文・出典・通常ナビゲーションを表示。モバイルメニューはJSで拡張。
- 76個の出典URLへの取得がHTTP 200。ただしInstagram本文はログイン画面であり、投稿確認済みという意味ではありません。
- 既存追跡ファイルへの変更なし。担当Bの店舗・アセット・一覧データのみ追加。

ブラウザ目視確認は未実施です。管理プレビューのrelayがport 4173でタイムアウトし、CUA初期化も失敗しました。CSSには700px以下の1列構成・文字折返し・幅制約を実装していますが、390px端末、デスクトップ、Safari/WebKitでの実表示・メニュー操作・写真クロップの目視確認は必要です。JavaScriptは構文・実装の静的確認のみです。

価格・口コミ・店名由来・未検証の連絡先は掲載していません。営業時間は出典付きの掲載情報として扱い、資料間の差・移転・開店前の古い記述は各店ページに明記しています。現行メニュー・在庫・臨時営業の保証はしていません。

## ルートと配色参考

| ID | 店舗・ルート | 配色 | 参考資料と判断 |
| --- | --- | --- | --- |
| CAFE-041 | mico `/mico/` | #f0f1eb / #25332c / #466651 / #d7ded3 | Instagramプロフィール画像の銀色の立体文字と白地、食べログの銀のトレー・深緑の器を参照。白とグレーを基調に、料理写真の緑を補助色へ。 [資料1](https://tabelog.com/ishikawa/A1702/A170201/17016227/) / [資料2](https://www.instagram.com/mico.kagaonsen/) |
| CAFE-042 | 喫茶コビト `/kissa-kobito/` | #f5f0e5 / #49302a / #7b3e31 / #e3d7c2 | Instagramの赤茶の縦組みロゴ、こまつ観光ナビの喫茶コビト写真の木製家具と白壁を参照。縦の文字組みと暖かい木肌色。 [資料1](https://tabelog.com/ishikawa/A1702/A170202/17016089/) / [資料2](https://www.komatsuguide.jp/feature/detail_267.html) / [資料3](https://www.instagram.com/kissa.kobito) |
| CAFE-043 | our `/our/` | #f8f5ec / #242b30 / #245d89 / #ecd37d | Instagramプロフィールの青・黄・オレンジの抽象形と、食べログの木目・白いカップを参照。青い文字と切り紙状の図形で構成。久米繊維の記事写真は衣類中心のため店内配色とは扱わない。 [資料1](https://tabelog.com/fukui/A1801/A180102/18010855/) / [資料2](https://kume.jp/2026/10/261006/) / [資料3](https://www.instagram.com/our_fukui) |
| CAFE-044 | カフェ花 `/cafe-hana/` | #f3ecdb / #392d26 / #695334 / #ddd0ad | 食べログのモーニング写真の飴色の卓と黒い器を参照。ふーぽの複数店記事の先頭画像はいなり寿司で別店のため、花の配色根拠から除外。落ち着いた茶と紙色の額縁構成。 [資料1](https://tabelog.com/fukui/A1802/A180202/18001833/) / [資料2](https://fupo.jp/article/newopen_202610-2/) |
| CAFE-045 | 3POZZO cafe `/3pozzo-cafe/` | #f4f5e8 / #163f41 / #207983 / #dfc78f | Instagramプロフィールのターコイズと白い輪郭、PORTAの青緑の皿・木の卓を参照。丸い縁とアーチで柔らかい構成。 [資料1](https://tabelog.com/yamanashi/A1903/A190302/19015032/) / [資料2](https://www.porta-y.jp/gourmet/3581420) / [資料3](https://www.instagram.com/3pozzo_cafe) |
| CAFE-046 | cohaccha `/cohaccha/` | #fbf4e8 / #3d3525 / #58704c / #e7c99b | Instagramプロフィール画像の木製サインと黒い筆記体、食べログの白い花柄の皿と木の卓を参照。紙のメニュー帳のような構成。 [資料1](https://tabelog.com/yamanashi/A1901/A190101/19015055/) / [資料2](https://www.instagram.com/coha_showa/) |
| CAFE-047 | 古民家カフェ 温 `/kominka-onn/` | #f0ebdb / #302e24 / #2d706c / #d5be85 | Instagramプロフィールの黒い円と稲穂、PORTAの木の卓・深い色の器、食べログの青緑のカップを参照。縦組みと墨色の罫線。 [資料1](https://tabelog.com/yamanashi/A1901/A190101/19014998/) / [資料2](https://www.porta-y.jp/porta-press/press-vt2y1x3r) / [資料3](https://www.instagram.com/onn.cafe/) |
| CAFE-048 | LAVENDER LANE Tea Room `/lavender-lane/` | #f8f3f8 / #492c5d / #72458f / #e5d8e7 | Instagramの紫のティーポットのプロフィール画像と、食べログのティースタンド・白い茶器を参照。紫の細い枠線と欧文セリフ。紹介記事の先頭道路写真は配色根拠から除外。 [資料1](https://tabelog.com/nagano/A2001/A200101/20029892/) / [資料2](https://naganogourmetbekkan.net/lavenderlane/) / [資料3](https://www.instagram.com/lavenderlane_tearoom/) |
| CAFE-049 | カフェみなも `/cafe-minamo/` | #f3f2ed / #3c4546 / #526e72 / #d9dedd | Instagramプロフィールの濃いグレーの曲線、Web-Komachiの淡い暖簾とグレーの外観、食べログの白皿を参照。水面状の線は自主制作で、店名由来の説明ではない。 [資料1](https://tabelog.com/nagano/A2002/A200201/20030009/) / [資料2](https://www.web-komachi.com/?p=307955) / [資料3](https://www.instagram.com/minamo_cafe) |
| CAFE-050 | anew egg sandwich & cafe `/anew/` | #fff5db / #4c351c / #885421 / #f0bf55 | Instagramのたまごサンドのイラスト、クリーム色の地と茶色の文字、食べログの商品写真の黄色を参照。黄・茶の大きな文字とサンド状の層。 [資料1](https://tabelog.com/gifu/A2101/A210102/21025137/) / [資料2](https://www.instagram.com/anew_kakamigaha/) |
| CAFE-051 | Campanella `/campanella/` | #eae6d7 / #223936 / #2e5d59 / #c5ab62 | 食べログの青緑と金彩の皿、木目の卓、ラテの写真を参照。深い青緑と真鍮色の細線、雑誌のような段組み。公式Instagramは未特定。 [資料1](https://tabelog.com/gifu/A2101/A210101/21025076/) / [資料2](https://kaiten-heiten.com/%E3%80%90%E9%96%8B%E5%BA%97%E3%80%91cafe-campanella/) |
| CAFE-052 | Cafe R･Dreams `/r-dreams/` | #f7efde / #503a2a / #855d36 / #dfc296 | Instagramプロフィールの木の看板と白いカップ、食べログのタイルの外観を参照。木色と白い線の手帳構成。店舗内部と投稿写真の全体傾向は未確認。 [資料1](https://tabelog.com/shizuoka/A2205/A220503/22046681/) / [資料2](https://www.ekiten.jp/shop_15483094/) / [資料3](https://www.instagram.com/r.dreams1219) |
| CAFE-053 | BLOSSOM COFFEE HOUSE `/blossom-coffee-house/` | #e9e7e5 / #202021 / #9d1557 / #e7c4d3 | Instagramプロフィール画像の黒地・鮮やかなピンク、食べログの商品写真のコンクリートグレーを参照。太い欧文とピンクの面。実際のブランドロゴは複製しない。 [資料1](https://tabelog.com/aichi/A2301/A230105/23098267/) / [資料2](https://www.instagram.com/blossom.nagoya/) |
| CAFE-054 | Jinryo Coffee `/jinryo-coffee/` | #f5eee2 / #44362b / #47654c / #d6c5a3 | Instagramプロフィールの茶色の抽象カップ、食べログの木のトレーと青緑の皿を参照。松本珈琲工房の記事先頭の緑の外観は店舗同定できないため配色根拠に使わない。 [資料1](https://tabelog.com/aichi/A2303/A230301/23098304/) / [資料2](https://matsumoto-coffee.com/blog/seminar/2585/) / [資料3](https://www.instagram.com/jinryo_coffee/) |
| CAFE-055 | PATISSERIE & 喫茶 KIGI `/kigi/` | #eceddf / #203c31 / #4b6352 / #cbb58d | Instagramプロフィールの深い緑地と白いセリフ体、食べログの縦長パフェと灰紫の背景を参照。緑の見開き、縦長の図形と欧文セリフ。 [資料1](https://tabelog.com/aichi/A2301/A230112/23098019/) / [資料2](https://www.instagram.com/kigi_kissa/) |
| CAFE-056 | ルネル洋菓子店 `/renelle/` | #f8f5f1 / #3c4244 / #606e7d / #e8ddd1 | Instagramの白地と細い黒い筆記体、食べログの青い背景・白いクリーム・黒皿を参照。白い展示室のような余白と青灰色の文字。 [資料1](https://tabelog.com/aichi/A2301/A230113/23098295/) / [資料2](https://www.instagram.com/renelle_yougashiten/) |
| CAFE-057 | 7uts `/7uts/` | #f1eddf / #252f63 / #334197 / #e3c33a | Instagramプロフィールの丸い青い文字、号外NETの木の棚・青文字のクッション・黄色やオレンジのランプを参照。太い文字と丸い面を重ねたポスター構成。 [資料1](https://tabelog.com/mie/A2402/A240202/24022804/) / [資料2](https://suzuka-kameyama.goguynet.jp/2026/09/14/7uts/) / [資料3](https://www.instagram.com/7uts_coffee_mie) |
| CAFE-058 | riverside cafe ＆ sleep `/riverside-cafe-sleep/` | #e6efea / #263f38 / #46695e / #acd0c8 | Instagramプロフィールの淡い青緑と茶の輪、紹介記事の木の建物と緑、食べログの青いカップを参照。横に広い構成と川のような線。 [資料1](https://tabelog.com/mie/A2404/A240402/24022885/) / [資料2](https://mycmyc.blog.fc2.com/blog-entry-3402.html) / [資料3](https://www.instagram.com/riversidecafe.sleep) |
| CAFE-059 | カフェとごはん ひだまり `/hidamari/` | #fff7e1 / #463b26 / #856524 / #ecd37f | Instagramプロフィールの黄色の円と手書き文字、食べログ・滋賀つーしんの御膳の木色と白い器を参照。黄色の余白と献立帳のような罫線。 [資料1](https://tabelog.com/shiga/A2503/A250301/25014589/) / [資料2](https://shiga2.jp/hidamari-omihachiman-renewal-open/shiga2/) / [資料3](https://www.instagram.com/hidamari_cafebistro/) |
| CAFE-060 | 給食日和 `/kyushoku-biyori/` | #fff1d3 / #54382d / #a3412c / #e8b341 | Instagramプロフィールの黄色の円とえんじの縁、食べログの金属トレー・白い皿を参照。給食のトレーを抽象化した図形と明るい見出し。 [資料1](https://tabelog.com/shiga/A2501/A250101/25014660/) / [資料2](https://kokoiro.jp/shop/kyushokubiyori/) / [資料3](https://www.instagram.com/kyusyokubiyori/) |
| CAFE-061 | TOWZA DINER 1830 `/towza-diner/` | #fff0d8 / #652d25 / #b52d1d / #edc078 | Instagramプロフィールの鮮やかな赤と白い太字だけを直接確認。食べログの代表画像はNO PHOTOで、店内・商品写真は未確認。赤い活字を起点にした暫定デザイン。 [資料1](https://tabelog.com/kyoto/A2601/A260503/26046119/) / [資料2](https://www.instagram.com/towza_diner_1830) |
| CAFE-062 | DEL `/del/` | #fbf0d7 / #632820 / #a33327 / #e6c394 | Instagramプロフィールのクリーム色と赤い太字、食べログの赤いカップ印刷・木の卓を参照。切り紙状の赤い面と大きな活字。 [資料1](https://tabelog.com/osaka/A2701/A270201/27159757/) / [資料2](https://www.instagram.com/del_southhorie) |
| CAFE-063 | LOAFF `/loaff/` | #f7f3e9 / #292f2a / #5b614d / #e0d2b3 | Instagramプロフィールのオフホワイト・黒い広い字間、食べログのカップ写真の白とシナモン色を参照。広い余白、水平の文字組みと二面の写真。 [資料1](https://tabelog.com/osaka/A2701/A270203/27160061/) / [資料2](https://kansai-kaiten.com/loaff-osakashitennouji2610/) / [資料3](https://www.instagram.com/loaff.brunch) |
| CAFE-064 | on cafe `/on-cafe/` | #f4f2ed / #252b29 / #5d6d60 / #ddd8c9 | Instagramプロフィールの白黒の円形サインと筆記体、食べログの白い壁・木の棚を参照。円と余白の構成。コピーのonはデザイン表現で、店名由来の説明ではない。 [資料1](https://tabelog.com/hyogo/A2804/A280402/28078110/) / [資料2](https://www.instagram.com/on._.cafe_) |
| CAFE-065 | 喫茶 Stern `/kissa-stern/` | #f3eadc / #472f29 / #765342 / #d2b68a | Instagramの白地と細い黒の文字、移転後のKOBE Brightenの記事にある木の壁・茶色の空間と白皿を参照。移転前店舗の写真と区別し、木色の誌面を構成。 [資料1](https://tabelog.com/hyogo/A2801/A280101/28078155/) / [資料2](https://kobebrighten.com/ja/news/kissa-stern-sannomiya-kobe/) / [資料3](https://www.instagram.com/stern.glutenfree/) |
| CAFE-066 | キララカフェ `/kirara-cafe/` | #f5eedf / #493c30 / #776446 / #d7c4a0 | Instagramプロフィールの生成りの円形看板と細い茶色の文字、食べログの木のカウンター・白いカップを参照。細い植物の線と丸い写真枠。星の文字装飾は使用しない。 [資料1](https://tabelog.com/nara/A2903/A290301/29015812/) / [資料2](https://www.instagram.com/kirara_cafe_nara) |
| CAFE-067 | good `/good/` | #eef2f5 / #173d78 / #224f8e / #dce3eb | Instagramプロフィールの濃い青と白い斜体、食べログの白皿のモーニング、紹介記事の青いメニュー文字を参照。青白の明快な二分割と欧文イタリック。 [資料1](https://tabelog.com/wakayama/A3001/A300101/30012683/) / [資料2](https://article.yahoo.co.jp/detail/1cd54db19bd5daa9327529c24a87ab6d92089885) / [資料3](https://www.instagram.com/good_morning_lunch) |
| CAFE-068 | ponte `/ponte/` | #f7f0de / #493523 / #616d3c / #e6b65c | Instagramプロフィールの茶色の橋・緑の芽と白地、食べログの木の卓と青灰のカップを参照。茶と緑に、柑橘を連想する自主制作の黄の円を加えた。 [資料1](https://tabelog.com/wakayama/A3002/A300203/30012678/) / [資料2](https://www.instagram.com/ponte_cafe_) |
| CAFE-069 | ara `/ara/` | #eeefeb / #303b3f / #506a74 / #cfdadd | Instagramの黒い円と流れる白文字、食べログの灰色の卓・白い器とアイスコーヒーを参照。海が見えるという掲載情報に合わせた青灰はデザイン上の選択で、海の実景写真は未確認。 [資料1](https://tabelog.com/tottori/A3103/A310302/31007396/) / [資料2](https://www.instagram.com/ara_daisen.waft) |
| CAFE-070 | おやじかふぇ `/oyaji-cafe/` | #f0e3cd / #402b23 / #8a4430 / #c2a16d | とっとりずむの赤茶レンガ・木の家具・赤い座面と、食べログの黒い料理皿を参照。茶とえんじ、レコード状の円。Instagramの人物プロフィール画像は複製しない。 [資料1](https://tabelog.com/tottori/A3101/A310101/31007444/) / [資料2](https://tottorizumu.com/oyazi-cafe/) / [資料3](https://www.instagram.com/oyaji_cafe_jiji) |
