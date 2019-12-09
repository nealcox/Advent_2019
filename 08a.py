import sys
from collections import Counter


def main():
    width = 25
    height = 6

    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        width = int(sys.argv[2])
        height = int(sys.argv[3])
    else:
        input_file = "08-input.txt"
    digits = get_digits(input_file)

    layer = 0
    across = 0
    down = 0
    num_per_layer = width * height
    decoded = []

    for i in range(len(digits)):
        if i % num_per_layer == 0:
            decoded.append([])
        #        if i % width == 0:
        #            decoded[-1].append([])
        #        decoded[-1][-1].append(digits[i])
        decoded[-1].append(digits[i])

    layer_min_0s = 0
    min_0s = float("inf")
    for i, l in enumerate(decoded):
        c = Counter(l)
        num_0s = c["0"]
        if num_0s < min_0s:
            min_0s = num_0s
            layer_min_0s = i
            print(f"{i}: l: num 0s {c['0']}")
            print(f"Num 1s = {c['1']}, Num 2s = {c['2']}, product = {c['1']*c['2']}")


def get_digits(filename):
    with open(filename) as f:
        digits = f.read().strip()
    return digits


if __name__ == "__main__":
    main()
