from PIL import Image
from itertools import product

def get_tiles(filename, rows, cols):
    img = Image.open(filename)
    w, h = img.size

    dw = w // cols
    dh = h // rows

    grid = product(range(0, h-h%dh, dh), range(0, w-w%dw, dw))
    boxes = map( lambda x : (x[1], x[0], x[1]+dw, x[0]+dh), grid)
    return map(img.crop, boxes)