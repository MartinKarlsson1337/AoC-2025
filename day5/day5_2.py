from tqdm.auto import tqdm

class Range:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def contains(self, value: int) -> bool:
        return self.start <= value <= self.end
    
    def merge(self, other: 'Range') -> 'Range':
        new_start = min(self.start, other.start)
        new_end = max(self.end, other.end)
        return Range(new_start, new_end)

class RangeManager:
    def __init__(self):
        self.ranges: list[Range] = []

    def optimize_ranges(self) -> list[Range] | None:
        merged_ranges = []
        for range1 in self.get_ranges():
            for range2 in self.get_ranges():
                if range1 is range2:
                    continue

                if range1.contains(range2.start) or range1.contains(range2.end) or \
                   range2.contains(range1.start) or range2.contains(range1.end):
                    merged_range = range1.merge(range2)
                    self.ranges.remove(range1)
                    self.ranges.remove(range2)
                    self.ranges.append(merged_range)
                    merged_ranges.append((range1, range2, merged_range))

        return merged_ranges if merged_ranges else None

    def add_range(self, start: int, end: int):
        new_range = Range(start, end)
        self.ranges.append(new_range)
        merged_range = self.optimize_ranges()
        while merged_range is not None:
            merged_range = self.optimize_ranges()

    def get_min(self):
        if not self.ranges:
            return None
        return min(range.start for range in self.ranges)

    def get_max(self):
        if not self.ranges:
            return None
        return max(range.end for range in self.ranges)

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
        start, end = parse_range(line)
        rm.add_range(start, end)

    
    start, end = rm.get_min(), rm.get_max()
    print(f"Overall range: {start} - {end}")
    print("Ranges: ")
    print("\n".join([f"{r.start} - {r.end}" for r in rm.get_ranges()]))

    print(len([i for i in rm.get_ranges()]))
        
    sum = 0
    for range in rm.get_ranges():
        sum += range.end - range.start + 1

    print(f"Total fresh food items: {sum}")
