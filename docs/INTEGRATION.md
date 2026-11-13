# Integrating AXR Icons

## Source of truth

- `registry.json` has one record per icon. All asset paths are repository-relative.
- PNG 64 is the recommended format for on-screen stack tiles. Use PNG 32 at 1x or 64 at 2x for a 32 CSS-pixel tile; select the proper density using `srcset`.
- PNG 256 is the best visual master in this package. Do not claim the auto-traced SVGs reproduce its gradients exactly.
- SVG `vector` is editable contour art, not guaranteed pixel-perfect.
- SVG `fidelity` embeds an actual PNG, so **it is not a true editable vector**.

## JavaScript usage

```js
import registry from './registry.json' with { type: 'json' };
import { buildStackIndex, resolveIcon } from './src/resolve.mjs';

const index = buildStackIndex(registry);
const path = resolveIcon(index, 'Next.js', { format: 'png', size: 64 });
// assets/png/64/013-next-js.png
const svg = resolveIcon(index, 'C++', { format: 'svg', svgVariant: 'vector' });
// assets/svg/vector/022-cpp.svg
```

In a browser using a static site, load the registry through `fetch` rather than JSON import if broad support is needed. Build your own fallback for stacks not present in the catalog. Never load an untrusted SVG into an inline DOM container; using an `<img>` is safer for image display.

## Example for an app running in a subpath

```js
const img = document.createElement('img');
img.src = new URL(path, 'https://example.com/my-icons/').toString();
img.width = 32;
img.height = 32;
img.alt = 'Next.js';
```

Pin an immutable commit/tag or bundle the assets into the app. Do not depend on the mutable PR branch in production.

## Overlay into the existing GitHub branch

This package is a prepared working-tree **overlay**, not a git clone. It can be copied into the reviewed `axrobert/icons` feature branch after approval. Its `README.md`, `index.html`, `style.css`, `registry.json`, validation script and documentation replace the old draft equivalents. The old `icons/*.svg` prototypes are not removed by this overlay; leave them untouched until a separately reviewed cleanup removes or archives them. Do not mix `icons/*.svg` (old prototypes) with the new `assets/` collection in consumer apps.

The legacy `scripts/sheet_to_assets.py` is a generator for new candidate art, not the source of truth for this supplied 126-piece collection.
