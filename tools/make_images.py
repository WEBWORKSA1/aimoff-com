#!/usr/bin/env python3
"""Generates PNG icons + Open Graph image (run by the build workflow)."""
import os
from PIL import Image, ImageDraw, ImageFont
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
IMG = os.path.join(ROOT, 'assets', 'img')

def icon(n):
    im = Image.new('RGB', (n, n), '#070b14'); d = ImageDraw.Draw(im); c = n / 2; s = n / 32; w = int(2.4 * s)
    d.ellipse([c - 11 * s, c - 11 * s, c + 11 * s, c + 11 * s], outline='#e8eefc', width=w)
    d.ellipse([c - 5 * s, c - 5 * s, c + 5 * s, c + 5 * s], outline='#22e3c4', width=w)
    d.ellipse([18.1 * s, 9.1 * s, 22.9 * s, 13.9 * s], fill='#ff4d6d')
    for a, b in [((16, 3), (16, 8)), ((16, 24), (16, 29)), ((3, 16), (8, 16)), ((24, 16), (29, 16))]:
        d.line([a[0] * s, a[1] * s, b[0] * s, b[1] * s], fill='#e8eefc', width=w)
    im.save(os.path.join(IMG, f'icon-{n}.png'))

def font(bold, size):
    for p in ['/usr/share/fonts/truetype/dejavu/DejaVuSans%s.ttf' % ('-Bold' if bold else ''),
              '/usr/share/fonts/truetype/liberation/LiberationSans-%s.ttf' % ('Bold' if bold else 'Regular')]:
        if os.path.exists(p): return ImageFont.truetype(p, size)
    return ImageFont.load_default()

def og():
    im = Image.new('RGB', (1200, 630), '#070b14'); d = ImageDraw.Draw(im)
    for x in range(0, 1200, 60): d.line([x, 0, x, 630], fill='#111a2c')
    for y in range(0, 630, 60): d.line([0, y, 1200, y], fill='#111a2c')
    f1, f2 = font(True, 110), font(False, 40)
    d.text((90, 190), 'Aim', font=f1, fill='#e8eefc'); w = d.textlength('Aim', font=f1); d.text((90 + w, 190), 'Off', font=f1, fill='#22e3c4')
    d.text((92, 340), 'Free aim trainer - reaction & CPS tests', font=f2, fill='#93a1bf')
    d.text((92, 395), 'sensitivity converter - guides - contests', font=f2, fill='#93a1bf')
    cx, cy = 930, 315
    for r, c in [(200, '#1f2b45'), (130, '#7c5cff'), (60, '#22e3c4')]: d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=c, width=8)
    d.ellipse([cx + 40, cy - 110, cx + 100, cy - 50], fill='#ff4d6d')
    im.save(os.path.join(IMG, 'og.png'))

if __name__ == '__main__':
    os.makedirs(IMG, exist_ok=True); icon(192); icon(512); og(); print('images ok')
