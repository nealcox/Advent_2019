lower = 240920
upper = 789857

possibles = 0
for test_num in range(lower, upper + 1):
    test = str(test_num)

    double_digit = False
    increase_found = False
    for i in range(len(test) - 1):
        if test[i] == test[i + 1]:
            double_digit = True
        if test[i] > test[i + 1]:
            increase_found = True
    if double_digit and not increase_found:
        print(test_num)
        possibles += 1
print(possibles)
