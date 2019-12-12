import sys
import re
from collections import defaultdict, deque, namedtuple

Vec = namedtuple("Vec", ["x", "y", "z"])
Moon = namedtuple("Moon", ["pos", "vel"])
MAX_STEPS = 1000


def main():
    global MAX_STEPS

    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = "12-input.txt"
    moons = setup(input_file)

    step = 0
    print(f"After {step} steps:")
    for m in moons:
        print(m)
    while step <= MAX_STEPS:
        step += 1
        moons = gravity(moons)
        moons = velocity(moons)
        energy = [pe(m) * ke(m) for m in moons]
        print(f"After {step} steps:")
        for m in moons:
            print(m)
        print(f"Energy of each moon: {energy}, total: {sum(energy)}")

        print()


def pe(moon):
    p = abs(moon.pos.x) + abs(moon.pos.y) + abs(moon.pos.z)
    return p


def ke(moon):
    return abs(moon.vel.x) + abs(moon.vel.y) + abs(moon.vel.z)


def gravity(moons):
    new_moons = []
    for m in moons:
        v_x, v_y, v_z = m.vel
        for other_m in moons:
            v_x += sign(other_m.pos.x - m.pos.x)
            v_y += sign(other_m.pos.y - m.pos.y)
            v_z += sign(other_m.pos.z - m.pos.z)
        new_moons.append(Moon(m.pos, Vec(v_x, v_y, v_z)))
    return new_moons


def velocity(moons):
    new_moons = []
    for m in moons:
        new_pos = Vec(m.pos.x + m.vel.x, m.pos.y + m.vel.y, m.pos.z + m.vel.z)
        new_moons.append(Moon(new_pos, m.vel))
    return new_moons


def sign(i):
    if i < 0:
        return -1
    elif i == 0:
        return 0
    elif i > 0:
        return 1
    else:
        raise ValueError


def setup(filename):
    reg = re.compile("-?\d+")
    moons = []
    with open(filename) as f:
        for line in f.readlines():
            m_s = reg.findall(line)
            m_pos = Vec(int(m_s[0]), int(m_s[1]), int(m_s[2]))
            moons.append(Moon(m_pos, Vec(0, 0, 0)))
    return moons


if __name__ == "__main__":
    main()
