# AXR Icons

**Small icons. Big personality.** Original illustrated stack mascots for AXROBERT / AXR Stats.

> [!IMPORTANT]
> **Artwork is under active design review.** This branch contains concepts, not an approved icon pack. Shape clarity, consistent character proportions and recognizability matter more than shipping lots of mediocre icons.

## New: image-first artwork pipeline (batches of six)

The current 30-icon preview above still shows the **old unapproved SVG concepts**, not newly generated icons. We're replacing them **six at a time**, using image generation and human review first, then real vector tracing and a small-size QA sheet. New icons must not silently overwrite the old artwork until approved.

[See the five batches and review checklist](docs/BATCH-WORKFLOW.md). For conversion: `python -m pip install -r scripts/requirements-artwork.txt` then `python scripts/sheet_to_assets.py sheet.png --out artwork/candidates/batch-01 --names linux github python javascript typescript html`. Use `python scripts/test_artwork_pipeline.py` for the synthetic six-tile smoke test.

## All 30 icons — visual gallery

Click any icon to view/download its full-size, editable SVG. The grid below shows **every model side by side** without opening each file individually.

| | | | | | |
|:---:|:---:|:---:|:---:|:---:|:---:|
| <a href="icons/linux.svg"><img src="icons/linux.svg" width="72" height="72" alt="Linux icon"></a><br><sub><b>Linux</b></sub> | <a href="icons/github.svg"><img src="icons/github.svg" width="72" height="72" alt="GitHub icon"></a><br><sub><b>GitHub</b></sub> | <a href="icons/python.svg"><img src="icons/python.svg" width="72" height="72" alt="Python icon"></a><br><sub><b>Python</b></sub> | <a href="icons/javascript.svg"><img src="icons/javascript.svg" width="72" height="72" alt="JavaScript icon"></a><br><sub><b>JavaScript</b></sub> | <a href="icons/typescript.svg"><img src="icons/typescript.svg" width="72" height="72" alt="TypeScript icon"></a><br><sub><b>TypeScript</b></sub> | <a href="icons/html.svg"><img src="icons/html.svg" width="72" height="72" alt="HTML icon"></a><br><sub><b>HTML</b></sub> |
| <a href="icons/css.svg"><img src="icons/css.svg" width="72" height="72" alt="CSS icon"></a><br><sub><b>CSS</b></sub> | <a href="icons/git.svg"><img src="icons/git.svg" width="72" height="72" alt="Git icon"></a><br><sub><b>Git</b></sub> | <a href="icons/docker.svg"><img src="icons/docker.svg" width="72" height="72" alt="Docker icon"></a><br><sub><b>Docker</b></sub> | <a href="icons/kubernetes.svg"><img src="icons/kubernetes.svg" width="72" height="72" alt="Kubernetes icon"></a><br><sub><b>Kubernetes</b></sub> | <a href="icons/rust.svg"><img src="icons/rust.svg" width="72" height="72" alt="Rust icon"></a><br><sub><b>Rust</b></sub> | <a href="icons/react.svg"><img src="icons/react.svg" width="72" height="72" alt="React icon"></a><br><sub><b>React</b></sub> |
| <a href="icons/nextjs.svg"><img src="icons/nextjs.svg" width="72" height="72" alt="Next.js icon"></a><br><sub><b>Next.js</b></sub> | <a href="icons/nodejs.svg"><img src="icons/nodejs.svg" width="72" height="72" alt="Node.js icon"></a><br><sub><b>Node.js</b></sub> | <a href="icons/postgresql.svg"><img src="icons/postgresql.svg" width="72" height="72" alt="PostgreSQL icon"></a><br><sub><b>PostgreSQL</b></sub> | <a href="icons/mysql.svg"><img src="icons/mysql.svg" width="72" height="72" alt="MySQL icon"></a><br><sub><b>MySQL</b></sub> | <a href="icons/mongodb.svg"><img src="icons/mongodb.svg" width="72" height="72" alt="MongoDB icon"></a><br><sub><b>MongoDB</b></sub> | <a href="icons/redis.svg"><img src="icons/redis.svg" width="72" height="72" alt="Redis icon"></a><br><sub><b>Redis</b></sub> |
| <a href="icons/go.svg"><img src="icons/go.svg" width="72" height="72" alt="Go icon"></a><br><sub><b>Go</b></sub> | <a href="icons/java.svg"><img src="icons/java.svg" width="72" height="72" alt="Java icon"></a><br><sub><b>Java</b></sub> | <a href="icons/c.svg"><img src="icons/c.svg" width="72" height="72" alt="C icon"></a><br><sub><b>C</b></sub> | <a href="icons/cpp.svg"><img src="icons/cpp.svg" width="72" height="72" alt="C++ icon"></a><br><sub><b>C++</b></sub> | <a href="icons/bash.svg"><img src="icons/bash.svg" width="72" height="72" alt="Bash icon"></a><br><sub><b>Bash</b></sub> | <a href="icons/archlinux.svg"><img src="icons/archlinux.svg" width="72" height="72" alt="Arch Linux icon"></a><br><sub><b>Arch Linux</b></sub> |
| <a href="icons/ubuntu.svg"><img src="icons/ubuntu.svg" width="72" height="72" alt="Ubuntu icon"></a><br><sub><b>Ubuntu</b></sub> | <a href="icons/debian.svg"><img src="icons/debian.svg" width="72" height="72" alt="Debian icon"></a><br><sub><b>Debian</b></sub> | <a href="icons/windows.svg"><img src="icons/windows.svg" width="72" height="72" alt="Windows icon"></a><br><sub><b>Windows</b></sub> | <a href="icons/macos.svg"><img src="icons/macos.svg" width="72" height="72" alt="macOS icon"></a><br><sub><b>macOS</b></sub> | <a href="icons/figma.svg"><img src="icons/figma.svg" width="72" height="72" alt="Figma icon"></a><br><sub><b>Figma</b></sub> | <a href="icons/tailwindcss.svg"><img src="icons/tailwindcss.svg" width="72" height="72" alt="Tailwind CSS icon"></a><br><sub><b>Tailwind CSS</b></sub> |

<sub>Rendered from the actual SVG files. Every cell uses a 72 × 72 px preview; the vector source scales to 16, 24, 32, 64 and larger pixel sizes.</sub>

## Explore the interactive gallery

Start a local web server in the repository directory:

```bash
python -m http.server 8000
```

Open **http://localhost:8000** — search and category filtering work without external dependencies. For direct repository browsing, use the **branch selector** to choose `feat/mascot-icon-system-v1` until the PR is approved and merged.

## How new icons are created

1. Read [the design system](docs/DESIGN-SYSTEM.md) and [the AI creation contract](docs/AI-ICON-CONTRACT.md).
2. Choose a *distinct technology metaphor*, not a recolored copy of another mascot or a third-party logo.
3. Draw an original standalone SVG with `viewBox="0 0 96 96"` and a uniform rounded tile; inspect at **16 / 24 / 32 / 64 px**.
4. Register it in [registry.json](registry.json) using the stable machine-readable technology slug.
5. Run `python scripts/validate.py` and inspect the full gallery at actual app size before requesting visual review.

## Project layout

| Path | Purpose |
|:--|:--|
| [icons/](icons/) | All 30 source SVG files |
| [registry.json](registry.json) | Stack identifiers, display names and categories |
| [docs/DESIGN-SYSTEM.md](docs/DESIGN-SYSTEM.md) | Mandatory geometry, color and illustration rules |
| [docs/AI-ICON-CONTRACT.md](docs/AI-ICON-CONTRACT.md) | Generation workflow and acceptance criteria |
| [index.html](index.html) | Searchable preview gallery |
| [scripts/validate.py](scripts/validate.py) | XML, safety, duplicates and registry checks |

## Integrating with AXR Stats

No production integration yet. Once artwork is visually approved, tag a release and vendor or pin the SVG assets; map stack names to their slugs and provide a fallback for unknown technologies. Do not use a mutable draft branch as a production dependency.

## License and ownership

No public-use license chosen yet. All rights reserved until a license is selected. Technologies and brand names remain the property of their respective owners; this collection is not endorsed by them.
