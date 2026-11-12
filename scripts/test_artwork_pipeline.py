#!/usr/bin/env python3
"""Technical smoke test for the 6-icon image-first tracing pipeline."""
import json
import subprocess
import sys
import tempfile
from pathlib import Path
import xml.etree.ElementTree as ET
from PIL import Image,ImageDraw

def main():
    root=Path(__file__).resolve().parent
    with tempfile.TemporaryDirectory() as d:
        work=Path(d);sheet=Image.new('RGB',(960,700),'#090b0e');draw=ImageDraw.Draw(sheet)
        colors=['#ff922e','#30354e','#1c8bdd','#ffba28','#2e77dc','#fc7347']
        names=['linux','github','python','javascript','typescript','html']
        for i,color in enumerate(colors):
            x=80+(i%3)*290;y=52+(i//3)*330
            draw.rounded_rectangle((x,y,x+190,y+190),radius=43,fill=color)
            draw.ellipse((x+40,y+45,x+150,y+145),fill='white')
            draw.ellipse((x+75,y+84,x+84,y+107),fill='#172331')
            draw.ellipse((x+110,y+84,x+119,y+107),fill='#172331')
        file=work/'source.png';file.parent.mkdir(exist_ok=True);sheet.save(file)
        out=work/'out'
        res=subprocess.run([sys.executable,str(root/'sheet_to_assets.py'),str(file),'--out',str(out),'--names',*names],capture_output=True,text=True)
        if res.returncode:raise RuntimeError(res.stdout+'\n'+res.stderr)
        data=json.loads((out/'manifest.json').read_text())
        assert len(data['assets'])==6
        for a in data['assets']:
            png=out/a['png'];svg=out/a['svg']
            assert png.is_file() and svg.is_file()
            raw=svg.read_text()
            assert '<image' not in raw and 'data:' not in raw
            assert len(ET.fromstring(raw).findall('{http://www.w3.org/2000/svg}path'))>0
        assert (out/'review-sizes.png').is_file()
        print('PASS: six PNGs and six real editable SVGs, manifest, QA contact sheet')

if __name__=='__main__':main()
