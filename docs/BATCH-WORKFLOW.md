# AXR Icons — six-icon production pipeline

## Current release gate
**No new generated artwork has been approved or merged.** The old SVGs remain under `icons/` and will not be replaced by a traced experiment.

## Batch plan (6 at a time)

| Batch | Stack slugs | Status |
|---|---|---|
| 01 | linux, github, python, javascript, typescript, html | Artwork generation pending — automated image service unavailable this turn |
| 02 | css, git, docker, kubernetes, rust, react | Not started |
| 03 | nextjs, nodejs, postgresql, mysql, mongodb, redis | Not started |
| 04 | go, java, c, cpp, bash, archlinux | Not started |
| 05 | ubuntu, debian, windows, macos, figma, tailwindcss | Not started |

## Strict art-first process
1. Generate **ONE 3×2 raster sheet containing six isolated tiles only**. The art direction is the user's six-icon flat reference, not the later glossy thirty-icon experiment.
2. Approve the complete sheet. All six tiles must be the same dimensions, padding, perspective (orthographic / flat 2D) and optical weight.
3. Export six individually cropped **RGBA PNGs** at 512×512. Keep the untouched original generated sheet.
4. Trace each raster illustration into genuine closed **SVG paths** (not `<image href="data:image/png...">`, not a giant base64 raster inside XML).
5. Compare actual PNG and SVG at 16, 24, 32, 64 and 128px. Refine contour geometry manually where automated tracing loses face, details or color layers.
6. Publish first in `artwork/candidates/batch-XX/` with a contact sheet. **Do not overwrite `icons/*.svg` automatically**.
7. Only after visual approval update `icons/` and `registry.json`, and keep the README gallery showing the production-approved SVGs.

## Image prompt for batch 01
> Generate EXACTLY SIX individual original, flat-design mascot icons on an evenly spaced 3 columns × 2 rows sheet. Top: Linux (little friendly penguin), GitHub (white cat-like mascot), Python (coiled snake). Bottom: JavaScript (friendly lightning character), TypeScript (symmetrical document creature), HTML (folded markup-fox). Each has its own colorful, high-contrast rounded square background. Central white silhouette, small dark oval eyes, at most one secondary detail per icon. Sharp professional minimal app-icon illustration, unmistakable technology-inspired characters, even optical dimensions, consistent round corner radii and margins. No labels, no typography, no logos copied from vendors, no glow, no 3D, no chrome, no plastic, no excessive decoration, no drop shadows around the tile. Generous constant gap between tiles on a nearly black plain background. Legible at 24px.

## Acceptance criteria
- No copy-paste of same character body for different stacks.
- Consistent icon silhouette height, tile radius, visual mass and spacing.
- No complex rendering that turns into ugly contour noise during vectorization.
- SVG shape paths editable; no raster references or external assets.
- GitHub CI may test technical properties, but **human visual review remains the release gate**.
- Preserve PNG as canonical illustration reference even when exporting SVG.

## Local conversion
```bash
python -m pip install -r scripts/requirements-artwork.txt
python scripts/sheet_to_assets.py sheet.png --out artwork/candidates/batch-01 --names linux github python javascript typescript html
```

The script is a technical starting point for flat white mascots on colored tiles, **not a universal pixel-perfect vectorizer**. It intentionally rejects some complex sheets; do not claim quality merely because it produced six .svg files.
