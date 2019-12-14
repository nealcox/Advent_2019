import sys
from collections import defaultdict
from itertools import permutations
from intcode_machine import IntcodeMachine

"""

    0 is an empty tile. No game object appears in this tile.
    1 is a wall tile. Walls are indestructible barriers.
    2 is a block tile. Blocks can be broken by the ball.
    3 is a horizontal paddle tile. The paddle is indestructible.
    4 is a ball tile. The ball moves diagonally and bounces off objects.
"""

def main():

    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "13-input.txt"
    machine = IntcodeMachine()
    machine.load_memory(filename)

    finished = False
    while not finished:
        result = machine.run_program()
        if isinstance(result,int):
            finished = True
        elif result == "Awaiting Input":
            i = int(input("Enter no:"))
            machine.inputs.append(i)
            machine.run()
        else:
            raise ValueError(f"Unknown return value {result}")
    num_blocks = 0
    for index in range(0,len(machine.outputs),3):
        x,y,tile = machine.outputs[index:index+3]
        print(x,y,tile)
        if tile == 2:
            num_blocks += 1

    print(num_blocks)
        

        
        




if __name__ == "__main__":
    main()
