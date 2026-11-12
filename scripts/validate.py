#!/usr/bin/env python3
"""Validate original SVG assets and registry without third-party dependencies."""
from collections import Counter
from pathlib import Path
import json
import re
import sys
import xml.etree.ElementTree as ET

base = Path(__file__).resolve().parents[1]
registry = json.loads((base/"registry.json").read_text())
errors = []
slugs = [r["slug"] for r in registry]
if len(slugs) < 30: errors.append("Expected 30+ icons")
for slug, count in Counter(slugs).items():
    if count != 1: errors.append(f"Duplicate {slug}")
illustrations = []
svg_ns = "{http://www.w3.org/2000/svg}"
for item in registry:
    slug, file = item["slug"], item["file"]
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
        errors.append(f"Invalid slug: {slug}")
    if file != f"icons/{slug}.svg":
        errors.append(f"File path mismatch: {file}")
        continue
    path = base / file
    if not path.is_file():
        errors.append(f"Missing asset: {file}")
        continue
    raw = path.read_text(encoding="utf-8")
    if re.search(r"<script\b|<foreignObject\b|<image\b|\bon[a-z]+\s*=|\bhref\s*=|javascript:|data:|@import|<style\b", raw, re.I):
        errors.append(f"Unsafe SVG: {file}")
    try: root = ET.fromstring(raw)
    except ET.ParseError as exc:
        errors.append(f"Invalid XML {file}: {exc}")
        continue
    if root.tag != svg_ns+"svg" or root.get("viewBox") != "0 0 96 96":
        errors.append(f"Bad SVG canvas: {file}")
    if root.find(svg_ns+"title") is None: errors.append(f"Missing title: {file}")
    rects = root.findall(svg_ns+"rect")
    if not any(x.get("width") == "94" and x.get("rx") == "23" for x in rects):
        errors.append(f"Wrong tile: {file}")
    match = re.search(r'<g stroke-linecap="round" stroke-linejoin="round">(.*?)</g>',raw,re.S)
    if not match: errors.append(f"Missing mascot: {file}")
    else: illustrations.append(match.group(1))
if len(set(illustrations)) != len(illustrations):
    errors.append("Duplicate mascot illustration")
for f in (base/"icons").glob("*.svg"):
    if f.stem not in slugs: errors.append(f"Unregistered icon: {f.name}")
if errors:
    print("\n".join("ERROR: "+i for i in errors))
    sys.exit(1)
print(f"Validated {len(slugs)} different stack illustrations (safe XML and registry).")
