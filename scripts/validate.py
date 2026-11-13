#!/usr/bin/env python3
"""Validate the 126 icon assets, registry, checksums and README gallery."""
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET

try:
    from PIL import Image
except ImportError:
    raise SystemExit('Pillow is required: python -m pip install Pillow>=10')

ROOT = Path(__file__).resolve().parents[1]
NAMESPACE = '{http://www.w3.org/2000/svg}'
SIZE = (16, 32, 64, 256)
REQUIRED = {'languages','frontend','backend','databases','cloud','devops',
            'observability','desktop','ai','tools','os','games','design'}


def normalize(value):
    value = str(value).lower().strip()
    value = value.replace('c++', 'cpp').replace('c#', 'csharp').replace('.net','dotnet')
    return re.sub(r'^-+|-+$','',re.sub('[^a-z0-9]+','-',value))


def validate(root=ROOT):
    problems = []
    registry = json.loads((root/'registry.json').read_text(encoding='utf-8'))
    if len(registry) != 126:
        problems.append(f'Expected 126 registry entries; got {len(registry)}')
    names = [x['slug'] for x in registry]
    if len(set(names)) != len(names): problems.append('Duplicate registry slugs')
    expected_assets = set()
    aliases = {}
    for idx, icon in enumerate(registry, 1):
        slug = icon['slug']
        if idx != icon['id']: problems.append(f'Index mismatch: {slug}')
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', slug): problems.append(f'Invalid slug: {slug}')
        if icon['category'] not in REQUIRED: problems.append(f'Unknown category: {slug}')
        if not 1 <= icon['lot'] <= 16: problems.append(f'Invalid lot: {slug}')
        for candidate in [slug, icon['name'], *icon['aliases']]:
            key = normalize(candidate)
            if key in aliases and aliases[key] != slug:
                problems.append(f'Alias collision {candidate} with {aliases[key]}')
            aliases[key] = slug
        for size in SIZE:
            path = icon['assets']['png'][str(size)]
            expected_assets.add(path)
            file = root/path
            if not file.is_file():
                problems.append('Missing PNG: ' + path)
                continue
            with Image.open(file) as img:
                img.load()
                if img.size != (size,size) or img.mode != 'RGBA':
                    problems.append('Wrong PNG size/mode: ' + path)
                else:
                    alpha = img.getchannel('A')
                    if any(alpha.getpixel((x,y)) > 24 for x,y in
                           [(0,0),(0,size-1),(size-1,0),(size-1,size-1)]):
                        problems.append('Nontransparent PNG corner: ' + path)
        for variant in ('vector','fidelity'):
            path = icon['assets']['svg'][variant]
            expected_assets.add(path)
            file = root/path
            if not file.is_file():
                problems.append('Missing SVG: ' + path)
                continue
            text = file.read_text(encoding='utf-8')
            if re.search(r'<script\b|<foreignObject\b|\bon\w+\s*=|javascript:|https?://(?!www\.w3\.org/)', text, re.I):
                problems.append('Unsafe SVG contents: ' + path)
            try: svg = ET.fromstring(text)
            except ET.ParseError as exc:
                problems.append(f'Invalid XML {path}: {exc}')
                continue
            if svg.tag != NAMESPACE+'svg' or svg.get('viewBox') != '0 0 256 256':
                problems.append('Bad SVG root/viewBox: ' + path)
            tags = Counter(t.tag.rsplit('}',1)[-1] for t in svg.iter())
            if svg.find(NAMESPACE+'title') is None:
                problems.append('No SVG title: ' + path)
            if variant == 'vector':
                if tags['path'] == 0 or tags['image'] > 0 or 'data:image' in text:
                    problems.append('Non-vector SVG: ' + path)
                if re.search(r'\bhref\s*=',text,re.I): problems.append('SVG has external href: '+path)
            elif tags['image'] != 1 or 'data:image/png;base64,' not in text:
                problems.append('Fidelity SVG must embed exactly one PNG: '+path)
    checksums=(root/'assets/checksums.sha256').read_text(encoding='utf-8').splitlines()
    check_paths = {}
    for line in checksums:
        try: expected, rel = line.split('  ', 1)
        except ValueError:
            problems.append('Bad checksums entry: '+line[:80]);continue
        if rel in check_paths:
            problems.append('Duplicate checksum: '+rel)
        check_paths[rel]=expected
        file=root/rel
        if not file.is_file():
            problems.append('Missing checksummed asset: '+rel)
        elif hashlib.sha256(file.read_bytes()).hexdigest()!=expected:
            problems.append('Asset content changed: '+rel)
    expected_assets.add('assets/preview/collection-126.png')
    if expected_assets != set(check_paths):
        problems.append('Checksums manifest does not match registry assets')
    all_binary = {p.relative_to(root).as_posix() for p in (root/'assets').rglob('*') if p.suffix in {'.png','.svg'}}
    if all_binary != expected_assets:
        problems.append('Extra/missing binary assets in assets/')
    readme=(root/'README.md').read_text(encoding='utf-8')
    preview_paths=re.findall(r'<img src="(assets/png/64/[^\"]+\.png)"',readme)
    if len(preview_paths)!=126 or set(preview_paths)!={i['assets']['png']['64'] for i in registry}:
        problems.append('README does not preview exactly 126 live 64px icons')
    for static in ['index.html','style.css','src/gallery.mjs','src/resolve.mjs','NOTICE.md']:
        if not (root/static).is_file(): problems.append('Missing static project file: '+static)
    if any(p.name == 'CONTEXT.md' for p in root.rglob('*')):
        problems.append('Private continuity file must not be in repository')
    return problems


if __name__ == '__main__':
    problems = validate()
    if problems:
        for problem in problems: print('FAIL:', problem)
        sys.exit(1)
    print('PASS: 126 slugs, 504 PNGs, 126 vector SVGs, 126 fidelity SVGs, registry, checksums, gallery.')
