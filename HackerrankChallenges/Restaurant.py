import math


def restaurant(l, b):
    a = 1
    m = max(l, b)
    for i in range(m, 0, -1):
        if l % i == 0 and b % i == 0:
            a = i
            return int((l*b) / math.pow(a, 2))


t = int(input())

for t_itr in range(t):
    lb = input().split()
    l = int(lb[0])
    b = int(lb[1])
    result = restaurant(l, b)
    print(result)
