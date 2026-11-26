# Batch A: CAFE-011–CAFE-040

30店舗の自主制作・非公式トップページです。店舗未承認のデザイン案として、各ページに noindex,nofollow とイメージ写真の表示を置いています。

## 編集範囲

追加は30店舗の index.html、assets/batch-a/、collections/batch-a.json のみ。共通一覧・共有CSS/JS・cafes.json・既存店舗は変更していません。mainから始めた専用ブランチで納品し、統合・公開は担当外です。

## 確認方法

リポジトリのルートで実行します。

```sh
python3 scripts/check_presentation.py
python3 assets/batch-a/verify.py
node --check assets/batch-a/site.js
node --test assets/batch-a/check-menu.cjs
```

ページは静的HTMLのためJavaScriptなしでも本文・リンク・ナビゲーションを利用できます。JavaScriptはモバイルナビゲーションの開閉にのみ使用しています。

## ルートと配色

配色は順に背景・本文・アクセント・補助背景。店舗のブランド規定色を示すものではありません。

| ID | 店名・ルート | 配色 | 構成 |
| --- | --- | --- | --- |
| CAFE-011 | [Hoki Cafe](../../hoki-cafe/) · `/hoki-cafe/` | #f2eee4 / #183141 / #7c570e / #ded3ac | split |
| CAFE-012 | [喫茶ブロンディー](../../kissa-blondy/) · `/kissa-blondy/` | #f2e6ce / #3c241d / #763d27 / #deca9f | frame |
| CAFE-013 | [Asile](../../asile/) · `/asile/` | #f4efe5 / #382b23 / #6d3c36 / #dbceb3 | diptych |
| CAFE-014 | [中野珈琲店](../../nakano-coffee/) · `/nakano-coffee/` | #edf0eb / #29382e / #4a6150 / #ced5c9 | letter |
| CAFE-015 | [まんがめし喫茶 ひよこ堂](../../hiyokodo/) · `/hiyokodo/` | #f7efce / #303c30 / #9b3125 / #e4c46a | poster |
| CAFE-016 | [喫茶 夜 桜山](../../kissa-yoru-sakurayama/) · `/kissa-yoru-sakurayama/` | #20231f / #f5efdf / #e5bc77 / #373c33 | night |
| CAFE-017 | [cafe MARM](../../cafe-marm/) · `/cafe-marm/` | #faf7ef / #3f332b / #895344 / #e5d5bb | grid |
| CAFE-018 | [蚯蚓](../../mimizu/) · `/mimizu/` | #ede2d2 / #3d2e29 / #99502d / #d4b08a | editorial |
| CAFE-019 | [KO-MEGURI](../../ko-meguri/) · `/ko-meguri/` | #f5f3e9 / #374334 / #566746 / #dce1ce | arch |
| CAFE-020 | [きゃどぽんぽんじ〜な](../../kyado-ponponjina/) · `/kyado-ponponjina/` | #e8ece9 / #273c3d / #78513b / #bdcfc7 | split |
| CAFE-021 | [CAFE & DINING Le Lien](../../le-lien/) · `/le-lien/` | #f9f0e9 / #4f3e35 / #8b4b41 / #e8d2be | diptych |
| CAFE-022 | [くまきち日和](../../kumakichi-biyori/) · `/kumakichi-biyori/` | #edece1 / #303e34 / #4d6850 / #d0d6bf | vertical |
| CAFE-023 | [なんでもない日に、踊ろうよ](../../nandemonaihi/) · `/nandemonaihi/` | #f6efe3 / #423c2e / #8c4630 / #e7ceb3 | letter |
| CAFE-024 | [Green & Cafe HANA](../../green-cafe-hana/) · `/green-cafe-hana/` | #edf1e6 / #2c422e / #486738 / #cbd9b5 | garden |
| CAFE-025 | [Re:sky](../../resky/) · `/resky/` | #f3e9dd / #282d33 / #a74432 / #e6c5a7 | poster |
| CAFE-026 | [Quebec亭](../../quebectei/) · `/quebectei/` | #f1e9da / #44392d / #82633f / #dac7a5 | frame |
| CAFE-027 | [FUFUFU](../../fufufu/) · `/fufufu/` | #e9e8dd / #2e3b32 / #536a4c / #c9ccb5 | editorial |
| CAFE-028 | [my.Honey](../../my-honey/) · `/my-honey/` | #fff4c7 / #382e24 / #923b2d / #edbe52 | pop |
| CAFE-029 | [Le’Chainon](../../le-chainon/) · `/le-chainon/` | #f5edf5 / #48364a / #725274 / #d8c8e3 | pop |
| CAFE-030 | [アメリカンダイナーHOODHOUSE](../../hoodhouse/) · `/hoodhouse/` | #f3dfb5 / #282522 / #982d26 / #e8b64d | diner |
| CAFE-031 | [聖奈珈琲](../../sena-coffee/) · `/sena-coffee/` | #f3eee5 / #46362d / #784738 / #d8c6ad | letter |
| CAFE-032 | [BOUNCE](../../bounce/) · `/bounce/` | #f0f3ed / #244432 / #3f634b / #d5dfd0 | grid |
| CAFE-033 | [cafe tarte plus](../../tarte-plus/) · `/tarte-plus/` | #f5eae1 / #4c3937 / #8d5255 / #dfc4b5 | arch |
| CAFE-034 | [vigo](../../vigo/) · `/vigo/` | #f0ece0 / #323e30 / #516347 / #d6ccb1 | garden |
| CAFE-035 | [ちょい呑み処ten](../../ten/) · `/ten/` | #f5eed8 / #30463a / #48634d / #d8bca0 | diptych |
| CAFE-036 | [溶時](../../toki/) · `/toki/` | #f7f5eb / #40433e / #756536 / #e5dfbe | vertical |
| CAFE-037 | [Cache Cache](../../cache-cache/) · `/cache-cache/` | #f3eee6 / #413d32 / #74633e / #d6ccb8 | arch |
| CAFE-038 | [キッチンカーの古民家cafe Zen](../../cafe-zen/) · `/cafe-zen/` | #eae7da / #343b2d / #56613b / #c7c9b0 | vertical |
| CAFE-039 | [喫茶 Perla](../../kissa-perla/) · `/kissa-perla/` | #eee9df / #30383e / #645740 / #d1c9ba | frame |
| CAFE-040 | [甘味処 食べ鯛](../../tabetai/) · `/tabetai/` | #f1e8d9 / #183d4e / #7d4739 / #d7b990 | poster |

## 店舗ごとの参考資料と確認範囲

確認日：2026年11月26日。第三者の掲載情報は店舗の現在の営業を保証するものではありません。価格・口コミ・未確認の由来や連絡先は本文に採用していません。

### CAFE-011 Hoki Cafe

公式Instagramは公開プロフィール名とプロフィール画像のみ確認。投稿一覧・個別投稿は閲覧できず、投稿写真を確認したとはしていません。 公式プロフィール画像の濃紺の板壁と黄色の文字、食べログの明るい窓辺・木製家具から、紺と黄土色、直線的な分割構成へ。

配色・写真の参考：[資料1](https://tabelog.com/hokkaido/A0104/A010401/1086431/)、[資料2](https://www.instagram.com/hokicafe1026)

店舗情報の根拠：[資料1](https://tabelog.com/hokkaido/A0104/A010401/1086431/)、[資料2](https://www.shopship.jp/asahikawa/open-close/hokicafe1026/)

### CAFE-012 喫茶ブロンディー

公式Instagramのプロフィール・投稿は直接確認できませんでした。公開の店舗写真を補助資料にしています。 食べログの白いカップの茶色の縁、濃茶の卓上、柄入りの椅子と暗めの店内写真から、琥珀・焦茶と額縁型の構図へ。Instagramはプロフィールも直接確認できず。

配色・写真の参考：[資料1](https://tabelog.com/hokkaido/A0101/A010305/1086434/)、[資料2](https://www.instagram.com/blondy_roastery)

店舗情報の根拠：[資料1](https://tabelog.com/hokkaido/A0101/A010305/1086434/)、[資料2](https://plaza.rakuten.co.jp/yorozuken/diary/202610240003/)

### CAFE-013 Asile

公式Instagramは公開プロフィール名とプロフィール画像のみ確認。投稿一覧・個別投稿は閲覧できず、投稿写真を確認したとはしていません。 公式プロフィールの細い金色の文字と植物、食べログのワイン・木のカウンターから、クリームとワイン色、細い明朝と二連写真へ。

配色・写真の参考：[資料1](https://tabelog.com/aomori/A0201/A020101/2014023/)、[資料2](https://www.instagram.com/asile_369_/)

店舗情報の根拠：[資料1](https://tabelog.com/aomori/A0201/A020101/2014023/)、[資料2](https://www.acci.or.jp/salon/【会員事業所紹介】カフェ・バル-asile/)

### CAFE-014 中野珈琲店

公式Instagramは公開プロフィール名とプロフィール画像のみ確認。投稿一覧・個別投稿は閲覧できず、投稿写真を確認したとはしていません。 食べログの白壁と暗い木のカウンター、窓外の緑から、白灰・深緑と便箋のような端正な文字組みへ。営業時間は新聞記事と食べログに相違があるため現行未確認。

配色・写真の参考：[資料1](https://tabelog.com/aomori/A0202/A020201/2014002/)、[資料2](https://www.instagram.com/nakanocoffee10/)

店舗情報の根拠：[資料1](https://tabelog.com/aomori/A0202/A020201/2014002/)、[資料2](https://hirosaki.keizai.biz/headline/2773/)

### CAFE-015 まんがめし喫茶 ひよこ堂

公式Instagramは公開プロフィール名とプロフィール画像のみ確認。投稿一覧・個別投稿は閲覧できず、投稿写真を確認したとはしていません。 食べログの本棚、木の机、赤いカウンター椅子と緑の壁から、紙色・赤・深緑、紙面を組むようなポスター構成へ。プロフィールの既存キャラクターは複製しない。

配色・写真の参考：[資料1](https://tabelog.com/iwate/A0301/A030103/3013251/)、[資料2](https://www.instagram.com/hiyoko_dou/)

店舗情報の根拠：[資料1](https://tabelog.com/iwate/A0301/A030103/3013251/)、[資料2](https://kaiten-heiten-24.com/hiyoko-dou/)

### CAFE-016 喫茶 夜 桜山

公式Instagramは公開プロフィール名とプロフィール画像のみ確認。投稿一覧・個別投稿は閲覧できず、投稿写真を確認したとはしていません。 公式プロフィールの余白を生かした縦の文字、食べログの暗い木の机・ランプの灯りから、墨緑と琥珀、縦組みの余白へ。

配色・写真の参考：[資料1](https://tabelog.com/iwate/A0301/A030101/3013416/)、[資料2](https://www.instagram.com/sakurayama_yoru/)

店舗情報の根拠：[資料1](https://tabelog.com/iwate/A0301/A030101/3013416/)

### CAFE-017 cafe MARM

公式Instagramは公開プロフィール名とプロフィール画像のみ確認。投稿一覧・個別投稿は閲覧できず、投稿写真を確認したとはしていません。 公式プロフィールの黒い太字MARMと白地、食べログの豆皿・淡い木の卓上から、白と茶、整然としたグリッドへ。

配色・写真の参考：[資料1](https://tabelog.com/miyagi/A0404/A040404/4030479/)、[資料2](https://www.instagram.com/cafe.marm)

店舗情報の根拠：[資料1](https://tabelog.com/miyagi/A0404/A040404/4030479/)、[資料2](https://freimann.hatenablog.com/entry/2026/10/09/170000)

### CAFE-018 蚯蚓

公式Instagramは公開プロフィール名とプロフィール画像のみ確認。投稿一覧・個別投稿は閲覧できず、投稿写真を確認したとはしていません。 公式プロフィールの茶色の線画、食べログの褐色の器・オレンジの椅子・木の棚から、土色と焼けた橙、雑誌風の大小写真へ。

配色・写真の参考：[資料1](https://tabelog.com/miyagi/A0401/A040105/4030460/)、[資料2](https://www.instagram.com/mimizu_kaffee)

店舗情報の根拠：[資料1](https://tabelog.com/miyagi/A0401/A040105/4030460/)、[資料2](https://sendaiminami-tusin.com/mimizu2610/)

### CAFE-019 KO-MEGURI

公式Instagramは公開プロフィール名とプロフィール画像のみ確認。投稿一覧・個別投稿は閲覧できず、投稿写真を確認したとはしていません。 公式プロフィールの木目の丸い看板、食べログの白い椅子・植物柄・緑の鉢から、白とオリーブ、アーチと植物の線へ。補助ブログは503。

配色・写真の参考：[資料1](https://tabelog.com/akita/A0505/A050501/5011649/)、[資料2](https://www.instagram.com/ko_meguri.cafe/)

店舗情報の根拠：[資料1](https://tabelog.com/akita/A0505/A050501/5011649/)

### CAFE-020 きゃどぽんぽんじ〜な

公式Instagramは公開プロフィール名とプロフィール画像のみ確認。投稿一覧・個別投稿は閲覧できず、投稿写真を確認したとはしていません。 食べログとあきたタウン情報の青緑の壁・木製椅子・琥珀色の飲み物から、青緑と栗色、丸みを抑えた横長構成へ。店名由来は本文に採用しない。

配色・写真の参考：[資料1](https://tabelog.com/akita/A0501/A050101/5011631/)、[資料2](https://www.instagram.com/pon.pon_cafe/)

店舗情報の根拠：[資料1](https://tabelog.com/akita/A0501/A050101/5011631/)、[資料2](https://web.akita-townjoho.jp/post-category/20260430-kyadoponponjina/)

### CAFE-021 CAFE & DINING Le Lien

公式Instagramは公開プロフィール名とプロフィール画像のみ確認。投稿一覧・個別投稿は閲覧できず、投稿写真を確認したとはしていません。 公式プロフィールの端正なセリフ体、食べログの淡いカウンター・ピンクと黄の外壁から、淡い桃と赤茶、二つの時間を見せる構成へ。

配色・写真の参考：[資料1](https://tabelog.com/yamagata/A0602/A060202/6013562/)、[資料2](https://www.instagram.com/cafe_lelien2026)

店舗情報の根拠：[資料1](https://tabelog.com/yamagata/A0602/A060202/6013562/)

### CAFE-022 くまきち日和

公式Instagramは公開プロフィール名とプロフィール画像のみ確認。投稿一覧・個別投稿は閲覧できず、投稿写真を確認したとはしていません。 公式プロフィールの墨の古民家線画、食べログの畳・濃い梁・窓の緑・青い器から、畳色と深緑、縦書きの導入へ。食べログの古い開業予定記述は営業時間に使わない。

配色・写真の参考：[資料1](https://tabelog.com/yamagata/A0602/A060203/6013674/)、[資料2](https://www.instagram.com/kumakichi_biyori_yamagata.cafe)

店舗情報の根拠：[資料1](https://tabelog.com/yamagata/A0602/A060203/6013674/)、[資料2](https://camp-fire.jp/projects/977512/view?list=prefecture_yamagata_projects_fresh)、[資料3](https://camp-fire.jp/projects/977512/view/activities/910342)

### CAFE-023 なんでもない日に、踊ろうよ

公式Instagramは公開プロフィール名とプロフィール画像のみ確認。投稿一覧・個別投稿は閲覧できず、投稿写真を確認したとはしていません。 公式プロフィールの朱色の線画、食べログの畳・木枠の窓・クリームソーダの緑から、紙色と朱茶、手紙のように読み進める構成へ。

配色・写真の参考：[資料1](https://tabelog.com/yamagata/A0603/A060303/6013517/)、[資料2](https://www.instagram.com/nandemonaihini_/)

店舗情報の根拠：[資料1](https://tabelog.com/yamagata/A0603/A060303/6013517/)、[資料2](https://yama-katsu.jp/press/30267/)、[資料3](https://yuzamachi.com/taberu/nandemonaihini/2026/07/14/)

### CAFE-024 Green & Cafe HANA

公式Instagramは公開プロフィール名とプロフィール画像のみ確認。投稿一覧・個別投稿は閲覧できず、投稿写真を確認したとはしていません。 公式プロフィールのオリーブ色の植物・丸い看板、食べログの窓際の緑と木のテーブルから、葉色と白、窓形の写真枠へ。施設ニュースは本文の一次資料として採用。

配色・写真の参考：[資料1](https://tabelog.com/fukushima/A0704/A070401/7021049/)、[資料2](https://www.instagram.com/green_and_caffe_hana)

店舗情報の根拠：[資料1](https://tabelog.com/fukushima/A0704/A070401/7021049/)、[資料2](https://www.gurutto-iwaki.com/detail/1792/news/news-931717.html)

### CAFE-025 Re:sky

公式Instagramを同定できませんでした。公開の店舗紹介と食べログの写真を補助資料にしています。 食べログの白黒チェッカーのカウンター、赤い店内小物、木の床から、黒白とくすんだ赤、アメリカンポスターへ。公式Instagramは割当資料に記載がなく同定できず。

配色・写真の参考：[資料1](https://tabelog.com/fukushima/A0705/A070501/7020931/)

店舗情報の根拠：[資料1](https://tabelog.com/fukushima/A0705/A070501/7020931/)、[資料2](https://www.gurutto-aizu.com/detail/1158/index.html)

### CAFE-026 Quebec亭

公式Instagramのプロフィール・投稿は直接確認できませんでした。公開の店舗写真を補助資料にしています。 食べログの料理写真で確認できた木のトレー、茶褐色の器と濃い輪郭から、木色と茶、控えめな額縁構成へ。店内全景・Instagramプロフィールと投稿は未確認。

配色・写真の参考：[資料1](https://tabelog.com/ibaraki/A0805/A080503/8031302/)、[資料2](https://www.instagram.com/cafequebec2026/)

店舗情報の根拠：[資料1](https://tabelog.com/ibaraki/A0805/A080503/8031302/)

### CAFE-027 FUFUFU

公式Instagramは公開プロフィール名とプロフィール画像のみ確認。投稿一覧・個別投稿は閲覧できず、投稿写真を確認したとはしていません。 公式プロフィールの灰色地と手書き風白文字、食べログの木の外壁・緑・レコード周りから、灰緑と木色、雑誌のコラムのような配置へ。

配色・写真の参考：[資料1](https://tabelog.com/tochigi/A0901/A090101/9024341/)、[資料2](https://www.instagram.com/fufufu.store)

店舗情報の根拠：[資料1](https://tabelog.com/tochigi/A0901/A090101/9024341/)、[資料2](https://www.tochinavi.net/spot/newopen/detail.shtml?id=4313)

### CAFE-028 my.Honey

公式Instagramは公開プロフィール名とプロフィール画像のみ確認。投稿一覧・個別投稿は閲覧できず、投稿写真を確認したとはしていません。 公式プロフィールの蜂蜜色、食べログの黄色い外壁と赤い扉から、蜂蜜色と赤茶、丸い写真と太い文字へ。写真内の他店舗掲載に見える料理は参考から除外。

配色・写真の参考：[資料1](https://tabelog.com/tochigi/A0901/A090101/9024337/)、[資料2](https://www.instagram.com/myhoney1919)

店舗情報の根拠：[資料1](https://tabelog.com/tochigi/A0901/A090101/9024337/)、[資料2](https://utsunomiya.goguynet.jp/2026/07/14/my-honey/)

### CAFE-029 Le’Chainon

公式Instagramは公開プロフィール名とプロフィール画像のみ確認。投稿一覧・個別投稿は閲覧できず、投稿写真を確認したとはしていません。 公式プロフィールの水色・桃・緑の花、食べログのカラフルな花と紫の小物から、淡い紫とミントを手掛かりに、柔らかな円形構成へ。

配色・写真の参考：[資料1](https://tabelog.com/gunma/A1001/A100102/10027439/)、[資料2](https://www.instagram.com/le.chainon8787/)

店舗情報の根拠：[資料1](https://tabelog.com/gunma/A1001/A100102/10027439/)

### CAFE-030 アメリカンダイナーHOODHOUSE

公式Instagramは公開プロフィール名とプロフィール画像のみ確認。投稿一覧・個別投稿は閲覧できず、投稿写真を確認したとはしていません。 公式プロフィールの赤と黄の太字、食べログの黒白チェッカー床・暗い木のカウンターから、赤・黄・黒、太い文字と帯の構成へ。

配色・写真の参考：[資料1](https://tabelog.com/gunma/A1001/A100101/10026738/)、[資料2](https://www.instagram.com/hoodhouse_maebashi/)

店舗情報の根拠：[資料1](https://tabelog.com/gunma/A1001/A100101/10026738/)、[資料2](https://saikura.info/open-hood-house-maebashi-20261029/)

### CAFE-031 聖奈珈琲

公式Instagramは公開プロフィール名とプロフィール画像のみ確認。投稿一覧・個別投稿は閲覧できず、投稿写真を確認したとはしていません。 公式プロフィールの生成りと赤茶の明朝、食べログの白壁・木の天井・大きな窓から、生成りと赤茶、静かな便箋型へ。slugは指定どおりsena-coffee、店名表記を優先。

配色・写真の参考：[資料1](https://tabelog.com/gunma/A1002/A100202/10027456/)、[資料2](https://www.instagram.com/seinacoffee/)

店舗情報の根拠：[資料1](https://tabelog.com/gunma/A1002/A100202/10027456/)

### CAFE-032 BOUNCE

公式Instagramは公開プロフィール名とプロフィール画像のみ確認。投稿一覧・個別投稿は閲覧できず、投稿写真を確認したとはしていません。 公式プロフィールの深緑のセリフ体、食べログの白い壁・灰色の床・緑の植物から、白と深緑、余白のある整ったグリッドへ。

配色・写真の参考：[資料1](https://tabelog.com/saitama/A1105/A110503/11068999/)、[資料2](https://www.instagram.com/bounce.wellness)

店舗情報の根拠：[資料1](https://tabelog.com/saitama/A1105/A110503/11068999/)

### CAFE-033 cafe tarte plus

公式Instagramは公開プロフィール名とプロフィール画像のみ確認。投稿一覧・個別投稿は閲覧できず、投稿写真を確認したとはしていません。 公式プロフィールの茶地と白文字、食べログの淡い壁・赤茶の腰壁・丸い照明・曲線のモールから、ローズブラウンとアーチの構成へ。

配色・写真の参考：[資料1](https://tabelog.com/saitama/A1104/A110402/11068975/)、[資料2](https://www.instagram.com/cafe_tarte_plus)

店舗情報の根拠：[資料1](https://tabelog.com/saitama/A1104/A110402/11068975/)、[資料2](https://kuki-satte.goguynet.jp/2026/11/07/tarte-plus/)

### CAFE-034 vigo

公式Instagramは公開プロフィール名とプロフィール画像のみ確認。投稿一覧・個別投稿は閲覧できず、投稿写真を確認したとはしていません。 公式プロフィールのモノクロの鹿と植物の線画、食べログの木の梁・白壁・植物から、墨緑と木色、温室を連想する窓枠へ。鹿のロゴは複製しない。

配色・写真の参考：[資料1](https://tabelog.com/chiba/A1201/A120101/12068435/)、[資料2](https://www.instagram.com/vigo_waffle)

店舗情報の根拠：[資料1](https://tabelog.com/chiba/A1201/A120101/12068435/)、[資料2](https://www.gummaumaimono.info/entry/2026/10/15/214835)

### CAFE-035 ちょい呑み処ten

公式Instagramは公開プロフィール名とプロフィール画像のみ確認。投稿一覧・個別投稿は閲覧できず、投稿写真を確認したとはしていません。 公式プロフィールの生成りと黒い円、食べログの深緑の壁・花柄のテーブルクロス・木の床から、生成りと深緑、昼夜の二連構成へ。

配色・写真の参考：[資料1](https://tabelog.com/chiba/A1203/A120301/12068592/)、[資料2](https://www.instagram.com/ten_choinomidokoro/)

店舗情報の根拠：[資料1](https://tabelog.com/chiba/A1203/A120301/12068592/)

### CAFE-036 溶時

公式Instagramは公開プロフィール名とプロフィール画像のみ確認。投稿一覧・個別投稿は閲覧できず、投稿写真を確認したとはしていません。 公式プロフィールの白地に細い黒線、食べログの白い氷と淡い黄色のソース・木の卓上から、白と淡い黄、縦に余白をとる構成へ。かき氷の実商品写真は転載しない。

配色・写真の参考：[資料1](https://tabelog.com/tokyo/A1304/A130401/13326656/)、[資料2](https://www.instagram.com/toki_kakigori/)

店舗情報の根拠：[資料1](https://tabelog.com/tokyo/A1304/A130401/13326656/)

### CAFE-037 Cache Cache

公式Instagramは公開プロフィール名とプロフィール画像のみ確認。投稿一覧・個別投稿は閲覧できず、投稿写真を確認したとはしていません。 公式プロフィールの円形セリフ文字、食べログの和紙の丸い照明・黒い窓枠・緑と木の床から、紙色・墨・黄土色、丸い灯りを思わせるアーチへ。

配色・写真の参考：[資料1](https://tabelog.com/kanagawa/A1404/A140408/14105535/)、[資料2](https://www.instagram.com/maison.cachecache)

店舗情報の根拠：[資料1](https://tabelog.com/kanagawa/A1404/A140408/14105535/)

### CAFE-038 キッチンカーの古民家cafe Zen

公式Instagramは公開プロフィール名とプロフィール画像のみ確認。投稿一覧・個別投稿は閲覧できず、投稿写真を確認したとはしていません。 公式プロフィールの木地に墨の円、食べログの木枠の窓・濃い茶色の机・緑の器から、木色と墨緑、縦書きの余白と円形装飾へ。

配色・写真の参考：[資料1](https://tabelog.com/kanagawa/A1404/A140406/14105729/)、[資料2](https://www.instagram.com/8453cafe.zen2490)

店舗情報の根拠：[資料1](https://tabelog.com/kanagawa/A1404/A140406/14105729/)

### CAFE-039 喫茶 Perla

公式Instagramは公開プロフィール名とプロフィール画像のみ確認。投稿一覧・個別投稿は閲覧できず、投稿写真を確認したとはしていません。 公式プロフィールの黒い看板と金色の文字、食べログの木の卓上・グレーの器・白壁から、墨青と控えめな金茶、細い額縁の構成へ。補助記事は取得503。

配色・写真の参考：[資料1](https://tabelog.com/niigata/A1501/A150101/15025978/)、[資料2](https://www.instagram.com/kissa_perla/)

店舗情報の根拠：[資料1](https://tabelog.com/niigata/A1501/A150101/15025978/)、[資料2](https://r.gnavi.co.jp/k11bxjtf0000/)

### CAFE-040 甘味処 食べ鯛

公式Instagramは公開プロフィール名とプロフィール画像のみ確認。投稿一覧・個別投稿は閲覧できず、投稿写真を確認したとはしていません。 公式プロフィールの墨の六角形と小豆色、食べログの青い外壁・木の縦格子・たい焼きの焼き色から、藍と小豆・木色、和のポスター構成へ。

配色・写真の参考：[資料1](https://tabelog.com/toyama/A1602/A160202/16012063/)、[資料2](https://www.instagram.com/tabetai_kanmidokoro/)

店舗情報の根拠：[資料1](https://tabelog.com/toyama/A1602/A160202/16012063/)、[資料2](https://toyama-watch.com/archives/29554)

## 写真の利用条件

掲載素材は既存リポジトリの assets/photos.json に出典があるUnsplash写真から選び、担当専用のディレクトリへ同一バイトで複製しました。[Unsplash License](https://unsplash.com/license)で利用条件を確認しています。原画像URL・ライセンスURL・SHA-256は image-sources.json にあります。実店舗写真は配色調査のみで、掲載・埋め込み・直リンク表示をしていません。写真近傍・alt・フッターでイメージ素材であることを明記しています。

## 検証結果と限界

- 30ページ・ID範囲・指定ルート・一覧データの必須項目・画像ファイル・内部リンク・アンカー・h1・SVGアクセシビリティ・noindex・非公式表示を静的検査。
- 基本文字色のコントラストは全30件で4.5:1以上（最低4.57:1）。
- JavaScript構文とモバイルメニューの5ケースをNodeで検査。これはブラウザ上の検査ではありません。
- 外部URLは120件をGET確認し119件がHTTP 200。Unsplash Licenseの直接GETのみ401でしたが、同URLの本文はWeb検索ツールで確認できています。HTTP 200はInstagram投稿の閲覧や店舗の営業継続を保証しません。
- 390px付近用のメディアクエリ・長文折り返し・縦組み・メニュー状態の静的検査を実施。
- ブラウザ初期化は `the gaas-browser node_repl sandbox cannot be disabled`、管理プレビューは `relay could not open browser port 4173` で失敗。デスクトップ・390pxの実描画、画像の実描画、タップ操作、Safari/WebKitは未検証です。
- 公式Instagramの個別投稿・投稿一覧は全店未確認。27店舗は公開プロフィール名・プロフィール画像のみを確認。喫茶ブロンディーとQuebec亭はプロフィールも直接確認できず、Re:skyは公式アカウントを同定できませんでした。
- くまきち日和は食べログの開業予定表記が古いため営業時間に使わず、開業報告を採用。中野珈琲店は資料間で営業時間が異なるため掲載を省略。
- Green & Cafe HANA、Quebec亭、tarte plus、Cache Cacheなど、掲載上の時間を確認できない店舗は公式案内へ誘導。全店舗の臨時休業・現行メニュー・写真転載許諾は確認できていません。店舗写真は掲載していません。
