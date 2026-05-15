from PIL import Image
for f in ["linkedin.png", "linkedin_solid.png", "icons-solid/icon_06_10.png", "icons/icon_07_02.png"]:
    im = Image.open(f).convert("RGBA")
    bbox = im.getbbox()
    print(f"{f}: size={im.size}, content bbox={bbox}")
