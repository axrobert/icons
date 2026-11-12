# AI Icon Creation Contract

## Template for generating a new stack mascot

Create an ORIGINAL, technology-inspired SVG mascot icon for `{STACK}` with slug `{SLUG}`. Read `docs/DESIGN-SYSTEM.md` and THREE approved icons in this repository. The reference moodboard defines the overall aesthetic, not copyable silhouettes.

- Tile geometry: viewBox 0 0 96 96, x=1 y=1 w=94 h=94 rx=23.
- Choose a distinct gradient pair in colors characteristic of the concept; central dominant white mascot, subtle dark small oval eyes as appropriate.
- Convey the technology via a friendly pictorial metaphor; avoid direct reproductions of company logos.
- No duplicate silhouettes from previous icons, no generic SVG packs, no embedded images, no external assets, no scripts, no animation, no text inside the icon.
- Remain legible at 24, 32 and 64 px; use few high-quality curves and large forms. High optical consistency, not merely equal SVG canvas dimensions.
- Keep the resulting source editable and accessible with `<title>`.

Then add `icons/{SLUG}.svg` and its record in `registry.json`; run `python scripts/validate.py`. Present a rendered 24px / 32px / 64px comparison for human review. Passing lint does not prove the design is ready. No copy-pasted brand marks.
