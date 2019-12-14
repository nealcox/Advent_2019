from time import sleep
import curses
import sys
from collections import deque
from itertools import permutations
from intcode_machine import IntcodeMachine

"""
- Position the Cursor:
  \033[<L>;<C>H
     Or
  \033[<L>;<C>f
  puts the cursor at line L and column C.
- Move the cursor up N lines:
  \033[<N>A
- Move the cursor down N lines:
  \033[<N>B
- Move the cursor forward N columns:
  \033[<N>C
- Move the cursor backward N columns:
  \033[<N>D

- Clear the screen, move to (0,0):
  \033[2J
- Erase to end of line:
  \033[K

- Save cursor position:
  \033[s
- Restore cursor position:
  \033[u
"""

EMPTY = 0
WALL = 1
BLOCK = 2
PADDLE = 3
BALL = 4

chars = {EMPTY: " ", WALL: "#", BLOCK: "@", PADDLE: "T", BALL: "O"}


def main():

    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "13-input.txt"
    machine = IntcodeMachine()
    machine.load_memory(filename)
    machine.memory[0] = 2

    finished = False
    index = 0
    x_ball = x_paddle = 0
    score = 0
    input("press ENTER")
    print("\033[2J") # Clear screen
    while not finished:
        result = machine.run_program()
        if isinstance(result, int):
            finished = True
            break
        elif result == "Awaiting Input":
            if x_ball > x_paddle:
                machine.inputs.append(1)
            elif x_ball < x_paddle:
                machine.inputs.append(-1)
            else:
                machine.inputs.append(0)

            #print("\033[34;0H")
            #k = input()


            #            if k == 'a':
            #                machine.inputs.append(-1)
            #            elif k == 's':
            #                machine.inputs.append(1)
            #            elif k == ' ':
            #                machine.inputs.append(0)
            #            elif k == 'q':
            #                if x_ball > x_paddle:
            #                    machine.inputs.append(1)
            #                elif x_ball < x_paddle:
            #                    machine.inputs.append(-1)
            #                else:
            #                    machine.inputs.append(0)
            #            else:
            #                raise ValueError(f"Wrong key {k}")
            machine.run()

        print(f"\033[0;0HX")
        while index < len(machine.outputs):
            x, y, tile_id = machine.outputs[index : index + 3]
            index += 3
            if tile_id == BALL:
                x_ball = x
            elif tile_id == PADDLE:
                x_paddle = x

            if x == -1:
                print(f"\033[35;5HScore: {tile_id}               ")
            else:
                print(f"\033[{y};{x}H{chars[tile_id]}")

    return score


if __name__ == "__main__":
    print(main())
