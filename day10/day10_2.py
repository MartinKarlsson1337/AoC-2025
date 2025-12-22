import numpy as np

import pulp
import numpy as np

def min_presses(joltages, buttons):
    m = len(joltages)
    n = len(buttons)

    A = np.zeros((m, n), dtype=int)
    for j, btn in enumerate(buttons):
        for i in btn:
            A[i, j] = 1

    prob = pulp.LpProblem("Joltage", pulp.LpMinimize)

    x = [
        pulp.LpVariable(f"x_{j}", lowBound=0, cat="Integer")
        for j in range(n)
    ]

    prob += pulp.lpSum(x)

    for i in range(m):
        prob += pulp.lpSum(A[i, j] * x[j] for j in range(n)) == joltages[i]

    prob.solve(pulp.PULP_CBC_CMD(msg=False))

    return int(pulp.value(prob.objective))

def get_buttons(line: str) -> list[tuple[int]]:
    line = line.split(']')[-1].split('{')[0].strip()
    buttons = []
    
    for button in line.split(' '):
        temp = []
        for i in button.strip('()').split(','):
            temp.append(int(i))
        buttons.append(tuple(temp))
        
    return buttons

def get_lights(line: str) -> list[str]:
    lights = line.split(']')[0]
    return list(lights[1:])

def get_joltages(line: str) -> list[int]:
    line = line.split('{')[-1][:-1]
    joltages = [int(i) for i in line.split(',')]
    return joltages

if __name__ == '__main__':
    with open('day10/day10.txt') as f:
        input_puzzle = f.readlines()

    total = 0
    for line in input_puzzle:
        line = line.strip()
        buttons = get_buttons(line)
        joltages = np.array(get_joltages(line))
        total += min_presses(joltages, buttons)

    print(total)





