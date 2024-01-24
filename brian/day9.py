from AdventUtils import *
import AdventUtils
AdventUtils.current_year = 2023

def decipher(line):
    nums=[]
    nums.append([int(d) for d in line.split(' ')])
    print(nums)
    while not all(x==0 for x in nums[-1]):
        diff = [nums[-1][i]-nums[-1][i-1] for i in range(1, len(nums[-1]))]
        print(diff)
        nums.append(diff)

    s = 0
    for i in range(len(nums)-2, -1, -1):
        s += nums[i][-1]
        print(s)
    return s


def mirage(input):
    return sum(decipher(line) for line in input)
        

in9 = parse(9, show=0)
#print(answer(9.1, 0, lambda: mirage(in9)))

from collections import deque

def decipher2(line):
    nums=[]
    nums.append(deque(int(d) for d in line.split(' ')))
    print(nums)
    while not all(x==0 for x in nums[-1]):
        diff = deque(nums[-1][i]-nums[-1][i-1] for i in range(1, len(nums[-1])))
        print(diff)
        nums.append(diff)

    s = 0
    for i in range(len(nums)-2, -1, -1):
        nums[i+1].appendleft(s)
        s = nums[i][0] - nums[i+1][0]

        print(s)

    return s


def mirage2(input):
    return sum(decipher2(line) for line in input)


print(answer(9.2, 1097, lambda: mirage2(in9)))


