# Atelier Collection

100 parallel cafe homepage proposals, based on Uff's composition: split photographic hero, generous margins, arched story photograph, offset image pair, quiet interlude and practical visit information.

- New collection: `/atelier/`, with stores at `/atelier/<existing-slug>/`.
- Every existing store page, `/archive/batch-a-v1/`, and the previous image archives are retained. The root gallery only gains a link to this collection. Each new page links back to its previous version.
- `content.json` records text and public contact/source links imported from the previously published proposals, plus a SHA-256 of each unchanged source HTML. This is a visual redesign, not a new verification of current menus, store operation or Instagram posts.
- Store names, introductions, addresses, opening-hour caveats, article sources and known Instagram/maps links are retained. Menu names and capacities appear only when already recorded. No prices, testimonials, booking functions or business histories are invented. All pages are `noindex,nofollow`, unofficial and visibly unapproved by the shops.
- Store colors derive from the existing design research, adjusted for legible dark text on light paper. Body text is 16px. Japanese display type is a self-hosted Noto Serif JP subset; Roman display type reuses licensed Cormorant Garamond. Main text contrast is at least 7:1 against the page background. Long names wrap. Mobile navigation supports Escape with focus restoration.
- All photos are attributed, existing Unsplash stock assets, labeled as illustrations. They do not depict the actual shops or products. See `photo-sources.json` for hashes and URLs; see `font-sources.json` and `fonts/mincho-OFL.txt` for font provenance. Decorative marks are inline SVG to avoid emoji substitution in Safari.

Rebuild with `python3 scripts/build_atelier.py` (requires Pillow). If new text introduces Japanese characters, update the font subset using the source and processing recorded in `font-sources.json`.

Before publication, run `python3 scripts/check_presentation.py`, `python3 scripts/check_collection.py`, `python3 scripts/check_atelier.py`, and `node --check assets/atelier/site.js`. Browser verification and platform limits are reported with the delivery.
