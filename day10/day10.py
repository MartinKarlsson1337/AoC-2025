from SearchProblemsAI.search_algorithms import BFS
from state import ButtonProblem
from tqdm.auto import tqdm


def get_lights(line: str) -> list[str]:
    lights = line.split(']')[0]
    return list(lights[1:])

def get_buttons(line: str) -> list[tuple[int]]:
    line = line.split(']')[-1].split('{')[0].strip()
    buttons = []
    
    for button in line.split(' '):
        temp = []
        for i in button.strip('()').split(','):
            temp.append(int(i))
        buttons.append(tuple(temp))
        
    return buttons

def get_joltages(line: str) -> list[int]:
    line = line.split('{')[-1][:-1]
    joltages = [int(i) for i in line.split(',')]
    return joltages

if __name__ == '__main__':
    with open('test.txt') as f:
        input_puzzle = f.readlines()
    
    sum = 0
    for line in tqdm(input_puzzle, total=len(input_puzzle)):
        line = line.strip()
        lights = get_lights(line)
        buttons = get_buttons(line)
        joltages = get_joltages(line)
        
        problem = ButtonProblem(lights, buttons, joltages)
        list_of_actions = BFS().solve(problem)
        sum += len(list_of_actions)
        
    print(sum)
        


    