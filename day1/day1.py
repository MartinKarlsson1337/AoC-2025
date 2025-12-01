

class Cell:
    def __init__(self, num, next_cell=None, prev_cell=None):
        self.num = num
        self.next = next_cell
        self.prev = prev_cell


class CircularList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    def next(self):
        self.current = self.current.next
        return self

    def prev(self):
        self.current = self.current.prev
        return self

    def jump(self, steps):
        for i in range(steps):
            self.next()

    def reverse(self, steps):
        for i in range(steps):
            self.prev()

    def add(self, cell):
        if self.head is None:
            self.head = cell
            self.tail = cell
            self.current = cell

        elif self.head.next is None:
            cell.next = self.head
            cell.prev = self.head
            self.head.prev = cell
            self.head.next = cell
            self.tail = cell

        else:
            cell.next = self.head
            cell.prev = self.tail
            self.head.prev = cell
            self.tail.next = cell
            self.tail = cell

if __name__ == "__main__":
    circular_list = CircularList()

    for i in range(100):
        new_cell = Cell(i)
        circular_list.add(new_cell)
   
    circular_list.jump(50)

    with open("day1.txt", "r") as f:
        commands = f.read().split("\n")

    
    count = 0
    for command in commands:
        if "L" in command:
            steps = int(command.split("L")[-1])
            circular_list.reverse(steps)

        if "R" in command:
            steps = int(command.split("R")[-1])
            circular_list.jump(steps)

        print("Current: ", circular_list.current.num)
        if circular_list.current.num == 0:
            count += 1

    print(count)
