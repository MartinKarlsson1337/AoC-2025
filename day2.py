import re

def match_num(num):
    for i in range(len(num)//2):
        pattern = "/^([0-9]{" + str(i) + "})\1+$/"
        matches = re.fullmatch(pattern, num)
        print(matches)

def check_num(num):
    first = num[0:(len(num)//2)]
    last = num[(len(num)//2):]
    
    return first == last

def is_valid_num(num):
    return len(num) % 2 == 0

def check_range(start, end):
    invalid_ids = []
    for i in range(start, end + 1):
        id_str = str(i)
        if is_valid_num(id_str):
            if check_num(id_str):
                invalid_ids.append(i)
                
    return invalid_ids
            

if __name__ == '__main__':
    with open('day2/day2.txt') as f:
        puzzle_input = f.read()
        
    puzzle_input = puzzle_input.split(',')
    
    sum = 0
    
    for i in puzzle_input:
        start, end = i.split('-')
        start_num, end_num = int(start), int(end)

        invalid_ids = check_range(start_num, end_num)
        
        for id in invalid_ids:
            sum += id
            
    print(sum)
        
        

        
            