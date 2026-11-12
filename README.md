# AXR Icons

Technology-inspired, original mascot SVGs for AXROBERT / AXR Stats.

**V2 artwork candidate.** 30 individual technology-inspired vectors have replaced the 10 repeated placeholder silhouettes. The art remains in review and is not yet approved for production.

## Preview

Run `python -m http.server 8000` in the repository root, then open <http://localhost:8000>. Search the responsive gallery, filter stacks and click a tile to download SVG.

## Icons

<img src="icons/linux.svg" width="34" height="34" alt="Linux"/> **Linux** · <img src="icons/github.svg" width="34" height="34" alt="GitHub"/> **GitHub** · <img src="icons/python.svg" width="34" height="34" alt="Python"/> **Python** · <img src="icons/javascript.svg" width="34" height="34" alt="JavaScript"/> **JavaScript** · <img src="icons/typescript.svg" width="34" height="34" alt="TypeScript"/> **TypeScript** · <img src="icons/html.svg" width="34" height="34" alt="HTML"/> **HTML** · <img src="icons/css.svg" width="34" height="34" alt="CSS"/> **CSS** · <img src="icons/git.svg" width="34" height="34" alt="Git"/> **Git** · <img src="icons/docker.svg" width="34" height="34" alt="Docker"/> **Docker** · <img src="icons/kubernetes.svg" width="34" height="34" alt="Kubernetes"/> **Kubernetes** · <img src="icons/rust.svg" width="34" height="34" alt="Rust"/> **Rust** · <img src="icons/react.svg" width="34" height="34" alt="React"/> **React** · <img src="icons/nextjs.svg" width="34" height="34" alt="Next.js"/> **Next.js** · <img src="icons/nodejs.svg" width="34" height="34" alt="Node.js"/> **Node.js** · <img src="icons/postgresql.svg" width="34" height="34" alt="PostgreSQL"/> **PostgreSQL** · <img src="icons/mysql.svg" width="34" height="34" alt="MySQL"/> **MySQL** · <img src="icons/mongodb.svg" width="34" height="34" alt="MongoDB"/> **MongoDB** · <img src="icons/redis.svg" width="34" height="34" alt="Redis"/> **Redis** · <img src="icons/go.svg" width="34" height="34" alt="Go"/> **Go** · <img src="icons/java.svg" width="34" height="34" alt="Java"/> **Java** · <img src="icons/c.svg" width="34" height="34" alt="C"/> **C** · <img src="icons/cpp.svg" width="34" height="34" alt="C++"/> **C++** · <img src="icons/bash.svg" width="34" height="34" alt="Bash"/> **Bash** · <img src="icons/archlinux.svg" width="34" height="34" alt="Arch Linux"/> **Arch Linux** · <img src="icons/ubuntu.svg" width="34" height="34" alt="Ubuntu"/> **Ubuntu** · <img src="icons/debian.svg" width="34" height="34" alt="Debian"/> **Debian** · <img src="icons/windows.svg" width="34" height="34" alt="Windows"/> **Windows** · <img src="icons/macos.svg" width="34" height="34" alt="macOS"/> **macOS** · <img src="icons/figma.svg" width="34" height="34" alt="Figma"/> **Figma** · <img src="icons/tailwindcss.svg" width="34" height="34" alt="Tailwind CSS"/> **Tailwind CSS**

## Integration

- `registry.json`: stable slug and asset mappings with categories.
- `icons/*.svg`: scalable standalone art using an identical tile canvas.
- `docs/DESIGN-SYSTEM.md`: core design rules.
- `docs/AI-ICON-CONTRACT.md`: AI-assisted authoring recipe.
- `scripts/validate.py`: local validator (`python scripts/validate.py`).
- `.github/workflows/svg-validate.yml`: GitHub validation.

Pin a released version, map stack slugs and show a fallback when an icon is missing. Do not use a moving PR branch in production. Human visual approval required.

## Licensing

No license chosen: all rights reserved pending the author's decision. Technology names may be trademarks.
