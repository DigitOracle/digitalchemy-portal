#!/usr/bin/env python3
"""Extract ADGM stamp from combined signature+stamp PDF.
Output: gold-tinted, transparent-background PNG suitable for portal hero overlay.
"""
import os, sys
import pypdfium2 as pdfium
from PIL import Image

PDF = r"C:\Users\kwils\OneDrive\Desktop\DigitAlchemy\Master Planning Framework\Maser Planning Framework\digitalalchemy_signature_stamp_combined.pdf"
OUT_DIR = r"C:\Users\kwils\OneDrive\Desktop\DigitAlchemy\digitalchemy-portal\public\images"
os.makedirs(OUT_DIR, exist_ok=True)
OUT_PATH = os.path.join(OUT_DIR, "adgm-stamp.png")

# Render PDF page 1 at high resolution
doc = pdfium.PdfDocument(PDF)
page = doc[0]
pil_img = page.render(scale=4.0).to_pil()
W, H = pil_img.size
print(f"Native render: {W} × {H}")

# Crop to just the right side (the round stamp) — left portion has signature trail
# Tighter crop: 58% to right edge, full height
crop_left = int(W * 0.58)
crop_right = W
crop_top = 0
crop_bottom = H
stamp = pil_img.crop((crop_left, crop_top, crop_right, crop_bottom))
print(f"Stamp crop: {stamp.size}")

# Now process: white → transparent, dark blue ink → gold #C9A227
GOLD_R, GOLD_G, GOLD_B = 0xC9, 0xA2, 0x27
img = stamp.convert("RGBA")
W, H = img.size
data = img.load()

for y in range(H):
    for x in range(W):
        r, g, b, a = data[x, y]
        # White / near-white → fully transparent
        if r > 235 and g > 235 and b > 235:
            data[x, y] = (0, 0, 0, 0)
        else:
            # Dark / colored pixels (the navy stamp ink) → gold
            # Use brightness to determine alpha (darker = more opaque)
            brightness = (r + g + b) / 3
            alpha = max(60, min(255, int(255 - (brightness / 240) * 200)))
            data[x, y] = (GOLD_R, GOLD_G, GOLD_B, alpha)

# Make it square (crop to center square since the stamp is round)
W, H = img.size
side = min(W, H)
left = (W - side) // 2
top = (H - side) // 2
img = img.crop((left, top, left + side, top + side))
print(f"Final square: {img.size}")

# Downscale to 512×512 for portal use (CSS displays at 120×120)
img = img.resize((512, 512), Image.LANCZOS)
img.save(OUT_PATH, "PNG", optimize=True)
print(f"Saved: {OUT_PATH}")
print(f"File size: {os.path.getsize(OUT_PATH) / 1024:.1f} KB")
