# Batch B: photographic editorial redesign

CAFE-041〜CAFE-070の30店舗。自主制作・店舗未承認の非公式デザイン案。全ページに `noindex,nofollow` と出典・イメージ写真の表示を維持しています。

## デザイン

店ごとの公開プロフィール画像と店舗写真を参考に、写真主体の6種類の構成、強弱のある店名の文字組み、深緑・コバルト・黒とピンクなどの配色で作成しました。30店舗それぞれの余白・文字の大きさ・改行・写真の組合せを設定しています。以前の大きな図形を中心とする構成を見直し、SVGは一覧サムネイル・ファビコン向けの文字主体のポスターに再設計しています。

- 担当30ルートの `index.html` と `design.css`
- `design-system.css` と `navigation.js`: 担当B専用
- `editorial/`: 新規イメージ写真17枚、WOFF2フォント3個、OFLライセンスと出典情報
- `photo-credits.json`: 既存・追加写真をまとめた正確な取得元とライセンス
- `provenance.json`: 情報源、配色根拠、確認できなかった点
- `collections/batch-b.json`: 指定された一覧統合用データ（30件）

## 写真・書体の利用条件

参考にした店舗写真・Instagramのプロフィール画像・ロゴは転載していません。ページの写真はUnsplash Licenseのイメージ素材で、実店舗・実商品と異なる旨を各写真の近くに表示しています。正確な画像URLと利用条件は `photo-credits.json` に、追加写真の写真家名・写真ページ・ライセンス確認の根拠は `editorial/credits.json` に記録しています。

ManropeとCormorant GaramondはGoogle Fontsの配信元から取得し、公開リポジトリのライセンスを確認したSIL Open Font License 1.1の書体です。ラテン文字サブセットをローカル配信し、ライセンス全文を `editorial/` に同梱しています。日本語は端末にある明朝・ゴシックのフォールバックです。外部の写真・フォントサービスへの読み込みはありません。

## 検証・限界

- `python3 scripts/check_presentation.py`: PASS（最新mainの他担当ページを含む101ページ）
- `node --check assets/batch-b/navigation.js`: PASS
- 30指定ID・ルート、画像デコード、ローカルHTML参照とアンカー、h1、SVG、JSON項目、noindex・非公式表示を静的検証
- 本文色と紙色・補助背景のコントラストは最低4.87:1
- 写真の上の文字には暗い色面を敷き、キャプションにも独立した色面を配置
- 900px以下で構成を組み替え、長い店名には個別の改行・文字サイズを設定
- メニューを閉じる際に非表示リンクへフォーカスを残さない処理とEscapeキー操作を実装

ブラウザ目視確認は未実施。管理プレビューのrelayがport 4173でタイムアウトし、CUA初期化も失敗しました。デスクトップ・390pxスマホ・Safari/WebKitでの実表示、メニューの実操作、写真のクロップは統合前に確認が必要です。静的検証の合格は実表示を保証しません。

店舗情報の確認日は2026年11月26日。Instagramは28店で公開プロフィール名と画像を確認できましたが、投稿一覧・本文・最新営業カレンダーは未確認です。カフェ花とCampanellaの公式Instagramは未特定です。営業時間は出典付きの掲載情報として扱い、資料間の差・移転・開店前の古い記述は各店で明記。価格・口コミ・店名由来・未検証の連絡先は掲載していません。現行メニューや在庫の保証はしていません。

共通一覧、共有CSS・JS、cafes.json、他担当の店舗は変更していません。mainへ直接反映・マージ・公開は行いません。

## 30店舗の配色と参考資料

| ID | 店舗・ルート | 配色 | 配色の根拠・構成 |
| --- | --- | --- | --- |
| CAFE-041 | mico `/mico/` | #152c28 / #f0f2e9 / #d2dbc7 / #213c35 | cover。Instagramプロフィール画像の銀色の立体文字と白地、食べログの銀のトレー・深緑の器を参照。白とグレーを基調に、料理写真の緑を補助色へ。 参照色を写真主体の明暗のある構成に展開。[参考1](https://tabelog.com/ishikawa/A1702/A170201/17016227/) / [参考2](https://www.instagram.com/mico.kagaonsen/) |
| CAFE-042 | 喫茶コビト `/kissa-kobito/` | #f7f3ec / #50362d / #793f31 / #e9dfd2 | vertical。Instagramの赤茶の縦組みロゴ、こまつ観光ナビの喫茶コビト写真の木製家具と白壁を参照。縦の文字組みと暖かい木肌色。 参照色を写真主体の明暗のある構成に展開。[参考1](https://tabelog.com/ishikawa/A1702/A170202/17016089/) / [参考2](https://www.komatsuguide.jp/feature/detail_267.html) / [参考3](https://www.instagram.com/kissa.kobito) |
| CAFE-043 | our `/our/` | #f5f3eb / #213a4e / #1e5b82 / #ebd268 | editorial。Instagramプロフィールの青・黄・オレンジの抽象形と、食べログの木目・白いカップを参照。青い文字と切り紙状の図形で構成。久米繊維の記事写真は衣類中心のため店内配色とは扱わない。 参照色を写真主体の明暗のある構成に展開。[参考1](https://tabelog.com/fukui/A1801/A180102/18010855/) / [参考2](https://kume.jp/2026/10/261006/) / [参考3](https://www.instagram.com/our_fukui) |
| CAFE-044 | カフェ花 `/cafe-hana/` | #2d2921 / #f5eedf / #dcc9a0 / #3b352b | vertical。食べログのモーニング写真の飴色の卓と黒い器を参照。ふーぽの複数店記事の先頭画像はいなり寿司で別店のため、花の配色根拠から除外。落ち着いた茶と紙色の額縁構成。 参照色を写真主体の明暗のある構成に展開。[参考1](https://tabelog.com/fukui/A1802/A180202/18001833/) / [参考2](https://fupo.jp/article/newopen_202610-2/) |
| CAFE-045 | 3POZZO cafe `/3pozzo-cafe/` | #eff2e9 / #143f44 / #246571 / #ccded8 | split。Instagramプロフィールのターコイズと白い輪郭、PORTAの青緑の皿・木の卓を参照。丸い縁とアーチで柔らかい構成。 参照色を写真主体の明暗のある構成に展開。[参考1](https://tabelog.com/yamanashi/A1903/A190302/19015032/) / [参考2](https://www.porta-y.jp/gourmet/3581420) / [参考3](https://www.instagram.com/3pozzo_cafe) |
| CAFE-046 | cohaccha `/cohaccha/` | #f6f2e9 / #363a2a / #52663d / #e4dccb | editorial。Instagramプロフィール画像の木製サインと黒い筆記体、食べログの白い花柄の皿と木の卓を参照。紙のメニュー帳のような構成。 参照色を写真主体の明暗のある構成に展開。[参考1](https://tabelog.com/yamanashi/A1901/A190101/19015055/) / [参考2](https://www.instagram.com/coha_showa/) |
| CAFE-047 | 古民家カフェ 温 `/kominka-onn/` | #eee8da / #303328 / #386554 / #d9d3c0 | vertical。Instagramプロフィールの黒い円と稲穂、PORTAの木の卓・深い色の器、食べログの青緑のカップを参照。縦組みと墨色の罫線。 参照色を写真主体の明暗のある構成に展開。[参考1](https://tabelog.com/yamanashi/A1901/A190101/19014998/) / [参考2](https://www.porta-y.jp/porta-press/press-vt2y1x3r) / [参考3](https://www.instagram.com/onn.cafe/) |
| CAFE-048 | LAVENDER LANE Tea Room `/lavender-lane/` | #eee8f1 / #3f2a50 / #65457f / #dfd4e8 | panorama。Instagramの紫のティーポットのプロフィール画像と、食べログのティースタンド・白い茶器を参照。紫の細い枠線と欧文セリフ。紹介記事の先頭道路写真は配色根拠から除外。 参照色を写真主体の明暗のある構成に展開。[参考1](https://tabelog.com/nagano/A2001/A200101/20029892/) / [参考2](https://naganogourmetbekkan.net/lavenderlane/) / [参考3](https://www.instagram.com/lavenderlane_tearoom/) |
| CAFE-049 | カフェみなも `/cafe-minamo/` | #edf0eb / #2e4644 / #456b69 / #d8e2db | panorama。Instagramプロフィールの濃いグレーの曲線、Web-Komachiの淡い暖簾とグレーの外観、食べログの白皿を参照。水面状の線は自主制作で、店名由来の説明ではない。 参照色を写真主体の明暗のある構成に展開。[参考1](https://tabelog.com/nagano/A2002/A200201/20030009/) / [参考2](https://www.web-komachi.com/?p=307955) / [参考3](https://www.instagram.com/minamo_cafe) |
| CAFE-050 | anew egg sandwich & cafe `/anew/` | #ffefcc / #4a3020 / #784522 / #ecc379 | poster。Instagramのたまごサンドのイラスト、クリーム色の地と茶色の文字、食べログの商品写真の黄色を参照。黄・茶の大きな文字とサンド状の層。 参照色を写真主体の明暗のある構成に展開。[参考1](https://tabelog.com/gifu/A2101/A210102/21025137/) / [参考2](https://www.instagram.com/anew_kakamigaha/) |
| CAFE-051 | Campanella `/campanella/` | #173b37 / #f2edda / #d2c08f / #254b45 | cover。食べログの青緑と金彩の皿、木目の卓、ラテの写真を参照。深い青緑と真鍮色の細線、雑誌のような段組み。公式Instagramは未特定。 参照色を写真主体の明暗のある構成に展開。[参考1](https://tabelog.com/gifu/A2101/A210101/21025076/) / [参考2](https://kaiten-heiten.com/%E3%80%90%E9%96%8B%E5%BA%97%E3%80%91cafe-campanella/) |
| CAFE-052 | Cafe R･Dreams `/r-dreams/` | #eee7d9 / #3f3026 / #715235 / #ded0b9 | panorama。Instagramプロフィールの木の看板と白いカップ、食べログのタイルの外観を参照。木色と白い線の手帳構成。店舗内部と投稿写真の全体傾向は未確認。 参照色を写真主体の明暗のある構成に展開。[参考1](https://tabelog.com/shizuoka/A2205/A220503/22046681/) / [参考2](https://www.ekiten.jp/shop_15483094/) / [参考3](https://www.instagram.com/r.dreams1219) |
| CAFE-053 | BLOSSOM COFFEE HOUSE `/blossom-coffee-house/` | #191919 / #f7f0e9 / #eda1c7 / #282024 | poster。Instagramプロフィール画像の黒地・鮮やかなピンク、食べログの商品写真のコンクリートグレーを参照。太い欧文とピンクの面。実際のブランドロゴは複製しない。 参照色を写真主体の明暗のある構成に展開。[参考1](https://tabelog.com/aichi/A2301/A230105/23098267/) / [参考2](https://www.instagram.com/blossom.nagoya/) |
| CAFE-054 | Jinryo Coffee `/jinryo-coffee/` | #f4eee2 / #3f3d2c / #49654a / #d6d3bd | split。Instagramプロフィールの茶色の抽象カップ、食べログの木のトレーと青緑の皿を参照。松本珈琲工房の記事先頭の緑の外観は店舗同定できないため配色根拠に使わない。 参照色を写真主体の明暗のある構成に展開。[参考1](https://tabelog.com/aichi/A2303/A230301/23098304/) / [参考2](https://matsumoto-coffee.com/blog/seminar/2585/) / [参考3](https://www.instagram.com/jinryo_coffee/) |
| CAFE-055 | PATISSERIE & 喫茶 KIGI `/kigi/` | #143b2e / #f1eddf / #c8c4a8 / #214c3b | editorial。Instagramプロフィールの深い緑地と白いセリフ体、食べログの縦長パフェと灰紫の背景を参照。緑の見開き、縦長の図形と欧文セリフ。 参照色を写真主体の明暗のある構成に展開。[参考1](https://tabelog.com/aichi/A2301/A230112/23098019/) / [参考2](https://www.instagram.com/kigi_kissa/) |
| CAFE-056 | ルネル洋菓子店 `/renelle/` | #f5f3f0 / #3b4145 / #596875 / #dddeda | editorial。Instagramの白地と細い黒い筆記体、食べログの青い背景・白いクリーム・黒皿を参照。白い展示室のような余白と青灰色の文字。 参照色を写真主体の明暗のある構成に展開。[参考1](https://tabelog.com/aichi/A2301/A230113/23098295/) / [参考2](https://www.instagram.com/renelle_yougashiten/) |
| CAFE-057 | 7uts `/7uts/` | #242f85 / #f8f0d6 / #f3da83 / #343f96 | cover。Instagramプロフィールの丸い青い文字、号外NETの木の棚・青文字のクッション・黄色やオレンジのランプを参照。太い文字と丸い面を重ねたポスター構成。 参照色を写真主体の明暗のある構成に展開。[参考1](https://tabelog.com/mie/A2402/A240202/24022804/) / [参考2](https://suzuka-kameyama.goguynet.jp/2026/09/14/7uts/) / [参考3](https://www.instagram.com/7uts_coffee_mie) |
| CAFE-058 | riverside cafe ＆ sleep `/riverside-cafe-sleep/` | #183d39 / #e9eee3 / #bbd6ca / #28514b | cover。Instagramプロフィールの淡い青緑と茶の輪、紹介記事の木の建物と緑、食べログの青いカップを参照。横に広い構成と川のような線。 参照色を写真主体の明暗のある構成に展開。[参考1](https://tabelog.com/mie/A2404/A240402/24022885/) / [参考2](https://mycmyc.blog.fc2.com/blog-entry-3402.html) / [参考3](https://www.instagram.com/riversidecafe.sleep) |
| CAFE-059 | カフェとごはん ひだまり `/hidamari/` | #f7efd9 / #4b3c24 / #7f5a21 / #ead08c | panorama。Instagramプロフィールの黄色の円と手書き文字、食べログ・滋賀つーしんの御膳の木色と白い器を参照。黄色の余白と献立帳のような罫線。 参照色を写真主体の明暗のある構成に展開。[参考1](https://tabelog.com/shiga/A2503/A250301/25014589/) / [参考2](https://shiga2.jp/hidamari-omihachiman-renewal-open/shiga2/) / [参考3](https://www.instagram.com/hidamari_cafebistro/) |
| CAFE-060 | 給食日和 `/kyushoku-biyori/` | #f7ecd0 / #52392c / #984229 / #e6be76 | panorama。Instagramプロフィールの黄色の円とえんじの縁、食べログの金属トレー・白い皿を参照。給食のトレーを抽象化した図形と明るい見出し。 参照色を写真主体の明暗のある構成に展開。[参考1](https://tabelog.com/shiga/A2501/A250101/25014660/) / [参考2](https://kokoiro.jp/shop/kyushokubiyori/) / [参考3](https://www.instagram.com/kyusyokubiyori/) |
| CAFE-061 | TOWZA DINER 1830 `/towza-diner/` | #a62e23 / #fff0d8 / #fff0d8 / #ba3f30 | poster。Instagramプロフィールの鮮やかな赤と白い太字だけを直接確認。食べログの代表画像はNO PHOTOで、店内・商品写真は未確認。赤い活字を起点にした暫定デザイン。 参照色を写真主体の明暗のある構成に展開。[参考1](https://tabelog.com/kyoto/A2601/A260503/26046119/) / [参考2](https://www.instagram.com/towza_diner_1830) |
| CAFE-062 | DEL `/del/` | #f4e8cc / #732b22 / #8d3024 / #e4c1a1 | poster。Instagramプロフィールのクリーム色と赤い太字、食べログの赤いカップ印刷・木の卓を参照。切り紙状の赤い面と大きな活字。 参照色を写真主体の明暗のある構成に展開。[参考1](https://tabelog.com/osaka/A2701/A270201/27159757/) / [参考2](https://www.instagram.com/del_southhorie) |
| CAFE-063 | LOAFF `/loaff/` | #f3f1e8 / #30382d / #53644d / #dadccf | editorial。Instagramプロフィールのオフホワイト・黒い広い字間、食べログのカップ写真の白とシナモン色を参照。広い余白、水平の文字組みと二面の写真。 参照色を写真主体の明暗のある構成に展開。[参考1](https://tabelog.com/osaka/A2701/A270203/27160061/) / [参考2](https://kansai-kaiten.com/loaff-osakashitennouji2610/) / [参考3](https://www.instagram.com/loaff.brunch) |
| CAFE-064 | on cafe `/on-cafe/` | #eeede6 / #293932 / #486451 / #d5d9cd | split。Instagramプロフィールの白黒の円形サインと筆記体、食べログの白い壁・木の棚を参照。円と余白の構成。コピーのonはデザイン表現で、店名由来の説明ではない。 参照色を写真主体の明暗のある構成に展開。[参考1](https://tabelog.com/hyogo/A2804/A280402/28078110/) / [参考2](https://www.instagram.com/on._.cafe_) |
| CAFE-065 | 喫茶 Stern `/kissa-stern/` | #36291f / #f3ebda / #dbc9a6 / #49372a | cover。Instagramの白地と細い黒の文字、移転後のKOBE Brightenの記事にある木の壁・茶色の空間と白皿を参照。移転前店舗の写真と区別し、木色の誌面を構成。 参照色を写真主体の明暗のある構成に展開。[参考1](https://tabelog.com/hyogo/A2801/A280101/28078155/) / [参考2](https://kobebrighten.com/ja/news/kissa-stern-sannomiya-kobe/) / [参考3](https://www.instagram.com/stern.glutenfree/) |
| CAFE-066 | キララカフェ `/kirara-cafe/` | #f0e9db / #4c3d2a / #725b39 / #dfd0b7 | split。Instagramプロフィールの生成りの円形看板と細い茶色の文字、食べログの木のカウンター・白いカップを参照。細い植物の線と丸い写真枠。星の文字装飾は使用しない。 参照色を写真主体の明暗のある構成に展開。[参考1](https://tabelog.com/nara/A2903/A290301/29015812/) / [参考2](https://www.instagram.com/kirara_cafe_nara) |
| CAFE-067 | good `/good/` | #123e86 / #f2f0e6 / #f2f0e6 / #245399 | poster。Instagramプロフィールの濃い青と白い斜体、食べログの白皿のモーニング、紹介記事の青いメニュー文字を参照。青白の明快な二分割と欧文イタリック。 参照色を写真主体の明暗のある構成に展開。[参考1](https://tabelog.com/wakayama/A3001/A300101/30012683/) / [参考2](https://article.yahoo.co.jp/detail/1cd54db19bd5daa9327529c24a87ab6d92089885) / [参考3](https://www.instagram.com/good_morning_lunch) |
| CAFE-068 | ponte `/ponte/` | #efe9d8 / #493923 / #5b6b3d / #ddc182 | editorial。Instagramプロフィールの茶色の橋・緑の芽と白地、食べログの木の卓と青灰のカップを参照。茶と緑に、柑橘を連想する自主制作の黄の円を加えた。 参照色を写真主体の明暗のある構成に展開。[参考1](https://tabelog.com/wakayama/A3002/A300203/30012678/) / [参考2](https://www.instagram.com/ponte_cafe_) |
| CAFE-069 | ara `/ara/` | #e5e9e6 / #34484d / #4a6972 / #cbd6d3 | panorama。Instagramの黒い円と流れる白文字、食べログの灰色の卓・白い器とアイスコーヒーを参照。海が見えるという掲載情報に合わせた青灰はデザイン上の選択で、海の実景写真は未確認。 参照色を写真主体の明暗のある構成に展開。[参考1](https://tabelog.com/tottori/A3103/A310302/31007396/) / [参考2](https://www.instagram.com/ara_daisen.waft) |
| CAFE-070 | おやじかふぇ `/oyaji-cafe/` | #3c2921 / #f0e5cf / #d7bc8c / #51372b | cover。とっとりずむの赤茶レンガ・木の家具・赤い座面と、食べログの黒い料理皿を参照。茶とえんじ、レコード状の円。Instagramの人物プロフィール画像は複製しない。 参照色を写真主体の明暗のある構成に展開。[参考1](https://tabelog.com/tottori/A3101/A310101/31007444/) / [参考2](https://tottorizumu.com/oyazi-cafe/) / [参考3](https://www.instagram.com/oyaji_cafe_jiji) |
