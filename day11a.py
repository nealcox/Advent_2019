import sys
from collections import defaultdict
from itertools import permutations
from intcode_machine import IntcodeMachine


def main():

    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "11-input.txt"
    machine = IntcodeMachine()
    machine.load_memory(filename)

    colours = defaultdict(int)
    x = y = 0
    heading = 'N'
    dx , dy = 0, -1
    index = 0
    max_x = max_y = 0
    min_x = min_y = 0
    colours[(x,y)] = 0
    finished = False
    while not finished:
        result = machine.run_program([colours[(x,y)]])
        if isinstance(result,int):
            finished = True
        elif result == "Awaiting Input":
            colour,turn = machine.outputs[index:index+2]
            index += 2
            if turn == 0:
                heading,dx,dy = turn_left(heading)
            elif turn == 1:
                heading,dx,dy = turn_right(heading)
            colours[(x,y)] = colour
            x,y = x + dx, y+dy
        else:
            raise ValueError(f"Unknown return value {result}")
    print(len(colours))
        

        
        
        
def turn_left(heading):
    if heading == 'N':
        return 'W',-1,0
    elif heading == 'W':
        return 'S',0,1
    elif heading == 'S':
        return 'E',1,0
    elif heading == 'E':
        return 'N',0,-1

def turn_right(heading):
    if heading == 'N':
        return 'E',1,0
    elif heading == 'E':
        return 'S',0,1
    elif heading == 'S':
        return 'W',-1,0
    elif heading == 'W':
        return 'N',0,-1






if __name__ == "__main__":
    main()
