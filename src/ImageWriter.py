import os

def writeFrames(tiles, name):
    fileName, ext = os.path.splitext(name)
    for i, tile in enumerate(tiles):
        tile.save(f'{fileName}_{i}{ext}')

def writeAnimation(tiles, name, fps):
    tiles = [ t for t in tiles ]
    tiles[0].save(name, save_all=True, append_images=tiles[1:], optimize=True, loop=0, disposal=2, duration=1000/fps)