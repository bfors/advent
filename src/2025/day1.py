with open("inputs/2025/input1.txt", "r") as f:
    num = 50
    zeros = 0

    for line in f:
        d = line[0]
        amt = int(line[1:-1])

        if d == "L":
            num = (num - amt) % 100
        elif d == "R":
            num = (num + amt) % 100

        if num == 0:
            zeros += 1

        print(f"{d}{amt} -> {num}")

    print(f"\nPassword: {zeros}")
