import sys
from collections import defaultdict, deque


def main():

    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = "06-input.txt"
    orbits = load_universe(input_file)

    orbit_map = get_orbit_map(orbits)
    orbits_for_objects = get_orbits_for_objects(orbit_map)

    print(f"Total num of orbits: {sum(orbits_for_objects.values())}")


def get_orbit_map(orbits):
    orbit_map = defaultdict(list)
    for orbit in orbits:
        orbit_map[orbit[0]].append(orbit[1])
    return orbit_map


def get_orbits_for_objects(orbit_map):
    num_orbits = {}

    suns = [thing for thing in orbit_map.keys() if thing not in orbit_map.values()]
    to_calc_for = deque()
    for sun in suns:
        to_calc_for.append(sun)
        num_orbits[sun] = 0
    while to_calc_for:
        planet = to_calc_for.popleft()
        moons = orbit_map[planet]
        for moon in moons:
            num_orbits[moon] = num_orbits[planet] + 1
            to_calc_for.append(moon)
    return num_orbits


def load_universe(filename):
    orbits = []
    with open(filename) as f:
        for line in f.readlines():
            earth, moon = line.strip().split(")")
            orbits.append((earth, moon))
    return orbits


if __name__ == "__main__":
    main()
