from SearchProblemsAI.search_problems import State, SearchProblem

class ButtonState(State):
    def __init__(self, indicator_lights: list[str]):
        self.indicator_lights = indicator_lights
        
    def __hash__(self):
        return hash(tuple(self.indicator_lights))
    
    def __eq__(self, other: 'ButtonState'):
        return self.indicator_lights == other.indicator_lights
    

def get_button_transition(state: ButtonState, button: tuple):
    new_state = [i for i in state.indicator_lights]
    
    for i in button:
        light_state = state.indicator_lights[i]
        if light_state == '.':
            new_state[i] = '#'
        else:
            new_state[i] = '.'
            
    return ButtonState(new_state)

class ButtonProblem(SearchProblem):
    def __init__(self, lights: list[str], buttons: list[tuple[int]], joltages: list[int]):
        self.lights = lights
        self.buttons = buttons
        self.jolatages = joltages
        
        self.goal_state = ButtonState(self.lights)
        
    def get_start_state(self):
        return ButtonState(['.' for _ in self.lights])
    
    def is_goal_state(self, state):
        return state == self.goal_state
    
    def get_actions(self, state):
        return self.buttons
    
    def get_transition(self, state, action):
        cost = 1
        new_state = get_button_transition(state, action)
        return (new_state, cost)
            
        
