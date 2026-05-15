from PIL import Image
import os

icon_dir = "icons"
threshold = 200  # pixels darker than this become black, lighter become transparent

converted = 0
for fname in os.listdir(icon_dir):
    if not fname.endswith(".png"):
        continue
    path = os.path.join(icon_dir, fname)
    img = Image.open(path).convert("RGBA")
    pixels = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            r, g, b, a = pixels[x, y]
            # Treat as dark if luminance is below threshold
            lum = 0.299 * r + 0.587 * g + 0.114 * b
            if a < 50 or lum > threshold:
                pixels[x, y] = (255, 255, 255, 0)   # transparent
            else:
                pixels[x, y] = (0, 0, 0, 255)        # pure black
    img.save(path)
    converted += 1

print(f"Converted {converted} icons to pure black + transparent")
