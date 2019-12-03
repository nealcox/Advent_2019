import sys


def main():

    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = "03-input.txt"
    path1, path2 = get_paths(input_file)

    where_been1 = get_where_been(path1)
    where_been2 = get_where_been(path2)

    intersections = where_been1 & where_been2

    closest = float("inf")
    for intersection in intersections:
        manhattan = abs(intersection[0]) + abs(intersection[1])
        if manhattan < closest:
            closest = manhattan

    print(closest)


def get_where_been(path):
    where_been = set()
    x = y = 0
    dxs = dict(zip("UDRL", [0, 0, 1, -1]))
    dys = dict(zip("UDRL", [-1, 1, 0, 0]))
    for movement in path:
        direction = movement[0]
        distance = int(movement[1:])
        for _ in range(1, distance + 1):
            x += dxs[direction]
            y += dys[direction]
            where_been.add((x, y))
    return where_been


def get_paths(filename):
    path1 = []
    path2 = []
    with open(filename) as f:
        for value in f.readline().split(","):
            path1.append(value)
        for value in f.readline().split(","):
            path2.append(value)
    return path1, path2


if __name__ == "__main__":
    main()
