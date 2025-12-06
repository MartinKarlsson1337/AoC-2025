import numpy as np

def filter_line(line):
    while '\n' in line:
        line.remove('\n')

    for i in range(len(line)):
        line[i] = line[i].strip().replace('\n', '')

    return line

def contains_number(s: str) -> bool:
    for char in s:
        if char.isdigit():
            return True
    return False

def parse_cephalopod_math(lines: np.ndarray, operators: list) -> np.ndarray:
    arr = [[]]
    index = 0
    for i in range(lines.shape[1]):
        col = lines[:, i]
        if not contains_number("".join(col.tolist())):
            arr.append([])
            index += 1

        else:
            arr[index].append(int("".join(col.tolist())))

    for r, row in enumerate(arr):
        operator = operators[r]
        while len(row) < lines.shape[0]:
            if operator == '+':
                row.append(0)
            elif operator == '*':
                row.append(1)

    return np.array(arr).transpose(1, 0)
        

if __name__ == '__main__':
    with open("day6/day6.txt", "r") as f:
        lines = f.read()

    lines = [list(i) for i in lines.splitlines()]
    operators = lines[-1]
    lines = np.array(lines[:-1])

    while ' ' in operators:
        operators.remove(' ')
    
    data = parse_cephalopod_math(lines, operators)

    sum = np.sum(data, axis=0)
    prod = np.prod(data, axis=0)

    total = 0
    for i, op in enumerate(operators):
        if op == '+':
            total += sum[i]
        elif op == '*':
            total += prod[i]

    print("Final total:", total)


