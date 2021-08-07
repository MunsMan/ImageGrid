from grid.grid import Grid
from PIL import Image


def loadImage(name: str = "test/test_image.jpg") -> Image.Image:
    return Image.open(name)


def test_shape():
    shape = (2, 3)
    name = "test"
    grid = Grid(loadImage(), shape, name)
    assert len(grid.grid) == shape[0]
    assert len(grid.grid[0]) == shape[1]
