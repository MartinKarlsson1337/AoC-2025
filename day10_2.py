from SearchProblemsAI.search_algorithms import A_star
from state import ButtonProblem, CounterProblem, CounterState
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
    with open('day10.txt') as f:
        input_puzzle = f.readlines()
    
    total_sum = 0
    for line in tqdm(input_puzzle, total=len(input_puzzle)):
        line = line.strip()
        lights = get_lights(line)
        buttons = get_buttons(line)
        joltages = get_joltages(line)
        
        problem = CounterProblem(lights, buttons, joltages)
        def counter_heuristic(state: CounterState) -> float:
            counters = state.counters
            buttons = problem.buttons
            
            # Identify zero positions
            missing = [i for i, v in enumerate(counters) if v == 0]
            if not missing:
                return 0
            
            # Compute max coverage of missing counters per action
            max_cover = 1
            for b in buttons:
                covered = sum(1 for i in b if counters[i] == 0)
                if covered > max_cover:
                    max_cover = covered

            # Lower bound on steps left:
            # ceil(#missing / max_cover)
            return (len(missing) + max_cover - 1) // max_cover

        
        list_of_actions = A_star(counter_heuristic).solve(problem)
        total_sum += len(list_of_actions)
        
    print(total_sum)
        


    