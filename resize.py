from PIL import Image
from utils import printProgressBar, count
from pathlib import Path
import argparse


def resize_images(path, format, height, width):
    amount = count(path, format)

    c = 0
    print('Resizing all {} images in {} to {}x{}'.format(format, path, width, height))
    for path in Path(path).rglob('*.' + format):
        img_open = Image.open(path)
        img_open = img_open.resize((width, height), Image.ANTIALIAS)

        img_open.save(path)
        # print('Saving: {}'.format(path))
        printProgressBar(c + 1, amount, prefix='Progress:', suffix='Complete', length=50)
        c += 1

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", help="Root path of images")
    parser.add_argument("-f", "--format", help="Format of images")
    parser.add_argument("-wi", "--width", help="Width of images")
    parser.add_argument("-he", "--height", help="Height of images")

    args = parser.parse_args()
    path = str(args.path)
    format = str(args.format)
    width = int(args.width)
    height = int(args.height)

    resize_images(path, format, height, width)