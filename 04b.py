lower = 240920
upper = 789857

possibles = 0
for test_num in range(lower, upper + 1):
    test = str(test_num)

    double_digit = set()
    triple_digit = set()
    increase_found = False
    for i in range(len(test) - 1):
        if test[i] == test[i + 1]:
            double_digit = double_digit | {i, i + 1}
            if (i < len(test) - 2) and (test[i] == test[i + 2]):
                triple_digit = triple_digit | {i, i + 1, i + 2}
        if test[i] > test[i + 1]:
            increase_found = True
    if double_digit and len(double_digit - triple_digit) > 0 and not increase_found:
        print(test_num)
        possibles += 1
print(possibles)
