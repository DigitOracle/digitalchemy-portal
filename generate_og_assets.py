"""
Generate OG share card (1200x630) + favicon (32) + apple-touch-icon (180)
Gold-on-navy. Matches portal palette. No external assets required.
"""
from PIL import Image, ImageDraw, ImageFont
import os

OUT_DIR = r"C:\Users\kwils\OneDrive\Desktop\DigitAlchemy\digitalchemy-portal\public\images"
os.makedirs(OUT_DIR, exist_ok=True)

NAVY_DEEP = (11, 5, 36)
NAVY      = (22, 28, 58)
GOLD      = (201, 162, 39)
GOLD_BR   = (229, 189, 63)
CREAM     = (250, 245, 237)
MUTED     = (180, 175, 160)

def _font(size, bold=False):
    # Try a few Windows fonts in order; degrade to default.
    candidates_bold = [
        r"C:\Windows\Fonts\seguisb.ttf",     # Segoe UI Semibold
        r"C:\Windows\Fonts\segoeuib.ttf",    # Segoe UI Bold
        r"C:\Windows\Fonts\arialbd.ttf",
    ]
    candidates_reg = [
        r"C:\Windows\Fonts\segoeui.ttf",
        r"C:\Windows\Fonts\arial.ttf",
    ]
    for p in (candidates_bold if bold else candidates_reg):
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
    return ImageFont.load_default()

# ── OG card 1200x630 ─────────────────────────────────────────
W, H = 1200, 630
img = Image.new("RGB", (W, H), NAVY_DEEP)
draw = ImageDraw.Draw(img)

# Subtle vertical band gradient (navy_deep -> navy)
for y in range(H):
    t = y / H
    r = int(NAVY_DEEP[0] + (NAVY[0] - NAVY_DEEP[0]) * t)
    g = int(NAVY_DEEP[1] + (NAVY[1] - NAVY_DEEP[1]) * t)
    b = int(NAVY_DEEP[2] + (NAVY[2] - NAVY_DEEP[2]) * t)
    draw.line([(0, y), (W, y)], fill=(r, g, b))

# Thin gold rule top + bottom
draw.rectangle([(0, 0), (W, 4)], fill=GOLD)
draw.rectangle([(0, H - 4), (W, H)], fill=GOLD)

# Eyebrow
eyebrow = "DIGITALCHEMY® TECH LIMITED  ·  ADGM 35004  ·  ABU DHABI"
f_eye = _font(20)
draw.text((72, 80), eyebrow, font=f_eye, fill=GOLD)

# Headline
f_h1 = _font(78, bold=True)
draw.text((72, 134), "Months Become Seconds.", font=f_h1, fill=CREAM)
draw.text((72, 230), "Complexity Becomes Clarity.", font=f_h1, fill=CREAM)

# Subhead
f_sub = _font(28)
sub_lines = [
    "The operating system for regulatory intelligence",
    "in the built environment.  Generic AI guesses.  DigitAlchemy® cites.",
]
y = 348
for line in sub_lines:
    draw.text((72, y), line, font=f_sub, fill=(220, 215, 200))
    y += 40

# Trust row chrome (bottom strip)
strip_y = 506
draw.rectangle([(0, strip_y), (W, strip_y + 1)], fill=(60, 50, 100))
chips = [
    "ADGM 35004",
    "UAE PATENT P2026-01477",
    "bSI ROADMAP Q3-2027",
    "IFC 4.3 ADD2 NATIVE",
]
f_chip = _font(18, bold=True)
x = 72
for i, label in enumerate(chips):
    bbox = draw.textbbox((0, 0), label, font=f_chip)
    w = bbox[2] - bbox[0]
    # chip background
    pad_x, pad_y = 16, 10
    draw.rectangle(
        [(x - pad_x, strip_y + 30), (x + w + pad_x, strip_y + 30 + 36 + pad_y)],
        outline=GOLD,
        width=1,
    )
    draw.text((x, strip_y + 42), label, font=f_chip, fill=GOLD_BR)
    x += w + pad_x * 2 + 14

# Wordmark bottom right
f_brand = _font(26, bold=True)
brand_text = "digitalchemy-portal.vercel.app"
bbox = draw.textbbox((0, 0), brand_text, font=f_brand)
bw = bbox[2] - bbox[0]
draw.text((W - bw - 72, 80), brand_text, font=f_brand, fill=CREAM)

og_path = os.path.join(OUT_DIR, "og-card-1200x630.png")
img.save(og_path, "PNG", optimize=True)
print(f"WROTE  {og_path}  ({os.path.getsize(og_path)//1024} KB)")

# ── Favicon 32 + apple-touch-icon 180 ────────────────────────
def make_mark(size):
    m = Image.new("RGB", (size, size), NAVY_DEEP)
    d = ImageDraw.Draw(m)
    # gold ring
    pad = max(2, size // 12)
    d.ellipse([(pad, pad), (size - pad, size - pad)], outline=GOLD, width=max(2, size // 18))
    # gold "DA" mark
    f = _font(int(size * 0.45), bold=True)
    txt = "DA"
    bbox = d.textbbox((0, 0), txt, font=f)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    d.text(((size - tw) / 2, (size - th) / 2 - size * 0.06), txt, font=f, fill=GOLD)
    return m

fav = make_mark(32)
fav_path = os.path.join(OUT_DIR, "favicon-32.png")
fav.save(fav_path, "PNG", optimize=True)
print(f"WROTE  {fav_path}  ({os.path.getsize(fav_path)//1024} KB)")

apple = make_mark(180)
apple_path = os.path.join(OUT_DIR, "apple-touch-icon-180.png")
apple.save(apple_path, "PNG", optimize=True)
print(f"WROTE  {apple_path}  ({os.path.getsize(apple_path)//1024} KB)")

print("\nDONE.")
