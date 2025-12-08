with open("inputs/2025/input1.txt", "r") as f:
    num = 50
    zeros = 0
    print("start")
    print(num)
    i = 0
    for line in f:
        i += 1
        d = line[0]
        amt = int(line[1:-1])

        if d == "L":
            num -= amt

            if num < 0:
                num %= -100
                num = 100 + num

        if d == "R":
            num += amt
            num %= 100

        if num == 0:
            zeros += 1
        print(f"{d}:{amt}   num: {num}")
    print(f"lines: {i}")
    print(zeros)
