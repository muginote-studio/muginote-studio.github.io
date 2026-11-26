# Batch A / Editorial redesign

CAFE-011〜040、30店舗の非公式デザイン案の改良版です。店名の文字組み、写真の面積、色面の明暗、本文への流れを再設計しました。13種類の基本構成を保ちつつ、共通のカップ・皿の装飾と繰り返しの見出しを削り、店舗別に余白と強弱を調整しています。

## 変更範囲

30店舗の index.html、assets/batch-a/、collections/batch-a.json のみ。共通index.html、cafes.json、共有CSS・JS、他担当の店舗とアセットは変更していません。最新mainから改良用ブランチを作成し、PRで納品します。統合・公開は元チャットの担当です。

既存の紹介本文、所在地・掲載営業時間、外部リンクは保持しました。全ページに自主制作・店舗未承認・noindex,nofollowの表示、写真近傍のイメージ表示があります。

## 書体

Cormorant Garamond、DM Sans、Barlow Condensed、Noto Serif JP、Noto Sans JPをローカル配信します。見出し等に使う文字でサブセット化されたGoogle Fontsの配布データを、輪郭を変えずにWOFF2へ圧縮しました。ブラウザがフォントを読めない場合はシステム書体にフォールバックします。

出典・原データと成果物のSHA-256・処理内容は font-sources.json、SIL Open Font Licenseは fonts/*-OFL.txt にあります。公式ロゴを再現したものではありません。

## 検証

```sh
python3 scripts/check_presentation.py
python3 assets/batch-a/verify.py
node --check assets/batch-a/site.js
node --test assets/batch-a/check-menu.cjs
```

- リポジトリ全体101ページの装飾・SVG・内部参照検査：PASS。
- 担当30件のID・ルート・h1・ラベル・必須データ・CSS/HTML参照・画像・フォントのSHA・WOFF2ヘッダ・ライセンス同梱：PASS。
- 本文/背景、本文/補助背景、アクセント/背景のコントラスト：全30件で4.5:1以上（最低4.89:1）。
- JavaScript構文とメニュー5ケース：PASS。JS自体の変更はありません。
- 紹介本文・訪問情報とリンク集合が改良前から変わっていないことを30件全て比較：PASS。
- 代表6店舗の320/390pxを想定した見出し幅を実フォントの送り幅で静的確認。実際のブラウザ描画テストではありません。
- ブラウザ初期化は今回も `the gaas-browser node_repl sandbox cannot be disabled` で失敗しました。スマホ・デスクトップの実描画、タップ、画像の切り取りの実描画、Safari/WebKitは未確認です。

## 店舗情報・写真の確認範囲

店舗情報の照合日は2026年11月26日。Instagram投稿一覧・個別投稿は全店未確認、27店舗は公開プロフィール名・画像のみ確認。喫茶ブロンディー・Quebec亭はプロフィールも直接未確認、Re:skyは公式アカウントを同定できませんでした。臨時休業や現行メニューは店舗に確認してください。

写真9点は既存のUnsplash Licenseの素材を継続使用しています。原画像URL・利用条件・SHAは image-sources.json にあります。店舗写真は配色の参考だけに使い、転載していません。実店舗・実商品と異なるイメージであることを写真の近く・alt・フッターに明示しています。

## 30件のルート・改良後の配色

配色は背景／文字／アクセント／補助背景の順。店舗のブランド規定色ではなく、参考資料をもとにしたデザイン案です。

| ID | 店舗・ルート | 配色 | 構成 |
| --- | --- | --- | --- |
| CAFE-011 | [Hoki Cafe](../../hoki-cafe/) `/hoki-cafe/` | #142c3a / #f3eee3 / #f1ce67 / #233e4c | split |
| CAFE-012 | [喫茶ブロンディー](../../kissa-blondy/) `/kissa-blondy/` | #efe2c7 / #34241b / #7a4328 / #dfc79b | frame |
| CAFE-013 | [Asile](../../asile/) `/asile/` | #322726 / #f3ede0 / #d9bc91 / #47312f | diptych |
| CAFE-014 | [中野珈琲店](../../nakano-coffee/) `/nakano-coffee/` | #f3f4ef / #253c30 / #46624e / #d5dfcf | letter |
| CAFE-015 | [まんがめし喫茶 ひよこ堂](../../hiyokodo/) `/hiyokodo/` | #f7f0dc / #702e23 / #9f301f / #ead5a9 | poster |
| CAFE-016 | [喫茶 夜 桜山](../../kissa-yoru-sakurayama/) `/kissa-yoru-sakurayama/` | #151c1b / #eee6d7 / #dab477 / #24302c | night |
| CAFE-017 | [cafe MARM](../../cafe-marm/) `/cafe-marm/` | #f8f6ed / #282820 / #795342 / #e9dfcc | grid |
| CAFE-018 | [蚯蚓](../../mimizu/) `/mimizu/` | #d58659 / #241a17 / #352019 / #e7ac7b | editorial |
| CAFE-019 | [KO-MEGURI](../../ko-meguri/) `/ko-meguri/` | #f0f0e3 / #2d402b / #526b3c / #d3debd | arch |
| CAFE-020 | [きゃどぽんぽんじ〜な](../../kyado-ponponjina/) `/kyado-ponponjina/` | #244a49 / #f1eddb / #e5bc7e / #365b58 | split |
| CAFE-021 | [CAFE & DINING Le Lien](../../le-lien/) `/le-lien/` | #f6e7dd / #53302e / #91524c / #e6b8a5 | diptych |
| CAFE-022 | [くまきち日和](../../kumakichi-biyori/) `/kumakichi-biyori/` | #e7e5d1 / #25362c / #4e633e / #c5ccb0 | vertical |
| CAFE-023 | [なんでもない日に、踊ろうよ](../../nandemonaihi/) `/nandemonaihi/` | #efead8 / #383c29 / #904b30 / #dbd1b1 | letter |
| CAFE-024 | [Green & Cafe HANA](../../green-cafe-hana/) `/green-cafe-hana/` | #e6ebce / #29422a / #4a6035 / #c9d4a6 | garden |
| CAFE-025 | [Re:sky](../../resky/) `/resky/` | #25282d / #f6ead6 / #e6a17e / #3b3b41 | poster |
| CAFE-026 | [Quebec亭](../../quebectei/) `/quebectei/` | #ede2c7 / #3d3224 / #785a32 / #d7bc8d | frame |
| CAFE-027 | [FUFUFU](../../fufufu/) `/fufufu/` | #e8ebdc / #263c31 / #546940 / #cad3b7 | editorial |
| CAFE-028 | [my.Honey](../../my-honey/) `/my-honey/` | #f5d66b / #3c271c / #833224 / #eaba48 | pop |
| CAFE-029 | [Le’Chainon](../../le-chainon/) `/le-chainon/` | #e6d9ee / #47304a / #714779 / #d1bcdf | pop |
| CAFE-030 | [アメリカンダイナーHOODHOUSE](../../hoodhouse/) `/hoodhouse/` | #962d23 / #f8e8bd / #ffd85d / #a93a2d | diner |
| CAFE-031 | [聖奈珈琲](../../sena-coffee/) `/sena-coffee/` | #f1e6d1 / #4b2e22 / #7e432f / #ddc2a0 | letter |
| CAFE-032 | [BOUNCE](../../bounce/) `/bounce/` | #f2f4ed / #153b29 / #3f6147 / #dce4d2 | grid |
| CAFE-033 | [cafe tarte plus](../../tarte-plus/) `/tarte-plus/` | #efe0d5 / #573936 / #8b4c4a / #dec3b1 | arch |
| CAFE-034 | [vigo](../../vigo/) `/vigo/` | #243c31 / #f0eddc / #cfbd82 / #355043 | garden |
| CAFE-035 | [ちょい呑み処ten](../../ten/) `/ten/` | #f2e5c8 / #254236 / #506847 / #d9c69b | diptych |
| CAFE-036 | [溶時](../../toki/) `/toki/` | #f7f6ec / #3c443e / #756236 / #e7e2bd | vertical |
| CAFE-037 | [Cache Cache](../../cache-cache/) `/cache-cache/` | #eee7d7 / #383d2d / #756039 / #d8ceb6 | arch |
| CAFE-038 | [キッチンカーの古民家cafe Zen](../../cafe-zen/) `/cafe-zen/` | #e7e4d5 / #293729 / #56623b / #cad0b2 | vertical |
| CAFE-039 | [喫茶 Perla](../../kissa-perla/) `/kissa-perla/` | #1d292f / #efe6d3 / #cfb47a / #2d3e43 | frame |
| CAFE-040 | [甘味処 食べ鯛](../../tabetai/) `/tabetai/` | #eee4d1 / #143c4c / #7b3f39 / #d7b591 | poster |

## 配色・写真の参考資料

### CAFE-011 Hoki Cafe

公式Instagramは公開プロフィール名とプロフィール画像のみ確認。投稿一覧・個別投稿は閲覧できず、投稿写真を確認したとはしていません。 公式プロフィール画像の濃紺の板壁と黄色の文字、食べログの明るい窓辺・木製家具から、紺と黄土色、直線的な分割構成へ。 改良版では店舗写真の参考色を保ち、色面の明暗、店名の大小、写真の切り取りを再構成。書体はOFLのローカル配信。公式ロゴの再現ではありません。

配色参考：[資料1](https://tabelog.com/hokkaido/A0104/A010401/1086431/)、[資料2](https://www.instagram.com/hokicafe1026)

店舗情報：[資料1](https://tabelog.com/hokkaido/A0104/A010401/1086431/)、[資料2](https://www.shopship.jp/asahikawa/open-close/hokicafe1026/)

### CAFE-012 喫茶ブロンディー

公式Instagramのプロフィール・投稿は直接確認できませんでした。公開の店舗写真を補助資料にしています。 食べログの白いカップの茶色の縁、濃茶の卓上、柄入りの椅子と暗めの店内写真から、琥珀・焦茶と額縁型の構図へ。Instagramはプロフィールも直接確認できず。 改良版では店舗写真の参考色を保ち、色面の明暗、店名の大小、写真の切り取りを再構成。書体はOFLのローカル配信。公式ロゴの再現ではありません。

配色参考：[資料1](https://tabelog.com/hokkaido/A0101/A010305/1086434/)、[資料2](https://www.instagram.com/blondy_roastery)

店舗情報：[資料1](https://tabelog.com/hokkaido/A0101/A010305/1086434/)、[資料2](https://plaza.rakuten.co.jp/yorozuken/diary/202610240003/)

### CAFE-013 Asile

公式Instagramは公開プロフィール名とプロフィール画像のみ確認。投稿一覧・個別投稿は閲覧できず、投稿写真を確認したとはしていません。 公式プロフィールの細い金色の文字と植物、食べログのワイン・木のカウンターから、クリームとワイン色、細い明朝と二連写真へ。 改良版では店舗写真の参考色を保ち、色面の明暗、店名の大小、写真の切り取りを再構成。書体はOFLのローカル配信。公式ロゴの再現ではありません。

配色参考：[資料1](https://tabelog.com/aomori/A0201/A020101/2014023/)、[資料2](https://www.instagram.com/asile_369_/)

店舗情報：[資料1](https://tabelog.com/aomori/A0201/A020101/2014023/)、[資料2](https://www.acci.or.jp/salon/【会員事業所紹介】カフェ・バル-asile/)

### CAFE-014 中野珈琲店

公式Instagramは公開プロフィール名とプロフィール画像のみ確認。投稿一覧・個別投稿は閲覧できず、投稿写真を確認したとはしていません。 食べログの白壁と暗い木のカウンター、窓外の緑から、白灰・深緑と便箋のような端正な文字組みへ。営業時間は新聞記事と食べログに相違があるため現行未確認。 改良版では店舗写真の参考色を保ち、色面の明暗、店名の大小、写真の切り取りを再構成。書体はOFLのローカル配信。公式ロゴの再現ではありません。

配色参考：[資料1](https://tabelog.com/aomori/A0202/A020201/2014002/)、[資料2](https://www.instagram.com/nakanocoffee10/)

店舗情報：[資料1](https://tabelog.com/aomori/A0202/A020201/2014002/)、[資料2](https://hirosaki.keizai.biz/headline/2773/)

### CAFE-015 まんがめし喫茶 ひよこ堂

公式Instagramは公開プロフィール名とプロフィール画像のみ確認。投稿一覧・個別投稿は閲覧できず、投稿写真を確認したとはしていません。 食べログの本棚、木の机、赤いカウンター椅子と緑の壁から、紙色・赤・深緑、紙面を組むようなポスター構成へ。プロフィールの既存キャラクターは複製しない。 改良版では店舗写真の参考色を保ち、色面の明暗、店名の大小、写真の切り取りを再構成。書体はOFLのローカル配信。公式ロゴの再現ではありません。

配色参考：[資料1](https://tabelog.com/iwate/A0301/A030103/3013251/)、[資料2](https://www.instagram.com/hiyoko_dou/)

店舗情報：[資料1](https://tabelog.com/iwate/A0301/A030103/3013251/)、[資料2](https://kaiten-heiten-24.com/hiyoko-dou/)

### CAFE-016 喫茶 夜 桜山

公式Instagramは公開プロフィール名とプロフィール画像のみ確認。投稿一覧・個別投稿は閲覧できず、投稿写真を確認したとはしていません。 公式プロフィールの余白を生かした縦の文字、食べログの暗い木の机・ランプの灯りから、墨緑と琥珀、縦組みの余白へ。 改良版では店舗写真の参考色を保ち、色面の明暗、店名の大小、写真の切り取りを再構成。書体はOFLのローカル配信。公式ロゴの再現ではありません。

配色参考：[資料1](https://tabelog.com/iwate/A0301/A030101/3013416/)、[資料2](https://www.instagram.com/sakurayama_yoru/)

店舗情報：[資料1](https://tabelog.com/iwate/A0301/A030101/3013416/)

### CAFE-017 cafe MARM

公式Instagramは公開プロフィール名とプロフィール画像のみ確認。投稿一覧・個別投稿は閲覧できず、投稿写真を確認したとはしていません。 公式プロフィールの黒い太字MARMと白地、食べログの豆皿・淡い木の卓上から、白と茶、整然としたグリッドへ。 改良版では店舗写真の参考色を保ち、色面の明暗、店名の大小、写真の切り取りを再構成。書体はOFLのローカル配信。公式ロゴの再現ではありません。

配色参考：[資料1](https://tabelog.com/miyagi/A0404/A040404/4030479/)、[資料2](https://www.instagram.com/cafe.marm)

店舗情報：[資料1](https://tabelog.com/miyagi/A0404/A040404/4030479/)、[資料2](https://freimann.hatenablog.com/entry/2026/10/09/170000)

### CAFE-018 蚯蚓

公式Instagramは公開プロフィール名とプロフィール画像のみ確認。投稿一覧・個別投稿は閲覧できず、投稿写真を確認したとはしていません。 公式プロフィールの茶色の線画、食べログの褐色の器・オレンジの椅子・木の棚から、土色と焼けた橙、雑誌風の大小写真へ。 改良版では店舗写真の参考色を保ち、色面の明暗、店名の大小、写真の切り取りを再構成。書体はOFLのローカル配信。公式ロゴの再現ではありません。

配色参考：[資料1](https://tabelog.com/miyagi/A0401/A040105/4030460/)、[資料2](https://www.instagram.com/mimizu_kaffee)

店舗情報：[資料1](https://tabelog.com/miyagi/A0401/A040105/4030460/)、[資料2](https://sendaiminami-tusin.com/mimizu2610/)

### CAFE-019 KO-MEGURI

公式Instagramは公開プロフィール名とプロフィール画像のみ確認。投稿一覧・個別投稿は閲覧できず、投稿写真を確認したとはしていません。 公式プロフィールの木目の丸い看板、食べログの白い椅子・植物柄・緑の鉢から、白とオリーブ、アーチと植物の線へ。補助ブログは503。 改良版では店舗写真の参考色を保ち、色面の明暗、店名の大小、写真の切り取りを再構成。書体はOFLのローカル配信。公式ロゴの再現ではありません。

配色参考：[資料1](https://tabelog.com/akita/A0505/A050501/5011649/)、[資料2](https://www.instagram.com/ko_meguri.cafe/)

店舗情報：[資料1](https://tabelog.com/akita/A0505/A050501/5011649/)

### CAFE-020 きゃどぽんぽんじ〜な

公式Instagramは公開プロフィール名とプロフィール画像のみ確認。投稿一覧・個別投稿は閲覧できず、投稿写真を確認したとはしていません。 食べログとあきたタウン情報の青緑の壁・木製椅子・琥珀色の飲み物から、青緑と栗色、丸みを抑えた横長構成へ。店名由来は本文に採用しない。 改良版では店舗写真の参考色を保ち、色面の明暗、店名の大小、写真の切り取りを再構成。書体はOFLのローカル配信。公式ロゴの再現ではありません。

配色参考：[資料1](https://tabelog.com/akita/A0501/A050101/5011631/)、[資料2](https://www.instagram.com/pon.pon_cafe/)

店舗情報：[資料1](https://tabelog.com/akita/A0501/A050101/5011631/)、[資料2](https://web.akita-townjoho.jp/post-category/20260430-kyadoponponjina/)

### CAFE-021 CAFE & DINING Le Lien

公式Instagramは公開プロフィール名とプロフィール画像のみ確認。投稿一覧・個別投稿は閲覧できず、投稿写真を確認したとはしていません。 公式プロフィールの端正なセリフ体、食べログの淡いカウンター・ピンクと黄の外壁から、淡い桃と赤茶、二つの時間を見せる構成へ。 改良版では店舗写真の参考色を保ち、色面の明暗、店名の大小、写真の切り取りを再構成。書体はOFLのローカル配信。公式ロゴの再現ではありません。

配色参考：[資料1](https://tabelog.com/yamagata/A0602/A060202/6013562/)、[資料2](https://www.instagram.com/cafe_lelien2026)

店舗情報：[資料1](https://tabelog.com/yamagata/A0602/A060202/6013562/)

### CAFE-022 くまきち日和

公式Instagramは公開プロフィール名とプロフィール画像のみ確認。投稿一覧・個別投稿は閲覧できず、投稿写真を確認したとはしていません。 公式プロフィールの墨の古民家線画、食べログの畳・濃い梁・窓の緑・青い器から、畳色と深緑、縦書きの導入へ。食べログの古い開業予定記述は営業時間に使わない。 改良版では店舗写真の参考色を保ち、色面の明暗、店名の大小、写真の切り取りを再構成。書体はOFLのローカル配信。公式ロゴの再現ではありません。

配色参考：[資料1](https://tabelog.com/yamagata/A0602/A060203/6013674/)、[資料2](https://www.instagram.com/kumakichi_biyori_yamagata.cafe)

店舗情報：[資料1](https://tabelog.com/yamagata/A0602/A060203/6013674/)、[資料2](https://camp-fire.jp/projects/977512/view?list=prefecture_yamagata_projects_fresh)、[資料3](https://camp-fire.jp/projects/977512/view/activities/910342)

### CAFE-023 なんでもない日に、踊ろうよ

公式Instagramは公開プロフィール名とプロフィール画像のみ確認。投稿一覧・個別投稿は閲覧できず、投稿写真を確認したとはしていません。 公式プロフィールの朱色の線画、食べログの畳・木枠の窓・クリームソーダの緑から、紙色と朱茶、手紙のように読み進める構成へ。 改良版では店舗写真の参考色を保ち、色面の明暗、店名の大小、写真の切り取りを再構成。書体はOFLのローカル配信。公式ロゴの再現ではありません。

配色参考：[資料1](https://tabelog.com/yamagata/A0603/A060303/6013517/)、[資料2](https://www.instagram.com/nandemonaihini_/)

店舗情報：[資料1](https://tabelog.com/yamagata/A0603/A060303/6013517/)、[資料2](https://yama-katsu.jp/press/30267/)、[資料3](https://yuzamachi.com/taberu/nandemonaihini/2026/07/14/)

### CAFE-024 Green & Cafe HANA

公式Instagramは公開プロフィール名とプロフィール画像のみ確認。投稿一覧・個別投稿は閲覧できず、投稿写真を確認したとはしていません。 公式プロフィールのオリーブ色の植物・丸い看板、食べログの窓際の緑と木のテーブルから、葉色と白、窓形の写真枠へ。施設ニュースは本文の一次資料として採用。 改良版では店舗写真の参考色を保ち、色面の明暗、店名の大小、写真の切り取りを再構成。書体はOFLのローカル配信。公式ロゴの再現ではありません。

配色参考：[資料1](https://tabelog.com/fukushima/A0704/A070401/7021049/)、[資料2](https://www.instagram.com/green_and_caffe_hana)

店舗情報：[資料1](https://tabelog.com/fukushima/A0704/A070401/7021049/)、[資料2](https://www.gurutto-iwaki.com/detail/1792/news/news-931717.html)

### CAFE-025 Re:sky

公式Instagramを同定できませんでした。公開の店舗紹介と食べログの写真を補助資料にしています。 食べログの白黒チェッカーのカウンター、赤い店内小物、木の床から、黒白とくすんだ赤、アメリカンポスターへ。公式Instagramは割当資料に記載がなく同定できず。 改良版では店舗写真の参考色を保ち、色面の明暗、店名の大小、写真の切り取りを再構成。書体はOFLのローカル配信。公式ロゴの再現ではありません。

配色参考：[資料1](https://tabelog.com/fukushima/A0705/A070501/7020931/)

店舗情報：[資料1](https://tabelog.com/fukushima/A0705/A070501/7020931/)、[資料2](https://www.gurutto-aizu.com/detail/1158/index.html)

### CAFE-026 Quebec亭

公式Instagramのプロフィール・投稿は直接確認できませんでした。公開の店舗写真を補助資料にしています。 食べログの料理写真で確認できた木のトレー、茶褐色の器と濃い輪郭から、木色と茶、控えめな額縁構成へ。店内全景・Instagramプロフィールと投稿は未確認。 改良版では店舗写真の参考色を保ち、色面の明暗、店名の大小、写真の切り取りを再構成。書体はOFLのローカル配信。公式ロゴの再現ではありません。

配色参考：[資料1](https://tabelog.com/ibaraki/A0805/A080503/8031302/)、[資料2](https://www.instagram.com/cafequebec2026/)

店舗情報：[資料1](https://tabelog.com/ibaraki/A0805/A080503/8031302/)

### CAFE-027 FUFUFU

公式Instagramは公開プロフィール名とプロフィール画像のみ確認。投稿一覧・個別投稿は閲覧できず、投稿写真を確認したとはしていません。 公式プロフィールの灰色地と手書き風白文字、食べログの木の外壁・緑・レコード周りから、灰緑と木色、雑誌のコラムのような配置へ。 改良版では店舗写真の参考色を保ち、色面の明暗、店名の大小、写真の切り取りを再構成。書体はOFLのローカル配信。公式ロゴの再現ではありません。

配色参考：[資料1](https://tabelog.com/tochigi/A0901/A090101/9024341/)、[資料2](https://www.instagram.com/fufufu.store)

店舗情報：[資料1](https://tabelog.com/tochigi/A0901/A090101/9024341/)、[資料2](https://www.tochinavi.net/spot/newopen/detail.shtml?id=4313)

### CAFE-028 my.Honey

公式Instagramは公開プロフィール名とプロフィール画像のみ確認。投稿一覧・個別投稿は閲覧できず、投稿写真を確認したとはしていません。 公式プロフィールの蜂蜜色、食べログの黄色い外壁と赤い扉から、蜂蜜色と赤茶、丸い写真と太い文字へ。写真内の他店舗掲載に見える料理は参考から除外。 改良版では店舗写真の参考色を保ち、色面の明暗、店名の大小、写真の切り取りを再構成。書体はOFLのローカル配信。公式ロゴの再現ではありません。

配色参考：[資料1](https://tabelog.com/tochigi/A0901/A090101/9024337/)、[資料2](https://www.instagram.com/myhoney1919)

店舗情報：[資料1](https://tabelog.com/tochigi/A0901/A090101/9024337/)、[資料2](https://utsunomiya.goguynet.jp/2026/07/14/my-honey/)

### CAFE-029 Le’Chainon

公式Instagramは公開プロフィール名とプロフィール画像のみ確認。投稿一覧・個別投稿は閲覧できず、投稿写真を確認したとはしていません。 公式プロフィールの水色・桃・緑の花、食べログのカラフルな花と紫の小物から、淡い紫とミントを手掛かりに、柔らかな円形構成へ。 改良版では店舗写真の参考色を保ち、色面の明暗、店名の大小、写真の切り取りを再構成。書体はOFLのローカル配信。公式ロゴの再現ではありません。

配色参考：[資料1](https://tabelog.com/gunma/A1001/A100102/10027439/)、[資料2](https://www.instagram.com/le.chainon8787/)

店舗情報：[資料1](https://tabelog.com/gunma/A1001/A100102/10027439/)

### CAFE-030 アメリカンダイナーHOODHOUSE

公式Instagramは公開プロフィール名とプロフィール画像のみ確認。投稿一覧・個別投稿は閲覧できず、投稿写真を確認したとはしていません。 公式プロフィールの赤と黄の太字、食べログの黒白チェッカー床・暗い木のカウンターから、赤・黄・黒、太い文字と帯の構成へ。 改良版では店舗写真の参考色を保ち、色面の明暗、店名の大小、写真の切り取りを再構成。書体はOFLのローカル配信。公式ロゴの再現ではありません。

配色参考：[資料1](https://tabelog.com/gunma/A1001/A100101/10026738/)、[資料2](https://www.instagram.com/hoodhouse_maebashi/)

店舗情報：[資料1](https://tabelog.com/gunma/A1001/A100101/10026738/)、[資料2](https://saikura.info/open-hood-house-maebashi-20261029/)

### CAFE-031 聖奈珈琲

公式Instagramは公開プロフィール名とプロフィール画像のみ確認。投稿一覧・個別投稿は閲覧できず、投稿写真を確認したとはしていません。 公式プロフィールの生成りと赤茶の明朝、食べログの白壁・木の天井・大きな窓から、生成りと赤茶、静かな便箋型へ。slugは指定どおりsena-coffee、店名表記を優先。 改良版では店舗写真の参考色を保ち、色面の明暗、店名の大小、写真の切り取りを再構成。書体はOFLのローカル配信。公式ロゴの再現ではありません。

配色参考：[資料1](https://tabelog.com/gunma/A1002/A100202/10027456/)、[資料2](https://www.instagram.com/seinacoffee/)

店舗情報：[資料1](https://tabelog.com/gunma/A1002/A100202/10027456/)

### CAFE-032 BOUNCE

公式Instagramは公開プロフィール名とプロフィール画像のみ確認。投稿一覧・個別投稿は閲覧できず、投稿写真を確認したとはしていません。 公式プロフィールの深緑のセリフ体、食べログの白い壁・灰色の床・緑の植物から、白と深緑、余白のある整ったグリッドへ。 改良版では店舗写真の参考色を保ち、色面の明暗、店名の大小、写真の切り取りを再構成。書体はOFLのローカル配信。公式ロゴの再現ではありません。

配色参考：[資料1](https://tabelog.com/saitama/A1105/A110503/11068999/)、[資料2](https://www.instagram.com/bounce.wellness)

店舗情報：[資料1](https://tabelog.com/saitama/A1105/A110503/11068999/)

### CAFE-033 cafe tarte plus

公式Instagramは公開プロフィール名とプロフィール画像のみ確認。投稿一覧・個別投稿は閲覧できず、投稿写真を確認したとはしていません。 公式プロフィールの茶地と白文字、食べログの淡い壁・赤茶の腰壁・丸い照明・曲線のモールから、ローズブラウンとアーチの構成へ。 改良版では店舗写真の参考色を保ち、色面の明暗、店名の大小、写真の切り取りを再構成。書体はOFLのローカル配信。公式ロゴの再現ではありません。

配色参考：[資料1](https://tabelog.com/saitama/A1104/A110402/11068975/)、[資料2](https://www.instagram.com/cafe_tarte_plus)

店舗情報：[資料1](https://tabelog.com/saitama/A1104/A110402/11068975/)、[資料2](https://kuki-satte.goguynet.jp/2026/11/07/tarte-plus/)

### CAFE-034 vigo

公式Instagramは公開プロフィール名とプロフィール画像のみ確認。投稿一覧・個別投稿は閲覧できず、投稿写真を確認したとはしていません。 公式プロフィールのモノクロの鹿と植物の線画、食べログの木の梁・白壁・植物から、墨緑と木色、温室を連想する窓枠へ。鹿のロゴは複製しない。 改良版では店舗写真の参考色を保ち、色面の明暗、店名の大小、写真の切り取りを再構成。書体はOFLのローカル配信。公式ロゴの再現ではありません。

配色参考：[資料1](https://tabelog.com/chiba/A1201/A120101/12068435/)、[資料2](https://www.instagram.com/vigo_waffle)

店舗情報：[資料1](https://tabelog.com/chiba/A1201/A120101/12068435/)、[資料2](https://www.gummaumaimono.info/entry/2026/10/15/214835)

### CAFE-035 ちょい呑み処ten

公式Instagramは公開プロフィール名とプロフィール画像のみ確認。投稿一覧・個別投稿は閲覧できず、投稿写真を確認したとはしていません。 公式プロフィールの生成りと黒い円、食べログの深緑の壁・花柄のテーブルクロス・木の床から、生成りと深緑、昼夜の二連構成へ。 改良版では店舗写真の参考色を保ち、色面の明暗、店名の大小、写真の切り取りを再構成。書体はOFLのローカル配信。公式ロゴの再現ではありません。

配色参考：[資料1](https://tabelog.com/chiba/A1203/A120301/12068592/)、[資料2](https://www.instagram.com/ten_choinomidokoro/)

店舗情報：[資料1](https://tabelog.com/chiba/A1203/A120301/12068592/)

### CAFE-036 溶時

公式Instagramは公開プロフィール名とプロフィール画像のみ確認。投稿一覧・個別投稿は閲覧できず、投稿写真を確認したとはしていません。 公式プロフィールの白地に細い黒線、食べログの白い氷と淡い黄色のソース・木の卓上から、白と淡い黄、縦に余白をとる構成へ。かき氷の実商品写真は転載しない。 改良版では店舗写真の参考色を保ち、色面の明暗、店名の大小、写真の切り取りを再構成。書体はOFLのローカル配信。公式ロゴの再現ではありません。

配色参考：[資料1](https://tabelog.com/tokyo/A1304/A130401/13326656/)、[資料2](https://www.instagram.com/toki_kakigori/)

店舗情報：[資料1](https://tabelog.com/tokyo/A1304/A130401/13326656/)

### CAFE-037 Cache Cache

公式Instagramは公開プロフィール名とプロフィール画像のみ確認。投稿一覧・個別投稿は閲覧できず、投稿写真を確認したとはしていません。 公式プロフィールの円形セリフ文字、食べログの和紙の丸い照明・黒い窓枠・緑と木の床から、紙色・墨・黄土色、丸い灯りを思わせるアーチへ。 改良版では店舗写真の参考色を保ち、色面の明暗、店名の大小、写真の切り取りを再構成。書体はOFLのローカル配信。公式ロゴの再現ではありません。

配色参考：[資料1](https://tabelog.com/kanagawa/A1404/A140408/14105535/)、[資料2](https://www.instagram.com/maison.cachecache)

店舗情報：[資料1](https://tabelog.com/kanagawa/A1404/A140408/14105535/)

### CAFE-038 キッチンカーの古民家cafe Zen

公式Instagramは公開プロフィール名とプロフィール画像のみ確認。投稿一覧・個別投稿は閲覧できず、投稿写真を確認したとはしていません。 公式プロフィールの木地に墨の円、食べログの木枠の窓・濃い茶色の机・緑の器から、木色と墨緑、縦書きの余白と円形装飾へ。 改良版では店舗写真の参考色を保ち、色面の明暗、店名の大小、写真の切り取りを再構成。書体はOFLのローカル配信。公式ロゴの再現ではありません。

配色参考：[資料1](https://tabelog.com/kanagawa/A1404/A140406/14105729/)、[資料2](https://www.instagram.com/8453cafe.zen2490)

店舗情報：[資料1](https://tabelog.com/kanagawa/A1404/A140406/14105729/)

### CAFE-039 喫茶 Perla

公式Instagramは公開プロフィール名とプロフィール画像のみ確認。投稿一覧・個別投稿は閲覧できず、投稿写真を確認したとはしていません。 公式プロフィールの黒い看板と金色の文字、食べログの木の卓上・グレーの器・白壁から、墨青と控えめな金茶、細い額縁の構成へ。補助記事は取得503。 改良版では店舗写真の参考色を保ち、色面の明暗、店名の大小、写真の切り取りを再構成。書体はOFLのローカル配信。公式ロゴの再現ではありません。

配色参考：[資料1](https://tabelog.com/niigata/A1501/A150101/15025978/)、[資料2](https://www.instagram.com/kissa_perla/)

店舗情報：[資料1](https://tabelog.com/niigata/A1501/A150101/15025978/)、[資料2](https://r.gnavi.co.jp/k11bxjtf0000/)

### CAFE-040 甘味処 食べ鯛

公式Instagramは公開プロフィール名とプロフィール画像のみ確認。投稿一覧・個別投稿は閲覧できず、投稿写真を確認したとはしていません。 公式プロフィールの墨の六角形と小豆色、食べログの青い外壁・木の縦格子・たい焼きの焼き色から、藍と小豆・木色、和のポスター構成へ。 改良版では店舗写真の参考色を保ち、色面の明暗、店名の大小、写真の切り取りを再構成。書体はOFLのローカル配信。公式ロゴの再現ではありません。

配色参考：[資料1](https://tabelog.com/toyama/A1602/A160202/16012063/)、[資料2](https://www.instagram.com/tabetai_kanmidokoro/)

店舗情報：[資料1](https://tabelog.com/toyama/A1602/A160202/16012063/)、[資料2](https://toyama-watch.com/archives/29554)
