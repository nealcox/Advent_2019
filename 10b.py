import sys
from collections import defaultdict, deque
from math import atan2, gcd, pi


def main():

    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = "10-input.txt"
    asteroids = setup(input_file)

    max_x = max_y = 0
    for a in asteroids:
        x = a[0]
        y = a[1]
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y

    print(f"Input:")
    for r in range(max_y + 1):
        for c in range(max_x + 1):
            if (c, r) in asteroids:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()

    num_can_see = {}

    for a in asteroids:
        vectors = get_vectors(a, asteroids)
        num_can_see[a] = len(vectors)

    max_seen = max(num_can_see.values())
    position = [p for p in num_can_see if num_can_see[p] == max_seen][0]
    print(position, max_seen)

    vectors = list(get_vectors(position, asteroids))
    angles_for_vectors = {}
    for v in vectors:
        angle = atan2(v[1], v[0]) + 3 * pi / 2
        if angle >= pi:
            angle -= 2 * pi
        angles_for_vectors[v] = angle

    vectors.sort(key=lambda v: angles_for_vectors[v])

    asteroids_by_vector = defaultdict(list)
    for v in vectors:
        x, y = position
        while (0 <= x <= max_x) and (0 <= y <= max_y):
            x += v[0]
            y += v[1]
            if (x, y) in asteroids:
                asteroids_by_vector[v].append((x, y))

    destroy_num = 1
    index = 0
    while destroy_num < 202:
        while not asteroids_by_vector[vectors[index]]:
            index = (index + 1) % len(vectors)
        destroyed = asteroids_by_vector[vectors[index]].pop(0)

        print(f"{destroy_num:00d}: {destroyed}")
        destroy_num += 1
        index = (index + 1) % len(vectors)


def get_vectors(origin, asteroids):
    vectors = set()
    others = [a_ for a_ in asteroids if a_ != origin]
    xa = origin[0]
    ya = origin[1]
    to_check = others[:]
    can_see = set()
    for a_ in to_check:
        dx, dy = a_[0] - xa, a_[1] - ya
        g = gcd(dx, dy)
        dx, dy = dx // g, dy // g
        vectors.add((dx, dy))
    return vectors


def setup(filename):
    asteroids = []
    with open(filename) as f:
        for y, row in enumerate(f.readlines()):
            for x, space in enumerate(row.strip()):
                if space == "#":
                    asteroids.append((x, y))
    return asteroids


if __name__ == "__main__":
    main()
