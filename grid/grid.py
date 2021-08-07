import numpy as np
from os import path
from PIL import Image


class Grid:
    def __init__(self, image: Image.Image, shape, name: str, output: str = None, type: str = "jpg") -> None:
        self.__array: np.array = np.array(image)
        self.__type = type
        self.__shape = shape
        self.name = name
        self.__output = output
        self.grid = self.__splitImage()
        self.__splitRow()

    def save(self):
        for i, row in enumerate(self.grid):
            for j, column in enumerate(row):
                filename = f"{self.name}_{i}x{j}.{self.__type}"
                if self.__output:
                    filename = path.join(self.__output, filename)
                Image.fromarray(column).save(filename)

    def __splitImage(self):
        splits = self.__shape[0]
        return np.array_split(self.__array, splits, 0)

    def __splitRow(self):
        splits = self.__shape[1]
        grid = []
        for row in self.grid:
            grid.append(np.array_split(row, splits, 1))
        self.grid = grid
