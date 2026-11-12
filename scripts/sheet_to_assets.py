#!/usr/bin/env python3
"""Split one 3x2 icon sheet into 6 RGBA PNGs and true path-based SVG candidates.

pip install -r scripts/requirements-artwork.txt
python scripts/sheet_to_assets.py sheet.png --out artwork/candidates/batch-01 \
    --names linux github python javascript typescript html

No AI generation happens in this script. Output is UNAPPROVED until visual QA.
"""
import argparse
import json
from pathlib import Path
import re
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageChops


def detect_tiles(img):
    h,w=img.shape[:2]
    edge=np.concatenate([img[:max(8,h//40)].reshape(-1,3),
                         img[-max(8,h//40):].reshape(-1,3)],axis=0)
    bg=np.median(edge,axis=0)
    diff=np.linalg.norm(img.astype(np.float32)-bg,axis=2)
    mask=(diff>60).astype(np.uint8)*255
    mask=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,np.ones((9,9),np.uint8))
    contours,_=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    boxes=[]
    for region in contours:
        x,y,bw,bh=cv2.boundingRect(region)
        if bw>.075*w and bh>.1*h and .78<=bw/bh<=1.25:
            boxes.append((x,y,bw,bh))
    if len(boxes)!=6:
        raise ValueError(f'Expected exactly 6 isolated colored tiles, found {len(boxes)}')
    boxes.sort(key=lambda b:b[1]+b[3]/2)
    boxes=sorted(boxes[:3],key=lambda b:b[0])+sorted(boxes[3:],key=lambda b:b[0])
    sizes=[(b[2]+b[3])/2 for b in boxes]
    if max(sizes)/min(sizes)>1.18:
        raise ValueError('Inconsistent tile dimensions — regenerate artwork')
    return boxes


def crop(img,box,size=512):
    x,y,w,h=box
    side=max(w,h)
    cx=x+w/2;cy=y+h/2
    tile=img.crop((round(cx-side/2),round(cy-side/2),
                   round(cx+side/2),round(cy+side/2)))
    tile=tile.resize((size,size),Image.Resampling.LANCZOS).convert('RGBA')
    m=Image.new('L',(size*3,size*3),0)
    ImageDraw.Draw(m).rounded_rectangle((0,0,size*3-1,size*3-1),
                                         radius=round(size*3*.22),fill=255)
    tile.putalpha(ImageChops.multiply(tile.getchannel('A'),
                                     m.resize((size,size),Image.Resampling.LANCZOS)))
    return tile


def contours(mask,small=8,epsilon=.65):
    cn,hier=cv2.findContours(mask.astype(np.uint8),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    paths=[]
    for contour in cn:
        if cv2.contourArea(contour)<small:continue
        points=cv2.approxPolyDP(contour,epsilon,True).reshape(-1,2).astype(float)
        if len(points)<3:continue
        mid=(points+np.roll(points,-1,axis=0))/2
        parts=[f'M {mid[-1,0]:.1f},{mid[-1,1]:.1f}']
        for i,(x,y) in enumerate(points):
            parts.append(f'Q {x:.1f},{y:.1f} {mid[i,0]:.1f},{mid[i,1]:.1f}')
        paths.append(' '.join(parts)+' Z')
    return paths


def trace(tile,slug,size=256):
    im=np.asarray(tile.resize((size,size),Image.Resampling.LANCZOS).convert('RGBA'))
    rgb=im[:,:,:3]; alpha=im[:,:,3]
    hsv=cv2.cvtColor(rgb,cv2.COLOR_RGB2HSV)
    white=(hsv[:,:,2]>=177)&(hsv[:,:,1]<112)&(alpha>200)
    dark=(hsv[:,:,2]<128)&(alpha>200)
    light_ratio=white.sum()/max(1,(alpha>200).sum())
    polarity='light' if light_ratio>=.045 else 'dark'
    raw=white if polarity=='light' else dark
    subject=cv2.morphologyEx(raw.astype(np.uint8),cv2.MORPH_CLOSE,
                             cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3)))
    fraction=subject.sum()/max(1,(alpha>200).sum())
    if not .045<=fraction<=.62:raise ValueError(f'{slug}: unsuitable image (subject coverage {fraction:.1%})')
    base=contours(subject*255,24)
    inside=np.zeros_like(subject)
    cn,_=cv2.findContours(subject,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    good=[a for a in cn if cv2.contourArea(a)>24]
    cv2.drawContours(inside,good,-1,1,cv2.FILLED)
    inside=cv2.erode(inside,np.ones((3,3),np.uint8))
    details=((hsv[:,:,2]<120) if polarity=='light' else
             ((hsv[:,:,2]>190)&(hsv[:,:,1]<105)))&(inside>0)&(alpha>200)
    fine=contours(details.astype(np.uint8)*255,8,.5)
    def bg(x1,x2,y1,y2):
        block=rgb[round(size*y1):round(size*y2),round(size*x1):round(size*x2)]
        return '#'+''.join(f'{int(x):02x}' for x in np.median(block.reshape(-1,3),axis=0))
    top=bg(.06,.14,.2,.35);bottom=bg(.06,.14,.67,.8)
    lines=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}" width="512" height="512" role="img" aria-labelledby="title">',
           f'<title id="title">AXR {slug} concept, traced</title>',
           f'<defs><linearGradient id="tile" x1="0" y1="0" x2="0" y2="1"><stop stop-color="{top}"/><stop offset="1" stop-color="{bottom}"/></linearGradient></defs>',
           f'<rect x="1" y="1" width="{size-2}" height="{size-2}" rx="{round(size*.22)}" fill="url(#tile)"/>']
    for d in base:lines.append(f'<path fill="{("#fff" if polarity=="light" else "#303039")}" d="{d}"/>')
    for d in fine:lines.append(f'<path fill="{("#19212b" if polarity=="light" else "#fff")}" d="{d}"/>')
    lines.append('</svg>')
    return '\n'.join(lines)+'\n',len(base)+len(fine)


def preview(items,out):
    sizes=[16,24,32,64,128]
    image=Image.new('RGB',(1024,1155),'#10151c')
    draw=ImageDraw.Draw(image)
    draw.text((22,20),'AXR ICONS — SIX-ICON QUALITY REVIEW',fill='white')
    for row,(slug,path) in enumerate(items):
        y=65+180*row
        draw.text((20,y+45),slug,fill='white')
        src=Image.open(path).convert('RGBA')
        for column,size in enumerate(sizes):
            x=200+160*column
            icon=src.resize((size,size),Image.Resampling.LANCZOS)
            image.paste(icon,(x,y+10+(128-size)//2),icon)
            draw.text((x,y+153),f'{size}px',fill='#a8b9c9')
        if row<5:draw.line((20,y+177,1004,y+177),fill='#29323b',width=1)
    image.save(out)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('sheet',type=Path)
    parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--names',nargs=6,required=True)
    args=parser.parse_args()
    if len(set(args.names))!=6 or any(not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',x) for x in args.names):
        parser.error('Supply 6 unique safe slugs')
    image=Image.open(args.sheet).convert('RGB')
    boxes=detect_tiles(np.asarray(image))
    args.out.mkdir(parents=True,exist_ok=True)
    entries=[];items=[]
    for slug,box in zip(args.names,boxes):
        png=args.out/f'{slug}.png';svg=args.out/f'{slug}.svg'
        icon=crop(image,box)
        vector,n=trace(icon,slug)
        icon.save(png,optimize=True)
        svg.write_text(vector,encoding='utf-8')
        entries.append({'slug':slug,'png':png.name,'svg':svg.name,'paths':n,'approved':False})
        items.append((slug,png))
    preview(items,args.out/'review-sizes.png')
    (args.out/'manifest.json').write_text(json.dumps({'batch':6,'assets':entries},indent=2)+'\n')
    print(f'Created {len(items)} PNGs and SVGs. Check {args.out / "review-sizes.png"}')


if __name__=='__main__':main()
