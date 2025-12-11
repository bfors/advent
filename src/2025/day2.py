import math

dif = 0 + 150

num = 0
amt = 100
orig = num
dif = num - amt
zs = int(math.fabs(math.floor(dif / 100)))

num = (num - amt) % 100
if num == 0:
    zs += 1

if orig == 0:
    zs -= 1


print(f"{orig} - {amt} -> {num}")
print(zs)
