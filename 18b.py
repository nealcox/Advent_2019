import sys
from collections import defaultdict, deque, namedtuple
from math import atan2, gcd
from string import ascii_lowercase, ascii_uppercase

Pos = namedtuple("Pos", ("x", "y"))
State = namedtuple("State", ("keys", "ps"))


def main():

    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = "18-input.txt"
    grid, p = setup(input_file)

    all_keys = set(c for c in grid.values() if c in ascii_lowercase)

    steps = 0
    ps = set()
    ks = frozenset()
    for (dx, dy) in {(1, 0), (-1, 0), (0, 1), (0, -1)}:
        grid[Pos(p.x + dx, p.y + dy)] = "#"
    grid[p] = "#"
    for (dx, dy) in {(1, 1), (1, -1), (-1, 1), (-1, -1)}:
        ps.add(Pos(p.x + dx, p.y + dy))
    state = State(ks, frozenset(ps))
    states = defaultdict(lambda: float("inf"))
    for p in ps:
        states[(frozenset(), p)] = steps

    tests = set()
    tests.add(state)
    finished = False
    while not finished:
        print(f"Steps: {steps}")
        # print(f"To test: {tests}")
        next_tests = set()
        steps += 1
        for state in tests:
            for pos in state.ps:
                for (dx, dy) in {(1, 0), (-1, 0), (0, 1), (0, -1)}:
                    next_ps = set()
                    for p in state.ps:
                        if p != pos:
                            next_ps.add(p)
                    ks = state.keys
                    next_pos = Pos(pos.x + dx, pos.y + dy)
                    if grid[next_pos] == "#" or (
                        grid[next_pos] in ascii_uppercase
                        and grid[next_pos].lower() not in state.keys
                    ):
                        pass
                    else:
                        c = grid[next_pos]
                        if c in ascii_lowercase:
                            ks = frozenset(state.keys | set(c))
                            if ks == all_keys:
                                finished = True
                                print(f"All keys collected after {steps} steps")
                        next_ps.add(next_pos)
                        next_ps = frozenset(next_ps)
                        next_state = State(ks, next_ps)
                        for p in next_ps:
                            if steps <= states[(ks, p)]:
                                states[(ks, p)] = steps
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
