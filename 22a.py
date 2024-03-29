import re
import sys
from collections import defaultdict
from itertools import permutations


def main():
    if len(sys.argv) > 2:
        filename = sys.argv[1]
        num_cards = int(sys.argv[2])
    else:
        filename = "input.txt"
        num_cards = 10007
    with open(filename) as f:
        input_text = f.read().strip()
    print(f"Answer: {calculate(input_text, num_cards)}")


def calculate(input_text, num_cards):

    answer = None
    given = partlines(input_text)

    # Equivalent transformation: a deal with increment followed by a cut
    # 0 maps to:
    test_points = []
    for test_point in (0,1,2019):
        for transform in given:
            if transform[0] == "deal" and transform[-1] == "stack":
                test_point = num_cards - 1 - test_point
            elif transform[0] == "deal":
                test_point = (test_point * int(transform[-1])) % num_cards
            elif transform[0] == "cut":
                test_point = (test_point - int(transform[-1])) % num_cards
        test_points.append(test_point)
    cut_val = (num_cards - test_points[0]) % num_cards
    inc_val = (test_points[1] - test_points[0]) % num_cards
    print(f"[0,1] map to {test_points}, so equivalent is 'deal with increment"
            f" {inc_val}', followed by 'cut {cut_val}'")

    answer = test_points[-1]
    return answer


def parse(s):
    given = partlines(s)
    return given


def partlines(s):
    given = []
    for line in s.split("\n"):
        line = line.split()
        given.append(line)
    return given


def get_one_int_per_line(s):
    ints = []
    for line in s.split("\n"):
        ints.append(int(i))
    return ints


def get_re(s):
    given = []
    r = re.compile(r"(\d+)")
    for line in s.split("\n"):
        res = []
        for i in r.findall(line):
            res.append(int(i))
        given.append(res)
    return given


if __name__ == "__main__":
    exit(main())
