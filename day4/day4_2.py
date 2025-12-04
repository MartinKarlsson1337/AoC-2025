from typing import Iterator

class Mat:
    def __init__(self):
        self.mat = None

    def add_row(self, row) -> None:
        if self.mat is None:
            self.mat = []
            self.mat.append(row)

        elif len(row) == len(self.mat[0]):
            self.mat.append(row)

    def get(self, row, col) -> any:
        if 0 <= row < len(self.mat) and 0 <= col < len(self.mat[0]):
            return self.mat[row][col]
        return None

    def set(self, row, col, val) -> None:
        if 0 <= row < len(self.mat) and 0 <= col < len(self.mat[0]):
            self.mat[row][col] = val

    def __repr__(self) -> str:
        return "\n".join([str(row) for row in self.mat])

class Conv:
    def __init__(self, kernel_size=3, kernel_func=None):
        self.kernel_size = kernel_size
        self.kernel = []
        self.kernel_func = kernel_func

        for i in range(-self.kernel_size//2 + 1, self.kernel_size//2 + 1):
            for j in range(-self.kernel_size//2 + 1, self.kernel_size//2 + 1):
                self.kernel.append((i, j))


    def get_neighbors(self, mat: Mat, row, col) -> list[any]:
        res = []
        for i in self.kernel:
            res.append(mat.get(row + i[0], col + i[1]))

        return res
    
    def conv(self, mat: Mat) -> Iterator:
        for row in range(len(mat.mat)):
            for col in range(len(mat.mat[row])):
                neighbors = self.get_neighbors(mat, row, col)
                if self.kernel_func:
                    neighbors = self.kernel_func(neighbors)
                yield (row, col), neighbors
    

if __name__ == "__main__":
    with open('day4/day4.txt', 'r') as f:
        puzzle_input = f.read().strip().splitlines()

    mat = Mat()
    for line in puzzle_input:
        nums = []
        for element in line:
            if element == '.':
                nums.append(0)
            if element == '@':
                nums.append(1)
        
        mat.add_row(nums)

    def kernel_func(n):
        if n[len(n)//2] == 1:
            return n
        return None

    conv = Conv(kernel_func=kernel_func)

    number_of_accessible_rolls = 0
    change = 1
    while change > 0: 
        change = 0
        for (row, col), i in conv.conv(mat):
            if i is not None and sum([x for x in i if x is not None]) < 5:
                number_of_accessible_rolls += 1
                change += 1
                mat.set(row, col, 0)
    
    print(f"accessible rolls: {number_of_accessible_rolls}")