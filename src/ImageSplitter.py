from PIL import Image
from itertools import product

def get_tiles(filename, rows, cols, margins):
    img = Image.open(filename)
    w, h = img.size

    w -= 2*margins[1]
    h -= 2*margins[0]

    dw = w // cols
    dh = h // rows

    grid = product(range(0, h-h%dh, dh), range(0, w-w%dw, dw))
    boxes = map( lambda x : (x[1] + margins[1], x[0] + margins[0], x[1]+dw+margins[1], x[0]+dh+margins[0]), grid)
    return map(img.crop, boxes)