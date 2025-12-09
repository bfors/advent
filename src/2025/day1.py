# Part 1
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

        # print(f"{d}{amt} -> {num}")

    # print(f"\nPassword: {zeros}")


# Part 2
with open("inputs/2025/input1.txt", "r") as f:
    num = 50
    zeros = 0

    for line in f:
        d = line[0]
        amt = int(line[1:-1])

        if d == "L":
            # Count crossings: position 0 appears at intervals of 100 clicks
            # Starting at 0 doesn't count, but landing on 0 does
            if num == 0:
                zeros_crossed = amt // 100
            else:
                # First crossing after 'num' clicks, then every 100 clicks
                zeros_crossed = max(0, (amt - num) // 100 + 1)
            num = (num - amt) % 100
        elif d == "R":
            # Count how many multiples of 100 we pass: 100, 200, 300, ...
            zeros_crossed = (amt + num) // 100
            num = (num + amt) % 100

        zeros += zeros_crossed
        # print(f"{d}{amt} -> {num} (crossed {zeros_crossed} times)")

    print(f"Password: {zeros}")
