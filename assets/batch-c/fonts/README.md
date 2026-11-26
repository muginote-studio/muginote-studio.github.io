# Local web fonts for batch C

These WOFF2 files are subsets of the open-source Google Fonts distributions. The original SIL Open Font License 1.1 texts and copyright notices are bundled. See sources.json for exact upstream files, license URLs, modifications, weight ranges and checksums.

- noto-serif-jp.woff2 — Noto Serif JP, normal 400–600
- noto-sans-jp.woff2 — Noto Sans JP, normal 400–600
- bodoni-moda.woff2 — Bodoni Moda, normal 400–700, optical size frozen at 48
- bodoni-moda-italic.woff2 — Bodoni Moda, italic 400–700, optical size frozen at 48
- dm-sans.woff2 — DM Sans, normal 400–700, optical size frozen at 14

Use local @font-face declarations with font-display: swap and system fallbacks. Japanese text added later must be checked against the subset character map; absent glyphs should fall back to a system font. Fonts contain the current HTML/editorial text, Latin, Japanese kana and punctuation, rather than the entire CJK character repertoire.
