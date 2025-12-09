from typing import Iterator

class Grid:
    def __init__(self):
        self.grid = []

    def insert(self, x: int, y: int, value: str) -> None:
        if y < len(self.grid) and x < len(self.grid[0]):
            self.grid[y][x] = value

    def get(self, x: int, y: int) -> str:
        return self.grid[y][x]

    def window(self, window_size=1) -> Iterator:
        for i, row in enumerate(self.grid):
            if i + window_size < len(self.grid):
                yield [row, self.grid[i + window_size]]
            
            else:
                yield self.grid[i:]

    def rows(self) -> Iterator:
        for row in self.grid:
            yield row

    def append_row(self, row: list[str]) -> None:
        self.grid.append(row)



if __name__ == '__main__':
    with open('day7/test.txt') as f:
        input_puzzle = f.read()

    input_puzzle = [list(i) for i in input_puzzle.splitlines()]

    grid = Grid()

    for row in input_puzzle:
        grid.append_row(row)

    split_count = 0
    for y, row in enumerate(grid.window()):
        print(y)
        if len(row) == 1:
            break
        
        else:
            for x, i in enumerate(row[0]):
                if i == 'S' or i == '|':
                    if row[1][x] == '.':
                        grid.insert(x, y+1, '|')
                    
                    elif row[1][x] == '^':
                        if grid.get(x-1, y+1) == '.' or grid.get(x+1, y+1) == '.':
                            grid.insert(x-1, y+1, '|')
                            grid.insert(x+1, y+1, '|')
                            split_count += 1

    with open('day7/output2.txt', 'a') as f:
        for row in grid.rows():
            row_str = "".join(row) + '\n'
            f.write(row_str)

                    
    print(split_count)


    