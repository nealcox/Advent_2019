def main():
    total_fuel = 0

    with open("01-input.txt") as f:
        modules = [int(module.strip()) for module in f.readlines()]

    to_calculate_fuel_for = modules
    while to_calculate_fuel_for:
        next_fuels = []
        for module in to_calculate_fuel_for:
            fuel = fuel_for_module(module)
            total_fuel += fuel
            if fuel > 0:
                next_fuels.append(fuel)
            to_calculate_fuel_for = next_fuels
    print(total_fuel)


def fuel_for_module(mass):
    return max(int(mass // 3) - 2, 0)


if __name__ == "__main__":
    main()
