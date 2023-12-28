import src.ImageSplitter as ImageSplitter
import src.ImageWriter as ImageWriter
from itertools import islice
import os
import argparse


def main(infile, outfile, rows, cols, frames, margins, fps):
    if frames is None:
        frames = rows * cols

    print(f'{infile} -> {outfile}: {rows}x{cols} [{frames}], margins: {margins}')
    tiles = ImageSplitter.get_tiles(infile, rows, cols, margins)
    tiles = islice(tiles, frames)

    _, extention = os.path.splitext(outfile)

    if (extention == '.gif' or extention == '.webp'):
        ImageWriter.writeAnimation(tiles, outfile, fps)
    else:
        ImageWriter.writeFrames(tiles, outfile)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input"  , type=str, required=True, help= "Input file")
    parser.add_argument("-o", "--output" , type=str, required=True, help= "Output file")
    parser.add_argument("-r", "--rows"   , type=int, required=True, help= "Number of rows")
    parser.add_argument("-c", "--columns", type=int, required=True, help= "Number of columns")
    parser.add_argument("-f", "--frames" , type=int, required=False, help= "Number of frames")
    parser.add_argument("-mv", "--vmargins" , type=int, required=False, help= "Pixels in vertical margin", default=0)
    parser.add_argument("-mh", "--hmargins" , type=int, required=False, help= "Pixels in horizontal margin", default=0)
    parser.add_argument("-s", "--fps", type=int, required=False, help="Frames per second", default=12)
    args = parser.parse_args()

    main(args.input, args.output, args.rows, args.columns, args.frames, (args.vmargins, args.hmargins), args.fps)

