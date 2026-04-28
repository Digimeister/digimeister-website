from PIL import Image
import os

img = Image.open("1-bit 16px icons part-1 outlines.png")
print("Size:", img.size)
print("Mode:", img.mode)

w, h = img.size
icon_size = 16
cols = w // icon_size
rows = h // icon_size
print(f"Grid: {cols} cols x {rows} rows = {cols * rows} icons")

out_dir = "icons"
os.makedirs(out_dir, exist_ok=True)

count = 0
for row in range(rows):
    for col in range(cols):
        x = col * icon_size
        y = row * icon_size
        icon = img.crop((x, y, x + icon_size, y + icon_size))
        filename = f"{out_dir}/icon_{row:02d}_{col:02d}.png"
        icon.save(filename)
        count += 1

print(f"Saved {count} icons to '{out_dir}/'")
