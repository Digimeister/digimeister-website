from PIL import Image
import os

# Trim the 1px sprite-sheet border on each side → true 16x16 pixel art
icon_dir = "icons"
for fname in os.listdir(icon_dir):
    if not fname.endswith(".png"):
        continue
    path = os.path.join(icon_dir, fname)
    img = Image.open(path)
    w, h = img.size
    if w == 18 and h == 18:
        img = img.crop((1, 1, 17, 17))   # 1px inset on all sides → 16x16
    img.save(path)

print("Trimmed all 18x18 icons to 16x16")
