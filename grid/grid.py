import numpy as np
from PIL import Image


class Grid:
    def __init__(self, image: Image.Image, shape, name: str, type: str = "jpg") -> None:
        self.__array: np.array = np.array(image)
        self.__type = type
        self.__shape = shape
        self.name = name
        self.grid = self.__splitImage()
        self.__splitRow()

    def save(self):
        for i, row in enumerate(self.grid):
            for j, column in enumerate(row):
                Image.fromarray(column).save(
                    f"{self.name}_{i}x{j}.{self.__type}")

    def __splitImage(self):
        splits = self.__shape[0]
        return np.array_split(self.__array, splits, 0)

    def __splitRow(self):
        splits = self.__shape[1]
        grid = []
        for row in self.grid:
            grid.append(np.array_split(row, splits, 1))
        self.grid = grid
