# AXR Icons — visual refinement QA

## V3 — Pilot refinement

The following 8 mascots have been redrawn with more deliberate forms, facial features and semantic details:

| Icon | Metaphor | Target |
|---|---|---|
| Linux | Friendly penguin, distinct beak and feet | Recognizable at 24px |
| GitHub | Cat with subtle whisker-like arms | Ear/face balance |
| Python | Coiled snake, large head | Character consistency |
| JavaScript | Spiky, lively companion | No lettering dependence |
| Docker | Whale supporting containers | Cargo and expression |
| Rust | Soft crab with claws | Clear silhouette |
| PostgreSQL | Elephant with trunk | Avoid clutter |
| React | Smiling atom core and orbits | Recognizable at 32px |

## Remaining 22

The existing icons are still marked V2 and remain *unapproved*. Do not mass recolor or paste the same eyes onto every existing corporate motif. Continue incremental artwork improvements based on the eight design pilots and human review.

## Review checklist

- [ ] Inspect V3 mascots together with the original six-tile reference.
- [ ] Compare all 30 at **16 / 24 / 32 / 64px** with consistent optical sizes.
- [ ] Reject any mascot whose dominant silhouette is not recognizable without its stack name.
- [ ] Check eyes/secondary highlights never disappear or turn into visual noise.
- [ ] Validate all SVG XML and safe assets with `python scripts/validate.py`.
- [ ] Get explicit visual approval before merge/integration into AXR Stats.

**Note:** the automated SVG validator cannot prove design quality; this is intentionally still a draft PR.
