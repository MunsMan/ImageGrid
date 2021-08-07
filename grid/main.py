from typing import Tuple
from PIL import Image
from pathlib import Path
import click
import warnings

from .grid import Grid


def nameFromPath(path: str) -> str:
    return "".join(path.split("/")[-1].split(".")[0:-1])


def typeFromPath(path: str) -> str:
    return path.split(".")[-1]


def loadImage(filepath: Path) -> Image:
    return Image.open(filepath)


def getFormat(format) -> Tuple[bool, Tuple[int, int]]:
    if len(format) == 1:
        if format[0].find(",") != -1:
            format = format[0].split(",")
            try:
                format = (int(format[0]), int(format[1]))
            except:
                print("Couldn't parse specified Format.")
                print("Format need to be <Integer,Integer>")
                exit()
            return True, format
    return False, ()


@ click.command(context_settings={"ignore_unknown_options": True})
@ click.argument("image", nargs=1, type=click.Path(exists=True))
@ click.option('-r', '--row', 'row', default=1, type=int, help="Number of Images in a row.")
@ click.option('-c', '--column', 'column', default=1, type=int, help="Number of Images in a column.")
@ click.option('-o', '--output', 'output', type=click.Path(exists=True), help="Output directory for the Grid")
@ click.option('--warning', default=False, help="To show warnings from dependencies.")
def main(image, row, column, output, warning):
    """
    This script splits the image into multiple by the provided grid shape.

    The original Image will not be changed, the script creates a copy and works with that.
    """
    if not warning:
        warnings.filterwarnings("ignore")
    if row == column == 1:
        click.echo(click.get_current_context().get_help())
        exit()
    filename = nameFromPath(image)
    filetype = typeFromPath(image)
    filepath: Path = Path(image)
    image = loadImage(filepath)
    grid: Grid = Grid(image, (column, row), filename, output, type=filetype)
    grid.save()


if __name__ == "__main__":
    main()
