import sys
import re
from collections import defaultdict, deque, namedtuple
from copy import deepcopy

Vec = namedtuple("Vec", ["x", "y", "z"])
Moon = namedtuple("Moon", ["pos", "vel"])
MAX_STEPS = 3000000000


def main():
    global MAX_STEPS

    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = "12-input.txt"
    moons = setup(input_file)

    initial = deepcopy(moons)
    initial_x = [(m.pos.x,m.vel.x) for m in moons]
    initial_y = [(m.pos.y,m.vel.y) for m in moons]
    initial_z = [(m.pos.z,m.vel.z) for m in moons]
    x_found = False
    y_found = False
    z_found = False

    step = 0
    print(f"After {step} steps:")
    for m in moons:
        print(m)
    while step <= MAX_STEPS:
        step += 1
        moons = gravity(moons)
        moons = velocity(moons)
#        print(f"After {step} steps:")
#        for m in moons:
#            print(m)
#        print()
        x_s = [(m.pos.x,m.vel.x) for m in moons]
        y_s = [(m.pos.y,m.vel.y) for m in moons]
        z_s = [(m.pos.z,m.vel.z) for m in moons]
        if not x_found and x_s == initial_x:
            x_found = True
            x_cycle = step
            print(f"x cycles after {step} steps.")
        if not y_found and y_s == initial_y:
            y_found = True
            y_cycle = step
            print(f"y cycles after {step} steps.")
        if not z_found and z_s == initial_z:
            z_found = True
            z_cycle = step
            print(f"z cycles after {step} steps.")
        if x_found and y_found and z_found:
            print(f"All cycles found")
            g = gcd(x_cycle,y_cycle)
            lcm_xy = x_cycle * y_cycle //g
            g = gcd(lcm_xy,z_cycle)
            lcm_xyz = lcm_xy * z_cycle //g
            print(f"System cycles after {lcm_xyz} steps.")
            break
        if moons == initial:
            print(f"Back to starting position after {step} steps.")
            break


def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)


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
