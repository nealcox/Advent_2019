import re
import sys
from collections import defaultdict, namedtuple
from copy import copy
from string import ascii_uppercase



def main():
    if len(sys.argv) == 1:
        filename = "22-input.txt"
        pack_size = 10007
    else:
        filename = sys.argv[1]
        pack_size  = int(sys.argv[2])


    deal_text = get_input(filename)

    deals = []
    lines = []
    for line_text in deal_text.strip().split("\n"):
        line = line_text.split(' ')
        lines.append((line[0],line[-1]))

    for line in lines:
        if line[0] == "cut":
            deals.append(("cut",int(line[1])))
        elif line[0] == "deal":
            if line[1] == "stack":
                deals.append(("new_stack",))
            else:
                deals.append(("deal",int(line[1])))
        else:
            raise ValueError(f"Invalid deal {line}")
    cards = list(range(pack_size))

    for deal in deals:
        if deal[0] == "cut":
            cards = cut_n(cards,deal[1])
        elif deal[0] == "deal":
            cards = deal_n(cards,deal[1])
        elif deal[0] == "new_stack":
            cards = new_stack(cards)
        else:
            raise ValueError(f"Invalid deal {deal}")

    if len(sys.argv) == 1:
        print(f"Card 2019 at position {cards.index(2019)}.")
    else:
        print(cards)
        print(f"Card 1 at position {cards.index(1)}.")


def new_stack(cards):
    return [c for c in reversed(cards)]

def cut_n(cards,n):
    return cards[n:] + cards[:n]

def deal_n(cards,n):
    l = len(cards)
    new_cards = [0]*l
    index = 0
    for i in range(l):
        new_cards[index] = cards[i]
        index = (index + n) % l
    return new_cards



    

def get_input(filename):
    with open(filename) as f:
        inputs = f.read()
    return inputs


if __name__ == "__main__":
    main()
