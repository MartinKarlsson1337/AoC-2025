import numpy as np


class Present:
    def __init__(self, index: int, shape: list[list[str]]):
        self.index = index
        self.shape = np.zeros((3, 3), dtype=np.int8)
        self.area = 0

        for i, row in enumerate(shape):
            for j, col in enumerate(row):
                if col == '#':
                    self.area += 1
                    self.shape[i, j] = 1

    def __repr__(self):
        return '\n'.join([str(i) for i in self.shape.tolist()])
    
    def rotate(self):
        self.shape = np.rot90(self.shape)

    def hflip(self):
        self.shape = np.flip(self.shape, axis=1)

    def vflip(self):
        self.shape = np.flip(self.shape, axis=0)

class Region:
    def __init__(self, w: int, h: int, requirements: list[int]):
        self.w = w
        self.h = h
        self.grid = np.zeros((self.h, self.w), dtype=np.bool)
        self.requirements = requirements
        
    def __repr__(self):
        return "\n".join([str(i) for i in self.grid])

    def is_within_bounds(self, x, y):
        return 0 < x < self.w-1 and 0 < y < self.h-1

    def can_place_present(self, x: int, y: int):
        if self.is_within_bounds(x, y):
            return (self.grid[y-1:y+2, x-1:x+2] == False).all()
        return False

    def place_present(self, present: Present, x: int, y:int):
        if self.can_place_present(x, y):
            self.grid[y-1:y+2, x-1:x+2] = present.shape

    