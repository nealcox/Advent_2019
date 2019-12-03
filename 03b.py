import sys


def main():

    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = "03-input.txt"
    path1, path2 = get_paths(input_file)

    where_been1 = get_where_been(path1)
    where_been2 = get_where_been(path2)

    intersections = set(where_been1.keys()) & set(where_been2.keys())

    min_steps = float("inf")

    for intersection in intersections:
        num_steps = where_been1[intersection] + where_been2[intersection]
        if num_steps < min_steps:
            min_steps = num_steps

    print(min_steps)


def get_where_been(path):
    where_been = {}
    x = y = 0
    steps = 0
    for movement in path:
        direction = movement[0]
        distance = int(movement[1:])
        if direction == "U":
            for i in range(1, distance + 1):
                steps += 1
                y -= 1
                if (x, y) not in where_been:
                    where_been[(x, y)] = steps
        elif direction == "D":
            for i in range(1, distance + 1):
                steps += 1
                y += 1
                if (x, y) not in where_been:
                    where_been[(x, y)] = steps
        elif direction == "R":
            for i in range(1, distance + 1):
                steps += 1
                x += 1
                if (x, y) not in where_been:
                    where_been[(x, y)] = steps
        elif direction == "L":
            for i in range(1, distance + 1):
                steps += 1
                x -= 1
                if (x, y) not in where_been:
                    where_been[(x, y)] = steps
        else:
            raise ValueError(f"Cannot process {movement}")
    return where_been


def get_paths(filename):
    path1 = []
    path2 = []
    with open(filename) as f:
        for value in f.readline().strip().split(","):
            path1.append(value)
        for value in f.readline().strip().split(","):
            path2.append(value)
    return path1, path2


if __name__ == "__main__":
    main()
