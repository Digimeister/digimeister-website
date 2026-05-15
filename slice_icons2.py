from PIL import Image
import os, shutil

# Both sprite sheets use a consistent grid:
# - Cell stride: 24px
# - First icon offset: 7px from top-left
# - Icon content area: 18x18 (16x16 art + 1px breathing room each side)
img = Image.open("1-bit 16px icons part-1 outlines.png").convert("RGBA")
w, h = img.size
print(f"Image size: {w}x{h}")

OFFSET = 7
STRIDE = 24
ICON   = 18

cols = (w - OFFSET) // STRIDE + 1   # last cell can extend past stride*n
rows = (h - OFFSET) // STRIDE + 1
# Trim if last cell would extend past image bounds
while OFFSET + (cols - 1) * STRIDE + ICON > w + 1:
    cols -= 1
while OFFSET + (rows - 1) * STRIDE + ICON > h + 1:
    rows -= 1
print(f"Grid: {cols} cols x {rows} rows = {cols*rows} icons")

out = "icons"
if os.path.exists(out):
    shutil.rmtree(out)
os.makedirs(out)

count = 0
for r in range(rows):
    for c in range(cols):
        x = OFFSET + c * STRIDE
        y = OFFSET + r * STRIDE
        # Clamp to image bounds
        x2 = min(x + ICON, w)
        y2 = min(y + ICON, h)
        crop = img.crop((x, y, x2, y2)).convert("RGBA")
        # Threshold by luminance — outline sheet has anti-aliased edges and off-white bg
        pixels = crop.load()
        for py in range(crop.height):
            for px in range(crop.width):
                rv, gv, bv, av = pixels[px, py]
                lum = 0.299 * rv + 0.587 * gv + 0.114 * bv
                if av < 50 or lum > 200:
                    pixels[px, py] = (255, 255, 255, 0)
                else:
                    pixels[px, py] = (0, 0, 0, 255)
        crop.save(f"{out}/icon_{r:02d}_{c:02d}.png")
        count += 1

print(f"Saved {count} icons to '{out}/'")
