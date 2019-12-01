def main():
    total_fuel = 0
    with open("01-input.txt") as f:
        for module in f.readlines():
            total_fuel += fuel_for_module(int(module.strip()))
    print(total_fuel)


def fuel_for_module(mass):
    return int(mass // 3) - 2


assert fuel_for_module(12) == 2
assert fuel_for_module(100756) == 33583
if __name__ == "__main__":
    main()
