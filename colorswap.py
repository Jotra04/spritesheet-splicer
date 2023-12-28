from PIL import Image
from itertools import product
import sys

def main(img_path, palette_path, overlays, outFile):
    print(overlays)
    img = Image.open(img_path)
    w, h = img.size
    pixel_map = img.load()

    palette_map = Image.open(palette_path).load()

    for i, j in product(range(w), range(h)):
        alpha = pixel_map[i,j][-1]
        if alpha > 0 and alpha+1 < 255:
            pixel_map[i,j] = palette_map[alpha, 0]

    for overlay in overlays:
        overlay_img = Image.open(overlay)
        img.paste(overlay_img, mask=overlay_img)

    img.save(outFile)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3:-1], sys.argv[-1])