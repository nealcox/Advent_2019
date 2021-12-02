import re
import sys
from collections import defaultdict
from itertools import permutations


def main():
    if len(sys.argv) > 2:
        filename = sys.argv[1]
        num_cards = int(sys.argv[2])
        num_deals = 1
    else:
        filename = "input.txt"
        num_cards = 119315717514047
        num_deals = 101741582076661
    with open(filename) as f:
        input_text = f.read().strip()
    print(f"Answer: {calculate(input_text, num_cards, num_deals)}")


def calculate(input_text, num_cards, num_deals):

    given = partlines(input_text)

    # Equivalent transformation: a deal with increment followed by a cut
    test_points = []
    for test_point in (0,1):
        for transform in given:
            if transform[0] == "deal" and transform[-1] == "stack":
                test_point = num_cards - 1 - test_point
            elif transform[0] == "deal":
                test_point = (test_point * int(transform[-1])) % num_cards
            elif transform[0] == "cut":
                test_point = (test_point - int(transform[-1])) % num_cards
        test_points.append(test_point)
    cut_val = -test_points[0]
    inc_val = (test_points[1] - test_points[0]) % num_cards

    # Repeated application:
    # consider "a" -> a * inc_val - cut_val
    # then         -> (a * inc_val - cut_val) * inc_val - cut_val after 2 goes
    # then         -> a * (inc_val) ** 3 - cut_val * (1 + inc_val + inc_val **2)
    #                                                             after 3 goes
    # ie -> a * inc_val ** n + cut_val * (inc_val ** n -1) / (inc_val - 1)

    inc_val_multi = pow(inc_val,num_deals,num_cards)
    cut_val_multi = (
            -cut_val * 
            ( pow(inc_val, num_deals, num_cards) - 1) *
            pow(inc_val - 1, -1, num_cards)
            ) % num_cards

    # Require what maps to 2020, so first undo the cut:
    ans = (2020 - cut_val_multi ) % num_cards

    # now undo the multiplication
    ans = ans * pow(inc_val_multi, -1, num_cards) % num_cards

    return ans


def partlines(s):
    given = []
    for line in s.split("\n"):
        line = line.split()
        given.append(line)
    return given


if __name__ == "__main__":
    exit(main())
