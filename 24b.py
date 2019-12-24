import sys
from collections import defaultdict, namedtuple
from copy import copy, deepcopy


def main():
    if len(sys.argv) == 1:
        filename = "24-input.txt"
        max_mins = 200
    else:
        filename = sys.argv[1]
        if sys.argv[2]:
            max_mins = int(sys.argv[2])
        else:
            max_mins = 10

    scan = defaultdict(dot)
    seen = set()
    seen.add(biodivesity(scan))

    start_text = get_input(filename)

    z = 0
    for y, line in enumerate(start_text.split("\n")):
        for x, c in enumerate(line.strip("\n")):
            scan[(x, y,z)] = c
    width = x
    height = y
    min_z = max_z = 0

    finished=False
    mins=0
    print_scan(scan,mins)
    while not finished:
        mins += 1
        next_scan = get_next_scan(scan)
        print_scan(next_scan,mins)
        #bio = biodivesity(next_scan)
        infected = get_infected(next_scan)
        print(mins,infected)
        if mins > max_mins:
            finished = True
            print(f"Infected: {infected}")
        scan = next_scan
        seen.add(biodivesity(scan))


def dot(x=None,y=None,z=None):
    return "."
def get_infected(scan):
    return sum( 1 for v in scan.values() if v == "#")

def biodivesity(scan):
    power = -1 
    bio = 0
    z = 0
    for y in range(5):
        for x in range(5):
            power += 1
            if scan[x,y,z] == '#':
                bio += 2** power
    return bio



def get_next_scan(scan):
    this_scan = deepcopy(scan)
    next_scan = defaultdict(dot)
    positions = list(this_scan.keys())
    to_check = deepcopy(positions)
    for p in positions:
        adj = get_adjacents(*p)
        for a in adj:
            to_check.append(a)
    for p in to_check:
        x, y, z = p
        if not (x == 2 and y == 2):
            num_adj = 0
            adjacents = get_adjacents( x,y,z)
            for p2 in adjacents:
                    if scan[p2] == "#":
                        num_adj += 1
                
            if scan[x,y,z] == "#":
                if num_adj == 1:
                    next_scan[x,y,z] = '#'
                else:
                    next_scan[x,y,z] = '.'
            elif num_adj == 1 or num_adj == 2:
                next_scan[x,y,z] = '#'
            else:
                next_scan[x,y,z] = scan[x,y,z]
    return next_scan
                
                    
def get_adjacents(x,y,z):
    displacements = {(1,0),(-1,0),(0,1),(0,-1)}
    adjacents = set()
    for dx,dy in displacements:
        adj =  (x+dx,y+dy,z)
        done = False
        if x + dx < 0:
            adjacents.add( (1,2,z-1) )
            done =True
        if y + dy < 0:
            adjacents.add( (2,1,z-1) )
            done =True
        if x + dx > 4:
            adjacents.add( (3,2,z-1) )
            done =True
        if y + dy > 4:
            adjacents.add( (2,3,z-1) )
            done =True
        if x+dx == 2 and y +dy == 2:
            if dx == 1:
                for i in range(5):
                    adjacents.add( (0,i, z+1) )
            if dx == -1:
                for i in range(5):
                    adjacents.add( (4,i, z+1) )
            if dy == 1:
                for i in range(5):
                    adjacents.add( (i,0, z+1) )
            if dy == -1:
                for i in range(5):
                    adjacents.add( (i,4, z+1) )
            done =True
        if not done:
            adjacents.add( adj )
    return adjacents


def print_scan(scan,mins=None):
    if mins:
        print(f"After {mins} minutes:")
    min_z = max_z = 0
    for p in scan.keys():
        _,_,z = p
        if z < min_z:
            min_z = z
        if z > max_z:
            max_z = z
    for z in range(min_z,max_z+1):
        print(f"Level {z}:")
        for y in range(5):
            for x in range(5):
                if x == 2 and y == 2:
                    print("?",end="")
                else:
                    print(scan[x,y,z],end="")
            print()
    print(f"Infected: {get_infected(scan)}")
    print()
    

def get_input(filename):
    with open(filename) as f:
        inputs = f.read()
    return inputs


if __name__ == "__main__":
    main()
    print((1,2,-1),get_adjacents(1,2,-1))
