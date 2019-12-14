import sys
import re
from collections import defaultdict, deque, namedtuple

Qty_Type = namedtuple("Qty_Type", ["qty", "type"])
Input = namedtuple("Input", ["qty","ingredients"])
MAX_STEPS = 1000


def main():
    global MAX_STEPS

    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = "14-input.txt"
    recipes = setup(input_file)
    recipes['ORE'] = Input(1,[Qty_Type(1,'ORE')])
    finished = False
    step = 0
    required = [Qty_Type(1,"FUEL")]
    spare = defaultdict(int)
    while not finished:
        step += 1
        next_required = defaultdict(int)
        for r in required:
            have = spare[r.type]
            recipe = recipes[r.type]
            batches_to_make= -(-(r.qty - have)//recipe.qty)
            spare[r.type] = have + batches_to_make*recipe.qty - r.qty
            for ing in recipe.ingredients:
                next_required[ing.type] += batches_to_make*ing.qty

        required = [Qty_Type(next_required[ingredient],ingredient) for ingredient in next_required.keys()]

        if len(required) == 1:
            finished = True
    print(f"{required[0].qty} units of ORE needed")


def setup(filename):
    reg = re.compile(",|=>")
    recipes = {}
    with open(filename) as f:
        for line in f.readlines():
            r_l = re.split(',|=>',line.strip())
            to = parse(r_l[-1])
            from_ = []
            for r in r_l[:-1]:
                from_.append(parse(r))
            if to.type in recipes.keys():
                raise ValueError(f"Duplicate output {to.type}")
            recipes[to.type] = Input(to.qty,from_)


    return recipes

def parse(qt):
    q,t =  qt.strip().split(' ')

    return Qty_Type(int(q),t)

if __name__ == "__main__":
    main()
