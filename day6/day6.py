import numpy as np

def filter_line(line):
    while '' in line:
        line.remove("")

    while '\n' in line:
        line.remove('\n')

    for i in range(len(line)):
        line[i] = line[i].strip().replace('\n', '')

    return line

if __name__ == '__main__':
    with open("day6/day6.txt", "r") as f:
        lines = f.readlines()

    lines = [filter_line(line.split(' ')) for line in lines]

    print(lines)

    operators = lines[-1]
    data = np.array(lines[:-1], dtype=int)
    
    sum = np.sum(data, axis=0)
    prod = np.prod(data, axis=0)

    total = 0
    for i, op in enumerate(operators):
        if op == '+':
            total += sum[i]
        elif op == '*':
            total += prod[i]

    print("Final total:", total)
