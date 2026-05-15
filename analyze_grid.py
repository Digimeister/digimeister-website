from PIL import Image
import numpy as np

img = Image.open("1-bit 16px icons part-1 outlines.png").convert("RGBA")
data = np.array(img)
w, h = img.size
print(f"Image size: {w}x{h}")

# Look for column boundaries by finding vertical lines that are mostly white/transparent
# A column boundary is a column of pixels that is all background (white or transparent)

# Check alpha channel - transparent = background
alpha = data[:, :, 3]
# Also check if white (R=255, G=255, B=255)
rgb = data[:, :, :3]
is_white = np.all(rgb == 255, axis=2)
is_bg = (alpha == 0) | is_white

# Find columns that are fully background
col_all_bg = np.all(is_bg, axis=0)  # True if entire column is background
row_all_bg = np.all(is_bg, axis=1)  # True if entire row is background

print("\nFirst 80 columns (T=all-bg, .=has-content):")
print(''.join('T' if col_all_bg[i] else '.' for i in range(min(80, w))))

print("\nFirst 80 rows (T=all-bg, .=has-content):")
print(''.join('T' if row_all_bg[i] else '.' for i in range(min(80, h))))

# Find runs of content vs background to determine cell size
# Look for repeating pattern
content_cols = np.where(~col_all_bg)[0]
if len(content_cols) > 0:
    # Find gaps between content columns
    gaps = np.where(np.diff(content_cols) > 1)[0]
    if len(gaps) > 1:
        # Cell width = distance between gap starts
        gap_positions = content_cols[gaps] + 1
        print(f"\nGap positions in columns: {gap_positions[:20]}")
        if len(gap_positions) > 1:
            strides = np.diff(gap_positions)
            print(f"Strides between gaps: {strides[:20]}")
