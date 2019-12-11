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
    colours[(x,y)] = 1
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
            if x < min_x:
                min_x = x
            if x > max_x:
                max_x = x
            if y < min_x:
                min_x = y
            if y > max_y:
                max_y = y

        else:
            raise ValueError(f"Unknown return value {result}")
    print(len(colours))
    for y in range(min_y,max_y+1):
        for x in range(min_x,max_x+1):
            if colours[(x,y)] == 1:
                print('#',end="")
            elif colours[(x,y)] == 0:
                print(' ',end="")
            else:
                raise ValueError(f"Error at position ({x}, {y}): colour {colours[(x,y)]}")
        print()
    print()
        

        
        
        
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
