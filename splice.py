import src.ImageSplitter as ImageSplitter
import src.ImageWriter as ImageWriter
from itertools import islice
import os
import argparse


def main(infile, outfile, rows, cols, frames):
    if frames is None:
        frames = rows * cols
    print(f'{infile} -> {outfile}: {rows}x{cols} [{frames}]')
    tiles = ImageSplitter.get_tiles(infile, rows, cols)
    tiles = islice(tiles, frames)

    _, extention = os.path.splitext(outfile)

    if (extention == '.gif' or extention == '.webp'):
        ImageWriter.writeAnimation(tiles, outfile)
    else:
        ImageWriter.writeFrames(tiles, outfile)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input"  , type=str, required=True, help= "Input file")
    parser.add_argument("-o", "--output" , type=str, required=True, help= "Output file")
    parser.add_argument("-r", "--rows"   , type=int, required=True, help= "Number of rows")
    parser.add_argument("-c", "--columns", type=int, required=True, help= "Number of columns")
    parser.add_argument("-f", "--frames" , type=int, required=False, help= "Number of frames")
    args = parser.parse_args()

    main(args.input, args.output, args.rows, args.columns, args.frames)

