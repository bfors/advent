text = None
with open("inputs/2025/input2.txt", "r") as f:
    text = f.read()


for num in text.split(","):
    print(num)
