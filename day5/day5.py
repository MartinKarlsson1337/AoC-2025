from dataclasses import dataclass

class RangeManager:
    def __init__(self):
        self.ranges = []

    def add_range(self, start: int, end: int):
        self.ranges.append((start, end))

    def get_ranges(self):
        for range in self.ranges:
            yield range
    

def parse_range(line: str):
    start_str, end_str = line.split('-')
    return int(start_str), int(end_str)

if __name__ == "__main__":
    rm = RangeManager()
    with open('day5/day5.txt', 'r') as f:
        puzzle_input = f.read().strip().splitlines()

    split = puzzle_input.index('')
    range_lines = puzzle_input[:split]
    food_lines = puzzle_input[split + 1:]

    for line in range_lines:
        print(line)
        start, end = parse_range(line)
        rm.add_range(start, end)

    fresh_count = 0
    for line in food_lines:
        food_id = int(line)
        is_fresh = False
        for start, end in rm.get_ranges():
            if start <= food_id <= end:
                is_fresh = True
                break

        if is_fresh:
            fresh_count += 1

    print(f"Total fresh food items: {fresh_count}")
