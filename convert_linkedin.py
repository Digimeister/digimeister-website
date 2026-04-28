from PIL import Image

def to_pixel_art(src, dst, threshold=128):
    img = Image.open(src).convert("RGBA")

    # Composite onto white so any transparency becomes white background
    flat = Image.new("RGBA", img.size, (255, 255, 255, 255))
    flat.paste(img, (0, 0), img)

    # Downscale to 16x16 with high-quality filter
    small = flat.convert("L").resize((16, 16), Image.Resampling.LANCZOS)

    # Threshold to pure black + transparent
    art = Image.new("RGBA", (16, 16), (0, 0, 0, 0))
    px = art.load()
    src_px = small.load()
    for y in range(16):
        for x in range(16):
            if src_px[x, y] < threshold:
                px[x, y] = (0, 0, 0, 255)

    # Place in 18x18 canvas with 1px padding (matches the other icon pack)
    canvas = Image.new("RGBA", (18, 18), (0, 0, 0, 0))
    canvas.paste(art, (1, 1), art)
    canvas.save(dst)
    print(f"Converted {src} -> {dst} (16x16 inside 18x18)")

to_pixel_art("linkedin.png",       "linkedin.png")
to_pixel_art("linkedin_solid.png", "linkedin_solid.png")
