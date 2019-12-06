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

    routes_for_objects = get_routes_for_objects(orbit_map)
    you_route = routes_for_objects['YOU']
    san_route = routes_for_objects['SAN']

    num_common_objects = 0
    while you_route[num_common_objects] == san_route[num_common_objects]:
        num_common_objects += 1
    print(f"Length 'YOU' {len(you_route)}")
    print(f"Length 'SAN' {len(san_route)}")
    print(f"num_common_objects {num_common_objects}")
    moves_to_last_common_object = len(you_route) - num_common_objects
    print(f"moves_to_last_common_object {moves_to_last_common_object}")
    from_last_common_object_to_SAN = len(san_route) - num_common_objects
    print(f"from_last_common_object_to_SAN {from_last_common_object_to_SAN}")
    min_moves = moves_to_last_common_object + from_last_common_object_to_SAN
    print(f"Minimum number of moves: {min_moves}")




def get_orbit_map(orbits):
    orbit_map = defaultdict(list)
    for orbit in orbits:
        orbit_map[orbit[0]].append(orbit[1])
    return orbit_map


def get_routes_for_objects(orbit_map):
    routes = {}

    suns = [thing for thing in orbit_map.keys() if thing not in orbit_map.values()]
    to_calc_for = deque()
    for sun in suns:
        to_calc_for.append(sun)
        routes[sun] = []
    while to_calc_for:
        planet = to_calc_for.popleft()
        moons = orbit_map[planet]
        for moon in moons:
            routes[moon] = routes[planet][:] 
            routes[moon].append(planet)
            to_calc_for.append(moon)
    return routes

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
