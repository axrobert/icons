# Artwork specification and limitations

This collection consists of 126 illustrated, technology-inspired tiles, with an RGBA pixel master and multiple export formats per icon.

## Preservation policy

The imported PNGs are copied without editing pixels, recoloring, cropping or regenerating. They retain the original per-tile artwork. A curated second variant was already selected for HTML, CSS and Git in the input pack; the imported masters follow that selection.

## Quality gate

1. The 126 slugs must be unique and mapped to the intended technology.
2. All PNG sizes must be present, correctly sized, and transparent at the outer corners.
3. Raster SVG wrappers must be clearly labeled **embedded PNG**.
4. The automatically traced vector variant must contain true paths and must not embed images, JavaScript, remote URLs or event handlers.
5. Preview the collection together and inspect small-size legibility, padding and halos before treating it as production-ready.
6. Revisit individual vectors if near-pixel fidelity matters; do not silently treat them as a replacement for raster sources.

## Adding new icons

Produce only **six icons at a time**, based on approved existing illustrations. First generate/edit the raster artwork; then extract its PNG master, export sizes, trace to editable SVG, check small sizes and add a unique registry entry. Keep drafts isolated, do not replace existing approved icons without reviewing the diff. Do not copy protected vendor logos or claim that these designs are official.

## Legal

Technology names and vendor identities are trademarks of their owners. This package does not constitute affiliation or endorsement. No open-source license has been chosen for the artwork; do not assume reuse rights until the repository owner adds an explicit license.
