import sys
from collections import defaultdict, namedtuple
from copy import copy


Position = namedtuple('Position',['x','y'])

def main():
    if len(sys.argv) == 1:
        filename = "24-input.txt"
    else:
        filename = sys.argv[1]

    scan = defaultdict(str)
    seen = set()
    seen.add(biodivesity(scan))

    start_text = get_input(filename)

    for y, line in enumerate(start_text.split("\n")):
        for x, c in enumerate(line.strip("\n")):
            scan[(x, y)] = c
    width = x
    height = y

    finished=False
    mins=0
    print_scan(scan,mins)
    while not finished:
        mins += 1
        next_scan = get_next_scan(scan)
        print_scan(next_scan,mins)
        bio = biodivesity(next_scan)
        if bio in seen:
            finished = True
            print(f"Already seen this scan")
            print(f"Biodiversity rating: {bio}")
        scan = next_scan
        seen.add(biodivesity(scan))


def biodivesity(scan):
    power = -1 
    bio = 0
    for y in range(5):
        for x in range(5):
            power += 1
            if scan[x,y] == '#':
                bio += 2** power
    return bio



def get_next_scan(scan):
    next_scan = defaultdict(str)
    displacments = {(1,0),(-1,0),(0,1),(0,-1)}
    for x in range(5):
        for y in range(5):
            num_adj = 0
            for dx ,dy in displacments:
                    if scan[x+dx,y+dy] == "#":
                        num_adj += 1
                
            if scan[x,y] == "#":
                if num_adj == 1:
                    next_scan[x,y] = '#'
                else:
                    next_scan[x,y] = '.'
            elif num_adj == 1 or num_adj == 2:
                next_scan[x,y] = '#'
            else:
                next_scan[x,y] = scan[x,y]
    return next_scan
                
                    


def print_scan(scan,mins=None):
    if mins:
        print(f"After {mins} minutes:")
    for y in range(5):
        for x in range(5):
            print(scan[x,y],end="")
        print()
    print(f"Biodiversuty: {biodivesity(scan)}")
    print()
    

def get_input(filename):
    with open(filename) as f:
        inputs = f.read()
    return inputs


if __name__ == "__main__":
    main()
