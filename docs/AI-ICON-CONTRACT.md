# AXR Icons — AI-assisted illustration contract

**Canonical workflow: image first, SVG second.** Do NOT write the final icon's SVG geometry from a language-model text prompt.

1. Read `docs/BATCH-WORKFLOW.md`, reference the *flat, minimalist six-tile moodboard* and the existing approved PNGs, not only the old unapproved SVGs.
2. Generate exactly **six** different technology mascots in one equally spaced 3×2 sheet, never thirty.
3. Require 2D flat vector-like illustration, no 3D, gloss, lighting bloom, typography, raster noise or vendor logo tracing.
4. Obtain visual approval and extract six separate transparent PNG files.
5. Trace from those PNGs to actual closed SVG paths with `scripts/sheet_to_assets.py`. Clean the resulting paths and restore intentionally different colors; automated tracing can lose details.
6. Compare PNG/SVG side by side at **16, 24, 32, 64 px**. Reject low-quality contours and tiny facial details that turn into blobs.
7. Stage the output separately, never overwrite `icons/` without approval. Approved assets must remain separately available as PNG and SVG.
8. Update the README six-at-a-time and keep the complete 30-icon production gallery side by side.

**Important:** raster inside SVG (`<image>` + base64) is not vectorization. A traced SVG made of hundreds of noisy paths is also not an acceptable final design.
