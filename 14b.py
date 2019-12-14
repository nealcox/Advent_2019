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
    
    ore_for_one = ore_for_fuel(1,recipes)
    max_ore =1000000000000
    lower_est = max_ore // ore_for_one
    lower_est_ore = ore_for_fuel(lower_est,recipes)
    upper_est = lower_est * 2
    upper_est_ore = ore_for_fuel(upper_est,recipes)
    while upper_est_ore < max_ore:
        upper_est *= 22
    print(f"Lower est {lower_est} uses {lower_est_ore}: Upper est {upper_est} uses {upper_est_ore}")
    while True:
        mid_est = (lower_est + upper_est) //2
        ore_for_mid = ore_for_fuel(mid_est,recipes)
        print(f"{mid_est} needs {ore_for_mid}")
        if ore_for_mid > max_ore:
            upper_est = mid_est
            upper_est_ore = ore_for_mid
        elif ore_for_mid < max_ore:
            lower_est = mid_est
            lower_est_ore = ore_for_mid
        print(f"Lower est {lower_est} uses {lower_est_ore}: Upper est {upper_est} uses {upper_est_ore}")
        if upper_est - lower_est ==1:
            print(f"Can produce {lower_est} units of fuel")
            break



def ore_for_fuel(amt,recipes):
    finished = False
    required = [Qty_Type(amt,"FUEL")]
    spare = defaultdict(int)
    while not finished:
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
    return required[0].qty


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
