import sys

def main():

    if len(sys.argv) > 1:
        path1,path2 = get_paths(sys.argv[1])
    else:
        path1,path2 = get_paths("03-input.txt")

    print(f"paths:\n{path1}\n{path2}")

    where_been1 = get_where_been(path1)
    where_been2 = get_where_been(path2)

    print(f"Where been:\n{where_been1}\n{where_been2}")
    
    intersections = where_been1 & where_been2
    print(f"Intersections: {intersections}")

    closest = float("inf")

    for intersection in intersections:
        manhattan = abs(intersection[0]) + abs(intersection[1])
        if manhattan < closest:
            closest = manhattan

    print(closest)
        
        





def get_where_been(path):
    where_been = set()
    x = y = 0
    for movement in path:
        direction = movement[0]
        distance = int(movement[1:])
        if direction == 'U':
            for i in range(1,distance +1):
                y -= 1
                where_been.add( (x,y) )
        elif direction == 'D':
            for i in range(1,distance +1):
                y += 1
                where_been.add( (x,y) )
        elif direction == 'R':
            for i in range(1,distance +1):
                x += 1
                where_been.add( (x,y) )
        elif direction == 'L':
            for i in range(1,distance +1):
                x -= 1
                where_been.add( (x,y) )
        else:
            print(f"Cannot process {movement}")
    return where_been



    


def get_paths(filename):
    path1 = []
    path2 = []
    with open(filename) as f:
        for value in f.readline().strip().split(','):
            path1.append(value)
        for value in f.readline().strip().split(','):
            path2.append(value)
    return path1, path2


if __name__ == "__main__":
    main()
