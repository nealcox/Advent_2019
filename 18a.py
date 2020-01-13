import sys
from collections import defaultdict, deque, namedtuple
from math import atan2, gcd
from string import ascii_lowercase, ascii_uppercase

Pos = namedtuple("Pos", ("x", "y"))
State = namedtuple("State", ("keys", "pos"))


def main():

    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = "18-input.txt"
    grid, p = setup(input_file)

    all_keys = set(c for c in grid.values() if c in ascii_lowercase)

    steps = 0
    state = State(frozenset(), p)
    states = defaultdict(lambda: float("inf"))
    states[state] = steps

    tests = set()
    tests.add(state)
    finished = False
    while not finished:
        next_tests = set()
        steps += 1
        for state in tests:
            for (dx, dy) in {(1, 0), (-1, 0), (0, 1), (0, -1)}:
                p = state.pos
                ks = state.keys
                next_p = Pos(p.x + dx, p.y + dy)
                if grid[next_p] == "#" or (
                    grid[next_p] in ascii_uppercase
                    and grid[next_p].lower() not in state.keys
                ):
                    pass
                else:
                    c = grid[next_p]
                    if c in ascii_lowercase:
                        ks = frozenset(ks | set(c))
                        if ks == all_keys:
                            finished = True
                            print(f"All keys collected after {steps} steps")
                    next_state = State(ks, next_p)
                    if steps <= states[next_state]:
                        states[next_state] = steps
                        next_tests.add(next_state)
        if next_tests:
            tests = next_tests
        else:
            finished = True


def setup(filename):
    grid = {}
    p = None
    with open(filename) as f:
        for y, row in enumerate(f.readlines()):
            for x, c in enumerate(row.strip()):
                grid[Pos(x, y)] = c
                if c == "@":
                    p = Pos(x, y)
    return grid, p


if __name__ == "__main__":
    main()
