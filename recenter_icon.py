from PIL import Image

src = "icons/icon_06_10.png"
img = Image.open(src).convert("RGBA")
w, h = img.size
print(f"Image size: {w}x{h}")

# Find bbox of non-transparent pixels
bbox = img.getbbox()
print(f"Content bbox: {bbox}")

if bbox:
    # Crop to content
    content = img.crop(bbox)
    cw, ch = content.size
    print(f"Content size: {cw}x{ch}")

    # Create new transparent canvas same size as original
    centered = Image.new("RGBA", (w, h), (0, 0, 0, 0))

    # Paste content centered
    offset_x = (w - cw) // 2
    offset_y = (h - ch) // 2
    centered.paste(content, (offset_x, offset_y))

    centered.save(src)
    print(f"Recentered. New offset: ({offset_x}, {offset_y})")
