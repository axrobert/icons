# AXR Icon Design System V1

## Art direction

- Original illustrated mascots, friendly and clean, on vivid rounded square tiles. Inspired by the user's six-tile reference, not copied from it.
- SVG viewBox 0 0 96 96; background 94x94, x/y=1, rounded corners 23.
- White foreground silhouette, one distinct visual metaphor per technology; small expressive eyes where useful.
- Legible at 24 / 32 / 64 / 128px, optical mass consistent between stacks.
- No vendor-logo tracing, raster images, text inside tiles, icon fonts, remote assets, purple blanket palettes, complex 3D, blur, excess bloom or generic brand SVG downloads.
- Distinct personality: e.g. databases as containers/creatures, Docker as friendly cargo character, Linux as original penguin-inspired character (not the Tux trademark illustration).

## AI production workflow

1. Inspect the user-provided moodboard and 4 approved AXR icons as references; do NOT trace their silhouettes.
2. Research the semantic meaning of the stack to create a unique visual metaphor.
3. Draw standalone original SVG on the standard 96x96 grid; optimize paths manually or programmatically.
4. Check image at 24px and 32px on #0c1015 background; eyes and shape must remain distinguishable.
5. Validate safe SVG; reject script, foreignObject, external href/font/image and event handlers.
6. Add `icons/<slug>.svg` and record in `registry.json`; update previews.
7. Review visual quality in gallery before merging. Never call an unreviewed icon final.

## Generation prompt

> Generate an original technology mascot icon for {stack} in AXR Icon System. Match approved SVG icon sources for geometry and optical weight. 96x96 viewBox, 94x94 rounded 23px colorful tile, large central white illustrated mascot with distinct technology-inspired silhouette, optional two small charcoal eyes, tiny playful spark, minimal gentle shading. Must be readable at 24px. Deliver standalone safe SVG and registry entry. Avoid corporate logo copies, emoji and generic stock vectors.

## Next steps

Replace V1 geometric placeholder shapes with technology-specific mascots, one at a time, with visual approval; run SVG lint + screenshot comparisons; then integrate into AXR Stats with fallback for unknown stacks.
